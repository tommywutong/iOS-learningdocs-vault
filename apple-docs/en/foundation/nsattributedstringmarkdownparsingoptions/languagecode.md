---
title: languageCode
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstringmarkdownparsingoptions/languagecode
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownparsingoptions/languagecode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstringmarkdownparsingoptions/languagecode.json'
content_hash: 'sha256:737c4c8343c74001'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedStringMarkdownParsingOptions](../nsattributedstringmarkdownparsingoptions.md)

# languageCode

<sub>Instance Property</sub>

The BCP-47 language code for this document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (copy, nullable) NSString * languageCode;
```

## Discussion

If not `nil`, the string applies the [languageIdentifier](../attributescopes/foundationattributes/languageidentifier.md) attribute to any range in the returned string that doesn’t otherwise specify a language attribute. The default is `nil`, which applies no attributes.

## See Also

### Determining Markdown Parsing Options

- [allowsExtendedAttributes](allowsextendedattributes.md) — A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [appliesSourcePositionAttributes](appliessourcepositionattributes.md) — A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](failurepolicy.md) — The policy for handling a parsing failure.
- [NSAttributedStringMarkdownParsingFailurePolicy](../nsattributedstringmarkdownparsingfailurepolicy.md) — A type that represents policies for handling parsing failures.
- [interpretedSyntax](interpretedsyntax.md) — The syntax for intepreting a Markdown string.
- [NSAttributedStringMarkdownInterpretedSyntax](../nsattributedstringmarkdowninterpretedsyntax.md) — A type that represents the syntax for intepreting a Markdown string.
