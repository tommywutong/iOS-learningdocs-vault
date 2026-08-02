---
title: 'Inside Macintosh: Overview Errata'
apple_id: DTS10002524
resource_type: Technical Note
platform: macOS
topic: null
technology: null
published: '1994-10-01'
source_url: https://developer.apple.com/library/archive/technotes/im_errata/im_errata_04.html
archived_at: '2026-07-26T19:53:37.449469Z'
---
> 导航：[总目录](../../../README.md) · [technotes](../../../_indexes/technotes.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Notes](https://developer.apple.com/library/archive/technicalnotes/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalnotes/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalnotes/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Document[close button](javascript:closeWatermark())

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Carbon](https://developer.apple.com/referencelibrary/Carbon/index.html)

|  |
| --- |
| Technical Note IMERRATA04Inside Macintosh: Overview Errata |

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | |  | | --- | | images/tnmenutop.gif | | CONTENTS | | [Topics](#)   [Chapter 1 - Introduction](#)   [Chapter 3 - Resources](#)   [Chapter 5 - Drawing](#)   [References](#)   [Downloadables](#) | | images/tnmenubottom.gif | | This Technical Note discusses known errors and omissions in _Inside Macintosh: Overview_.  [Oct 01 1994] |       ---      Topics  - Correction to `GreetMe` Application Code Listing October 1994 - `UseResFile` Incorrectly Named October 1994 - Correction to List of Reserved Resource Types October 1994 - Correction to QuickDraw Coordinate Plane October 1994   [Back to top](#) Chapter 1 - IntroductionCorrection to `GreetMe` Application Code Listing Page 3  The call to the `TextFont` function in Listing 1-1 should occur before `StringWidth` is called. In addition, Listing 1-1 should include all the standard initializations, even for managers not explicitly called by the code listing. For example, Listing 1-1 should call `TEInit`.  [Back to top](#) Chapter 3 - ResourcesUseResFile Incorrectly Named Page 54  The documentation refers to the `SetResFile` routine. The routine should be `UseResFile`. Correction to List of Reserved Resource Types Page 55  The documentation states that "Apple reserves for its own use all resource types that include any lowercase letters." This is incorrect. Apple reserves resource types consisting entirely of lowercase letters and special symbols, as well as any other system-defined resource types that already exist. In general, developer-defined resource types should contain at least one uppercase letter.  [Back to top](#) Chapter 5 - DrawingCorrection to QuickDraw Coordinate Plane Page 86  The documentation states that the QuickDraw coordinate plane extends from -32767 to 32,767 along the _x_ and _y_ axes. The correct range is -32,768 to 32,767.  [Back to top](#) References _Inside Macintosh: Overview_  [Back to top](#)   Downloadables  |  |  |  | | --- | --- | --- | | Acrobat gif | Acrobat version of this Note (40K) | [Download](https://developer.apple.com/library/archive/technotes/im_errata/pdf/im_errata_04.pdf) |    [Back to top](#) |

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
