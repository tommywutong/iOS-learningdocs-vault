---
title: NSStringDrawingContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsstringdrawingcontext
source_url: 'https://developer.apple.com/documentation/uikit/nsstringdrawingcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringdrawingcontext.json'
content_hash: 'sha256:6a7793f521170818'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSStringDrawingContext

<sub>Class</sub>

An object that manages metrics for drawing attributed strings.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class NSStringDrawingContext
```

## Overview

Prior to drawing, you can create an instance of this class and use it to specify the minimum scale factor and tracking adjustments for a string. After drawing, you can retrieve the actual values that were used during drawing.

To use this class, allocate and initialize a new instance, set the minimum values, and pass your object to one of the corresponding [NSAttributedString](../foundation/nsattributedstring.md) methods that take the context object as a parameter. Upon completion of drawing, you can use the actual drawing values to make adjustments or record where the string was actually drawn.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the scale factors

- [minimumScaleFactor](nsstringdrawingcontext/minimumscalefactor.md) — The scale factor that determines the smallest font size to use during drawing.
- [actualScaleFactor](nsstringdrawingcontext/actualscalefactor.md) — The actual scale factor that the system applied to the font during drawing.

### Getting the drawing bounds

- [totalBounds](nsstringdrawingcontext/totalbounds.md) — The most recent bounding rectangle that the system used to draw the string.

### Deprecated

- [minimumTrackingAdjustment](nsstringdrawingcontext/minimumtrackingadjustment.md) — The smallest amount of space, in points, to maintain between characters. _(deprecated)_
- [actualTrackingAdjustment](nsstringdrawingcontext/actualtrackingadjustment.md) — The actual tracking value that the system applied during drawing. _(deprecated)_

## See Also

### Strings

- [NSStringDrawingOptions](nsstringdrawingoptions.md) — Constants that specify the rendering options for drawing a string.
- [UIBaselineAdjustment](uibaselineadjustment.md) — Vertical adjustment options.
