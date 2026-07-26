---
title: 'init(_:table:locale:bundle:comment:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/localizedstringresource/init(_:table:locale:bundle:comment:)-69k32'
source_url: 'https://developer.apple.com/documentation/foundation/localizedstringresource/init(_:table:locale:bundle:comment:)-69k32'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/localizedstringresource/init%28_%3Atable%3Alocale%3Abundle%3Acomment%3A%29-69k32.json'
content_hash: 'sha256:2507c38ca193b6d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LocalizedStringResource](../localizedstringresource.md)

# init(_:table:locale:bundle:comment:)

<sub>Initializer</sub>

Creates a localized string resource from a localization key and its bundle properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ keyAndValue: String.LocalizationValue, table: String? = nil, locale: Locale = .current, bundle: LocalizedStringResource.BundleDescription = .main, comment: StaticString? = nil)
```

## Parameters

- `keyAndValue` — The key for an entry in the specified table.

- `table` — The name of the table containing the key-value pairs. If not provided, `nil`, or an empty string, this value defaults to `Localizable.strings.`

- `locale` — The locale for the resource to use. By default, the resource uses [current](../locale/current.md).

- `bundle` — A [BundleDescription](bundledescription.md) that indicates where to locate the table’s strings file. By default, the resource uses the main bundle.

- `comment` — The comment to place above the key-value pair in the strings file. This parameter provides the translator with some context about the localized string’s presentation to the user.
