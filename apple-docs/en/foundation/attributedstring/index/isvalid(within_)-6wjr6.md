---
title: 'isValid(within:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/index/isvalid(within:)-6wjr6'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/index/isvalid(within:)-6wjr6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/index/isvalid%28within%3A%29-6wjr6.json'
content_hash: 'sha256:75a2cca0399a30a3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [Index](../index.md)

# isValid(within:)

<sub>Instance Method</sub>

Indicates whether the index is valid for use with the provided discontiguous attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isValid(within text: DiscontiguousAttributedSubstring) -> Bool
```

## Parameters

- `text` — A discontiguous attributed string used to validate the index.

## Return Value

`true` when the index is valid for use with the provided discontiguous attributed string; otherwise, false. An index is valid if it is both within the bounds of the discontiguous attributed string and was produced from the provided string without any intermediate mutations.
