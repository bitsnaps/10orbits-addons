from openerp import models, fields, api
from datetime import date

class Product(models.Model):
    _inherit = 'product.template'

    minimum_qty = fields.Integer(string='Minimum Quantity', default=100,
                                          help='When stock on hand falls below this number, it will be included in the low stock report. Set to -1 to exclude from the report.')

    def send_low_stock_via_email(self):
        header_label_list = ["Internal Refrence", "Name", "Qty On Hand", "Low Stock Qty"]
        product_obj  = self.env['product.product']
        product_ids  = product_obj.search([])
        product_ids = product_ids.filtered(lambda r: r.qty_available <= r.minimum_qty and r.minimum_qty >= 0)
        print('sdjfhssdf', product_ids)
        group = self.env.ref('stock.group_stock_manager')
        print(group)
        recipients = []
        for recipient in group.users:
            recipients.append((4, recipient.partner_id.id))
        # Notification message body
        body = """  
        <table class="table table-bordered">
            <tr style="font-size:14px; border: 1px solid black">
                <th style="text-align:center; border: 1px solid black">%s</th>
                <th style="text-align:center; border: 1px solid black">%s</th>
                <th style="text-align:center; border: 1px solid black">%s</th>
                <th style="text-align:center; border: 1px solid black">%s</th>
                </tr>
             """ %(header_label_list[0], header_label_list[1], header_label_list[2], header_label_list[3])
        for product_ids in product_ids:
            body += """ 
                <tr style="font-size:14px; border: 1px solid black">
                    <td style="text-align:center; border: 1px solid black">%s</td>
                    <td style="text-align:center; border: 1px solid black">%s</td>
                    <td style="text-align:center; border: 1px solid black">%s</td>
                    <td style="text-align:center; border: 1px solid black">%s</td>
                </tr>
                """ %(product_ids.default_code, product_ids.name, product_ids.qty_available, product_ids.minimum_qty)
            "</table>"
        post_vars = {'subject': "Low stock notification",
            'body': body,
            'partner_ids': recipients,}
        self.message_post(
            type="notification",
            subtype="mt_comment",
            **post_vars)