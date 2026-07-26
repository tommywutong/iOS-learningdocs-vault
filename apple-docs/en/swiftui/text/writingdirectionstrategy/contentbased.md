---
title: contentBased
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/writingdirectionstrategy/contentbased
source_url: 'https://developer.apple.com/documentation/swiftui/text/writingdirectionstrategy/contentbased'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/writingdirectionstrategy/contentbased.json'
content_hash: 'sha256:69cc69d95aed9d33'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Text](../../text.md) · [WritingDirectionStrategy](../writingdirectionstrategy.md)

# contentBased

<sub>Type Property</sub>

The writing direction following the language of the string that is laid out.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let contentBased: Text.WritingDirectionStrategy
```

## Discussion

The system may use different sources to determine the language of the string. This may include the characters used in the string, especially BiDi isolation markers, the language of the localization file the string was loaded from, or explicit annotations with the [languageIdentifier](../../../foundation/attributescopes/foundationattributes/languageidentifier.md) attribute.
