---
title: Movie Import Component Selectors
apple_id: DTS10001952
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1996-08-21'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc09.html
archived_at: '2026-07-18T02:38:46.869804Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > QuickTime Component Creation](https://developer.apple.com/referencelibrary/QuickTime/idxQuickTimeComponentCreation-date.html)

|  |
| --- |
| Technical Q&A QTMCC09Movie Import Component Selectors |

|  |
| --- |
| Q I'm working on a movie import component which manages multiple data files. I have noticed in QuickTime 2.5 that there are new selectors in the Movie Import API that are not described in [_Inside Mac:QuickTime Components._](https://developer.apple.com/documentation/quicktime/qtdevdocs/RM/frameset.htm) Although I found some information in [Technote QT04: QuickTime 1.6.1 Features](https://developer.apple.com/library/archive/technotes/qt/qt_04.html), I have not been able to locate any information about the 'kMovieImportGetFileTypeSelect' and'kMovieImportDataRefSelect' selectors. Can you tell me something about these? A The 'kMovieImportGetFileTypeSelect' and 'kMovieImportDataRefSelect' selectors were added to support some features that were under investigation with the QuickTime for Netscape plug-in. At this time, there isn't any other code that makes use of these selectors. While these APIs are supported by some of the Apple Movie Import Components, they do not provide any new functionality and there is no reason to consider implementing them in your Movie Import Component at this time. Documentation will be provided on these routines if and when it is actually required. [Aug 21 1996] |

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
