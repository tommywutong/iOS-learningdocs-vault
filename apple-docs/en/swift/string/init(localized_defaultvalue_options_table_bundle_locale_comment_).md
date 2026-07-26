---
title: 'init(localized:defaultValue:options:table:bundle:locale:comment:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(localized:defaultvalue:options:table:bundle:locale:comment:)'
source_url: 'https://developer.apple.com/documentation/swift/string/init(localized:defaultvalue:options:table:bundle:locale:comment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28localized%3Adefaultvalue%3Aoptions%3Atable%3Abundle%3Alocale%3Acomment%3A%29.json'
content_hash: 'sha256:7c4cb40b61982098'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(localized:defaultValue:options:table:bundle:locale:comment:)

<sub>Initializer</sub>

Creates a localized string from an arbitrary static string key, applying the specified options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(localized key: StaticString, defaultValue: String.LocalizationValue, options: String.LocalizationOptions, table: String? = nil, bundle: Bundle? = nil, locale: Locale = .current, comment: StaticString? = nil)
```

## Parameters

- `defaultValue` — A default value to use if looking up a localized string from the bundle fails. This is typically the localizable string in the development language.

- `options` — A localization options instance that specifies localization options to apply, such as replacement values for formatted strings.

- `table` — The bundle’s string table to search. If `table` is `nil` or is an empty string, the method attempts to use the table named `Localizable`. The default is `nil`.

- `bundle` — The bundle to use for looking up strings. If `nil`, an app searches its main bundle. The default is `nil`.

- `locale` — The locale to use when localizing interpolated values, such as numbers. This doesn’t change which locale the system uses to look up the localized string. If `nil`, this initializer uses the current locale. The default is `nil`.

- `comment` — The comment to place above the key-value pair in the strings file. This parameter provides the translator with some context about the localized string’s presentation to the user.

## Discussion

Use the `defaultValue` initializers when you want to use an explicit _key_ to look up localized strings. This is useful if the localizable string in your development language is ambiguous. For example _call_ in English can be a noun or a verb. In this case, you might want to use `.strings` file entries like `CALL_NOUN` and `CALL_VERB` to disambiguate the uses for localizers. You then use this initializer, providing both a key and a default value to use if the system can’t find the key at runtime.

```swift
// Assume the strings file or catalog contains the following:
// English: CALL_VERB = "Call", CALL_NOUN = "Call"
// French: CALL_VERB = "Appeler", CALL_NOUN = "Appel"
let callVerb = String(localized: "CALL_VERB", defaultValue: "Call")
let callNoun = String(localized: "CALL_NOUN", defaultValue: "Call")
// callVerb == "Call" in en locale, "Appeler" in fr locale.
// callNoun == "Call" in en locale, "Appel" in fr locale.
```

Use the `options` parameter to include any replacement values to insert into the localized formatted string. The following example shows how to insert strongly-typed replacement values into a string:

```swift
// Assume the strings file or catalog contains the explicit key "POSITION_IN_QUEUE",
// with localizations "Position in queue: %lld." for English and
// "Position dans la file d’attente: %lld." for French.
var options = String.LocalizationOptions()
options.replacements = [12]
let localized = String (localized: "POSITION_IN_QUEUE",
                        defaultValue:"Position in queue: \(placeholder: .int).",
                        options: options)
// localized = "Position in queue: 12." in en locale, "Position dans la file d’attente: 12." in fr locale.
```

To use the default localization as the key rather than an explicit key, use [init(localized:options:table:bundle:locale:comment:)](<init(localized_options_table_bundle_locale_comment_).md>) instead. If you need to provide localized strings to another process that might be using a different locale, use [init(localized:options:)](<init(localized_options_).md>).

## See Also

### Creating a Localized String

- [init(localized:table:bundle:locale:comment:)](<init(localized_table_bundle_locale_comment_).md>) — Creates a localized string from an interpolated string.
- [init(localized:options:table:bundle:locale:comment:)](<init(localized_options_table_bundle_locale_comment_).md>) — Creates a localized string from an interpolated string, applying the specified options.
- [LocalizationValue](localizationvalue.md) — A reference to a localizable string, with optional string interpolation.
- [LocalizationOptions](localizationoptions.md) — Options to apply when initializing a localized string.
- [init(localized:defaultValue:table:bundle:locale:comment:)](<init(localized_defaultvalue_table_bundle_locale_comment_).md>) — Creates a localized string from an arbitrary static string key.
- [init(localized:)](<init(localized_).md>) — Creates a localized string from a localized string resource.
- [init(localized:options:)](<init(localized_options_).md>) — Creates a localized string from a localized string resource, applying the specified options.
