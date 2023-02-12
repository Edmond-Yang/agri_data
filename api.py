import json
import fitz

class pdfAPI():

    def parse_pdf_title(self, file) -> dict:
        doc = fitz.open(stream = file, filetype="pdf")

        for i in range(doc.pageCount):
            content = doc.loadPage(i).getText('text').split('\n')
            for text in content:
                text = text.replace(' ', '')
                if len(text) != 0:
                    return {'標題': text}

        return {'標題': ''}


    def parse_pdf_article(self, file, title : str) -> dict:
        
        doc = fitz.open(stream=file, filetype="pdf")

        data = {'全文': ''}

        for i in range(doc.pageCount):
            content = doc.loadPage(i).getText('text').replace(' ', '').replace('·', '').split('\n')
            for text in content:
                if len(text) >= 20:
                    data['全文'] += text

        data['全文'] = data['全文'].replace(title, '', 1)
        return data

    def __call__(self, file) -> dict:

        data = self.parse_pdf_title(file)
        data.update(self.parse_pdf_article(file, data['標題']))
        return data



if __name__ == '__main__':

    api = pdfAPI()
    data = api('茶葉知識文獻拷貝')

    outputfile = open(f'茶葉知識文獻拷貝_test.json', 'w', encoding='utf-8')
    json.dump(data, outputfile, ensure_ascii=False)