---
title: AttributedString.MarkdownParsingOptions.FailurePolicy.returnPartiallyParsedIfPossible
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/markdownparsingoptions/failurepolicy-swift.enum/returnpartiallyparsedifpossible
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/failurepolicy-swift.enum/returnpartiallyparsedifpossible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/markdownparsingoptions/failurepolicy-swift.enum/returnpartiallyparsedifpossible.json'
content_hash: 'sha256:f4f273651b8b5d03'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [AttributedString](../../../attributedstring.md) · [MarkdownParsingOptions](../../markdownparsingoptions.md) · [FailurePolicy](../failurepolicy-swift.enum.md)

# AttributedString.MarkdownParsingOptions.FailurePolicy.returnPartiallyParsedIfPossible

<sub>Case</sub>

A policy to return a partially-parsed string, if possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case returnPartiallyParsedIfPossible
```

## Discussion

With this policy, the returned string may include unparsed markup. If returning a partially parsed string isn’t possible, the parser may throw an error anyway.

## See Also

### Declaring Failure Policies

- [AttributedString.MarkdownParsingOptions.FailurePolicy.throwError](throwerror.md) — A policy to throw an error from the initializer if parsing fails.
