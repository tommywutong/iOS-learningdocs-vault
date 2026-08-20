---
title: Additional URL Access Error Codes
apple_id: DTS10001478
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2002-12-18'
source_url: https://developer.apple.com/library/archive/qa/nw/nw66.html
archived_at: '2026-07-18T02:29:47.949592Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Internet & Web](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxInternetWeb-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Internet & Web](https://developer.apple.com/referencelibrary/InternetWeb/index.html)

|  |
| --- |
| Technical Q&A NW66Additional URL Access Error Codes |

|  |
| --- |
| ---   Q: When calling `URLDownload` or `URLOpen` in Mac OS 9.x, I occasionally see error codes that aren't documented. What do these error codes mean?  A: Here are the meanings of some additional error codes that may be returned by URL Access when running on Mac OS 9.x:  The following errors are returned from the SSL code used by URL Access.   - __-10__: The server requires 128-bit encryption, but URL Access doesn't   support it. (URL Access began supporting 128-bit encryption in   version 2.1, which shipped with Mac OS 9.1) - __-15__: The URL Access Manager does not have the server's root certificate   and thus cannot validate the certificate received from the server.   There is no mechanism to add new root certificates to URL Access when   running on Mac OS 9.x, so to work around this limitation, you will need   to add a certificate to your server that is known to URL Access. - __-6986__: Also known as X509CertChainInvalidErr. The certificate   on the server has expired. In URL Access 2.4.1, the behavior was changed to   allow expired certificates by default which should eliminate this error. - __-6996__: Also known as SSLProtocolErr. If you see this error, you may be   able to fix it by adding a certificate to your server that's supported   by URL Access. If that doesn't help, there is currently no other way to   workaround this error. You should not see this error when running on Mac OS X 10.1   and later.         For your reference, here are the root certificates contained in   URL Access 2.0 which shipped with Mac OS 9.0:         GTE CyberTrust Global Root    GTE CyberTrust Root    GTE CyberTrust Root 2    GTE CyberTrust Root 3    GTE CyberTrust Root 4    GTE CyberTrust Root 5    RSA Data Security, Inc.    TC TrustCenter Class 0 CA    TC TrustCenter Class 1 CA    TC TrustCenter Class 2 CA    TC TrustCenter Class 3 CA    TC TrustCenter Class 4 CA    Thawte Personal Basic CA    Thawte Personal Freemail CA    Thawte Personal Premium CA    Thawte Premium Server CA    Thawte Server CA    Verisign, Inc. Class 1 G2    Verisign, Inc. Class 1 Primary    Verisign, Inc. Class 2 G2    Verisign, Inc. Class 2 Primary    Verisign, Inc. Class 3 G2    Verisign, Inc. Class 3 Primary    Verisign, Inc. Class 4 G2            These additional certificates were shipped with Mac OS 9.1:        Baltimore CyberTrust Code Signing Root    Baltimore CyberTrust Mobile Root    Baltimore CyberTrust Root   The following is an internal TCP-level error:   - __-23008__: A connection used by URL Access no longer exists. This   is usually a benign condition since HTTP provides for recovery if   a connection is unexpectedly closed. |

#### [Dec 18 2002]

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
