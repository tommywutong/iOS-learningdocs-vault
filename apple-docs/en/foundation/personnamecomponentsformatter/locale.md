---
title: locale
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/personnamecomponentsformatter/locale
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponentsformatter/locale.json'
content_hash: 'sha256:caa336f0eaefabc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PersonNameComponentsFormatter](../personnamecomponentsformatter.md)

# locale

<sub>Instance Property</sub>

Specifies the locale to format names.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale! { get set }
```

## Discussion

Defaults to `autoupdatingCurrentLocale`. Also resets to `autoupdatingCurrentLocale` on assignment of `nil`.
