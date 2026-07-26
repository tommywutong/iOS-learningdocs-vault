---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simdstorage/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/simdstorage/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simdstorage/subscript%28_%3A%29.json'
content_hash: 'sha256:9722ee71746b007e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMDStorage](../simdstorage.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(index: Int) -> Self.Scalar { get set }
```

## Parameters

- `index` — The index of the element to access. `index` must be in the range `0..<scalarCount`.

## Default Implementations

### SIMDStorage Implementations

- [subscript(_:)](<subscript(__)-11tl0.md>) — Extracts the scalars at specified indices to form a SIMD2.
- [subscript(_:)](<subscript(__)-4bxif.md>) — Extracts the scalars at specified indices to form a SIMD64.
- [subscript(_:)](<subscript(__)-4wdyq.md>) — Extracts the scalars at specified indices to form a SIMD4.
- [subscript(_:)](<subscript(__)-5dslw.md>) — Extracts the scalars at specified indices to form a SIMD8.
- [subscript(_:)](<subscript(__)-8lp1s.md>) — Extracts the scalars at specified indices to form a SIMD16.
- [subscript(_:)](<subscript(__)-9go95.md>) — Extracts the scalars at specified indices to form a SIMD32.
- [subscript(_:)](<subscript(__)-9ota9.md>) — Extracts the scalars at specified indices to form a SIMD3.
