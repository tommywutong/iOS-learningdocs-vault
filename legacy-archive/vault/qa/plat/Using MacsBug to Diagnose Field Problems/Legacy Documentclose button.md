---
title: Using MacsBug to Diagnose Field Problems
apple_id: DTS10001529
resource_type: QA
platform: Xcode Developer Tools
topic: null
technology: null
published: '1996-02-15'
source_url: https://developer.apple.com/library/archive/qa/plat/plat19.html
archived_at: '2026-07-18T02:29:52.202834Z'
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
| Technical Q&A PLAT19Using MacsBug to Diagnose Field Problems |

|  |  |
| --- | --- |
| ---   Q: I have a customer who is encountering a problem using my product. Can you suggest a way to use MacsBug to diagnose problems at a customer site?  A: Yes. Here, in a few steps, is a technique for using MacsBug to diagnose field problems.   1. Take a clean copy of the latest MacsBug. (You can find the latest MacsBug on the Tool Chest developer CD in the path    __:Tool Chest:Testing & Debugging:Debuggers & dcmds:MacsBug 6.5.2__     or from anonymous ftp via    [MacsBug download](ftp://dev.apple.com/devworld/Tool_Chest/Testing_-_Debugging/Debuggers_-_dcmds/)). 2. Create a file using ResEdit (or Resorcerer, etc.) containing a '`mxbm`' resource (the '`mxbm`' resource contains macro definitions). 3. In this '`mxbm`' resource, define the macro 'everytime' as follows:  |  | | --- | | ``` stdloginto 'Send to the programmer' ``` |   This way, if MacsBug is ever invoked due to a program error, you will automatically get a log of what occurred. The log, named "Send to the programmer" will exist on the desktop.  4) Have your customer send you the log file created by the above steps. See Also:  - See page 219 of the _MacsBug Reference and Debugging Guide_, Apple   Computer (Addison-Wesley) for details of the 'everytime' macro.  - For details of what '`stdloginto`' does, look at the '`mxbm`' resource 'log stuff'   in MacsBug's resource fork. |

#### [Feb 15 1996]

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
