---
title: CGSize
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cgsize
source_url: 'https://developer.apple.com/documentation/corefoundation/cgsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cgsize.json'
content_hash: 'sha256:955a17979bd599fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CGSize

<sub>Structure</sub>

A structure that contains width and height values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CGSize
```

## Overview

A [CGSize](cgsize.md) structure is sometimes used to represent a distance vector, rather than a physical size. As a vector, its values can be negative. To normalize a [CGRect](cgrect.md) structure so that its size is represented by positive values, call the [standardized](cgrect/standardized.md) function.

## Relationships

- **Conforms To**: [Animatable](../swiftui/animatable.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Geometric Properties

- [width](cgsize/width.md) — A width value.
- [height](cgsize/height.md) — A height value.

### Special Values

- [zero](cgsize/zero.md)
- [init()](<cgsize/init().md>) — Creates a size with zero width and height.

### Transforming Sizes

- [applying(_:)](<cgsize/applying(__).md>)

### Alternate Representations

- [dictionaryRepresentation](cgsize/dictionaryrepresentation.md)
- [init(dictionaryRepresentation:)](<cgsize/init(dictionaryrepresentation_).md>)
- [customPlaygroundQuickLook](cgsize/customplaygroundquicklook.md) — A custom playground Quick Look for this instance. _(deprecated)_

### Comparing Sizes

- [CGSizeEqualToSize(_:_:)](<../coregraphics/cgsizeequaltosize(____).md>) — Returns whether two sizes are equal.

### Initializers

- [init(_:)](<cgsize/init(__).md>) — Convert `CVImageSize` to [CGSize](cgsize.md)
- [init(width:height:)](<cgsize/init(width_height_)-2du3k.md>)
- [init(width:height:)](<cgsize/init(width_height_)-63ffm.md>)
- [init(width:height:)](<cgsize/init(width_height_)-83b96.md>)

### Instance Properties

- [formattedDescription](cgsize/formatteddescription.md)

### Instance Methods

- [equalTo(_:)](<cgsize/equalto(__).md>)

## See Also

### Structures

- [CGAffineTransform](cgaffinetransform.md)
- [CGAffineTransformComponents](cgaffinetransformcomponents.md)
- [CGFloat](cgfloat-swift.struct.md) — The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [CGPoint](cgpoint.md)
- [CGRect](cgrect.md)
- [CGVector](cgvector.md) — A structure that contains a two-dimensional vector.
