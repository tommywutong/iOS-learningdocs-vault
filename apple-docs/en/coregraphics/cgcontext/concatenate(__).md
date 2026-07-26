---
title: 'concatenate(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/concatenate(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/concatenate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/concatenate%28_%3A%29.json'
content_hash: 'sha256:0a5af0d587518d48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# concatenate(_:)

<sub>Instance Method</sub>

Transforms the user coordinate system in a context using a specified matrix.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func concatenate(_ transform: CGAffineTransform)
```

## Parameters

- `transform` — The transformation matrix to apply to the specified context’s current transformation matrix.

## Discussion

When you call this function, it concatenates (that is, it combines) two matrices, by multiplying them together. The order in which matrices are concatenated is important, as the operations are not commutative. The resulting CTM in the context is:   `CTMnew = transform * CTMcontext.`

## See Also

### Working with the Current Transformation Matrix

- [CGContextGetCTM](ctm.md) — Returns the current transformation matrix.
- [CGContextRotateCTM](<rotate(by_).md>) — Rotates the user coordinate system in a context.
- [CGContextScaleCTM](<scaleby(x_y_).md>) — Changes the scale of the user coordinate system in a context.
- [CGContextTranslateCTM](<translateby(x_y_).md>) — Changes the origin of the user coordinate system in a context.
