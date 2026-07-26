---
title: String.LocalizationValue
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/localizationvalue
source_url: 'https://developer.apple.com/documentation/swift/string/localizationvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/localizationvalue.json'
content_hash: 'sha256:4a23bcfb32e6125e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# String.LocalizationValue

<sub>Structure</sub>

A reference to a localizable string, with optional string interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct LocalizationValue
```

## Overview

Use this type when the localization key is the localized string value in the development language.  This type also supports creating localized strings that depend on a value you provide at runtime. For example, if your app’s strings catalog contains a localizable entry for `"Hello, \(userName)."`, you create a localized string like the following:

```swift
    let greeting = String(localized: "Hello, \(userName).")
```

If you want to use an arbitary string as your localization key, use [String](../string.md) initializers that take a [StaticString](../staticstring.md) and a `defaultValue` parameter, like [init(localized:defaultValue:table:bundle:locale:comment:)](<init(localized_defaultvalue_table_bundle_locale_comment_).md>) and [init(localized:defaultValue:options:table:bundle:locale:comment:)](<init(localized_defaultvalue_options_table_bundle_locale_comment_).md>).

If you need to provide localized strings to another process that might be using a different locale, initialize with a `LocalizedStringResource`, using [init(localized:)](<init(localized_).md>) or [init(localized:options:)](<init(localized_options_).md>).

## Relationships

- **Conforms To**: [Copyable](../copyable.md), [Decodable](../decodable.md), [Encodable](../encodable.md), [Equatable](../equatable.md), [Escapable](../escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringInterpolation](../expressiblebystringinterpolation.md), [ExpressibleByStringLiteral](../expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../expressiblebyunicodescalarliteral.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Creating a string localization value instance

- [init(_:)](<localizationvalue/init(__).md>) — Creates a localization value instance.

### Supporting types

- [Placeholder](localizationvalue/placeholder.md) — An enumeration of types that can appear as a placeholder in a string interpolation.

## See Also

### Creating a Localized String

- [init(localized:table:bundle:locale:comment:)](<init(localized_table_bundle_locale_comment_).md>) — Creates a localized string from an interpolated string.
- [init(localized:options:table:bundle:locale:comment:)](<init(localized_options_table_bundle_locale_comment_).md>) — Creates a localized string from an interpolated string, applying the specified options.
- [LocalizationOptions](localizationoptions.md) — Options to apply when initializing a localized string.
- [init(localized:defaultValue:table:bundle:locale:comment:)](<init(localized_defaultvalue_table_bundle_locale_comment_).md>) — Creates a localized string from an arbitrary static string key.
- [init(localized:defaultValue:options:table:bundle:locale:comment:)](<init(localized_defaultvalue_options_table_bundle_locale_comment_).md>) — Creates a localized string from an arbitrary static string key, applying the specified options.
- [init(localized:)](<init(localized_).md>) — Creates a localized string from a localized string resource.
- [init(localized:options:)](<init(localized_options_).md>) — Creates a localized string from a localized string resource, applying the specified options.
