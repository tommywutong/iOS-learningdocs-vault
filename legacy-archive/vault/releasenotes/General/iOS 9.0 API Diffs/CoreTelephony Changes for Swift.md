---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/CoreTelephony.html
archived_at: '2026-07-18T02:56:47.079774Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreTelephony Changes for Swift

### CoreTelephony

Added [CTCellularData](https://developer.apple.com/documentation/coretelephony/ctcellulardata)Added [CTCellularData.cellularDataRestrictionDidUpdateNotifier](https://developer.apple.com/documentation/coretelephony/ctcellulardata/1620325-cellulardatarestrictiondidupdate)Added [CTCellularData.restrictedState](https://developer.apple.com/documentation/coretelephony/ctcellulardata/1620311-restrictedstate)Added [CTCellularDataRestrictedState [enum]](https://developer.apple.com/documentation/coretelephony/ctcellulardatarestrictedstate)Added [CTCellularDataRestrictedState.NotRestricted](https://developer.apple.com/documentation/coretelephony/ctcellulardatarestrictedstate/notrestricted)Added [CTCellularDataRestrictedState.Restricted](https://developer.apple.com/documentation/coretelephony/ctcellulardatarestrictedstate/kctcellulardatarestricted)Added [CTCellularDataRestrictedState.RestrictedStateUnknown](https://developer.apple.com/documentation/coretelephony/ctcellulardatarestrictedstate/kctcellulardatarestrictedstateunknown)Added [CellularDataRestrictionDidUpdateNotifier](https://developer.apple.com/documentation/coretelephony/cellulardatarestrictiondidupdatenotifier)Modified [CTCall](https://developer.apple.com/documentation/coretelephony/ctcall)

|  | Declaration |
| --- | --- |
| From | ``` class CTCall : NSObject {     var callState: String! { get }     var callID: String! { get } } ``` |
| To | ``` class CTCall : NSObject {     var callState: String { get }     var callID: String { get } } ``` |

Modified [CTCall.callID](https://developer.apple.com/documentation/coretelephony/ctcall/1618271-callid)

|  | Declaration |
| --- | --- |
| From | ``` var callID: String! { get } ``` |
| To | ``` var callID: String { get } ``` |

Modified [CTCall.callState](https://developer.apple.com/documentation/coretelephony/ctcall/1618272-callstate)

|  | Declaration |
| --- | --- |
| From | ``` var callState: String! { get } ``` |
| To | ``` var callState: String { get } ``` |

Modified [CTCallCenter](https://developer.apple.com/documentation/coretelephony/ctcallcenter)

|  | Declaration |
| --- | --- |
| From | ``` class CTCallCenter : NSObject {     var currentCalls: Set<NSObject>! { get }     var callEventHandler: ((CTCall!) -> Void)! } ``` |
| To | ``` class CTCallCenter : NSObject {     var currentCalls: Set<CTCall>? { get }     var callEventHandler: ((CTCall) -> Void)? } ``` |

Modified [CTCallCenter.callEventHandler](https://developer.apple.com/documentation/coretelephony/ctcallcenter/1620310-calleventhandler)

|  | Declaration |
| --- | --- |
| From | ``` var callEventHandler: ((CTCall!) -> Void)! ``` |
| To | ``` var callEventHandler: ((CTCall) -> Void)? ``` |

Modified [CTCallCenter.currentCalls](https://developer.apple.com/documentation/coretelephony/ctcallcenter/1620320-currentcalls)

|  | Declaration |
| --- | --- |
| From | ``` var currentCalls: Set<NSObject>! { get } ``` |
| To | ``` var currentCalls: Set<CTCall>? { get } ``` |

Modified [CTCarrier](https://developer.apple.com/documentation/coretelephony/ctcarrier)

|  | Declaration |
| --- | --- |
| From | ``` class CTCarrier : NSObject {     var carrierName: String! { get }     var mobileCountryCode: String! { get }     var mobileNetworkCode: String! { get }     var isoCountryCode: String! { get }     var allowsVOIP: Bool { get } } ``` |
| To | ``` class CTCarrier : NSObject {     var carrierName: String? { get }     var mobileCountryCode: String? { get }     var mobileNetworkCode: String? { get }     var isoCountryCode: String? { get }     var allowsVOIP: Bool { get } } ``` |

Modified [CTCarrier.carrierName](https://developer.apple.com/documentation/coretelephony/ctcarrier/1620313-carriername)

|  | Declaration |
| --- | --- |
| From | ``` var carrierName: String! { get } ``` |
| To | ``` var carrierName: String? { get } ``` |

Modified [CTCarrier.isoCountryCode](https://developer.apple.com/documentation/coretelephony/ctcarrier/1620317-isocountrycode)

|  | Declaration |
| --- | --- |
| From | ``` var isoCountryCode: String! { get } ``` |
| To | ``` var isoCountryCode: String? { get } ``` |

Modified [CTCarrier.mobileCountryCode](https://developer.apple.com/documentation/coretelephony/ctcarrier/1620309-mobilecountrycode)

|  | Declaration |
| --- | --- |
| From | ``` var mobileCountryCode: String! { get } ``` |
| To | ``` var mobileCountryCode: String? { get } ``` |

Modified [CTCarrier.mobileNetworkCode](https://developer.apple.com/documentation/coretelephony/ctcarrier/1620324-mobilenetworkcode)

|  | Declaration |
| --- | --- |
| From | ``` var mobileNetworkCode: String! { get } ``` |
| To | ``` var mobileNetworkCode: String? { get } ``` |

Modified [CTSubscriber](https://developer.apple.com/documentation/coretelephony/ctsubscriber)

|  | Declaration |
| --- | --- |
| From | ``` class CTSubscriber : NSObject {     var carrierToken: NSData! { get } } ``` |
| To | ``` class CTSubscriber : NSObject {     var carrierToken: NSData? { get } } ``` |

Modified [CTSubscriber.carrierToken](https://developer.apple.com/documentation/coretelephony/ctsubscriber/1620318-carriertoken)

|  | Declaration |
| --- | --- |
| From | ``` var carrierToken: NSData! { get } ``` |
| To | ``` var carrierToken: NSData? { get } ``` |

Modified [CTSubscriberInfo](https://developer.apple.com/documentation/coretelephony/ctsubscriberinfo)

|  | Declaration |
| --- | --- |
| From | ``` class CTSubscriberInfo : NSObject {     class func subscriber() -> CTSubscriber! } ``` |
| To | ``` class CTSubscriberInfo : NSObject {     class func subscriber() -> CTSubscriber } ``` |

Modified [CTSubscriberInfo.subscriber() -> CTSubscriber [class]](https://developer.apple.com/documentation/coretelephony/ctsubscriberinfo/1620278-subscriber)

|  | Declaration |
| --- | --- |
| From | ``` class func subscriber() -> CTSubscriber! ``` |
| To | ``` class func subscriber() -> CTSubscriber ``` |

Modified [CTTelephonyNetworkInfo](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo)

|  | Declaration |
| --- | --- |
| From | ``` class CTTelephonyNetworkInfo : NSObject {     var subscriberCellularProvider: CTCarrier! { get }     var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier!) -> Void)!     var currentRadioAccessTechnology: String! { get } } ``` |
| To | ``` class CTTelephonyNetworkInfo : NSObject {     var subscriberCellularProvider: CTCarrier? { get }     var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier) -> Void)?     var currentRadioAccessTechnology: String? { get } } ``` |

Modified [CTTelephonyNetworkInfo.currentRadioAccessTechnology](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/1616895-currentradioaccesstechnology)

|  | Declaration |
| --- | --- |
| From | ``` var currentRadioAccessTechnology: String! { get } ``` |
| To | ``` var currentRadioAccessTechnology: String? { get } ``` |

Modified [CTTelephonyNetworkInfo.subscriberCellularProvider](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/1616900-subscribercellularprovider)

|  | Declaration |
| --- | --- |
| From | ``` var subscriberCellularProvider: CTCarrier! { get } ``` |
| To | ``` var subscriberCellularProvider: CTCarrier? { get } ``` |

Modified [CTTelephonyNetworkInfo.subscriberCellularProviderDidUpdateNotifier](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/1616898-subscribercellularproviderdidupd)

|  | Declaration |
| --- | --- |
| From | ``` var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier!) -> Void)! ``` |
| To | ``` var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier) -> Void)? ``` |

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
