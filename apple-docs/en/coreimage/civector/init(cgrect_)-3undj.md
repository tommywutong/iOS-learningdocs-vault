---
title: 'init(cgRect:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/civector/init(cgrect:)-3undj'
source_url: 'https://developer.apple.com/documentation/coreimage/civector/init(cgrect:)-3undj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector/init%28cgrect%3A%29-3undj.json'
content_hash: 'sha256:617b7930151c536e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIVector](../civector.md)

# init(cgRect:)

<sub>Initializer</sub>

Create a Core Image vector object that is initialized with four values provided by a `CGRect` structure.

<sub>visionOS</sub>

```swift
convenience init(cgRect r: CGRect)
```

## Parameters

- `r` — The `CGRect` structure.

## Return Value

An autoreleased [CIVector](../civector.md) object of length 4.

## Discussion

The `CGRect` structure’s `x`, `y`, `height` and `width` values are stored in the vector’s four values.

## See Also

### Creating a Vector

- [+ vectorWithCGAffineTransform:](<init(cgaffinetransform_)-59e4k.md>) — Create a Core Image vector object that is initialized with six values provided by a `CGAffineTransform` structure.
- [+ vectorWithCGPoint:](<init(cgpoint_)-3mobm.md>) — Create a Core Image vector object that is initialized with two values provided by a `CGPoint` structure.
