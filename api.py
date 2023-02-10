import json
import fitz

class pdfAPI():

    def parse_pdf_title(self, filename: str) -> dict:
        doc = fitz.open(filename)
        print ("number of pages: %i" % doc.pageCount)

        for i in range(doc.pageCount):
            content = doc.loadPage(i).getText('text').split('\n')
            for text in content:
                text = text.replace(' ', '')
                if len(text) != 0:
                    return {'title': text}

        return {'title': ''}


    def parse_pdf_article(self, filename: str, title : str) -> dict:
        
        doc = fitz.open(filename)
        print ("number of pages: %i" % doc.pageCount)

        data = {'article': ''}

        for i in range(doc.pageCount):
            content = doc.loadPage(i).getText('text').replace(' ', '').replace('·', '').split('\n')
            for text in content:
                if len(text) >= 20:
                    data['article'] += text

        data['article'] = data['article'].replace(title, '', 1)
        return data

    def __call__(self, filename: str) -> dict:

        data = self.parse_pdf_title(f'{filename}.pdf')
        data.update(self.parse_pdf_article(f'{filename}.pdf', data['title']))

        return data



if __name__ == '__main__':

    api = pdfAPI()
    data = api('茶葉知識文獻拷貝')

    outputfile = open(f'茶葉知識文獻拷貝_test.json', 'w', encoding='utf-8')
    json.dump(data, outputfile, ensure_ascii=False)