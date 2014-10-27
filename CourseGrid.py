import sys
import os
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *
import math as m
import random as r

class ClickableLabel(QLabel):
    def __init__(self, parent=None):
        super(ClickableLabel, self).__init__(parent)

    def mouseReleaseEvent(self,event):
        self.emit(SIGNAL("clicked()"))

class RahaMuunnin(QDialog):    

    def __init__(self, parent=None):
        super(RahaMuunnin, self).__init__(parent)

        self.setWindowTitle("Markka-euro -laskin")

        hyllystö = QVBoxLayout()
        ylärivi = QHBoxLayout()
        alarivi = QHBoxLayout()

        hyllystö.addSpacing(20)
        hyllystö.addLayout(ylärivi)
        hyllystö.addSpacing(20)
        hyllystö.addLayout(alarivi)
        hyllystö.addSpacing(20)

        euroLabel = QLabel("€")
        markkaLabel = QLabel("mk")

        eurot = QLineEdit()
        markat = QLineEdit()

        markkaMuuttoLinkki = ClickableLabel("<font color=blue>Muuta markoiksi</font>")
        euroMuuttoLinkki = ClickableLabel("<font color=blue>Muuta euroiksi</font>")

        ylärivi.addWidget(eurot)
        alarivi.addWidget(markat)

        ylärivi.addWidget(euroLabel)
        alarivi.addWidget(markkaLabel)

        ylärivi.addSpacing(70)
        alarivi.addSpacing(70)

        ylärivi.addWidget(markkaMuuttoLinkki)
        alarivi.addWidget(euroMuuttoLinkki)

        def markoiksiMuunnos():

            try:            
                väliTulos = (float(eurot.text())*5.94573)
                tulos = round(väliTulos,2)
                markat.setText(str(tulos))
            
            except:
                markat.setText("Error")    

        def euroiksiMuunnos():

            try:            
                väliTulos = (float(markat.text())/5.94573)
                tulos = round(väliTulos,2)
                eurot.setText(str(tulos))
            
            except:
                eurot.setText("Error")

        self.connect(markkaMuuttoLinkki, SIGNAL("clicked()"), markoiksiMuunnos)
        self.connect(euroMuuttoLinkki, SIGNAL("clicked()"), euroiksiMuunnos)

        self.setLayout(hyllystö)

class Laskin(QDialog):    

    def __init__(self, parent=None):
        super(Laskin, self).__init__(parent)

        self.setWindowTitle("Laskin")

        #Painonappien määrittelyt

        plusNappi = QPushButton("+")
        miinusNappi = QPushButton("-")
        kertoNappi = QPushButton("*")
        potenssiNappi = QPushButton("^")
        clearNappi = QPushButton("C")

        #Syötekenttien määrittelyt
        
        kenttä1 = QLineEdit()
        kenttä2 = QLineEdit()        

        #Tuloskenttien määrittelyt

        tulosKenttä = QLabel("")

        #Kenttien lukujen asettelu

        tulosKenttä.setAlignment(100)
        kenttä1.setAlignment(100)
        kenttä2.setAlignment(100)

        #Layoutin asetus
        
        hyllystö = QVBoxLayout()
        ylärivi = QHBoxLayout()
        keskirivi = QHBoxLayout()
        alarivi = QHBoxLayout()
        
        hyllystö.addLayout(ylärivi)
        hyllystö.addLayout(keskirivi)
        hyllystö.addLayout(alarivi)

        ylärivi.addWidget(kenttä1)
        ylärivi.addWidget(kenttä2)


        #Nappien lisäys layoutiin

        keskirivi.addWidget(plusNappi)
        keskirivi.addWidget(miinusNappi)
        keskirivi.addWidget(kertoNappi)
        keskirivi.addWidget(potenssiNappi)
        keskirivi.addWidget(clearNappi)

        alarivi.addWidget(tulosKenttä)

        #Laskutoimitusten funktiot

        def virheTesti(arvo1, arvo2):
            try:
                tulos = float(arvo1)+float(arvo2)
            except:
                tulosKenttä.setText("Error")

        def plusLasku():
            virheTesti(kenttä1.text(), kenttä2.text())
            try:
                tulos = float(kenttä1.text())+(float(kenttä2.text()))
                tulosKenttä.setText(str(tulos))
            except:
                pass
            
        def vähennysLasku():
            virheTesti(kenttä1.text(), kenttä2.text())
            try:
                tulos = float(kenttä1.text())-(float(kenttä2.text()))
                tulosKenttä.setText(str(tulos))
            except:
                pass
        
        def kertoLasku():
            virheTesti(kenttä1.text(), kenttä2.text())
            try:
                tulos = float(kenttä1.text())*(float(kenttä2.text()))
                tulosKenttä.setText(str(tulos))
            except:
                pass

        def potenssiLasku():
            virheTesti(kenttä1.text(), kenttä2.text())
            try:
                tulos = float(kenttä1.text())**(float(kenttä2.text()))
                tulosKenttä.setText(str(tulos))
            except:
                pass

        def tyhjääKaikki():
            tulosKenttä.setText("")
            kenttä1.setText("")
            kenttä2.setText("")
            
        #Signaalit painikkeille
        
        self.connect(plusNappi, SIGNAL("clicked()"), plusLasku)
        self.connect(miinusNappi, SIGNAL("clicked()"), vähennysLasku)
        self.connect(kertoNappi, SIGNAL("clicked()"), kertoLasku)
        self.connect(potenssiNappi, SIGNAL("clicked()"), potenssiLasku)
        self.connect(clearNappi, SIGNAL("clicked()"), tyhjääKaikki)
        
        self.setLayout(hyllystö)

class AsteMuunnin(QDialog):    

    def __init__(self, parent=None):
        super(AsteMuunnin, self).__init__(parent)

        self.setWindowTitle("Astemuunnos")

        hyllystö = QVBoxLayout()
        ylärivi = QHBoxLayout()
        alarivi = QHBoxLayout()

        hyllystö.addLayout(ylärivi)
        hyllystö.addLayout(alarivi)

        celsiusLabel = QLabel("C:")
        farenheitLabel = QLabel("F:")

        celsiusSyöte = QLineEdit()
        farenheitSyöte = QLineEdit()

        farenheitNappi = QPushButton("=>F")
        celsiusNappi = QPushButton("=>C")

        ylärivi.addWidget(celsiusLabel)
        ylärivi.addWidget(celsiusSyöte)
        ylärivi.addWidget(farenheitNappi)

        alarivi.addWidget(farenheitLabel)
        alarivi.addWidget(farenheitSyöte)
        alarivi.addWidget(celsiusNappi)

        def Celsiuksiksi():

            try:            
                väliTulos = (float(farenheitSyöte.text())-32)*5/9
                tulos = round(väliTulos,2)
                celsiusSyöte.setText(str(tulos))
            
            except:
                farenheitSyöte.setText("Error")

        def Farenheiteiksi():
            try:
                väliTulos = float(celsiusSyöte.text())*1.8+32
                tulos = round(väliTulos,2)
                farenheitSyöte.setText(str(tulos))
            except:
                celsiusSyöte.setText("Error")
            
        self.connect(celsiusNappi, SIGNAL("clicked()"), Celsiuksiksi)
        self.connect(farenheitNappi, SIGNAL("clicked()"), Farenheiteiksi)
        

        self.setLayout(hyllystö)

class PalkkaLaskuri(QDialog):    

    def __init__(self, parent=None):
        super(PalkkaLaskuri, self).__init__(parent)

        self.setWindowTitle("Palkkalaskuri")

        #Layoutin asetus
        
        hyllystö = QVBoxLayout()
        ekarivi = QHBoxLayout()
        tokarivi = QHBoxLayout()
        kolmasrivi = QHBoxLayout()
        neljäsrivi = QHBoxLayout()
        viidesrivi = QHBoxLayout()
        kuudesrivi = QHBoxLayout()
        seitsemäsrivi = QHBoxLayout()
        kahdeksasrivi = QHBoxLayout()
        yhdeksäsrivi = QHBoxLayout()

        hyllystö.addSpacing(20)
        hyllystö.addLayout(ekarivi)
        hyllystö.addSpacing(20)
        hyllystö.addLayout(tokarivi)
        hyllystö.addSpacing(20)
        hyllystö.addLayout(kolmasrivi)
        hyllystö.addSpacing(20)
        hyllystö.addLayout(neljäsrivi)
        hyllystö.addSpacing(20)
        hyllystö.addLayout(viidesrivi)
        hyllystö.addSpacing(20)
        hyllystö.addLayout(kuudesrivi)
        hyllystö.addSpacing(20)
        hyllystö.addLayout(seitsemäsrivi)
        hyllystö.addSpacing(20)
        hyllystö.addLayout(kahdeksasrivi)
        hyllystö.addSpacing(20)
        hyllystö.addLayout(yhdeksäsrivi)
        hyllystö.addSpacing(20)

        #Tekstikilvet

        nimiKilpi = QLabel("Nimi")
        palkkaKilpi = QLabel("Palkka")
        telProsKilpi = QLabel("Tel%")
        työtVakProsKilpi = QLabel("Työtvak%")
        tuloRajaKilpi = QLabel("Tuloraja")
        alempiKilpi = QLabel("Alempi%")
        ylempiKilpi = QLabel("Ylempi%")
        telKilpi = QLabel("Tel")
        työttömyysVakuutusKilpi = QLabel("Työttömyysvakuutus")
        verotKilpi = QLabel("Verot")
        nettoKilpi = QLabel("Netto")

        

        #Tekstikentät

        nimiKenttä = QLineEdit()
        palkkaKenttä = QLineEdit()
        telProsKenttä = QLineEdit("<font color=blue>4,7</font>")
        telProsKenttä.setReadOnly(True)
        työtVakProsKenttä= QLineEdit("0,6")
        työtVakProsKenttä.setReadOnly(True)
        tuloRajaKenttä= QLineEdit()
        alempiProsKenttä= QLineEdit()
        ylempiProsKenttä= QLineEdit()
        telKenttä= QLineEdit()
        telKenttä.setReadOnly(True)
        työttömyysVakuutusKenttä= QLineEdit()
        työttömyysVakuutusKenttä.setReadOnly(True)
        verotKenttä= QLineEdit()
        verotKenttä.setReadOnly(True)
        nettoKenttä= QLineEdit()
        nettoKenttä.setReadOnly(True)

        #Painike

        laskeNappi = QPushButton("Laske")


        #Objektien kiinnitys layoutiin
        
        ekarivi.addWidget(nimiKilpi)
        ekarivi.addSpacing(60)
        ekarivi.addWidget(nimiKenttä)
        tokarivi.addWidget(palkkaKilpi)
        tokarivi.addSpacing(60)
        tokarivi.addWidget(palkkaKenttä)
        kolmasrivi.addWidget(telProsKilpi)
        kolmasrivi.addSpacing(60)
        kolmasrivi.addWidget(telProsKenttä)
        kolmasrivi.addSpacing(60)
        kolmasrivi.addWidget(työtVakProsKilpi)
        kolmasrivi.addSpacing(20)
        kolmasrivi.addWidget(työtVakProsKenttä)
        neljäsrivi.addWidget(alempiKilpi)
        neljäsrivi.addSpacing(60)
        neljäsrivi.addWidget(alempiProsKenttä)
        neljäsrivi.addWidget(ylempiKilpi)
        neljäsrivi.addWidget(ylempiProsKenttä)
        viidesrivi.addWidget(laskeNappi)
        kuudesrivi.addWidget(telKilpi)
        kuudesrivi.addWidget(telKenttä)
        kuudesrivi.addWidget(työttömyysVakuutusKilpi)
        kuudesrivi.addWidget(työttömyysVakuutusKenttä)
        seitsemäsrivi.addWidget(verotKilpi)
        seitsemäsrivi.addWidget(verotKenttä)

        #TODO: LASKUFUNKTIOT, TULOSKENTTIEN HARMAANNUTTAMINEN JA KENTTIEN SIJOITTELU

        
        
        self.setLayout(hyllystö)

