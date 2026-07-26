---
title: 'init(referencing:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/init(referencing:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/init(referencing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/init%28referencing%3A%29.json'
content_hash: 'sha256:3e067c7821239b64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# init(referencing:)

<sub>Initializer</sub>

Initialize a `Data` by adopting a reference type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(referencing reference: NSData)
```

## Parameters

- `reference` — The instance of `NSData` that you wish to wrap. This instance will be copied by `struct Data`.

## Discussion

You can use this initializer to create a `struct Data` that wraps a `class NSData`. `struct Data` will use the `class NSData` for all operations. Other initializers (including casting using `as Data`) may choose to hold a reference or not, based on a what is the most efficient representation.

If the resulting value is mutated, then `Data` will invoke the `mutableCopy()` function on the reference to copy the contents. You may customize the behavior of that function if you wish to return a specialized mutable subclass.
