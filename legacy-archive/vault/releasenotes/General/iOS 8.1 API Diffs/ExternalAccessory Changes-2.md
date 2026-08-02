---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/ExternalAccessory.html
archived_at: '2026-07-18T02:56:11.883397Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# ExternalAccessory Changes

## ExternalAccessory

Removed EAWiFiUnconfiguredAccessoryProperties.valueAdded EAWiFiUnconfiguredAccessoryBrowser.configureAccessory(EAWiFiUnconfiguredAccessory!, withConfigurationUIOnViewController: UIViewController!)Added EAWiFiUnconfiguredAccessoryProperties.init(rawValue: UInt)Modified EAAccessory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessory.connected

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessory.connectionID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessory.delegate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessory.firmwareRevision

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessory.hardwareRevision

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessory.manufacturer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessory.modelNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessory.name

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessory.protocolStrings

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessory.serialNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessoryDelegate.accessoryDidDisconnect(EAAccessory!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessoryManager

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessoryManager.connectedAccessories

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessoryManager.registerForLocalNotifications()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessoryManager.sharedAccessoryManager() -> EAAccessoryManager! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessoryManager.showBluetoothAccessoryPickerWithNameFilter(NSPredicate!, completion: EABluetoothAccessoryPickerCompletion!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified EAAccessoryManager.unregisterForLocalNotifications()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EASession

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EASession.accessory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EASession.init(accessory: EAAccessory!, forProtocol: String!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(accessory accessory: EAAccessory!, forProtocol protocolString: String!) ``` | iOS 8.0 |
| To | ``` init!(accessory accessory: EAAccessory!, forProtocol protocolString: String!) ``` | iOS 3.0 |

Modified EASession.inputStream

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EASession.outputStream

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EASession.protocolString

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAWiFiUnconfiguredAccessoryBrowser.init(delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate!, queue: dispatch_queue_t!)

|  | Declaration |
| --- | --- |
| From | ``` init(delegate delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate!, queue queue: dispatch_queue_t!) ``` |
| To | ``` init!(delegate delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate!, queue queue: dispatch_queue_t!) ``` |

Modified EAWiFiUnconfiguredAccessoryProperties [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct EAWiFiUnconfiguredAccessoryProperties : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var PropertySupportsAirPlay: EAWiFiUnconfiguredAccessoryProperties { get }     static var PropertySupportsAirPrint: EAWiFiUnconfiguredAccessoryProperties { get }     static var PropertySupportsHomeKit: EAWiFiUnconfiguredAccessoryProperties { get } } ``` |
| To | ``` struct EAWiFiUnconfiguredAccessoryProperties : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var PropertySupportsAirPlay: EAWiFiUnconfiguredAccessoryProperties { get }     static var PropertySupportsAirPrint: EAWiFiUnconfiguredAccessoryProperties { get }     static var PropertySupportsHomeKit: EAWiFiUnconfiguredAccessoryProperties { get } } ``` |

Modified EAWiFiUnconfiguredAccessoryProperties.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified EAAccessoryDidConnectNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessoryDidDisconnectNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessoryKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified EAAccessorySelectedKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

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
