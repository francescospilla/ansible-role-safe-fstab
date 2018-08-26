from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError, AnsibleFilterError


def split(string, separator=' '):
    try:
        return [s for s in string.split(separator) if s]
    except Exception as e:
        raise AnsibleFilterError('Error in split in split filter plugin:\n{0}'.format(e), orig_exec=e)


class FilterModule(object):
    ''' A filter to split a string into a list. '''

    def filters(self):
        return {
            'split': split
}
