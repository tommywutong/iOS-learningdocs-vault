---
title: 'encode(contentsOf:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyedencodingcontainer/encode(contentsof:)-9s06k'
source_url: 'https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encode(contentsof:)-9s06k'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyedencodingcontainer/encode%28contentsof%3A%29-9s06k.json'
content_hash: 'sha256:6fe8f9ad11a93991'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedEncodingContainer](../unkeyedencodingcontainer.md)

# encode(contentsOf:)

<sub>Instance Method</sub>

Encodes the elements of the given sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encode<T>(contentsOf sequence: T) throws where T : Sequence, T.Element == UInt16
```

## Parameters

- `sequence` — The sequences whose contents to encode.

## Discussion

> [!danger] Throws
> An error if any of the contained values throws an error.

## Default Implementations

### UnkeyedEncodingContainer Implementations

- [encode(contentsOf:)](<encode(contentsof_)-1k4wu.md>)
- [encode(contentsOf:)](<encode(contentsof_)-28q9o.md>)
- [encode(contentsOf:)](<encode(contentsof_)-2rt93.md>)
- [encode(contentsOf:)](<encode(contentsof_)-2yymi.md>)
- [encode(contentsOf:)](<encode(contentsof_)-4lzqs.md>)
- [encode(contentsOf:)](<encode(contentsof_)-59l2f.md>)
- [encode(contentsOf:)](<encode(contentsof_)-5zeys.md>)
- [encode(contentsOf:)](<encode(contentsof_)-6e9jx.md>)
- [encode(contentsOf:)](<encode(contentsof_)-7485u.md>)
- [encode(contentsOf:)](<encode(contentsof_)-74qqt.md>)
- [encode(contentsOf:)](<encode(contentsof_)-7pqnf.md>)
- [encode(contentsOf:)](<encode(contentsof_)-97v19.md>)
- [encode(contentsOf:)](<encode(contentsof_)-9cu3t.md>)
- [encode(contentsOf:)](<encode(contentsof_)-9dfsi.md>)
- [encode(contentsOf:)](<encode(contentsof_)-9lwpz.md>)
- [encode(contentsOf:)](<encode(contentsof_)-zmlx.md>)
- [encode(contentsOf:)](<encode(contentsof_)-zo1s.md>)
