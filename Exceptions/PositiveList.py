class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, p_object):
        if p_object <= 0:
            raise NonPositiveError(p_object)
        else:
            super(PositiveList, self).append(p_object)
