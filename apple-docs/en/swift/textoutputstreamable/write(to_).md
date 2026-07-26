---
title: 'write(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/textoutputstreamable/write(to:)'
source_url: 'https://developer.apple.com/documentation/swift/textoutputstreamable/write(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/textoutputstreamable/write%28to%3A%29.json'
content_hash: 'sha256:ac367399b96f2808'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TextOutputStreamable](../textoutputstreamable.md)

# write(to:)

<sub>Instance Method</sub>

Writes a textual representation of this instance into the given output stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write<Target>(to target: inout Target) where Target : TextOutputStream
```
