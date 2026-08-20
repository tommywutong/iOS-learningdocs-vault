---
title: Using SourceSafe without MPW or Toolserver
apple_id: DTS10001525
resource_type: QA
platform: Xcode Developer Tools
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/plat/plat15.html
archived_at: '2026-07-18T02:29:51.953146Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Tools](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTools-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Tools](https://developer.apple.com/referencelibrary/Java/idxTools-date.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A PLAT15Using SourceSafe without MPW or Toolserver |

|  |
| --- |
| ---   Q: We are using SourceSafe for cross-platform source-code control (Mac and Windows). In the current version, while even the DOS version has a somewhat-graphical user interface, the Mac version runs as an MPW tool and only supports an ugly command-line interface.  I have been assigned the task of putting a pretty GUI on it for our artists to use, since these people have never seen a command line. I need to find a way to do this _without_ requiring them to have MPW or Toolserver on their machines. Where can I find source code, sample code, and/or documentation that explains how to run an MPW tool from another application - without having MPW or Toolserver available?  A: Short of rewriting SourceSafe as a stand-alone application, there is no way to achieve what you want to do. SourceSafe is a tool that is a small part of a large integrated environment - MPW. When you take MPW away, SourceSafe cannot run, because it requires the services that MPW provides. These services include file management, memory management, standard I/O, and others. If you want to run SourceSafe without MPW or ToolServer, you have to replace this functionality. Apple does not recommend that you try this without the source code for MPW, which Apple will not release. For additional information, see "Writing and Building MPW Tools," which is Chapter 9 of _Building and Managing Programs in MPW_ . |

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
