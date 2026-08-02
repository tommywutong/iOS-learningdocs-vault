---
title: Special Profile Sizes in ColorSync Manager
apple_id: DTS10001131
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/c/cs03.html
archived_at: '2026-07-18T02:29:24.499715Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > ColorSync](https://developer.apple.com/referencelibrary/GraphicsImaging/idxColorSync-date.html)

|  |
| --- |
| Technical Q&A CS03Special Profile Sizes in ColorSync Manager |

|  |
| --- |
| ---   Q: There is no mention of special profile sizes (for processing efficiency) in ColorSync Manager (2.0) or in International Color Consortium Profile Format. Specifically, it does not say whether defining the 3-D lookup tables with sizes that are a power of 2 (+1) is any faster than using any other sizes. Defining tables that are 5x5x5, 9x9x9, 17x17x17, or 33x33x33 should be faster to implement, since you can use fast shifts instead of integer divides in the lookup math. Does the default CMM have any optimizations such as this? If so, what are they?  A: It doesn't matter how you dimension the tables, because the default CMM creates private multi-dimensional tables internally.  Q: On page 1-28 of ColorSync Manager (2.0), under "L\*a\*b\* Color Value", it states that each color component is within the range of 0 to 65,280. Shouldn't this be 0 to 65,535, since this is this value for the other spaces and in ICC Profile Format.  A: 65,280 is the correct value. The ICC profile specifies 0xFF00 as the maximum value for this space.  Q: What exactly are the internal parameters for the quality setting (i.e., how many bits and how large a LUT is built for "draft" versus "normal" versus "best")?  A: The quality flag bits provide a convenient place in the profile for an application to indicate the desired quality (potentially at the expense of speed and memory) of a color match. In ColorSync 2.0, these qualities do not mandate the use of one algorithm over another. Instead, they are just "recommendations," which the CMM may choose to ignore or implement.  This is the procedure the CMM uses to decide whether to ignore or implement the quality recommendations specified in the flag bits:   1. When the `'appl'` CMM builds a `ColorWorld` from two or more profiles, and one or more of these profiles contains TRC curves or A2Bx tables, it also builds a private, multi-dimensional look-up table. 2. The quality flag bits determine the resolution of the private, multi-dimensional look-up table. 3. Draft quality is treated the same as Normal quality by the `'appl'` CMM. This is how the trade-offs for Best quality differ from those for Normal/Draft quality:  1. Quality: In most cases, since the quality is only slightly better in Best mode, the difference is difficult to see, unless one of the profiles has a high gamma value. For high gamma values, the extra resolution in the private, multi-dimensional look-up table is helpful. 2. Speed: Best mode typically takes twice as long to build a `ColorWorld` (approximately two seconds versus approximately one second). However, once the `ColorWorld` is built, the time to use it is the same for either mode. In other words, the time to match a bitmap is the same for both modes (the rate is approximately 1.5MB/second on a PowerMac 8100/110). 3. Memory: Best mode requires significantly more memory than Normal/Draft mode. A `ColorWorld` typically requires 120K of heap space in Best mode versus 25K in Normal mode, and the "high-water" memory requirement while building a ColorWorld is typically 300K for Best mode versus 90K for Normal mode.   Note that these guidelines apply only to the default `'appl'` CMM. The trade-offs between speed, quality, and resources may be quite different for other CMMs.  Q: On page 1-64 of ColorSync Manager (2.0), it states that a device-linked profile may not be used with `NCWNewColorWorld`, and `NCMBeginMatching` implies that device-linked profiles cannot be used. How is a device-linked profile used for color matching? Is this what `CWConcatColorWorld` is used for?  A: Use `CWConcatColorWorld` for color matching by passing it the device-linked profile.  Q: On pages 55 and 56 of ICC Profile Format, in the description of the profile headers, there is no mention of the "quality" setting. Isn't the quality setting part of the profile?  A: A profile is typically a self-contained set of data that includes all the information a CMM needs to perform a color match. Therefore, when an application needs to embed a profile in a document, it should not have to make any changes to the profile. However, there are two profile attributes that an application can change to modify the profile's behavior ("rendering intent" and "quality"). To change the behavior of a profile when embedding it in a document, the application first sets the appropriate bit in the profile's header.  Q: On page 55 of ICC Profile Format where the header is described, what is the rendering intent of this profile for the CMM? Doesn't the user select the rendering intent? Doesn't the profile contain data that allows it to be converted under any of the four rendering intents? Is this a "default" rendering intent that is used if the user does not specify one explicitly, or is this field always hard-coded with 0, 1, 2, and 3 in the four bytes to signify that all four rendering intents are supported? Why does this field exist if all of these intents must always be supported?  A: "Rendering Intent" can be changed before a profile is embedded. The value of the profile's header-intent field determines how the CMM performs the color match. For example, a CMM would use the A2B2 tag if the rendering intent was three. However, the profile may also contain A2B0 and A2B1 tags (not used in this example) regardless of the intent value. There is no default intent, but most profiles start with the intent field set to 0.  Q: Is an "Embedded Profile," as mentioned in "Profile Flags" on page 57 of ICC Profile Format, a profile that is included in a data file (as opposed to one that stands alone)? The documents states that, "Profile cannot be used independently from the embedded color data." What does this mean, and is it only applicable to an embedded profile?  A: Two bits were added to the ICC specification for copyright information to protect the rights of profile builders. Setting the "Profile Embedded" bit while embedding a profile in a document tells other applications that can extract profiles from documents that the embedded profile is protected. Although the "Profile Embedded" bit cannot prevent unethical behavior by another application (such as copying the embedded profile), setting this bit and the "Profile Use" bit indicates the profile vendor's intent to retain the rights to the profile's contents.  Q: I want to go directly from an input CMYK space to an output CMYK space (without going through an intermediate three-component space) to preserve the original GCR/UCR settings. Can I create a "link" profile for this purpose? If I do, will I have to write my own CMM to use it?  A: You can build a CMYK to CMYK device-link profile for this purpose, and you can use it without writing your own CMM. |

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
