#include <iostream>
#include <string>
using namespace std;
class Carrera {
    private:
    float d_to;
    int dificultad;
public:
    Carrera (float dis_to, int dificultad);
    void Ganar(string d_to, int dificultad);
    void Estado(string d_to, int ganador);
    void Mejor();
};
class Auto {
    private:
    float vMax;
    float ac;
    float tRe;
public:
    Auto(float vMax, float ac) {
        this->vMax = vMax;
        this->ac = ac;
        this->tRe = 0.0f;
    }
void simularCarrera(Carrera carrera) {
    float distanciaRecorrida = 0.0f;
    while (distanciaRecorrida < carrera.getDis_o()) {
        tRe += ac;
        distanciaRecorrida += vMax * tRe;
    }
}
float getTRe() { return tRe; }
};


//2:
#include <iostream>
using namespace std;
class Productos{
public:
    int cod1p;
    int cod1g;
    int cod2p;
    int cod2g;
    int cod3p;
    int cod3g;
    string descrip1p;
    string descrip2p;
    string descrip3p;
    string descrip1g;
    string descrip2g;
    string descrip3g;
    int stock1p;        //STOCK papitas pequeñas
    int stock1g;        //STOCK papitas grandes
    int stock2p;        //stock piqueos pequeños 
    int stock2g;        //stock piqueos grandes
    int stock3p;        //stock cocacolas pequeñas
    int stock3g;        //stock cocacolas grandes
    float precio1p;       // 1 papitas 
    float precio2p;       //2 piqueos
    float precio3p;       // 3 coca cola
    float precio1g;       // g por grande
    float precio2g;       // p por pequeña
    float precio3g;

    Productos(){                               //los atributos se colocan por defecto en priva
        cod1p=1;
        cod1g=2;
        cod2p=3;
        cod2g=4;
        cod3p=5;
        cod3g=6;
        stock1p=10;
        stock1g=10;
        stock2p=10;
        stock2g=10;
        stock3p=10;
        stock3g=10;
        precio1p=1.5;
        precio1g=5;
        precio2p=2;
        precio2g=7;
        precio3p=3;
        precio3g=12;
        descrip1p="bolsa pequeña de papitas  -> contiene 100g";
        descrip1g="bolsa grande de papitas -> contiene 500g";
        descrip2p="bolsa pequeña de piqueos -> contiene 100g";
        descrip2g="bolsa grande de piqueos -> contiene 500g";
        descrip3p="botella pequeña de Coca Cola -> contiene 500 ml";
        descrip3g="botella pequeña de Coca Cola ->  contiene 3 L (litros)";
    }
};

class Pedidos{
   public:
   Productos prodAC;   //produto a comprar
   int cantP1p;
   int cantP1g;
   int cantP2p;
   int cantP2g;
   int cantP3p;
   int cantP3g;
   Pedidos(){
    cantP1p=0;
    cantP1g=0;
    cantP2p=0;
    cantP2g=0;
    cantP3p=0;
    cantP3g=0;
   }

};
class Gestor_inventario{
   public:
   Productos proges;
   int neto1p;
   int neto1g;
   int neto2p;
   int neto2g;
   int neto3p;
   int neto3g;

   Gestor_inventario(){
    neto1g=proges.stock1g;
    neto1p=proges.stock1p;
    neto2p=proges.stock2p;
    neto2g=proges.stock2g;
    neto3p=proges.stock3p;
    neto3g=proges.stock3g;
   }
};

class Reportes{
    public:
    Pedidos gr;
    int ventas1p;
    int ventas1g;
    int ventas2p;
    int ventas2g;
    int ventas3p;
    int ventas3g;
    Reportes(){
        ventas1p=gr.cantP1p;
        ventas1g=gr.cantP1g;
        ventas2p=gr.cantP2p;
        ventas2g=gr.cantP2g;
        ventas3p=gr.cantP3p;
        ventas3g=gr.cantP3g;
    }
};
class Acumulada {
    public:
    Pedidos ac;
    int acu1p;
    int acu1g;
    int acu2p;
    int acu2g;
    int acu3p;
    int acu3g;
    Acumulada(){
        acu1p=0;
        acu1g=0;
        acu2p=0;
        acu2g=0;
        acu3p=0;
        acu3g=0;
    }
};
class Agregar_stock{
    public:
    int agre1p;
    int agre1g;
    int agre2p;
    int agre2g;
    int agre3p;
    int agre3g;
    Agregar_stock(){
        agre1p=0;
        agre1g=0;
        agre2p=0;
        agre2g=0;
        agre3p=0;
        agre3g=0;
    }
};

