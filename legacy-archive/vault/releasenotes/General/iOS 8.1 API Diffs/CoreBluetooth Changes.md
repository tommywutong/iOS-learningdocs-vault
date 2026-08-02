---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/CoreBluetooth.html
archived_at: '2026-07-18T02:56:08.128956Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# CoreBluetooth Changes

## CoreBluetooth

Removed CBAttributePermissions.valueRemoved CBCharacteristicProperties.valueAdded CBAttributePermissions.init(rawValue: UInt)Added CBCharacteristicProperties.init(rawValue: UInt)Modified CBATTRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBAttributePermissions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct CBAttributePermissions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Readable: CBAttributePermissions { get }     static var Writeable: CBAttributePermissions { get }     static var ReadEncryptionRequired: CBAttributePermissions { get }     static var WriteEncryptionRequired: CBAttributePermissions { get } } ``` | iOS 8.0 |
| To | ``` struct CBAttributePermissions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Readable: CBAttributePermissions { get }     static var Writeable: CBAttributePermissions { get }     static var ReadEncryptionRequired: CBAttributePermissions { get }     static var WriteEncryptionRequired: CBAttributePermissions { get } } ``` | iOS 6.0 |

Modified CBAttributePermissions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified CBCentral

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBCentralManager

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CBCentralManager.init(delegate: CBCentralManagerDelegate!, queue: dispatch_queue_t!)

|  | Declaration |
| --- | --- |
| From | ``` init(delegate delegate: CBCentralManagerDelegate!, queue queue: dispatch_queue_t!) ``` |
| To | ``` init!(delegate delegate: CBCentralManagerDelegate!, queue queue: dispatch_queue_t!) ``` |

Modified CBCentralManager.init(delegate: CBCentralManagerDelegate!, queue: dispatch_queue_t!, options:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(delegate delegate: CBCentralManagerDelegate!, queue queue: dispatch_queue_t!, options options: [NSObject : AnyObject]!) ``` | iOS 8.0 |
| To | ``` init!(delegate delegate: CBCentralManagerDelegate!, queue queue: dispatch_queue_t!, options options: [NSObject : AnyObject]!) ``` | iOS 7.0 |

