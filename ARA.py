# Annual Report Analysis functions
def grossMargin(a,b):
    """ Angiver hvor meget der er tilbage af omsætningen efter vareforbrug """
    """ Gross profit / revenue * 100 """
    return a/b*100
def calculateAg(a,b,c):
    """Resultat af primær drift+finansielle indtægter/gennemsnitlige aktiver"""
    return (a+b)/c*100
def calculateOg(a,b,c):
    """Resultat af primær drift+finansielle indtægter/nettoomsætning"""
    return (a+b)/c*100
def calculateAoh(a,b):
    """Nettoomsætning/Gennemsnitlige aktiver """
    return a/b
def calculateGr(a,b):
    """Finansielle omkostninger/gennemsnitlige forpligtelser"""
    return a/b*100
def calculateEkf(a,b):
    """Resultat før skat/gennemsnitlige egenkapital"""
    return a/b*100
def calculateGearing(a,b):
    """Gennemsnitlige forpligtelser/gennemsnitlige egenkapital"""
    return a/b
def calculateSg(a,b):
    """Egenkapital/aktiver"""
    return a/b*100
def calculateLg(a,b):
    """Omsætningsaktiver/kortfristede gældsforpligtelser"""
    return a/b*100
def earningCapacity():
    """ Indtjeningsevne """
    """ From gross profit up to operation profit """
    """ Analyze the ability to stay profitable """
    return 1
def indexNum(a,b):
    """Årets tal/basisåret"""
    return a/b*100
def relativeDev():
    """Åretstal-basisår/basisår*100"""
    return (b-a)/b*100





def agText(x,y,a,b,name):
    if(a>b):
        c = a-b
        ag_output = "Rentabiliteten i {} er forringet i analyseperioden, idet afkastningsgraden er faldet fra {}% i regnskabsår {} til {}% i regnskabsår {}, dvs. et fald på {} procentpoint ({}%).".format(name,a,x,b,y,c,differens(a,b))
        if(b>7):
            PH1 = " Afkastningsgraden ligger i {} på et tilfredsstillende niveau sammenlignet med markedsrente plus et risikotillæg.".format(y)
            return ag_output+PH1
        if(b<7):
            PH1 = " Afkastningsgraden ligger i {} på et utilfredsstillende niveau sammenlignet med markedsrente plus et risikotillæg.".format(y)
            return ag_output+PH1
    if(a<b):
        c = b-a
        ag_output = "Rentabiliteten i {} er forbedret i analyseperioden, idet afkastningsgraden er steget fra {}% i regnskabsår {} til {}% i regnskabsår {}, dvs. en stigning på {} procentpoint ({}%).".format(name,a,x,b,y,c,differens(a,b))
        if(b>7):
            PH1 = " Afkastningsgraden ligger i {} på et tilfredsstillende niveau sammenlignet med markedsrente plus et risikotillæg.".format(y)
            return ag_output+PH1
        if(b<7):
            PH1 = " Afkastningsgraden ligger i {} på et utilfredsstillende niveau sammenlignet med markedsrente plus et risikotillæg.".format(y)
            return ag_output+PH1
    if(a==b):
        ag_output = "Rentabiliteten i {} er hverken forbedret eller forringet i analyseperioden, idet afkastningsgraden på {}% er den samme i første og sidste regnskabsår.".format(name,a)
        if(b>7):
            PH1 = " Afkastningsgraden ligger i {} på et tilfredsstillende niveau sammenlignet med markedsrente plus et risikotillæg.".format(y)
            return ag_output+PH1
        if(b<7):
            PH1 = " Afkastningsgraden ligger i {} på et utilfredsstillende niveau sammenlignet med markedsrente plus et risikotillæg.".format(y)
            return ag_output+PH1
