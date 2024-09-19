#include "drone_deliver.h"

DroneDelivery::DroneDelivery() {
    PilotArdu.init();  // Inicializa o sistema ArduPilot
}

DroneDelivery::~DroneDelivery() {
    // Libera recursos, se necessário
}

void DroneDelivery::init() {
    std::cout << "Inicializando sistema de entrega..." << std::endl;
  // Inicializa motores, sensores e sistema de navegação
}

void DroneDelivery::takeoff() {
    PilotArdu.armMotors();
  PilotArdu.takeoff(10);  // Decolagem para 10 metros de altitude
}

void DroneDelivery::land() {
    PilotArdu.land(); //Iniciando pouso
}

void DroneDelivery::returnToBase() {
    PilotArdu.goTo(); // Coordenadas da base 
  land();
}