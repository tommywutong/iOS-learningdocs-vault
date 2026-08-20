---
title: Developer Tools JBoss and Tomcat Do Not Start After Installing Java 1.4.2 Update
apple_id: DTS10003207
resource_type: QA
platform: Java
topic: Cross Platform
technology: null
published: '2004-03-04'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1025.html
archived_at: '2026-07-18T02:38:03.408944Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Internet & Web](https://developer.apple.com/referencelibrary/Java/idxInternetWeb-date.html)

|  |
| --- |
| Technical Q&A QA1025Developer Tools JBoss and Tomcat Do Not Start After Installing Java 1.4.2 Update |

|  |
| --- |
| ---   Q: How do I re-enable JBoss and Tomcat to work after installing the Java 1.4.2 Update?  A: The run.conf script for starting the JBoss server has a hardcoded reference to the 1.4.1 JVM. Installing the Java 1.4.2 Update removes the Java 1.4.1 installation, and JBoss/Tomcat services will not be able to start.  To re-enable JBoss and Tomcat the reference below should be changed in the file: `/Library/JBoss/3.2/bin/run.conf`  from: `JAVA=/System/Library/Frameworks/JavaVM.framework/Versions/1.4.1/Home/bin/java`  to: `JAVA=/usr/bin/java`   ---  [Mar 04, 2004] |

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
