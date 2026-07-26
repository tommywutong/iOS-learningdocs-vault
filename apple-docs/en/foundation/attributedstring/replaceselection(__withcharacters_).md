---
title: 'replaceSelection(_:withCharacters:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/replaceselection(_:withcharacters:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/replaceselection(_:withcharacters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/replaceselection%28_%3Awithcharacters%3A%29.json'
content_hash: 'sha256:d7a7412e357ad353'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# replaceSelection(_:withCharacters:)

<sub>Instance Method</sub>

Replace the selection with new content, attributed with the typing attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replaceSelection(_ selection: inout AttributedTextSelection, withCharacters newContent: some Collection<Character>)
```

## Discussion

Operates just like [replaceSelection(_:with:)](<replaceselection(__with_).md>), but applies the typing attributes to the new content before inserting it.
