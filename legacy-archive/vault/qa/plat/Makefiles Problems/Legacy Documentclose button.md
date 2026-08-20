---
title: Makefiles Problems
apple_id: DTS10001520
resource_type: QA
platform: Xcode Developer Tools
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/plat/plat10.html
archived_at: '2026-07-18T02:29:51.701159Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Tools](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTools-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Tools](https://developer.apple.com/referencelibrary/Java/idxTools-date.html)

|  |
| --- |
| Technical Q&A PLAT10Makefiles Problems |

|  |  |  |
| --- | --- | --- |
| ---   Q: We're having trouble with one of our MPW makefiles. We want to force a full build of the application whenever the "Test.make" file or the "DefineCreator" file is changed, but we've been unable to do this successfully. Although we've had some success, the methods we've tried always execute some of the commands, even if none of the dependents have changed.  A: There are two approaches you can take to resolve this problem:  Add the make file and the "DefineCreator" file to each dependency line in your make file. For example, in 7Edit, each of the object files is dependent on the corresponding .h and .c files, as well as on the MakeFile itself, so the dependency line for each C file is:   |  | | --- | | ``` SVEditUtils.c.o [[florin]] makefile SVEditUtils.h SVEditUtils.c SVEditGlobals.h     c  SVEditUtils.c -sym on ``` |   Since adding the MakeFile and any additional files to each dependency line could be more work than it's worth, you could also use a double dependency rule to make all the object files dependent on the MakeFile and your "DefineCreator" file. Your MakeFile might include the following:   |  | | --- | | ``` OBJECTS = [[partialdiff]]    SVEditGlobals.c.o [[partialdiff]]    SVEditUtils.c.o [[partialdiff]]    SVEditAEUtils.c.o [[partialdiff]]    SVEditions.c.o [[partialdiff]]    SVEditWindow.c.o [[partialdiff]]    SVEditFile.c.o [[partialdiff]]    SVAppleEvents.c.o [[partialdiff]]    SVEditMain.c.o [[partialdiff]] {OBJECTS} [[florin]][[florin]] makeFile DefineCreator SVEditGlobals.c.o [[florin]][[florin]] SVEditGlobals.h SVEditGlobals.c ``` |   (more dependencies following...)  If either the MakeFile or the DefineCreator file is changed, the entire application will be rebuilt. You don't need to include any further build commands, since you would be using the default build rules in this case.  For additional information, see __"Make and Make Files" in Chapter 4 of _Building and Managing Programs in MPW____._ |

#### [Jun 01 1995]

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
