---
title: Using qd and QDGlobals
apple_id: DTS10001893
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-02-09'
source_url: https://developer.apple.com/library/archive/qa/qd/qd40.html
archived_at: '2026-07-18T02:38:37.582309Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/Carbon/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Graphics & Imaging](https://developer.apple.com/referencelibrary/Carbon/idxGraphicsImaging-date.html)

|  |
| --- |
| Technical Q&A QD40Using qd and QDGlobals |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---   Q: I have a sample program compiled with SC. When I try to link the sample program, I get the following linker error:   |  | | --- | | ``` ### Link: Error: Undefined entry, name: (Error 28) "qd"   Referenced from: main in file: :Obj 68K:FIFDECO.c.o ``` |   "qd" is the QuickDraw global variable. If I declare the global, as in   |  | | --- | | ``` QDGlobals qd; ``` |   the error goes away. This is confusing, because globals declared for PowerPC code should also be automatically declared for 68K files. In fact, this same code compiles and links correctly with Symantec C++ v7.0 IDE, as well as Metrowerks Codewarrior. Is there some new library I need to include to get the 68K global declared? Or has some subtle change been made to the header files?  A: Recently, there has been a change to the MPW libraries for the classic Macintosh runtime architecture. The MPW libraries now require that the QuickDraw global qd be defined in the global space of your code, the same as in the MPW libraries for the other Macintosh runtime architectures (namely, PowerPC and CFM-68K runtime architectures). If you are working in the MPW environment, a simple definition such as:   |  | | --- | | ```  QDGlobals qd; ``` |   is all that is necessary. If you are working in multiple environments (say, MPW, Metrowerks, and Symantec), use a preprocessor conditional such as:   |  | | --- | | ``` #if GENERATINGCFM 	QDGlobals qd;	// Required for all CFM environments #else #ifndef SYMANTEC_C || SYMANTEC_CPLUS #define __MPW_ONLY__ #endif #if defined (__SC__) && defined(__MPW_ONLY__)  	QDGlobals qd;	// Required for SC in MPW compilations #endif #undef __MPW_ONLY__ #endif ``` |   may be required. For more details on the use of QDGlobals and qd, see [Technote 1016 - Where Has my qd gone? How Do I Use qd and QDGlobals Correctly?](https://developer.apple.com/library/archive/technotes/tn/tn1016.html) |

#### [Feb 09 1996]

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
