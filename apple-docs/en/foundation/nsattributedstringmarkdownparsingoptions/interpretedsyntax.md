---
title: interpretedSyntax
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstringmarkdownparsingoptions/interpretedsyntax
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownparsingoptions/interpretedsyntax'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstringmarkdownparsingoptions/interpretedsyntax.json'
content_hash: 'sha256:803af006c2308ea1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedStringMarkdownParsingOptions](../nsattributedstringmarkdownparsingoptions.md)

# interpretedSyntax

<sub>Instance Property</sub>

The syntax for intepreting a Markdown string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property NSAttributedStringMarkdownInterpretedSyntax interpretedSyntax;
```

## Discussion

If your Markdown data uses syntax that this setting excludes, the parser still parses it and includes its text in the final result. However, the relevant text won’t have attributes.

## See Also

### Determining Markdown Parsing Options

- [allowsExtendedAttributes](allowsextendedattributes.md) — A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [appliesSourcePositionAttributes](appliessourcepositionattributes.md) — A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](failurepolicy.md) — The policy for handling a parsing failure.
- [NSAttributedStringMarkdownParsingFailurePolicy](../nsattributedstringmarkdownparsingfailurepolicy.md) — A type that represents policies for handling parsing failures.
- [NSAttributedStringMarkdownInterpretedSyntax](../nsattributedstringmarkdowninterpretedsyntax.md) — A type that represents the syntax for intepreting a Markdown string.
- [languageCode](languagecode.md) — The BCP-47 language code for this document.
