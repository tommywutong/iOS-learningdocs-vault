---
title: 'AirLocate: Using CoreLocation to monitor, range, and configure your device
  as an iBeacon'
apple_id: DTS40013430
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreLocation
published: '2014-01-06'
source_url: https://developer.apple.com/library/archive/samplecode/AirLocate/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:00:56.212090Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AirLocate: Using CoreLocation to monitor, range, and configure your device as an iBeacon](AirLocate-%20Using%20CoreLocation%20to%20monitor%2C%20range%2C%20and%20configure%20your%20device%20as%20an.md)


[Next](AirLocate-APLAppDelegate.h.md)[Previous](AirLocate-%20Using%20CoreLocation%20to%20monitor%2C%20range%2C%20and%20configure%20your%20device%20as%20an.md)

# ReadMe.txt

```

AirLocate
=========

AirLocate shows how to use CLLocationManager to monitor and range CLBeaconRegions.
The code also provides an example of how you can calibrate and configure an iOS device as a beacon with CoreBluetooth.

You can configure an iOS device as a beacon as follows:

1) Obtain two iOS devices equipped with Bluetooth LE. One will be a target device, one will be a remote (calibration) device.
2) Load and launch this app on both devices.
3) Turn the target device into a beacon by selecting Configuration and turning on the Enabled switch.
4) Take the calibration device and move one meter away from the target device.
5) On the calibration device start the calibration process by selecting Calibration.
6) Choose the target device from the table view.
7) The calibration process will start. You should wave the calibration device from side-to-side while this process is running.
8) When the calibration process is done, it will show a calibrated RSSI value on the screen.
9) On the target device, go back to the Configuration screen and enter this value under Measured Power.

Note: The calibration process is optional, but recommended as it will fine-tune ranging for your environment.
You can configure an iOS device as a beacon without calibrating it by not specifying a measured power.
If a measured power is not specified, CoreLocation default to a pre-determined value.

Once you've setup your target device as a beacon, you can use this app to demo beacon ranging and monitoring.
To demo ranging, select Ranging from the remote device. ALRangingViewController ranges a set of CLBeaconRegions.
To demo monitoring, select Monitoring from the remote device. ALMonitoringViewController allows you to configure a CLBeaconRegion to monitor.


AirLocate is best viewed on an iPhone

===========================================================================
PACKAGING LIST:

ALCalibrationBeginViewController
ALCalibrationEndViewController

- View controllers for calibrating the measured power of a beacon.
- ALCalibrationBeginViewController allows you to choose a beacon to calibrate.
- ALCalibrationEndViewController shows you the calibrated measured power value for the chosen beacon.

ALCalibrationCalculator

- Calculates the measured power value for a chosen beacon.

ALConfigurationViewController

- View controller to configure the iOS device as a beacon.

ALMonitoringViewController

- View controller to monitor a specific beacon region.

ALRangingViewController

- View controller ranges a set of known beacon regions.


===========================================================================
Copyright (C) 2013 Apple Inc. All rights reserved.
```

[Next](AirLocate-APLAppDelegate.h.md)[Previous](AirLocate-%20Using%20CoreLocation%20to%20monitor%2C%20range%2C%20and%20configure%20your%20device%20as%20an.md)

