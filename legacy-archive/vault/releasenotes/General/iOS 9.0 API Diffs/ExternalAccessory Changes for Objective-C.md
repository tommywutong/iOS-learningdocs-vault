---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/ExternalAccessory.html
archived_at: '2026-07-18T02:56:32.833795Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# ExternalAccessory Changes for Objective-C

### ExternalAccessory

#### EAAccessory.h

Added [EAAccessory.dockType](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613905-docktype)Modified [EAAccessory.protocolStrings](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613877-protocolstrings)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *protocolStrings ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *protocolStrings ``` |

#### EAAccessoryManager.h

Modified [EAAccessoryManager.connectedAccessories](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/1613821-connectedaccessories)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *connectedAccessories ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<EAAccessory *> *connectedAccessories ``` |

#### EAWiFiUnconfiguredAccessoryBrowser.h

Modified [EAWiFiUnconfiguredAccessoryBrowser.unconfiguredAccessories](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613871-unconfiguredaccessories)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, atomic) NSSet *unconfiguredAccessories ``` |
| To | ``` @property(readonly, copy, atomic, nonnull) NSSet<EAWiFiUnconfiguredAccessory *> *unconfiguredAccessories ``` |

Modified [-[EAWiFiUnconfiguredAccessoryBrowserDelegate accessoryBrowser:didFindUnconfiguredAccessories:]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/1613861-accessorybrowser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)accessoryBrowser:(EAWiFiUnconfiguredAccessoryBrowser *)browser didFindUnconfiguredAccessories:(NSSet *)accessories ``` |
| To | ``` - (void)accessoryBrowser:(EAWiFiUnconfiguredAccessoryBrowser * _Nonnull)browser didFindUnconfiguredAccessories:(NSSet<EAWiFiUnconfiguredAccessory *> * _Nonnull)accessories ``` |

Modified [-[EAWiFiUnconfiguredAccessoryBrowserDelegate accessoryBrowser:didRemoveUnconfiguredAccessories:]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/1613862-accessorybrowser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)accessoryBrowser:(EAWiFiUnconfiguredAccessoryBrowser *)browser didRemoveUnconfiguredAccessories:(NSSet *)accessories ``` |
| To | ``` - (void)accessoryBrowser:(EAWiFiUnconfiguredAccessoryBrowser * _Nonnull)browser didRemoveUnconfiguredAccessories:(NSSet<EAWiFiUnconfiguredAccessory *> * _Nonnull)accessories ``` |

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
