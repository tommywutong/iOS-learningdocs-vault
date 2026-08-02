---
title: What is a 'scsz' resource in Java?
apple_id: DTS10001390
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-17'
source_url: https://developer.apple.com/library/archive/qa/java/java15.html
archived_at: '2026-07-18T02:29:41.695795Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA15What is a 'scsz' resource in Java? |

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ---   Q: What is an `'scsz'` resource, and why do I need one in order to provide scripting support for my Java application?  A: The `'scsz'` resource is a scripting size resource that provides information about an application's capabilities for use by scripting components. In AppleScript for Java, the scripting size resource determines whether dynamic terminology should be generated using the Java introspector, or whether the `'aete'` should be used.  As an application developer, you can turn off dynamic generation of the `'aete'` (and thus freezing your terminology) by editing the `'scsz'`.  The following configurations are possible:   |  |  |  | | --- | --- | --- | | 'scsz' present | high bit set | result | | YES | YES | automatic generation on | | YES | NO | automatic generation off | | NO |  | automatic generation off |   The default `'scsz'` resource that comes with the MRJ SDK, has the high bit set. We recommend that you use this configuration during the development of your application, and then remove the resource once your `'aete'` is finalized.  For more information, see:  [The Scripting Size Resource](https://developer.apple.com/documentation/mac/IAC/IAC-315.html)  [Handling the Get AETE Event](https://developer.apple.com/documentation/mac/IAC/IAC-307.html) [May 17 1999] |

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
