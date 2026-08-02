---
title: White Backgrounds for Dialog editText Items
apple_id: DTS10002220
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-10-13'
source_url: https://developer.apple.com/library/archive/qa/tb/tb34.html
archived_at: '2026-07-18T02:38:56.839689Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB34White Backgrounds for Dialog editText Items |

|  |
| --- |
| Q I would like to have a colored background for my dialog box but I would like the TextEdit fields in my dialog box to be white. Is this possible to do? Is there some sample code available?   A Generally speaking, this coloring is achieved via resources, not code. In addition to the '`dctb`' resource, you need to create an '`ictb`' resource. To download a sample of an application using this kind of resource click [here](https://developer.apple.com/library/archive/qa/tb/downloads/whiteedittext.hqx).   The '`ictb`' resource is documented on page 6-76 and starting again on page 6-158 of  _[Inside Macintosh: Macintosh Toolbox Essentials](https://developer.apple.com/documentation/mac/Toolbox/Toolbox-2.html)_. The best way I know of to create and edit '`ictb`' resources is with Resorcerer, but you can also create them with a '`.r`' file compiled by either MPW's Rez or the Metrowerks CodeWarrior equivalent.   Here are some references to web sites for the aforementioned tools:   - Resorcerer : [<http://www.mathemaesthetics.com/>](http://www.mathemaesthetics.com/) - Apple Developer Tools : [<http://developer.apple.com/tools/>](https://developer.apple.com/tools/) - CodeWarrior : [<http://www.metrowerks.com/>](http://www.metrowerks.com/)  [Oct 13 1997] |

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
