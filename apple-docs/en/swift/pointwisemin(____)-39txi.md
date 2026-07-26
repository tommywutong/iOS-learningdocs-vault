---
title: 'pointwiseMin(_:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/pointwisemin(_:_:)-39txi'
source_url: 'https://developer.apple.com/documentation/swift/pointwisemin(_:_:)-39txi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/pointwisemin%28_%3A_%3A%29-39txi.json'
content_hash: 'sha256:c47e65065c34176b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# pointwiseMin(_:_:)

<sub>Function</sub>

The lanewise minimum of two vectors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func pointwiseMin<T>(_ a: T, _ b: T) -> T where T : SIMD, T.Scalar : FloatingPoint
```

## Discussion

Each element of the result is the minimum of the corresponding elements of the inputs.

## See Also

### Supporting Functions

- [all(_:)](<all(__).md>) — True if every lane of mask is true.
- [any(_:)](<any(__).md>) — True if any lane of mask is true.
- [pointwiseMax(_:_:)](<pointwisemax(____)-29hn2.md>) — The lanewise maximum of two vectors.
- [pointwiseMax(_:_:)](<pointwisemax(____)-2k6er.md>) — The lanewise maximum of two vectors.
- [pointwiseMin(_:_:)](<pointwisemin(____)-8v95p.md>) — The lanewise minimum of two vectors.
