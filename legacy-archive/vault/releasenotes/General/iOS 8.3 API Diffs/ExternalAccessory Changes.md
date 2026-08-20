---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/ExternalAccessory.html
archived_at: '2026-07-18T02:56:24.702569Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# ExternalAccessory Changes

## ExternalAccessory

Modified EAWiFiUnconfiguredAccessoryBrowser.unconfiguredAccessories

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var unconfiguredAccessories: NSSet! { get } ``` |
| To | ``` var unconfiguredAccessories: Set<NSObject>! { get } ``` |

Modified EAWiFiUnconfiguredAccessoryBrowserDelegate.accessoryBrowser(EAWiFiUnconfiguredAccessoryBrowser!, didFindUnconfiguredAccessories: Set<NSObject>!)

|  | Declaration |
| --- | --- |
| From | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser!, didFindUnconfiguredAccessories accessories: NSSet!) ``` |
| To | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser!, didFindUnconfiguredAccessories accessories: Set<NSObject>!) ``` |

Modified EAWiFiUnconfiguredAccessoryBrowserDelegate.accessoryBrowser(EAWiFiUnconfiguredAccessoryBrowser!, didRemoveUnconfiguredAccessories: Set<NSObject>!)

|  | Declaration |
| --- | --- |
| From | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser!, didRemoveUnconfiguredAccessories accessories: NSSet!) ``` |
| To | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser!, didRemoveUnconfiguredAccessories accessories: Set<NSObject>!) ``` |

Modified EAAccessoryDidConnectNotification

|  | Declaration |
| --- | --- |
| From | ``` let EAAccessoryDidConnectNotification: NSString! ``` |
| To | ``` let EAAccessoryDidConnectNotification: String ``` |

Modified EAAccessoryDidDisconnectNotification

|  | Declaration |
| --- | --- |
| From | ``` let EAAccessoryDidDisconnectNotification: NSString! ``` |
| To | ``` let EAAccessoryDidDisconnectNotification: String ``` |

Modified EAAccessoryKey

|  | Declaration |
| --- | --- |
| From | ``` let EAAccessoryKey: NSString! ``` |
| To | ``` let EAAccessoryKey: String ``` |

Modified EAAccessorySelectedKey

|  | Declaration |
| --- | --- |
| From | ``` let EAAccessorySelectedKey: NSString! ``` |
| To | ``` let EAAccessorySelectedKey: String ``` |

Modified EABluetoothAccessoryPickerErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let EABluetoothAccessoryPickerErrorDomain: NSString! ``` |
| To | ``` let EABluetoothAccessoryPickerErrorDomain: String ``` |

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