class Kalenterit(QDialog):    

    def __init__(self, parent=None):
        super(Kalenterit, self).__init__(parent)

        self.setWindowTitle("Kalenterit")

        #Layoutin asetus
        
        hyllystö = QVBoxLayout()
        ruudukko = QGridLayout()

        ensimmäinenrivi = QHBoxLayout()
        toinenrivi = QHBoxLayout()
        kolmasrivi = QHBoxLayout()

        hyllystö.addLayout(ensimmäinenrivi)

        #Kalenteri ja muut vimpaimet

        valitsePäiväKilpi = QLabel("Valitse päivä")
        toinenValitsePäiväKilpi = QLabel("Valitse päivä")

        #TODO: daysTo() FUNKTIO BUGAA, EI LASKE OIKEIN PÄIVIÄ, KEKSI JOTAKIN
        tulostusKilpi = QLabel("Ero tähän päivään 0 päivää")

        kalenteri = QCalendarWidget()

        kalenteriCombo = QDateTimeEdit()
        kalenteriCombo.calendarPopup()
        kalenteriCombo.setDisplayFormat("d.MMMM yyyy")
        kalenteriCombo.setDate(QDate.currentDate())

        #print(dir(kalenteriCombo))
        
        pvmYksi = kalenteri.selectedDate()
        pvmKaksi = QDate.currentDate()
        ETA = pvmKaksi.daysTo(pvmYksi)
        

        #Objektien kiinnitys layoutiin

        ruudukko.addWidget(valitsePäiväKilpi,0,0)
        ruudukko.addWidget(toinenValitsePäiväKilpi,0,1)

        ruudukko.addLayout(hyllystö,1,0)
        ruudukko.addWidget(kalenteri, 1,1)

        hyllystö.addWidget(kalenteriCombo)
        hyllystö.addWidget(tulostusKilpi)        
    
        #Signaalit

        def changeGridDate():
            
            kalenteri.setSelectedDate(kalenteriCombo.date())
            pvmYksi = kalenteri.selectedDate()
            pvmKaksi = QDate.currentDate()
            ETA = pvmKaksi.daysTo(pvmYksi)
            tulostusKilpi.setText("Ero tähän päivään "+str(ETA)+" päivää")

        def changeComboDate():
            pvmYksi = kalenteri.selectedDate()
            pvmKaksi = QDate.currentDate()
            ETA = pvmKaksi.daysTo(pvmYksi)
            

            kalenteriCombo.setDate(kalenteri.selectedDate())
            tulostusKilpi.setText("Ero tähän päivään "+str(ETA)+" päivää")

        self.connect(kalenteri,SIGNAL("selectionChanged()"),changeComboDate)
        self.connect(kalenteriCombo,SIGNAL("dateChanged()"),changeGridDate)

        #Layoutin asetus dialogiin
        
        self.setLayout(ruudukko)

def HoitoBoxExclusion(inp):
    täysiHoito = inp.parent().children()[2]
    puoliHoito = inp.parent().children()[6]
    if puoliHoito.isChecked() and inp == täysiHoito:
        puoliHoito.setChecked(False)  
    if täysiHoito.isChecked() and inp == puoliHoito:
        täysiHoito.setChecked(False)
        
    

class CustomCheckBox(QCheckBox):
    def __init__(self, parent=None):
        super(CustomCheckBox, self).__init__(parent)

    def mouseReleaseEvent(self,event):
        self.emit(SIGNAL(HoitoBoxExclusion(self)))
        self.toggle()    

class CheckBoxit(QDialog):    

    def __init__(self, parent=None):
        super(CheckBoxit, self).__init__(parent)

        self.setWindowTitle("Checkboxit")

        #Layoutin asetus
        
        ruudukko = QGridLayout()
        
        #CheckBoxit

        täysCheck = CustomCheckBox()
        puoliCheck = CustomCheckBox()
        retkiYksiCheck = CustomCheckBox()
        retkiKaksiCheck = CustomCheckBox()

        #Tekstikilvet

        tyhjä1 = QLabel()
        tyhjä2 = QLabel()
        täysiKilpi = QLabel("Täysihoito")
        täysiHinta = QLabel("200")
        puoliKilpi = QLabel("Puolihoito")
        puoliHinta = QLabel("100")
        retkiYksiKilpi = QLabel("Retki 1")
        retkiYksiHinta = QLabel("50")
        retkiKaksiKilpi = QLabel("Retki 2")
        retkiKaksiHinta = QLabel("30")
        loppuHintaKilpi = QLabel("")
        euroKilpi1 = QLabel("€")
        euroKilpi2 = QLabel("€")
        euroKilpi3 = QLabel("€")
        euroKilpi4 = QLabel("€")
        euroKilpi5 = QLabel("€")

        #Täysi- ja puolihoidon eksklusiivisuus

        hoidot = QButtonGroup()
        hoidot.addButton(täysCheck)
        hoidot.addButton(puoliCheck)

        #Laskentanappi

        laskentaNappi = QPushButton("Hyväksy")

        #Vimpainten asettaminen layoutiin

        ruudukko.addWidget(tyhjä1,0,0)
        ruudukko.addWidget(täysCheck,1,0)
        ruudukko.addWidget(täysiKilpi,1,1)
        ruudukko.addWidget(täysiHinta,1,2)
        ruudukko.addWidget(euroKilpi1,1,3)
        ruudukko.addWidget(puoliCheck,2,0)
        ruudukko.addWidget(puoliKilpi)
        ruudukko.addWidget(puoliHinta)
        ruudukko.addWidget(euroKilpi2)
        ruudukko.addWidget(retkiYksiCheck)
        ruudukko.addWidget(retkiYksiKilpi)
        ruudukko.addWidget(retkiYksiHinta)
        ruudukko.addWidget(euroKilpi3)
        ruudukko.addWidget(retkiKaksiCheck)
        ruudukko.addWidget(retkiKaksiKilpi)
        ruudukko.addWidget(retkiKaksiHinta)
        ruudukko.addWidget(euroKilpi4)
        ruudukko.addWidget(laskentaNappi)
        ruudukko.addWidget(tyhjä2)
        ruudukko.addWidget(loppuHintaKilpi)        
        ruudukko.addWidget(euroKilpi5)

        def laskeHinta():
            hinta = 0
            if täysCheck.isChecked() == True:
                hinta+=float(täysiHinta.text())
            if puoliCheck.isChecked() == True:
                hinta+=float(puoliHinta.text())
            if retkiYksiCheck.isChecked() == True:
                hinta+=float(retkiYksiHinta.text())
            if retkiKaksiCheck.isChecked() == True:
                hinta+=float(retkiKaksiHinta.text())
            loppuHintaKilpi.setText(str(hinta))
            
        self.connect(laskentaNappi, SIGNAL("clicked()"),laskeHinta)

        #Layoutin aktivointi
        
        self.setLayout(ruudukko)

class ÄänestysRadioButton(QRadioButton):
    def __init__(self, parent=None):
        super(ÄänestysRadioButton, self).__init__(parent)

        def ääntenLisäys():             
            self.parent().annetutÄänet[self.text()]+=1            
        
        self.connect(self,SIGNAL("clicked()"),ääntenLisäys)

        

class ÄänestysTilanneIkkuna(QDialog):    

    def __init__(self, parent=None):
        super(ÄänestysTilanneIkkuna, self).__init__(parent)

        self.setWindowTitle("Äänestystilanne")

        #Layoutin tyyppi

        hyllykkö = QVBoxLayout()

        #TODO: äänimäärien haku ja päivittäminen aina uuden äänen ilmaantuessa

        self.annetutÄänet = {"15":0,"16":0,"17":0,"18":0}
        self.sukuPuoliÄän = {"miehet":0,"naiset":0}

        #Vimpainten määrittely

        self.sukuPuoliJakaumaKilpi = QLabel("Äänestäneistä miehiä: "+str(self.sukuPuoliÄän["miehet"])+" naisia "+str(self.sukuPuoliÄän["naiset"]))

        viisitoistaKilpi = QLabel("15: "+str(self.annetutÄänet['15'])+" ääntä")
        kuusitoistaKilpi = QLabel("16: "+str(self.annetutÄänet['16'])+" ääntä")
        seitsemäntoistaKilpi = QLabel("17: "+str(self.annetutÄänet['17'])+" ääntä")
        kahdeksantoistaKilpi = QLabel("18: "+str(self.annetutÄänet['18'])+" ääntä")
        
        OKnappi = QPushButton("OK")

        #Napin toiminnallisuus

        self.connect(OKnappi,SIGNAL("clicked()"),self.close)

        #Ulkoinen pääsy kilpiin listan kautta

        self.ääniKilpiDict = {"15":viisitoistaKilpi,"16":kuusitoistaKilpi,"17":seitsemäntoistaKilpi,"18":kahdeksantoistaKilpi}
        

        #Vimpainten lisääminen layoutiin

        hyllykkö.addWidget(self.sukuPuoliJakaumaKilpi)
        hyllykkö.addWidget(viisitoistaKilpi)
        hyllykkö.addWidget(kuusitoistaKilpi)
        hyllykkö.addWidget(seitsemäntoistaKilpi)
        hyllykkö.addWidget(kahdeksantoistaKilpi)
        hyllykkö.addWidget(OKnappi)

        #Äänestystilanteen päivitys
        
        self.setLayout(hyllykkö)       
        

