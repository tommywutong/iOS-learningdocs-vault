---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/localizationvalue/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/localizationvalue/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/localizationvalue/init%28_%3A%29.json'
content_hash: 'sha256:9d0e9231768dd0df'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [LocalizationValue](../localizationvalue.md)

# init(_:)

<sub>Initializer</sub>

Creates a localization value instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ value: String)
```

## Parameters

- `value` — A string that provides the localization key to look up. This parameter also serves as the default value if the system can’t find a localized string.

## Discussion

Creating a [LocalizationValue](../localizationvalue.md) with this initializer creates a localized value with no interpolated values.
