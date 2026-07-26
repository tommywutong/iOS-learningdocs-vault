---
title: AttributeScopes.FoundationAttributes.ReplacementIndexAttribute
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/foundationattributes/replacementindexattribute
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/replacementindexattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/foundationattributes/replacementindexattribute.json'
content_hash: 'sha256:a502863818555423'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [FoundationAttributes](../foundationattributes.md)

# AttributeScopes.FoundationAttributes.ReplacementIndexAttribute

<sub>Enumeration</sub>

A type for using a replacement index as an attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum ReplacementIndexAttribute
```

## Overview

When you use the [applyReplacementIndexAttribute](../../attributedstring/formattingoptions/applyreplacementindexattribute.md) formatting option, the resulting formatted string uses this attribute to mark the location of replacement strings. This allows you to relate ranges to replacements even if localizers change the word order in format strings.

## Relationships

- **Conforms To**: [AttributedStringKey](../../attributedstringkey.md), [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Copyable](../../../swift/copyable.md), [DecodableAttributedStringKey](../../decodableattributedstringkey.md), [EncodableAttributedStringKey](../../encodableattributedstringkey.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## See Also

### Using string formatting attributes

- [replacementIndex](replacementindex.md) — A property for accessing a replacement index attribute.
