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
doc_path: '/documentation/foundation/attributedstring/index/isvalid(within:)-8fw50'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/index/isvalid(within:)-8fw50'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/index/isvalid%28within%3A%29-8fw50.json'
content_hash: 'sha256:225f8e2e134f7cb9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [Index](../index.md)

# isValid(within:)

<sub>Instance Method</sub>

Indicates whether the index is valid for use with the provided attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isValid(within text: some AttributedStringProtocol) -> Bool
```

## Parameters

- `text` — An attributed string used to validate the index.

## Return Value

`true` when the index is valid for use with the provided attributed string; otherwise, false. An index is valid if it is both within the bounds of the attributed string and was produced from the provided string without any intermediate mutations.
