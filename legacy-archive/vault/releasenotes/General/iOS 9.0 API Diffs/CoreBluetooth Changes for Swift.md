---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/CoreBluetooth.html
archived_at: '2026-07-18T02:56:43.331689Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreBluetooth Changes for Swift

### CoreBluetooth

Removed CBAttributePermissions.init(_: UInt)Removed CBCentralManagerDelegate.centralManager(_: CBCentralManager!, didRetrieveConnectedPeripherals: [AnyObject]!)Removed CBCentralManagerDelegate.centralManager(_: CBCentralManager!, didRetrievePeripherals: [AnyObject]!)Removed CBCharacteristicProperties.init(_: UInt)Removed CBMutableCharacteristic.UUIDRemoved CBMutableService.isPrimaryRemoved CBMutableService.UUIDAdded [CBCentralManager.isScanning](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1620640-isscanning)Added [CBError.ConnectionLimitReached](https://developer.apple.com/documentation/corebluetooth/cberror/code/connectionlimitreached)Added [CBPeripheral.maximumWriteValueLengthForType(_: CBCharacteristicWriteType) -> Int](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1620312-maximumwritevaluelengthfortype)Added [CBPeripheralState.Disconnecting](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate/cbperipheralstatedisconnecting)Modified [CBATTError [enum]](https://developer.apple.com/documentation/corebluetooth/cbatterror)

|  | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- |
| From | ``` enum CBATTError : Int {     case Success     case InvalidHandle     case ReadNotPermitted     case WriteNotPermitted     case InvalidPdu     case InsufficientAuthentication     case RequestNotSupported     case InvalidOffset     case InsufficientAuthorization     case PrepareQueueFull     case AttributeNotFound     case AttributeNotLong     case InsufficientEncryptionKeySize     case InvalidAttributeValueLength     case UnlikelyError     case InsufficientEncryption     case UnsupportedGroupType     case InsufficientResources } ``` | Equatable, Hashable, RawRepresentable | -- |
| To | ``` enum CBATTError : Int {     case Success     case InvalidHandle     case ReadNotPermitted     case WriteNotPermitted     case InvalidPdu     case InsufficientAuthentication     case RequestNotSupported     case InvalidOffset     case InsufficientAuthorization     case PrepareQueueFull     case AttributeNotFound     case AttributeNotLong     case InsufficientEncryptionKeySize     case InvalidAttributeValueLength     case UnlikelyError     case InsufficientEncryption     case UnsupportedGroupType     case InsufficientResources } extension CBATTError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension CBATTError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable | Int |

Modified [CBATTRequest](https://developer.apple.com/documentation/corebluetooth/cbattrequest)

|  | Declaration |
| --- | --- |
| From | ``` class CBATTRequest : NSObject {     var central: CBCentral! { get }     var characteristic: CBCharacteristic! { get }     var offset: Int { get }     @NSCopying var value: NSData! } ``` |
| To | ``` class CBATTRequest : NSObject {     init()     var central: CBCentral { get }     var characteristic: CBCharacteristic { get }     var offset: Int { get }     @NSCopying var value: NSData? } ``` |

Modified [CBATTRequest.central](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518995-central)

|  | Declaration |
| --- | --- |
| From | ``` var central: CBCentral! { get } ``` |
| To | ``` var central: CBCentral { get } ``` |

Modified [CBATTRequest.characteristic](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518716-characteristic)

|  | Declaration |
| --- | --- |
| From | ``` var characteristic: CBCharacteristic! { get } ``` |
| To | ``` var characteristic: CBCharacteristic { get } ``` |

Modified [CBATTRequest.value](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518795-value)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var value: NSData! ``` |
| To | ``` @NSCopying var value: NSData? ``` |

Modified [CBAttribute](https://developer.apple.com/documentation/corebluetooth/cbattribute)

|  | Declaration |
| --- | --- |
| From | ``` class CBAttribute : NSObject {     var UUID: CBUUID! { get } } ``` |
| To | ``` class CBAttribute : NSObject {     init()     var UUID: CBUUID { get } } ``` |

Modified [CBAttribute.UUID](https://developer.apple.com/documentation/corebluetooth/cbattribute/1620638-uuid)

|  | Declaration |
| --- | --- |
| From | ``` var UUID: CBUUID! { get } ``` |
| To | ``` var UUID: CBUUID { get } ``` |

Modified [CBAttributePermissions [struct]](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBAttributePermissions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Readable: CBAttributePermissions { get }     static var Writeable: CBAttributePermissions { get }     static var ReadEncryptionRequired: CBAttributePermissions { get }     static var WriteEncryptionRequired: CBAttributePermissions { get } } ``` | RawOptionSetType |
| To | ``` struct CBAttributePermissions : OptionSetType {     init(rawValue rawValue: UInt)     static var Readable: CBAttributePermissions { get }     static var Writeable: CBAttributePermissions { get }     static var ReadEncryptionRequired: CBAttributePermissions { get }     static var WriteEncryptionRequired: CBAttributePermissions { get } } ``` | OptionSetType |

Modified [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager)

|  | Declaration |
| --- | --- |
| From | ``` class CBCentralManager : NSObject {     weak var delegate: CBCentralManagerDelegate!     var state: CBCentralManagerState { get }     convenience init!(delegate delegate: CBCentralManagerDelegate!, queue queue: dispatch_queue_t!)     init!(delegate delegate: CBCentralManagerDelegate!, queue queue: dispatch_queue_t!, options options: [NSObject : AnyObject]!)     func retrievePeripherals(_ peripheralUUIDs: [AnyObject]!)     func retrievePeripheralsWithIdentifiers(_ identifiers: [AnyObject]!) -> [AnyObject]!     func retrieveConnectedPeripherals()     func retrieveConnectedPeripheralsWithServices(_ serviceUUIDs: [AnyObject]!) -> [AnyObject]!     func scanForPeripheralsWithServices(_ serviceUUIDs: [AnyObject]!, options options: [NSObject : AnyObject]!)     func stopScan()     func connectPeripheral(_ peripheral: CBPeripheral!, options options: [NSObject : AnyObject]!)     func cancelPeripheralConnection(_ peripheral: CBPeripheral!) } ``` |
| To | ``` class CBCentralManager : NSObject {     unowned(unsafe) var delegate: CBCentralManagerDelegate?     var state: CBCentralManagerState { get }     var isScanning: Bool { get }     convenience init(delegate delegate: CBCentralManagerDelegate?, queue queue: dispatch_queue_t?)     init(delegate delegate: CBCentralManagerDelegate?, queue queue: dispatch_queue_t?, options options: [String : AnyObject]?)     func retrievePeripheralsWithIdentifiers(_ identifiers: [NSUUID]) -> [CBPeripheral]     func retrieveConnectedPeripheralsWithServices(_ serviceUUIDs: [CBUUID]) -> [CBPeripheral]     func scanForPeripheralsWithServices(_ serviceUUIDs: [CBUUID]?, options options: [String : AnyObject]?)     func stopScan()     func connectPeripheral(_ peripheral: CBPeripheral, options options: [String : AnyObject]?)     func cancelPeripheralConnection(_ peripheral: CBPeripheral) } ``` |

Modified [CBCentralManager.cancelPeripheralConnection(_: CBPeripheral)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518952-cancelperipheralconnection)

|  | Declaration |
| --- | --- |
| From | ``` func cancelPeripheralConnection(_ peripheral: CBPeripheral!) ``` |
| To | ``` func cancelPeripheralConnection(_ peripheral: CBPeripheral) ``` |

Modified [CBCentralManager.connectPeripheral(_: CBPeripheral, options: [String : AnyObject]?)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518766-connect)

|  | Declaration |
| --- | --- |
| From | ``` func connectPeripheral(_ peripheral: CBPeripheral!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` func connectPeripheral(_ peripheral: CBPeripheral, options options: [String : AnyObject]?) ``` |

Modified [CBCentralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518944-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: CBCentralManagerDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: CBCentralManagerDelegate? ``` |

Modified [CBCentralManager.init(delegate: CBCentralManagerDelegate?, queue: dispatch_queue_t?)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518695-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(delegate delegate: CBCentralManagerDelegate!, queue queue: dispatch_queue_t!) ``` |
| To | ``` convenience init(delegate delegate: CBCentralManagerDelegate?, queue queue: dispatch_queue_t?) ``` |

Modified [CBCentralManager.init(delegate: CBCentralManagerDelegate?, queue: dispatch_queue_t?, options: [String : AnyObject]?)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1519001-initwithdelegate)

|  | Declaration |
| --- | --- |
| From | ``` init!(delegate delegate: CBCentralManagerDelegate!, queue queue: dispatch_queue_t!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` init(delegate delegate: CBCentralManagerDelegate?, queue queue: dispatch_queue_t?, options options: [String : AnyObject]?) ``` |

Modified [CBCentralManager.retrieveConnectedPeripheralsWithServices(_: [CBUUID]) -> [CBPeripheral]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518924-retrieveconnectedperipheralswith)

|  | Declaration |
| --- | --- |
| From | ``` func retrieveConnectedPeripheralsWithServices(_ serviceUUIDs: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func retrieveConnectedPeripheralsWithServices(_ serviceUUIDs: [CBUUID]) -> [CBPeripheral] ``` |

Modified [CBCentralManager.retrievePeripheralsWithIdentifiers(_: [NSUUID]) -> [CBPeripheral]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1519127-retrieveperipheralswithidentifie)

|  | Declaration |
| --- | --- |
| From | ``` func retrievePeripheralsWithIdentifiers(_ identifiers: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func retrievePeripheralsWithIdentifiers(_ identifiers: [NSUUID]) -> [CBPeripheral] ``` |

Modified [CBCentralManager.scanForPeripheralsWithServices(_: [CBUUID]?, options: [String : AnyObject]?)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518986-scanforperipheralswithservices)

|  | Declaration |
| --- | --- |
| From | ``` func scanForPeripheralsWithServices(_ serviceUUIDs: [AnyObject]!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` func scanForPeripheralsWithServices(_ serviceUUIDs: [CBUUID]?, options options: [String : AnyObject]?) ``` |

Modified [CBCentralManagerDelegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol CBCentralManagerDelegate : NSObjectProtocol {     func centralManagerDidUpdateState(_ central: CBCentralManager!)     optional func centralManager(_ central: CBCentralManager!, willRestoreState dict: [NSObject : AnyObject]!)     optional func centralManager(_ central: CBCentralManager!, didRetrievePeripherals peripherals: [AnyObject]!)     optional func centralManager(_ central: CBCentralManager!, didRetrieveConnectedPeripherals peripherals: [AnyObject]!)     optional func centralManager(_ central: CBCentralManager!, didDiscoverPeripheral peripheral: CBPeripheral!, advertisementData advertisementData: [NSObject : AnyObject]!, RSSI RSSI: NSNumber!)     optional func centralManager(_ central: CBCentralManager!, didConnectPeripheral peripheral: CBPeripheral!)     optional func centralManager(_ central: CBCentralManager!, didFailToConnectPeripheral peripheral: CBPeripheral!, error error: NSError!)     optional func centralManager(_ central: CBCentralManager!, didDisconnectPeripheral peripheral: CBPeripheral!, error error: NSError!) } ``` |
| To | ``` protocol CBCentralManagerDelegate : NSObjectProtocol {     func centralManagerDidUpdateState(_ central: CBCentralManager)     optional func centralManager(_ central: CBCentralManager, willRestoreState dict: [String : AnyObject])     optional func centralManager(_ central: CBCentralManager, didDiscoverPeripheral peripheral: CBPeripheral, advertisementData advertisementData: [String : AnyObject], RSSI RSSI: NSNumber)     optional func centralManager(_ central: CBCentralManager, didConnectPeripheral peripheral: CBPeripheral)     optional func centralManager(_ central: CBCentralManager, didFailToConnectPeripheral peripheral: CBPeripheral, error error: NSError?)     optional func centralManager(_ central: CBCentralManager, didDisconnectPeripheral peripheral: CBPeripheral, error error: NSError?) } ``` |

Modified [CBCentralManagerDelegate.centralManager(_: CBCentralManager, didConnectPeripheral: CBPeripheral)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518969-centralmanager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func centralManager(_ central: CBCentralManager!, didConnectPeripheral peripheral: CBPeripheral!) ``` | iOS 8.0 |
| To | ``` optional func centralManager(_ central: CBCentralManager, didConnectPeripheral peripheral: CBPeripheral) ``` | iOS 5.0 |

Modified [CBCentralManagerDelegate.centralManager(_: CBCentralManager, didDisconnectPeripheral: CBPeripheral, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518791-centralmanager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func centralManager(_ central: CBCentralManager!, didDisconnectPeripheral peripheral: CBPeripheral!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func centralManager(_ central: CBCentralManager, didDisconnectPeripheral peripheral: CBPeripheral, error error: NSError?) ``` | iOS 5.0 |

Modified [CBCentralManagerDelegate.centralManager(_: CBCentralManager, didDiscoverPeripheral: CBPeripheral, advertisementData: [String : AnyObject], RSSI: NSNumber)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518937-centralmanager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func centralManager(_ central: CBCentralManager!, didDiscoverPeripheral peripheral: CBPeripheral!, advertisementData advertisementData: [NSObject : AnyObject]!, RSSI RSSI: NSNumber!) ``` | iOS 8.0 |
| To | ``` optional func centralManager(_ central: CBCentralManager, didDiscoverPeripheral peripheral: CBPeripheral, advertisementData advertisementData: [String : AnyObject], RSSI RSSI: NSNumber) ``` | iOS 5.0 |

Modified [CBCentralManagerDelegate.centralManager(_: CBCentralManager, didFailToConnectPeripheral: CBPeripheral, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518988-centralmanager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func centralManager(_ central: CBCentralManager!, didFailToConnectPeripheral peripheral: CBPeripheral!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func centralManager(_ central: CBCentralManager, didFailToConnectPeripheral peripheral: CBPeripheral, error error: NSError?) ``` | iOS 5.0 |

Modified [CBCentralManagerDelegate.centralManager(_: CBCentralManager, willRestoreState: [String : AnyObject])](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518819-centralmanager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func centralManager(_ central: CBCentralManager!, willRestoreState dict: [NSObject : AnyObject]!) ``` | iOS 8.0 |
| To | ``` optional func centralManager(_ central: CBCentralManager, willRestoreState dict: [String : AnyObject]) ``` | iOS 5.0 |

Modified [CBCentralManagerDelegate.centralManagerDidUpdateState(_: CBCentralManager)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518888-centralmanagerdidupdatestate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func centralManagerDidUpdateState(_ central: CBCentralManager!) ``` | iOS 8.0 |
| To | ``` func centralManagerDidUpdateState(_ central: CBCentralManager) ``` | iOS 5.0 |

Modified [CBCentralManagerState [enum]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CBCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` class CBCharacteristic : CBAttribute {     weak var service: CBService! { get }     var properties: CBCharacteristicProperties { get }     var value: NSData! { get }     var descriptors: [AnyObject]! { get }     var isBroadcasted: Bool { get }     var isNotifying: Bool { get } } ``` |
| To | ``` class CBCharacteristic : CBAttribute {     unowned(unsafe) var service: CBService { get }     var properties: CBCharacteristicProperties { get }     var value: NSData? { get }     var descriptors: [CBDescriptor]? { get }     var isBroadcasted: Bool { get }     var isNotifying: Bool { get } } ``` |

Modified [CBCharacteristic.descriptors](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518957-descriptors)

|  | Declaration |
| --- | --- |
| From | ``` var descriptors: [AnyObject]! { get } ``` |
| To | ``` var descriptors: [CBDescriptor]? { get } ``` |

Modified [CBCharacteristic.service](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518728-service)

|  | Declaration |
| --- | --- |
| From | ``` weak var service: CBService! { get } ``` |
| To | ``` unowned(unsafe) var service: CBService { get } ``` |

Modified [CBCharacteristic.value](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518878-value)

|  | Declaration |
| --- | --- |
| From | ``` var value: NSData! { get } ``` |
| To | ``` var value: NSData? { get } ``` |

Modified [CBCharacteristicProperties [struct]](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBCharacteristicProperties : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Broadcast: CBCharacteristicProperties { get }     static var Read: CBCharacteristicProperties { get }     static var WriteWithoutResponse: CBCharacteristicProperties { get }     static var Write: CBCharacteristicProperties { get }     static var Notify: CBCharacteristicProperties { get }     static var Indicate: CBCharacteristicProperties { get }     static var AuthenticatedSignedWrites: CBCharacteristicProperties { get }     static var ExtendedProperties: CBCharacteristicProperties { get }     static var NotifyEncryptionRequired: CBCharacteristicProperties { get }     static var IndicateEncryptionRequired: CBCharacteristicProperties { get } } ``` | RawOptionSetType |
| To | ``` struct CBCharacteristicProperties : OptionSetType {     init(rawValue rawValue: UInt)     static var Broadcast: CBCharacteristicProperties { get }     static var Read: CBCharacteristicProperties { get }     static var WriteWithoutResponse: CBCharacteristicProperties { get }     static var Write: CBCharacteristicProperties { get }     static var Notify: CBCharacteristicProperties { get }     static var Indicate: CBCharacteristicProperties { get }     static var AuthenticatedSignedWrites: CBCharacteristicProperties { get }     static var ExtendedProperties: CBCharacteristicProperties { get }     static var NotifyEncryptionRequired: CBCharacteristicProperties { get }     static var IndicateEncryptionRequired: CBCharacteristicProperties { get } } ``` | OptionSetType |

Modified [CBCharacteristicWriteType [enum]](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CBDescriptor](https://developer.apple.com/documentation/corebluetooth/cbdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` class CBDescriptor : CBAttribute {     weak var characteristic: CBCharacteristic! { get }     var value: AnyObject! { get } } ``` |
| To | ``` class CBDescriptor : CBAttribute {     unowned(unsafe) var characteristic: CBCharacteristic { get }     var value: AnyObject? { get } } ``` |

Modified [CBDescriptor.characteristic](https://developer.apple.com/documentation/corebluetooth/cbdescriptor/1519035-characteristic)

|  | Declaration |
| --- | --- |
| From | ``` weak var characteristic: CBCharacteristic! { get } ``` |
| To | ``` unowned(unsafe) var characteristic: CBCharacteristic { get } ``` |

Modified [CBDescriptor.value](https://developer.apple.com/documentation/corebluetooth/cbdescriptor/1518778-value)

|  | Declaration |
| --- | --- |
| From | ``` var value: AnyObject! { get } ``` |
| To | ``` var value: AnyObject? { get } ``` |

Modified [CBError [enum]](https://developer.apple.com/documentation/corebluetooth/cberror)

|  | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- |
| From | ``` enum CBError : Int {     case Unknown     case InvalidParameters     case InvalidHandle     case NotConnected     case OutOfSpace     case OperationCancelled     case ConnectionTimeout     case PeripheralDisconnected     case UUIDNotAllowed     case AlreadyAdvertising     case ConnectionFailed } ``` | Equatable, Hashable, RawRepresentable | -- |
| To | ``` enum CBError : Int {     case Unknown     case InvalidParameters     case InvalidHandle     case NotConnected     case OutOfSpace     case OperationCancelled     case ConnectionTimeout     case PeripheralDisconnected     case UUIDNotAllowed     case AlreadyAdvertising     case ConnectionFailed     case ConnectionLimitReached } extension CBError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension CBError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable | Int |

Modified [CBMutableCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` class CBMutableCharacteristic : CBCharacteristic {     var permissions: CBAttributePermissions     var subscribedCentrals: [AnyObject]! { get }     var UUID: CBUUID!     var properties: CBCharacteristicProperties     var value: NSData!     var descriptors: [AnyObject]!     init!(type UUID: CBUUID!, properties properties: CBCharacteristicProperties, value value: NSData!, permissions permissions: CBAttributePermissions) } ``` |
| To | ``` class CBMutableCharacteristic : CBCharacteristic {     var permissions: CBAttributePermissions     var subscribedCentrals: [CBCentral]? { get }     var properties: CBCharacteristicProperties     var value: NSData?     var descriptors: [CBDescriptor]?     init(type UUID: CBUUID, properties properties: CBCharacteristicProperties, value value: NSData?, permissions permissions: CBAttributePermissions) } ``` |

Modified [CBMutableCharacteristic.descriptors](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1518827-descriptors)

|  | Declaration |
| --- | --- |
| From | ``` var descriptors: [AnyObject]! ``` |
| To | ``` var descriptors: [CBDescriptor]? ``` |

Modified [CBMutableCharacteristic.init(type: CBUUID, properties: CBCharacteristicProperties, value: NSData?, permissions: CBAttributePermissions)](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1519073-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` init!(type UUID: CBUUID!, properties properties: CBCharacteristicProperties, value value: NSData!, permissions permissions: CBAttributePermissions) ``` |
| To | ``` init(type UUID: CBUUID, properties properties: CBCharacteristicProperties, value value: NSData?, permissions permissions: CBAttributePermissions) ``` |

Modified [CBMutableCharacteristic.subscribedCentrals](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1518926-subscribedcentrals)

|  | Declaration |
| --- | --- |
| From | ``` var subscribedCentrals: [AnyObject]! { get } ``` |
| To | ``` var subscribedCentrals: [CBCentral]? { get } ``` |

Modified [CBMutableCharacteristic.value](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1519121-value)

|  | Declaration |
| --- | --- |
| From | ``` var value: NSData! ``` |
| To | ``` var value: NSData? ``` |

Modified [CBMutableDescriptor](https://developer.apple.com/documentation/corebluetooth/cbmutabledescriptor)

|  | Declaration |
| --- | --- |
| From | ``` class CBMutableDescriptor : CBDescriptor {     init!(type UUID: CBUUID!, value value: AnyObject!) } ``` |
| To | ``` class CBMutableDescriptor : CBDescriptor {     init(type UUID: CBUUID, value value: AnyObject?) } ``` |

Modified [CBMutableDescriptor.init(type: CBUUID, value: AnyObject?)](https://developer.apple.com/documentation/corebluetooth/cbmutabledescriptor/1518999-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` init!(type UUID: CBUUID!, value value: AnyObject!) ``` |
| To | ``` init(type UUID: CBUUID, value value: AnyObject?) ``` |

Modified [CBMutableService](https://developer.apple.com/documentation/corebluetooth/cbmutableservice)

|  | Declaration |
| --- | --- |
| From | ``` class CBMutableService : CBService {     var UUID: CBUUID!     var isPrimary: Bool     var includedServices: [AnyObject]!     var characteristics: [AnyObject]!     init!(type UUID: CBUUID!, primary isPrimary: Bool) } ``` |
| To | ``` class CBMutableService : CBService {     var includedServices: [CBService]?     var characteristics: [CBCharacteristic]?     init(type UUID: CBUUID, primary isPrimary: Bool) } ``` |

Modified [CBMutableService.characteristics](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/1434317-characteristics)

|  | Declaration |
| --- | --- |
| From | ``` var characteristics: [AnyObject]! ``` |
| To | ``` var characteristics: [CBCharacteristic]? ``` |

Modified [CBMutableService.includedServices](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/1434320-includedservices)

|  | Declaration |
| --- | --- |
| From | ``` var includedServices: [AnyObject]! ``` |
| To | ``` var includedServices: [CBService]? ``` |

Modified [CBMutableService.init(type: CBUUID, primary: Bool)](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/1434330-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` init!(type UUID: CBUUID!, primary isPrimary: Bool) ``` |
| To | ``` init(type UUID: CBUUID, primary isPrimary: Bool) ``` |

Modified [CBPeer](https://developer.apple.com/documentation/corebluetooth/cbpeer)

|  | Declaration |
| --- | --- |
| From | ``` class CBPeer : NSObject, NSCopying {     var UUID: CFUUID! { get }     var identifier: NSUUID! { get } } ``` |
| To | ``` class CBPeer : NSObject, NSCopying {     init()     var identifier: NSUUID { get } } ``` |

Modified [CBPeer.identifier](https://developer.apple.com/documentation/corebluetooth/cbpeer/1620687-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: NSUUID! { get } ``` |
| To | ``` var identifier: NSUUID { get } ``` |

Modified [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral)

|  | Declaration |
| --- | --- |
| From | ``` class CBPeripheral : CBPeer {     weak var delegate: CBPeripheralDelegate!     var name: String! { get }     var RSSI: NSNumber! { get }     var isConnected: Bool { get }     var state: CBPeripheralState { get }     var services: [AnyObject]! { get }     func readRSSI()     func discoverServices(_ serviceUUIDs: [AnyObject]!)     func discoverIncludedServices(_ includedServiceUUIDs: [AnyObject]!, forService service: CBService!)     func discoverCharacteristics(_ characteristicUUIDs: [AnyObject]!, forService service: CBService!)     func readValueForCharacteristic(_ characteristic: CBCharacteristic!)     func writeValue(_ data: NSData!, forCharacteristic characteristic: CBCharacteristic!, type type: CBCharacteristicWriteType)     func setNotifyValue(_ enabled: Bool, forCharacteristic characteristic: CBCharacteristic!)     func discoverDescriptorsForCharacteristic(_ characteristic: CBCharacteristic!)     func readValueForDescriptor(_ descriptor: CBDescriptor!)     func writeValue(_ data: NSData!, forDescriptor descriptor: CBDescriptor!) } ``` |
| To | ``` class CBPeripheral : CBPeer {     unowned(unsafe) var delegate: CBPeripheralDelegate?     var name: String? { get }     var RSSI: NSNumber? { get }     var state: CBPeripheralState { get }     var services: [CBService]? { get }     func readRSSI()     func discoverServices(_ serviceUUIDs: [CBUUID]?)     func discoverIncludedServices(_ includedServiceUUIDs: [CBUUID]?, forService service: CBService)     func discoverCharacteristics(_ characteristicUUIDs: [CBUUID]?, forService service: CBService)     func readValueForCharacteristic(_ characteristic: CBCharacteristic)     func maximumWriteValueLengthForType(_ type: CBCharacteristicWriteType) -> Int     func writeValue(_ data: NSData, forCharacteristic characteristic: CBCharacteristic, type type: CBCharacteristicWriteType)     func setNotifyValue(_ enabled: Bool, forCharacteristic characteristic: CBCharacteristic)     func discoverDescriptorsForCharacteristic(_ characteristic: CBCharacteristic)     func readValueForDescriptor(_ descriptor: CBDescriptor)     func writeValue(_ data: NSData, forDescriptor descriptor: CBDescriptor) } ``` |

Modified [CBPeripheral.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518730-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: CBPeripheralDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: CBPeripheralDelegate? ``` |

Modified [CBPeripheral.discoverCharacteristics(_: [CBUUID]?, forService: CBService)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518797-discovercharacteristics)

|  | Declaration |
| --- | --- |
| From | ``` func discoverCharacteristics(_ characteristicUUIDs: [AnyObject]!, forService service: CBService!) ``` |
| To | ``` func discoverCharacteristics(_ characteristicUUIDs: [CBUUID]?, forService service: CBService) ``` |

Modified [CBPeripheral.discoverDescriptorsForCharacteristic(_: CBCharacteristic)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519070-discoverdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` func discoverDescriptorsForCharacteristic(_ characteristic: CBCharacteristic!) ``` |
| To | ``` func discoverDescriptorsForCharacteristic(_ characteristic: CBCharacteristic) ``` |

Modified [CBPeripheral.discoverIncludedServices(_: [CBUUID]?, forService: CBService)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519014-discoverincludedservices)

|  | Declaration |
| --- | --- |
| From | ``` func discoverIncludedServices(_ includedServiceUUIDs: [AnyObject]!, forService service: CBService!) ``` |
| To | ``` func discoverIncludedServices(_ includedServiceUUIDs: [CBUUID]?, forService service: CBService) ``` |

Modified [CBPeripheral.discoverServices(_: [CBUUID]?)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518706-discoverservices)

|  | Declaration |
| --- | --- |
| From | ``` func discoverServices(_ serviceUUIDs: [AnyObject]!) ``` |
| To | ``` func discoverServices(_ serviceUUIDs: [CBUUID]?) ``` |

Modified [CBPeripheral.name](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519029-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified [CBPeripheral.readValueForCharacteristic(_: CBCharacteristic)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518759-readvalueforcharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` func readValueForCharacteristic(_ characteristic: CBCharacteristic!) ``` |
| To | ``` func readValueForCharacteristic(_ characteristic: CBCharacteristic) ``` |

Modified [CBPeripheral.readValueForDescriptor(_: CBDescriptor)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518789-readvaluefordescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func readValueForDescriptor(_ descriptor: CBDescriptor!) ``` |
| To | ``` func readValueForDescriptor(_ descriptor: CBDescriptor) ``` |

Modified [CBPeripheral.RSSI](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518869-rssi)

|  | Declaration |
| --- | --- |
| From | ``` var RSSI: NSNumber! { get } ``` |
| To | ``` var RSSI: NSNumber? { get } ``` |

Modified [CBPeripheral.services](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518978-services)

|  | Declaration |
| --- | --- |
| From | ``` var services: [AnyObject]! { get } ``` |
| To | ``` var services: [CBService]? { get } ``` |

Modified [CBPeripheral.setNotifyValue(_: Bool, forCharacteristic: CBCharacteristic)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518949-setnotifyvalue)

|  | Declaration |
| --- | --- |
| From | ``` func setNotifyValue(_ enabled: Bool, forCharacteristic characteristic: CBCharacteristic!) ``` |
| To | ``` func setNotifyValue(_ enabled: Bool, forCharacteristic characteristic: CBCharacteristic) ``` |

Modified [CBPeripheral.writeValue(_: NSData, forCharacteristic: CBCharacteristic, type: CBCharacteristicWriteType)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518747-writevalue)

|  | Declaration |
| --- | --- |
| From | ``` func writeValue(_ data: NSData!, forCharacteristic characteristic: CBCharacteristic!, type type: CBCharacteristicWriteType) ``` |
| To | ``` func writeValue(_ data: NSData, forCharacteristic characteristic: CBCharacteristic, type type: CBCharacteristicWriteType) ``` |

Modified [CBPeripheral.writeValue(_: NSData, forDescriptor: CBDescriptor)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519107-writevalue)

|  | Declaration |
| --- | --- |
| From | ``` func writeValue(_ data: NSData!, forDescriptor descriptor: CBDescriptor!) ``` |
| To | ``` func writeValue(_ data: NSData, forDescriptor descriptor: CBDescriptor) ``` |

Modified [CBPeripheralDelegate](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol CBPeripheralDelegate : NSObjectProtocol {     optional func peripheralDidUpdateName(_ peripheral: CBPeripheral!)     optional func peripheralDidInvalidateServices(_ peripheral: CBPeripheral!)     optional func peripheral(_ peripheral: CBPeripheral!, didModifyServices invalidatedServices: [AnyObject]!)     optional func peripheralDidUpdateRSSI(_ peripheral: CBPeripheral!, error error: NSError!)     optional func peripheral(_ peripheral: CBPeripheral!, didReadRSSI RSSI: NSNumber!, error error: NSError!)     optional func peripheral(_ peripheral: CBPeripheral!, didDiscoverServices error: NSError!)     optional func peripheral(_ peripheral: CBPeripheral!, didDiscoverIncludedServicesForService service: CBService!, error error: NSError!)     optional func peripheral(_ peripheral: CBPeripheral!, didDiscoverCharacteristicsForService service: CBService!, error error: NSError!)     optional func peripheral(_ peripheral: CBPeripheral!, didUpdateValueForCharacteristic characteristic: CBCharacteristic!, error error: NSError!)     optional func peripheral(_ peripheral: CBPeripheral!, didWriteValueForCharacteristic characteristic: CBCharacteristic!, error error: NSError!)     optional func peripheral(_ peripheral: CBPeripheral!, didUpdateNotificationStateForCharacteristic characteristic: CBCharacteristic!, error error: NSError!)     optional func peripheral(_ peripheral: CBPeripheral!, didDiscoverDescriptorsForCharacteristic characteristic: CBCharacteristic!, error error: NSError!)     optional func peripheral(_ peripheral: CBPeripheral!, didUpdateValueForDescriptor descriptor: CBDescriptor!, error error: NSError!)     optional func peripheral(_ peripheral: CBPeripheral!, didWriteValueForDescriptor descriptor: CBDescriptor!, error error: NSError!) } ``` |
| To | ``` protocol CBPeripheralDelegate : NSObjectProtocol {     optional func peripheralDidUpdateName(_ peripheral: CBPeripheral)     optional func peripheral(_ peripheral: CBPeripheral, didModifyServices invalidatedServices: [CBService])     optional func peripheralDidUpdateRSSI(_ peripheral: CBPeripheral, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didReadRSSI RSSI: NSNumber, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didDiscoverIncludedServicesForService service: CBService, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsForService service: CBService, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueForCharacteristic characteristic: CBCharacteristic, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didWriteValueForCharacteristic characteristic: CBCharacteristic, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didUpdateNotificationStateForCharacteristic characteristic: CBCharacteristic, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didDiscoverDescriptorsForCharacteristic characteristic: CBCharacteristic, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueForDescriptor descriptor: CBDescriptor, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didWriteValueForDescriptor descriptor: CBDescriptor, error error: NSError?) } ``` |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didDiscoverCharacteristicsForService: CBService, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518821-peripheral)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral!, didDiscoverCharacteristicsForService service: CBService!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsForService service: CBService, error error: NSError?) ``` | iOS 5.0 |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didDiscoverDescriptorsForCharacteristic: CBCharacteristic, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518785-peripheral)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral!, didDiscoverDescriptorsForCharacteristic characteristic: CBCharacteristic!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didDiscoverDescriptorsForCharacteristic characteristic: CBCharacteristic, error error: NSError?) ``` | iOS 5.0 |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didDiscoverIncludedServicesForService: CBService, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519124-peripheral)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral!, didDiscoverIncludedServicesForService service: CBService!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didDiscoverIncludedServicesForService service: CBService, error error: NSError?) ``` | iOS 5.0 |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didDiscoverServices: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518744-peripheral)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral!, didDiscoverServices error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: NSError?) ``` | iOS 5.0 |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didModifyServices: [CBService])](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518865-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral!, didModifyServices invalidatedServices: [AnyObject]!) ``` |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didModifyServices invalidatedServices: [CBService]) ``` |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didReadRSSI: NSNumber, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1620304-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral!, didReadRSSI RSSI: NSNumber!, error error: NSError!) ``` |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didReadRSSI RSSI: NSNumber, error error: NSError?) ``` |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didUpdateNotificationStateForCharacteristic: CBCharacteristic, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518768-peripheral)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral!, didUpdateNotificationStateForCharacteristic characteristic: CBCharacteristic!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didUpdateNotificationStateForCharacteristic characteristic: CBCharacteristic, error error: NSError?) ``` | iOS 5.0 |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didUpdateValueForCharacteristic: CBCharacteristic, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518708-peripheral)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral!, didUpdateValueForCharacteristic characteristic: CBCharacteristic!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueForCharacteristic characteristic: CBCharacteristic, error error: NSError?) ``` | iOS 5.0 |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didUpdateValueForDescriptor: CBDescriptor, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518929-peripheral)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral!, didUpdateValueForDescriptor descriptor: CBDescriptor!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueForDescriptor descriptor: CBDescriptor, error error: NSError?) ``` | iOS 5.0 |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didWriteValueForCharacteristic: CBCharacteristic, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518823-peripheral)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral!, didWriteValueForCharacteristic characteristic: CBCharacteristic!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didWriteValueForCharacteristic characteristic: CBCharacteristic, error error: NSError?) ``` | iOS 5.0 |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didWriteValueForDescriptor: CBDescriptor, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519062-peripheral)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral!, didWriteValueForDescriptor descriptor: CBDescriptor!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didWriteValueForDescriptor descriptor: CBDescriptor, error error: NSError?) ``` | iOS 5.0 |

Modified [CBPeripheralDelegate.peripheralDidUpdateName(_: CBPeripheral)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518801-peripheraldidupdatename)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheralDidUpdateName(_ peripheral: CBPeripheral!) ``` |
| To | ``` optional func peripheralDidUpdateName(_ peripheral: CBPeripheral) ``` |

Modified [CBPeripheralDelegate.peripheralDidUpdateRSSI(_: CBPeripheral, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519083-peripheraldidupdaterssi)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheralDidUpdateRSSI(_ peripheral: CBPeripheral!, error error: NSError!) ``` |
| To | ``` optional func peripheralDidUpdateRSSI(_ peripheral: CBPeripheral, error error: NSError?) ``` |

Modified [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager)

|  | Declaration |
| --- | --- |
| From | ``` class CBPeripheralManager : NSObject {     weak var delegate: CBPeripheralManagerDelegate!     var state: CBPeripheralManagerState { get }     var isAdvertising: Bool { get }     class func authorizationStatus() -> CBPeripheralManagerAuthorizationStatus     convenience init!(delegate delegate: CBPeripheralManagerDelegate!, queue queue: dispatch_queue_t!)     init!(delegate delegate: CBPeripheralManagerDelegate!, queue queue: dispatch_queue_t!, options options: [NSObject : AnyObject]!)     func startAdvertising(_ advertisementData: [NSObject : AnyObject]!)     func stopAdvertising()     func setDesiredConnectionLatency(_ latency: CBPeripheralManagerConnectionLatency, forCentral central: CBCentral!)     func addService(_ service: CBMutableService!)     func removeService(_ service: CBMutableService!)     func removeAllServices()     func respondToRequest(_ request: CBATTRequest!, withResult result: CBATTError)     func updateValue(_ value: NSData!, forCharacteristic characteristic: CBMutableCharacteristic!, onSubscribedCentrals centrals: [AnyObject]!) -> Bool } ``` |
| To | ``` class CBPeripheralManager : NSObject {     unowned(unsafe) var delegate: CBPeripheralManagerDelegate?     var state: CBPeripheralManagerState { get }     var isAdvertising: Bool { get }     class func authorizationStatus() -> CBPeripheralManagerAuthorizationStatus     convenience init(delegate delegate: CBPeripheralManagerDelegate?, queue queue: dispatch_queue_t?)     init(delegate delegate: CBPeripheralManagerDelegate?, queue queue: dispatch_queue_t?, options options: [String : AnyObject]?)     func startAdvertising(_ advertisementData: [String : AnyObject]?)     func stopAdvertising()     func setDesiredConnectionLatency(_ latency: CBPeripheralManagerConnectionLatency, forCentral central: CBCentral)     func addService(_ service: CBMutableService)     func removeService(_ service: CBMutableService)     func removeAllServices()     func respondToRequest(_ request: CBATTRequest, withResult result: CBATTError)     func updateValue(_ value: NSData, forCharacteristic characteristic: CBMutableCharacteristic, onSubscribedCentrals centrals: [CBCentral]?) -> Bool } ``` |

Modified [CBPeripheralManager.addService(_: CBMutableService)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393255-addservice)

|  | Declaration |
| --- | --- |
| From | ``` func addService(_ service: CBMutableService!) ``` |
| To | ``` func addService(_ service: CBMutableService) ``` |

Modified [CBPeripheralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393313-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: CBPeripheralManagerDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: CBPeripheralManagerDelegate? ``` |

Modified [CBPeripheralManager.init(delegate: CBPeripheralManagerDelegate?, queue: dispatch_queue_t?)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393299-initwithdelegate)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(delegate delegate: CBPeripheralManagerDelegate!, queue queue: dispatch_queue_t!) ``` |
| To | ``` convenience init(delegate delegate: CBPeripheralManagerDelegate?, queue queue: dispatch_queue_t?) ``` |

Modified [CBPeripheralManager.init(delegate: CBPeripheralManagerDelegate?, queue: dispatch_queue_t?, options: [String : AnyObject]?)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393295-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(delegate delegate: CBPeripheralManagerDelegate!, queue queue: dispatch_queue_t!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` init(delegate delegate: CBPeripheralManagerDelegate?, queue queue: dispatch_queue_t?, options options: [String : AnyObject]?) ``` |

Modified [CBPeripheralManager.removeService(_: CBMutableService)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393287-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeService(_ service: CBMutableService!) ``` |
| To | ``` func removeService(_ service: CBMutableService) ``` |

Modified [CBPeripheralManager.respondToRequest(_: CBATTRequest, withResult: CBATTError)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393293-respond)

|  | Declaration |
| --- | --- |
| From | ``` func respondToRequest(_ request: CBATTRequest!, withResult result: CBATTError) ``` |
| To | ``` func respondToRequest(_ request: CBATTRequest, withResult result: CBATTError) ``` |

Modified [CBPeripheralManager.setDesiredConnectionLatency(_: CBPeripheralManagerConnectionLatency, forCentral: CBCentral)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393277-setdesiredconnectionlatency)

|  | Declaration |
| --- | --- |
| From | ``` func setDesiredConnectionLatency(_ latency: CBPeripheralManagerConnectionLatency, forCentral central: CBCentral!) ``` |
| To | ``` func setDesiredConnectionLatency(_ latency: CBPeripheralManagerConnectionLatency, forCentral central: CBCentral) ``` |

Modified [CBPeripheralManager.startAdvertising(_: [String : AnyObject]?)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393252-startadvertising)

|  | Declaration |
| --- | --- |
| From | ``` func startAdvertising(_ advertisementData: [NSObject : AnyObject]!) ``` |
| To | ``` func startAdvertising(_ advertisementData: [String : AnyObject]?) ``` |

Modified [CBPeripheralManager.updateValue(_: NSData, forCharacteristic: CBMutableCharacteristic, onSubscribedCentrals: [CBCentral]?) -> Bool](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393281-updatevalue)

|  | Declaration |
| --- | --- |
| From | ``` func updateValue(_ value: NSData!, forCharacteristic characteristic: CBMutableCharacteristic!, onSubscribedCentrals centrals: [AnyObject]!) -> Bool ``` |
| To | ``` func updateValue(_ value: NSData, forCharacteristic characteristic: CBMutableCharacteristic, onSubscribedCentrals centrals: [CBCentral]?) -> Bool ``` |

Modified [CBPeripheralManagerAuthorizationStatus [enum]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CBPeripheralManagerConnectionLatency [enum]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerconnectionlatency)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CBPeripheralManagerDelegate](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol CBPeripheralManagerDelegate : NSObjectProtocol {     func peripheralManagerDidUpdateState(_ peripheral: CBPeripheralManager!)     optional func peripheralManager(_ peripheral: CBPeripheralManager!, willRestoreState dict: [NSObject : AnyObject]!)     optional func peripheralManagerDidStartAdvertising(_ peripheral: CBPeripheralManager!, error error: NSError!)     optional func peripheralManager(_ peripheral: CBPeripheralManager!, didAddService service: CBService!, error error: NSError!)     optional func peripheralManager(_ peripheral: CBPeripheralManager!, central central: CBCentral!, didSubscribeToCharacteristic characteristic: CBCharacteristic!)     optional func peripheralManager(_ peripheral: CBPeripheralManager!, central central: CBCentral!, didUnsubscribeFromCharacteristic characteristic: CBCharacteristic!)     optional func peripheralManager(_ peripheral: CBPeripheralManager!, didReceiveReadRequest request: CBATTRequest!)     optional func peripheralManager(_ peripheral: CBPeripheralManager!, didReceiveWriteRequests requests: [AnyObject]!)     optional func peripheralManagerIsReadyToUpdateSubscribers(_ peripheral: CBPeripheralManager!) } ``` |
| To | ``` protocol CBPeripheralManagerDelegate : NSObjectProtocol {     func peripheralManagerDidUpdateState(_ peripheral: CBPeripheralManager)     optional func peripheralManager(_ peripheral: CBPeripheralManager, willRestoreState dict: [String : AnyObject])     optional func peripheralManagerDidStartAdvertising(_ peripheral: CBPeripheralManager, error error: NSError?)     optional func peripheralManager(_ peripheral: CBPeripheralManager, didAddService service: CBService, error error: NSError?)     optional func peripheralManager(_ peripheral: CBPeripheralManager, central central: CBCentral, didSubscribeToCharacteristic characteristic: CBCharacteristic)     optional func peripheralManager(_ peripheral: CBPeripheralManager, central central: CBCentral, didUnsubscribeFromCharacteristic characteristic: CBCharacteristic)     optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveReadRequest request: CBATTRequest)     optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveWriteRequests requests: [CBATTRequest])     optional func peripheralManagerIsReadyToUpdateSubscribers(_ peripheral: CBPeripheralManager) } ``` |

Modified [CBPeripheralManagerDelegate.peripheralManager(_: CBPeripheralManager, central: CBCentral, didSubscribeToCharacteristic: CBCharacteristic)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393261-peripheralmanager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager!, central central: CBCentral!, didSubscribeToCharacteristic characteristic: CBCharacteristic!) ``` | iOS 8.0 |
| To | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, central central: CBCentral, didSubscribeToCharacteristic characteristic: CBCharacteristic) ``` | iOS 6.0 |

Modified [CBPeripheralManagerDelegate.peripheralManager(_: CBPeripheralManager, central: CBCentral, didUnsubscribeFromCharacteristic: CBCharacteristic)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393289-peripheralmanager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager!, central central: CBCentral!, didUnsubscribeFromCharacteristic characteristic: CBCharacteristic!) ``` | iOS 8.0 |
| To | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, central central: CBCentral, didUnsubscribeFromCharacteristic characteristic: CBCharacteristic) ``` | iOS 6.0 |

Modified [CBPeripheralManagerDelegate.peripheralManager(_: CBPeripheralManager, didAddService: CBService, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393279-peripheralmanager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager!, didAddService service: CBService!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, didAddService service: CBService, error error: NSError?) ``` | iOS 6.0 |

Modified [CBPeripheralManagerDelegate.peripheralManager(_: CBPeripheralManager, didReceiveReadRequest: CBATTRequest)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393257-peripheralmanager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager!, didReceiveReadRequest request: CBATTRequest!) ``` | iOS 8.0 |
| To | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveReadRequest request: CBATTRequest) ``` | iOS 6.0 |

Modified [CBPeripheralManagerDelegate.peripheralManager(_: CBPeripheralManager, didReceiveWriteRequests: [CBATTRequest])](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393315-peripheralmanager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager!, didReceiveWriteRequests requests: [AnyObject]!) ``` | iOS 8.0 |
| To | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveWriteRequests requests: [CBATTRequest]) ``` | iOS 6.0 |

Modified [CBPeripheralManagerDelegate.peripheralManager(_: CBPeripheralManager, willRestoreState: [String : AnyObject])](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393317-peripheralmanager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager!, willRestoreState dict: [NSObject : AnyObject]!) ``` | iOS 8.0 |
| To | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, willRestoreState dict: [String : AnyObject]) ``` | iOS 6.0 |

Modified [CBPeripheralManagerDelegate.peripheralManagerDidStartAdvertising(_: CBPeripheralManager, error: NSError?)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393321-peripheralmanagerdidstartadverti)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheralManagerDidStartAdvertising(_ peripheral: CBPeripheralManager!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func peripheralManagerDidStartAdvertising(_ peripheral: CBPeripheralManager, error error: NSError?) ``` | iOS 6.0 |

Modified [CBPeripheralManagerDelegate.peripheralManagerDidUpdateState(_: CBPeripheralManager)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393271-peripheralmanagerdidupdatestate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func peripheralManagerDidUpdateState(_ peripheral: CBPeripheralManager!) ``` | iOS 8.0 |
| To | ``` func peripheralManagerDidUpdateState(_ peripheral: CBPeripheralManager) ``` | iOS 6.0 |

Modified [CBPeripheralManagerDelegate.peripheralManagerIsReadyToUpdateSubscribers(_: CBPeripheralManager)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393248-peripheralmanagerisreadytoupdate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peripheralManagerIsReadyToUpdateSubscribers(_ peripheral: CBPeripheralManager!) ``` | iOS 8.0 |
| To | ``` optional func peripheralManagerIsReadyToUpdateSubscribers(_ peripheral: CBPeripheralManager) ``` | iOS 6.0 |

Modified [CBPeripheralManagerState [enum]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CBPeripheralState [enum]](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum CBPeripheralState : Int {     case Disconnected     case Connecting     case Connected } ``` | -- |
| To | ``` enum CBPeripheralState : Int {     case Disconnected     case Connecting     case Connected     case Disconnecting } ``` | Int |

Modified [CBService](https://developer.apple.com/documentation/corebluetooth/cbservice)

|  | Declaration |
| --- | --- |
| From | ``` class CBService : CBAttribute {     weak var peripheral: CBPeripheral! { get }     var isPrimary: Bool { get }     var includedServices: [AnyObject]! { get }     var characteristics: [AnyObject]! { get } } ``` |
| To | ``` class CBService : CBAttribute {     unowned(unsafe) var peripheral: CBPeripheral { get }     var isPrimary: Bool { get }     var includedServices: [CBService]? { get }     var characteristics: [CBCharacteristic]? { get } } ``` |

Modified [CBService.characteristics](https://developer.apple.com/documentation/corebluetooth/cbservice/1434319-characteristics)

|  | Declaration |
| --- | --- |
| From | ``` var characteristics: [AnyObject]! { get } ``` |
| To | ``` var characteristics: [CBCharacteristic]? { get } ``` |

Modified [CBService.includedServices](https://developer.apple.com/documentation/corebluetooth/cbservice/1434324-includedservices)

|  | Declaration |
| --- | --- |
| From | ``` var includedServices: [AnyObject]! { get } ``` |
| To | ``` var includedServices: [CBService]? { get } ``` |

Modified [CBService.peripheral](https://developer.apple.com/documentation/corebluetooth/cbservice/1434334-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` weak var peripheral: CBPeripheral! { get } ``` |
| To | ``` unowned(unsafe) var peripheral: CBPeripheral { get } ``` |

Modified [CBUUID](https://developer.apple.com/documentation/corebluetooth/cbuuid)

|  | Declaration |
| --- | --- |
| From | ``` class CBUUID : NSObject, NSCopying {     var data: NSData! { get }     var UUIDString: String! { get }     init!(string theString: String!) -> CBUUID     class func UUIDWithString(_ theString: String!) -> CBUUID!     init!(data theData: NSData!) -> CBUUID     class func UUIDWithData(_ theData: NSData!) -> CBUUID!     init!(CFUUID theUUID: CFUUID!) -> CBUUID     class func UUIDWithCFUUID(_ theUUID: CFUUID!) -> CBUUID!     init!(NSUUID theUUID: NSUUID!) -> CBUUID     class func UUIDWithNSUUID(_ theUUID: NSUUID!) -> CBUUID! } ``` |
| To | ``` class CBUUID : NSObject, NSCopying {     var data: NSData { get }     var UUIDString: String { get }      init(string theString: String)     class func UUIDWithString(_ theString: String) -> CBUUID      init(data theData: NSData)     class func UUIDWithData(_ theData: NSData) -> CBUUID      init(CFUUID theUUID: CFUUID)     class func UUIDWithCFUUID(_ theUUID: CFUUID) -> CBUUID      init(NSUUID theUUID: NSUUID)     class func UUIDWithNSUUID(_ theUUID: NSUUID) -> CBUUID } ``` |

Modified [CBUUID.data](https://developer.apple.com/documentation/corebluetooth/cbuuid/1519007-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` var data: NSData { get } ``` |

Modified [CBUUID.init(CFUUID: CFUUID)](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518861-uuidwithcfuuid)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init!(CFUUID theUUID: CFUUID!) -> CBUUID ``` | iOS 8.1 | -- |
| To | ``` init(CFUUID theUUID: CFUUID) ``` | iOS 5.0 | iOS 9.0 |

Modified [CBUUID.init(data: NSData)](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518799-uuidwithdata)

|  | Declaration |
| --- | --- |
| From | ``` init!(data theData: NSData!) -> CBUUID ``` |
| To | ``` init(data theData: NSData) ``` |

Modified [CBUUID.init(NSUUID: NSUUID)](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518783-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(NSUUID theUUID: NSUUID!) -> CBUUID ``` |
| To | ``` init(NSUUID theUUID: NSUUID) ``` |

Modified [CBUUID.init(string: String)](https://developer.apple.com/documentation/corebluetooth/cbuuid/1519025-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(string theString: String!) -> CBUUID ``` |
| To | ``` init(string theString: String) ``` |

Modified [CBUUID.UUIDString](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518742-uuidstring)

|  | Declaration |
| --- | --- |
| From | ``` var UUIDString: String! { get } ``` |
| To | ``` var UUIDString: String { get } ``` |

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
