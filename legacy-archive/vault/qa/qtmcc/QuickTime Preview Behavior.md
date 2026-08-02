---
title: QuickTime Preview Behavior
apple_id: DTS10001953
resource_type: QA
platform: macOS
topic: Cross Platform
technology: null
published: '1996-11-27'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc10.html
archived_at: '2026-07-18T02:38:46.927658Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > QuickTime for Windows](https://developer.apple.com/referencelibrary/QuickTime/idxQuickTimeforWindows-date.html)

|  |
| --- |
| Technical Q&A QTMCC10QuickTime Preview Behavior |

|  |
| --- |
| Q What's the logic behind the create/update preview behavior in the SFPGetFilePreview dialog? If I create previews for QT movies I sometimes get preview movies and sometimes preview pictures. With QT movies that already have previews I sometimes get an update button and sometimes I get a dimmed create button. What determines the behavior?   AThe expected behavior is this: PICT files (or files that QuickTime can import as PICT ala the new graphic import components) don't have durations to them so they can only have a preview PICT in the StandardFilePreview dialog. Movies can have both a poster PICT and a movie preview.  In StandardFilePreview, via the preview components, when a movie or PICT file is selected, the preview component will first see if a preview already exists in the file, stored in the 'pnot' resource. The 'pnot' resource also identifies whether the preview is a PICT, a movie, etc. The preview component then compares a timestamp in the 'pnot' resource to the modification date of the selected file to see if the preview is current or not. If the 'pnot' date is older than the last modified date of the file, StandardFilePreview will show the Update button in its dialog (using the 'pmak' components to create the new preview if the user selects this option).  If no 'pnot' resource is found in the selected file and a 'pmak' component exists that can create a preview for the selected file type (QuickTime 2.5 supplies PICT, MOOV, and QTIF 'pmak' components) then the Create button will be active in the StandardFilePreview dialog.  It should be noted that sound files preview in a little different way. The 'pnot' components create an automatic 10-second (if there's that much sound) preview for supported sound file types without needing a 'pnot' resource in the file.  You can read more about Preview Components in [Inside Mac:QuickTime Components.](https://developer.apple.com/documentation/quicktime/qtdevdocs/RM/frameset.htm) [Nov 27 1996] |

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
