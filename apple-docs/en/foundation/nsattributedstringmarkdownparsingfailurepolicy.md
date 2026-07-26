---
title: NSAttributedStringMarkdownParsingFailurePolicy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstringmarkdownparsingfailurepolicy
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownparsingfailurepolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstringmarkdownparsingfailurepolicy.json'
content_hash: 'sha256:85bf032694290570'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSAttributedStringMarkdownParsingFailurePolicy

<sub>Enumeration</sub>

A type that represents policies for handling parsing failures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
enum NSAttributedStringMarkdownParsingFailurePolicy : NSInteger;
```

## Topics

### Failure Policies

- [NSAttributedStringMarkdownParsingFailureReturnError](nsattributedstringmarkdownparsingfailurepolicy/nsattributedstringmarkdownparsingfailurereturnerror.md) — A policy to return an error from the initializer if parsing fails.
- [NSAttributedStringMarkdownParsingFailureReturnPartiallyParsedIfPossible](nsattributedstringmarkdownparsingfailurepolicy/nsattributedstringmarkdownparsingfailurereturnpartiallyparsedifpossible.md) — A policy to return a partially parsed string, if possible.

## See Also

### Determining Markdown Parsing Options

- [allowsExtendedAttributes](nsattributedstringmarkdownparsingoptions/allowsextendedattributes.md) — A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [appliesSourcePositionAttributes](nsattributedstringmarkdownparsingoptions/appliessourcepositionattributes.md) — A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](nsattributedstringmarkdownparsingoptions/failurepolicy.md) — The policy for handling a parsing failure.
- [interpretedSyntax](nsattributedstringmarkdownparsingoptions/interpretedsyntax.md) — The syntax for intepreting a Markdown string.
- [NSAttributedStringMarkdownInterpretedSyntax](nsattributedstringmarkdowninterpretedsyntax.md) — A type that represents the syntax for intepreting a Markdown string.
- [languageCode](nsattributedstringmarkdownparsingoptions/languagecode.md) — The BCP-47 language code for this document.
