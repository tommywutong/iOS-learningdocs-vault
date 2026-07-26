---
title: locale
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/localizedstringresource/locale
source_url: 'https://developer.apple.com/documentation/foundation/localizedstringresource/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/localizedstringresource/locale.json'
content_hash: 'sha256:0a6d722453d4777c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LocalizedStringResource](../localizedstringresource.md)

# locale

<sub>Instance Property</sub>

The locale to use to look up the localized string from the string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale
```

## Discussion

To perform localization in a different locale, change this value before passing it to a [String](../../swift/string.md) or [AttributedString](../attributedstring.md) initializer that takes a [LocalizedStringResource](../localizedstringresource.md).

## See Also

### Accessing resource properties

- [key](key.md) — The key to use to look up a localized string.
- [defaultValue](defaultvalue.md) — The resource’s default value.
- [table](table.md) — The name of the table containing the key-value pairs.
- [bundle](bundle.md) — The bundle containing the table’s strings file.
- [BundleDescription](bundledescription.md) — The location of a bundle to use for looking up localized strings, such as the main bundle, or a bundle at a specific file URL.
