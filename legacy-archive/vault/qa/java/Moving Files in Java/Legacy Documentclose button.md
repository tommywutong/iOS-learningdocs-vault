---
title: Moving Files in Java
apple_id: DTS10001396
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-02-02'
source_url: https://developer.apple.com/library/archive/qa/java/java21.html
archived_at: '2026-07-18T02:29:42.058008Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA21Moving Files in Java |

|  |
| --- |
| ---   Q: How do I move a file from one directory to another? Do I have to use the Mac OS Toolbox?  A: As long as the files are on the same volume, you just need to use the `java.io.File.renameTo()` method. Using this call for files and directories works equally well, but due to some platform-specific runtime implementation differences, this is one of those things that falls into the write once, test multiple places, and tweak until done catagories. This call will fail if you try to move a file from one volume to another.  Moving to another volume is more difficult, since this actually involves copying the file, and there is no standard Java call to copy a file. You would need to create your own, and on the Mac this becomes more complicated because you must worry about resource forks and file types. For this, you would need to use JDirect, or possibly [JConfig](http://www.tolstoy.com/samizdat/jconfig.html) or Greg Guerin's [MacBinary Toolkit](http://www.amug.org/~glguerin/sw/#macbinary). [Feb 02 2000] |

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
