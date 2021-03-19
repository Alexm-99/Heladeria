import sqlite3
from datetime import date


path='Data/db_favan.db'
class Consultas():

    

    def consultaIdPersonal(self, idx):
        print(idx)
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT ID_PERSONAL, CED_PERS, NOM_PERS, APE_PERS, ID_SUCURSAL_fk FROM PERSONAL WHERE ID_PERSONAL = ? ", (idx,))
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        try:
            dato = cursor.fetchall()
            return dato
        except:
            conexion.close()
            return cursor

        
    def consultaCedPersonal(self, cedula):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT ID_PERSONAL,CED_PERS, NOM_PERS, APE_PERS, ID_SUCURSAL_fk FROM PERSONAL WHERE CED_PERS = ?", (cedula,))
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        try:
            dato = cursor.fetchall()
            return dato
        except:
            conexion.close()
            return cursor



   
    def consultaIdCliente(self, idx):
        
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM CLIENTE WHERE ID_CLIENTE = ?", (idx,))
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        try:
            dato = cursor.fetchall()
            return dato
        except:
            conexion.close()
            return cursor

        
    def consultaCedCliente(self, cedula):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM CLIENTE WHERE CED_CLIENTE = ?", (cedula,))
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        try:
            dato = cursor.fetchall()
            return dato
        except:
            conexion.close()
            return cursor


    def consultaIdClienteFactura(self,id):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        #cursor.execute("INSERT INTO SUCURSAL VALUES ('SU01','MANTA','CALLE13')")
        #cursor.execute("INSERT INTO FACTURA VALUES ('FA02','PER02','01','SU01','10-10-2020')")
        #cursor.execute("INSERT INTO DETALLE_FACTURA VALUES ('DF01','','01','SU01','10-10-2020')")
        #conexion.commit()
        cursor.execute("SELECT ID_FACTURA, ID_CLIENTE, CED_CLIENTE, NOM_CLIENTE || ' ' || \
            APE_CLIENTE, DETALLE_FACTURA.IVA,DETALLE_FACTURA.DESCUENTO,DETALLE_FACTURA.TOTAL, FACTURA.FECHA  \
            FROM CLIENTE INNER JOIN FACTURA ON FACTURA.ID_CLIENTE_fk = CLIENTE.ID_CLIENTE \
                INNER JOIN DETALLE_FACTURA ON DETALLE_FACTURA.ID_FACTURA_fk = FACTURA.ID_FACTURA \
                WHERE CLIENTE.ID_CLIENTE = ?", (id,))
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        try:
            dato = cursor.fetchall()
            return dato
        except:
            conexion.close()
            return cursor

    def ConsultaPrecioAderezo(self,idx):
        conexion = sqlite3.connect('Data/db_favan.db')
        cursor = conexion.cursor()        
        cursor.execute("SELECT VALOR_ADEREZO FROM ADEREZO WHERE NOM_ADEREZO = ?", (idx,))      
        dato = cursor.fetchone()
        conexion.close()
        return dato

    def ConsultaAderezo(self,idx):
        conexion = sqlite3.connect('Data/db_favan.db')
        cursor = conexion.cursor()    
        if idx=="1234567":    
            cursor.execute("SELECT * FROM ADEREZO")
        else:
            cursor.execute("SELECT * FROM ADEREZO WHERE ID_ADEREZO = ?", (idx,))
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        dato = cursor.fetchall()
        conexion.close()
        return dato
    def consultaTamanio_envase(self,Tamanio,Envase):
        conexion = sqlite3.connect('Data/db_favan.db')
        cursor = conexion.cursor()        
        cursor.execute("SELECT * FROM TAMANIO WHERE TIPO_TAMANIO = ?", (Tamanio,))      
        dato = cursor.fetchone()
        cursor.execute("SELECT * FROM ENVASE WHERE TIPO_ENVASE = ?", (Envase,))
        dato=dato + cursor.fetchone()  
        conexion.close()
        return dato
    def consulta_cliente_id(self, idx):
        conexion = sqlite3.connect('Data/db_favan.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT CED_CLIENTE, NOM_CLIENTE|| ' ' || APE_CLIENTE, COR_CLIENTE, TELF_CLIENTE FROM CLIENTE WHERE ID_CLIENTE = ?", (idx,))      
        return cursor.fetchone()
    def consulta_cliente_ced(self, idx):
        conexion = sqlite3.connect('Data/db_favan.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT ID_CLIENTE, NOM_CLIENTE|| ' ' || APE_CLIENTE, COR_CLIENTE, TELF_CLIENTE FROM CLIENTE WHERE CED_CLIENTE = ?", (idx,))
        return cursor.fetchone()
    def consultar_ultimo_H(self):
        conexion = sqlite3.connect('Data/db_favan.db')
        cursor = conexion.cursor()        
        cursor.execute("SELECT * FROM PEDIDO WHERE ID_HELADO = (SELECT MAX(ID_HELADO) FROM PEDIDO)")      
        dato = cursor.fetchone()
        conexion.close()
        return dato
    def cosultaNomAde(self,tamanio,envase):
        conexion = sqlite3.connect('Data/db_favan.db')
        cursor = conexion.cursor()        
        cursor.execute("SELECT TIPO_TAMANIO FROM TAMANIO WHERE ID_TAMANIO = ?",(tamanio,))      
        dato = cursor.fetchone()
        cursor.execute("SELECT TIPO_ENVASE FROM ENVASE WHERE ID_ENVASE = ?",(envase,))      
        dato = dato+ cursor.fetchone()
        conexion.close()
        return dato
#------------------------------------DETALLE FACTURA------------------------------------
class Detalle_Factura():
    def __init__(self):
        self.ID_DETALLE_FAC=""
        self.ID_FACTURA=""
        self.ID_HELADO=""
        self.SUBTOTAL=0
        self.DESCUENTO=10
        self.IVA=0.0
        self.TOTAL=0

    def contar_id(self):
        conexion = sqlite3.connect('Data/db_favan.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT count(ID) FROM DETALLE_FACTURA")
        id_new=cursor.fetchone()
        self.ID_DETALLE_FAC="DTF"+str(id_new[0]+1)
        cursor.close()
        conexion.close()
        return self.ID_DETALLE_FAC
    def registro(self):
        path = 'Data/db_favan.db'
        try:
            conexion = sqlite3.connect(path)
            cursor = conexion.cursor()
            lista=[self.ID_DETALLE_FAC,self.ID_FACTURA,self.ID_HELADO,self.DESCUENTO,self.IVA,self.TOTAL]
            conexion.execute("INSERT INTO DETALLE_FACTURA VALUES (?, ?, ?, ?, ?, ?)", lista)
            conexion.commit()
            cursor.close()
            conexion.close()
            return 'Guardado con éxito' 
        except sqlite3.IntegrityError as e:
            cursor.close()
            conexion.close()
            return 'No se Guardo. El id es único \n{}'.format(e)    


    

#----------------------------- FACTURA------------------------------------------------------

class Facturas():
    def __init__(self):
        self.ID_FACTURA=""
        self.ID_PERSONAL="f"
        self.ID_CLIENTE=""
        self.FECHA=str(date.today())
    def registro(self):
        path = 'Data/db_favan.db'
        try:
            conexion = sqlite3.connect(path)
            cursor = conexion.cursor()
            lista=[self.ID_FACTURA,self.ID_PERSONAL,self.ID_CLIENTE,self.FECHA]
            conexion.execute("INSERT INTO FACTURA VALUES (?, ?, ?, ?)", lista)
            conexion.commit()
            cursor.close()
            conexion.close()
            return 'Guardado con éxito' 
        except sqlite3.IntegrityError as e:
            cursor.close()
            conexion.close()
            return 'No se Guardo. El id es único \n{}'.format(e)    
    
    def contar_id(self):
        conexion = sqlite3.connect('Data/db_favan.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT count(ID_FACTURA) FROM FACTURA")
        id_new=cursor.fetchone()
        self.ID_FACTURA="FC"+str(id_new[0]+1)
        cursor.close()
        conexion.close()
        return self.ID_FACTURA

#----------------------------------- PEDIDO -------------------------------------------
class Pedido():
    def __init__(self):
        self.ID_HELADO=""
        self.ENVASE=""
        self.TAMANIO=""
        self.ADEREZO=""
        self.LIST_ADEREZO=[]
        self.PRECIO=0.0


    def contar_id(self):
        conexion = sqlite3.connect('Data/db_favan.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT count(ID_HELADO) FROM PEDIDO")
        id_new=cursor.fetchone()
        self.ID_HELADO="H "+str(id_new[0]+1)
        cursor.close()
        conexion.close()

    def listaArreglada(self):
        listA=""
        for i in range(self.LIST_ADEREZO.__len__()):
            if i == self.LIST_ADEREZO.__len__()-1:
                listA= listA +str(self.LIST_ADEREZO[i])
            else:
                listA= listA +str(self.LIST_ADEREZO[i]) +", "
        return listA
    def registro(self):
        path = 'Data/db_favan.db'
        try:
            conexion = sqlite3.connect(path)
            cursor = conexion.cursor()
            lista=[self.ID_HELADO,self.ENVASE,self.TAMANIO,self.ADEREZO,str(self.LIST_ADEREZO),self.PRECIO]
            conexion.execute("INSERT INTO PEDIDO VALUES (?, ?, ?, ?, ?, ?)", lista)
            conexion.commit()
            cursor.close()
            conexion.close()
            return 'Guardado con éxito' 
        except sqlite3.IntegrityError as e:
            cursor.close()
            conexion.close()
            return 'No se Guardo. El id es único \n{}'.format(e)



#------------------------------------SUCURSAL--------------------------------------------------
class Bd_Sucursal():

    def consultaIdSucursal(self, idx):
        
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM SUCURSAL WHERE ID_SUCURSAL = ?", (idx,))
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        try:
            dato = cursor.fetchall()
            return dato
        except:
            conexion.close()
            return cursor

    

    def idSelect(self):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT ID_SUCURSAL FROM SUCURSAL")
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        try:
            dato = cursor.fetchall()
            return dato
        except:
            conexion.close()
            return cursor
    
    def registro(self, campos):
      
        try:
            conexion = sqlite3.connect(path)
            cursor = conexion.cursor()
            conexion.executemany("INSERT INTO SUCURSAL VALUES (?, ?, ?)", campos)
            conexion.commit()
            cursor.close()
            conexion.close()
            return 'Guardado con éxito' 
        except sqlite3.IntegrityError as e:
            cursor.close()
            conexion.close()
            return 'No se Guardo. El id es único \n{}'.format(e)

        

    def actualiza(self):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM SUCURSAL")
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        dato = cursor.fetchall()
        conexion.close()
        return dato

        
    def updateSucursal(self, datos):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        sql = ''' UPDATE SUCURSAL SET SUC_CIUDAD = ? ,
                  SUC_DIRECCION = ?				  
                WHERE ID_SUCURSAL = ?
        '''
        cursor.execute(sql, datos)
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        conexion.commit()
        conexion.close()
        
    def deleteSucursal(self, datos):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        sql = 'DELETE FROM SUCURSAL WHERE ID_SUCURSAL = ?'
        cursor.execute(sql, (datos,))
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        conexion.commit()
        conexion.close()
#-------------------------------------------------------------------------------------------------------------------
class Clientes():
    

    def idSelect(self):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT ID_CLIENTE FROM CLIENTE")
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        try:
            dato = cursor.fetchall()
            return dato
        except:
            conexion.close()
            return cursor
    
    def registro(self, campos):
      
        try:
            conexion = sqlite3.connect(path)
            cursor = conexion.cursor()
            conexion.executemany("INSERT INTO CLIENTE VALUES (?, ?, ?, ?, ?, ?)", campos)
            conexion.commit()
            cursor.close()
            conexion.close()
            return 'Guardado con éxito' 
        except sqlite3.IntegrityError as e:
            cursor.close()
            conexion.close()
            return 'No se Guardo. El id es único \n{}'.format(e)

        

    def actualiza(self):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM CLIENTE")
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        dato = cursor.fetchall()
        conexion.close()
        return dato

        
    def updateCliente(self, datos):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        sql = ''' UPDATE CLIENTE SET CED_CLIENTE = ? ,
                  NOM_CLIENTE = ?,
                  APE_CLIENTE = ?,
				  COR_CLIENTE = ?,
				  TELF_CLIENTE = ?
              WHERE ID_CLIENTE = ?
        '''
        cursor.execute(sql, datos)
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        conexion.commit()
        conexion.close()
        
    def deleteCliente(self, datos):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        sql = 'DELETE FROM CLIENTE WHERE ID_CLIENTE = ?'
        cursor.execute(sql, (datos,))
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        conexion.commit()
        conexion.close()
#-----------------------------------------------------------------------------------------------------------------------------------------
class Bd_Personal():


   

    def consultaIdPersonal(self, idx):
        
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM PERSONAL WHERE ID_PERSONAL = ?", (idx,))
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        try:
            dato = cursor.fetchall()
            return dato
        except:
            conexion.close()
            return cursor

    

    def idSelect(self):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT ID_PERSONAL FROM PERSONAL")
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        try:
            dato = cursor.fetchall()
            return dato
        except:
            conexion.close()
            return cursor
    
    def registro(self, campos):
      
        try:
            conexion = sqlite3.connect(path)
            cursor = conexion.cursor()
            conexion.executemany("INSERT INTO PERSONAL VALUES (?, ?, ?, ?, ?, ? )", campos)
            conexion.commit()
            cursor.close()
            conexion.close()
            return 'Guardado con éxito' 
        except sqlite3.IntegrityError as e:
            cursor.close()
            conexion.close()
            return 'No se Guardo. El id es único \n{}'.format(e)

        

    def actualiza(self):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM PERSONAL")
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        dato = cursor.fetchall()
        conexion.close()
        return dato

        
    def updatePersonal(self, datos):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        sql = ''' UPDATE PERSONAL SET CED_PERS = ? ,
                  NOM_PERS = ?,
                  APE_PERS = ?,
                  PASS_PERS = ?,
                  ID_SUCURSAL_fk = ?				  
                WHERE ID_PERSONAL = ?
        '''
        cursor.execute(sql, datos)
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        conexion.commit()
        conexion.close()
        
    def deletePersonal(self, datos):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        sql = 'DELETE FROM PERSONAL WHERE ID_PERSONAL = ?'
        cursor.execute(sql, (datos,))
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        conexion.commit()
        conexion.close()
#----------------------------------------LOGIN------------------------------------------------------------
class bdLogin():

    def verificarInicio(self, datos):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT ID_ADMIN, PASS_ADMIN FROM ADMIN WHERE ID_ADMIN = ? ", (datos,))
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        try:
            dato = cursor.fetchall()
            return dato
        except:
            conexion.close()
            return cursor

    def idSelectLogin(self):
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        cursor.execute("SELECT ID_ADMIN FROM ADMIN")
        # Recorremos todo el registro con el método fetchall, devuelve una tupla
        try:
            dato = cursor.fetchall()
            return dato
        except:
            conexion.close()
            return cursor

    def registro(self, campos):
      
        try:
            conexion = sqlite3.connect(path)
            cursor = conexion.cursor()
            conexion.executemany("INSERT INTO ADMIN VALUES (?, ?, ?)", campos)
            conexion.commit()
            cursor.close()
            conexion.close()
            return 'Guardado con éxito' 
        except sqlite3.IntegrityError as e:
            cursor.close()
            conexion.close()
            return 'No se Guardo. El id es único \n{}'.format(e)


#----------------------------------------REGISTRO TABLAS
class RegistroTablas():

    def RTablas(self):    
        
        conexion = sqlite3.connect(path)
        cursor = conexion.cursor()
        # SE CREO LA TABLA SUCURSAL
        

        cursor.execute("CREATE TABLE IF NOT EXISTS SUCURSAL " \
            """(ID_SUCURSAL VARCHAR(10) NOT NULL, 
            SUC_CIUDAD VARCHAR(100) NOT NULL, 
            SUC_DIRECCION VARCHAR(100) NOT NULL, 
            PRIMARY KEY('ID_SUCURSAL'))""")


        cursor.execute("CREATE TABLE IF NOT EXISTS ADMIN" \
            """(ID_ADMIN	VARCHAR(10) NOT NULL,
            PASS_ADMIN	VARCHAR(11) NOT NULL,
            ID_PERSONAL_fk VARCHAR(10) NOT NULL,
            FOREIGN KEY(ID_PERSONAL_fk) REFERENCES PERSONAL(ID_PERSONAL))""");

        # SE CREO TABLA DE PERSONAL
        cursor.execute("CREATE TABLE IF NOT EXISTS PERSONAL" \
            """(ID_PERSONAL	VARCHAR(10) NOT NULL,
            CED_PERS	VARCHAR(11) NOT NULL,
            NOM_PERS	VARCHAR(100) NOT NULL,
            APE_PERS	VARCHAR(100) NOT NULL,
            PASS_PERS	VARCHAR(20) NOT NULL,
            ID_SUCURSAL_fk	VARCHAR(10),
            FOREIGN KEY(ID_SUCURSAL_fk) REFERENCES SUCURSAL(ID_SUCURSAL),
            PRIMARY KEY("ID_PERSONAL"))""");
 
        

        

        

        #SE CREO TABLA ADEREZO
        cursor.execute("CREATE TABLE IF NOT EXISTS ADEREZO" \
            """(ID_ADEREZO	VARCHAR(10) NOT NULL,
            NOM_ADEREZO	VARCHAR(100) NOT NULL,
            VALOR_ADEREZO NUMERIC NOT NULL,
            PRIMARY KEY("ID_ADEREZO"))""");

        #SE CREO TABLA ENVASE
        cursor.execute("CREATE TABLE IF NOT EXISTS ENVASE" \
            """(ID_ENVASE	VARCHAR(10) NOT NULL,
            TIPO_ENVASE	VARCHAR(100) NOT NULL,
            VALOR_ENVASE NUMERIC NOT NULL,
            PRIMARY KEY("ID_ENVASE"))""");

        #SE CREO LA TABLA TAMANIO

        cursor.execute("CREATE TABLE IF NOT EXISTS TAMANIO" \
            """(ID_TAMANIO	VARCHAR(10) NOT NULL,
            TIPO_TAMANIO VARCHAR(100) NOT NULL,
            VALOR_TAMANIO NUMERIC NOT NULL,
            PRIMARY KEY("ID_TAMANIO"))""");

        #SE CREO LA TABLA HELADO
        cursor.execute("CREATE TABLE IF NOT EXISTS PEDIDO" \
            """(ID_HELADO	VARCHAR(10) NOT NULL,
            ID_ENVASE VARCHAR(10) NOT NULL,
            ID_TAMANIO VARCHAR(10) NOT NULL,
            ID_ADEREZO VARCHAR(10) NOT NULL,
            LISTA_ADRZ VARCHAR(100) NOT NULL,
            PRECIO NUMERIC NOT NULL,

            FOREIGN KEY(ID_ENVASE) REFERENCES ENVASE(ID_ENVASE),
            FOREIGN KEY(ID_TAMANIO) REFERENCES TAMANIO(ID_TAMANIO),
            FOREIGN KEY(ID_ADEREZO) REFERENCES ADEREZO(ID_ADEREZO),
            PRIMARY KEY("ID_HELADO"))""");

        #SE CREO LA TABLA CLIENTE
        cursor.execute("CREATE TABLE IF NOT EXISTS CLIENTE" \
            """(ID_CLIENTE	VARCHAR(10) NOT NULL,
            CED_CLIENTE	VARCHAR(11) NOT NULL,
            NOM_CLIENTE	VARCHAR(100) NOT NULL,
            APE_CLIENTE	VARCHAR(100) NOT NULL,
            COR_CLIENTE VARCHAR(20) NOT NULL,
            TELF_CLIENTE VARCHAR(10) NOT NULL,
            PRIMARY KEY("ID_CLIENTE"))""");

        #SE CREO LA TABLA FACTURA
        cursor.execute("CREATE TABLE IF NOT EXISTS FACTURA" \
            """(ID_FACTURA	VARCHAR(10) NOT NULL,
            ID_PERSONAL_fk VARCHAR(10) NOT NULL,
            ID_CLIENTE_fk VARCHAR(10) NOT NULL,
            ID_SUCURSAL_fk VARCHAR(10) NOT NULL,
            FECHA VARCHAR(10) NOT NULL,

            FOREIGN KEY(ID_PERSONAL_fk) REFERENCES PERSONAL(ID_PERSONAL),
            FOREIGN KEY(ID_CLIENTE_fk) REFERENCES CLIENTE(ID_CLIENTE),
            FOREIGN KEY(ID_SUCURSAL_fk) REFERENCES SUCURSAL(ID_SUCURSAL),
            PRIMARY KEY("ID_FACTURA"))""");

        # SE CREO LA TABLA DETALLE_FACTURA

        cursor.execute("CREATE TABLE IF NOT EXISTS DETALLE_FACTURA" \
            """(ID VARCHAR(10) NOT NULL,
            ID_FACTURA_fk VARCHAR(10) NOT NULL,
            ID_HELADO_fk VARCHAR(10) NOT NULL,
            DESCUENTO NUMERIC NOT NULL,
            IVA NUMERIC NOT NULL,
            TOTAL NUMERIC NOT NULL,

            FOREIGN KEY(ID_FACTURA_fk) REFERENCES FACTURA(ID_FACTURA),
            FOREIGN KEY(ID_HELADO_fk) REFERENCES PEDIDO(ID_HELADO_fk),
            PRIMARY KEY("ID"))""");

       

        # Guardamos los cambios haciendo un commit
        conexion.commit()
        conexion.close()

con = RegistroTablas()
con.RTablas()
#print(x)