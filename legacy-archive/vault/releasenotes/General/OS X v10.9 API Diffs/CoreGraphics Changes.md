---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/CoreGraphics.html
archived_at: '2026-07-18T02:54:11.346084Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# CoreGraphics Changes

## CoreGraphics

CGContext.hModified [CGContextSelectFont()](https://developer.apple.com/documentation/coregraphics/cgcontext/1586511-selectfont)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CGContextShowGlyphs()](https://developer.apple.com/documentation/coregraphics/1586500-cgcontextshowglyphs)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CGContextShowGlyphsAtPoint()](https://developer.apple.com/documentation/coregraphics/cgcontext/1586502-showglyphsatpoint)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CGContextShowGlyphsWithAdvances()](https://developer.apple.com/documentation/coregraphics/1586503-cgcontextshowglyphswithadvances)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | void CGContextShowGlyphsWithAdvances ( CGContextRef c, const CGGlyph glyphs[], const CGSize advances[], size_t count); |
| To | OS X 10.9 | void CGContextShowGlyphsWithAdvances ( CGContextRef context, const CGGlyph glyphs[], const CGSize advances[], size_t count); |

Modified [CGContextShowText()](https://developer.apple.com/documentation/coregraphics/cgcontext/1586507-showtext)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CGContextShowTextAtPoint()](https://developer.apple.com/documentation/coregraphics/1586505-cgcontextshowtextatpoint)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CGTextEncoding](https://developer.apple.com/documentation/coregraphics/cgtextencoding)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

CGDirectDisplay.hRemoved CGBeamPositionRemoved CGByteValueRemoved CGDirectPaletteRefRemoved CGDisplayBeamPosition()Removed CGDisplayBestModeForParametersAndRefreshRateWithProperty()Removed CGDisplayCanSetPalette()Removed CGDisplayCoordRemoved CGDisplaySetPalette()Removed CGDisplayWaitForBeamPositionOutsideLines()Removed CGMouseDeltaRemoved CGTableCountModified [CGDisplayIsCaptured()](https://developer.apple.com/documentation/coregraphics/1562061-cgdisplayiscaptured)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

CGDirectPalette.hRemoved CGDeviceByteColorRemoved CGPaletteBlendFractionRemoved CGPaletteCreateCopy()Removed CGPaletteCreateDefaultColorPalette()Removed CGPaletteCreateFromPaletteBlendedWithColor()Removed CGPaletteCreateWithByteSamples()Removed CGPaletteCreateWithCapacity()Removed CGPaletteCreateWithDisplay()Removed CGPaletteCreateWithSamples()Removed CGPaletteGetColorAtIndex()Removed CGPaletteGetIndexForColor()Removed CGPaletteGetNumberOfSamples()Removed CGPaletteIsEqualToPalette()Removed CGPaletteRelease()Removed CGPaletteSetColorAtIndex()CGDisplayConfiguration.hModified [CGDisplayIOServicePort()](https://developer.apple.com/documentation/coregraphics/1543516-cgdisplayioserviceport)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

CGDisplayFade.hModified [CGDisplayFadeOperationInProgress()](https://developer.apple.com/documentation/coregraphics/1571962-cgdisplayfadeoperationinprogress)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

CGEventTypes.hAdded [CGGesturePhase](https://developer.apple.com/documentation/coregraphics/cggesturephase)Added [CGMomentumScrollPhase](https://developer.apple.com/documentation/coregraphics/cgmomentumscrollphase)Added [CGScrollPhase](https://developer.apple.com/documentation/coregraphics/cgscrollphase)Added [kCGGesturePhaseBegan](https://developer.apple.com/documentation/coregraphics/cggesturephase/kcggesturephasebegan)Added [kCGGesturePhaseCancelled](https://developer.apple.com/documentation/coregraphics/cggesturephase/cancelled)Added [kCGGesturePhaseChanged](https://developer.apple.com/documentation/coregraphics/cggesturephase/changed)Added [kCGGesturePhaseEnded](https://developer.apple.com/documentation/coregraphics/cggesturephase/kcggesturephaseended)Added [kCGGesturePhaseMayBegin](https://developer.apple.com/documentation/coregraphics/cggesturephase/maybegin)Added [kCGGesturePhaseNone](https://developer.apple.com/documentation/coregraphics/cggesturephase/kcggesturephasenone)Added [kCGMomentumScrollPhaseBegin](https://developer.apple.com/documentation/coregraphics/cgmomentumscrollphase/begin)Added [kCGMomentumScrollPhaseContinue](https://developer.apple.com/documentation/coregraphics/cgmomentumscrollphase/continuous)Added [kCGMomentumScrollPhaseEnd](https://developer.apple.com/documentation/coregraphics/cgmomentumscrollphase/end)Added [kCGMomentumScrollPhaseNone](https://developer.apple.com/documentation/coregraphics/cgmomentumscrollphase/none)Added [kCGScrollPhaseBegan](https://developer.apple.com/documentation/coregraphics/cgscrollphase/kcgscrollphasebegan)Added [kCGScrollPhaseCancelled](https://developer.apple.com/documentation/coregraphics/cgscrollphase/kcgscrollphasecancelled)Added [kCGScrollPhaseChanged](https://developer.apple.com/documentation/coregraphics/cgscrollphase/changed)Added [kCGScrollPhaseEnded](https://developer.apple.com/documentation/coregraphics/cgscrollphase/kcgscrollphaseended)Added [kCGScrollPhaseMayBegin](https://developer.apple.com/documentation/coregraphics/cgscrollphase/kcgscrollphasemaybegin)Added [kCGScrollWheelEventMomentumPhase](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgscrollwheeleventmomentumphase)CGFont.hModified [CGGlyphMax](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum/max)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CGGlyphMin](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum/min)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

CGGeometry.hAdded #def CGVECTOR_DEFINEDAdded [CGVector](https://developer.apple.com/documentation/coregraphics/cgvector)Added [CGVectorMake()](https://developer.apple.com/documentation/coregraphics/1454811-cgvectormake)CGPath.hAdded [CGPathAddRoundedRect()](https://developer.apple.com/documentation/coregraphics/1411124-cgpathaddroundedrect)Added [CGPathCreateWithRoundedRect()](https://developer.apple.com/documentation/coregraphics/cgpath/1411218-init)CGRemoteOperation.hModified [CGCursorIsDrawnInFramebuffer()](https://developer.apple.com/documentation/coregraphics/1541804-cgcursorisdrawninframebuffer)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CGCursorIsVisible()](https://developer.apple.com/documentation/coregraphics/1541812-cgcursorisvisible)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

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
