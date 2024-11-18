import json,sys,datetime
from Connection import connection
from Utils import header
def Remove_promotions_tradicional():
    with open ("json/promos-tradicional.json", "r") as r:
        promotions_tradicional = json.load(r)
    
    with open ("json/clientes-mayoristas.json", "r") as r:
        customers_mayoristas = json.load(r)
    countrows = 0
    
    try:
        file = open("logs/log_delete.emrc","w")    
        for customer in customers_mayoristas:
            sys.stdout.write("#")
            sys.stdout.flush()
            for promotion in promotions_tradicional:
                #data
                cvepmc = promotion.get('CVEPMC')
                nompmc = promotion.get('NOMPMC')
                cvecli = customer.get('CVECLI')
                nomcli = customer.get('CLIENTE')
                #Conection Sql Server
                con = connection()
                sql = con.cursor()
                #Execute query
                command = "delete from tsive012pc where cvepmc=? and cvecli=?"
                params = (cvepmc,cvecli)
                sql.execute(command,params)
                rows = sql.rowcount
                if(rows>0):
                    countrows+=1
                    file.write(f"La promocion: {cvepmc} {nompmc} del cliente: {cvecli} {nomcli} se ha eliminado \n")
                else:
                    file.write(f"La promocion: {cvepmc} {nompmc} del cliente: {cvecli} {nomcli} no esta asignada \n")    
                sql.commit()
                sql.close()
    except Exception as ex:
            print("Ha ocurrido un problema a la hora de eliminar la promoción: ", cvepmc, "Con el cliente: ", cvecli ," ",ex)                 
    finally:
        print("\n Numero de promociones eliminadas: ", str(countrows))
        file.write(f"Total de eliminaciones: {countrows} \n")
        file.close()
def Add_promotions_mayoristas():
    with open ("json/promos-mayoristas.json", "r") as r:
        promotions_mayoristas = json.load(r)
    
    with open ("json/clientes-mayoristas.json", "r") as r:
        customers_mayoristas = json.load(r)
    countrows = 0
    try:
        file = open("logs/log_add.emrc","w")
        for customer in customers_mayoristas:
            sys.stdout.write("#")
            sys.stdout.flush()
            for promotion in promotions_mayoristas:
                #data
                cvepmc = promotion.get('CVEPMC')
                nompmc = promotion.get('NOMPMC')
                cvecli = customer.get('CVECLI')
                nomcli = customer.get('CLIENTE')
                #Conection Sql Server
                con = connection()
                sql = con.cursor()
                #Execute query
                command = "select * from tsive012pc where cvepmc = ? and cvecli = ?;"
                params = (cvepmc,cvecli)
                sql.execute(command,params)
                rows = sql.fetchall()
                if(len(rows)>=1):
                    file.write(f"La promocion: {cvepmc} {nompmc} del cliente: {cvecli} {nomcli} ya se encuentra registrada {len(rows)} veces \n")
                else:
                    now = datetime.datetime.now()
                    command = "insert into tsive012pc values (?,?,0,'COMERSAT',?,NULL, NULL, NULL , NULL, 2,1,NULL)"
                    params = (cvepmc,cvecli,now)
                    sql.execute(command,params)
                    rows = sql.rowcount
                    if(rows>0):
                        countrows+=1
                        file.write(f"La promocion: {cvepmc} {nompmc} del cliente: {cvecli} {nomcli} se ha insertado \n")   
                sql.commit()
                sql.close()
    except Exception as ex:
            print("Ha ocurrido un problema a la hora de eliminar la promoción: ", cvepmc, "Con el cliente: ", cvecli ," ",ex)                 
    finally:
        print("\n Numero de promociones agregadas: ", str(countrows))
        file.write(f"Total de promociones agregadas: {countrows} \n")
        file.close()
        
if __name__ == '__main__':
    header()
    print("----------------------------")
    print("|1.- Delete Promotions ----|")
    print("|2.-  Add Promotions    ---|")
    print("----------------------------")
    opt = int(input("Option: "))
    if(opt==1):
        Remove_promotions_tradicional()
    if(opt==2):
        Add_promotions_mayoristas()