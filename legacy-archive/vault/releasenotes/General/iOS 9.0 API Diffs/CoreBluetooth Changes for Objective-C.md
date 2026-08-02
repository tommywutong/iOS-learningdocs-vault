---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/CoreBluetooth.html
archived_at: '2026-07-18T02:56:31.363558Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreBluetooth Changes for Objective-C

### CoreBluetooth

#### CBATTRequest.h

Modified [CBATTRequest.central](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518995-central)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, nonatomic) CBCentral *central ``` |
| To | ``` @property(readonly, nonatomic, nonnull) CBCentral *central ``` |

Modified [CBATTRequest.characteristic](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518716-characteristic)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, nonatomic) CBCharacteristic *characteristic ``` |
| To | ``` @property(readonly, nonatomic, nonnull) CBCharacteristic *characteristic ``` |

#### CBCentralManager.h

Removed -[CBCentralManager retrieveConnectedPeripherals]Removed -[CBCentralManager retrievePeripherals:]Removed -[CBCentralManagerDelegate centralManager:didRetrieveConnectedPeripherals:]Removed -[CBCentralManagerDelegate centralManager:didRetrievePeripherals:]Added [CBCentralManager.isScanning](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1620640-isscanning)Modified [-[CBCentralManager connectPeripheral:options:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518766-connect)

|  | Declaration |
| --- | --- |
| From | ``` - (void)connectPeripheral:(CBPeripheral *)peripheral options:(NSDictionary *)options ``` |
| To | ``` - (void)connectPeripheral:(CBPeripheral * _Nonnull)peripheral options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [CBCentralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518944-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, nonatomic) id<CBCentralManagerDelegate> delegate ``` |
| To | ``` @property(assign, nonatomic, nullable) id<CBCentralManagerDelegate> delegate ``` |

Modified [-[CBCentralManager initWithDelegate:queue:options:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1519001-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithDelegate:(id<CBCentralManagerDelegate>)delegate queue:(dispatch_queue_t)queue options:(NSDictionary *)options ``` |
| To | ``` - (instancetype _Nonnull)initWithDelegate:(id<CBCentralManagerDelegate> _Nullable)delegate queue:(dispatch_queue_t _Nullable)queue options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[CBCentralManager retrieveConnectedPeripheralsWithServices:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518924-retrieveconnectedperipheralswith)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)retrieveConnectedPeripheralsWithServices:(NSArray *)serviceUUIDs ``` |
| To | ``` - (NSArray<CBPeripheral *> * _Nonnull)retrieveConnectedPeripheralsWithServices:(NSArray<CBUUID *> * _Nonnull)serviceUUIDs ``` |

Modified [-[CBCentralManager retrievePeripheralsWithIdentifiers:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1519127-retrieveperipheralswithidentifie)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)retrievePeripheralsWithIdentifiers:(NSArray *)identifiers ``` |
| To | ``` - (NSArray<CBPeripheral *> * _Nonnull)retrievePeripheralsWithIdentifiers:(NSArray<NSUUID *> * _Nonnull)identifiers ``` |

Modified [-[CBCentralManager scanForPeripheralsWithServices:options:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518986-scanforperipheralswithservices)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scanForPeripheralsWithServices:(NSArray *)serviceUUIDs options:(NSDictionary *)options ``` |
| To | ``` - (void)scanForPeripheralsWithServices:(NSArray<CBUUID *> * _Nullable)serviceUUIDs options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[CBCentralManagerDelegate centralManager:didDiscoverPeripheral:advertisementData:RSSI:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518937-centralmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)centralManager:(CBCentralManager *)central didDiscoverPeripheral:(CBPeripheral *)peripheral advertisementData:(NSDictionary *)advertisementData RSSI:(NSNumber *)RSSI ``` |
| To | ``` - (void)centralManager:(CBCentralManager * _Nonnull)central didDiscoverPeripheral:(CBPeripheral * _Nonnull)peripheral advertisementData:(NSDictionary<NSString *,id> * _Nonnull)advertisementData RSSI:(NSNumber * _Nonnull)RSSI ``` |

Modified [-[CBCentralManagerDelegate centralManager:willRestoreState:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518819-centralmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)centralManager:(CBCentralManager *)central willRestoreState:(NSDictionary *)dict ``` |
| To | ``` - (void)centralManager:(CBCentralManager * _Nonnull)central willRestoreState:(NSDictionary<NSString *,id> * _Nonnull)dict ``` |

#### CBCharacteristic.h

Removed CBMutableCharacteristic.UUIDModified [CBCharacteristic.descriptors](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518957-descriptors)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) NSArray *descriptors ``` |
| To | ``` @property(retain, readonly, nullable) NSArray<CBDescriptor *> *descriptors ``` |

Modified [CBCharacteristic.service](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518728-service)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, readonly, nonatomic) CBService *service ``` |
| To | ``` @property(assign, readonly, nonatomic, nonnull) CBService *service ``` |

Modified [CBMutableCharacteristic.descriptors](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1518827-descriptors)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readwrite) NSArray *descriptors ``` |
| To | ``` @property(retain, readwrite, nullable) NSArray<CBDescriptor *> *descriptors ``` |

Modified [CBMutableCharacteristic.subscribedCentrals](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1518926-subscribedcentrals)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) NSArray *subscribedCentrals ``` |
| To | ``` @property(retain, readonly, nullable) NSArray<CBCentral *> *subscribedCentrals ``` |

#### CBDescriptor.h

Modified [CBDescriptor.characteristic](https://developer.apple.com/documentation/corebluetooth/cbdescriptor/1519035-characteristic)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, readonly, nonatomic) CBCharacteristic *characteristic ``` |
| To | ``` @property(assign, readonly, nonatomic, nonnull) CBCharacteristic *characteristic ``` |

#### CBError.h

Added [CBErrorConnectionLimitReached](https://developer.apple.com/documentation/corebluetooth/cberror/code/connectionlimitreached)

#### CBPeer.h

Removed CBPeer.UUID

#### CBPeripheral.h

Removed CBPeripheral.isConnectedRemoved [-[CBPeripheralDelegate peripheralDidInvalidateServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1805265-peripheraldidinvalidateservices)Added [-[CBPeripheral maximumWriteValueLengthForType:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1620312-maximumwritevaluelengthfortype)Added [CBPeripheralStateDisconnecting](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate/disconnecting)Modified [CBPeripheral.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518730-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, nonatomic) id<CBPeripheralDelegate> delegate ``` |
| To | ``` @property(assign, nonatomic, nullable) id<CBPeripheralDelegate> delegate ``` |

Modified [-[CBPeripheral discoverCharacteristics:forService:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518797-discovercharacteristics)

|  | Declaration |
| --- | --- |
| From | ``` - (void)discoverCharacteristics:(NSArray *)characteristicUUIDs forService:(CBService *)service ``` |
| To | ``` - (void)discoverCharacteristics:(NSArray<CBUUID *> * _Nullable)characteristicUUIDs forService:(CBService * _Nonnull)service ``` |

Modified [-[CBPeripheral discoverIncludedServices:forService:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519014-discoverincludedservices)

|  | Declaration |
| --- | --- |
| From | ``` - (void)discoverIncludedServices:(NSArray *)includedServiceUUIDs forService:(CBService *)service ``` |
| To | ``` - (void)discoverIncludedServices:(NSArray<CBUUID *> * _Nullable)includedServiceUUIDs forService:(CBService * _Nonnull)service ``` |

Modified [-[CBPeripheral discoverServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518706-discoverservices)

|  | Declaration |
| --- | --- |
| From | ``` - (void)discoverServices:(NSArray *)serviceUUIDs ``` |
| To | ``` - (void)discoverServices:(NSArray<CBUUID *> * _Nullable)serviceUUIDs ``` |

Modified [CBPeripheral.services](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518978-services)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) NSArray *services ``` |
| To | ``` @property(retain, readonly, nullable) NSArray<CBService *> *services ``` |

Modified [-[CBPeripheralDelegate peripheral:didModifyServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518865-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheral:(CBPeripheral *)peripheral didModifyServices:(NSArray *)invalidatedServices ``` |
| To | ``` - (void)peripheral:(CBPeripheral * _Nonnull)peripheral didModifyServices:(NSArray<CBService *> * _Nonnull)invalidatedServices ``` |

#### CBPeripheralManager.h

Modified [CBPeripheralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393313-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, nonatomic) id<CBPeripheralManagerDelegate> delegate ``` |
| To | ``` @property(assign, nonatomic, nullable) id<CBPeripheralManagerDelegate> delegate ``` |

Modified [-[CBPeripheralManager initWithDelegate:queue:options:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393295-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithDelegate:(id<CBPeripheralManagerDelegate>)delegate queue:(dispatch_queue_t)queue options:(NSDictionary *)options ``` |
| To | ``` - (instancetype _Nonnull)initWithDelegate:(id<CBPeripheralManagerDelegate> _Nullable)delegate queue:(dispatch_queue_t _Nullable)queue options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[CBPeripheralManager startAdvertising:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393252-startadvertising)

|  | Declaration |
| --- | --- |
| From | ``` - (void)startAdvertising:(NSDictionary *)advertisementData ``` |
| To | ``` - (void)startAdvertising:(NSDictionary<NSString *,id> * _Nullable)advertisementData ``` |

Modified [-[CBPeripheralManager updateValue:forCharacteristic:onSubscribedCentrals:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393281-updatevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)updateValue:(NSData *)value forCharacteristic:(CBMutableCharacteristic *)characteristic onSubscribedCentrals:(NSArray *)centrals ``` |
| To | ``` - (BOOL)updateValue:(NSData * _Nonnull)value forCharacteristic:(CBMutableCharacteristic * _Nonnull)characteristic onSubscribedCentrals:(NSArray<CBCentral *> * _Nullable)centrals ``` |

Modified [-[CBPeripheralManagerDelegate peripheralManager:didReceiveWriteRequests:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393315-peripheralmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheralManager:(CBPeripheralManager *)peripheral didReceiveWriteRequests:(NSArray *)requests ``` |
| To | ``` - (void)peripheralManager:(CBPeripheralManager * _Nonnull)peripheral didReceiveWriteRequests:(NSArray<CBATTRequest *> * _Nonnull)requests ``` |

Modified [-[CBPeripheralManagerDelegate peripheralManager:willRestoreState:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393317-peripheralmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheralManager:(CBPeripheralManager *)peripheral willRestoreState:(NSDictionary *)dict ``` |
| To | ``` - (void)peripheralManager:(CBPeripheralManager * _Nonnull)peripheral willRestoreState:(NSDictionary<NSString *,id> * _Nonnull)dict ``` |

#### CBService.h

Removed CBMutableService.isPrimaryRemoved CBMutableService.UUIDModified [CBMutableService.characteristics](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/1434317-characteristics)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readwrite) NSArray *characteristics ``` |
| To | ``` @property(retain, readwrite, nullable) NSArray<CBCharacteristic *> *characteristics ``` |

Modified [CBMutableService.includedServices](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/1434320-includedservices)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readwrite) NSArray *includedServices ``` |
| To | ``` @property(retain, readwrite, nullable) NSArray<CBService *> *includedServices ``` |

Modified [CBService.characteristics](https://developer.apple.com/documentation/corebluetooth/cbservice/1434319-characteristics)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) NSArray *characteristics ``` |
| To | ``` @property(retain, readonly, nullable) NSArray<CBCharacteristic *> *characteristics ``` |

Modified [CBService.includedServices](https://developer.apple.com/documentation/corebluetooth/cbservice/1434324-includedservices)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) NSArray *includedServices ``` |
| To | ``` @property(retain, readonly, nullable) NSArray<CBService *> *includedServices ``` |

Modified [CBService.peripheral](https://developer.apple.com/documentation/corebluetooth/cbservice/1434334-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, readonly, nonatomic) CBPeripheral *peripheral ``` |
| To | ``` @property(assign, readonly, nonatomic, nonnull) CBPeripheral *peripheral ``` |

#### CBUUID.h

Removed CBUUIDAppearanceStringRemoved CBUUIDDeviceNameStringRemoved CBUUIDGenericAccessProfileStringRemoved CBUUIDGenericAttributeProfileStringRemoved CBUUIDPeripheralPreferredConnectionParametersStringRemoved CBUUIDPeripheralPrivacyFlagStringRemoved CBUUIDReconnectionAddressStringRemoved CBUUIDServiceChangedStringModified [+[CBUUID UUIDWithCFUUID:]](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518861-uuidwithcfuuid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

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
