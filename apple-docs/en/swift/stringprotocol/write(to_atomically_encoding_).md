---
title: 'write(to:atomically:encoding:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/write(to:atomically:encoding:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/write(to:atomically:encoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/write%28to%3Aatomically%3Aencoding%3A%29.json'
content_hash: 'sha256:69a281115fafa93f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# write(to:atomically:encoding:)

<sub>Instance Method</sub>

Writes the contents of the `String` to the URL specified by url using the specified encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(to url: URL, atomically useAuxiliaryFile: Bool, encoding enc: String.Encoding) throws
```
