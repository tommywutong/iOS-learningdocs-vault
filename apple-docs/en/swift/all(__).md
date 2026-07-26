---
title: 'all(_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/all(_:)'
source_url: 'https://developer.apple.com/documentation/swift/all(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/all%28_%3A%29.json'
content_hash: 'sha256:02e1bf3d5866431a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# all(_:)

<sub>Function</sub>

True if every lane of mask is true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func all<Storage>(_ mask: SIMDMask<Storage>) -> Bool where Storage : SIMD, Storage.Scalar : FixedWidthInteger, Storage.Scalar : SignedInteger
```

## See Also

### Supporting Functions

- [any(_:)](<any(__).md>) — True if any lane of mask is true.
- [pointwiseMax(_:_:)](<pointwisemax(____)-29hn2.md>) — The lanewise maximum of two vectors.
- [pointwiseMax(_:_:)](<pointwisemax(____)-2k6er.md>) — The lanewise maximum of two vectors.
- [pointwiseMin(_:_:)](<pointwisemin(____)-39txi.md>) — The lanewise minimum of two vectors.
- [pointwiseMin(_:_:)](<pointwisemin(____)-8v95p.md>) — The lanewise minimum of two vectors.
