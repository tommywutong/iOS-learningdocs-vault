---
title: 'typesettingLanguage(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/typesettinglanguage(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/typesettinglanguage(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/typesettinglanguage%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:d6316a1df4a10761'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# typesettingLanguage(_:isEnabled:)

<sub>Instance Method</sub>

Specifies the language for typesetting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func typesettingLanguage(_ language: Locale.Language, isEnabled: Bool = true) -> some View

```

## Parameters

- `language` — The explicit language to use for typesetting.

- `isEnabled` — A Boolean value that indicates whether text language is added

## Return Value

A view with the typesetting language set to the value you supply.

## Discussion

In some cases `Text` may contain text of a particular language which doesn’t match the device UI language. In that case it’s useful to specify a language so line height, line breaking and spacing will respect the script used for that language. For example:

```swift
Text(verbatim: "แอปเปิล")
    .typesettingLanguage(.init(languageCode: .thai))
```

Note: this language does not affect text localization.

## See Also

### Localizing text

- [Preparing views for localization](../preparing-views-for-localization.md) — Specify hints and add strings to localize your SwiftUI views.
- [LocalizedStringKey](../localizedstringkey.md) — The key used to look up an entry in a strings file or strings dictionary file.
- [locale](../environmentvalues/locale.md) — The current locale that views should use.
- [TypesettingLanguage](../typesettinglanguage.md) — Defines how typesetting language is determined for text.
