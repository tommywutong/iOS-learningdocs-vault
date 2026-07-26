---
title: NSLocalizedStringFromTableInBundle
framework: Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslocalizedstringfromtableinbundle
source_url: 'https://developer.apple.com/documentation/foundation/nslocalizedstringfromtableinbundle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocalizedstringfromtableinbundle.json'
content_hash: 'sha256:cb518ed6ae2c3d68'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSLocalizedStringFromTableInBundle

<sub>Macro</sub>

Returns a localized version of a string from the table and bundle that you specify, which Xcode autogenerates when exporting localizations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define NSLocalizedStringFromTableInBundle(key, tbl, bundle, comment)
```

## Parameters

- `key` — The key for a string in the specified table. > [!note] Note > Xcode can’t export localizations for strings whose `key` is a string variable, `nil`, or an empty string.

- `tbl` — The name of the table containing the key-value pairs. Also, the suffix for the strings file (a file with the `.strings` extension) to store the localized string. The default table in `Localizable.strings` is used when `tableName` is `nil` or an empty string.

- `bundle` — The bundle containing the table’s strings file. The main bundle is used when `bundle` is `nil`.

- `comment` — The comment to place above the key-value pair in the strings file. This parameter provides the translator with some context about the localized string’s presentation to the user.

## Return Value

The result of sending [- localizedStringForKey:value:table:](<bundle/localizedstring(forkey_value_table_).md>) to `bundle`, passing the specified `key` and `tableName`.

## Discussion

Use this macro to automatically generate a strings file named `[tableName].strings` located in `bundle` from your code when exporting localizations from Xcode or the `genstrings` utility. You can specify Unicode characters in `key` using `\\Uxxxx`—see the `-u` option for the `genstrings` utility.

The initial value for `key` in the strings file is `key`. To avoid collisions between words or phrases with multiple meanings, use a unique `key` for each use of the same phrase. Use the [NSLocalizedStringWithDefaultValue](nslocalizedstringwithdefaultvalue.md) macro to specify another value for `key`.

For information about inserting plural nouns and units into localized strings, see [Localizing strings that contain plurals](../xcode/localizing-strings-that-contain-plurals.md).

As of OS X 10.11 and iOS 9, [Bundle](bundle.md) is thread-safe. As such, you can safely call [NSLocalizedStringFromTableInBundle](nslocalizedstringfromtableinbundle.md) from any execution context.

> [!important] Important
> The values for `key`, `tableName`, and `comment` must be string literal values. Xcode can read these values from source code to automatically create localization tables when exporting localizations, but it doesn’t resolve string variables. If you want to use string variables, manually create a strings file and use [- localizedStringForKey:value:table:](<bundle/localizedstring(forkey_value_table_).md>) instead. For more information on strings files, see [String Resources](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Strings/Strings.html#//apple_ref/doc/uid/10000051i-CH6).

> [!tip] Tip
> Break up long string values into consecutive string literals.

```objc
NSLocalizedStringFromTableInBundle(
    @"Did you know that venus flytraps have flowers"
        @" atop very long stems?\nThe long stem keeps"
        @" insects a safe distance away from their"
        @" digestive leaves below.",
    @"Localized",
    [NSBundle mainBundle],
    @"An interesting fact about venus flytraps shown"
        @" on the loading screen.");
```

## See Also

### Related Documentation

- [Exporting localizations](../xcode/exporting-localizations.md) — Provide the localizable files from your project to localizers.
- [Importing localizations](../xcode/importing-localizations.md) — Import the files that you translate or adapt for a language and region into your project.

### Localization

- [NSLocale](nslocale.md) — Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
- [NSOrthography](nsorthography.md) — A description of the linguistic content of natural language text, typically used for spelling and grammar checking.
- [NSLocalizedString](nslocalizedstring.md) — Returns a localized version of a string from the default table, which Xcode autogenerates when exporting localizations.
- [NSLocalizedStringFromTable](nslocalizedstringfromtable.md) — Returns a localized version of a string from the table that you specify, which Xcode autogenerates when exporting localizations.
- [NSLocalizedStringWithDefaultValue](nslocalizedstringwithdefaultvalue.md) — Returns a localized version of a string identified by a key in the table that you specify, which Xcode autogenerates when exporting localizations.
