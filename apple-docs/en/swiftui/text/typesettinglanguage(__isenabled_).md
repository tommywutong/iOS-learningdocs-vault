---
title: 'typesettingLanguage(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/typesettinglanguage(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/typesettinglanguage(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/typesettinglanguage%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:c83804b748e18874'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# typesettingLanguage(_:isEnabled:)

<sub>Instance Method</sub>

Specifies the language for typesetting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func typesettingLanguage(_ language: Locale.Language, isEnabled: Bool = true) -> Text
```

## Parameters

- `language` — The explicit language to use for typesetting.

- `isEnabled` — A Boolean value that indicates whether text language is added

## Return Value

Text with the typesetting language set to the value you supply.

## Discussion

In some cases `Text` may contain text of a particular language which doesn’t match the device UI language. In that case it’s useful to specify a language so line height, line breaking and spacing will respect the script used for that language. For example:

```swift
Text(verbatim: "แอปเปิล")
    .typesettingLanguage(.init(languageCode: .thai))
```

Note: this language does not affect text localization.
