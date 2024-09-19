#include "drone_deliver.h"

void DroneDelivery::avoidObstacle() {
    // criar logica para desviar o drone usando sensores de visão
}


void DroneDelivery::detectObstacles() {
    MVSDK::Image image = MVSDK::CaptureImage();
  if (MVSDK::DetectObstacle(image)) {
    avoidObstacle();
  }
}

void DroneDelivery::monitorBattery() {
     double voltage = getBatteryVoltage();
  if (voltage < 30) {
    returnToBase();
  }
}

double DroneDelivery::getBatteryVoltage() {
    return PilotArdu.getBatteryVoltage();
}

