import logging


DEFAULT_TABLE_X_SIZE = 30


class BadDataStructure(Exception):
    pass


class NoDataForTable(Exception):
    pass


class TGTable(object):
    """ Table for telegram chat init from python lists, arrays and dicts

        :param dict data: Dictionary with data to build
        :param bool build_on_init: Creating table when table.__init__() *(optional)*
        :param bool slim: Trims the size of the table columns to the minimum required size
            CURRENTLY DEPRECATED
            *(optional)*
        :param aiogram.types.markdown md: automatically apply telegram markdownto the table
    """

    def __str__(self):
        if self.table:
            return self.__repr__()
        return f"{self.__class__} {hex(self.__hash__())}"

    def __repr__(self):
        return self.table

    def __add__(self, other):
        return other + self.table

    def __init__(self, data, md=None, build_on_init=True, slim=True, **kwargs):
        self.x_table_size = DEFAULT_TABLE_X_SIZE
        self.columns_num = 1
        self.x_row_size = 1
        self.x_cell_size = lambda: (self.x_table_size - 1) // self.columns_num

        self.x_sep = '|'
        self.y_sep = '-'
        self.y_sep_bold = '='
        self.space = ' '

        self.none_symbols = (self.x_sep, self.y_sep, self.y_sep_bold, self.space)

        self.table = str()
        self.data = data
        self.md = md
        self.slim = slim

        self.empty_row_bold = self._get_empty_row(separate=self.y_sep_bold)

        if build_on_init:
            self.build()

    def _to_cell(self, value=None):
        if not value:
            value = self._get_empty_cell()
        if isinstance(value, float):
            if not (value % 1):
                value = "%i" % int(value)
            else:
                value = "%f" % value

        if self.slim:
            if len(value) > self.x_cell_size():
                value = value[0:self.x_cell_size()]
        _diff = 0
        if len(value) < self.x_cell_size():
            _diff = self.x_cell_size() - len(value)

        value = str(value)
        for i in range(_diff):
            value += self.space
        return value

    def _to_row(self, *values):
        row = str()
        for cell in range(self.columns_num):
            try:
                row += self._to_cell(values[cell]) + self.x_sep
            except IndexError:
                row += self._get_empty_cell() + self.x_sep
        return row[0:-1]

    def _get_empty_cell(self, fill=None):
        if not fill:
            fill = self.space
        empty_cell = ''
        for symbol in range(self.x_cell_size()):
            empty_cell += fill
        return empty_cell

    def _get_empty_row(self, separate=None):
        empty_row = ''
        for cell in range(self.columns_num):
            empty_row += self._get_empty_cell(fill=separate)
        return empty_row

    def _concat_rows_to_text(self, *rows):
        concated_rows = str()
        for row in rows:
            concated_rows += row + '\n'
        return concated_rows

    def slim_rows(self, rows):
        slised_rows = rows

        for i in range(self.x_table_size-1):
            current_symbol_set = set(self.none_symbols)
            for row in rows:
                current_symbol_set.add(row[i])
            if current_symbol_set == set(self.none_symbols):
                print("Column can be cuted")

        return slised_rows

    def build(self):
        head_data = self.data.get('head')
        body_data = self.data.get('body')

        try:
            assert body_data or head_data
        except AssertionError:
            raise BadDataStructure
        table_array = []
        max_body_row_len = max(len(i) for i in body_data)

        if head_data:
            assert len(head_data) >= max_body_row_len
            self.columns_num = len(head_data)
            head_text = self._to_row(*head_data)
            table_array += [head_text, self.empty_row_bold]
        else:
            self.columns_num = max_body_row_len
            head_text = self.empty_row_bold
            table_array += [head_text]

        if body_data:
            body_rows_array = list()
            for row_value in body_data:
                body_rows_array.append(self._to_row(*row_value))
        else:
            body_rows_array = [self.empty_row_bold]

        table_array += [*body_rows_array]

        # if self.slim:
        #     table_array = self.slim_rows(table_array)

        self.table = self._concat_rows_to_text(*table_array)

        if self.md:
            self.table = self.md(self.table)