def ogText(a):
    if(a>b):
        c = a-b
        og_output = "\nVirksomhedens indtjeningsevne er forringet, idet overskudsgraden er faldet fra {}% i regnskabsår {} til {}% i regnskabsår {}, dvs. et fald på {}% ({}%). Dette har påvirket afkastningsgraden negativt.".format(a,x,b,y,c,differens(a,b))
        return og_output
    if(a<b):
        c = a-b
        og_output = "\nVirksomhedens indtjeningsevne er forringet, idet overskudsgraden er faldet fra {}% i regnskabsår {} til {}% i regnskabsår {}, dvs. et fald på {}% ({}%). Dette har påvirket afkastningsgraden positivt.".format(a,x,b,y,c,differens(a,b))
        return og_output
    if(a==b):
        og_output = "\nVirksomhedens indtjeningsevne er uændret idet overskudsgraden er uændret fra {}% i regnskabsår {} til {}% i regnskabsår {}. Dette har således ikke påvirket afkastningsgraden.".format(a,x,b,y)
        return og_output
def aohText(a):
    if(a>b):
        c = a-b
        aoh_output = "\nVirksomhedens kapitaltilpasningsevne er forringet i perioden, idet aktivernes omsætningshastighed er faldet fra {}% i regnskabsår {} til {}% i regnskabsår {}, dvs. et fald på {} procentpoint ({}%). Dette har påvirket afkastningsgraden negativt.".format(a,x,b,y,c,differens(a,b))
        return aoh_output
    if(a<b):
        c = b-a
        aoh_output = "\nVirksomhedens kapitaltilpasningsevne er forbedret i perioden, idet aktivernes omsætningshastighed er steget fra {}% i regnskabsår {} til {}% i regnskabsår {}, dvs. en stigning på {} procentpoint ({}%). Dette har påvirket afkastningsgraden positivt.".format(a,x,b,y,c,differens(a,b))
        return aoh_output
    if(a==b):
        aoh_output = "\nVirksomhedens kapitaltilpasningsevne er uændret i perioden, idet aktivernes omsætningshastighed er uændret fra {}g i regnskabsår {} til {}g i regnskabsår {}. Dette har således ikke påvirket afkastningsgraden.".format(a,x,b,y)
        return aoh_output
def grText(a):
    if(a>b):
        c = a-b
        gr_output = "\nGældsrenten er forringet i analyseperioden, idet den er faldet fra {}% i regnskabsår {} til {}% i regnskabsår {}, dvs. et fald på {} procentpoint ({}%).".format(a,x,b,y,c,differens(a,b))
        if(b>AG):
            PH1 = " Afkastningsgraden for {} viser, at hver investeret krone har givet et afkast på {} øre. Man har imidlertid i gennemsnit betalt {} øre i rente for hver lånte krone. Det medfører, at der er opnået et tab og betyder at det ikke har kunnet betale sig at arbejde med gæld.".format(y,AG,b)
            return gr_output+PH1
        if(b<AG):
            PH1 = " Afkastningsgraden for {} viser, at hver investeret krone har givet et afkast på {} øre. Man har imidlertid i gennemsnit betalt {} øre i rente for hver lånte krone. Det medfører, at der er opnået en fortjeneste og betyder at det har kunnet betale sig at arbejde med gæld.".format(y,AG,b)
            return gr_output+PH1
        if(b==AG):
            PH1 = " Afkastningsgraden for {} viser, at hver investeret krone har givet et afkast på {} øre. Man har imidlertid i gennemsnit betalt {} øre i rente for hver lånte krone. Det medfører, at der hverken er tjent eller tabt penge ved at arbejde med gæld.".format(y,AG,b)
            return gr_output+PH1
    if(a<b):
        c = b-a
        gr_output = "\nGældsrenten er forbedret i analyseperioden, idet den er steget fra {}% i regnskabsår {} til {}% i regnskabsår {}, dvs. en stigning på {} procentpoint ({}%).".format(a,x,b,y,c,differens(a,b))
        if(b>AG):
            PH1 = " Afkastningsgraden for {} viser, at hver investeret krone har givet et afkast på {} øre. Man har imidlertid i gennemsnit betalt {} øre i rente for hver lånte krone. Det medfører, at der er opnået et tab og betyder at det ikke har kunnet betale sig at arbejde med gæld.".format(y,AG,b)
            return gr_output+PH1
        if(b<AG):
            PH1 = " Afkastningsgraden for {} viser, at hver investeret krone har givet et afkast på {} øre. Man har imidlertid i gennemsnit betalt {} øre i rente for hver lånte krone. Det medfører, at der er opnået en fortjeneste og betyder at det har kunnet betale sig at arbejde med gæld.".format(y,AG,b)
            return gr_output+PH1
        if(b==AG):
            PH1 = " Afkastningsgraden for {} viser, at hver investeret krone har givet et afkast på {} øre. Man har imidlertid i gennemsnit betalt {} øre i rente for hver lånte krone. Det medfører, at der hverken er tjent eller tabt penge ved at arbejde med gæld.".format(y,AG,b)
            return gr_output+PH1
    if(a==b):
        gr_output = "\nGældsrenten er uændret i analyseperioden, idet den i første regnskabsår er {}% til det sidste regnskabsår som var {}%.".format(a,b)
        if(b>AG):
            PH1 = " Afkastningsgraden for {} viser, at hver investeret krone har givet et afkast på {} øre. Man har imidlertid i gennemsnit betalt {} øre i rente for hver lånte krone. Det medfører, at der er opnået et tab og betyder at det ikke har kunnet betale sig at arbejde med gæld.".format(y,AG,b)
            return gr_output+PH1
        if(b<AG):
            PH1 = " Afkastningsgraden for {} viser, at hver investeret krone har givet et afkast på {} øre. Man har imidlertid i gennemsnit betalt {} øre i rente for hver lånte krone. Det medfører, at der er opnået en fortjeneste og betyder at det har kunnet betale sig at arbejde med gæld.".format(y,AG,b)
            return gr_output+PH1
        if(b==AG):
            PH1 = " Afkastningsgraden for {} viser, at hver investeret krone har givet et afkast på {} øre. Man har imidlertid i gennemsnit betalt {} øre i rente for hver lånte krone. Det medfører, at der hverken er tjent eller tabt penge ved at arbejde med gæld.".format(y,AG,b)
            return gr_output+PH1             
