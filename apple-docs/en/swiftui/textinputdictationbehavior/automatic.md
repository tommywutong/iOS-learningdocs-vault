---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textinputdictationbehavior/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/textinputdictationbehavior/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textinputdictationbehavior/automatic.json'
content_hash: 'sha256:9fe5ded3ac8ec598'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextInputDictationBehavior](../textinputdictationbehavior.md)

# automatic

<sub>Type Property</sub>

A platform-appropriate default text input dictation behavior.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let automatic: TextInputDictationBehavior
```

## Discussion

The automatic behavior uses a [TextInputDictationActivation](../textinputdictationactivation.md) value of [onLook](../textinputdictationactivation/onlook.md) for visionOS apps and [onSelect](../textinputdictationactivation/onselect.md) for iOS apps.

## See Also

### Getting behavior values

- [inline(activation:)](<inline(activation_).md>) — Adds a dictation microphone in the search bar.
- [preventDictation](preventdictation.md) — Prevents the search bar from having a dictation microphone.
