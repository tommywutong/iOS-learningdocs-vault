---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/CoreBluetooth.html
archived_at: '2026-07-18T02:55:55.991668Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# CoreBluetooth Changes

## CoreBluetooth

CBAttribute.h (Added)Added [CBAttribute](https://developer.apple.com/documentation/corebluetooth/cbattribute)Added [CBAttribute.UUID](https://developer.apple.com/documentation/corebluetooth/cbattribute/1620638-uuid)CBCentral.hRemoved CBCentral.UUIDRemoved CBCentral.identifierModified [CBCentral](https://developer.apple.com/documentation/corebluetooth/cbcentral)

|  | Protocols | Superclasses |
| --- | --- | --- |
| From | NSCopying | NSObject |
| To | -- | CBPeer |

CBCentralManager.hModified [-[CBCentralManager initWithDelegate:queue:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518695-initwithdelegate)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDelegate:(id<CBCentralManagerDelegate>)delegate queue:(dispatch_queue_t)queue ``` |
| To | ``` - (instancetype)initWithDelegate:(id<CBCentralManagerDelegate>)delegate queue:(dispatch_queue_t)queue ``` |

Modified [-[CBCentralManager initWithDelegate:queue:options:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1519001-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDelegate:(id<CBCentralManagerDelegate>)delegate queue:(dispatch_queue_t)queue options:(NSDictionary *)options ``` |
| To | ``` - (instancetype)initWithDelegate:(id<CBCentralManagerDelegate>)delegate queue:(dispatch_queue_t)queue options:(NSDictionary *)options ``` |

Modified [-[CBCentralManagerDelegate centralManager:didConnectPeripheral:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518969-centralmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBCentralManagerDelegate centralManager:didDisconnectPeripheral:error:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518791-centralmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBCentralManagerDelegate centralManager:didDiscoverPeripheral:advertisementData:RSSI:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518937-centralmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBCentralManagerDelegate centralManager:didFailToConnectPeripheral:error:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518988-centralmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[CBCentralManagerDelegate centralManager:didRetrieveConnectedPeripherals:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified -[CBCentralManagerDelegate centralManager:didRetrievePeripherals:]

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBCentralManagerDelegate centralManager:willRestoreState:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518819-centralmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

CBCharacteristic.hRemoved CBCharacteristic.UUIDModified [CBCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic)

|  | Superclasses |
| --- | --- |
| From | NSObject |
| To | CBAttribute |

Modified [CBCharacteristic.isBroadcasted](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518920-isbroadcasted)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[CBMutableCharacteristic initWithType:properties:value:permissions:]](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1519073-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithType:(CBUUID *)UUID properties:(CBCharacteristicProperties)properties value:(NSData *)value permissions:(CBAttributePermissions)permissions ``` |
| To | ``` - (instancetype)initWithType:(CBUUID *)UUID properties:(CBCharacteristicProperties)properties value:(NSData *)value permissions:(CBAttributePermissions)permissions ``` |

CBDescriptor.hRemoved CBDescriptor.UUIDModified [CBDescriptor](https://developer.apple.com/documentation/corebluetooth/cbdescriptor)

|  | Superclasses |
| --- | --- |
| From | NSObject |
| To | CBAttribute |

Modified [-[CBMutableDescriptor initWithType:value:]](https://developer.apple.com/documentation/corebluetooth/cbmutabledescriptor/1518999-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithType:(CBUUID *)UUID value:(id)value ``` |
| To | ``` - (instancetype)initWithType:(CBUUID *)UUID value:(id)value ``` |

CBPeer.h (Added)Added [CBPeer](https://developer.apple.com/documentation/corebluetooth/cbpeer)Added CBPeer.UUIDAdded [CBPeer.identifier](https://developer.apple.com/documentation/corebluetooth/cbpeer/1620687-identifier)CBPeripheral.hRemoved CBPeripheral.UUIDRemoved CBPeripheral.identifierAdded [-[CBPeripheralDelegate peripheral:didReadRSSI:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1620304-peripheral)Modified [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral)

|  | Protocols | Superclasses |
| --- | --- | --- |
| From | NSCopying | NSObject |
| To | -- | CBPeer |

Modified [CBPeripheral.RSSI](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518869-rssi)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[CBPeripheralDelegate peripheral:didDiscoverCharacteristicsForService:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518821-peripheral)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralDelegate peripheral:didDiscoverDescriptorsForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518785-peripheral)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralDelegate peripheral:didDiscoverIncludedServicesForService:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519124-peripheral)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralDelegate peripheral:didDiscoverServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518744-peripheral)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralDelegate peripheral:didModifyServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518865-peripheral)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralDelegate peripheral:didUpdateNotificationStateForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518768-peripheral)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralDelegate peripheral:didUpdateValueForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518708-peripheral)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralDelegate peripheral:didUpdateValueForDescriptor:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518929-peripheral)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralDelegate peripheral:didWriteValueForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518823-peripheral)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralDelegate peripheral:didWriteValueForDescriptor:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519062-peripheral)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralDelegate peripheralDidInvalidateServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1805265-peripheraldidinvalidateservices)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralDelegate peripheralDidUpdateName:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518801-peripheraldidupdatename)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralDelegate peripheralDidUpdateRSSI:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519083-peripheraldidupdaterssi)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

CBPeripheralManager.hModified [-[CBPeripheralManager initWithDelegate:queue:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393299-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDelegate:(id<CBPeripheralManagerDelegate>)delegate queue:(dispatch_queue_t)queue ``` |
| To | ``` - (instancetype)initWithDelegate:(id<CBPeripheralManagerDelegate>)delegate queue:(dispatch_queue_t)queue ``` |

Modified [-[CBPeripheralManager initWithDelegate:queue:options:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393295-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDelegate:(id<CBPeripheralManagerDelegate>)delegate queue:(dispatch_queue_t)queue options:(NSDictionary *)options ``` |
| To | ``` - (instancetype)initWithDelegate:(id<CBPeripheralManagerDelegate>)delegate queue:(dispatch_queue_t)queue options:(NSDictionary *)options ``` |

Modified [-[CBPeripheralManagerDelegate peripheralManager:central:didSubscribeToCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393261-peripheralmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralManagerDelegate peripheralManager:central:didUnsubscribeFromCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393289-peripheralmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralManagerDelegate peripheralManager:didAddService:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393279-peripheralmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralManagerDelegate peripheralManager:didReceiveReadRequest:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393257-peripheralmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralManagerDelegate peripheralManager:didReceiveWriteRequests:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393315-peripheralmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralManagerDelegate peripheralManager:willRestoreState:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393317-peripheralmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralManagerDelegate peripheralManagerDidStartAdvertising:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393321-peripheralmanagerdidstartadverti)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CBPeripheralManagerDelegate peripheralManagerIsReadyToUpdateSubscribers:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393248-peripheralmanagerisreadytoupdate)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

CBService.hRemoved CBService.UUIDModified [-[CBMutableService initWithType:primary:]](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/1434330-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithType:(CBUUID *)UUID primary:(BOOL)isPrimary ``` |
| To | ``` - (instancetype)initWithType:(CBUUID *)UUID primary:(BOOL)isPrimary ``` |

Modified [CBService](https://developer.apple.com/documentation/corebluetooth/cbservice)

|  | Superclasses |
| --- | --- |
| From | NSObject |
| To | CBAttribute |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
