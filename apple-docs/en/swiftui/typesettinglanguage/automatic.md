---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/typesettinglanguage/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/typesettinglanguage/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/typesettinglanguage/automatic.json'
content_hash: 'sha256:70fcacee273e97ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TypesettingLanguage](../typesettinglanguage.md)

# automatic

<sub>Type Property</sub>

Automatic language behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let automatic: TypesettingLanguage
```

## Discussion

When determining the language to use for typesetting the current UI language and preferred languages will be considered. For example, if the current UI locale is for English and Thai is included in the preferred languages then line heights will be taller to accommodate the taller glyphs used by Thai.

## See Also

### Getting language behavior

- [explicit(_:)](<explicit(__).md>) — Use explicit language.
