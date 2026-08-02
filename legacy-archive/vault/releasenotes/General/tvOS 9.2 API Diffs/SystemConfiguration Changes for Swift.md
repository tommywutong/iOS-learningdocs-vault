---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Swift/SystemConfiguration.html
archived_at: '2026-07-18T02:58:06.962487Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# SystemConfiguration Changes for Swift

### SystemConfiguration

Modified [SCBondStatus](https://developer.apple.com/documentation/systemconfiguration/scbondstatusref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SCBondStatusRef | ``` typealias SCBondStatusRef = SCBondStatus ``` |
| To | SCBondStatus | ``` class SCBondStatus { } ``` |

Modified [SCDynamicStore](https://developer.apple.com/documentation/systemconfiguration/scdynamicstoreref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SCDynamicStoreRef | ``` typealias SCDynamicStoreRef = SCDynamicStore ``` |
| To | SCDynamicStore | ``` class SCDynamicStore { } ``` |

Modified [SCNetworkConnection](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnection)

|  | Name | Declaration |
| --- | --- | --- |
| From | SCNetworkConnectionRef | ``` typealias SCNetworkConnectionRef = SCNetworkConnection ``` |
| To | SCNetworkConnection | ``` class SCNetworkConnection { } ``` |

Modified [SCNetworkInterface](https://developer.apple.com/documentation/systemconfiguration/scnetworkinterfaceref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SCNetworkInterfaceRef | ``` typealias SCNetworkInterfaceRef = SCNetworkInterface ``` |
| To | SCNetworkInterface | ``` class SCNetworkInterface { } ``` |

Modified [SCNetworkProtocol](https://developer.apple.com/documentation/systemconfiguration/scnetworkprotocol)

|  | Name | Declaration |
| --- | --- | --- |
| From | SCNetworkProtocolRef | ``` typealias SCNetworkProtocolRef = SCNetworkProtocol ``` |
| To | SCNetworkProtocol | ``` class SCNetworkProtocol { } ``` |

Modified [SCNetworkReachability](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachability)

|  | Name | Declaration |
| --- | --- | --- |
| From | SCNetworkReachabilityRef | ``` typealias SCNetworkReachabilityRef = SCNetworkReachability ``` |
| To | SCNetworkReachability | ``` class SCNetworkReachability { } ``` |

Modified [SCNetworkService](https://developer.apple.com/documentation/systemconfiguration/scnetworkservice)

|  | Name | Declaration |
| --- | --- | --- |
| From | SCNetworkServiceRef | ``` typealias SCNetworkServiceRef = SCNetworkService ``` |
| To | SCNetworkService | ``` class SCNetworkService { } ``` |

Modified [SCNetworkSet](https://developer.apple.com/documentation/systemconfiguration/scnetworksetref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SCNetworkSetRef | ``` typealias SCNetworkSetRef = SCNetworkSet ``` |
| To | SCNetworkSet | ``` class SCNetworkSet { } ``` |

Modified [SCPreferences](https://developer.apple.com/documentation/systemconfiguration/scpreferencesref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SCPreferencesRef | ``` typealias SCPreferencesRef = SCPreferences ``` |
| To | SCPreferences | ``` class SCPreferences { } ``` |

Modified [SCBondInterface](https://developer.apple.com/documentation/systemconfiguration/scbondinterfaceref)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCBondInterfaceRef = SCBondInterface ``` |
| To | ``` typealias SCBondInterface = SCNetworkInterfaceRef ``` |

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
