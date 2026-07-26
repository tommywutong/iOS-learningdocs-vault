---
title: 'init(localized:options:table:bundle:locale:comment:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(localized:options:table:bundle:locale:comment:)'
source_url: 'https://developer.apple.com/documentation/swift/string/init(localized:options:table:bundle:locale:comment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28localized%3Aoptions%3Atable%3Abundle%3Alocale%3Acomment%3A%29.json'
content_hash: 'sha256:2d3389eb9acea6f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(localized:options:table:bundle:locale:comment:)

<sub>Initializer</sub>

Creates a localized string from an interpolated string, applying the specified options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(localized keyAndValue: String.LocalizationValue, options: String.LocalizationOptions, table: String? = nil, bundle: Bundle? = nil, locale: Locale = .current, comment: StaticString? = nil)
```

## Parameters

- `keyAndValue` — A localization value instance that provides the localization key to look up. This parameter also serves as the default value if the system can’t find a localized string.

- `options` — A localization options instance that specifies localization options to apply, such as replacement values for formatted strings.

- `table` — The bundle’s string table to search. If `table` is `nil` or is an empty string, the method attempts to use the table named `Localizable`. The default is `nil`.

- `bundle` — The bundle to use for looking up strings. If `nil`, an app searches its main bundle. The default is `nil`.

- `locale` — The locale to use when localizing interpolated values, such as numbers. This doesn’t change which locale the system uses to look up the localized string. If `nil`, this initializer uses the current locale. The default is `nil`.

- `comment` — The comment to place above the key-value pair in the strings file. This parameter provides the translator with some context about the localized string’s presentation to the user.

## Discussion

Use this initializer when the development-language string serves as your localization key. You can use a fixed string for the key or a string that the system interpolates from values you provide at runtime. For example, if your app’s strings catalog contains a localizable entry for ` “Hello, %@.”`, you create a localized string like the following:

```swift
// Assume the strings file or catalog contains "Hello, %@." for English
// and "Bonjour, %@." for French.
let userName = "Juan"
let greeting = String(localized: "Hello, \(userName).")
// greeting == "Hello, Juan." in en locale, "Bonjour, Juan." in fr locale.
```

Use the `options` parameter to include any replacement values to insert into the localized formatted string. The formatted string uses the syntax `\(placeholder: TYPE)` to strongly type replacement values. The following example shows how to insert strongly typed replacement values into a string:

```swift
// Assume the strings file or catalog contains "Position in queue: %lld."
// for English and "Position dans la file d’attente: %lld." for French.
var options = String.LocalizationOptions()
options.replacements = [12]
let queueMessage = String (localized: "Position in queue: \(placeholder: .int).",
                           options: options)
// queueMessage == "Position in queue: 12." in en locale, "Position dans la file d’attente: 12." in fr locale.
```

If you prefer to use an arbitrary localization key rather than the localized string in the development language, use [init(localized:defaultValue:options:table:bundle:locale:comment:)](<init(localized_defaultvalue_options_table_bundle_locale_comment_).md>). If you need to provide localized strings to another process that might be using a different locale, use [init(localized:options:)](<init(localized_options_).md>).

## See Also

### Creating a Localized String

- [init(localized:table:bundle:locale:comment:)](<init(localized_table_bundle_locale_comment_).md>) — Creates a localized string from an interpolated string.
- [LocalizationValue](localizationvalue.md) — A reference to a localizable string, with optional string interpolation.
- [LocalizationOptions](localizationoptions.md) — Options to apply when initializing a localized string.
- [init(localized:defaultValue:table:bundle:locale:comment:)](<init(localized_defaultvalue_table_bundle_locale_comment_).md>) — Creates a localized string from an arbitrary static string key.
- [init(localized:defaultValue:options:table:bundle:locale:comment:)](<init(localized_defaultvalue_options_table_bundle_locale_comment_).md>) — Creates a localized string from an arbitrary static string key, applying the specified options.
- [init(localized:)](<init(localized_).md>) — Creates a localized string from a localized string resource.
- [init(localized:options:)](<init(localized_options_).md>) — Creates a localized string from a localized string resource, applying the specified options.
