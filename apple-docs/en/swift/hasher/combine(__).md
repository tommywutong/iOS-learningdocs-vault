---
title: 'combine(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/hasher/combine(_:)'
source_url: 'https://developer.apple.com/documentation/swift/hasher/combine(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/hasher/combine%28_%3A%29.json'
content_hash: 'sha256:737f93b830f1e592'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Hasher](../hasher.md)

# combine(_:)

<sub>Instance Method</sub>

Adds the given value to this hasher, mixing its essential parts into the hasher state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func combine<H>(_ value: borrowing H) where H : Hashable, H : ~Copyable, H : ~Escapable
```

## Parameters

- `value` — A value to add to the hasher.

## See Also

### Adding Values

- [combine(bytes:)](<combine(bytes_).md>) — Adds the contents of the given buffer to this hasher, mixing it into the hasher state.
