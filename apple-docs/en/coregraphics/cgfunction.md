---
title: CGFunction
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfunction
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfunction.json'
content_hash: 'sha256:d951edaa0234a9eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGFunction

<sub>Class</sub>

A general facility for defining and using callback functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGFunction
```

## Overview

These functions can take an arbitrary number of floating-point input values and pass back an arbitrary number of floating-point output values.

Core Graphics uses function objects to implement shadings. [CGShading](cgshading.md) describes the parameters and semantics required for the callbacks used by function objects.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Function Objects

- [CGFunctionCreate](<cgfunction/init(info_domaindimension_domain_rangedimension_range_callbacks_).md>) — Creates a Core Graphics function.

### Callbacks

- [CGFunctionCallbacks](cgfunctioncallbacks.md) — A structure that contains callbacks needed by a `CGFunctionRef` object.
- [CGFunctionEvaluateCallback](cgfunctionevaluatecallback.md) — Performs custom operations on the supplied input data to produce output data.
- [CGFunctionReleaseInfoCallback](cgfunctionreleaseinfocallback.md) — Performs custom clean-up tasks when Core Graphics deallocates a `CGFunctionRef` object.

### Working with Core Foundation Types

- [CGFunctionGetTypeID](cgfunction/typeid.md) — Returns the type identifier for Core Graphics function objects.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)

### Utility and Support Classes

- [CGDataConsumer](cgdataconsumer.md) — An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [CGDataProvider](cgdataprovider.md) — An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [CGShading](cgshading.md) — A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [CGGradient](cggradient.md) — A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [CGPattern](cgpattern.md) — A 2D pattern to be used for drawing graphics paths.
