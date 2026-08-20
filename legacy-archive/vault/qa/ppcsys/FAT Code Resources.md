---
title: FAT Code Resources
apple_id: DTS10001545
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/ppcsys/ppcsys04.html
archived_at: '2026-07-18T02:29:54.163927Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Runtime Architecture](https://developer.apple.com/referencelibrary/Carbon/idxRuntimeArchitecture-date.html)

|  |
| --- |
| Technical Q&A PPCSYS04FAT Code Resources |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---   Q: I'm still having problems creating FAT code resources. Here's what I need to know: What exactly is a PEF container? You mentioned in passing that it was the output of MakePEF. When I look at that output, it has no resources; yet the MixedMode.r file says to include the line:   |  | | --- | | ``` $$Resource(BDef.rsrc", 'pCod', 128) // Specify name, type, and ID 	 of resourcecontaining a PEF container ``` |   How do I create a RESOURCE with a PEF container?  A: The output of MakePEF normally goes to the data fork of the file you specify in its "-o" option. With a Rez "read" statement you can read the PEF container and move it into the resource fork of an intermediate file (BDef.rsrc):   |  | | --- | | ``` read 'pCod' (128) "my.pef"; ``` |   The final $$Resource ("BDef.rsrc", 'pCod', 128), then reads that resource back in.  Q: In MixedMode.r, it gives an example of using a 'sdes' such as:   |  | | --- | | ``` type 'BDef' as 'sdes'; resource 'BDef' (1) {  $1,     // 68k ProcInfo  $1,     // PPC ProcInfo ``` |   What is the definition of `ProcInfo`?  A: `ProcInfo` describes the parameters and result values of your routine. Using the description of what exactly the "fields" are in this 32 bit value, you should be able to figure out the hex value. This has to be filled in for both the 68K and PowerPC versions. Since both are identical (= have the same prototype), the same value has to be used.  Q: In my 68K code resource, I use:   |  | | --- | | ``` RememberA0(); SetUpA4(); RememberA4(); ``` |   The note in `'sdes'` says that this can't be used currently for resources containing code with register-based calling conventions.  Will this affect me? Can I simply use different registers to circumvent this conflict? If this does affect me, how do you build a code resource without using the `Remember` and `SetUp` functions?  A: The `'sdes'` resource starts with some 68K code preamble that determines if `MixedMode` is available. This code thrashes D0, A0, and A1, so you can't use these registers to pass parameters. Note that A4 is not touched in the preamble. |

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
