---
title: Long Timeout When Opening Certain Files - A StyleWriter Quirk
apple_id: DTS10001895
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-04-08'
source_url: https://developer.apple.com/library/archive/qa/qd/qd42.html
archived_at: '2026-07-18T02:38:37.693688Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A QD42Long Timeout When Opening Certain Files - A StyleWriter Quirk |

|  |
| --- |
| ---   Q: One of our customers has been complaining that while opening my app files, the computer idles in a `_vSyncWait` loop for about 45 seconds before that file becomes ready for use. The same thing happens when the application is launched. It seems that the computer is idling while trying to connect to a remote printer (in this case, a StyleWriter). The printer is off-line since the computer it is connected to is off. When the printer is connected locally, there are no problems whatsoever.  Obviously, the PrinterShare software is (incorrectly) looking for a nonexistent print server when the driver is opened, and taking a long time to timeout on the remote connection. It seems reasonable that the printing software should -only- try a remote connection when it's actually spooling or imaging to the remote printer.  Can you offer any insight or workaround?  A: Your customer is probably using the StyleWriter 1200 driver for the printer. This driver is intended to work for three printers (StyleWriter I, StyleWriter II, StyleWriter 1200), each with different engines, options and print records. When any validation is needed for the print record, PrinterShare needs to communicate with the printer to find out exactly which variety of StyleWriter the user has attached before it can validate. This is where trouble begins.  PrinterShare is attempting to communicate with the printer to find out what kind it is, but since there is no printer out there the user has to wait for a timeout (in this case, 45 secs).  This leaves you with basically two solutions:   1. Leave your app as is, since this should only happen with the StyleWriter    1200 driver. 2. Don't do any `PrintRecord` validation or driver opening until your app is    actually going to print. This way the timeout wait is somewhat justified and    understandable to the user, since there is no printer out there. |

#### [Apr 08 1996]

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
