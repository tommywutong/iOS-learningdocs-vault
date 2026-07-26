---
title: 'withBytes(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/foundation/contiguousbytes/withbytes(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/contiguousbytes/withbytes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/contiguousbytes/withbytes%28_%3A%29.json'
content_hash: 'sha256:b5d5568db32d53c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ContiguousBytes](../contiguousbytes.md)

# withBytes(_:)

<sub>Instance Method</sub>

Calls the given closure with the contents of underlying storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withBytes<R, E>(_ body: (RawSpan) throws(E) -> R) throws(E) -> R where E : Error
```

## Discussion

> [!note] Note
> Calling `withBytes` multiple times does not guarantee that the same span will be passed in every time.

## Default Implementations

### ContiguousBytes Implementations

- [withBytes(_:)](<withbytes(__)-5qdgz.md>) — Calls the given closure with the contents of underlying storage.
