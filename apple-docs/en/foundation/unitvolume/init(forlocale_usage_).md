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
doc_path: '/documentation/foundation/unitvolume/init(forlocale:usage:)'
source_url: 'https://developer.apple.com/documentation/foundation/unitvolume/init(forlocale:usage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitvolume/init%28forlocale%3Ausage%3A%29.json'
content_hash: 'sha256:db51cf2f1fad6dbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UnitVolume](../unitvolume.md)

# init(forLocale:usage:)

<sub>Initializer</sub>

Creates a `UnitVolume` which the specified `locale` prefers for the specific `usage`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(forLocale: Locale, usage: MeasurementFormatUnitUsage<UnitVolume> = .general)
```
