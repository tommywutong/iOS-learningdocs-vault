---
title: How to Disable the JIT
apple_id: DTS10001380
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-02-22'
source_url: https://developer.apple.com/library/archive/qa/java/java05.html
archived_at: '2026-07-18T02:29:40.827281Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md) · [Stack Crawl Not Showing Line Numbers](Legacy%20Documentclose%20button.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA05How to Disable the JIT |

|  |
| --- |
| ---   Q: How do I disable the JIT?  A: You can manually move the "MRJ Symantec JITC" library file out of the MRJ Libraries folder; move it outside the System Folder, but not into the same folder as the application you are running. Because of the way shared libraries are loaded, if the library file is located in the same folder as the application running Java, whether the application is a browser, the Apple Applet Runner, JBindery, or a double-clickable JBound application, the JIT library will be located and activated. Programmatically, you can call the method `Compiler.disable()` from the beginning of your program's `main()` method. |

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
