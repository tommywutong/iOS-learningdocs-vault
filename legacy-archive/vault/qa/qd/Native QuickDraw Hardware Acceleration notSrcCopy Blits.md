---
title: Native QuickDraw Hardware Acceleration notSrcCopy Blits
apple_id: DTS10001913
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-06-28'
source_url: https://developer.apple.com/library/archive/qa/qd/qd60.html
archived_at: '2026-07-18T02:38:38.685909Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A QD60Native QuickDraw Hardware Acceleration notSrcCopy Blits |

|  |  |
| --- | --- |
| ---   Q: How does Native QuickDraw (NQD) Hardware Acceleration (HWA) handle `notSrcCopy` Blits?  A: NQD HWA handler routes all `notSrcCopy` blits to the appropriate hardware accelerated blitter as described below.  The key to understanding the `notSrcCopy` blit is to realize that QuickDraw will do one of three things based on color depth and color table matching:   - If color depths (and color tables in case of 8 bits per pixel color) match, the blit will be sent to bit blit function for direct blitting. - If color depths (or color tables) do not match and the source is 16 bits per pixel or greater, the blit will be sent to the scale blit function with the mode indicating `notSrcCopy`. Additionally, `bMustScale` will be set to __0__ and the `scaleTable` will be invalid (do not assume it will be `NULL`). In this case, the accelerator developer should apply standard color QuickDraw rules for `notSrcCopy` to the source, generating the appropriate destination color (using the inverse color table if required for 8 bits per pixel destinations). - If color depths (or color tables) do not match and the source is 8 bits per pixel or less, the blit will be sent to the scale blit function with the mode indicating `srcCopy`. Additionally, `bMustScale` will be __1__ and the `scaleTable` will be valid. The scale table will have 2 elements for 1-bit sources and 256 elements for 8 bits per pixel sources. Each element will contain the color or index (in destination bit depth) into which each source index should map. For 16 and 32 bits per pixel destinations, the alpha bits will be zeroed (that is, `0x7FF` and `0x00FFFFFF` for white for 16 and 32 bits per pixel respectively). In this case, the blitter can use this mapping to directly map source to destination pixels.     |  | | --- | | __Note:__  In all modes it was observed that the `scaleTableIsRGBTable` field was always __0__. Use `bMustScale` to determine whether or not to use the `scaleTable` pointer and assume each entry in the scale table will be an RGB color or a color index as appropriate for the destination bit depth. |     [Jun 28 1999] Sending feedback…We’re sorry, an error has occurred. Please try submitting your feedback later. Thank you for providing feedback! Your input helps improve our developer documentation. How helpful is this document?\*   Very helpful   Somewhat helpful   Not helpful How can we improve this document?  Fix typos or links   Fix incorrect information   Add or update code samples   Add or update illustrations   Add information about...  \* _\* Required information_   To submit a product bug or enhancement request, please visit the [Bug Reporter](https://developer.apple.com/bugreporter/) page.  Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html) before you send us your feedback.  Copyright © 2016 Apple Inc. All rights reserved.   - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) - [Privacy Policy](http://www.apple.com/privacy/)    --- |
