---
title: BTLE Central Peripheral Transfer
apple_id: DTS40012927
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreBluetooth
published: '2012-11-15'
source_url: https://developer.apple.com/library/archive/samplecode/BTLE_Transfer/Introduction/Intro.html
archived_at: '2026-07-18T03:01:40.956363Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](BTLE%20Transfer-AppDelegate.h.md)

# BTLE Central Peripheral Transfer

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2012-11-15 This sample shows how to transfer data using CoreBluetooth's Peripheral and Central modes. |
| __Build Requirements:__ | Xcode 4.5 with iOS 6 SDK |
| __Runtime Requirements:__ | iOS 6 |

This sample shows how to transfer data from an iOS device in CoreBluetooth Peripheral Mode to another in Central Mode, by using a CBCharacteristic on the Peripheral side that changes its value. The value change is automatically picked up on the Central side.

This sample shows how to handle flow control in this scenario.

It also covers a rudimentary way of connecting two devices using the RSSI value as an approximation of distance between them.

[Next](BTLE%20Transfer-AppDelegate.h.md)