def ekfText(a):
    if(a>b):
        c = a-b
        ekf_output = "\nEgenkapitalens forrentning er faldet fra {}% i regnskabsår {} til {}% i regnskabsår {}, dvs. et fald på {} procentpoint ({}%).".format(a,x,b,y,c,differens(a,b))
        if(b>7):
            PH1 = " Egenkapitalens forrentning befinder sig i {} på et tilfredsstillende niveau sammenlignet med markedsrenten plus et risikotillæg.".format(y)
            return ekf_output+PH1
        if(b<=7):
            PH1 = " Egenkapitalens forrentning befinder sig i {} på et utilfredsstillende niveau sammenlignet med markedsrenten plus et risikotillæg.".format(y)
            return ekf_output+PH1
    if(a<b):
        c = b-a
        ekf_output = "\nEgenkapitalens forrentning er forbedret fra {}% i regnskabsår {} til {}% i regnskabsår {}, dvs. en stigning på {} procentpoint ({}%).".format(a,x,b,y,c,differens(a,b))
        if(b>7):
            PH1 = " Egenkapitalens forrentning befinder sig i {} på et tilfredsstillende niveau sammenlignet med markedsrenten plus et risikotillæg.".format(y)
            return ekf_output+PH1
        if(b<=7):
            PH1 = " Egenkapitalens forrentning befinder sig i {} på et utilfredsstillende niveau sammenlignet med markedsrenten plus et risikotillæg.".format(y)
            return ekf_output+PH1
    if(a==b):
        c = a-b
        ekf_output = "\nEgenkapitalens forrentning er uændret fra {}% i regnskabsår {} til {}% i regnskabsår {}.".format(a,x,b,y,c,differens(a,b))
        if(b>7):
            PH1 = " Egenkapitalens forrentning befinder sig i {} på et tilfredsstillende niveau sammenlignet med markedsrenten plus et risikotillæg.".format(y)
            return ekf_output+PH1
        if(b<=7):
            PH1 = " Egenkapitalens forrentning befinder sig i {} på et utilfredsstillende niveau sammenlignet med markedsrenten plus et risikotillæg.".format(y)
            return ekf_output+PH1
