---
title: 'withUnsafeMutableBytes(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/withunsafemutablebytes(_:)-79c12'
source_url: 'https://developer.apple.com/documentation/foundation/data/withunsafemutablebytes(_:)-79c12'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/withunsafemutablebytes%28_%3A%29-79c12.json'
content_hash: 'sha256:2c98a0f0ebaa9e91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# withUnsafeMutableBytes(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func withUnsafeMutableBytes<E, ResultType>(_ body: (UnsafeMutableRawBufferPointer) throws(E) -> ResultType) throws(E) -> ResultType where E : Error, ResultType : ~Copyable
```
