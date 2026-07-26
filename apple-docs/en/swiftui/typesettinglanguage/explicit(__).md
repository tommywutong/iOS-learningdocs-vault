---
title: 'explicit(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/typesettinglanguage/explicit(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/typesettinglanguage/explicit(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/typesettinglanguage/explicit%28_%3A%29.json'
content_hash: 'sha256:4542901c7569b6aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TypesettingLanguage](../typesettinglanguage.md)

# explicit(_:)

<sub>Type Method</sub>

Use explicit language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func explicit(_ language: Locale.Language) -> TypesettingLanguage
```

## Parameters

- `language` — The language to use for typesetting.

## Return Value

A `TypesettingLanguage`.

## Discussion

An explicit language will be used for typesetting. For example, if used with Thai language the line heights will be as tall as needed to accommodate Thai.

## See Also

### Getting language behavior

- [automatic](automatic.md) — Automatic language behavior.