Modified CBCentralManager.retrieveConnectedPeripheralsWithServices([AnyObject]!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBCentralManager.retrievePeripheralsWithIdentifiers([AnyObject]!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBCharacteristic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CBCharacteristic.isBroadcasted

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified CBCharacteristicProperties [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CBCharacteristicProperties : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Broadcast: CBCharacteristicProperties { get }     static var Read: CBCharacteristicProperties { get }     static var WriteWithoutResponse: CBCharacteristicProperties { get }     static var Write: CBCharacteristicProperties { get }     static var Notify: CBCharacteristicProperties { get }     static var Indicate: CBCharacteristicProperties { get }     static var AuthenticatedSignedWrites: CBCharacteristicProperties { get }     static var ExtendedProperties: CBCharacteristicProperties { get }     static var NotifyEncryptionRequired: CBCharacteristicProperties { get }     static var IndicateEncryptionRequired: CBCharacteristicProperties { get } } ``` |
| To | ``` struct CBCharacteristicProperties : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Broadcast: CBCharacteristicProperties { get }     static var Read: CBCharacteristicProperties { get }     static var WriteWithoutResponse: CBCharacteristicProperties { get }     static var Write: CBCharacteristicProperties { get }     static var Notify: CBCharacteristicProperties { get }     static var Indicate: CBCharacteristicProperties { get }     static var AuthenticatedSignedWrites: CBCharacteristicProperties { get }     static var ExtendedProperties: CBCharacteristicProperties { get }     static var NotifyEncryptionRequired: CBCharacteristicProperties { get }     static var IndicateEncryptionRequired: CBCharacteristicProperties { get } } ``` |

Modified CBCharacteristicProperties.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified CBDescriptor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CBMutableCharacteristic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBMutableCharacteristic.subscribedCentrals

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBMutableCharacteristic.init(type: CBUUID!, properties: CBCharacteristicProperties, value: NSData!, permissions: CBAttributePermissions)

|  | Declaration |
| --- | --- |
| From | ``` init(type UUID: CBUUID!, properties properties: CBCharacteristicProperties, value value: NSData!, permissions permissions: CBAttributePermissions) ``` |
| To | ``` init!(type UUID: CBUUID!, properties properties: CBCharacteristicProperties, value value: NSData!, permissions permissions: CBAttributePermissions) ``` |

Modified CBMutableDescriptor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBMutableDescriptor.init(type: CBUUID!, value: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(type UUID: CBUUID!, value value: AnyObject!) ``` |
| To | ``` init!(type UUID: CBUUID!, value value: AnyObject!) ``` |

Modified CBMutableService

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBMutableService.init(type: CBUUID!, primary: Bool)

|  | Declaration |
| --- | --- |
| From | ``` init(type UUID: CBUUID!, primary isPrimary: Bool) ``` |
| To | ``` init!(type UUID: CBUUID!, primary isPrimary: Bool) ``` |

Modified CBPeer.identifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBPeripheral

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CBPeripheral.RSSI

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified CBPeripheralDelegate.peripheral(CBPeripheral!, didModifyServices:[AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBPeripheralDelegate.peripheralDidUpdateName(CBPeripheral!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBPeripheralDelegate.peripheralDidUpdateRSSI(CBPeripheral!, error: NSError!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified CBPeripheralManager

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBPeripheralManager.authorizationStatus() -> CBPeripheralManagerAuthorizationStatus [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBPeripheralManager.init(delegate: CBPeripheralManagerDelegate!, queue: dispatch_queue_t!)

|  | Declaration |
| --- | --- |
| From | ``` init(delegate delegate: CBPeripheralManagerDelegate!, queue queue: dispatch_queue_t!) ``` |
| To | ``` init!(delegate delegate: CBPeripheralManagerDelegate!, queue queue: dispatch_queue_t!) ``` |

Modified CBPeripheralManager.init(delegate: CBPeripheralManagerDelegate!, queue: dispatch_queue_t!, options:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(delegate delegate: CBPeripheralManagerDelegate!, queue queue: dispatch_queue_t!, options options: [NSObject : AnyObject]!) ``` | iOS 8.0 |
| To | ``` init!(delegate delegate: CBPeripheralManagerDelegate!, queue queue: dispatch_queue_t!, options options: [NSObject : AnyObject]!) ``` | iOS 7.0 |

Modified CBPeripheralManagerAuthorizationStatus [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBPeripheralManagerConnectionLatency [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBPeripheralManagerState [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBPeripheralState [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBService

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CBUUID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CBUUID.init(CFUUID: CFUUID!)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | UUIDWithCFUUID(_:) | ``` class func UUIDWithCFUUID(_ theUUID: CFUUID!) -> CBUUID! ``` | iOS 8.0 |
| To | init(CFUUID:) | ``` init!(CFUUID theUUID: CFUUID!) -> CBUUID ``` | iOS 8.1 |

Modified CBUUID.init(NSUUID: NSUUID!)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | UUIDWithNSUUID(_:) | ``` class func UUIDWithNSUUID(_ theUUID: NSUUID!) -> CBUUID! ``` | iOS 8.0 |
| To | init(NSUUID:) | ``` init!(NSUUID theUUID: NSUUID!) -> CBUUID ``` | iOS 8.1 |

Modified CBUUID.UUIDString

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified CBUUID.init(data: NSData!)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | UUIDWithData(_:) | ``` class func UUIDWithData(_ theData: NSData!) -> CBUUID! ``` | iOS 8.0 |
| To | init(data:) | ``` init!(data theData: NSData!) -> CBUUID ``` | iOS 8.1 |

Modified CBUUID.init(string: String!)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | UUIDWithString(_:) | ``` class func UUIDWithString(_ theString: String!) -> CBUUID! ``` | iOS 8.0 |
| To | init(string:) | ``` init!(string theString: String!) -> CBUUID ``` | iOS 8.1 |

Modified CBAdvertisementDataIsConnectable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBAdvertisementDataOverflowServiceUUIDsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBAdvertisementDataSolicitedServiceUUIDsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBCentralManagerOptionRestoreIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBCentralManagerOptionShowPowerAlertKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBCentralManagerRestoredStatePeripheralsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBCentralManagerRestoredStateScanOptionsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBCentralManagerRestoredStateScanServicesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBCentralManagerScanOptionSolicitedServiceUUIDsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBConnectPeripheralOptionNotifyOnConnectionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBConnectPeripheralOptionNotifyOnNotificationKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBPeripheralManagerOptionRestoreIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBPeripheralManagerOptionShowPowerAlertKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBPeripheralManagerRestoredStateAdvertisementDataKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CBPeripheralManagerRestoredStateServicesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

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
