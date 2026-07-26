---
title: 'init(_:defaultValue:table:locale:bundle:comment:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/localizedstringresource/init(_:defaultvalue:table:locale:bundle:comment:)-1apqa'
source_url: 'https://developer.apple.com/documentation/foundation/localizedstringresource/init(_:defaultvalue:table:locale:bundle:comment:)-1apqa'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/localizedstringresource/init%28_%3Adefaultvalue%3Atable%3Alocale%3Abundle%3Acomment%3A%29-1apqa.json'
content_hash: 'sha256:8c82479f718cdab5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LocalizedStringResource](../localizedstringresource.md)

# init(_:defaultValue:table:locale:bundle:comment:)

<sub>Initializer</sub>

Creates a localized string resource from a static string and its bundle properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ key: StaticString, defaultValue: String.LocalizationValue, table: String? = nil, locale: Locale = .current, bundle: LocalizedStringResource.BundleDescription = .main, comment: StaticString? = nil)
```

## Parameters

- `key` — The key for an entry in the specified table.

- `defaultValue` — A localization value to use if `key` doesn’t exist in `table`. Xcode’s Product \> Export Localizations feature also extracts this value as the default translation in the project’s development locale.

- `table` — The name of the table containing the key-value pairs. If not provided, `nil`, or an empty string, this value defaults to `Localizable.strings.`

- `locale` — The locale for the resource to use. By default, the resource uses [current](../locale/current.md).

- `bundle` — A [BundleDescription](bundledescription.md) that indicates where to locate the table’s strings file. By default, the resource uses the main bundle.

- `comment` — The comment to place above the key-value pair in the strings file. This parameter provides the translator with some context about the localized string’s presentation to the user.
