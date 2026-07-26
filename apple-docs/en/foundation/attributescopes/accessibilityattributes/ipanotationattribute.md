---
title: AttributeScopes.AccessibilityAttributes.IPANotationAttribute
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/accessibilityattributes/ipanotationattribute
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/ipanotationattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/accessibilityattributes/ipanotationattribute.json'
content_hash: 'sha256:6f31285c90359bbd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [AccessibilityAttributes](../accessibilityattributes.md)

# AttributeScopes.AccessibilityAttributes.IPANotationAttribute

<sub>Enumeration</sub>

An attribute to define the International Phonetic Alphabet representation for speech.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum IPANotationAttribute
```

## Overview

The IPA representation defines pronunciation of words that have the same spelling but different sounds.

For example, consider the different pronunciations of the word “live” in the following two sentences:

- “Anne wants to live on Main Street.”
- “Maria wants to go to the live concert.”

In the first sentence, “live” rhymes with “give.”  Its IPA representation would be “lɪv”. In the second sentence, it rhymes with “hive”. Its IPA representation would be “laɪv”.

> [!note] Note
> This attribute is not used on macOS

## Relationships

- **Conforms To**: [AttributedStringKey](../../attributedstringkey.md), [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Copyable](../../../swift/copyable.md), [DecodableAttributedStringKey](../../decodableattributedstringkey.md), [EncodableAttributedStringKey](../../encodableattributedstringkey.md), [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)
