---
title: Native App Slowdown
apple_id: DTS10001546
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/ppcsys/ppcsys05.html
archived_at: '2026-07-18T02:29:54.269071Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A PPCSYS05Native App Slowdown |

|  |  |
| --- | --- |
| ---   Q: We are drawing palette icons using a loop which contains the following:   |  | | --- | | ```      GetIcon      HLock      CopyBits      ReleaseResource ``` |   Our native PowerMacintosh version seems to draw these palettes slower than our 68K version running under emulation, which suggests a Mixed Mode Manager slowdown. All of the routines we call, however, are documented as native on the PowerMac.  Here are some rough but representative timings:  Timings on 8100/80 - 8 bit screen - System 7.5  microseconds percent of loop  `GetIcon` 2000us 38%  `CopyBits` 400us 7%  `ReleaseResource` 2850us 54%  Is it reasonable for `CopyBits` from a 1-bit bitmap to an 8-bit screen to take less than 10% of the time of this loop? I have verified that all of the icon resources are in memory when this takes place, so the `GetIcon` & `ReleaseResource` just need to deal with the resource map.  Aren't all the Resource Manager calls native? These timings seem to indicate they are calling emulated routines.  A: It is not really surprising that you're seeing these numbers, since the Resource Manager calls you are using are not native, and they generally call File Manager routines, which aren't native either. In a way, what you're asking is, which routines are native and which are not? Unfortunately, this is the wrong question: just because something is not native now doesn't mean it never will be. Designing your application based on assumptions you think are valid today is a dangerous thing to do, because your workaround won't necessarily continue to be faster in the future.  Relying on the Resource Manager to be fast is generally not a good idea. Resource files slow down drastically once they reach a certain size (see the Toolbox Technote, "OV 8 Managerial Abuse"). Also, if the resource chain is long, you'll have problems. Since these are icons in a palette, you'll probably want to cache them somewhere, because you'll continually need them as you update your palette.  One approach you can take is to load your icons in one of the first few operations in your initialization code, just after calling `MaxApplZone` (possibly moving them high and locking them, since you don't want them to move during a `CopyBits` operation). This technique yields very good performance on the redraws that the palette needs, in exchange for a few kilobytes of memory. Don't forget to mark the resources as non-purgeable, just for good measure.  Rather than using `CopyBits`, you might want to use the IconUtilities package to obtain and draw your icons (this is documented in _Inside Macintosh: More Macintosh Toolbox_), either to load an icon family, or to build an icon cache. Using the Icon utilities helps your application to do the right thing for different screen depths. Also, the icon drawing routines are optimized to perform well under a variety of conditions.  Finally, if you need to get at Icons for documents and applications, check out the MoreFiles sample. This is on the Developer CD Series as sample code. DTGetIcon is a useful utility for obtaining Icons. |

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
