from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        #logo
        self.set_line_width(1)
        self.set_draw_color(15,80,160)
        self.line(10,6,200,6)
        
        self.image('logo-palmeiras.png',10,8,95)
        #fonte
        self.set_font('helvetica','',12)
        #titulo
        #self.cell width, heitgh
        self.set_text_color(108,117,125)
        self.cell(100)
        self.cell(0, 6, 'City, State, Country', ln=1)
        self.cell(100)
        self.cell(0, 6, '+XX(XX) XXXXX-XXXX', ln=1)
        self.cell(100)
        self.cell(0, 6, 'www.XXXXXXXXXXXXXX.com', ln=1)
        self.cell(100)
        self.cell(0, 6, 'contactto@example.com', ln=1)
        self.line(10,35,200,35)
        # Line break
        self.ln(10)
        
    def intro(self,texto):
        self.set_font('helvetica','B',14)
        
        self.cell(0,6,'Objetivo',align='C')
        self.ln(10)
        self.set_font('helvetica','',12)
        self.multi_cell(0,5,texto)
        self.ln(10)
    
    def consumo(self,texto,consumo):
        self.set_font('helvetica','B',14)
        
        self.cell(0,6,'Análise básica de consumo',align='C')
        self.ln(10)
        self.set_font('helvetica','',12)
        self.multi_cell(0,5,texto)
        self.ln(10)
        spacing=2
        # data = consumo
        #col_width = self.w / 4.5
        #row_height = self.font_size
        #for row in data:
        #    self.cell(col_width/2)
        #    for item in row:                
        #        self.cell(col_width, row_height*spacing,
        #                 txt=str(item), border=1,align='C')
        #    self.ln(row_height*spacing)
        self.ln(10)
        self.image('consumo.png',w=180)
        
        
    def tarifas(self,texto):
        spacing=2
        data = [['Faixa de consumo m³','Valor da tarifa R$'],
               ['1-7','2,99/2,99'],
               ['8-13','3,59/3,59'],
               ['14-20','7,10/7,10'],
               ['21-30','10,66/10,66'],
               ['31-45','17,05/17,05'],
                ['46-9999','23,87/23,87']
               ]
        self.set_font('helvetica','B',14)
        
        self.cell(0,6,'Faixas de tarifação',align='C')
        self.ln(10)
        self.set_font('helvetica','',12)
        self.multi_cell(0,5,texto)
        self.ln(10)
        ## Tabela de tarifas da CAESB
        col_width = self.w / 4.5
        row_height = self.font_size
        for row in data:
            self.cell(col_width)
            for item in row:                
                self.cell(col_width, row_height*spacing,
                         txt=item, border=1,align='C')
            self.ln(row_height*spacing)
        self.ln(10)
        self.cell(col_width/2)
        self.image('plot1.png',w=140)
        
    def grafico(self,image):
        self.image(image,60,200,120)
        
            

## Setting pdf 

#pdf.grafico('plot1.png')
## célula 2
#pdf.cell(120,110,'aksjdf alkdjf aklsdj fkasdsjf alksfj aklsdjf klasdfj ',ln=True,border=True)