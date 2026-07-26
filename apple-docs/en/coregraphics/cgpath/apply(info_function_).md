---
title: 'apply(info:function:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpath/apply(info:function:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/apply(info:function:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/apply%28info%3Afunction%3A%29.json'
content_hash: 'sha256:f978a8a45fa02048'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# apply(info:function:)

<sub>Instance Method</sub>

For each element in a graphics path, calls a custom applier function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func apply(info: UnsafeMutableRawPointer?, function: CGPathApplierFunction)
```

## Parameters

- `info` — A pointer to the user data that Core Graphics will pass to the function being applied, or `NULL`.

- `function` — A pointer to the function to apply. See [CGPathApplierFunction](../cgpathapplierfunction.md) for more information.

## Discussion

For each element in the specified path, Core Graphics calls the applier function, which can examine (but not modify) the element.

## See Also

### Applying a Function to the Elements of a Path

- [CGPathApplierFunction](../cgpathapplierfunction.md) — Defines a callback function that can view an element in a graphics path.
- [CGPathElement](../cgpathelement.md) — A data structure that provides information about a path element.
- [CGPathElementType](../cgpathelementtype.md) — The type of element found in a path.