def gearingText(a):
    if(a>b):
        c = a-b
        gearing_output = "\nGearingen er forringet i analyseperioden, idet gearingen er faldet fra {} i regnskabsår {} til {} i regnskabsår {}, dvs. et fald på {} ({}%).".format(a,x,b,y,c,differens(a,b))
        if(b>1):
            PH1 = "I {} er gearingen over 1.00, hvilket vil sige at den gennemsnitlige egenkapital er mindre end de gennemsnitlige forpligtelser.".format(y)
            if(AG>GR):
                PH2 = " Da virksomheden tjente penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været større end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG<GR):
                PH2 = " Da virksomheden mistede penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været lavere end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG==GR):
                PH2 = " Da virksomheden hverken tjente eller mistede penge ved at arbejde med gæld i {}, har gearingen ikke den store indflydelse på egenkapitalens forrentning.".format(y)
                return gearing_output+PH1+PH2
        if(b<1):
            PH1 = "I {} er gearingen under 1.00, hvilket vil sige at den gennemsnitlige egenkapital er højere end de gennemsnitlige forpligtelser.".format(y)
            if(AG>GR):
                PH2 = " Da virksomheden tjente penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været større end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG<GR):
                PH2 = " Da virksomheden mistede penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været lavere end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG==GR):
                PH2 = " Da virksomheden hverken tjente eller mistede penge ved at arbejde med gæld i {}, har gearingen ikke den store indflydelse på egenkapitalens forrentning.".format(y)
                return gearing_output+PH1+PH2
        if(b==1):
            PH1 = "I {} er gearingen lig 1.00, hvilket vil sige at den gennemsnitlige egenkapital og de gennemsnitlige forpligtelser er lige store.".format(y)
            if(AG>GR):
                PH2 = " Da virksomheden tjente penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været større end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG<GR):
                PH2 = " Da virksomheden mistede penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været lavere end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG==GR):
                PH2 = " Da virksomheden hverken tjente eller mistede penge ved at arbejde med gæld i {}, har gearingen ikke den store indflydelse på egenkapitalens forrentning.".format(y)
                return gearing_output+PH1+PH2
    if(a<b):
        c = b-a
        gearing_output = "\nGearingen er forbedret i analyseperioden, idet gearingen er steget fra {} i regnskabsår {} til {} i regnskabsår {}, dvs. en stigning på {} ({}%).".format(a,x,b,y,c,differens(a,b))
        if(b>1):
            PH1 = "I {} er gearingen over 1.00, hvilket vil sige at den gennemsnitlige egenkapital er mindre end de gennemsnitlige forpligtelser.".format(y)
            if(AG>GR):
                PH2 = " Da virksomheden tjente penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været større end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG<GR):
                PH2 = " Da virksomheden mistede penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været lavere end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG==GR):
                PH2 = " Da virksomheden hverken tjente eller mistede penge ved at arbejde med gæld i {}, har gearingen ikke den store indflydelse på egenkapitalens forrentning.".format(y)
                return gearing_output+PH1+PH2
        if(b<1):
            PH1 = "I {} er gearingen under 1.00, hvilket vil sige at den gennemsnitlige egenkapital er højere end de gennemsnitlige forpligtelser.".format(y)
            if(AG>GR):
                PH2 = " Da virksomheden tjente penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været større end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG<GR):
                PH2 = " Da virksomheden mistede penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været lavere end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG==GR):
                PH2 = " Da virksomheden hverken tjente eller mistede penge ved at arbejde med gæld i {}, har gearingen ikke den store indflydelse på egenkapitalens forrentning.".format(y)
                return gearing_output+PH1+PH2
        if(b==1):
            PH1 = "I {} er gearingen lig 1.00, hvilket vil sige at den gennemsnitlige egenkapital og de gennemsnitlige forpligtelser er lige store.".format(y)
            if(AG>GR):
                PH2 = " Da virksomheden tjente penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været større end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG<GR):
                PH2 = " Da virksomheden mistede penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været lavere end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG==GR):
                PH2 = " Da virksomheden hverken tjente eller mistede penge ved at arbejde med gæld i {}, har gearingen ikke den store indflydelse på egenkapitalens forrentning.".format(y)
                return gearing_output+PH1+PH2
    if(a==b):
        gearing_output = "\nGearingen er uændret i analyseperioden, idet gearingen er uændret fra {} i regnskabsår {} til {} i regnskabsår {}.".format()
        if(b>1):
            PH1 = "I {} er gearingen over 1.00, hvilket vil sige at den gennemsnitlige egenkapital er mindre end de gennemsnitlige forpligtelser.".format(y)
            if(AG>GR):
                PH2 = " Da virksomheden tjente penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været større end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG<GR):
                PH2 = " Da virksomheden mistede penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været lavere end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG==GR):
                PH2 = " Da virksomheden hverken tjente eller mistede penge ved at arbejde med gæld i {}, har gearingen ikke den store indflydelse på egenkapitalens forrentning.".format(y)
                return gearing_output+PH1+PH2
        if(b<1):
            PH1 = "I {} er gearingen under 1.00, hvilket vil sige at den gennemsnitlige egenkapital er højere end de gennemsnitlige forpligtelser.".format(y)
            if(AG>GR):
                PH2 = " Da virksomheden tjente penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været større end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG<GR):
                PH2 = " Da virksomheden mistede penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været lavere end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG==GR):
                PH2 = " Da virksomheden hverken tjente eller mistede penge ved at arbejde med gæld i {}, har gearingen ikke den store indflydelse på egenkapitalens forrentning.".format(y)
                return gearing_output+PH1+PH2
        if(b==1):
            PH1 = "I {} er gearingen lig 1.00, hvilket vil sige at den gennemsnitlige egenkapital og de gennemsnitlige forpligtelser er lige store.".format(y)
            if(AG>GR):
                PH2 = " Da virksomheden tjente penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været større end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG<GR):
                PH2 = " Da virksomheden mistede penge på at arbejde med gæld i {}, ville egenkapitalens forrentning havde været lavere end tilfældet nu, hvis gearingen havde været højere.".format(y)
                return gearing_output+PH1+PH2
            if(AG==GR):
                PH2 = " Da virksomheden hverken tjente eller mistede penge ved at arbejde med gæld i {}, har gearingen ikke den store indflydelse på egenkapitalens forrentning.".format(y)
                return gearing_output+PH1+PH2
