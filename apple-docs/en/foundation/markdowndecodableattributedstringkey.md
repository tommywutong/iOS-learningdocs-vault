---
title: MarkdownDecodableAttributedStringKey
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/markdowndecodableattributedstringkey
source_url: 'https://developer.apple.com/documentation/foundation/markdowndecodableattributedstringkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/markdowndecodableattributedstringkey.json'
content_hash: 'sha256:2719c4a8fa78b4b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# MarkdownDecodableAttributedStringKey

<sub>Protocol</sub>

A protocol that defines how an attribute key decodes a value that corresponds to Markdown syntax.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol MarkdownDecodableAttributedStringKey : AttributedStringKey
```

## Overview

This protocol is separate from [DecodableAttributedStringKey](decodableattributedstringkey.md) to separate explicit attributes defined by the SDK from Markdown’s semantic styling attributes. You use these attributes with Apple’s extended syntax for markdown: `^[text](attribute: value)`.

Using this protocol allows your markup names to differ from the names of your attributes. For example, the automatic grammar agreement feature uses markup like `^[text to inflect](inflect: true)`. This feature defines an [InflectionRuleAttribute](attributescopes/foundationattributes/inflectionruleattribute.md) that conforms to [MarkdownDecodableAttributedStringKey](markdowndecodableattributedstringkey.md). The value of its `AttributeScopes/FoundationAttributes/InflectionRuleAttribute/name` proprerty is `NSInflect`, while its `AttributeScopes/FoundationAttributes/InflectionRuleAttribute/markdownName-aom1`, used in actual Markdown strings like the one shown here, is `inflect`.

To define your own attributes for use with Markdown syntax, make sure your attributes conform to this protocol. The markdown parser ignores attributes that don’t conform, even if you use the extended Markdown syntax.

> [!tip] Tip
> When creating attributed strings from Markdown-based initializers like [init(markdown:options:baseURL:)](<attributedstring/init(markdown_options_baseurl_)-52n3u.md>), be sure to set the [allowsExtendedAttributes](attributedstring/markdownparsingoptions/allowsextendedattributes.md) option. If you don’t include this option, the string won’t parse [MarkdownDecodableAttributedStringKey](markdowndecodableattributedstringkey.md)-based attributes.

## Relationships

- **Inherits From**: [AttributedStringKey](attributedstringkey.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [AdjustedPitchAttribute](attributescopes/accessibilityattributes/adjustedpitchattribute.md), [AnnouncementPriorityAttribute](attributescopes/accessibilityattributes/announcementpriorityattribute.md), [HeadingLevelAttribute](attributescopes/accessibilityattributes/headinglevelattribute.md), [IPANotationAttribute](attributescopes/accessibilityattributes/ipanotationattribute.md), [IncludesPunctuationAttribute](attributescopes/accessibilityattributes/includespunctuationattribute.md), [QueueAnnouncementAttribute](attributescopes/accessibilityattributes/queueannouncementattribute.md), [SpellOutAttribute](attributescopes/accessibilityattributes/spelloutattribute.md), [TextCustomAttribute](attributescopes/accessibilityattributes/textcustomattribute.md), [TextualContextAttribute](attributescopes/accessibilityattributes/textualcontextattribute.md), [AgreementArgumentAttribute](attributescopes/foundationattributes/agreementargumentattribute.md), [AgreementConceptAttribute](attributescopes/foundationattributes/agreementconceptattribute.md), [InflectionAlternativeAttribute](attributescopes/foundationattributes/inflectionalternativeattribute.md), [InflectionRuleAttribute](attributescopes/foundationattributes/inflectionruleattribute.md), [LanguageIdentifierAttribute](attributescopes/foundationattributes/languageidentifierattribute.md), [LocalizedNumberFormatAttribute](attributescopes/foundationattributes/localizednumberformatattribute.md), [MorphologyAttribute](attributescopes/foundationattributes/morphologyattribute.md), [ReferentConceptAttribute](attributescopes/foundationattributes/referentconceptattribute.md)

## Topics

### Decoding Values

- [decodeMarkdown(from:)](<markdowndecodableattributedstringkey/decodemarkdown(from_).md>) — Decodes a value from the provided decoder.

### Accessing the Markdown Name

- [markdownName](markdowndecodableattributedstringkey/markdownname.md) — The Markdown name associated with an attributed string key.
