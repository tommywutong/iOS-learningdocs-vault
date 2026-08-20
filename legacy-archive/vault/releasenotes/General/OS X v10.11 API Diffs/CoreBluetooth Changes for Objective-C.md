---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CoreBluetooth.html
archived_at: '2026-07-18T02:52:57.626559Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreBluetooth Changes for Objective-C

### CoreBluetooth

#### CBATTRequest.h

Modified [CBATTRequest.central](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518995-central)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, nonatomic) CBCentral *central ``` |
| To | ``` @property(readonly, retain, nonatomic, nonnull) CBCentral *central ``` |

Modified [CBATTRequest.characteristic](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518716-characteristic)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, nonatomic) CBCharacteristic *characteristic ``` |
| To | ``` @property(readonly, retain, nonatomic, nonnull) CBCharacteristic *characteristic ``` |

Modified [CBATTRequest.value](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518795-value)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) NSData *value ``` |
| To | ``` @property(readwrite, copy, nullable) NSData *value ``` |

#### CBCentral.h

Modified CBCentral.identifier

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSUUID *identifier ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSUUID *identifier ``` |

Modified CBCentral.UUID

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CFUUIDRef UUID ``` |
| To | ``` @property(readonly, nonatomic, nonnull) CFUUIDRef UUID ``` |

#### CBCentralManager.h

Modified [-[CBCentralManager cancelPeripheralConnection:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518952-cancelperipheralconnection)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cancelPeripheralConnection:(CBPeripheral *)peripheral ``` |
| To | ``` - (void)cancelPeripheralConnection:(CBPeripheral * _Nonnull)peripheral ``` |

