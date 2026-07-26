---
title: 'CTFontGetUIFontType(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontgetuifonttype(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontgetuifonttype(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontgetuifonttype%28_%3A%29.json'
content_hash: 'sha256:469f4857cb424f7f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontGetUIFontType(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontGetUIFontType(_ font: CTFont) -> CTFontUIFontType
```

## Discussion

Get the CTFontUIFontType of UI font. Note that this value may differ from the uiType parameter originally passed to CTFontCreateUIFontForLanguage, as the system may use a different uiType value internally.
