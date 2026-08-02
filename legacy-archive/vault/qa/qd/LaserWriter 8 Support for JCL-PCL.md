---
title: LaserWriter 8 Support for *JCL/PCL
apple_id: DTS10001910
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-05-25'
source_url: https://developer.apple.com/library/archive/qa/qd/qd57.html
archived_at: '2026-07-18T02:38:38.508750Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A QD57LaserWriter 8 Support for \*JCL/PCL |

|  |
| --- |
| ---   Q: I have \*JCL/PCL keywords in my PPD to describe some hardware-specific features, but the LaserWriter 8 drivers seem to ignore them. Why?  A: LaserWriter 8 does not have support for \*JCL keywords. Apple has opted not to add this support due to the complications it introduces. For instance, when saving to disk, if the JCL code is included, then that file cannot be sent to a non-JCL PostScript printer. If the JCL is not included in the file, then certain printer features are not accessible. We also feel that all features of a PostScript printer should be controllable via PostScript; therefore, we recommend that printer vendors ensure that all of the printer features are in their printer implementation of PostScript. Instead of relying on \*JCL keywords to describe your hardware-specific features, we recommend that you use the PostScript page device mechanism and provide access to the feature(s) you need via `setpagedevice` code in the PPD file. |

#### [May 25 1998]

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
