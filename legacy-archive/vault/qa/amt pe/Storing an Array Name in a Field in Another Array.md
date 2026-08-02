---
title: Storing an Array Name in a Field in Another Array
apple_id: DTS10001126
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/amt_pe/amt_pe24.html
archived_at: '2026-07-18T02:29:23.947920Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Apple Applications](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxAppleApplications-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Apple Applications](https://developer.apple.com/referencelibrary/AppleApplications/index.html)

|  |
| --- |
| Technical Q&A AMTPE24Storing an Array Name in a Field in Another Array |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ---   The Apple Media Tool and Apple Media Tool Programming Environment products have been discontinued. For more information check out: [AMT/PE Discontinued](https://developer.apple.com/library/archive/qa/amt_pe/whatsup.html).  Q: I am having a problem accessing items from arrays with other arrays. I get a runtime error:   |  | | --- | | ``` File 'SERVER DRIVE:PROJECTS:TEST:LBB PROJECT WITH AMTCX:SOURCES:ALPHADB.K'; Line 89 # K call: MESSAGE has no _COUNT! ``` |    I use the following code to extract the name of a particular array and make CurrentAlphaIndex refer to that particular array:   |  | | --- | | ``` self.CorrectAlphaArray := self.AlphaArray; self.CurrentAlphaIndex := (self.CorrectAlphaArray @ self.CurrentRec @ 3); ``` |    This is the line it stops working on:   |  | | --- | | ``` while (loopIndex <= #(self.CurrentAlphaIndex @ LineNum @ 2)) loop ``` |    What gives?  A: Because of the way the parser works (it works from right to left, instead of left to right), when you have several @ characters in the same statement, you have to use parentheses to specify how the expression should be parsed.  In other words, the parser is reading:   |  | | --- | | ``` self.CurrentAlphaIndex @ LineNum @ 2 ``` |    as:   |  | | --- | | ``` self.CurrentAlphaIndex := (self.CorrectAlphaArray @ (self.CurrentRec @ 3)); ``` |    However, what you _mean_ is:   |  | | --- | | ``` self.CurrentAlphaIndex := ((self.CorrectAlphaArray @ self.CurrentRec) @ 3); ``` |    This is also true for the other line:   |  | | --- | | ``` while (loopIndex <= #(self.CurrentAlphaIndex @ LineNum @ 2)) loop ``` |    The solution is to use parentheses to specify what you want. |

#### [Aug 01 1995]

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
