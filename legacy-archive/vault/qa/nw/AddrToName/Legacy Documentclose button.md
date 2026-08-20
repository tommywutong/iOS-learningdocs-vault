---
title: AddrToName
apple_id: DTS10001451
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-09-27'
source_url: https://developer.apple.com/library/archive/qa/nw/nw39.html
archived_at: '2026-07-18T02:29:46.303200Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW39AddrToName |

|  |
| --- |
| ---   Q: Under MacTCP and OT 1.0.x, if I'm using a Hosts file and I do an AddrToName, the name resolves to the correct address. Under OT 1.1 it returns an `authNameErr`. What's going on?  A: In 1.0.8, Open Transport mapped name-to-address and address-to-name translations into the same cache, and searched there whenever either a name-to-address or address-to-name mapping was requested. Sounds good, yes? Problem is, it broke several server load-sharing implementations that registered a service name as a single alias for a list of CNAMEs, each of which pointed to a server running the service. Under the former caching scheme, load-sharing utilizing reverse lookups didn't work for the Mac - we'd always wind up with the same host name and hardware address for the original alias.  As a result, OT 1.1 no longer caches address-to-name mappings (PTR records), nor does it search the name-to-address cache for address-to-name requests. (We also modified our treatment of CNAME records received, but that's irrelevant to your question.) Instead, it queries the configured domain name servers; apparently you got no authoritative information from any of them (or, perhaps, weren't using them at all).  Strictly speaking, the behavior you are now seeing is more correct than that seen before. A DNS A resource record maps a name to an address. In order to map an address to a name, a PTR record is required. The previous behavior of the MacTCP and Open Transport TCP/IP DNRs, treating the one as the mirror image of the other, was incorrect and has been changed accordingly.  The Mac Hosts file historically did not support PTR records, and does not support PTR records now because in order to do so, we would have to go back to caching those records, once again breaking the load-sharing schemes. The Hosts file supports only A (name to address), CNAME (alias to fully qualified domain name) and NS (domain name server's fully qualified domain name) resource records. If you need a PTR mapping, you need to register it with your local Domain Name server administrator, or maintain it within your own code from the results of your earlier name-to-address request.  It's unfortunate that this no longer works for you, but we're trying to make Open Transport support the widest range of possible clients. Occasionally those clients' needs conflict with each other, and then we have to make choices. When we do so, we try to make the choice that is more technically correct, and this, unfortunately, was such a choice. |

#### [Sep 27 1996]

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

---
