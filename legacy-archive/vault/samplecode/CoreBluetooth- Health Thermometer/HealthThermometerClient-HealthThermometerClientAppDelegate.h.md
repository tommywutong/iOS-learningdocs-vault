---
title: 'CoreBluetooth: Health Thermometer'
apple_id: DTS40011370
resource_type: Sample Code
platform: macOS
topic: null
technology: IOBluetooth
published: '2018-03-08'
source_url: https://developer.apple.com/library/archive/samplecode/HealthThermometer/Listings/HealthThermometerClient_HealthThermometerClientAppDelegate_h.html
archived_at: '2026-07-18T03:11:46.357859Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CoreBluetooth: Health Thermometer](CoreBluetooth-%20Health%20Thermometer.md)


[Next](LICENSE.txt.md)[Previous](HealthThermometerClient-HealthThermometerClientAppDelegate.m.md)

# HealthThermometerClient/HealthThermometerClientAppDelegate.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Interface file for Health Thermometer Client app using Bluetooth Low Energy (LE) Health Thermometer Service. This app demonstrats the use of CoreBluetooth APIs for LE devices.
 */

#import <Cocoa/Cocoa.h>
#import <CoreBluetooth/CoreBluetooth.h>

@interface HealthThermometerClientAppDelegate : NSObject <NSApplicationDelegate,CBCentralManagerDelegate, CBPeripheralDelegate> 
{
    NSWindow *window;
    NSWindow *scanSheet;

    NSString * deviceName;
    NSString * manufactureName;
    NSString * tempType;
    NSString * tempString;
    NSString * timeStampString;
    NSString * connectStatus;
    NSString * mesurementType;

    CBCentralManager *manager;
    CBPeripheral *testPeripheral;
    CBCharacteristic * temperatureMeasurementChar;
    CBCharacteristic * intermediateTempChar;

    NSMutableArray *thermometers;
    NSArrayController *arrayController;   
    BOOL autoConnect;

    IBOutlet NSButton * connectButton;
    IBOutlet NSProgressIndicator *progressIndicator;
    IBOutlet NSButton * startStopButton;
}

@property (assign) IBOutlet NSWindow *window;
@property (assign) IBOutlet NSWindow *scanSheet;
@property (copy) NSString* deviceName;
@property (copy) NSString * manufactureName;
@property (copy) NSString* tempType;
@property (copy) NSString* tempString;
@property (copy) NSString* timeStampString;
@property (copy) NSString * connectStatus;
@property (copy) NSString * mesurementType;
@property (retain) CBCharacteristic * temperatureMeasurementChar;
@property (retain) CBCharacteristic * intermediateTempChar;
@property (retain) NSMutableArray *thermometers;
@property (assign) IBOutlet NSArrayController *arrayController;

- (IBAction) openScanSheet:(id) sender;
- (IBAction) closeScanSheet:(id)sender;
- (IBAction) cancelScanSheet:(id)sender;
- (IBAction) connectButtonPressed:(id)sender;
- (IBAction) startButtonPressed:(id)sender;

- (void) startScan;
- (void) stopScan;
- (BOOL) isLECapableHardware;

@end


@interface ThermometerView : NSView
{
}

@end
```

[Next](LICENSE.txt.md)[Previous](HealthThermometerClient-HealthThermometerClientAppDelegate.m.md)

