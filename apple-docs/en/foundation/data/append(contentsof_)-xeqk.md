---
title: 'append(contentsOf:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/append(contentsof:)-xeqk'
source_url: 'https://developer.apple.com/documentation/foundation/data/append(contentsof:)-xeqk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/append%28contentsof%3A%29-xeqk.json'
content_hash: 'sha256:67fafe73fa72db73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# append(contentsOf:)

<sub>Instance Method</sub>

Appends the bytes in the specified sequence to the end of the data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(contentsOf elements: some ContiguousBytes & Sequence<UInt8>)
```
