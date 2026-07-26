---
title: CGAffineTransform
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cgaffinetransform
source_url: 'https://developer.apple.com/documentation/corefoundation/cgaffinetransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cgaffinetransform.json'
content_hash: 'sha256:b13d726e671a2cad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CGAffineTransform

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CGAffineTransform
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init()](<cgaffinetransform/init().md>)
- [init(_:)](<cgaffinetransform/init(__).md>)
- [init(_:_:_:_:_:_:)](<cgaffinetransform/init(____________).md>)
- [init(a:b:c:d:tx:ty:)](<cgaffinetransform/init(a_b_c_d_tx_ty_).md>)
- [init(rotationAngle:)](<cgaffinetransform/init(rotationangle_).md>)
- [init(scaleX:y:)](<cgaffinetransform/init(scalex_y_).md>)
- [init(translationX:y:)](<cgaffinetransform/init(translationx_y_).md>)

### Instance Properties

- [a](cgaffinetransform/a.md)
- [b](cgaffinetransform/b.md)
- [c](cgaffinetransform/c.md)
- [d](cgaffinetransform/d.md)
- [isIdentity](cgaffinetransform/isidentity.md)
- [tx](cgaffinetransform/tx.md)
- [ty](cgaffinetransform/ty.md)

### Instance Methods

- [concatenating(_:)](<cgaffinetransform/concatenating(__).md>)
- [decomposed()](<cgaffinetransform/decomposed().md>)
- [inverted()](<cgaffinetransform/inverted().md>)
- [rotated(by:)](<cgaffinetransform/rotated(by_).md>)
- [scaledBy(x:y:)](<cgaffinetransform/scaledby(x_y_).md>)
- [translatedBy(x:y:)](<cgaffinetransform/translatedby(x_y_).md>)

### Type Properties

- [identity](cgaffinetransform/identity.md)

## See Also

### Structures

- [CGAffineTransformComponents](cgaffinetransformcomponents.md)
- [CGFloat](cgfloat-swift.struct.md) — The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [CGPoint](cgpoint.md)
- [CGRect](cgrect.md)
- [CGSize](cgsize.md) — A structure that contains width and height values.
- [CGVector](cgvector.md) — A structure that contains a two-dimensional vector.
