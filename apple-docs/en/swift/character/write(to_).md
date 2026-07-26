---
title: 'write(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/character/write(to:)'
source_url: 'https://developer.apple.com/documentation/swift/character/write(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/write%28to%3A%29.json'
content_hash: 'sha256:7b7ddec19d15ed1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# write(to:)

<sub>Instance Method</sub>

Writes the character into the given output stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write<Target>(to target: inout Target) where Target : TextOutputStream
```

## Parameters

- `target` — An output stream.
