import json
import sys
from Connection import connection
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
    
if __name__ == '__main__':
    Remove_promotions_tradicional()