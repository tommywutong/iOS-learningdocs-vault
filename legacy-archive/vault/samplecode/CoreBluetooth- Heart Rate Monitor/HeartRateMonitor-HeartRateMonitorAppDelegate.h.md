---
title: 'CoreBluetooth: Heart Rate Monitor'
apple_id: DTS40011322
resource_type: Sample Code
platform: macOS
topic: null
technology: IOBluetooth
published: '2018-03-08'
source_url: https://developer.apple.com/library/archive/samplecode/HeartRateMonitor/Listings/HeartRateMonitor_HeartRateMonitorAppDelegate_h.html
archived_at: '2026-07-18T03:11:46.897012Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CoreBluetooth: Heart Rate Monitor](CoreBluetooth-%20Heart%20Rate%20Monitor.md)


[Next](LICENSE.txt.md)[Previous](HeartRateMonitor-ReadMe.md.md)

# HeartRateMonitor/HeartRateMonitorAppDelegate.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Interface file for Heart Rate Monitor app using Bluetooth Low Energy (LE) Heart Rate Service. This app demonstrats the use of CoreBluetooth APIs for LE devices.
 */

#import <Cocoa/Cocoa.h>
#import <CoreBluetooth/CoreBluetooth.h>

@interface HeartRateMonitorAppDelegate : NSObject <NSApplicationDelegate, CBCentralManagerDelegate, CBPeripheralDelegate> 
{
    NSWindow *window;
    NSWindow *scanSheet;
    NSView *heartView;
    NSTimer *pulseTimer;
    NSArrayController *arrayController;

    CBCentralManager *manager;
    CBPeripheral *peripheral;

    NSMutableArray *heartRateMonitors;

    NSString *manufacturer;

    uint16_t heartRate;

    IBOutlet NSButton* connectButton;
    BOOL autoConnect;

    // Progress Indicator
    IBOutlet NSButton * indicatorButton;
    IBOutlet NSProgressIndicator *progressIndicator;    
}

@property (assign) IBOutlet NSWindow *window;
@property (assign) IBOutlet NSWindow *scanSheet;
@property (assign) IBOutlet NSView *heartView;
@property (assign) IBOutlet NSArrayController *arrayController;
@property (assign) uint16_t heartRate;
@property (retain) NSTimer *pulseTimer;
@property (retain) NSMutableArray *heartRateMonitors;
@property (copy) NSString *manufacturer;
@property (copy) NSString *connected;

- (IBAction) openScanSheet:(id) sender;
- (IBAction) closeScanSheet:(id)sender;
- (IBAction) cancelScanSheet:(id)sender;
- (IBAction) connectButtonPressed:(id)sender;

- (void) startScan;
- (void) stopScan;
- (BOOL) isLECapableHardware;

- (void) pulse;
- (void) updateWithHRMData:(NSData *)data;


@end
```

[Next](LICENSE.txt.md)[Previous](HeartRateMonitor-ReadMe.md.md)

