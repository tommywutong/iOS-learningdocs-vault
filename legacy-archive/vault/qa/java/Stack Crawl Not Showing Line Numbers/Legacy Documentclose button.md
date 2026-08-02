---
title: Stack Crawl Not Showing Line Numbers
apple_id: DTS10001381
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-02-22'
source_url: https://developer.apple.com/library/archive/qa/java/java06.html
archived_at: '2026-07-18T02:29:40.924981Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA06Stack Crawl Not Showing Line Numbers |

|  |
| --- |
| ---   Q: I have a Java stack crawl (from an exception printed to the console, or via the `'mrj' dcmd`) that does not show source line numbers for some or all methods. How can I get it to show the line numbers so I can debug the problem?  A: There are two explanations. The most likely is that the method has been translated to native code by the JIT. In this case, the phrase "(Compiled code)" will appear where the source filename and line number would have been. If you're debugging and really need the line numbers, disable the JIT -- see the Q&A on [disabling the JIT](Legacy%20Documentclose%20button-2.md).  If there is no "(Compiled code)" text, or if you've already disabled the JIT and still don't get line numbers, then the Java compiler must have omitted the source-file and line-number tables when it compiled the class. This is a compiler setting which can be changed. Recompiling with this option ON will solve the problem; however, leaving out these tables makes your compiled code noticeably smaller. If you're using the "javac" compiler which comes with the MRJ SDK, this is accomplished through the "Debugging tables" checkbox. If you're using Metrowerks CodeWarrior, make sure the debugging dot (in the column underneath the bug icon) is ON for all source files, then recompile. (Note also that turning on optimization and inlining in the Metrowerks compiler can make line numbers inaccurate or confusing.) |

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
