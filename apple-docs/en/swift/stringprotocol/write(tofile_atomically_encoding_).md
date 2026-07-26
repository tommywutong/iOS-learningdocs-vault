---
title: 'write(toFile:atomically:encoding:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/write(tofile:atomically:encoding:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/write(tofile:atomically:encoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/write%28tofile%3Aatomically%3Aencoding%3A%29.json'
content_hash: 'sha256:6307ef857860a071'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# write(toFile:atomically:encoding:)

<sub>Instance Method</sub>

Writes the contents of the `String` to a file at a given path using a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write<T>(toFile path: T, atomically useAuxiliaryFile: Bool, encoding enc: String.Encoding) throws where T : StringProtocol
```
