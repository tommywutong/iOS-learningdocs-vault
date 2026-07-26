---
title: AttributedString.FormattingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/formattingoptions
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/formattingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/formattingoptions.json'
content_hash: 'sha256:67d880bde35c3c66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# AttributedString.FormattingOptions

<sub>Structure</sub>

Options that affect the handling of attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FormattingOptions
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating Formatting Options

- [init()](<init().md>) — Creates an empty attributed string.
- [init(_:)](<init(__)-1fru0.md>) — Creates a value-type attributed string from a reference type.
- [init(_:)](<init(__)-8tnoq.md>) — Creates an attributed string from an attributed substring.

### Using Defined Formatting Options

- [applyReplacementIndexAttribute](formattingoptions/applyreplacementindexattribute.md) — An option to add an attribute that marks replacements in localized strings.

## See Also

### Creating a Localized Attributed String

- [init(localized:options:table:bundle:locale:comment:)](<init(localized_options_table_bundle_locale_comment_)-8dlnl.md>) — Creates an attributed string by looking up a localized string from the app’s bundle.
- [init(localized:options:table:bundle:locale:comment:including:)](<init(localized_options_table_bundle_locale_comment_including_)-8uknv.md>) — Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope.
- [init(localized:options:table:bundle:locale:comment:including:)](<init(localized_options_table_bundle_locale_comment_including_)-5jzpg.md>) — Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope that a key path identifies.
- [String.LocalizationValue](../../swift/string/localizationvalue.md) — A reference to a localizable string, with optional string interpolation.
- [init(localized:)](<init(localized_).md>) — Creates a localized attributed string from a localized string resource.
- [init(localized:including:)](<init(localized_including_)-2xebo.md>) — Creates a localized attributed string from a localized string resource, including an attribute scope.
- [init(localized:including:)](<init(localized_including_)-15xc5.md>) — Creates a localized attributed string from a localized string resource, including an attribute scope that a key path identifies.
- [LocalizedStringResource](../localizedstringresource.md) — A reference to a localizable string, accessible from another process.