class RadioButtonit(QDialog):    

    #Äänestystilannelaskurina toimiva kirjasto

    

    def __init__(self, parent=None):
        super(RadioButtonit, self).__init__(parent)

        self.setWindowTitle("Mielipidekysely")

        self.setFixedSize(QSize(300,320))

        #Annettujen äänien kerääminen

        self.annetutÄänet = {"15":0,"16":0,"17":0,"18":0}
        miesÄänet = 0
        naisÄänet = 0

        #Tarvittavat vimpaimet

        tiedotKilpi = QLabel("Tiedot äänestäjästä")

        ikäRyhmäKilpi = QLabel("Ikäryhmä")

        nuorinNappi = QRadioButton("15-20")
        toinenIkäNappi = QRadioButton("20-30")
        kolmasIkäNappi = QRadioButton("30-50")
        neljäsIkäNappi = QRadioButton("Yli 50")

        ikäRyhmä = QButtonGroup()

        spRyhmä = QButtonGroup()   

        ääniRyhmä = QButtonGroup()

        sukuPuoliKilpi = QLabel("Sukupuoli")
        miesNappi = QRadioButton("mies")
        naisNappi = QRadioButton("nainen")            

        äänestysAiheKilpi = QLabel("Sopiva äänestysiän alaraja?")

        ekaÄänestysNappi = ÄänestysRadioButton("15")
        tokaÄänestysNappi = ÄänestysRadioButton("16")
        kolmasÄänestysNappi = ÄänestysRadioButton("17")
        neljäsÄänestysNappi = ÄänestysRadioButton("18")

        äänestysTilanneNappi = QPushButton("Näytä äänestystilanne")

        #Pohjalayoutin osat

        hyllystö = QVBoxLayout()

        ekaRadioRivi = QHBoxLayout()

        ikäRadioRyhmä = QVBoxLayout()
        sukupuoliRadioRyhmä = QVBoxLayout()
        
        tokaRadioRivi = QGridLayout()

        #Vimpainten asettelu layoutiin
        #ja layoutien asettelu toisiinsa

        hyllystö.addWidget(tiedotKilpi)

        hyllystö.addLayout(ekaRadioRivi)
        ekaRadioRivi.addLayout(ikäRadioRyhmä)
        ekaRadioRivi.addLayout(sukupuoliRadioRyhmä)

        ikäRadioRyhmä.addWidget(ikäRyhmäKilpi)
        ikäRadioRyhmä.addWidget(nuorinNappi)
        ikäRadioRyhmä.addWidget(toinenIkäNappi)
        ikäRadioRyhmä.addWidget(kolmasIkäNappi)
        ikäRadioRyhmä.addWidget(neljäsIkäNappi)

        sukupuoliRadioRyhmä.addWidget(sukuPuoliKilpi)
        sukupuoliRadioRyhmä.addWidget(miesNappi)
        sukupuoliRadioRyhmä.addWidget(naisNappi)
        sukupuoliRadioRyhmä.addSpacing(30)

        

        tokaRadioRivi.addWidget(ekaÄänestysNappi)
        tokaRadioRivi.addWidget(tokaÄänestysNappi,0,1)
        tokaRadioRivi.addWidget(kolmasÄänestysNappi)
        tokaRadioRivi.addWidget(neljäsÄänestysNappi)

        hyllystö.addSpacing(30)

        hyllystö.addWidget(äänestysAiheKilpi)

        hyllystö.addLayout(tokaRadioRivi)

        #RadioButtoneiden jako ryhmiin

        ikäRyhmä.addButton(nuorinNappi)
        ikäRyhmä.addButton(toinenIkäNappi)
        ikäRyhmä.addButton(kolmasIkäNappi)
        ikäRyhmä.addButton(neljäsIkäNappi)

        #Jostakin syystä nappi.group()-rivien poistaminen kytkee kaikki radio-
        #napit yhteen.
        
        nuorinNappi.group()
        
        spRyhmä.addButton(miesNappi)

        miesNappi.group()
            
        spRyhmä.addButton(naisNappi)

        ääniRyhmä.addButton(ekaÄänestysNappi)
        ääniRyhmä.addButton(tokaÄänestysNappi)
        ääniRyhmä.addButton(kolmasÄänestysNappi)
        ääniRyhmä.addButton(neljäsÄänestysNappi)

        hyllystö.addWidget(äänestysTilanneNappi)

        self.setLayout(hyllystö)        

        #Äänestystilanneikkunan avaaminen

        äänTilanneIkkuna = ÄänestysTilanneIkkuna()

        #TODO: äänimääräikkunan toiminnallisuus, ei ota syötettä normaalisti

        def äänenLisäys():
            
            
            if spRyhmä.checkedButton() == miesNappi:
                äänTilanneIkkuna.sukuPuoliÄän["miehet"]+=1                
            if spRyhmä.checkedButton() == naisNappi:
                äänTilanneIkkuna.sukuPuoliÄän["naiset"]+=1

            if spRyhmä.checkedButton() == miesNappi or spRyhmä.checkedButton() == naisNappi:
                kohdeIkä = ääniRyhmä.checkedButton().text()
                kohde = äänTilanneIkkuna.ääniKilpiDict[kohdeIkä]
                äänTilanneIkkuna.annetutÄänet[kohdeIkä]+=1
                kohde.setText(kohdeIkä+": "+str(äänTilanneIkkuna.annetutÄänet[kohdeIkä])+" ääntä")
            
                
                äänTilanneIkkuna.sukuPuoliJakaumaKilpi.setText("Äänestäneistä miehiä: "+str(äänTilanneIkkuna.sukuPuoliÄän["miehet"])+" naisia "+str(äänTilanneIkkuna.sukuPuoliÄän["naiset"]))


        def avaaTilanneIkkuna():            
            
            if miesNappi.isChecked() == True:
                äänTilanneIkkuna.sukuPuoliÄän["miehet"]+=1
            if naisNappi.isChecked() == True:
                äänTilanneIkkuna.sukuPuoliÄän["naiset"]+=1
            for ji in tokaRadioRivi.children():
                äänTilanneIkkuna.annetutÄänet[ji.text()]+=1  
            äänTilanneIkkuna.show()            
            äänTilanneIkkuna.move(self.pos().toTuple()[0]+340,self.pos().toTuple()[1])

        for jaja in ääniRyhmä.buttons():
            self.connect(jaja,SIGNAL("clicked()"),äänenLisäys)
            
        self.connect(äänestysTilanneNappi, SIGNAL("clicked()"),avaaTilanneIkkuna)


class VarmistusRuutu(QDialog):
    def __init__(self, parent=None):
        super(VarmistusRuutu, self).__init__(parent)

        self.setWindowTitle("Varmistus")                

        #Vimpainten määrittely

        self.tulostusKilpi = QLabel("")

        KylläNappi = QPushButton("Kyllä")
        EiNappi = QPushButton("Ei")

        #Layoutit

        hyllykkö = QVBoxLayout()

        nappiTaso = QHBoxLayout()

        #Vimpainten sijoittelu

        hyllykkö.addWidget(self.tulostusKilpi)

        hyllykkö.addLayout(nappiTaso)

        nappiTaso.addWidget(KylläNappi)

        nappiTaso.addWidget(EiNappi)            

        self.connect(KylläNappi, SIGNAL("clicked()"),self.close)
        self.connect(EiNappi, SIGNAL("clicked()"),self.close)

        self.setLayout(hyllykkö)
        
        #TODO: Ikkunan käyttökelpoisuus, ei ota syötettä niin kauan kuin pääikkuna
        #on maisemissa


class TyöasemaÄänestys(QDialog):

    def __init__(self, parent=None):
        super(TyöasemaÄänestys, self).__init__(parent)

        self.setWindowTitle("Paras työasema")

        #Layoutin muodostus

        hyllykkö = QVBoxLayout()

        #Neljä riviä horizontal boxeja

        konetyyppiRivi = QHBoxLayout()
        kaksiTärkeintäGrid = QGridLayout()
        
        #Vimpainten määrittelyt

        #TODO: selvitä, miten lihavointi toimii
        ensimKysymysKilpi = QLabel("<font type=bold>Valitse ensin työaseman perustyyppi</font>")

        pöytäkoneNappi = QRadioButton("Pöytäkone")
        kannettavaNappi = QRadioButton("Kannettava")
        
        toinenKysymysKilpi = QLabel("Valitse työaseman kaksi tärkeintä ominaisuutta")

        keskusMuistinKokoNappi = QCheckBox("Keskusmuistin koko")
        näytönKokoNappi = QCheckBox("Näytön koko")
        ulkoisenMuistinKokoNappi = QCheckBox("Ulkoisen muistin koko")
        painoNappi = QCheckBox("Paino")
        prosessorinTehotNappi = QCheckBox("Prosessorin tehot")
        akunKestoNappi = QCheckBox("Akun kesto")

        äänestäNappi = QPushButton("Äänestä")
        äänestäNappi.setMinimumHeight(40)

        #Horisontaalisen laatikon sisältö

        konetyyppiRivi.addWidget(pöytäkoneNappi)
        konetyyppiRivi.addWidget(kannettavaNappi)

        #Gridin sisältö

        kaksiTärkeintäGrid.addWidget(keskusMuistinKokoNappi,0,0)
        kaksiTärkeintäGrid.addWidget(näytönKokoNappi,0,1)
        
        kaksiTärkeintäGrid.addWidget(ulkoisenMuistinKokoNappi,1,0)
        kaksiTärkeintäGrid.addWidget(painoNappi)

        kaksiTärkeintäGrid.addWidget(prosessorinTehotNappi)
        kaksiTärkeintäGrid.addWidget(akunKestoNappi)
        
        #Sisällön järjestely layoutiin
        hyllykkö.addWidget(ensimKysymysKilpi)
        hyllykkö.addSpacing(30)
        
        hyllykkö.addLayout(konetyyppiRivi)
        hyllykkö.addSpacing(30)
        
        hyllykkö.addWidget(toinenKysymysKilpi)
        hyllykkö.addSpacing(30)
        hyllykkö.addLayout(kaksiTärkeintäGrid)
        hyllykkö.addSpacing(30)
        
        hyllykkö.addWidget(äänestäNappi)

        #Valintojen joukkouttaminen

        valintaJoukko = QButtonGroup()

        valintaJoukko.addButton(keskusMuistinKokoNappi)
        valintaJoukko.addButton(näytönKokoNappi)
        valintaJoukko.addButton(ulkoisenMuistinKokoNappi)
        valintaJoukko.addButton(painoNappi)
        valintaJoukko.addButton(prosessorinTehotNappi)
        valintaJoukko.addButton(akunKestoNappi)
        valintaJoukko.setExclusive(False)

        #Valintamuuttujien alustus

        valittuKoneTyyppi = ""
        valittujenLista = []
        self.valittujenKirjainJono = ""

        #Varmistusikkunan määrittely                                      

        

        #Äänen antamisen varmistus
    
        def varmistusIkkunanAvaus():            
            self.valittujenKirjainJono = ""
            if pöytäkoneNappi.isChecked() == True:
                valittuKoneTyyppi = "Pöytäkone"
            if kannettavaNappi.isChecked() == True:
                valittuKoneTyyppi = "Kannettava"
            for val in self.valittujenLista:
                self.valittujenKirjainJono+=str(val.text())+" "

            
            äänestysLopputulos = valittuKoneTyyppi+" "+self.valittujenKirjainJono

            varmistusIkkuna = VarmistusRuutu()            
            varmistusIkkuna.move(self.pos().toTuple()[0]+340,self.pos().toTuple()[1])
            varmistusIkkuna.tulostusKilpi.setText(äänestysLopputulos) #äänestysLopputulos)
            varmistusIkkuna.exec_()
            varmistusIkkuna.show()
            

        #Valintojen rajaamiseen valmistava muuttuja

        self.checkCount = 0

        #Akun keston poistaminen valinnoista/lisääminen valintoihin

        def akunKestoPois():
            if akunKestoNappi.isChecked() == True:
                akunKestoNappi.setChecked(False)
                self.checkCount-=1
            akunKestoNappi.setDisabled(True)
            kaksiValittu()
    
        def akunKestoPäälle():
            
            if self.checkCount != 2:                            
                akunKestoNappi.setDisabled(False)
            
        #Valintojen rajaaminen kahteen

        def kaksiValittu():
            self.checkCount = 0
            unCheckedList = []
            self.valittujenLista = []
            for wid in valintaJoukko.buttons():
                if wid.isChecked()==True:
                    self.checkCount+=1
                    self.valittujenLista.append(wid)
                else:
                    unCheckedList.append(wid)
                    
            if self.checkCount == 2:
                for aban in unCheckedList:
                    aban.setDisabled(True)
            if self.checkCount <=1:
                for den in valintaJoukko.buttons():                    
                    den.setDisabled(False)
                if pöytäkoneNappi.isChecked() == True:
                    unCheckedList.append(wid)
                if pöytäkoneNappi.isChecked() == True:                       
                    akunKestoNappi.setDisabled(True)


                   
        #Signaalien yhdistäminen valittaviin vimpaimiin
        
        self.connect(äänestäNappi, SIGNAL("clicked()"),varmistusIkkunanAvaus)
        self.connect(pöytäkoneNappi, SIGNAL("clicked()"),akunKestoPois)
        self.connect(kannettavaNappi, SIGNAL("pressed()"),akunKestoPäälle)
        for vJ in valintaJoukko.buttons():
            self.connect(vJ, SIGNAL("clicked()"),kaksiValittu)
        #self.connect(pöytäkoneNappi, SIGNAL("pressed()"),kaksiValittu)
        
        self.setLayout(hyllykkö)
        
