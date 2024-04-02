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
