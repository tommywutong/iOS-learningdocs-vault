---
title: locale
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/listformatter/locale
source_url: 'https://developer.apple.com/documentation/foundation/listformatter/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/listformatter/locale.json'
content_hash: 'sha256:8a7da42fffff28f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ListFormatter](../listformatter.md)

# locale

<sub>Instance Property</sub>

The locale to use when formatting items in the list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale! { get set }
```

## Discussion

The default value is [autoupdatingCurrentLocale](../nslocale/autoupdatingcurrent.md). If you set this property to `nil`, the formatter resets to using [autoupdatingCurrentLocale](../nslocale/autoupdatingcurrent.md).

## See Also

### Configuring Formatter Options

- [itemFormatter](itemformatter.md) — An object that formats each item in the list.