"""
def sgText(a):
    sg_output = "\nSoliditetsgraden var i {} {}%, dvs. at {}% af de samlede investeringer (aktiver) i {} var finansieret med egenkapital.".format(x,a,a,name)
    text = " Man kan også udtrykke det på den måde, at {}% af hver investeret krone i virksomheden kom fra virksomhedsejerne.".format(a)
    if(a>c):
        delta = a-c
        PH1 = " I {} faldt soliditetsgraden til {}%, dvs. et fald på {}%.".format(z,c,differens(a,c))
        if(c>b):
            cc = c-b
            PH2 = " I det sidste regnskabsår som værende {}, faldt soliditetsgraden til {}%, dvs. et fald på {}%.".format(y,b,cc)
            if(b<30):
                PH3 = " I {} er soliditetsgraden på et relativt lavt niveau. Ud fra et soliditetshensyn er dette utilfredsstillende, da virksomheden kun kan tåle at tabe {}% af aktivernes værdi, inden långiverne lider tab.".format(y,b)
                PH4 = " Det betyder at det bliver sværere for virksomheden at optage lån, specielt vil banker være mere forsigtige med at udstede et lån med lavere rente overfor virksomheden."
                return sg_output+text+PH1+PH2+PH3+PH4
            if(b>30):
                PH3 = "
        if(c<b):
    if(a<c):

    if(a==c):     

    if(a<c):
def lgText(a):
    print("")
"""


