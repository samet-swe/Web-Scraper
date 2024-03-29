from fpdf import FPDF, XPos, YPos
from fpdf.enums import XPos, YPos

import scraper

title = 'My Book List'

class PDF(FPDF):
    def header(self):
        # font
        self.set_font('helvetica', 'BU', 15)
        
        # Calculate width of title and position to center title
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w-title_w) / 2)
        
        # Thickness of frame (border)
        self.set_line_width(1)
        
        # Title
        self.cell(title_w, 10, title, new_x = XPos.LMARGIN, new_y = YPos.NEXT, align = 'C')
        
        # Padding
        self.cell(20)
        
        # line break
        self.ln(10)

    def footer(self):
        # Set position of the footer (negative number is from bottom, positive number from top)
        self.set_y(-15)
        
        # Set font
        self.set_font('helvetica', 'I', 8)
        
        # Set font color grey
        self.set_text_color(169, 169, 169)
        
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align = 'C')
            
    # List content
    def list_body(self, bl):
        # Set font
        self.set_font('times', '', 12)
        
        for book in bl:
            if book[2] == 'One':
                txt = f'The book --{book[0]}-- costs ${book[1]} and has a rating of {book[2]} star.'
            else:
                txt = f'The book --{book[0]}-- costs ${book[1]} and has a rating of {book[2]} stars.'
        
            # Insert text
            self.cell(0,5, txt, markdown = True)
            self.ln()
        
        # End of List
        self.set_font('times', 'I', 12)
        self.cell(0,5, 'END OF LIST', new_x = XPos.LMARGIN, new_y = YPos.NEXT)
        
    def print_list(self, bl):
        self.add_page()
        self.list_body(bl)
        
def main(books):
    pdf = PDF()

    # metadata
    pdf.set_title(title)
    pdf.set_author('Me')

    # get total page number
    pdf.alias_nb_pages()

    # Set auto page break
    pdf.set_auto_page_break(auto=True, margin = 15)

    pdf.print_list(books)

    pdf.output('Book List.pdf')

if __name__ == '__main__':
    scraper.main()



