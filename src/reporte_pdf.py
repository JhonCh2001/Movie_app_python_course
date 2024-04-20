from fpdf import FPDF
import base64

class PDFWithBackground(FPDF):
    def __init__(self):
        super().__init__()
        self.background = None
 
    def set_background(self, image_path):
        self.background = image_path
 
    def add_page(self, orientation=''):
        super().add_page(orientation)
        if self.background:
            self.image(self.background, 0, 0, self.w, self.h)
 
    def footer(self):
        # Posición a 1.5 cm desde el fondo
        self.set_y(-15)
        # Configurar la fuente para el pie de página
        self.set_font('Arial', 'I', 8)
        # Número de página
        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'C')

def crear_reporte(year):
    pdf = PDFWithBackground()
    pdf.set_background('Images/background.png')

    pdf.add_page()

    pdf.set_y(100)
    pdf.set_font('Courier', style = 'B', size = 57)
    pdf.cell(0,0,'Reporte',0,1,'C')

    pdf.set_y(125)
    pdf.set_font('Courier', style = 'B', size = 57)
    pdf.cell(0,0,'automático en',0,1,'C')

    pdf.set_y(150)
    pdf.set_font('Courier', style = 'B', size = 57)
    pdf.cell(0,0,'Python',0,1,'C')

    pdf.set_y(170)
    pdf.set_font('Courier', size = 27)
    pdf.cell(0,0,'Curso de Python',0,1,'C')

    pdf.set_y(180)
    pdf.set_font('Courier', size = 17)
    pdf.cell(0,0,'Desde aspectos básicos hasta aplciaciones analíticas.',0,1,'C')

    pdf.add_page()

    pdf.set_y(45)
    pdf.set_font('Courier',style = 'B', size = 27) # Vienen por defecto, Arial, Times, Courier
    pdf.cell(0,0,'Mi primer reporte',0,1,'R')

    pdf.set_y(54)
    pdf.set_font('Courier', size = 14) # Vienen por defecto, Arial, Times, Courier
    pdf.cell(0,0,'Desarrollado con python :D',0,1,'R')

    pdf.set_y(75)
    pdf.set_font('Courier',size = 20) # Vienen por defecto, Arial, Times, Courier
    pdf.cell(0,0,'reporte general por anios y edades permitidas',0,1,'R')

    imagen = 'visualization.png'

    pdf.image(f'Images/{imagen}',x=15,y=83,w=190,h=65)

    pdf.set_y(155)
    pdf.set_font('Courier',size=15)
    pdf.multi_cell(190,6,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin lectus lacus, ultricies eu dolor eget, molestie pulvinar turpis. Vestibulum cursus elementum lectus in bibendum. Nam sollicitudin accumsan elit, in condimentum sapien egestas pellentesque. Cras sagittis ornare quam, ut faucibus lorem congue in. Nullam sit amet tristique diam. Praesent ultrices fringilla.',0,1,'L')

    pdf.add_page()

    pdf.set_y(45)
    pdf.set_font('Courier', style = 'B', size = 23) # Vienen por defecto, Arial, Times, Courier
    pdf.cell(0,0,f'Reporte del año {year}',0,1,'R')

    pdf.image(f'Images/donut_platform_year_{year}.png',x=15,y=63,w=90,h=90)
    pdf.image(f'Images/histogram_age_year_{year}.png',x=15,y=143,w=90,h=65)

    pdf.set_y(103)
    pdf.set_font('Courier', style = 'B', size = 13) # Vienen por defecto, Arial, Times, Courier
    pdf.cell(0,0,f'Películas por plataforma {year}',0,1,'R')

    pdf.set_y(178)
    pdf.set_font('Courier', style = 'B', size = 13) # Vienen por defecto, Arial, Times, Courier
    pdf.cell(0,0,f'Edades permitidas por película {year}',0,1,'R')

    return pdf

def create_download_link(val, filename):
    b64 = base64.b64encode(val)
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Descargar reporte en PDF</a>'