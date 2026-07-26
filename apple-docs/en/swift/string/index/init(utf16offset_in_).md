---
title: 'init(utf16Offset:in:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/index/init(utf16offset:in:)'
source_url: 'https://developer.apple.com/documentation/swift/string/index/init(utf16offset:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/index/init%28utf16offset%3Ain%3A%29.json'
content_hash: 'sha256:0969911ffd01864f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [Index](../index.md)

# init(utf16Offset:in:)

<sub>Initializer</sub>

Creates a new index at the specified UTF-16 code unit offset

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(utf16Offset offset: Int, in s: S) where S : StringProtocol
```

## Parameters

- `offset` — An offset in UTF-16 code units.
