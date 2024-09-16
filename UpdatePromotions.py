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
        for customer in customers_mayoristas:
            sys.stdout.write("#")
            sys.stdout.flush()
            for promotion in promotions_tradicional:
                #data
                cvepmc = promotion.get('CVEPMC')
                cvecli = customer.get('CVECLI')
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
                sql.commit()
                sql.close()
    except Exception as ex:
            print("Ha ocurrido un problema a la hora de eliminar la promoción: ", cvepmc, "Con el cliente: ", cvecli ," ",ex)                 
    finally:
        print("\n Numero de promociones eliminadas: ", str(countrows))
    
if __name__ == '__main__':
    Remove_promotions_tradicional()