#include "drone_deliver.h"

bool DroneDelivery::checkLandingZone() {
    MVSDK::Image image = MVSDK::CaptureImage();
  return !MVSDK::DetectObstacle(image);  // Retorna true se a zona estiver livre
}

void DroneDelivery::executeDelivery(double lat, double lon) {
    std::cout << "Executando entrega na coordenada: " << lat << ", " << lon << std::endl;
  PilotArdu.goTo(lat, lon);  // Navega até o local de entrega
  if (checkLandingZone()) {
    land();
  } else {
    std::cout << "Zona de aterragem ocupada, esperando..." << std::endl;
  }
}