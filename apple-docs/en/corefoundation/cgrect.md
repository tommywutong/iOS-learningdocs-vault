---
title: CGRect
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cgrect
source_url: 'https://developer.apple.com/documentation/corefoundation/cgrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cgrect.json'
content_hash: 'sha256:50f0dd59639ba04a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CGRect

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CGRect
```

## Relationships

- **Conforms To**: [Animatable](../swiftui/animatable.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init()](<cgrect/init().md>)
- [init(dictionaryRepresentation:)](<cgrect/init(dictionaryrepresentation_).md>)
- [init(origin:size:)](<cgrect/init(origin_size_).md>)
- [init(x:y:width:height:)](<cgrect/init(x_y_width_height_)-27bxn.md>)
- [init(x:y:width:height:)](<cgrect/init(x_y_width_height_)-3kjh6.md>)
- [init(x:y:width:height:)](<cgrect/init(x_y_width_height_)-3xq19.md>)

### Instance Properties

- [customPlaygroundQuickLook](cgrect/customplaygroundquicklook.md) — A custom playground Quick Look for this instance. _(deprecated)_
- [dictionaryRepresentation](cgrect/dictionaryrepresentation.md)
- [formattedDescription](cgrect/formatteddescription.md)
- [height](cgrect/height.md)
- [integral](cgrect/integral.md)
- [isEmpty](cgrect/isempty.md)
- [isInfinite](cgrect/isinfinite.md)
- [isNull](cgrect/isnull.md)
- [maxX](cgrect/maxx.md)
- [maxY](cgrect/maxy.md)
- [midX](cgrect/midx.md)
- [midY](cgrect/midy.md)
- [minX](cgrect/minx.md)
- [minY](cgrect/miny.md)
- [origin](cgrect/origin.md)
- [size](cgrect/size.md)
- [standardized](cgrect/standardized.md)
- [width](cgrect/width.md)

### Instance Methods

- [applying(_:)](<cgrect/applying(__).md>)
- [clip()](<cgrect/clip().md>) — Modifies the current graphics context clipping path by intersecting it with this rect. This permanently modifies the graphics state, so the current state should be saved beforehand and restored afterwards.
- [contains(_:)](<cgrect/contains(__)-6n2uh.md>)
- [contains(_:)](<cgrect/contains(__)-8fdse.md>)
- [divided(atDistance:from:)](<cgrect/divided(atdistance_from_).md>)
- [equalTo(_:)](<cgrect/equalto(__).md>)
- [fill(using:)](<cgrect/fill(using_).md>) — Fills this rect in the current NSGraphicsContext in the context’s fill color. The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFill()`.
- [frame(withWidth:using:)](<cgrect/frame(withwidth_using_).md>) — Draws a frame around the inside of this rect in the current NSGraphicsContext in the context’s fill color The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSFrameRect()`.
- [inset(by:)](<cgrect/inset(by_).md>)
- [insetBy(dx:dy:)](<cgrect/insetby(dx_dy_).md>)
- [intersection(_:)](<cgrect/intersection(__).md>)
- [intersects(_:)](<cgrect/intersects(__).md>)
- [offsetBy(dx:dy:)](<cgrect/offsetby(dx_dy_).md>)
- [union(_:)](<cgrect/union(__).md>)

### Type Properties

- [infinite](cgrect/infinite.md)
- [null](cgrect/null.md)
- [zero](cgrect/zero.md)

## See Also

### Structures

- [CGAffineTransform](cgaffinetransform.md)
- [CGAffineTransformComponents](cgaffinetransformcomponents.md)
- [CGFloat](cgfloat-swift.struct.md) — The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [CGPoint](cgpoint.md)
- [CGSize](cgsize.md) — A structure that contains width and height values.
- [CGVector](cgvector.md) — A structure that contains a two-dimensional vector.
