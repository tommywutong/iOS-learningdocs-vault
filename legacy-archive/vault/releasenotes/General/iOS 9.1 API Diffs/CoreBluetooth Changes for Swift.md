---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/CoreBluetooth.html
archived_at: '2026-07-18T02:57:07.105908Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# CoreBluetooth Changes for Swift

### CoreBluetooth

Modified [CBATTError [enum]](https://developer.apple.com/documentation/corebluetooth/cbatterror)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum CBATTError : Int {     case Success     case InvalidHandle     case ReadNotPermitted     case WriteNotPermitted     case InvalidPdu     case InsufficientAuthentication     case RequestNotSupported     case InvalidOffset     case InsufficientAuthorization     case PrepareQueueFull     case AttributeNotFound     case AttributeNotLong     case InsufficientEncryptionKeySize     case InvalidAttributeValueLength     case UnlikelyError     case InsufficientEncryption     case UnsupportedGroupType     case InsufficientResources } extension CBATTError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension CBATTError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum CBATTError : Int {     case Success     case InvalidHandle     case ReadNotPermitted     case WriteNotPermitted     case InvalidPdu     case InsufficientAuthentication     case RequestNotSupported     case InvalidOffset     case InsufficientAuthorization     case PrepareQueueFull     case AttributeNotFound     case AttributeNotLong     case InsufficientEncryptionKeySize     case InvalidAttributeValueLength     case UnlikelyError     case InsufficientEncryption     case UnsupportedGroupType     case InsufficientResources } extension CBATTError : _BridgedNSError { } extension CBATTError : _BridgedNSError { } ``` | -- |

Modified [CBATTRequest](https://developer.apple.com/documentation/corebluetooth/cbattrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CBAttribute](https://developer.apple.com/documentation/corebluetooth/cbattribute)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CBCentral](https://developer.apple.com/documentation/corebluetooth/cbcentral)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CBCentralManagerState [enum]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CBCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CBCharacteristicWriteType [enum]](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CBDescriptor](https://developer.apple.com/documentation/corebluetooth/cbdescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CBError [enum]](https://developer.apple.com/documentation/corebluetooth/cberror)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum CBError : Int {     case Unknown     case InvalidParameters     case InvalidHandle     case NotConnected     case OutOfSpace     case OperationCancelled     case ConnectionTimeout     case PeripheralDisconnected     case UUIDNotAllowed     case AlreadyAdvertising     case ConnectionFailed     case ConnectionLimitReached } extension CBError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension CBError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum CBError : Int {     case Unknown     case InvalidParameters     case InvalidHandle     case NotConnected     case OutOfSpace     case OperationCancelled     case ConnectionTimeout     case PeripheralDisconnected     case UUIDNotAllowed     case AlreadyAdvertising     case ConnectionFailed     case ConnectionLimitReached } extension CBError : _BridgedNSError { } extension CBError : _BridgedNSError { } ``` | -- |

Modified [CBMutableCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CBMutableDescriptor](https://developer.apple.com/documentation/corebluetooth/cbmutabledescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CBMutableService](https://developer.apple.com/documentation/corebluetooth/cbmutableservice)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CBPeer](https://developer.apple.com/documentation/corebluetooth/cbpeer)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CBPeripheralManagerAuthorizationStatus [enum]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CBPeripheralManagerConnectionLatency [enum]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerconnectionlatency)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CBPeripheralManagerState [enum]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CBPeripheralState [enum]](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CBService](https://developer.apple.com/documentation/corebluetooth/cbservice)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CBUUID](https://developer.apple.com/documentation/corebluetooth/cbuuid)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

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
