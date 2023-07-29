import requests
import os

class ApiConnector:
    def __init__(self) -> None:
        self.headers = {"Content-Type": "application/json"}
        self.url = 'https://invoice-generator.com'
        self.invoices_directory = f"{os.path.dirname(os.path.abspath(__file__))}/{'invoices'}"

    def connect_to_api_and_save_invoice_pdf(self, from_who,to_who,logo,number,date,due_date,items,notes,terms,tax,discounts) -> None:
        invoice_parsed = {
            'from': from_who,
            'to': to_who,
            'logo': logo,
            'number': number,
            'currency': 'EUR',
            'date': date,
            'due_date': due_date,
            'items': items,
            'fields':{"tax":"%","discounts": "%","shipping": False} ,
            'discounts': discounts,
            'tax': tax,
            'notes': notes,
            'terms': terms
        }
   
        r = requests.post(self.url, json=invoice_parsed, headers=self.headers)
        if r.status_code == 200 or r.status_code == 201:
            pdf = r.content
            self.save_invoice_to_pdf(pdf, number)
            nombre = f"{number}_invoice.pdf"
            root = f"invoices/{nombre}"

        else:
            print("Fail :", r.text)
            
        return root

    def save_invoice_to_pdf(self, pdf_content: str, invoice_number) -> None:
        invoice_name = f"{invoice_number}_invoice.pdf"
        invoice_path = f"{self.invoices_directory}/{invoice_name}"
        with open(invoice_path, 'wb') as f:
            f.write(pdf_content)