import pandas as pd

competicion=pd.read_excel('Futbol_Partidos.xlsx')


n_fecha=competicion['fecha']
n= int(len(n_fecha))
sum_g=[]
sum_v=[]
sum_t=[]
pais_T=[]
sumg=0
suma1=0
sum=0

pais_l= competicion['local'].drop_duplicates()
torneo= competicion['torneo'].drop_duplicates()

def goles_local():

    for x in range (len(pais_l)):
        pais=str(pais_l.iloc[x])
        sumg=0
        for m in range (len(n_fecha)):
            p=str(competicion.loc[m,'local'])
            if pais==p:
               n= int( competicion.loc[m,'goles_local'])
               sumg=sumg+n
               
        sum_g.append(sumg)
    
    goles_l={'Pais':pais_l , 'Goles Local':sum_g}
    gol_l=pd.DataFrame(data=goles_l)
    return gol_l


def goles_visitante():
    for x in range (len(pais_l)):
        pais=str(pais_l.iloc[x])
        sum=0
        for m in range (len(n_fecha)):
            p=str(competicion.loc[m,'visitante'])
            if pais==p:
                n= int( competicion.loc[m,'goles_visita'])
                sum=sum+n
        sum_v.append(sum)
    
    goles_v={'Pais':pais_l , 'Goles Visitante':sum_v}
    gol_v=pd.DataFrame(data=goles_v)
    return gol_v

def goles_totales():
    goles_v=competicion['goles_visita'].sum()
    goles_l=competicion['goles_local'].sum()
    goles_t=goles_v+goles_l
    return goles_t