---
title: hashValue
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cgfloat-swift.struct/hashvalue
source_url: 'https://developer.apple.com/documentation/corefoundation/cgfloat-swift.struct/hashvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cgfloat-swift.struct/hashvalue.json'
content_hash: 'sha256:3427445adbded6e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CGFloat](../cgfloat-swift.struct.md)

# hashValue

<sub>Instance Property</sub>

The hash value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hashValue: Int { get }
```

## Discussion

**Axiom:** `x == y` implies `x.hashValue == y.hashValue`.

> [!note] Note
> The hash value is not guaranteed to be stable across different invocations of the same program.  Do not persist the hash value across program runs.
