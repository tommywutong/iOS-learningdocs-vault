---
title: 'encode(contentsOf:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyedencodingcontainer/encode(contentsof:)-9sogk'
source_url: 'https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encode(contentsof:)-9sogk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyedencodingcontainer/encode%28contentsof%3A%29-9sogk.json'
content_hash: 'sha256:f8b5cc3f3ef6bcd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedEncodingContainer](../unkeyedencodingcontainer.md)

# encode(contentsOf:)

<sub>Instance Method</sub>

Encodes the elements of the given sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encode<T>(contentsOf sequence: T) throws where T : Sequence, T.Element == UInt128
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
