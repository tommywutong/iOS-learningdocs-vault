---
title: EADemo
apple_id: DTS40010079
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: ExternalAccessory
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/EADemo/Listings/EADemo_EADSessionController_h.html
archived_at: '2026-07-18T03:07:28.022569Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [EADemo](EADemo.md)


[Next](EADemo-EADSessionController.m.md)[Previous](EADemo-AppDelegate.h.md)

# EADemo/EADSessionController.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Provides an interface for communication with an EASession. Also the delegate for the EASession input and output stream objects.
 */

@import Foundation;
@import ExternalAccessory;

extern NSString *EADSessionDataReceivedNotification;

// NOTE: EADSessionController is not threadsafe, calling methods from different threads will lead to unpredictable results
@interface EADSessionController : NSObject <EAAccessoryDelegate, NSStreamDelegate>

+ (EADSessionController *)sharedController;

- (void)setupControllerForAccessory:(EAAccessory *)accessory withProtocolString:(NSString *)protocolString;

- (BOOL)openSession;
- (void)closeSession;

- (void)writeData:(NSData *)data;

- (NSUInteger)readBytesAvailable;
- (NSData *)readData:(NSUInteger)bytesToRead;

@property (nonatomic, readonly) EAAccessory *accessory;
@property (nonatomic, readonly) NSString *protocolString;

@end
```

[Next](EADemo-EADSessionController.m.md)[Previous](EADemo-AppDelegate.h.md)

