---
title: JBound App Results in -35 OSErr
apple_id: DTS10001378
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-02-22'
source_url: https://developer.apple.com/library/archive/qa/java/java03.html
archived_at: '2026-07-18T02:29:40.669179Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Tools](https://developer.apple.com/referencelibrary/Java/idxTools-date.html)

|  |
| --- |
| Technical Q&A JAVA03JBound App Results in -35 OSErr |

|  |
| --- |
| ---   Q: When I move my Java application which I created with JBindery to another machine and try to run it, I get an error "OSErr -35 processing classpath item." What is the problem, and how should it be addressed?  A: If you use the __Add Folder__ or __Add Zip File__ buttons (or drag and drop) to add things to the classpath, the application stores an alias pointing to the file or directory, and this tends to break when you move it to another machine or another file system.  To solve this problem, use __Add Manually__ and give a path relative to "$APPLICATION" (this is the default for the dialog box). For more information on how to use JBindery in this manner, please refer to the [JBindery documentation](https://developer.apple.com/documentation/java/MacOSandJava/JBindery/JBindery.html). |

#### [Feb 22 1999]

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
