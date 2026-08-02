---
title: Updating the TXT record of a Bonjour service
apple_id: DTS10002340
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2004-07-14'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1302.html
archived_at: '2026-07-18T02:38:31.194753Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



|  |  |
| --- | --- |
|  |  |
| [ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) > | [ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) > |
|  |  |

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Core Foundation](https://developer.apple.com/referencelibrary/Networking/idxCoreFoundation-date.html)

|  |
| --- |
| Technical Q&A QA1302Updating the TXT record of a Bonjour service |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Q: My application uses `CFNetServiceSetProtocolSpecificInformation` or `setProtocolSpecificInformation` to advertise some meta-data corresponding to my Bonjour service, but sometimes I need to update this meta-data after the service is registered. Is that possible? A: No. The only workaround is to completely unregister the service and then immediately re-register it with the new data. Unfortunately, this causes additional network traffic, so if you need to update this data often, then you should move completely to the low-level DNSServiceDiscovery API.  In Mac OS X 10.2.x, the function `DNSServiceRegistrationUpdateRecord` from the Mach-based DNSServiceDiscovery API will allow you to update the default TXT record for a service registration. If your application only requires Mac OS X 10.3 and later, you should use the socket-based DNSServiceDiscovery API instead of the Mach-based API. The function `DNSServiceUpdateRecord` will allow you to update the default TXT record for a service registration.  Both of these functions require that you specify the TTL (Time-to-Live) of the TXT record. The default TTL for TXT records in Mac OS X 10.2.x is 60 seconds, but the default TTL in Mac OS X 10.3.x is 240 seconds. It's recommended that you specify a value of 0 for the TTL, which will allow mDNSResponder to automatically choose the default value. Document Revision History  | Date | Notes | | --- | --- | | 2004-07-14 | Simplified description of work around. | | 2003-10-23 | New document that explains how to update a Bonjour TXT record while running on either Jaguar or Panther. | |

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
