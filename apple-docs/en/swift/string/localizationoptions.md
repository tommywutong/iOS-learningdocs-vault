---
title: String.LocalizationOptions
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/localizationoptions
source_url: 'https://developer.apple.com/documentation/swift/string/localizationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/localizationoptions.json'
content_hash: 'sha256:ef2caa7a5c543639'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# String.LocalizationOptions

<sub>Structure</sub>

Options to apply when initializing a localized string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct LocalizationOptions
```

## Overview

Use this type to configure how the system localizes strings. You can use the [replacements](localizationoptions/replacements.md) property to provide replacement values for localizable strings that use the `\(placeholder:)` syntax.

## Topics

### Specifying localization behavior

- [replacements](localizationoptions/replacements.md) — An array of replacement options.

### Initializers

- [init()](<localizationoptions/init().md>)

## See Also

### Creating a Localized String

- [init(localized:table:bundle:locale:comment:)](<init(localized_table_bundle_locale_comment_).md>) — Creates a localized string from an interpolated string.
- [init(localized:options:table:bundle:locale:comment:)](<init(localized_options_table_bundle_locale_comment_).md>) — Creates a localized string from an interpolated string, applying the specified options.
- [LocalizationValue](localizationvalue.md) — A reference to a localizable string, with optional string interpolation.
- [init(localized:defaultValue:table:bundle:locale:comment:)](<init(localized_defaultvalue_table_bundle_locale_comment_).md>) — Creates a localized string from an arbitrary static string key.
- [init(localized:defaultValue:options:table:bundle:locale:comment:)](<init(localized_defaultvalue_options_table_bundle_locale_comment_).md>) — Creates a localized string from an arbitrary static string key, applying the specified options.
- [init(localized:)](<init(localized_).md>) — Creates a localized string from a localized string resource.
- [init(localized:options:)](<init(localized_options_).md>) — Creates a localized string from a localized string resource, applying the specified options.
