---
title: 'init(localized:options:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(localized:options:)'
source_url: 'https://developer.apple.com/documentation/swift/string/init(localized:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28localized%3Aoptions%3A%29.json'
content_hash: 'sha256:b85e8aee6c00a84c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(localized:options:)

<sub>Initializer</sub>

Creates a localized string from a localized string resource, applying the specified options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(localized resource: LocalizedStringResource, options: String.LocalizationOptions)
```

## Parameters

- `resource` — A `LocalizedStringResource` that provides the localization key, table, bundle, and locale.

- `options` — A localization options instance that specifies localization options to apply, such as replacement values for formatted strings.

## Discussion

Call this initializer to look up the localization that `resource` indicates from a string catalog or `strings` file in your app bundle. Alter the resource’s `locale` prior to calling this method if you want to localize this string in a different locale than the process that creates the `LocalizedStringResource`.

```swift
// Assume the string catalog contains "Hello, world!" for English
// and "Bonjour, le monde!" for French.
var localizable = LocalizedStringResource("Hello, world!")
// Potentially using localizable in another process…
localizable.locale = Locale(identifier: "en")
let enLocalized = String(localized: localizable)
localizable.locale = Locale(identifier: "fr")
let frLocalized = String(localized: localizable)
// enLocalized == "Hello, world!"
// frLocalized == "Bonjour, le monde!"
```

Use the `options` parameter to include any replacement values to insert into the localized formatted string. The formatted string uses the syntax `\(placeholder: TYPE)` to strongly type replacement values. The following example shows how to insert strongly typed replacement values into a string:

```swift
// Assume the strings file or catalog contains "Position in queue: %lld."
// for English and "Position dans la file d’attente: %lld." for French.
var localizable = LocalizedStringResource("Position in queue: \(placeholder: .int).")
// Potentially using localizable in another process…
var options = String.LocalizationOptions()
options.replacements = [12]
localizable.locale = Locale(identifier: "en")
let enLocalized = String (localized: localizable, options: options)
localizable.locale = Locale(identifier: "fr")
let frLocalized = String (localized: localizable, options: options)
// enLocalized == "Position in queue: 12."
// frLocalized == "Position dans la file d’attente: 12."
```

If you don’t need the deferred-loading behavior of `LocalizedStringResource`, use [init(localized:options:table:bundle:locale:comment:)](<init(localized_options_table_bundle_locale_comment_).md>) instead. If you prefer to use an arbitrary localization key rather than the localized string in the development language, use [init(localized:defaultValue:options:table:bundle:locale:comment:)](<init(localized_defaultvalue_options_table_bundle_locale_comment_).md>).

## See Also

### Creating a Localized String

- [init(localized:table:bundle:locale:comment:)](<init(localized_table_bundle_locale_comment_).md>) — Creates a localized string from an interpolated string.
- [init(localized:options:table:bundle:locale:comment:)](<init(localized_options_table_bundle_locale_comment_).md>) — Creates a localized string from an interpolated string, applying the specified options.
- [LocalizationValue](localizationvalue.md) — A reference to a localizable string, with optional string interpolation.
- [LocalizationOptions](localizationoptions.md) — Options to apply when initializing a localized string.
- [init(localized:defaultValue:table:bundle:locale:comment:)](<init(localized_defaultvalue_table_bundle_locale_comment_).md>) — Creates a localized string from an arbitrary static string key.
- [init(localized:defaultValue:options:table:bundle:locale:comment:)](<init(localized_defaultvalue_options_table_bundle_locale_comment_).md>) — Creates a localized string from an arbitrary static string key, applying the specified options.
- [init(localized:)](<init(localized_).md>) — Creates a localized string from a localized string resource.
