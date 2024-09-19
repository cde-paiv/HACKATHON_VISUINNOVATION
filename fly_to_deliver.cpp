#include "drone_deliver.h"

void DroneDelivery::processCommand(DroneAction action) {
    switch (action) {
    case TAKEOFF:
      takeoff();
      break;
    case LAND:
      land();
      break;
    case DELIVER_PACKAGE: {
      int destination = getDestination(); // Função que retorna 1 para A, 2 para B, etc.
      switch (destination) {
        case 1:
          flyFromBaseToA();
          break;
        case 2:
          flyFromBaseToB();
          break;
        case 3:
          flyFromBaseToC();
          break;
        case 4:
          flyFromBaseToD();
          break;
        case 5:
          flyFromBaseToE();
          break;
        default:
          std::cout << "Destino inválido!" << std::endl;
          break;
      }
      break;
    }
    case RETURN_TO_BASE:
      returnToBase();
      break;
    case AVOID_OBSTACLE:
      avoidObstacle();
      break;
  }
}

int DroneDelivery::getDestination() {
    // Função que obtém o destino do comando do usuario
    int destination;
  std::cout << "Escolha o destino (1=A, 2=B, 3=C, 4=D, 5=E): ";
  std::cin >> destination; // Captura a entrada do usuário
  return destination;
}

void DroneDelivery::returnToBase() {
  std::cout << "Retornando para a Base..." << std::endl;
  double latBase = ; // Latitude da Base
  double lonBase = ; // Longitude da Base
  
  PilotArdu.goTo(latBase, lonBase); // Navega para a Base
  if (checkLandingZone()) {
    land(); // Pousa se a zona estiver livre
  } else {
    std::cout << "Zona de aterragem na Base ocupada. Esperando..." << std::endl;
  }
}

void DroneDelivery::flyFromBaseToA() {
  std::cout << "Voando da Base para a posição A..." << std::endl;
  double latA = ; // Latitude da posição A
  double lonA = ; // Longitude da posição A
  
  PilotArdu.goTo(latA, lonA); // Navega da Base para a posição A
  if (checkLandingZone()) {
    land(); // Pousa se a zona estiver livre
  } else {
    std::cout << "Zona de aterragem em A ocupada. Esperando..." << std::endl;
  }
}


