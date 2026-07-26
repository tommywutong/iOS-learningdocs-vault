---
title: mutableCopy()
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpath/mutablecopy()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/mutablecopy()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/mutablecopy%28%29.json'
content_hash: 'sha256:51d14c6933261d15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# mutableCopy()

<sub>Instance Method</sub>

Creates a mutable copy of an existing graphics path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mutableCopy() -> CGMutablePath?
```

## Return Value

A new, mutable, copy of the specified path. You are responsible for releasing this object.

## Discussion

You can modify a mutable graphics path by calling the various path geometry functions, such as [CGPathAddArc](../cgpathaddarc.md), [CGPathAddLineToPoint](../cgpathaddlinetopoint.md), and [CGPathMoveToPoint](../cgpathmovetopoint.md).

## See Also

### Copying a Graphics Path

- [CGPathCreateMutableCopyByTransformingPath](<mutablecopy(using_).md>) — Creates a mutable copy of a graphics path transformed by a transformation matrix.
