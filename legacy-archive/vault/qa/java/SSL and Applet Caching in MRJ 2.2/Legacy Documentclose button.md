---
title: SSL and Applet Caching in MRJ 2.2
apple_id: DTS10001397
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-02-02'
source_url: https://developer.apple.com/library/archive/qa/java/java22.html
archived_at: '2026-07-18T02:29:42.110033Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA22SSL and Applet Caching in MRJ 2.2 |

|  |
| --- |
| ---   Q: I have been told MRJ 2.2 has support for Secure Sockets Layer (SSL) and Applet Caching. What are the details and how can I take advantage of these features?  A: MRJ 2.2 relies on a Java-enabled browser to provide SSL and applet caching support. In order to make these features available to MRJ the browser must implement specific interfaces. Currently Microsoft Internet 5.0 provides MRJ with these interfaces and fully enables SSL and apple caching. Additionally, Apple is working closely with other browser vendors, such as Netscape, iCab, among others, to provide seamless integration of these technologies and support for MRJ.  When an enabled browser is used in conjunction with MRJ 2.2, applet caching and SSL support is automatic. Previous versions of MRJ do not have this functionality. Versions of Microsoft Internet Explorer prior to 5.0 also do not have these capabilities. [Feb 02 2000] |

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
