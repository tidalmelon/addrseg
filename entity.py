# -*- coding: utf-8 -*-

import os

class Company(object):
    """Represents a record."""

    Fields = dict(cname='cn', contacts='con', email='em', site='st', address='add', owner='own', reg_capital='rcap',
                reg_status='rsta', reg_time='rtim', reg_num='rno', reg_institute='rin', reg_location='rl', score='sc',
                industry='isty', org_type='ot', org_num='on', credit_code='crec', from_time='ft', approved_time='at',
                busi_scope='scp', staff='stf', invest='inv', addressseg='adt')

    def __str__(self):
        line = ''
        for name in self.Fields:
            if hasattr(self, name):
                val = getattr(self, name)
                val = val if val else ''
                line += name + ': ' + val + os.linesep
            else:
                line += name + ': ' + os.linesep
        line = line.strip()
        return line.encode('utf-8')

