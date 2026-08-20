---
title: QuickDraw GX Printer Drivers & Configuration
apple_id: DTS10001219
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd04.html
archived_at: '2026-07-18T02:29:32.271228Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD04QuickDraw GX Printer Drivers & Configuration |

|  |  |
| --- | --- |
| ---   Q: We want our printer drivers to be as consistent as possible with Apple's implementations. Our present method of querying the printer for configuration information, such as the number of trays and so on, is to send a blank page to open the connection. I noticed that, in QuickDraw GX 1.1d2, you query the printer for this information at DTP creation time. I'd like to see some samples of Apple's code so I can get an idea of how you accomplish this. I want to be sure I'm opening and closing the connection appropriately.  A: In pre-1.1.1 versions of QuickDraw GX, printer queries caused some problems for both our developers and our end users. While we don't have any code samples from QuickDraw GX 1.1d2 we can show you, because all the code is currently in our drivers, we can tell you how our drivers query the printer for configuration information.    This is a relatively simple process. What you need to do is to override `GXDefaultDesktopPrinter`. In your override module, you need to:   - Forward the message. - Get the `'comm'` resource from the DTP (use `GXFetchTaggedData` for this). - If the `'comm'` resource is a PAP resource (of type `'PPTL'`) then send the following messages:  |  | | --- | | ```     Send_GXOpenConnection     Send_SetupImageData     Send_GXCloseConnection ``` |   Bear in mind that this only works for a Postscript PAP case. If you're working on a raster printer, you need to query the printer yourself, instead of sending the `SetupImageData` message. Also, be sure to check the version of QuickDraw GX, as this method only works on 1.1.1 or later. |

#### [May 01 1995]

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
