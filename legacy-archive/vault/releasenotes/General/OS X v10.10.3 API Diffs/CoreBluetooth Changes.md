---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CoreBluetooth.html
archived_at: '2026-07-18T02:52:09.951134Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CoreBluetooth Changes

## CoreBluetooth

Added CBAttributePermissions.init(_: Int)Added CBAttributePermissions.init(rawValue: Int)Added CBCharacteristicProperties.init(_: Int)Added CBCharacteristicProperties.init(rawValue: Int)Modified CBATTError.Success

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBATTRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBATTRequest.value

|  | Declaration |
| --- | --- |
| From | ``` var value: NSData! ``` |
| To | ``` @NSCopying var value: NSData! ``` |

Modified CBAttributePermissions [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` enum CBAttributePermissions : Int {     case Readable     case Writeable     case ReadEncryptionRequired     case WriteEncryptionRequired } ``` | Equatable, Hashable, RawRepresentable | OS X 10.10 |
| To | ``` struct CBAttributePermissions : RawOptionSetType {     init(_ rawValue: Int)     init(rawValue rawValue: Int)     static var Readable: CBAttributePermissions { get }     static var Writeable: CBAttributePermissions { get }     static var ReadEncryptionRequired: CBAttributePermissions { get }     static var WriteEncryptionRequired: CBAttributePermissions { get } } ``` | RawOptionSetType | OS X 10.9 |

Modified CBAttributePermissions.ReadEncryptionRequired

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case ReadEncryptionRequired ``` | OS X 10.10 |
| To | ``` static var ReadEncryptionRequired: CBAttributePermissions { get } ``` | OS X 10.10.3 |

Modified CBAttributePermissions.Readable

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case Readable ``` | OS X 10.10 |
| To | ``` static var Readable: CBAttributePermissions { get } ``` | OS X 10.10.3 |

Modified CBAttributePermissions.WriteEncryptionRequired

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case WriteEncryptionRequired ``` | OS X 10.10 |
| To | ``` static var WriteEncryptionRequired: CBAttributePermissions { get } ``` | OS X 10.10.3 |

Modified CBAttributePermissions.Writeable

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case Writeable ``` | OS X 10.10 |
| To | ``` static var Writeable: CBAttributePermissions { get } ``` | OS X 10.10.3 |

Modified CBCentral

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBCentralManager

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CBCentralManager.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: CBCentralManagerDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: CBCentralManagerDelegate! ``` |

Modified CBCentralManager.init(delegate: CBCentralManagerDelegate!, queue: dispatch_queue_t!)

|  | Declaration |
| --- | --- |
| From | ``` init(delegate delegate: CBCentralManagerDelegate!, queue queue: dispatch_queue_t!) ``` |
| To | ``` init!(delegate delegate: CBCentralManagerDelegate!, queue queue: dispatch_queue_t!) ``` |

Modified CBCentralManager.init(delegate: CBCentralManagerDelegate!, queue: dispatch_queue_t!, options:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(delegate delegate: CBCentralManagerDelegate!, queue queue: dispatch_queue_t!, options options: [NSObject : AnyObject]!) ``` | OS X 10.10 |
| To | ``` init!(delegate delegate: CBCentralManagerDelegate!, queue queue: dispatch_queue_t!, options options: [NSObject : AnyObject]!) ``` | OS X 10.9 |

Modified CBCentralManager.retrieveConnectedPeripheralsWithServices([AnyObject]!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBCentralManager.retrievePeripheralsWithIdentifiers([AnyObject]!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBCentralManagerDelegate.centralManager(CBCentralManager!, didConnectPeripheral: CBPeripheral!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBCentralManagerDelegate.centralManager(CBCentralManager!, didDisconnectPeripheral: CBPeripheral!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBCentralManagerDelegate.centralManager(CBCentralManager!, didDiscoverPeripheral: CBPeripheral!, advertisementData:[NSObject: AnyObject]!, RSSI: NSNumber!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBCentralManagerDelegate.centralManager(CBCentralManager!, didFailToConnectPeripheral: CBPeripheral!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBCentralManagerDelegate.centralManager(CBCentralManager!, didRetrieveConnectedPeripherals:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBCentralManagerDelegate.centralManager(CBCentralManager!, didRetrievePeripherals:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBCentralManagerDelegate.centralManager(CBCentralManager!, willRestoreState:[NSObject: AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBCharacteristic

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CBCharacteristic.service

|  | Declaration |
| --- | --- |
| From | ``` var service: CBService! { get } ``` |
| To | ``` weak var service: CBService! { get } ``` |

Modified CBCharacteristicProperties [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` enum CBCharacteristicProperties : Int {     case Broadcast     case Read     case WriteWithoutResponse     case Write     case Notify     case Indicate     case AuthenticatedSignedWrites     case ExtendedProperties     case NotifyEncryptionRequired     case IndicateEncryptionRequired } ``` | Equatable, Hashable, RawRepresentable | OS X 10.10 |
| To | ``` struct CBCharacteristicProperties : RawOptionSetType {     init(_ rawValue: Int)     init(rawValue rawValue: Int)     static var Broadcast: CBCharacteristicProperties { get }     static var Read: CBCharacteristicProperties { get }     static var WriteWithoutResponse: CBCharacteristicProperties { get }     static var Write: CBCharacteristicProperties { get }     static var Notify: CBCharacteristicProperties { get }     static var Indicate: CBCharacteristicProperties { get }     static var AuthenticatedSignedWrites: CBCharacteristicProperties { get }     static var ExtendedProperties: CBCharacteristicProperties { get }     static var NotifyEncryptionRequired: CBCharacteristicProperties { get }     static var IndicateEncryptionRequired: CBCharacteristicProperties { get } } ``` | RawOptionSetType | OS X 10.10.3 |

Modified CBCharacteristicProperties.AuthenticatedSignedWrites

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case AuthenticatedSignedWrites ``` | OS X 10.10 |
| To | ``` static var AuthenticatedSignedWrites: CBCharacteristicProperties { get } ``` | OS X 10.10.3 |

Modified CBCharacteristicProperties.Broadcast

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case Broadcast ``` | OS X 10.10 |
| To | ``` static var Broadcast: CBCharacteristicProperties { get } ``` | OS X 10.10.3 |

Modified CBCharacteristicProperties.ExtendedProperties

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case ExtendedProperties ``` | OS X 10.10 |
| To | ``` static var ExtendedProperties: CBCharacteristicProperties { get } ``` | OS X 10.10.3 |

Modified CBCharacteristicProperties.Indicate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case Indicate ``` | OS X 10.10 |
| To | ``` static var Indicate: CBCharacteristicProperties { get } ``` | OS X 10.10.3 |

Modified CBCharacteristicProperties.IndicateEncryptionRequired

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case IndicateEncryptionRequired ``` | OS X 10.10 |
| To | ``` static var IndicateEncryptionRequired: CBCharacteristicProperties { get } ``` | OS X 10.9 |

Modified CBCharacteristicProperties.Notify

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case Notify ``` | OS X 10.10 |
| To | ``` static var Notify: CBCharacteristicProperties { get } ``` | OS X 10.10.3 |

Modified CBCharacteristicProperties.NotifyEncryptionRequired

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case NotifyEncryptionRequired ``` | OS X 10.10 |
| To | ``` static var NotifyEncryptionRequired: CBCharacteristicProperties { get } ``` | OS X 10.9 |

Modified CBCharacteristicProperties.Read

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case Read ``` | OS X 10.10 |
| To | ``` static var Read: CBCharacteristicProperties { get } ``` | OS X 10.10.3 |

Modified CBCharacteristicProperties.Write

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case Write ``` | OS X 10.10 |
| To | ``` static var Write: CBCharacteristicProperties { get } ``` | OS X 10.10.3 |

Modified CBCharacteristicProperties.WriteWithoutResponse

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case WriteWithoutResponse ``` | OS X 10.10 |
| To | ``` static var WriteWithoutResponse: CBCharacteristicProperties { get } ``` | OS X 10.10.3 |

Modified CBDescriptor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CBDescriptor.characteristic

|  | Declaration |
| --- | --- |
| From | ``` var characteristic: CBCharacteristic! { get } ``` |
| To | ``` weak var characteristic: CBCharacteristic! { get } ``` |

Modified CBError.AlreadyAdvertising

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBError.ConnectionTimeout

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBError.InvalidHandle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBError.InvalidParameters

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBError.NotConnected

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBError.OperationCancelled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBError.OutOfSpace

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBError.PeripheralDisconnected

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBError.UUIDNotAllowed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBMutableCharacteristic

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBMutableCharacteristic.subscribedCentrals

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBMutableCharacteristic.init(type: CBUUID!, properties: CBCharacteristicProperties, value: NSData!, permissions: CBAttributePermissions)

|  | Declaration |
| --- | --- |
| From | ``` init(type UUID: CBUUID!, properties properties: CBCharacteristicProperties, value value: NSData!, permissions permissions: CBAttributePermissions) ``` |
| To | ``` init!(type UUID: CBUUID!, properties properties: CBCharacteristicProperties, value value: NSData!, permissions permissions: CBAttributePermissions) ``` |

Modified CBMutableDescriptor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBMutableDescriptor.init(type: CBUUID!, value: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(type UUID: CBUUID!, value value: AnyObject!) ``` |
| To | ``` init!(type UUID: CBUUID!, value value: AnyObject!) ``` |

Modified CBMutableService

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBMutableService.init(type: CBUUID!, primary: Bool)

|  | Declaration |
| --- | --- |
| From | ``` init(type UUID: CBUUID!, primary isPrimary: Bool) ``` |
| To | ``` init!(type UUID: CBUUID!, primary isPrimary: Bool) ``` |

Modified CBPeripheral

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CBPeripheral.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: CBPeripheralDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: CBPeripheralDelegate! ``` |

Modified CBPeripheralAuthorizationStatus [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBPeripheralDelegate.peripheral(CBPeripheral!, didDiscoverCharacteristicsForService: CBService!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralDelegate.peripheral(CBPeripheral!, didDiscoverDescriptorsForCharacteristic: CBCharacteristic!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralDelegate.peripheral(CBPeripheral!, didDiscoverIncludedServicesForService: CBService!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralDelegate.peripheral(CBPeripheral!, didDiscoverServices: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralDelegate.peripheral(CBPeripheral!, didModifyServices:[AnyObject]!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified CBPeripheralDelegate.peripheral(CBPeripheral!, didUpdateNotificationStateForCharacteristic: CBCharacteristic!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralDelegate.peripheral(CBPeripheral!, didUpdateValueForCharacteristic: CBCharacteristic!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralDelegate.peripheral(CBPeripheral!, didUpdateValueForDescriptor: CBDescriptor!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralDelegate.peripheral(CBPeripheral!, didWriteValueForCharacteristic: CBCharacteristic!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralDelegate.peripheral(CBPeripheral!, didWriteValueForDescriptor: CBDescriptor!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralDelegate.peripheralDidUpdateName(CBPeripheral!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified CBPeripheralDelegate.peripheralDidUpdateRSSI(CBPeripheral!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralManager

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBPeripheralManager.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: CBPeripheralManagerDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: CBPeripheralManagerDelegate! ``` |

Modified CBPeripheralManager.init(delegate: CBPeripheralManagerDelegate!, queue: dispatch_queue_t!)

|  | Declaration |
| --- | --- |
| From | ``` init(delegate delegate: CBPeripheralManagerDelegate!, queue queue: dispatch_queue_t!) ``` |
| To | ``` init!(delegate delegate: CBPeripheralManagerDelegate!, queue queue: dispatch_queue_t!) ``` |

Modified CBPeripheralManager.init(delegate: CBPeripheralManagerDelegate!, queue: dispatch_queue_t!, options:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(delegate delegate: CBPeripheralManagerDelegate!, queue queue: dispatch_queue_t!, options options: [NSObject : AnyObject]!) ``` | OS X 10.10 |
| To | ``` init!(delegate delegate: CBPeripheralManagerDelegate!, queue queue: dispatch_queue_t!, options options: [NSObject : AnyObject]!) ``` | OS X 10.9 |

Modified CBPeripheralManagerConnectionLatency [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBPeripheralManagerDelegate.peripheralManager(CBPeripheralManager!, central: CBCentral!, didSubscribeToCharacteristic: CBCharacteristic!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralManagerDelegate.peripheralManager(CBPeripheralManager!, central: CBCentral!, didUnsubscribeFromCharacteristic: CBCharacteristic!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralManagerDelegate.peripheralManager(CBPeripheralManager!, didAddService: CBService!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralManagerDelegate.peripheralManager(CBPeripheralManager!, didReceiveReadRequest: CBATTRequest!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralManagerDelegate.peripheralManager(CBPeripheralManager!, didReceiveWriteRequests:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralManagerDelegate.peripheralManager(CBPeripheralManager!, willRestoreState:[NSObject: AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralManagerDelegate.peripheralManagerDidStartAdvertising(CBPeripheralManager!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralManagerDelegate.peripheralManagerIsReadyToUpdateSubscribers(CBPeripheralManager!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CBPeripheralManagerState [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBPeripheralState [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CBService

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CBService.peripheral

|  | Declaration |
| --- | --- |
| From | ``` var peripheral: CBPeripheral! { get } ``` |
| To | ``` weak var peripheral: CBPeripheral! { get } ``` |

Modified CBUUID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CBUUID.init(CFUUID: CFUUID!)

|  | Name | Declaration |
| --- | --- | --- |
| From | UUIDWithCFUUID(_:) | ``` class func UUIDWithCFUUID(_ theUUID: CFUUID!) -> CBUUID! ``` |
| To | init(CFUUID:) | ``` init!(CFUUID theUUID: CFUUID!) -> CBUUID ``` |

Modified CBUUID.init(NSUUID: NSUUID!)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | UUIDWithNSUUID(_:) | ``` class func UUIDWithNSUUID(_ theUUID: NSUUID!) -> CBUUID! ``` | OS X 10.10 |
| To | init(NSUUID:) | ``` init!(NSUUID theUUID: NSUUID!) -> CBUUID ``` | OS X 10.9 |

Modified CBUUID.init(data: NSData!)

|  | Name | Declaration |
| --- | --- | --- |
| From | UUIDWithData(_:) | ``` class func UUIDWithData(_ theData: NSData!) -> CBUUID! ``` |
| To | init(data:) | ``` init!(data theData: NSData!) -> CBUUID ``` |

Modified CBUUID.init(string: String!)

|  | Name | Declaration |
| --- | --- | --- |
| From | UUIDWithString(_:) | ``` class func UUIDWithString(_ theString: String!) -> CBUUID! ``` |
| To | init(string:) | ``` init!(string theString: String!) -> CBUUID ``` |

Modified CBATTErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let CBATTErrorDomain: NSString! ``` |
| To | ``` let CBATTErrorDomain: String ``` |

Modified CBAdvertisementDataIsConnectable

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CBAdvertisementDataIsConnectable: NSString! ``` | OS X 10.10 |
| To | ``` let CBAdvertisementDataIsConnectable: String ``` | OS X 10.9 |

Modified CBAdvertisementDataLocalNameKey

|  | Declaration |
| --- | --- |
| From | ``` let CBAdvertisementDataLocalNameKey: NSString! ``` |
| To | ``` let CBAdvertisementDataLocalNameKey: String ``` |

Modified CBAdvertisementDataManufacturerDataKey

|  | Declaration |
| --- | --- |
| From | ``` let CBAdvertisementDataManufacturerDataKey: NSString! ``` |
| To | ``` let CBAdvertisementDataManufacturerDataKey: String ``` |

Modified CBAdvertisementDataOverflowServiceUUIDsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CBAdvertisementDataOverflowServiceUUIDsKey: NSString! ``` | OS X 10.10 |
| To | ``` let CBAdvertisementDataOverflowServiceUUIDsKey: String ``` | OS X 10.9 |

Modified CBAdvertisementDataServiceDataKey

|  | Declaration |
| --- | --- |
| From | ``` let CBAdvertisementDataServiceDataKey: NSString! ``` |
| To | ``` let CBAdvertisementDataServiceDataKey: String ``` |

Modified CBAdvertisementDataServiceUUIDsKey

|  | Declaration |
| --- | --- |
| From | ``` let CBAdvertisementDataServiceUUIDsKey: NSString! ``` |
| To | ``` let CBAdvertisementDataServiceUUIDsKey: String ``` |

Modified CBAdvertisementDataSolicitedServiceUUIDsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CBAdvertisementDataSolicitedServiceUUIDsKey: NSString! ``` | OS X 10.10 |
| To | ``` let CBAdvertisementDataSolicitedServiceUUIDsKey: String ``` | OS X 10.9 |

Modified CBAdvertisementDataTxPowerLevelKey

|  | Declaration |
| --- | --- |
| From | ``` let CBAdvertisementDataTxPowerLevelKey: NSString! ``` |
| To | ``` let CBAdvertisementDataTxPowerLevelKey: String ``` |

Modified CBCentralManagerOptionShowPowerAlertKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CBCentralManagerOptionShowPowerAlertKey: NSString! ``` | OS X 10.10 |
| To | ``` let CBCentralManagerOptionShowPowerAlertKey: String ``` | OS X 10.9 |

Modified CBCentralManagerScanOptionAllowDuplicatesKey

|  | Declaration |
| --- | --- |
| From | ``` let CBCentralManagerScanOptionAllowDuplicatesKey: NSString! ``` |
| To | ``` let CBCentralManagerScanOptionAllowDuplicatesKey: String ``` |

Modified CBCentralManagerScanOptionSolicitedServiceUUIDsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CBCentralManagerScanOptionSolicitedServiceUUIDsKey: NSString! ``` | OS X 10.10 |
| To | ``` let CBCentralManagerScanOptionSolicitedServiceUUIDsKey: String ``` | OS X 10.9 |

Modified CBConnectPeripheralOptionNotifyOnDisconnectionKey

|  | Declaration |
| --- | --- |
| From | ``` let CBConnectPeripheralOptionNotifyOnDisconnectionKey: NSString! ``` |
| To | ``` let CBConnectPeripheralOptionNotifyOnDisconnectionKey: String ``` |

Modified CBErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let CBErrorDomain: NSString! ``` |
| To | ``` let CBErrorDomain: String ``` |

Modified CBPeripheralManagerOptionShowPowerAlertKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CBPeripheralManagerOptionShowPowerAlertKey: NSString! ``` | OS X 10.10 |
| To | ``` let CBPeripheralManagerOptionShowPowerAlertKey: String ``` | OS X 10.9 |

Modified CBUUIDAppearanceString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDAppearanceString: NSString! ``` |
| To | ``` let CBUUIDAppearanceString: String ``` |

Modified CBUUIDCharacteristicAggregateFormatString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDCharacteristicAggregateFormatString: NSString! ``` |
| To | ``` let CBUUIDCharacteristicAggregateFormatString: String ``` |

Modified CBUUIDCharacteristicExtendedPropertiesString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDCharacteristicExtendedPropertiesString: NSString! ``` |
| To | ``` let CBUUIDCharacteristicExtendedPropertiesString: String ``` |

Modified CBUUIDCharacteristicFormatString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDCharacteristicFormatString: NSString! ``` |
| To | ``` let CBUUIDCharacteristicFormatString: String ``` |

Modified CBUUIDCharacteristicUserDescriptionString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDCharacteristicUserDescriptionString: NSString! ``` |
| To | ``` let CBUUIDCharacteristicUserDescriptionString: String ``` |

Modified CBUUIDClientCharacteristicConfigurationString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDClientCharacteristicConfigurationString: NSString! ``` |
| To | ``` let CBUUIDClientCharacteristicConfigurationString: String ``` |

Modified CBUUIDDeviceNameString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDDeviceNameString: NSString! ``` |
| To | ``` let CBUUIDDeviceNameString: String ``` |

Modified CBUUIDGenericAccessProfileString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDGenericAccessProfileString: NSString! ``` |
| To | ``` let CBUUIDGenericAccessProfileString: String ``` |

Modified CBUUIDGenericAttributeProfileString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDGenericAttributeProfileString: NSString! ``` |
| To | ``` let CBUUIDGenericAttributeProfileString: String ``` |

Modified CBUUIDPeripheralPreferredConnectionParametersString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDPeripheralPreferredConnectionParametersString: NSString! ``` |
| To | ``` let CBUUIDPeripheralPreferredConnectionParametersString: String ``` |

Modified CBUUIDPeripheralPrivacyFlagString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDPeripheralPrivacyFlagString: NSString! ``` |
| To | ``` let CBUUIDPeripheralPrivacyFlagString: String ``` |

Modified CBUUIDReconnectionAddressString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDReconnectionAddressString: NSString! ``` |
| To | ``` let CBUUIDReconnectionAddressString: String ``` |

Modified CBUUIDServerCharacteristicConfigurationString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDServerCharacteristicConfigurationString: NSString! ``` |
| To | ``` let CBUUIDServerCharacteristicConfigurationString: String ``` |

Modified CBUUIDServiceChangedString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDServiceChangedString: NSString! ``` |
| To | ``` let CBUUIDServiceChangedString: String ``` |

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
