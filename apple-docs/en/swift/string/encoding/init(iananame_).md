---
title: 'init(ianaName:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/encoding/init(iananame:)'
source_url: 'https://developer.apple.com/documentation/swift/string/encoding/init(iananame:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/encoding/init%28iananame%3A%29.json'
content_hash: 'sha256:895a21f2aed52b45'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [Encoding](../encoding.md)

# init(ianaName:)

<sub>Initializer</sub>

Creates an instance from the name of the IANA registry “charset”.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(ianaName charsetName: String)
```

## Discussion

> [!note] Note
> The given name is compared to each IANA “charset” name with ASCII case-insensitive collation to determine which encoding is suitable.
