---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/CoreBluetooth.html
archived_at: '2026-07-18T02:54:54.276169Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# CoreBluetooth Changes for Objective-C

### CoreBluetooth

#### CBCentralManager.h

Removed CBCentralManager.stateAdded [-[CBCentralManager init]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1648596-init)Modified [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager)

|  | Superclasses |
| --- | --- |
| From | NSObject |
| To | CBManager |

Modified [CBCentralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518944-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) id<CBCentralManagerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak) id<CBCentralManagerDelegate> delegate ``` |

Modified [CBCentralManager.isScanning](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1620640-isscanning)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) BOOL isScanning ``` |
| To | ``` @property(nonatomic, assign, readonly) BOOL isScanning ``` |

Modified [CBCentralManagerStatePoweredOff](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/cbcentralmanagerstatepoweredoff)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CBCentralManagerStatePoweredOn](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/poweredon)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CBCentralManagerStateResetting](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/cbcentralmanagerstateresetting)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CBCentralManagerStateUnauthorized](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/cbcentralmanagerstateunauthorized)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CBCentralManagerStateUnknown](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/unknown)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CBCentralManagerStateUnsupported](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/unsupported)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### CBManager.h (Added)

Added [CBManager](https://developer.apple.com/documentation/corebluetooth/cbmanager)Added [CBManager.state](https://developer.apple.com/documentation/corebluetooth/cbmanager/1648600-state)Added [CBManagerState](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate)Added [CBManagerStatePoweredOff](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/poweredoff)Added [CBManagerStatePoweredOn](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/cbmanagerstatepoweredon)Added [CBManagerStateResetting](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/cbmanagerstateresetting)Added [CBManagerStateUnauthorized](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/unauthorized)Added [CBManagerStateUnknown](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/cbmanagerstateunknown)Added [CBManagerStateUnsupported](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/cbmanagerstateunsupported)

#### CBPeripheral.h

Modified [CBPeripheral.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518730-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) id<CBPeripheralDelegate> delegate ``` |
| To | ``` @property(weak, nonatomic) id<CBPeripheralDelegate> delegate ``` |

#### CBPeripheralManager.h

Removed CBPeripheralManager.stateAdded [-[CBPeripheralManager init]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1648153-init)Modified [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager)

|  | Superclasses |
| --- | --- |
| From | NSObject |
| To | CBManager |

Modified [CBPeripheralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393313-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) id<CBPeripheralManagerDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak) id<CBPeripheralManagerDelegate> delegate ``` |

Modified [CBPeripheralManager.isAdvertising](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393291-isadvertising)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) BOOL isAdvertising ``` |
| To | ``` @property(nonatomic, assign, readonly) BOOL isAdvertising ``` |

Modified [CBPeripheralManagerStatePoweredOff](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/cbperipheralmanagerstatepoweredoff)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CBPeripheralManagerStatePoweredOn](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/cbperipheralmanagerstatepoweredon)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CBPeripheralManagerStateResetting](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/resetting)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CBPeripheralManagerStateUnauthorized](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/cbperipheralmanagerstateunauthorized)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CBPeripheralManagerStateUnknown](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/unknown)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [CBPeripheralManagerStateUnsupported](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/unsupported)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### CBUUID.h

Added [CBUUIDCharacteristicValidRangeString](https://developer.apple.com/documentation/corebluetooth/cbuuidcharacteristicvalidrangestring)

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
