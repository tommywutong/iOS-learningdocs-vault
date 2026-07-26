---
title: 'init(forLocale:usage:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/unittemperature/init(forlocale:usage:)'
source_url: 'https://developer.apple.com/documentation/foundation/unittemperature/init(forlocale:usage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unittemperature/init%28forlocale%3Ausage%3A%29.json'
content_hash: 'sha256:4f4ccea7702d1786'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UnitTemperature](../unittemperature.md)

# init(forLocale:usage:)

<sub>Initializer</sub>

Creates a `UnitTemperature` which the specified `locale` prefers for the specific `usage`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(forLocale: Locale, usage: MeasurementFormatUnitUsage<UnitTemperature> = .general)
```
