---
title: 'pointwiseMax(_:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/pointwisemax(_:_:)-2k6er'
source_url: 'https://developer.apple.com/documentation/swift/pointwisemax(_:_:)-2k6er'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/pointwisemax%28_%3A_%3A%29-2k6er.json'
content_hash: 'sha256:9b8b56e1f7082a0f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# pointwiseMax(_:_:)

<sub>Function</sub>

The lanewise maximum of two vectors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func pointwiseMax<T>(_ a: T, _ b: T) -> T where T : SIMD, T.Scalar : Comparable
```

## Discussion

Each element of the result is the minimum of the corresponding elements of the inputs.

## See Also

### Supporting Functions

- [all(_:)](<all(__).md>) — True if every lane of mask is true.
- [any(_:)](<any(__).md>) — True if any lane of mask is true.
- [pointwiseMax(_:_:)](<pointwisemax(____)-29hn2.md>) — The lanewise maximum of two vectors.
- [pointwiseMin(_:_:)](<pointwisemin(____)-39txi.md>) — The lanewise minimum of two vectors.
- [pointwiseMin(_:_:)](<pointwisemin(____)-8v95p.md>) — The lanewise minimum of two vectors.
