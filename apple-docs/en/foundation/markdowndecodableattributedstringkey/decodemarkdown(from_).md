---
title: 'decodeMarkdown(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/markdowndecodableattributedstringkey/decodemarkdown(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/markdowndecodableattributedstringkey/decodemarkdown(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/markdowndecodableattributedstringkey/decodemarkdown%28from%3A%29.json'
content_hash: 'sha256:62a9e001068f610a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MarkdownDecodableAttributedStringKey](../markdowndecodableattributedstringkey.md)

# decodeMarkdown(from:)

<sub>Type Method</sub>

Decodes a value from the provided decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func decodeMarkdown(from decoder: any Decoder) throws -> Self.Value
```

## Parameters

- `decoder` — The decoder to read data from.

## Return Value

The decoded value.

## Discussion

This method throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Default Implementations

### MarkdownDecodableAttributedStringKey Implementations

- [decodeMarkdown(from:)](<decodemarkdown(from_)-8vpq6.md>) — Decodes a value from the provided decoder, using a default implementation.
