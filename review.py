# -*- coding: utf-8 -*-
"""
    review

    Nereid Reviews

    :copyright: (c) 2012 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.model import ModelSQL, ModelView, fields


class NereidReview(ModelSQL, ModelView):
    """
    Nereid Review
    """
    _name = "nereid.review"
    _description = __doc__
    _rec_name = 'title'

    title = fields.Char('Title')
    rating = fields.Integer('Rating(On a scale of 1-5)')
    comment = fields.Text('Comment')
    nereid_user = fields.Many2One('nereid.user', 'Nereid User')
    party = fields.Function(fields.Many2One(
        'party.party', 'Party'
    ), 'get_party')

    def get_party(self, ids, name):
        res = {}
        for review in self.browse(ids):
            if review.nereid_user:
                res[review.id] = review.nereid_user.party.id
        return res

NereidReview()
