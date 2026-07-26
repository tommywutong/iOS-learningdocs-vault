---
title: applyReplacementIndexAttribute
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/formattingoptions/applyreplacementindexattribute
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/formattingoptions/applyreplacementindexattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/formattingoptions/applyreplacementindexattribute.json'
content_hash: 'sha256:ba99e1515567812e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [FormattingOptions](../formattingoptions.md)

# applyReplacementIndexAttribute

<sub>Type Property</sub>

An option to add an attribute that marks replacements in localized strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let applyReplacementIndexAttribute: AttributedString.FormattingOptions
```

## Discussion

When you use this option, string formatting applies the [NSReplacementIndexAttributeName](../../nsattributedstring/key/replacementindex.md) key to the final range of each replacement. Its value is an `Int`, wrapping the integer ordinal of that particular replacement, such as the `2` in `%2$@`. This allows the developer to relate ranges to replacements even if a localizer modifies the word order.