class AnkkurointiTehtävä(QDialog):
    def __init__(self, parent=None):
        super(AnkkurointiTehtävä, self).__init__(parent)

        self.setWindowTitle("Matkan kesto")

        #Pohjalayout

        hyllykkö = QVBoxLayout()

        #Pienemmät layoutin palat

        ekaGrid = QGridLayout()

        tokaGrid = QGridLayout()

        kolmasGrid = QGridLayout()

        #Vimpainten määrittely

        lähtöPaikkaKilpi = QLabel("Lähtöpaikka")
        lähtöPaikkaKenttä = QLineEdit()

        kohdePaikkaKilpi = QLabel("Kohdepaikka")
        kohdePaikkaKenttä = QLineEdit()

        välimatkaKilpi = QLabel("Välimatka")
        välimatkaKenttä = QLineEdit()
        kmKilpi = QLabel("km")

        keskinopeusKilpi = QLabel("Keskinopeus")
        keskinopeusKenttä = QLineEdit()
        kmhKilpi = QLabel("km/h")
        
        laskeAikaNappi = QPushButton("Laske aika")
        #print(dir(laskeAikaNappi)) #.setHeight(30)
        #laskeAikaNappi.setSizePolicy(QSizePolicy("Expanding"))

        tulostusKilpi = QLabel("Ajoaika:")

        #Pienemmät layoutit sisään

        hyllykkö.addLayout(ekaGrid)

        hyllykkö.addLayout(tokaGrid)

        hyllykkö.addLayout(kolmasGrid)

        #Vimpainten asettelu layouteihin

        ekaGrid.addWidget(lähtöPaikkaKilpi,0,0)
        ekaGrid.addWidget(lähtöPaikkaKenttä,0,1)
        ekaGrid.addWidget(kohdePaikkaKilpi,1,0)
        ekaGrid.addWidget(kohdePaikkaKenttä)

        tokaGrid.addWidget(välimatkaKilpi,0,0)
        tokaGrid.addWidget(välimatkaKenttä,0,1)
        tokaGrid.addWidget(kmKilpi,0,2)
        tokaGrid.addWidget(keskinopeusKilpi,1,0)
        tokaGrid.addWidget(keskinopeusKenttä)
        tokaGrid.addWidget(kmhKilpi)

        kolmasGrid.addWidget(laskeAikaNappi,0,0)
        kolmasGrid.addWidget(tulostusKilpi,1,0)

        #Matka-ajan laskeminen ja näyttäminen kentissä

        def ajanKestonLasku():
            try:
                kulunutAika = float(välimatkaKenttä.text())*1000/(float(keskinopeusKenttä.text())/3.6)
                tulostusKilpi.setText("Ajoaika on "+str(int(kulunutAika/3600))+" tuntia ja "+str(round((kulunutAika%3600)/60,2))+" minuuttia")
            except:
                tulostusKilpi.setText("Syötevirhe")

        self.connect(laskeAikaNappi,SIGNAL("clicked()"),ajanKestonLasku)

        #Layoutin asettaminen avattuun ikkunaan

        self.setLayout(hyllykkö)           

        #TODO: nappien laajentaminen ikkunan mukana, kts. tehtävänanto

class TabPageTehtävä(QDialog):
    def __init__(self, parent=None):
        super(TabPageTehtävä, self).__init__(parent)

        self.setWindowTitle("Tabpaget")

        #Tabpagen ulkoinen layout

        hyllykkö = QVBoxLayout()

        #Tabpagen sisäiset layoutit

        kolmioHyllykkö = QVBoxLayout()
        kolmioLaskuSarakkeet = QGridLayout()
        kolmioHyllykkö.addLayout(kolmioLaskuSarakkeet)
        
        suoraKulmioHyllykkö = QVBoxLayout()
        suoraKulmioLaskuSarakkeet = QGridLayout()
        suoraKulmioHyllykkö.addLayout(suoraKulmioLaskuSarakkeet)
        
        ympyräHyllykkö = QVBoxLayout()
        ympyräLaskuSarakkeet = QHBoxLayout()
        ympyräHyllykkö.addLayout(ympyräLaskuSarakkeet)

        #Painonapit ja niiden toiminnot

        kolmioNappi = QPushButton("Laske pinta-ala")
        suoraKulmioNappi = QPushButton("Laske pinta-ala")
        ympyräNappi = QPushButton("Laske pinta-ala")

        def kolmioAlaLasku():
            try:
                kolmionAKenttä.setText("Pinta-ala: "+str(round(float(kolmionKantaKenttä.text())*float(kolmionKorkeusKenttä.text())/2,2)))
            except:
                kolmionAKenttä.setText("Error")

        def suoraKulmionAlaLasku():
            try:
                suoraKulmionAKenttä.setText("Pinta-ala: "+str(round(float(suoraKulmionKantaKenttä.text())*float(suoraKulmionKorkeusKenttä.text()),2)))
            except:
                suoraKulmionAKenttä.setText("Error")

        def ympyränAlaLasku():
            try:
                ympyränAKenttä.setText("Pinta-ala: "+str(round(float(ympyränSädeKenttä.text())**2*m.pi,2)))
            except:
                ympyränAKenttä.setText("Error")

        self.connect(kolmioNappi,SIGNAL("clicked()"),kolmioAlaLasku)
        self.connect(suoraKulmioNappi,SIGNAL("clicked()"),suoraKulmionAlaLasku)
        self.connect(ympyräNappi,SIGNAL("clicked()"),ympyränAlaLasku)

        #Kilvet ja -kentät

        kolmionKantaKilpi = QLabel("Kanta")
        kolmionKantaKenttä = QLineEdit()
        kolmionKorkeusKilpi = QLabel("Korkeus")
        kolmionKorkeusKenttä = QLineEdit()
        kolmionAKenttä = QLabel("Pinta-ala: ")
        

        suoraKulmionKantaKilpi = QLabel("Kanta")
        suoraKulmionKantaKenttä = QLineEdit()
        suoraKulmionKorkeusKilpi = QLabel("Korkeus")
        suoraKulmionKorkeusKenttä = QLineEdit()        
        suoraKulmionAKenttä = QLabel("Pinta-ala: ")
        
        ympyränSädeKilpi = QLabel("Säteen pituus")
        ympyränSädeKenttä = QLineEdit()
        ympyränAKenttä = QLabel("Pinta-ala: ")
        

        #Tabisivujen ja -pohjan määrittely

        kolmioSivu = QWidget()
        suoraKulmioSivu = QWidget()
        ympyräSivu = QWidget()
        
        kolmioSivu.setLayout(kolmioHyllykkö)
        suoraKulmioSivu.setLayout(suoraKulmioHyllykkö)
        ympyräSivu.setLayout(ympyräHyllykkö)

        pintaAlaSivut = QTabWidget()

        #Vimpainten lisääminen layouteihin

        kolmioLaskuSarakkeet.addWidget(kolmionKantaKilpi,0,0)
        kolmioLaskuSarakkeet.addWidget(kolmionKantaKenttä,0,1)
        kolmioLaskuSarakkeet.addWidget(kolmionKorkeusKilpi,1,0)
        kolmioLaskuSarakkeet.addWidget(kolmionKorkeusKenttä)
        kolmioHyllykkö.addWidget(kolmioNappi)
        kolmioHyllykkö.addWidget(kolmionAKenttä)        
        
        suoraKulmioLaskuSarakkeet.addWidget(suoraKulmionKantaKilpi,0,0)
        suoraKulmioLaskuSarakkeet.addWidget(suoraKulmionKantaKenttä,0,1)
        suoraKulmioLaskuSarakkeet.addWidget(suoraKulmionKorkeusKilpi,1,0)
        suoraKulmioLaskuSarakkeet.addWidget(suoraKulmionKorkeusKenttä)
        suoraKulmioHyllykkö.addWidget(suoraKulmioNappi)
        suoraKulmioHyllykkö.addWidget(suoraKulmionAKenttä)

        ympyräLaskuSarakkeet.addWidget(ympyränSädeKilpi,1,0)
        ympyräLaskuSarakkeet.addWidget(ympyränSädeKenttä)
        ympyräHyllykkö.addWidget(ympyräNappi)
        ympyräHyllykkö.addWidget(ympyränAKenttä)
        
        #Tabien lisääminen pohjaan

        pintaAlaSivut.addTab(kolmioSivu,"Kolmio")
        pintaAlaSivut.addTab(suoraKulmioSivu,"Suorakulmio")
        pintaAlaSivut.addTab(ympyräSivu,"Ympyrä")

        hyllykkö.addWidget(pintaAlaSivut)

        self.setLayout(hyllykkö)
        self.setMinimumSize(300,340)

class KurssiValintaLaatikko(QListWidget):
    def __init__(self, parent=None):
        super(KurssiValintaLaatikko, self).__init__(parent)

        self.valitutLista = []        

    #Määritellään hiirinapin vapautus uudestaan

    def mouseReleaseEvent(self, event):
        valmisTeksti = self.parent().valittuKurssiLaatikko.toPlainText()
        if self.currentItem().checkState() == Qt.Unchecked:
            self.currentItem().setCheckState(Qt.Checked)
            #Lisätään kurssilistalle
            
            self.parent().valittuKurssiLaatikko.setText(valmisTeksti+self.currentItem().text()+"\n")
        else:
            self.currentItem().setCheckState(Qt.Unchecked)
            self.parent().valittuKurssiLaatikko.setText(valmisTeksti.replace(self.currentItem().text()+"\n",""))
            
        


