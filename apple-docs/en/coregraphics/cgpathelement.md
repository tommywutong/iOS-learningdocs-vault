---
title: CGPathElement
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpathelement
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpathelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpathelement.json'
content_hash: 'sha256:ce34f64d54497aad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPathElement

<sub>Structure</sub>

A data structure that provides information about a path element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CGPathElement
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init(type:points:)](<cgpathelement/init(type_points_).md>)

### Instance Properties

- [points](cgpathelement/points.md) — An array of one or more points that serve as arguments.
- [type](cgpathelement/type.md) — An element type (or operation).

## See Also

### Applying a Function to the Elements of a Path

- [CGPathApply](<cgpath/apply(info_function_).md>) — For each element in a graphics path, calls a custom applier function.
- [CGPathApplierFunction](cgpathapplierfunction.md) — Defines a callback function that can view an element in a graphics path.
- [CGPathElementType](cgpathelementtype.md) — The type of element found in a path.