int main (){
    string x,y,z;
    int a,b,c1p,c1g,c2p,c2g,c3p,c3g,d,k,j;
    c1p,c1g,c2p,c2g,c3p,c3g=0;
    string resp1,resp2,resp3;
    Productos pr1;
    Pedidos pedYa;
    Gestor_inventario inven;
    string repe;
    Acumulada acum;
    Agregar_stock agre;
    repe="si";
    resp3="si";
    while(resp3=="si"){
        while (repe=="si"){
        cout<<"¿Que productos deseas comprar?"<<endl;
        do{
            cout<<"1-papitas"<<endl;
            cout<<"2-piqueos"<<endl;
            cout<<"3-Coca Cola"<<endl;
            cin>>a;
        }while(a<0 or a>3);
        switch (a)
        {
        case 1:
            cout<<"contamos con "<<pr1.stock1p-pedYa.cantP1p<<" "<<pr1.descrip1p<<" con un costo de: "<<pr1.precio1p<<endl;
            cout<<"contamos con "<<pr1.stock1g-pedYa.cantP1g<<" "<<pr1.descrip1g<<" con un costo de: "<<pr1.precio1g<<endl;
            do{
                cout<<"ingrese 1 para comprar: "<<pr1.descrip1p<<endl;
                cout<<"ingrese 2 para comprar: "<<pr1.descrip1g<<endl;
                cin>>b;
            }while(b<0 or b>2);
            switch (b)
            {
            case 1:
                do{
                    cout<<"Elija la cantidad a comprar:";
                    cin>>c1p;
                }while (c1p<0 or c1p>pr1.stock1p);
                acum.acu1p+=c1p;
                pedYa.cantP1p=acum.acu1p;
                inven.neto1p=inven.proges.stock1p-acum.acu1p;
                break;
            case 2:
               do{
                    cout<<"Elija la cantidad a comprar:";
                    cin>>c1g;
                }while (c1g<0 or c1g>pr1.stock1g);
                acum.acu1g+=c1g;
                pedYa.cantP1g=acum.acu1g;
                inven.neto1g=inven.proges.stock1g-acum.acu1g;
                break;
            }
            break;
        case 2:
            cout<<"contamos con "<<pr1.stock2p-pedYa.cantP2p<<" "<<pr1.descrip2p<<" con un costo de: "<<pr1.precio2p<<endl;
            cout<<"contamos con "<<pr1.stock2g-pedYa.cantP2g<<" "<<pr1.descrip2g<<" con un costo de: "<<pr1.precio2g<<endl;
            do{
                cout<<"ingrese 1 para comprar: "<<pr1.descrip2p<<endl;
                cout<<"ingrese 2 para comprar: "<<pr1.descrip2g<<endl;
                cin>>b;
            }while(b<0 or b>2);
            switch (b)
            {
            case 1:
                do{
                    cout<<"Elija la cantidad a comprar:";
                    cin>>c2p;
                }while (c2p<0 or c2p>pr1.stock2p);
                acum.acu2p+=c2p;
                pedYa.cantP2p=acum.acu2p;
                inven.neto2p=inven.proges.stock2p-acum.acu2p;
                break;
            case 2:
                do{
                    cout<<"Elija la cantidad a comprar:";
                    cin>>c2g;
                }while (c2g<0 or c2g>pr1.stock2g);
                acum.acu2g+=c2g;
                pedYa.cantP2g=acum.acu2g;
                inven.neto2g=inven.proges.stock2g-acum.acu2g;
                break;    
            }
            break;
        case 3:
            cout<<"contamos con "<<pr1.stock3p-pedYa.cantP3p<<" "<<pr1.descrip3p<<" con un costo de: "<<pr1.precio3p<<endl;
            cout<<"contamos con "<<pr1.stock3g-pedYa.cantP3g<<" "<<pr1.descrip3g<<" con un costo de: "<<pr1.precio3g<<endl;
            do{
                cout<<"ingrese 1 para comprar: "<<pr1.descrip3p<<endl;
                cout<<"ingrese 2 para comprar: "<<pr1.descrip3g<<endl;
                cin>>b;
            }while(b<0 or b>2);
            switch (b)
            {
            case 1:
                do{
                    cout<<"Elija la cantidad a comprar:";
                    cin>>c3p;
                }while (c3p<0 or c3p>pr1.stock3p);
                acum.acu3p+=c3p;
                pedYa.cantP3p=acum.acu3p;
                inven.neto3p=inven.proges.stock3p-acum.acu3p;
                break;
            case 2:
                do{
                    cout<<"Elija la cantidad a comprar:";
                    cin>>c3g;
                }while (c3g<0 or c3g>pr1.stock3g);
                acum.acu3g+=c3g;
                pedYa.cantP3g=acum.acu3g;
                inven.neto3g=inven.proges.stock3g-acum.acu3g;

                break;
            }    
            break;
        }
        cout<<"desea volver a comprar ?"<<endl;
        cin>>repe;
    }
    cout<<"desa ingresar como administrador?"<<endl;
    cin>>x;
    if (x=="si"){
        cout<<"ingrese la clave"<<endl;     //la clave es 123
        cin>>y;
        if (y=="123"){
            cout<<"¿Desea saber cuantos objetos hay en el inventario? ";
            cin>>resp1;
            if (resp1=="si"){
                cout<<"hay "<<inven.neto1p+agre.agre1p<<" "<<pr1.descrip1p<<endl;
                cout<<"hay "<<inven.neto1g+agre.agre1g<<" "<<pr1.descrip1g<<endl;
                cout<<"hay "<<inven.neto2p+agre.agre2p<<" "<<pr1.descrip2p<<endl;
                cout<<"hay "<<inven.neto2g+agre.agre2g<<" "<<pr1.descrip2g<<endl;
                cout<<"hay "<<inven.neto3p+agre.agre3p<<" "<<pr1.descrip3p<<endl;
                cout<<"hay "<<inven.neto3g+agre.agre3g<<" "<<pr1.descrip3g<<endl;
                }
            cout<<"La empresa desea ver las ventas del dia?"<<endl;
            cin>>resp2;
            if (resp2=="si"){
                cout<<"el stock inicial de"<<pr1.descrip1p<<" fue: "<<pr1.stock1p<<" y los productos vendidos fueron: "<<pedYa.cantP1p<<endl;
                cout<<"el stock inicial de"<<pr1.descrip1g<<" fue: "<<pr1.stock1g<<" y los productos vendidos fueron: "<<pedYa.cantP1g<<endl;
                cout<<"el stock inicial de"<<pr1.descrip2p<<" fue: "<<pr1.stock2p<<" y los productos vendidos fueron: "<<pedYa.cantP2p<<endl;
                cout<<"el stock inicial de"<<pr1.descrip2g<<" fue: "<<pr1.stock2g<<" y los productos vendidos fueron: "<<pedYa.cantP2g<<endl;
                cout<<"el stock inicial de"<<pr1.descrip3p<<" fue: "<<pr1.stock3p<<" y los productos vendidos fueron: "<<pedYa.cantP3p<<endl;
                cout<<"el stock inicial de"<<pr1.descrip3g<<" fue: "<<pr1.stock3g<<" y los productos vendidos fueron: "<<pedYa.cantP3g<<endl;
                }
            cout<<"¿desea agregar productos a la tienda?"<<endl;
            cin>>z;
            if (z=="si"){
                cout<<"¿que produto desea agregar al inventario?"<<endl;
                cout<<"1->"<<pr1.descrip1p<<endl;
                cout<<"2->"<<pr1.descrip1g<<endl;
                cout<<"3->"<<pr1.descrip2p<<endl;
                cout<<"4->"<<pr1.descrip2g<<endl;
                cout<<"5->"<<pr1.descrip3p<<endl;
                cout<<"6->"<<pr1.descrip3g<<endl;
                cin>>k;
            switch (k)
            {
            case 1:
                cout<<"ingrese la cantidad que agregara"<<endl;
                cin>>j;
                agre.agre1p=j;
                pr1.stock1p=inven.neto1p+agre.agre1p;
                break;
            case 2:
                cout<<"ingrese la cantidad que agregara"<<endl;
                cin>>j;
                agre.agre1g=j;
                pr1.stock1g=inven.neto1g+agre.agre1g;
                break;
            case 3:
                cout<<"ingrese la cantidad que agregara"<<endl;
                cin>>j;
                agre.agre2p=j;
                pr1.stock2p=inven.neto2p+agre.agre2p;
                break;
            case 4:
                cout<<"ingrese la cantidad que agregara"<<endl;
                cin>>j;
                agre.agre2g=j;
                pr1.stock2g=inven.neto2g+agre.agre2g;
                break;
            case 5:
                cout<<"ingrese la cantidad que agregara"<<endl;
                cin>>j;
                agre.agre3p=j;
                pr1.stock3p=inven.neto3p+agre.agre3p;
                break;
            case 6:
                cout<<"ingrese la cantidad que agregara"<<endl;
                cin>>j;
                agre.agre3g=j;
                pr1.stock3g=inven.neto3g+agre.agre3g;
                break;
                }
            }
        }
    }
    cout<<"¿desea que por motivos de ver si se aumento el stock se repita?"<<endl;
        cin>>resp3;
    }
    return 0;
}