class KurssiIlmTehtävä(QDialog):
    def __init__(self, parent=None):
        super(KurssiIlmTehtävä, self).__init__(parent)

        self.setWindowTitle("Kurssi-ilmoittautuminen")

        #Layoutien määrittely

        #Alin pohja
        hyllystö = QVBoxLayout()

        #Ylempi ruudukko
        yläRuudukko = QGridLayout()

        #Alempi ruudukko
        alaRuudukko = QGridLayout()

        #Vimpainten määrittely

        #Tekstikilvet
        nimiKilpi = QLabel("Nimi")
        luokkaKilpi = QLabel("Luokka")
        kurssitKilpi = QLabel("Kurssit")
        valitutKurssitKilpi = QLabel("Valitut kurssit")

        #Nimikenttä
        nimiKenttä = QLineEdit()

        #Luokkatila
        luokkaComboBox = QComboBox()        

        luokat = ["KCAUTE13KA",
                  "KCAUTE13SA",
                  "KCTITE13"]

        for jut in luokat:
            luokkaComboBox.addItem(jut)

        #Kurssilistan pohja
        self.kurssiLaatikko = KurssiValintaLaatikko()

        kurssiNimet = ["Englanti",
                       "Systeemityöprojekti",
                       "Tietojärjestelmien kehittäminen",
                       "Sovelluskehitys",
                       "Olio-ohjelmointi",
                       "Johdatus ohjelmointiin 2",
                       "Johdatus ohjelmointiin 1"]

        for kur in kurssiNimet:
            uusiKurssi = QListWidgetItem()
            uusiKurssi.setText(kur)
            uusiKurssi.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            uusiKurssi.setCheckState(Qt.Unchecked)
            self.kurssiLaatikko.insertItem(0,uusiKurssi)
        
        #Valittu tekstilaatikko, listboxin kanssa tuli monta päivää takkua
        #jälki 

        self.valittuKurssiLaatikko = QTextEdit()

        #Suljetaan tekstikentän suora käyttäjäsyöte pois
        self.valittuKurssiLaatikko.setDisabled(True)

        #Vimpainten asettelu pohjiin
        yläRuudukko.addWidget(nimiKilpi,0,0)
        yläRuudukko.addWidget(nimiKenttä,0,1)
        yläRuudukko.addWidget(luokkaKilpi,1,0)
        yläRuudukko.addWidget(luokkaComboBox)

        alaRuudukko.addWidget(kurssitKilpi,0,0)
        alaRuudukko.addWidget(valitutKurssitKilpi,0,1)
        alaRuudukko.addWidget(self.kurssiLaatikko,1,0)
        alaRuudukko.addWidget(self.valittuKurssiLaatikko)

        #Pohjien asettelu toisiinsa
        hyllystö.addLayout(yläRuudukko)
        hyllystö.addSpacing(70)
        hyllystö.addLayout(alaRuudukko)        
        
        #Layoutin käyttöönotto
        self.setLayout(hyllystö)

class MatkaListoillaTehtävä(QDialog):
    def __init__(self, parent=None):
        super(MatkaListoillaTehtävä, self).__init__(parent)

        self.setWindowTitle("Matkanteko listoilla")

        #Pohjalayout

        hyllykkö = QVBoxLayout()

        #Pienemmät layoutin palat

        ekaGrid = QGridLayout()

        tokaGrid = QGridLayout()

        kolmasGrid = QGridLayout()

        #Vimpainten määrittely

        lähtöPaikkaKilpi = QLabel("Lähtöpaikka")
        lähtöPaikkaKenttä = QListWidget()

        kohdePaikkaKilpi = QLabel("Kohdepaikka")
        kohdePaikkaKenttä = QListWidget()

        välimatkaKilpi = QLabel("Välimatka")
        välimatkaCombo = QComboBox()
        kmKilpi = QLabel("km")

        keskinopeusKilpi = QLabel("Keskinopeus")
        keskiNopeusCombo = QComboBox()
        kmhKilpi = QLabel("km/h")
        
        laskeAikaNappi = QPushButton("Laske aika")
        #print(dir(laskeAikaNappi)) #.setHeight(30)
        #laskeAikaNappi.setSizePolicy(QSizePolicy("Expanding"))

        tulostusKilpi = QLabel("Ajoaika:")

        #Pienemmät layoutit sisään

        hyllykkö.addLayout(ekaGrid)

        hyllykkö.addLayout(tokaGrid)

        hyllykkö.addLayout(kolmasGrid)

        #Vimpainten asettelu layouteihin

        ekaGrid.addWidget(lähtöPaikkaKilpi,0,0)
        ekaGrid.addWidget(lähtöPaikkaKenttä,0,1)
        ekaGrid.addWidget(kohdePaikkaKilpi,1,0)
        ekaGrid.addWidget(kohdePaikkaKenttä)

        tokaGrid.addWidget(välimatkaKilpi,0,0)
        tokaGrid.addWidget(välimatkaCombo,0,1)
        tokaGrid.addWidget(kmKilpi,0,2)
        
        tokaGrid.addWidget(keskinopeusKilpi,1,0)
        tokaGrid.addWidget(keskiNopeusCombo)
        tokaGrid.addWidget(kmhKilpi)

        kolmasGrid.addWidget(laskeAikaNappi,0,0)
        kolmasGrid.addWidget(tulostusKilpi,1,0)

        #Comboboxien täyttäminen

        for nopeu in range(61):
            keskiNopeusCombo.addItem(str(nopeu+40))

        for matkat in range(25,800,25):
            välimatkaCombo.addItem(str(matkat+30))

        #ListWidgettien täyttäminen

        paikkaKuntaLista = ["Jyväskylä",
                            "Helsinki",
                            "Seinäjoki",
                            "Rovaniemi",
                            "Parkano",
                            "Vaasa",
                            "Oulu"]

        for paikka in paikkaKuntaLista:
            lähtöPaikkaKenttä.addItem(paikka)
            kohdePaikkaKenttä.addItem(paikka)

        #Matka-ajan laskeminen ja näyttäminen kentissä

        def ajanKestonLasku():
            try:
                kulunutAika = float(välimatkaCombo.currentText())*1000/(float(keskiNopeusCombo.currentText())/3.6)
                tulostusKilpi.setText("Ajoaika on "+str(int(kulunutAika/3600))+" tuntia ja "+str(round((kulunutAika%3600)/60,2))+" minuuttia,\nväli "+str(lähtöPaikkaKenttä.currentItem().text())+"-"+str(kohdePaikkaKenttä.currentItem().text()))
            except:
                tulostusKilpi.setText("Syötevirhe")

        self.connect(laskeAikaNappi,SIGNAL("clicked()"),ajanKestonLasku)

        #Layoutin asettaminen avattuun ikkunaan

        self.setLayout(hyllykkö)

class PuuNäkymä(QTreeView):
    def __init__(self, parent=None):
        super(PuuNäkymä, self).__init__(parent)

    #def mousePressEvent(self, event):
    #print("beep")
    #print(dir(event))
    #print(dir(self))
    #print(self.currentChanged())#focusItem())
    #print(self.selectionModel().selectedIndexes()[0])
    #print(dir(self))
    #print(self.currentIndex)

class PictureBoxTehtävä(QDialog):
    def __init__(self, parent=None):
        super(PictureBoxTehtävä, self).__init__(parent)

        self.setWindowTitle("Kuvan avaus ja tallennus")
    
        #Pohjalayout

        hyllykkö = QVBoxLayout()
        nappiRivi = QHBoxLayout()

        #Tiedostomalli määrittely

        tiedostoPuu = PuuNäkymä()
        #tiedostoPuu.setColumnCount(1)

        malli = QFileSystemModel()
        #print(malli.permissions(0))
        #print(malli.readOnly())
        
        tiedostoPuu.setModel(malli)
        #print(dir(QDir.currentPath()))
        #print(dir(QDir.Writable.Files())) #.homePath())
        #print([5:])
        #malli.setReadOnly(False)
        #print(malli.FilePermissions)
        #print(QDir.currentPath())

        #print(dir(malli))
        malli.setRootPath(QDir.homePath())

        
        
        #kohdistus = malli.child(0,1)
        #kohdistus = QModelIndex((0,1))
        #kohdistus = malli.child((0,1))

        #kohde = QModelIndex()
        #kohde.row = 0
        #kohde.column = 1

        def refreshPath():
            print(malli.filePath(kohde))

        aikuri = QTimer(self)

        self.connect(aikuri, SIGNAL("timeout()"), refreshPath)

        aikuri.start(1000)
        
        #print()
        #tiedostoPuu.setRootIndex(malli.index(QDir.homePath()))

        #tiedostoPuu.expand(1)
        #Vimpainten määrittely
        
        polkuKenttä = QLineEdit()
        tallennusNappi = QPushButton("Tallenna")
        avausNappi = QPushButton("Avaa")

        #Graafisten osien määrittely

        kuvaNäkymä = QGraphicsView()

        kuvaNäytös = QGraphicsScene()

        kuvaNäkymä.setScene(kuvaNäytös)

        def huhuilu():
            print("rrz")

        self.connect(tiedostoPuu,SIGNAL("expanded()"),huhuilu)
        #print(dir(tiedostoPuu))
        

        #pMap = QPi

        #kuvaNäytös.add()

        #Vimpainten asettaminen pohjaan

        hyllykkö.addWidget(polkuKenttä)
        
        hyllykkö.addWidget(tiedostoPuu)
        hyllykkö.addLayout(nappiRivi)
        nappiRivi.addWidget(avausNappi)
        nappiRivi.addWidget(tallennusNappi)

        hyllykkö.addWidget(kuvaNäkymä)
        

        self.setLayout(hyllykkö)

        #TODO: Tiedostopuun toimiminen ilman adminoikeuksia
        #TODO: Tiedostopolun poimiminen tiedosto puusta ja siitä eteenpäin

