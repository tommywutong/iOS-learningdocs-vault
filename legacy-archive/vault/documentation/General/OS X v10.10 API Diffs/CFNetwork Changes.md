---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/CFNetwork.html
archived_at: '2026-07-15T07:34:44.886738Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# CFNetwork Changes

## CFNetwork

CFHTTPStream.hRemoved CFHTTPReadStreamSetProxy()CFNetServices.hAdded [CFNetServiceBrowserFlags](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserflags)Added [CFNetServiceRegisterFlags](https://developer.apple.com/documentation/cfnetwork/cfnetserviceregisterflags)Modified [kCFNetServiceFlagIsRegistrationDomain](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserflags/kcfnetserviceflagisregistrationdomain)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.4 |

CFNetworkDefs.hRemoved #def CFN_CPP_BEGINRemoved #def CFN_CPP_ENDCFNetworkErrors.hAdded [kCFURLErrorBackgroundSessionInUseByAnotherProcess](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorbackgroundsessioninusebyanotherprocess)Added [kCFURLErrorBackgroundSessionWasDisconnected](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorbackgroundsessionwasdisconnected)CFSocketStream.hRemoved [CFSocketStreamPairSetSecurityProtocol()](https://developer.apple.com/documentation/corefoundation/cfstream/1805747-cfsocketstreampairsetsecuritypro)Removed [CFStreamSocketSecurityProtocol](https://developer.apple.com/documentation/corefoundation/cfstream/cfstreamsocketsecurityprotocol)Removed [kCFStreamSocketSecurityNone](https://developer.apple.com/documentation/corefoundation/cfstream/cfstreamsocketsecurityprotocol/kcfstreamsocketsecuritynone)Removed [kCFStreamSocketSecuritySSLv2](https://developer.apple.com/documentation/corefoundation/cfstream/cfstreamsocketsecurityprotocol/kcfstreamsocketsecuritysslv2)Removed [kCFStreamSocketSecuritySSLv23](https://developer.apple.com/documentation/corefoundation/cfstream/cfstreamsocketsecurityprotocol/kcfstreamsocketsecuritysslv23)Removed [kCFStreamSocketSecuritySSLv3](https://developer.apple.com/documentation/corefoundation/cfstream/cfstreamsocketsecurityprotocol/kcfstreamsocketsecuritysslv3)Removed [kCFStreamSocketSecurityTLSv1](https://developer.apple.com/documentation/corefoundation/cfstream/cfstreamsocketsecurityprotocol/kcfstreamsocketsecuritytlsv1)Modified [kCFStreamErrorDomainSOCKS](https://developer.apple.com/documentation/corefoundation/kcfstreamerrordomainsocks)

|  | Introduction |
| --- | --- |
| From | OS X 10.2 |
| To | OS X 10.0 |

Modified [kCFStreamErrorDomainSSL](https://developer.apple.com/documentation/corefoundation/kcfstreamerrordomainssl)

|  | Introduction |
| --- | --- |
| From | OS X 10.1 |
| To | OS X 10.2 |

Modified [kCFStreamPropertySSLPeerCertificates](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertysslpeercertificates)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [kCFStreamSSLAllowsAnyRoot](https://developer.apple.com/documentation/cfnetwork/kcfstreamsslallowsanyroot)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [kCFStreamSSLAllowsExpiredCertificates](https://developer.apple.com/documentation/cfnetwork/kcfstreamsslallowsexpiredcertificates)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

Modified [kCFStreamSSLAllowsExpiredRoots](https://developer.apple.com/documentation/cfnetwork/kcfstreamsslallowsexpiredroots)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.6 |

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
