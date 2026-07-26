---
title: 'init(style:locale:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/personnamecomponents/formatstyle/init(style:locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponents/formatstyle/init(style:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponents/formatstyle/init%28style%3Alocale%3A%29.json'
content_hash: 'sha256:0ab57a75b71888f1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [PersonNameComponents](../../personnamecomponents.md) · [FormatStyle](../formatstyle.md)

# init(style:locale:)

<sub>Initializer</sub>

Creates an instance using the provided format style and locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(style: PersonNameComponents.FormatStyle.Style = .medium, locale: Locale = .autoupdatingCurrent)
```

## Parameters

- `style` — The [Style](style-swift.enum.md) used to format the name.

- `locale` — The [Locale](../../locale.md) used to create the string representation of the name.

## Discussion

Customize the person name components format style by providing a style and a locale.

The formatted style can be long, medium, short, or abbreviated. The default value is [PersonNameComponents.FormatStyle.Style.medium](style-swift.enum/medium.md).

The locale provides linguistic and cultural context to the formatted name. The default value is [autoupdatingCurrent](../../locale/autoupdatingcurrent.md).
