---
title: SyncCGContextOriginWithPort
apple_id: DTS10001566
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2001-04-11'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1010.html
archived_at: '2026-07-18T02:38:01.601003Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/GraphicsImaging/index.html) > [Quartz](https://developer.apple.com/library/archive/technicalqas/GraphicsImaging/idxQuartz-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > Quartz](https://developer.apple.com/referencelibrary/GraphicsImaging/idxQuartz-date.html)

|  |
| --- |
| Technical Q&A QA1010SyncCGContextOriginWithPort |

|  |  |  |
| --- | --- | --- |
| ---   Q: What is `SyncCGContextOriginWithPort` and why do I need it?  A: The Core Graphics coordinate space is defined differently than that of QuickDraw. In QuickDraw, the origin is at the upper left of the `CGrafPort` and the positive y-axis points down. Core Graphics, on the other hand, defines the origin to be the bottom left corner of the `CGContext` and the positive y-axis points up.  `SyncCGContextOriginWithPort` is a convenience function that moves the `CGContext` origin from the bottom left to adjust for any calls to `SetOrigin` for the port.     |  | | --- | | ``` //  Create the CGContext from a given QD port CGContextRef context; Rect portRect; OSStatus err = CreateCGContextForPort( qdPort, &context ); if ( noErr == err ) {     //  Adjust for any SetOrigin calls on qdPort     SyncCGContextOriginWithPort( context, qdPort );      //  Move the CG origin to the upper left of the port     GetPortBounds( qdPort, &portRect );     CGContextTranslateCTM( context, 0, (float)(portRect.bottom - portRect.top) );      //  Flip the y axis so that positive Y points down     //    Note that this will cause text drawn with Core Graphics     //  to draw upside down     CGContextScaleCTM( context, 1.0, -1.0 );      //  The CG coordinate space now matches the QD coordinate space     //  ...     //  Do your CG drawing here     //  ...      //  Release the context now that we are done with it     CGContextRelease( context ); } //  Back to normal QuickDraw drawing ``` | | __Listing 1__. Setting up the Core Graphics Context |     Note that `SyncCGContextOriginWithPort` does not flip the y-axis for you or move the origin from the bottom left to the upper left. Therefore you either need to account for the difference in your drawing code or call the code in Listing 1 to move the origin and flip the y-axis for all subsequent Core Graphics drawing operations on that context.   ---  [Apr 11 2001] |

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
