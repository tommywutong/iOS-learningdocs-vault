---
title: 'appendingFormat(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/appendingformat(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/appendingformat(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/appendingformat%28_%3A_%3A%29.json'
content_hash: 'sha256:2eb9cdcaaab9516b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# appendingFormat(_:_:)

<sub>Instance Method</sub>

Returns a string created by appending a string constructed from a given format string and the following arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func appendingFormat<T>(_ format: T, _ arguments: any CVarArg...) -> String where T : StringProtocol
```
