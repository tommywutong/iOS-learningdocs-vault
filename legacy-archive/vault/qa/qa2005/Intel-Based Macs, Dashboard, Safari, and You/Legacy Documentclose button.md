---
title: Intel-Based Macs, Dashboard, Safari, and You
apple_id: DTS10003815
resource_type: QA
platform: Safari|macOS
topic: Xcode
technology: null
published: '2006-12-13'
source_url: https://developer.apple.com/library/archive/qa/qa2005/qa1451.html
archived_at: '2026-07-18T02:38:33.731779Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



|  |  |
| --- | --- |
|  |  |
| [ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Apple Applications](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxAppleApplications-date.html) > | [ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Apple Applications](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxAppleApplications-date.html) > |
|  |  |

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Internet & Web > Web Content](https://developer.apple.com/referencelibrary/InternetWeb/idxWebContent-date.html)

|  |
| --- |
| Technical Q&A QA1451Intel-Based Macs, Dashboard, Safari, and You |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Q: How does the transition to Intel-based Macintosh computers affect Dashboard widgets and websites viewed in Safari? A: In most cases, Dashboard widgets contain standard web elements such as HTML, JavaScript, CSS, and of course image files. Widgets such as these, which don't use compiled code, should work exactly the same on Intel-based Macs as they do on PowerPC-based Macs.  Dashboard widgets that use plug-ins, however, will need to make sure those plug-ins have been built as universal binaries. There are two types of plug-ins that a widget can make use of:   - __Widget Plug-Ins.__ If your widget contains a plug-in, you must build the plug-in as a universal binary for it to run natively on an Intel-based Macintosh computer. - __Internet Plug-Ins.__ Internet plug-ins, typically incorporated via the `embed` tag, must also be built as universal binaries to run in Dashboard and/or Safari on Intel-based Macintosh computers. If your Dashboard widget (or website) uses a third-party internet plug-in, please contact the developer of that plug-in to make sure a universal binary version of the plug-in is available or in progress.   If you are the developer of a widget plug-in or internet plug-in, you should consult the [Universal Binary Programming Guidelines](https://developer.apple.com/documentation/MacOSX/Conceptual/universal_binary/) to find out whether or not your code needs to be updated for compatibility with Intel-based Macintosh computers. Depending on the tasks your plug-in performs, converting to a universal binary may require more effort than simply rebuilding it in Xcode with the appropriate flags. Document Revision History  | Date | Notes | | --- | --- | | 2006-12-13 | Editorial changes | | 2006-01-10 | New document that concerns and details regarding widget and web development for Intel-based Macintosh computers | |

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