class ImageListTehtävä(QDialog):
    def __init__(self, parent=None):
        super(ImageListTehtävä, self).__init__(parent)

        self.setWindowTitle("Kuvagalleria")

        self.setMinimumSize(700,600)

        #Pohjan asetus

        hyllystö = QVBoxLayout()

        #Gridi radiobuttoneille

        nappiGrid = QGridLayout()

        #Vimpainten määrittely

        kuvaNäkymä = QGraphicsView()

        kuvaNäytös = QGraphicsScene()

        kuvaNäkymä.setScene(kuvaNäytös)

        ympyräNappi = QRadioButton("Ympyrä")
        neliöNappi = QRadioButton("Neliö")
        kolmioNappi = QRadioButton("Kolmio")
        plasmaNappi = QRadioButton("Plasma")

        #Kuvien määrittely, polku suhteessa python-tiedoston paikkaan

        kolmioKuva = QPixmap("Kuvat/Kolmiokuva.jpg")
        neliöKuva = QPixmap("Kuvat/NeliöKuva.jpg")
        ympyräKuva = QPixmap("Kuvat/Ympyräkuva.jpg")
        plasmaKuva = QPixmap("Kuvat/Plasma.jpg")
        
        def kolmionValinta():
            try:
                kuvaNäytös.removeItem(self.hetkenKuva)                
            except:
                pass            
            self.hetkenKuva = kuvaNäytös.addPixmap(kolmioKuva)

        def neliönValinta():
            try:
                kuvaNäytös.removeItem(self.hetkenKuva)                
            except:
                pass            
            self.hetkenKuva = kuvaNäytös.addPixmap(neliöKuva)

        def ympyränValinta():
            try:
                kuvaNäytös.removeItem(self.hetkenKuva)                
            except:
                pass            
            self.hetkenKuva = kuvaNäytös.addPixmap(ympyräKuva)

        def plasmaValinta():
            try:
                kuvaNäytös.removeItem(self.hetkenKuva)                
            except:
                pass            
            self.hetkenKuva = kuvaNäytös.addPixmap(plasmaKuva)
            
        self.connect(kolmioNappi,SIGNAL("pressed()"),kolmionValinta)
        self.connect(neliöNappi,SIGNAL("pressed()"),neliönValinta)
        self.connect(ympyräNappi,SIGNAL("pressed()"),ympyränValinta)
        self.connect(plasmaNappi,SIGNAL("pressed()"),plasmaValinta)

        #Vimpainten asettaminen layoutiin

        hyllystö.addWidget(kuvaNäkymä)

        hyllystö.addLayout(nappiGrid)
        
        nappiGrid.addWidget(ympyräNappi,0,0)
        nappiGrid.addWidget(neliöNappi,0,1)
        nappiGrid.addWidget(kolmioNappi,1,0)
        nappiGrid.addWidget(plasmaNappi)        

        self.setLayout(hyllystö)

