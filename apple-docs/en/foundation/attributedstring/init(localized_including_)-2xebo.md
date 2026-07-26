---
title: 'init(localized:including:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/init(localized:including:)-2xebo'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/init(localized:including:)-2xebo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/init%28localized%3Aincluding%3A%29-2xebo.json'
content_hash: 'sha256:875605dc1d5da417'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# init(localized:including:)

<sub>Initializer</sub>

Creates a localized attributed string from a localized string resource, including an attribute scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(localized resource: LocalizedStringResource, including scope: S.Type) where S : AttributeScope
```

## Parameters

- `resource` — A [LocalizedStringResource](../localizedstringresource.md) that provides the localization key, table, bundle, and locale.

- `scope` — An attribute scope to associate with the attributed string.

## Discussion

Call this initializer to look up the localization indicated by `resource`. Alter the resource’s [locale](../localizedstringresource/locale.md) prior to calling this method if you want to localize this string in a different locale than the process that created the [LocalizedStringResource](../localizedstringresource.md).

The attributed string contains attributes of type [LocalizedStringArgumentAttributes](../attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct.md) to indicate runs containing formatted text, such as localized numbers or dates. Access these attributes with the attribute key [localizedNumericArgument](../attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizednumericargument.md) or [localizedDateArgument](../attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizeddateargument.md).

## See Also

### Creating a Localized Attributed String

- [init(localized:options:table:bundle:locale:comment:)](<init(localized_options_table_bundle_locale_comment_)-8dlnl.md>) — Creates an attributed string by looking up a localized string from the app’s bundle.
- [init(localized:options:table:bundle:locale:comment:including:)](<init(localized_options_table_bundle_locale_comment_including_)-8uknv.md>) — Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope.
- [init(localized:options:table:bundle:locale:comment:including:)](<init(localized_options_table_bundle_locale_comment_including_)-5jzpg.md>) — Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope that a key path identifies.
- [String.LocalizationValue](../../swift/string/localizationvalue.md) — A reference to a localizable string, with optional string interpolation.
- [FormattingOptions](formattingoptions.md) — Options that affect the handling of attributes.
- [init(localized:)](<init(localized_).md>) — Creates a localized attributed string from a localized string resource.
- [init(localized:including:)](<init(localized_including_)-15xc5.md>) — Creates a localized attributed string from a localized string resource, including an attribute scope that a key path identifies.
- [LocalizedStringResource](../localizedstringresource.md) — A reference to a localizable string, accessible from another process.
