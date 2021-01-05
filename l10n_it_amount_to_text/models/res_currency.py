# Copyright 2020 Sergio Zanchetta (Associazione PNLUG - Gruppo Odoo)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models

CURRENCY_NAME = {"Dollars": "dollari", "Euros": "euro", "Cents": "centesimi"}

class Currency(models.Model):
    _inherit = "res.currency"

    def _convert_currency_name_hook(self, label):
        """Hook to add currency translation."""
        return CURRENCY_NAME[label]

    def amount_to_text(self, amount):
        if not self.currency_unit_label:
            self.currency_unit_label = self._convert_currency_name_hook(self.currency_unit_label)
        if not self.currency_unit_label:
            self.currency_subunit_label = self._convert_currency_name_hook(self.currency_subunit_label)

        return super(Currency, self).amount_to_text(amount)
