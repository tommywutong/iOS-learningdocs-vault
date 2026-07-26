---
title: bundle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/localizedstringresource/bundle
source_url: 'https://developer.apple.com/documentation/foundation/localizedstringresource/bundle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/localizedstringresource/bundle.json'
content_hash: 'sha256:975fb5aaed160608'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LocalizedStringResource](../localizedstringresource.md)

# bundle

<sub>Instance Property</sub>

The bundle containing the table’s strings file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var bundle: LocalizedStringResource.BundleDescription { get }
```

## See Also

### Accessing resource properties

- [key](key.md) — The key to use to look up a localized string.
- [defaultValue](defaultvalue.md) — The resource’s default value.
- [table](table.md) — The name of the table containing the key-value pairs.
- [BundleDescription](bundledescription.md) — The location of a bundle to use for looking up localized strings, such as the main bundle, or a bundle at a specific file URL.
- [locale](locale.md) — The locale to use to look up the localized string from the string resource.