Modified [-[CBCentralManager connectPeripheral:options:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518766-connect)

|  | Declaration |
| --- | --- |
| From | ``` - (void)connectPeripheral:(CBPeripheral *)peripheral options:(NSDictionary *)options ``` |
| To | ``` - (void)connectPeripheral:(CBPeripheral * _Nonnull)peripheral options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [CBCentralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518944-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) id<CBCentralManagerDelegate> delegate ``` |
| To | ``` @property(assign, nonatomic, nullable) id<CBCentralManagerDelegate> delegate ``` |

Modified [-[CBCentralManager initWithDelegate:queue:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518695-initwithdelegate)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDelegate:(id<CBCentralManagerDelegate>)delegate queue:(dispatch_queue_t)queue ``` |
| To | ``` - (id _Nonnull)initWithDelegate:(id<CBCentralManagerDelegate> _Nullable)delegate queue:(dispatch_queue_t _Nullable)queue ``` |

Modified [-[CBCentralManager initWithDelegate:queue:options:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1519001-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDelegate:(id<CBCentralManagerDelegate>)delegate queue:(dispatch_queue_t)queue options:(NSDictionary *)options ``` |
| To | ``` - (id _Nonnull)initWithDelegate:(id<CBCentralManagerDelegate> _Nullable)delegate queue:(dispatch_queue_t _Nullable)queue options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[CBCentralManager retrieveConnectedPeripheralsWithServices:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518924-retrieveconnectedperipheralswith)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)retrieveConnectedPeripheralsWithServices:(NSArray *)serviceUUIDs ``` |
| To | ``` - (NSArray<CBPeripheral *> * _Nonnull)retrieveConnectedPeripheralsWithServices:(NSArray<CBUUID *> * _Nonnull)serviceUUIDs ``` |

Modified -[CBCentralManager retrievePeripherals:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)retrievePeripherals:(NSArray *)peripheralUUIDs ``` |
| To | ``` - (void)retrievePeripherals:(NSArray * _Nonnull)peripheralUUIDs ``` |

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

Modified [-[CBCentralManagerDelegate centralManager:didConnectPeripheral:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518969-centralmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)centralManager:(CBCentralManager *)central didConnectPeripheral:(CBPeripheral *)peripheral ``` |
| To | ``` - (void)centralManager:(CBCentralManager * _Nonnull)central didConnectPeripheral:(CBPeripheral * _Nonnull)peripheral ``` |

Modified [-[CBCentralManagerDelegate centralManager:didDisconnectPeripheral:error:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518791-centralmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)centralManager:(CBCentralManager *)central didDisconnectPeripheral:(CBPeripheral *)peripheral error:(NSError *)error ``` |
| To | ``` - (void)centralManager:(CBCentralManager * _Nonnull)central didDisconnectPeripheral:(CBPeripheral * _Nonnull)peripheral error:(NSError * _Nullable)error ``` |

Modified [-[CBCentralManagerDelegate centralManager:didDiscoverPeripheral:advertisementData:RSSI:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518937-centralmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)centralManager:(CBCentralManager *)central didDiscoverPeripheral:(CBPeripheral *)peripheral advertisementData:(NSDictionary *)advertisementData RSSI:(NSNumber *)RSSI ``` |
| To | ``` - (void)centralManager:(CBCentralManager * _Nonnull)central didDiscoverPeripheral:(CBPeripheral * _Nonnull)peripheral advertisementData:(NSDictionary<NSString *,id> * _Nonnull)advertisementData RSSI:(NSNumber * _Nonnull)RSSI ``` |

Modified [-[CBCentralManagerDelegate centralManager:didFailToConnectPeripheral:error:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518988-centralmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)centralManager:(CBCentralManager *)central didFailToConnectPeripheral:(CBPeripheral *)peripheral error:(NSError *)error ``` |
| To | ``` - (void)centralManager:(CBCentralManager * _Nonnull)central didFailToConnectPeripheral:(CBPeripheral * _Nonnull)peripheral error:(NSError * _Nullable)error ``` |

Modified -[CBCentralManagerDelegate centralManager:didRetrieveConnectedPeripherals:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)centralManager:(CBCentralManager *)central didRetrieveConnectedPeripherals:(NSArray *)peripherals ``` |
| To | ``` - (void)centralManager:(CBCentralManager * _Nonnull)central didRetrieveConnectedPeripherals:(NSArray<CBPeripheral *> * _Nonnull)peripherals ``` |

Modified -[CBCentralManagerDelegate centralManager:didRetrievePeripherals:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)centralManager:(CBCentralManager *)central didRetrievePeripherals:(NSArray *)peripherals ``` |
| To | ``` - (void)centralManager:(CBCentralManager * _Nonnull)central didRetrievePeripherals:(NSArray<CBPeripheral *> * _Nonnull)peripherals ``` |

Modified [-[CBCentralManagerDelegate centralManager:willRestoreState:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518819-centralmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)centralManager:(CBCentralManager *)central willRestoreState:(NSDictionary *)dict ``` |
| To | ``` - (void)centralManager:(CBCentralManager * _Nonnull)central willRestoreState:(NSDictionary<NSString *,id> * _Nonnull)dict ``` |

Modified [-[CBCentralManagerDelegate centralManagerDidUpdateState:]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518888-centralmanagerdidupdatestate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)centralManagerDidUpdateState:(CBCentralManager *)central ``` |
| To | ``` - (void)centralManagerDidUpdateState:(CBCentralManager * _Nonnull)central ``` |

#### CBCharacteristic.h

Modified [CBCharacteristic.descriptors](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518957-descriptors)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) NSArray *descriptors ``` |
| To | ``` @property(retain, readonly, nullable) NSArray<CBDescriptor *> *descriptors ``` |

Modified [CBCharacteristic.service](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518728-service)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, readonly, nonatomic) CBService *service ``` |
| To | ``` @property(assign, readonly, nonatomic, nonnull) CBService *service ``` |

Modified CBCharacteristic.UUID

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CBUUID *UUID ``` |
| To | ``` @property(readonly, nonatomic, nonnull) CBUUID *UUID ``` |

Modified [CBCharacteristic.value](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518878-value)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) NSData *value ``` |
| To | ``` @property(retain, readonly, nullable) NSData *value ``` |

Modified [CBMutableCharacteristic.descriptors](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1518827-descriptors)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readwrite) NSArray *descriptors ``` |
| To | ``` @property(retain, readwrite, nullable) NSArray<CBDescriptor *> *descriptors ``` |

Modified [-[CBMutableCharacteristic initWithType:properties:value:permissions:]](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1519073-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithType:(CBUUID *)UUID properties:(CBCharacteristicProperties)properties value:(NSData *)value permissions:(CBAttributePermissions)permissions ``` |
| To | ``` - (id _Nonnull)initWithType:(CBUUID * _Nullable)UUID properties:(CBCharacteristicProperties)properties value:(NSData * _Nullable)value permissions:(CBAttributePermissions)permissions ``` |

Modified [CBMutableCharacteristic.subscribedCentrals](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1518926-subscribedcentrals)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) NSArray *subscribedCentrals ``` |
| To | ``` @property(retain, readonly, nullable) NSArray<CBCentral *> *subscribedCentrals ``` |

Modified CBMutableCharacteristic.UUID

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readwrite, nonatomic) CBUUID *UUID ``` |
| To | ``` @property(retain, readwrite, nonatomic, nullable) CBUUID *UUID ``` |

Modified [CBMutableCharacteristic.value](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1519121-value)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readwrite) NSData *value ``` |
| To | ``` @property(retain, readwrite, nullable) NSData *value ``` |

#### CBDescriptor.h

Modified [CBDescriptor.characteristic](https://developer.apple.com/documentation/corebluetooth/cbdescriptor/1519035-characteristic)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, readonly, nonatomic) CBCharacteristic *characteristic ``` |
| To | ``` @property(assign, readonly, nonatomic, nonnull) CBCharacteristic *characteristic ``` |

Modified CBDescriptor.UUID

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CBUUID *UUID ``` |
| To | ``` @property(readonly, nonatomic, nonnull) CBUUID *UUID ``` |

Modified [CBDescriptor.value](https://developer.apple.com/documentation/corebluetooth/cbdescriptor/1518778-value)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) id value ``` |
| To | ``` @property(retain, readonly, nullable) id value ``` |

Modified [-[CBMutableDescriptor initWithType:value:]](https://developer.apple.com/documentation/corebluetooth/cbmutabledescriptor/1518999-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithType:(CBUUID *)UUID value:(id)value ``` |
| To | ``` - (id _Nonnull)initWithType:(CBUUID * _Nonnull)UUID value:(id _Nullable)value ``` |

#### CBError.h

Added CBErrorMaxConnection

#### CBPeripheral.h

Modified [CBPeripheral.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518730-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) id<CBPeripheralDelegate> delegate ``` |
| To | ``` @property(assign, nonatomic, nullable) id<CBPeripheralDelegate> delegate ``` |

Modified [-[CBPeripheral discoverCharacteristics:forService:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518797-discovercharacteristics)

|  | Declaration |
| --- | --- |
| From | ``` - (void)discoverCharacteristics:(NSArray *)characteristicUUIDs forService:(CBService *)service ``` |
| To | ``` - (void)discoverCharacteristics:(NSArray<CBUUID *> * _Nullable)characteristicUUIDs forService:(CBService * _Nonnull)service ``` |

Modified [-[CBPeripheral discoverDescriptorsForCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519070-discoverdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` - (void)discoverDescriptorsForCharacteristic:(CBCharacteristic *)characteristic ``` |
| To | ``` - (void)discoverDescriptorsForCharacteristic:(CBCharacteristic * _Nonnull)characteristic ``` |

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

Modified CBPeripheral.identifier

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSUUID *identifier ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSUUID *identifier ``` |

Modified [CBPeripheral.name](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519029-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) NSString *name ``` |
| To | ``` @property(retain, readonly, nullable) NSString *name ``` |

Modified [-[CBPeripheral readValueForCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518759-readvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)readValueForCharacteristic:(CBCharacteristic *)characteristic ``` |
| To | ``` - (void)readValueForCharacteristic:(CBCharacteristic * _Nonnull)characteristic ``` |

Modified [-[CBPeripheral readValueForDescriptor:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518789-readvaluefordescriptor)

|  | Declaration |
| --- | --- |
| From | ``` - (void)readValueForDescriptor:(CBDescriptor *)descriptor ``` |
| To | ``` - (void)readValueForDescriptor:(CBDescriptor * _Nonnull)descriptor ``` |

Modified [CBPeripheral.RSSI](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518869-rssi)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) NSNumber *RSSI ``` |
| To | ``` @property(retain, readonly, nullable) NSNumber *RSSI ``` |

Modified [CBPeripheral.services](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518978-services)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) NSArray *services ``` |
| To | ``` @property(retain, readonly, nullable) NSArray<CBService *> *services ``` |

Modified [-[CBPeripheral setNotifyValue:forCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518949-setnotifyvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setNotifyValue:(BOOL)enabled forCharacteristic:(CBCharacteristic *)characteristic ``` |
| To | ``` - (void)setNotifyValue:(BOOL)enabled forCharacteristic:(CBCharacteristic * _Nonnull)characteristic ``` |

Modified CBPeripheral.UUID

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CFUUIDRef UUID ``` |
| To | ``` @property(readonly, nonatomic, nonnull) CFUUIDRef UUID ``` |

Modified [-[CBPeripheral writeValue:forCharacteristic:type:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518747-writevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)writeValue:(NSData *)data forCharacteristic:(CBCharacteristic *)characteristic type:(CBCharacteristicWriteType)type ``` |
| To | ``` - (void)writeValue:(NSData * _Nonnull)data forCharacteristic:(CBCharacteristic * _Nonnull)characteristic type:(CBCharacteristicWriteType)type ``` |

Modified [-[CBPeripheral writeValue:forDescriptor:]](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519107-writevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)writeValue:(NSData *)data forDescriptor:(CBDescriptor *)descriptor ``` |
| To | ``` - (void)writeValue:(NSData * _Nonnull)data forDescriptor:(CBDescriptor * _Nonnull)descriptor ``` |

Modified [-[CBPeripheralDelegate peripheral:didDiscoverCharacteristicsForService:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518821-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheral:(CBPeripheral *)peripheral didDiscoverCharacteristicsForService:(CBService *)service error:(NSError *)error ``` |
| To | ``` - (void)peripheral:(CBPeripheral * _Nonnull)peripheral didDiscoverCharacteristicsForService:(CBService * _Nonnull)service error:(NSError * _Nullable)error ``` |

Modified [-[CBPeripheralDelegate peripheral:didDiscoverDescriptorsForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518785-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheral:(CBPeripheral *)peripheral didDiscoverDescriptorsForCharacteristic:(CBCharacteristic *)characteristic error:(NSError *)error ``` |
| To | ``` - (void)peripheral:(CBPeripheral * _Nonnull)peripheral didDiscoverDescriptorsForCharacteristic:(CBCharacteristic * _Nonnull)characteristic error:(NSError * _Nullable)error ``` |

Modified [-[CBPeripheralDelegate peripheral:didDiscoverIncludedServicesForService:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519124-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheral:(CBPeripheral *)peripheral didDiscoverIncludedServicesForService:(CBService *)service error:(NSError *)error ``` |
| To | ``` - (void)peripheral:(CBPeripheral * _Nonnull)peripheral didDiscoverIncludedServicesForService:(CBService * _Nonnull)service error:(NSError * _Nullable)error ``` |

Modified [-[CBPeripheralDelegate peripheral:didDiscoverServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518744-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheral:(CBPeripheral *)peripheral didDiscoverServices:(NSError *)error ``` |
| To | ``` - (void)peripheral:(CBPeripheral * _Nonnull)peripheral didDiscoverServices:(NSError * _Nullable)error ``` |

Modified [-[CBPeripheralDelegate peripheral:didModifyServices:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518865-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheral:(CBPeripheral *)peripheral didModifyServices:(NSArray *)invalidatedServices ``` |
| To | ``` - (void)peripheral:(CBPeripheral * _Nonnull)peripheral didModifyServices:(NSArray<CBService *> * _Nonnull)invalidatedServices ``` |

Modified [-[CBPeripheralDelegate peripheral:didUpdateNotificationStateForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518768-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheral:(CBPeripheral *)peripheral didUpdateNotificationStateForCharacteristic:(CBCharacteristic *)characteristic error:(NSError *)error ``` |
| To | ``` - (void)peripheral:(CBPeripheral * _Nonnull)peripheral didUpdateNotificationStateForCharacteristic:(CBCharacteristic * _Nonnull)characteristic error:(NSError * _Nullable)error ``` |

Modified [-[CBPeripheralDelegate peripheral:didUpdateValueForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518708-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheral:(CBPeripheral *)peripheral didUpdateValueForCharacteristic:(CBCharacteristic *)characteristic error:(NSError *)error ``` |
| To | ``` - (void)peripheral:(CBPeripheral * _Nonnull)peripheral didUpdateValueForCharacteristic:(CBCharacteristic * _Nonnull)characteristic error:(NSError * _Nullable)error ``` |

Modified [-[CBPeripheralDelegate peripheral:didUpdateValueForDescriptor:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518929-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheral:(CBPeripheral *)peripheral didUpdateValueForDescriptor:(CBDescriptor *)descriptor error:(NSError *)error ``` |
| To | ``` - (void)peripheral:(CBPeripheral * _Nonnull)peripheral didUpdateValueForDescriptor:(CBDescriptor * _Nonnull)descriptor error:(NSError * _Nullable)error ``` |

Modified [-[CBPeripheralDelegate peripheral:didWriteValueForCharacteristic:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518823-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheral:(CBPeripheral *)peripheral didWriteValueForCharacteristic:(CBCharacteristic *)characteristic error:(NSError *)error ``` |
| To | ``` - (void)peripheral:(CBPeripheral * _Nonnull)peripheral didWriteValueForCharacteristic:(CBCharacteristic * _Nonnull)characteristic error:(NSError * _Nullable)error ``` |

Modified [-[CBPeripheralDelegate peripheral:didWriteValueForDescriptor:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519062-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheral:(CBPeripheral *)peripheral didWriteValueForDescriptor:(CBDescriptor *)descriptor error:(NSError *)error ``` |
| To | ``` - (void)peripheral:(CBPeripheral * _Nonnull)peripheral didWriteValueForDescriptor:(CBDescriptor * _Nonnull)descriptor error:(NSError * _Nullable)error ``` |

Modified [-[CBPeripheralDelegate peripheralDidUpdateName:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518801-peripheraldidupdatename)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheralDidUpdateName:(CBPeripheral *)peripheral ``` |
| To | ``` - (void)peripheralDidUpdateName:(CBPeripheral * _Nonnull)peripheral ``` |

Modified [-[CBPeripheralDelegate peripheralDidUpdateRSSI:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519083-peripheraldidupdaterssi)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheralDidUpdateRSSI:(CBPeripheral *)peripheral error:(NSError *)error ``` |
| To | ``` - (void)peripheralDidUpdateRSSI:(CBPeripheral * _Nonnull)peripheral error:(NSError * _Nullable)error ``` |

#### CBPeripheralManager.h

Modified [-[CBPeripheralManager addService:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393255-add)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addService:(CBMutableService *)service ``` |
| To | ``` - (void)addService:(CBMutableService * _Nonnull)service ``` |

Modified [CBPeripheralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393313-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) id<CBPeripheralManagerDelegate> delegate ``` |
| To | ``` @property(assign, nonatomic, nullable) id<CBPeripheralManagerDelegate> delegate ``` |

Modified [-[CBPeripheralManager initWithDelegate:queue:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393299-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDelegate:(id<CBPeripheralManagerDelegate>)delegate queue:(dispatch_queue_t)queue ``` |
| To | ``` - (id _Nonnull)initWithDelegate:(id<CBPeripheralManagerDelegate> _Nullable)delegate queue:(dispatch_queue_t _Nullable)queue ``` |

Modified [-[CBPeripheralManager initWithDelegate:queue:options:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393295-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithDelegate:(id<CBPeripheralManagerDelegate>)delegate queue:(dispatch_queue_t)queue options:(NSDictionary *)options ``` |
| To | ``` - (id _Nonnull)initWithDelegate:(id<CBPeripheralManagerDelegate> _Nullable)delegate queue:(dispatch_queue_t _Nullable)queue options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[CBPeripheralManager removeService:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393287-removeservice)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeService:(CBMutableService *)service ``` |
| To | ``` - (void)removeService:(CBMutableService * _Nonnull)service ``` |

Modified [-[CBPeripheralManager respondToRequest:withResult:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393293-respond)

|  | Declaration |
| --- | --- |
| From | ``` - (void)respondToRequest:(CBATTRequest *)request withResult:(CBATTError)result ``` |
| To | ``` - (void)respondToRequest:(CBATTRequest * _Nonnull)request withResult:(CBATTError)result ``` |

Modified [-[CBPeripheralManager setDesiredConnectionLatency:forCentral:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393277-setdesiredconnectionlatency)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setDesiredConnectionLatency:(CBPeripheralManagerConnectionLatency)latency forCentral:(CBCentral *)central ``` |
| To | ``` - (void)setDesiredConnectionLatency:(CBPeripheralManagerConnectionLatency)latency forCentral:(CBCentral * _Nonnull)central ``` |

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

Modified [-[CBPeripheralManagerDelegate peripheralManager:central:didSubscribeToCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393261-peripheralmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheralManager:(CBPeripheralManager *)peripheral central:(CBCentral *)central didSubscribeToCharacteristic:(CBCharacteristic *)characteristic ``` |
| To | ``` - (void)peripheralManager:(CBPeripheralManager * _Nonnull)peripheral central:(CBCentral * _Nonnull)central didSubscribeToCharacteristic:(CBCharacteristic * _Nonnull)characteristic ``` |

Modified [-[CBPeripheralManagerDelegate peripheralManager:central:didUnsubscribeFromCharacteristic:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393289-peripheralmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheralManager:(CBPeripheralManager *)peripheral central:(CBCentral *)central didUnsubscribeFromCharacteristic:(CBCharacteristic *)characteristic ``` |
| To | ``` - (void)peripheralManager:(CBPeripheralManager * _Nonnull)peripheral central:(CBCentral * _Nonnull)central didUnsubscribeFromCharacteristic:(CBCharacteristic * _Nonnull)characteristic ``` |

Modified [-[CBPeripheralManagerDelegate peripheralManager:didAddService:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393279-peripheralmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheralManager:(CBPeripheralManager *)peripheral didAddService:(CBService *)service error:(NSError *)error ``` |
| To | ``` - (void)peripheralManager:(CBPeripheralManager * _Nonnull)peripheral didAddService:(CBService * _Nonnull)service error:(NSError * _Nullable)error ``` |

Modified [-[CBPeripheralManagerDelegate peripheralManager:didReceiveReadRequest:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393257-peripheralmanager)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheralManager:(CBPeripheralManager *)peripheral didReceiveReadRequest:(CBATTRequest *)request ``` |
| To | ``` - (void)peripheralManager:(CBPeripheralManager * _Nonnull)peripheral didReceiveReadRequest:(CBATTRequest * _Nonnull)request ``` |

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

Modified [-[CBPeripheralManagerDelegate peripheralManagerDidStartAdvertising:error:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393321-peripheralmanagerdidstartadverti)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheralManagerDidStartAdvertising:(CBPeripheralManager *)peripheral error:(NSError *)error ``` |
| To | ``` - (void)peripheralManagerDidStartAdvertising:(CBPeripheralManager * _Nonnull)peripheral error:(NSError * _Nullable)error ``` |

Modified [-[CBPeripheralManagerDelegate peripheralManagerDidUpdateState:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393271-peripheralmanagerdidupdatestate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheralManagerDidUpdateState:(CBPeripheralManager *)peripheral ``` |
| To | ``` - (void)peripheralManagerDidUpdateState:(CBPeripheralManager * _Nonnull)peripheral ``` |

Modified [-[CBPeripheralManagerDelegate peripheralManagerIsReadyToUpdateSubscribers:]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393248-peripheralmanagerisreadytoupdate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)peripheralManagerIsReadyToUpdateSubscribers:(CBPeripheralManager *)peripheral ``` |
| To | ``` - (void)peripheralManagerIsReadyToUpdateSubscribers:(CBPeripheralManager * _Nonnull)peripheral ``` |

#### CBService.h

Modified [CBMutableService.characteristics](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/1434317-characteristics)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readwrite) NSArray *characteristics ``` |
| To | ``` @property(retain, readwrite, nullable) NSArray<CBCharacteristic *> *characteristics ``` |

Modified [CBMutableService.includedServices](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/1434320-includedservices)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readwrite) NSArray *includedServices ``` |
| To | ``` @property(retain, readwrite, nullable) NSArray<CBService *> *includedServices ``` |

Modified [-[CBMutableService initWithType:primary:]](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/1434330-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithType:(CBUUID *)UUID primary:(BOOL)isPrimary ``` |
| To | ``` - (id _Nonnull)initWithType:(CBUUID * _Nullable)UUID primary:(BOOL)isPrimary ``` |

Modified CBMutableService.UUID

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readwrite, nonatomic) CBUUID *UUID ``` |
| To | ``` @property(retain, readwrite, nonatomic, nullable) CBUUID *UUID ``` |

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

Modified CBService.UUID

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CBUUID *UUID ``` |
| To | ``` @property(readonly, nonatomic, nonnull) CBUUID *UUID ``` |

#### CBUUID.h

Added CBUUIDValidRangeStringModified [CBUUID.data](https://developer.apple.com/documentation/corebluetooth/cbuuid/1519007-data)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSData *data ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSData *data ``` |

Modified [CBUUID.UUIDString](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518742-uuidstring)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *UUIDString ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *UUIDString ``` |

Modified [+[CBUUID UUIDWithCFUUID:]](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518861-uuidwithcfuuid)

|  | Declaration |
| --- | --- |
| From | ``` + (CBUUID *)UUIDWithCFUUID:(CFUUIDRef)theUUID ``` |
| To | ``` + (CBUUID * _Nonnull)UUIDWithCFUUID:(CFUUIDRef _Nonnull)theUUID ``` |

Modified [+[CBUUID UUIDWithData:]](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518799-uuidwithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (CBUUID *)UUIDWithData:(NSData *)theData ``` |
| To | ``` + (CBUUID * _Nonnull)UUIDWithData:(NSData * _Nonnull)theData ``` |

Modified [+[CBUUID UUIDWithNSUUID:]](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518783-init)

|  | Declaration |
| --- | --- |
| From | ``` + (CBUUID *)UUIDWithNSUUID:(NSUUID *)theUUID ``` |
| To | ``` + (CBUUID * _Nonnull)UUIDWithNSUUID:(NSUUID * _Nonnull)theUUID ``` |

Modified [+[CBUUID UUIDWithString:]](https://developer.apple.com/documentation/corebluetooth/cbuuid/1519025-uuidwithstring)

|  | Declaration |
| --- | --- |
| From | ``` + (CBUUID *)UUIDWithString:(NSString *)theString ``` |
| To | ``` + (CBUUID * _Nonnull)UUIDWithString:(NSString * _Nonnull)theString ``` |

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
