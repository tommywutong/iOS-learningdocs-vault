---
title: 'init(cgAffineTransform:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/civector/init(cgaffinetransform:)-59e4k'
source_url: 'https://developer.apple.com/documentation/coreimage/civector/init(cgaffinetransform:)-59e4k'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector/init%28cgaffinetransform%3A%29-59e4k.json'
content_hash: 'sha256:7276b272edd10164'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIVector](../civector.md)

# init(cgAffineTransform:)

<sub>Initializer</sub>

Create a Core Image vector object that is initialized with six values provided by a `CGAffineTransform` structure.

<sub>visionOS</sub>

```swift
convenience init(cgAffineTransform t: CGAffineTransform)
```

## Parameters

- `t` — The `CGAffineTransform` structure.

## Return Value

An autoreleased [CIVector](../civector.md) object of length 6.

## Discussion

The `CGAffineTransform` structure’s `a`, `b`, `c`, `d`, `tx` and `ty` values are stored in the vector’s six values.

## See Also

### Creating a Vector

- [+ vectorWithCGPoint:](<init(cgpoint_)-3mobm.md>) — Create a Core Image vector object that is initialized with two values provided by a `CGPoint` structure.
- [+ vectorWithCGRect:](<init(cgrect_)-3undj.md>) — Create a Core Image vector object that is initialized with four values provided by a `CGRect` structure.
