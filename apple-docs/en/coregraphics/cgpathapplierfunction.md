---
title: CGPathApplierFunction
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpathapplierfunction
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpathapplierfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpathapplierfunction.json'
content_hash: 'sha256:c8d4925c491d9ce7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPathApplierFunction

<sub>Type Alias</sub>

Defines a callback function that can view an element in a graphics path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGPathApplierFunction = (UnsafeMutableRawPointer?, UnsafePointer<CGPathElement>) -> Void
```

## Discussion

See also [CGPathApply](<cgpath/apply(info_function_).md>).

## See Also

### Applying a Function to the Elements of a Path

- [CGPathApply](<cgpath/apply(info_function_).md>) — For each element in a graphics path, calls a custom applier function.
- [CGPathElement](cgpathelement.md) — A data structure that provides information about a path element.
- [CGPathElementType](cgpathelementtype.md) — The type of element found in a path.
