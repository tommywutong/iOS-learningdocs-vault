---
title: ColorSync 2.0
apple_id: DTS10001130
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/c/cs02.html
archived_at: '2026-07-18T02:29:24.174529Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



|  |  |
| --- | --- |
|  |  |
| [ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) > | [ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) > |
|  |  |

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > ColorSync](https://developer.apple.com/referencelibrary/GraphicsImaging/idxColorSync-date.html)

|  |
| --- |
| Technical Q&A CS02ColorSync 2.0 |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Q: I'm using the `CMOpenProfile`() second argument (ColorSync2, seed #2), and I get a -4205 error when I attempt to open a profile. I currently fill the type field in the data structure `CMProfileLocation` with 0, but I don't know if this is correct. What is the item named type for? A: The second argument of the `CMProfileLocation` structure is a union of different types (corresponding to where a profile can be located) and a short field that allows you to determine which union field to use. In most cases, a ColorSync profile is stored in a disk file whose location your application provides using a data structure of type `CMProfileLocation`, which is described in "File Specification for File-Based Profiles" on page 1-19 of the Draft Documentation for Inside Macintosh: ColorSync.  You can specify this type of profile location with the `CMOpenProfile`, `CMNewProfile`, `CMCopyProfile`, and `CMNewLinkProfile` functions. This is a relocatable, memory-based profile, and the `CMProfLoc` union holds a handle to it in a structure of type `CMHandleLocation`. For a description of the `CMHandleLocation` type definition, see "Pointer Specification for Memory-Based  Profile" on page 1-20 of Inside Macintosh: ColorSync. You can specify this type of profile location only with the `CMOpenProfile` function. Document Revision History  | Date | Notes | | --- | --- | | 1995-05-01 | Explains CMProfileLocation's second argument, where a ColorSync profile is, and the type of a profile location. | |

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