class PikaValikkoTehtävä(QDialog):
    def __init__(self, parent=None):
        super(PikaValikkoTehtävä, self).__init__(parent)

        self.setWindowTitle("Pikavalikkotehtävä")

        hyllystö = QVBoxLayout()

        #Vimpainten määrittely

        """
        munMenu = QMenuBar()
        munMenu.addMenu("Files")

        hyllystö.setMenuBar(munMenu)

        """
        exitAction = QAction("Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        
        
        valeMain = QMainWindow()
        valeMain.statusBar()
        menubar = valeMain.menuBar()
        fileMenu = menubar.addMenu("Fuuu")
        fileMenu.addAction(exitAction)
        
        menubar = valeMain.addToolBar("Wee")

        qqBar = valeMain.addToolBar("QQ")

        #print(dir(qqBar))

        qqLabel = QLabel("lolololoo")

        jik = QComboBox()
        jik.addItem("ssrraa")
        hodd = jik.addItem("ottarr")

        print(dir(hodd))

        hooAction = QAction("ssrraa", jik)
        hooAction.triggered.connect(self.close)
        

        def zmm():
            print("hahaz")

        #self.connect(jik,SIGNAL("currentIndexChanged()"),zmm)

        #TODO: Menuosion toiminta, taustakuvat

        #hodd.triggered.connect(zmm)

        

        qqBar.addWidget(qqLabel)

        qqBar.addWidget(jik)

        hyllystö.addWidget(valeMain)

        te = QTextEdit()
        valeMain.setCentralWidget(te)

        #print(dir(valeMain))

        #poisAction = QAction(QIcon("exit24.png"),"Exit",self)
        #poisAction.triggered.connect(self.close)

        #self.addAction(poisAction)

        

        #menubar = self.menuBar()
        #self.toolbar = self.addToolBar("&Valitse taustakuvio")
        
        #print(dir(self))

        #Layoutin aktivointi

        self.setLayout(hyllystö)

class WebBrowserTehtävä(QDialog):
    def __init__(self, parent=None):
        super(WebBrowserTehtävä, self).__init__(parent)

        self.setWindowTitle("Pieni käärmebrowser")

        #Pohjalayout

        hyllystö = QVBoxLayout()

        #Hakurivi

        hakuRivi = QHBoxLayout()        

        #Vimpainten määrittely

        osoiteKenttä = QLineEdit()
        menoNappi = QPushButton("Go")

        #Selaimen osat
        
        selainPohja = QGraphicsView()

        selainNäytös = QGraphicsScene()
        
        selainPohja.setScene(selainNäytös)
        
        pohjaRuutu = selainNäytös.addRect(0,0,860,640)

        #Selain pitää sitoa scenen itemiin.

        selainAlue = QGraphicsWebView(parent = pohjaRuutu)

        selainAlue.load("http://www.maol.fi")

        #Pohjien sisältö

        hyllystö.addSpacing(20)
        hyllystö.addLayout(hakuRivi)
        hakuRivi.addWidget(osoiteKenttä)
        hakuRivi.addSpacing(30)
        hakuRivi.addWidget(menoNappi)
        hyllystö.addWidget(selainPohja)

        #Menonapin toiminta        

        def linkinAktivointi():
            selainAlue.load(osoiteKenttä.text())

        self.connect(menoNappi,SIGNAL("clicked()"),linkinAktivointi)

        #Pohjalayoutin aktivointi

        self.setLayout(hyllystö)
        
class VastaustenSeuranta(QDialog):
    def __init__(self, parent=None):
        super(VastaustenSeuranta, self).__init__(parent)

        self.setWindowTitle("Vastausten seuranta")

        #Pohjalayout

        hyllykkö = QVBoxLayout()

        #Vimpainten määrittelyt

        #Kertotaulutestien alue

        kertoKenttäYksi = QLineEdit()
        kertoKenttäYksi.setReadOnly(True)
        
        kertoMerkkiKilpi = QLabel("*")
        
        kertoKenttäKaksi = QLineEdit()
        kertoKenttäKaksi.setReadOnly(True)
        
        yhtäKuinMerkkiKilpi = QLabel("=")
        vastausKenttä = QLineEdit()
        vastausKenttä.setAutoFillBackground(True)

        #Vastausten seurannan alue

        tehtTehtäväKilpi = QLabel("Tehtyjä tehtäviä")
        oikVasKilpi = QLabel("Oikeita vastauksia")
        väärVasKilpi = QLabel("Vääriä vastauksia")
        oikProsKilpi = QLabel("Oikeiden %-osuus")

        täyttöKilpi = QLabel()
        täyttöKilpi.setMinimumWidth(150)

        tehtTehtäväKenttä = QLineEdit("0")
        tehtTehtäväKenttä.setReadOnly(True)
        
        oikVasKenttä = QLineEdit("0")
        oikVasKenttä.setReadOnly(True)
        
        väärVasKenttä = QLineEdit("0")
        väärVasKenttä.setReadOnly(True)

        oikProsKenttä = QLineEdit("0")
        oikProsKenttä.setReadOnly(True)

        uusiTestiNappi = QPushButton("Uusi testi")        
        uusiTestiNappi.setAutoDefault(False)        

        #Asetusten alue

        maxKertojaKilpi = QLabel("Max kertoja ja kerrottava")
        maxKertojaKenttä = QLineEdit("10")

        toistoRadioButton = QRadioButton("Sama tehtävä uudestaan")
        toistoRadioButton.setChecked(True)
        jatkoRadioButton = QRadioButton("Jatketaan normaalisti")

        käynTestKilpi = QLabel("Käynnistettyjen testien lukumäärä")
        käynTestKenttä = QLineEdit("1")
        käynTestKenttä.setReadOnly(True)
        

        #Tabpagen sisäiset layoutit

        laskeHyllykkö = QVBoxLayout()
        laskeRivi = QHBoxLayout()
        laskeSarakkeet = QGridLayout()        
        asetusNappiRyhmä = QGroupBox("Toiminta väärän vastauksen tapauksessa")
        asetusNappiHylly = QVBoxLayout()
        asetusNappiRyhmä.setLayout(asetusNappiHylly)
        käynTestiRivi = QHBoxLayout()
        
        asetusHyllykkö = QVBoxLayout()
        maxKertojaRivi = QHBoxLayout()
        asetusHyllykkö.addLayout(maxKertojaRivi)
        asetusHyllykkö.addWidget(asetusNappiRyhmä)
        asetusHyllykkö.addLayout(käynTestiRivi)       
        

        #Vimpainten ja alilayoutien asettelu tabeihin

        #Harjoitussivu

        laskeHyllykkö.addLayout(laskeRivi)

        laskeRivi.addWidget(kertoKenttäYksi)
        laskeRivi.addWidget(kertoMerkkiKilpi)
        laskeRivi.addWidget(kertoKenttäKaksi)
        laskeRivi.addWidget(yhtäKuinMerkkiKilpi)
        laskeRivi.addWidget(vastausKenttä)

        laskeHyllykkö.addLayout(laskeSarakkeet)        

        laskeSarakkeet.addWidget(tehtTehtäväKilpi,0,0)
        laskeSarakkeet.addWidget(täyttöKilpi,0,1)        
        laskeSarakkeet.addWidget(tehtTehtäväKenttä,0,2)
        laskeSarakkeet.addWidget(oikVasKilpi,1,0)
        laskeSarakkeet.addWidget(täyttöKilpi)
        laskeSarakkeet.addWidget(oikVasKenttä)
        laskeSarakkeet.addWidget(väärVasKilpi)
        laskeSarakkeet.addWidget(täyttöKilpi)
        laskeSarakkeet.addWidget(väärVasKenttä)
        laskeSarakkeet.addWidget(oikProsKilpi)
        laskeSarakkeet.addWidget(täyttöKilpi)
        laskeSarakkeet.addWidget(oikProsKenttä)

        laskeHyllykkö.addWidget(uusiTestiNappi)

        #Asetussivu

        maxKertojaRivi.addWidget(maxKertojaKilpi)
        maxKertojaRivi.addWidget(maxKertojaKenttä)

        asetusNappiHylly.addWidget(toistoRadioButton)
        asetusNappiHylly.addWidget(jatkoRadioButton)
        
        käynTestiRivi.addWidget(käynTestKilpi)
        käynTestiRivi.addWidget(käynTestKenttä)
        

        #print(dir(oikProsKenttä))

        #Tabisivujen ja -pohjan määrittely

        laskeSivu = QWidget()
        asetusSivu = QWidget()
        seurantaSivu = QWidget()
        
        laskeSivu.setLayout(laskeHyllykkö)
        asetusSivu.setLayout(asetusHyllykkö)

        kertoLaskuSivut = QTabWidget()        

        #Tabien lisääminen pohjaan

        kertoLaskuSivut.addTab(laskeSivu,"Testi")
        kertoLaskuSivut.addTab(asetusSivu,"Asetukset")

        hyllykkö.addWidget(kertoLaskuSivut)

        self.setLayout(hyllykkö)
        self.setMinimumSize(300,340)

        #Väripaletit

        vihrPal = QPalette()
        vihrPal.setColor(vastausKenttä.backgroundRole(),Qt.green)

        punPal = QPalette()
        punPal.setColor(vastausKenttä.backgroundRole(),Qt.red)

        valPal = QPalette()
        valPal.setColor(vastausKenttä.backgroundRole(),Qt.white)

        def uudetLuvut():
            kertoKenttäYksi.setText(str(r.randint(0,int(maxKertojaKenttä.text()))))
            kertoKenttäKaksi.setText(str(r.randint(0,int(maxKertojaKenttä.text()))))

        uudetLuvut()

        #Timeri

        välähdysAika = QTimer()  

        def väriReset():
            vastausKenttä.setPalette(valPal)
            välähdysAika.stop()       

        self.connect(välähdysAika,SIGNAL("timeout()"),väriReset)          

        #Testin toiminnallisuus            

        def uusiTesti():
            käynTestKenttä.setText(str(int(käynTestKenttä.text())+1))
            try:                
                uudetLuvut()
                
            except:
                kertoKenttäYksi.setText("Tarkista")
                kertoKenttäKaksi.setText("asetukset")
            tehtTehtäväKenttä.setText("0")
            oikVasKenttä.setText("0")
            väärVasKenttä.setText("0")
            oikProsKenttä.setText("0")
                        

        def tarkistaVastaus():
            tehtTehtäväKenttä.setText(str(int(tehtTehtäväKenttä.text())+1))
            try:
                if int(vastausKenttä.text()) == int(kertoKenttäYksi.text())*int(kertoKenttäKaksi.text()):
                    uudetLuvut()
                    vastausKenttä.setPalette(vihrPal)
                    oikVasKenttä.setText(str(int(oikVasKenttä.text())+1))
                    välähdysAika.start(2000)
                    vastausKenttä.setText("")                
                else:
                    
                    väärVasKenttä.setText(str(int(väärVasKenttä.text())+1))
                    vastausKenttä.setPalette(punPal)
                    välähdysAika.start(2000)
                    if jatkoRadioButton.isChecked() == True:
                        uudetLuvut()
                        
            
            except:                
                väärVasKenttä.setText(str(int(väärVasKenttä.text())+1))                
                vastausKenttä.setPalette(punPal)
                välähdysAika.start(1000)
                if jatkoRadioButton.isChecked() == True:
                    uudetLuvut()
            
            oikProsKenttä.setText(str(round(round(int(oikVasKenttä.text())/int(tehtTehtäväKenttä.text()),3)*100,2)))
            
        self.connect(uusiTestiNappi,SIGNAL("clicked()"),uusiTesti)
        self.connect(vastausKenttä,SIGNAL("returnPressed()"),tarkistaVastaus)

        #Pohjalayoutin aktivointi

        self.setLayout(hyllykkö)

class LottoRivit(QDialog):
    def __init__(self, parent=None):
        super(LottoRivit, self).__init__(parent)

        self.setWindowTitle("Lottoarvonta")

        #Pohjalayout

        hyllykkö = QVBoxLayout()

        #Pienemmät layoutit

        yläGridi = QGridLayout()

        #Vimpainten määrittely

        numeroMääräKilpi = QLabel("Arvottavien numeroiden lukumäärä")
        rivienMääräKilpi = QLabel("Arvottavien rivien lukumäärä")
        maxKilpi = QLabel("Arvottavien lukujen max")

        numeroMääräKenttä = QLineEdit()
        rivienMääräKenttä = QLineEdit()
        maxKenttä = QLineEdit()

        arvontaNappi = QPushButton("Arvo rivit")

        arvontaNappi.setFixedHeight(40)

        rivitKilpi = QLabel("Rivit:")

        arvontaRiviKenttä = QTextEdit()

        #Vimpainten sijoittelu pohjiin

        hyllykkö.addLayout(yläGridi)

        yläGridi.addWidget(numeroMääräKilpi,0,0)
        yläGridi.addWidget(numeroMääräKenttä,0,1)
        yläGridi.addWidget(rivienMääräKilpi,1,0)
        yläGridi.addWidget(rivienMääräKenttä)
        yläGridi.addWidget(maxKilpi)
        yläGridi.addWidget(maxKenttä)

        hyllykkö.addSpacing(20)

        hyllykkö.addWidget(arvontaNappi)

        hyllykkö.addWidget(rivitKilpi)
        hyllykkö.addWidget(arvontaRiviKenttä)

        def LottoArvonta():
            #Virhesyötetestaus

            try:
                nroMää = int(numeroMääräKenttä.text())
                riviMää = int(rivienMääräKenttä.text())
                maxLuku = int(maxKenttä.text())
                if nroMää > maxLuku:
                    arvontaRiviKenttä.setText("Liian lyhyet rivit numeromaksimiin nähden")                    
                else:
                    #Rivien arvonta
                    arvontaRiviKenttä.setText("")
                    loppuRivit = ""
                    for rvi in range(riviMää):
                        rivi = []
                        while len(rivi)<nroMää:                       
                            arvottuLuku = r.randint(1,maxLuku)
                            if arvottuLuku not in rivi:
                                rivi.append(arvottuLuku)
                        rivi.sort()
                        loppuRivit+=str(rivi).strip("[").strip("]")+"\n"
                    arvontaRiviKenttä.setText(loppuRivit[:-1])
            except:
                arvontaRiviKenttä.setText("Syötevirhe")
                
        self.connect(arvontaNappi,SIGNAL("clicked()"),LottoArvonta)

        #Pohjalayoutin aktivointi

        self.setLayout(hyllykkö)

class MerkkiJonoTehtävä(QDialog):
    def __init__(self, parent=None):
        super(MerkkiJonoTehtävä, self).__init__(parent)

        self.setWindowTitle("Merkkijonot")

        #Pohjalayout

        hyllykkö = QVBoxLayout()

        #Pienemmät layoutit

        yläGrid = QGridLayout()
        keskiGrid = QGridLayout()
        alaRivi = QHBoxLayout()

        hyllykkö.addLayout(yläGrid)
        hyllykkö.addLayout(keskiGrid)
        hyllykkö.addLayout(alaRivi)

        #Vimpainten määrittelyt

        jonoYKilpi = QLabel("Jono1")
        jonoKKilpi = QLabel("Jono2")

        jonoYKenttä = QLineEdit("")
        jonoKKenttä = QLineEdit("")

        jononPituusNappi = QPushButton("Merkkijonon pituus")
        onkoSamatNappi = QPushButton("Onko samat")
        keskimmäinenKirjNappi = QPushButton("Keskimmäinen kirjain")
        liitäYkkönenNappi = QPushButton("Liitä ykkönen")
        kaksiViimeistäNappi = QPushButton("Kaksi viimeistä kirjainta")
        monistuksetNappi = QPushButton("Monistukset")

        toistotLkmKilpi = QLabel("Toistot lkm")
        toistotLkmKenttä = QLineEdit()

        messu = QMessageBox()
        messu.setWindowTitle(" ")

        #Vimpainten asettelu layoutiin

        yläGrid.addWidget(jonoYKilpi,0,0)
        yläGrid.addWidget(jonoYKenttä,0,1)
        yläGrid.addWidget(jonoKKilpi,1,0)
        yläGrid.addWidget(jonoKKenttä)

        keskiGrid.addWidget(jononPituusNappi,0,0)
        keskiGrid.addWidget(onkoSamatNappi,0,1)
        keskiGrid.addWidget(keskimmäinenKirjNappi,1,0)
        keskiGrid.addWidget(liitäYkkönenNappi)
        keskiGrid.addWidget(kaksiViimeistäNappi)
        keskiGrid.addWidget(monistuksetNappi)

        alaRivi.addSpacing(monistuksetNappi.widthMM()+60)
        alaRivi.addWidget(toistotLkmKilpi)
        alaRivi.addWidget(toistotLkmKenttä)

        #Sisäiset muuttujat

        self.messuTeksti = ""

        #Nappien toiminnallisuus

        def näytäMessu():            
            messu.setText(self.messuTeksti)
            messu.exec_()

        def jonojenPituudet():
            self.messuTeksti = str(len(jonoYKenttä.text())+" merkkiä\n"+str(len(jonoKKenttä.text()))+" merkkiä\n")
            näytäMessu()

        def onkoSamat():
            if jonoYKenttä.text() == jonoKKenttä.text():
                self.messuTeksti = "Merkkijonot samat"
            else:
                self.messuTeksti = "Merkkijonot eroavat"
            näytäMessu()

        def keskimmäinenKirjain():
            self.messuTeksti = ""
            try:
                if len(jonoYKenttä.text())%2 == 0:
                    self.messuTeksti+="Jono 1 parillinen"
                else:
                    self.messuTeksti+="Jono 1 keskimmäinen merkki: "+str(jonoYKenttä.text()[int(len(jonoYKenttä.text())/2)])
                if len(jonoKKenttä.text())%2 == 0:
                    self.messuTeksti+="Jono 2 parillinen"
                else:
                    self.messuTeksti+="Jono 2 keskimmäinen merkki: "+str(jonoKKenttä.text()[int(len(jonoKKenttä.text())/2)])
            except:
                self.messuTeksti = "Syötevirhe"
            näytäMessu()

        def liitäYkkönen():
            self.messuTeksti = jonoKKenttä.text()+jonoYKenttä.text()
            näytäMessu()

        def kaksiViimeistä():
            self.messuTeksti = ""
            try:
                self.messuTeksti+="Jono 1 kaksi viimeistä merkkiä: "+str(jonoYKenttä.text()[-2:])+"\n"
                self.messuTeksti+="Jono 2 kaksi viimeistä merkkiä: "+str(jonoKKenttä.text()[-2:])
            except:
                self.messuTeksti = "Syötevirhe"
            näytäMessu()

        def liitäMonistus():
            self.messuTeksti = ""
            try:
                for toisto in range(int(toistotLkmKenttä.text())):
                    self.messuTeksti+= jonoYKenttä.text()
            except:
                self.messuTeksti = "Syötevirhe"
            näytäMessu()

            
        
        self.connect(jononPituusNappi,SIGNAL("clicked()"),jonojenPituudet)
        self.connect(onkoSamatNappi,SIGNAL("clicked()"),onkoSamat)
        self.connect(keskimmäinenKirjNappi,SIGNAL("clicked()"),keskimmäinenKirjain)
        self.connect(kaksiViimeistäNappi,SIGNAL("clicked()"),kaksiViimeistä)
        self.connect(liitäYkkönenNappi,SIGNAL("clicked()"),liitäYkkönen)
        self.connect(monistuksetNappi,SIGNAL("clicked()"),liitäMonistus)

        #juju = QMessageBox.information(self,"hasa","ili",QMessageBox.Ok)
        #sala = QMessageBox.about(self,"fuju","nora")
        
        #def onkoSamatTesti():
            

        #TODO: Avaa napeista uusi ikkuna, joka ei blokkaa vanhan toimintaa

        #Pohjalayoutin aktivointi

        self.setLayout(hyllykkö)

class DictionaryTehtävä(QDialog):
    def __init__(self, parent=None):
        super(DictionaryTehtävä, self).__init__(parent)

        self.setWindowTitle("Dictionary-tehtävä")

        #Pohjalayout

        hyllykkö = QVBoxLayout()

        #Alilayoutit ja niiden asettelu

        ekaRivi = QHBoxLayout()
        hyllykkö.addLayout(ekaRivi)

        tokaRivi = QHBoxLayout()
        hyllykkö.addLayout(tokaRivi)

        #Vimpainten määrittelyt

        tunnusKilpi = QLabel("Kurssin tunnus")
        self.tunnusKenttä = QLineEdit()
        virheKilpi = QLabel()
        virheKilpi.setMinimumWidth(200)

        nimiKilpi = QLabel("Kurssin nimi")
        self.nimiKenttä = QLineEdit()

        lisääKokoelmNappi = QPushButton("Lisää kokoelmaan")
        näytäKokoelmaNappi = QPushButton("Näytä kokoelma")        
        
        #Vimpainten asettelu layouteihin

        ekaRivi.addWidget(tunnusKilpi)
        ekaRivi.addWidget(self.tunnusKenttä)
        ekaRivi.addWidget(virheKilpi)

        tokaRivi.addWidget(nimiKilpi)
        tokaRivi.addWidget(self.nimiKenttä)

        hyllykkö.addWidget(lisääKokoelmNappi)
        hyllykkö.addWidget(näytäKokoelmaNappi)

        #Sisäinen kirjasto

        self.kurssiKirjasto = {}

        #Nappien toiminnallisuus
        def näytäKurssit():
            koonta = ""
            for i in self.kurssiKirjasto:
                koonta+=str(i) +" "+ str(self.kurssiKirjasto[i])+"\n"
            dictLaatikko = QMessageBox.question(self," ",koonta,QMessageBox.Ok)

        def lisääKurssi():
            try:
                tun = int(self.tunnusKenttä.text())
                self.kurssiKirjasto[tun] = self.nimiKenttä.text()
                virheKilpi.setText("")
                
            except:
                virheKilpi.setText("Tunnuksen tulee olla numero")         
        #QMessageBox.inputMethodEvent   
        
        self.connect(lisääKokoelmNappi,SIGNAL("clicked()"),lisääKurssi)
        self.connect(näytäKokoelmaNappi,SIGNAL("clicked()"),näytäKurssit)

        #Layoutin aktivointi

        self.setLayout(hyllykkö)

class Form(QDialog):    

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.setWindowTitle("Ohjelmoinnin Perusteet 2 PySide")

        #Harjoituksiin johtavien nappien määrittely

        EuroMarkkaHarjNap = QPushButton("Euro/markkamuunnin")            
        LaskinHarjNap = QPushButton("Laskin")
        AsteHarjNap = QPushButton("Astemuunnos")
        PalkkaHarjNap = QPushButton("Palkanlaskenta")
        KalenteriHarjNap = QPushButton("Kalenterit")
        CheckBoxHarjNap = QPushButton("Checkboxit")
        RadioButtonHarjNap = QPushButton("Mielipidekysely")
        TyöasemaÄänestysHarjNap = QPushButton("Paras työasema")
        AnkkurointiHarjNap = QPushButton("Ankkurointi")
        #LaskimenSkaalautHarjNap = QPushButton("Laskinskaalaus")
        TabPageHarjNap = QPushButton("TabPage")
        KursIlmHarjNap = QPushButton("Kurssi-ilmoittautuminen")
        MatkaListHarjNap = QPushButton("Matkanteko listoilla")
        PicboxHarjNap = QPushButton("Picturebox ja tallennus")
        ImageListHarjNap = QPushButton("Kuvalistat")
        PikaValikkoHarjNap = QPushButton("Pikavalikot")
        WebBrowserHarjNap = QPushButton("Web browser")
        StatKertTestiinHarjNap = QPushButton("Vastausten seuranta")
        KuvanHakuHarjNap = QPushButton("Kuvan haku ja tallennus")
        LottoHarjNap = QPushButton("Lottorivit")
        MerkkiJonoHarjNap = QPushButton("Merkkijonot")
        DictHarjNap = QPushButton("Dictionary-harjoitus")
        VanhaTentHarjNap = QPushButton("Vanha tentti")

        #Nappien toiminnallisuuden käynnistys

        def starttaaEurotMarkat():
            euroMarkkain = RahaMuunnin()
            euroMarkkain.exec_()

        def starttaaLaskin():
            laskukone = Laskin()
            laskukone.exec_()

        def starttaaAsteet():
            asteIkkuna = AsteMuunnin()
            asteIkkuna.exec_()

        def starttaaPalkkaLaskuri():
            palkkaIkkuna = PalkkaLaskuri()
            palkkaIkkuna.exec_()

        def starttaaKalenteri():
            kalenteriIkkuna = Kalenterit()
            kalenteriIkkuna.exec_()

        def starttaaCheckBoxit():
            checkBoxIkkuna = CheckBoxit()
            checkBoxIkkuna.exec_()

        def starttaaRadioButtonit():
            radioButtonIkkuna = RadioButtonit()
            radioButtonIkkuna.exec_()

        def starttaaTyöasemaÄänestys():
            työasemaIkkuna = TyöasemaÄänestys()
            työasemaIkkuna.exec_()

        def starttaaAnkkurointi():
            ankkurointiIkkuna = AnkkurointiTehtävä()
            ankkurointiIkkuna.exec_()

        def starttaaTabPaget():
            tabPageIkkuna = TabPageTehtävä()
            tabPageIkkuna.exec_()
            
        def starttaaKurssiIlm():
            kurssiIlmIkkuna = KurssiIlmTehtävä()
            kurssiIlmIkkuna.exec_()

        def starttaaMatkatListoilla():
            matkatListIkkuna = MatkaListoillaTehtävä()
            matkatListIkkuna.exec_()

        def starttaaPicBoxIkkuna():
            picBoxIkkuna = PictureBoxTehtävä()
            picBoxIkkuna.exec_()

        def starttaaImageList():
            imageListIkkuna = ImageListTehtävä()
            imageListIkkuna.exec_()

        def starttaaPikaValikko():
            pikaValikkoIkkuna = PikaValikkoTehtävä()
            pikaValikkoIkkuna.exec_()
        
        def starttaaWebBrowser():
            webBrowserIkkuna = WebBrowserTehtävä()
            webBrowserIkkuna.exec_()

        def starttaaVastaustenSeuranta():
            vastaustenSeurantaIkkuna = VastaustenSeuranta()
            vastaustenSeurantaIkkuna.exec_()

        def starttaaLottoRivit():
            lottoRiviIkkuna = LottoRivit()
            lottoRiviIkkuna.exec_()

        def starttaaMerkkiJonoTehtävä():
            merkkiJonoIkkuna = MerkkiJonoTehtävä()
            merkkiJonoIkkuna.exec_()

        def starttaaDictHarjoitus():
            dictHarjIkkuna = DictionaryTehtävä()
            dictHarjIkkuna.exec_()

        #Harjoitusikkunoiden avaaminen signaalista

        self.connect(EuroMarkkaHarjNap, SIGNAL("clicked()"),starttaaEurotMarkat)
        self.connect(LaskinHarjNap, SIGNAL("clicked()"),starttaaLaskin)
        self.connect(AsteHarjNap, SIGNAL("clicked()"),starttaaAsteet)
        self.connect(PalkkaHarjNap, SIGNAL("clicked()"),starttaaPalkkaLaskuri)
        self.connect(KalenteriHarjNap, SIGNAL("clicked()"),starttaaKalenteri)
        self.connect(CheckBoxHarjNap, SIGNAL("clicked()"),starttaaCheckBoxit)
        self.connect(RadioButtonHarjNap, SIGNAL("clicked()"),starttaaRadioButtonit)
        self.connect(TyöasemaÄänestysHarjNap, SIGNAL("clicked()"),starttaaTyöasemaÄänestys)
        self.connect(AnkkurointiHarjNap, SIGNAL("clicked()"),starttaaAnkkurointi)
        self.connect(TabPageHarjNap, SIGNAL("clicked()"),starttaaTabPaget)
        self.connect(KursIlmHarjNap, SIGNAL("clicked()"),starttaaKurssiIlm)
        self.connect(MatkaListHarjNap, SIGNAL("clicked()"),starttaaMatkatListoilla)
        self.connect(PicboxHarjNap, SIGNAL("clicked()"),starttaaPicBoxIkkuna)
        self.connect(ImageListHarjNap, SIGNAL("clicked()"), starttaaImageList)
        self.connect(PikaValikkoHarjNap, SIGNAL("clicked()"), starttaaPikaValikko)
        self.connect(WebBrowserHarjNap, SIGNAL("clicked()"), starttaaWebBrowser)
        self.connect(StatKertTestiinHarjNap, SIGNAL("clicked()"), starttaaVastaustenSeuranta)
        self.connect(LottoHarjNap, SIGNAL("clicked()"), starttaaLottoRivit)
        self.connect(MerkkiJonoHarjNap, SIGNAL("clicked()"), starttaaMerkkiJonoTehtävä)
        self.connect(DictHarjNap, SIGNAL("clicked()"), starttaaDictHarjoitus)
        
        #Layouttyypin määrittely
        
        allGrid = QGridLayout()

        #Painonappien lisäys layoutiin
        
        allGrid.addWidget(EuroMarkkaHarjNap,0,0)
        allGrid.addWidget(LaskinHarjNap,0,1)
        allGrid.addWidget(AsteHarjNap,0,2)
        allGrid.addWidget(PalkkaHarjNap,1,0)
        allGrid.addWidget(KalenteriHarjNap)
        allGrid.addWidget(CheckBoxHarjNap)
        allGrid.addWidget(RadioButtonHarjNap)
        allGrid.addWidget(TyöasemaÄänestysHarjNap)
        allGrid.addWidget(AnkkurointiHarjNap)
        #allGrid.addWidget(LaskimenSkaalautHarjNap)
        allGrid.addWidget(TabPageHarjNap)
        allGrid.addWidget(KursIlmHarjNap)
        allGrid.addWidget(MatkaListHarjNap)
        allGrid.addWidget(PicboxHarjNap)
        allGrid.addWidget(ImageListHarjNap)
        allGrid.addWidget(PikaValikkoHarjNap)
        allGrid.addWidget(WebBrowserHarjNap)
        allGrid.addWidget(StatKertTestiinHarjNap)
        allGrid.addWidget(KuvanHakuHarjNap)
        allGrid.addWidget(LottoHarjNap)
        allGrid.addWidget(MerkkiJonoHarjNap)
        allGrid.addWidget(DictHarjNap)
        allGrid.addWidget(VanhaTentHarjNap)

        for i in range(allGrid.count()):
            allGrid.itemAt(i).widget().setAutoDefault(False)
        
        #Ikkunasta toiseen siirrettävien muuttujien alustus

        self.äänestysLopputulos = ""
        
        #Layoutin aktivointi dialogi-ikkunassa

        self.setLayout(allGrid)

        
        
        
app = QApplication(sys.argv)
#Cleanup on exit

form = Form()
#form.connect(app,SIGNAL("aboutToQuit()"),clearSound)
form.show()
app.exec_()
          


