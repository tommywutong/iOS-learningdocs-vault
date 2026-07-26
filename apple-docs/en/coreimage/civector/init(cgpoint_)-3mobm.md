---
title: 'init(cgPoint:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/civector/init(cgpoint:)-3mobm'
source_url: 'https://developer.apple.com/documentation/coreimage/civector/init(cgpoint:)-3mobm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector/init%28cgpoint%3A%29-3mobm.json'
content_hash: 'sha256:0647f23c33824a17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIVector](../civector.md)

# init(cgPoint:)

<sub>Initializer</sub>

Create a Core Image vector object that is initialized with two values provided by a `CGPoint` structure.

<sub>visionOS</sub>

```swift
convenience init(cgPoint p: CGPoint)
```

## Parameters

- `p` — The `CGPoint` structure.

## Return Value

An autoreleased [CIVector](../civector.md) object of length 2.

## Discussion

The `CGRect` structure’s `y` and `y` values are stored in the vector’s two values.

## See Also

### Creating a Vector

- [+ vectorWithCGAffineTransform:](<init(cgaffinetransform_)-59e4k.md>) — Create a Core Image vector object that is initialized with six values provided by a `CGAffineTransform` structure.
- [+ vectorWithCGRect:](<init(cgrect_)-3undj.md>) — Create a Core Image vector object that is initialized with four values provided by a `CGRect` structure.
