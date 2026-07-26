---
title: AttributeScopes.TranslationAttributes
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/translationattributes
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/translationattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/translationattributes.json'
content_hash: 'sha256:a5ae3aae22ab376e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeScopes](../attributescopes.md)

# AttributeScopes.TranslationAttributes

<sub>Structure</sub>

A scope that defines translation-specific properties on attributed strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TranslationAttributes
```

## Overview

Use this scope to access translation attributes when working with [AttributedString](../attributedstring.md) instances.

## Relationships

- **Conforms To**: [AttributeScope](../attributescope.md), [DecodingConfigurationProviding](../decodingconfigurationproviding.md), [EncodingConfigurationProviding](../encodingconfigurationproviding.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Handling translation behavior

- [skipsTranslation](translationattributes/skipstranslation.md) — An attribute that marks portions of an attributed string to be excluded from translation.
- [SkipTranslationAttribute](translationattributes/skiptranslationattribute.md) — The attribute key for skipping translation.

## See Also

### Translation-Defined Attributes

- [translation](translation.md) — Provides access to translation-related attributes.
