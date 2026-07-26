---
title: 'asciiOnlyWordCharacters(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/asciionlywordcharacters(_:)'
source_url: 'https://developer.apple.com/documentation/swift/regex/asciionlywordcharacters(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/asciionlywordcharacters%28_%3A%29.json'
content_hash: 'sha256:a517debffbb6e3e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# asciiOnlyWordCharacters(_:)

<sub>Instance Method</sub>

Returns a regular expression that matches only ASCII characters as word characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func asciiOnlyWordCharacters(_ useASCII: Bool = true) -> Regex<Regex<Output>.RegexOutput>
```

## Parameters

- `useASCII` — A Boolean value indicating whether to match only ASCII characters as word characters.

## Return Value

The modified regular expression.
