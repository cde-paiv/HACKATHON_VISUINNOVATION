#ifndef DRONE_DELIVER_H
#define DRONE_DELIVER_H

#include <PilotArdu.h>
#include <MVSDK.h>
#include <vector>
#include <iostream>

enum DroneAction {
  TAKEOFF,
  FLYTOA,
  FLYTOB,
  FLYTOC,
  FLYTOD,
  FLYTOE,
  DELIVER_PACKAGE,
  RETURN_TO_HOME,
  LAND,
  AVOID_OBSTACLE
};

class DroneDelivery {
public:
  DroneDelivery();
  ~DroneDelivery();

  void init();                                    
  void processCommand(DroneAction action); 
  void monitorBattery();
  void detectObstacles();
  void executeDelivery(double lat, double lon);

private:
  void takeoff();            
  void land();               
  void returnToBase();
  void avoidObstacle();
  bool checkLandingZone();     
  double getBatteryVoltage(); 
};

#endif