---
title: allowsExtendedAttributes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstringmarkdownparsingoptions/allowsextendedattributes
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownparsingoptions/allowsextendedattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstringmarkdownparsingoptions/allowsextendedattributes.json'
content_hash: 'sha256:dd45bdd511d7c585'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedStringMarkdownParsingOptions](../nsattributedstringmarkdownparsingoptions.md)

# allowsExtendedAttributes

<sub>Instance Property</sub>

A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property BOOL allowsExtendedAttributes;
```

## Discussion

If this value is `NO`, the Markdown parser supports only the CommonMark syntax. The default is `NO`.

## See Also

### Determining Markdown Parsing Options

- [appliesSourcePositionAttributes](appliessourcepositionattributes.md) — A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](failurepolicy.md) — The policy for handling a parsing failure.
- [NSAttributedStringMarkdownParsingFailurePolicy](../nsattributedstringmarkdownparsingfailurepolicy.md) — A type that represents policies for handling parsing failures.
- [interpretedSyntax](interpretedsyntax.md) — The syntax for intepreting a Markdown string.
- [NSAttributedStringMarkdownInterpretedSyntax](../nsattributedstringmarkdowninterpretedsyntax.md) — A type that represents the syntax for intepreting a Markdown string.
- [languageCode](languagecode.md) — The BCP-47 language code for this document.
