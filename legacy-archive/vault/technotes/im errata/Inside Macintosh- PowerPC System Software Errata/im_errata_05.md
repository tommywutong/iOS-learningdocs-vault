---
title: 'Inside Macintosh: PowerPC System Software Errata'
apple_id: DTS10002525
resource_type: Technical Note
platform: macOS
topic: null
technology: null
published: '1994-10-01'
source_url: https://developer.apple.com/library/archive/technotes/im_errata/im_errata_05.html
archived_at: '2026-07-26T19:53:37.462668Z'
---
> 导航：[总目录](../../../README.md) · [technotes](../../../_indexes/technotes.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Notes](https://developer.apple.com/library/archive/technicalnotes/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalnotes/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalnotes/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Document[close button](javascript:closeWatermark())

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Note IMERRATA05Inside Macintosh: PowerPC System Software Errata |

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | |  | | --- | | images/tnmenutop.gif | | CONTENTS | | [Topics](#)   [Chapter 1 - Introduction to PowerPC System Software](#)    [Chapter 3 - Code Fragment Manager](#)   [References](#)   [Downloadables](#) | | images/tnmenubottom.gif | | This Technical Note discusses known errors and omissions in _Inside Macintosh: PowerPC System Software_.  [Oct 01 1994] |       ---      Topics  - Correction to Discussion of Routine Descriptors October 1994 - Correction to Figure 1-2 October 1994 - Clarification of MakePEF October 1994 - Correction to Listing 3-6 October 1994 - Clarification of `GetDiskFragment` Description October 1994 - Correction to `FindSymbol` Symbol Classes October 1994 - Correction to Description of `GetIndSymbol` October 1994   [Back to top](#) Chapter 1 - Introduction to PowerPC System SoftwareCorrection to Discussion of Routine Descriptors Page 1-17, Routine Descriptors  The last paragraph on this page mentions "the value passed in the `gActionProc` parameter". This is a typographical error. The correct description should be "the value passed in the `myActionProc` parameter." Correction to Figure 1-2 Page 1-24, Imports and Exports  Figure 1-2 contains an incorrect label." `Exit to Shell`" should be "`ExitToShell`." Clarification of MakePEF Page 1-26, Imports and Exports; page 1-38, Executable Resources  The MPW tool MakePEF might be replaced by other equivalent tools in future releases of the Macintosh on RISC development tools.  [Back to top](#) Chapter 3 - Code Fragment ManagerCorrection to Listing 3-6 Page 3-14, Getting Information About Exported Symbols  The index used in a call to `GetIndSymbol` is zero-based, not one-based. As a result, the `for` statement in Listing 3-6 should be as follows:   ``` for (myIndex = 0; myIndex < myCount; myIndex++) ```  Clarification of GetDiskFragment Description Page 3-19, 3-31  The constant `kWholeFork` (documented as a possible value for the `length` parameter to `GetDiskFragment`) and all the Rez constants listed on pages 3-30 through 3-31 are defined in the MPW interface file `CodeFragmentTypes.r`. To use the constant `kWholeFork` in C source files, you should define it to be 0. Correction to FindSymbol Symbol Classes Page 3-25, 3-32  The symbol class constants returned by `FindSymbol` are listed incorrectly. The correct constants should be `kCodeSym`,`kDataSym`, and `kTVectSym`. Correction to Description of GetIndSymbol Page 3-26  The index used in a call to `GetIndSymbol` is zero-based, not one-based. As a result, the description of the `symIndex` parameter should be as follows:  A symbol index. The value of this parameter should be greater than or equal to 0 and less than the value returned by the `CountSymbols` function.  [Back to top](#) References [Back to top](#)   Downloadables  |  |  |  | | --- | --- | --- | | Acrobat gif | Acrobat version of this Note (K) | [Download](https://developer.apple.com/library/archive/technotes/im_errata/pdf/im_errata_05.pdf) |    [Back to top](#) |

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
