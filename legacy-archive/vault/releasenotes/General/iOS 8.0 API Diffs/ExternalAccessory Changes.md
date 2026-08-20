---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/ExternalAccessory.html
archived_at: '2026-07-18T02:55:57.098129Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# ExternalAccessory Changes

## ExternalAccessory

EAAccessory.hModified [-[EAAccessoryDelegate accessoryDidDisconnect:]](https://developer.apple.com/documentation/externalaccessory/eaaccessorydelegate/1613858-accessorydiddisconnect)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

EASession.hModified [-[EASession initWithAccessory:forProtocol:]](https://developer.apple.com/documentation/externalaccessory/easession/1613849-initwithaccessory)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAccessory:(EAAccessory *)accessory forProtocol:(NSString *)protocolString ``` |
| To | ``` - (instancetype)initWithAccessory:(EAAccessory *)accessory forProtocol:(NSString *)protocolString ``` |

EAWiFiUnconfiguredAccessory.h (Added)Added [EAWiFiUnconfiguredAccessory](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory)Added [EAWiFiUnconfiguredAccessory.macAddress](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613860-macaddress)Added [EAWiFiUnconfiguredAccessory.manufacturer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613819-manufacturer)Added [EAWiFiUnconfiguredAccessory.model](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613893-model)Added [EAWiFiUnconfiguredAccessory.name](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613856-name)Added [EAWiFiUnconfiguredAccessory.properties](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613879-properties)Added [EAWiFiUnconfiguredAccessory.ssid](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613889-ssid)Added [EAWiFiUnconfiguredAccessoryProperties](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties)Added [EAWiFiUnconfiguredAccessoryPropertySupportsAirPlay](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties/1613793-propertysupportsairplay)Added [EAWiFiUnconfiguredAccessoryPropertySupportsAirPrint](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties/1613853-propertysupportsairprint)Added [EAWiFiUnconfiguredAccessoryPropertySupportsHomeKit](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties/1613857-propertysupportshomekit)EAWiFiUnconfiguredAccessoryBrowser.h (Added)Added [EAWiFiUnconfiguredAccessoryBrowser](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser)Added [-[EAWiFiUnconfiguredAccessoryBrowser configureAccessory:withConfigurationUIOnViewController:]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613907-configureaccessory)Added [EAWiFiUnconfiguredAccessoryBrowser.delegate](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613829-delegate)Added [-[EAWiFiUnconfiguredAccessoryBrowser initWithDelegate:queue:]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613881-init)Added [-[EAWiFiUnconfiguredAccessoryBrowser startSearchingForUnconfiguredAccessoriesMatchingPredicate:]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613869-startsearchingforunconfiguredacc)Added [-[EAWiFiUnconfiguredAccessoryBrowser stopSearchingForUnconfiguredAccessories]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613841-stopsearchingforunconfiguredacce)Added [EAWiFiUnconfiguredAccessoryBrowser.unconfiguredAccessories](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613871-unconfiguredaccessories)Added [EAWiFiUnconfiguredAccessoryBrowserDelegate](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate)Added [-[EAWiFiUnconfiguredAccessoryBrowserDelegate accessoryBrowser:didFindUnconfiguredAccessories:]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/1613861-accessorybrowser)Added [-[EAWiFiUnconfiguredAccessoryBrowserDelegate accessoryBrowser:didFinishConfiguringAccessory:withStatus:]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/1613911-accessorybrowser)Added [-[EAWiFiUnconfiguredAccessoryBrowserDelegate accessoryBrowser:didRemoveUnconfiguredAccessories:]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/1613862-accessorybrowser)Added [-[EAWiFiUnconfiguredAccessoryBrowserDelegate accessoryBrowser:didUpdateState:]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/1613845-accessorybrowser)Added [EAWiFiUnconfiguredAccessoryBrowserState](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate)Added [EAWiFiUnconfiguredAccessoryBrowserStateConfiguring](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate/configuring)Added [EAWiFiUnconfiguredAccessoryBrowserStateSearching](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate/searching)Added [EAWiFiUnconfiguredAccessoryBrowserStateStopped](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate/stopped)Added [EAWiFiUnconfiguredAccessoryBrowserStateWiFiUnavailable](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate/eawifiunconfiguredaccessorybrowserstatewifiunavailable)Added [EAWiFiUnconfiguredAccessoryConfigurationStatus](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus)Added [EAWiFiUnconfiguredAccessoryConfigurationStatusFailed](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus/failed)Added [EAWiFiUnconfiguredAccessoryConfigurationStatusSuccess](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus/success)Added [EAWiFiUnconfiguredAccessoryConfigurationStatusUserCancelledConfiguration](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus/eawifiunconfiguredaccessoryconfigurationstatususercancelledconfiguration)

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
