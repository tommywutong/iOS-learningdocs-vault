---
title: Make sure your PPD Plugin calls ppdCloseCompiledPPDFromTicket
apple_id: DTS10002377
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2004-02-19'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1275.html
archived_at: '2026-07-18T02:38:29.912599Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Printing > Carbon](https://developer.apple.com/referencelibrary/Printing/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A QA1275Make sure your PPD Plugin calls ppdCloseCompiledPPDFromTicket |

|  |
| --- |
| ---    Q: With my PPD Plugin installed, why can I only show the print dialog in an application a few dozen times before things start to misbehave?  A: This problem occurs when a PPD Plugin calls `ppdOpenCompiledPPDFromTicket` to gain access to the PPD contents but fails to make a matching call to `ppdCloseCompiledPPDFromTicket` . The end result is that the plugin, and therefore the application it is running under, opens lots of files but doesn't close them. Once the application hits the maximum number of open files, bad things start to happen, such as the Copies & Pages PDE failing to display.   ---  [Feb 19, 2004] |

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
