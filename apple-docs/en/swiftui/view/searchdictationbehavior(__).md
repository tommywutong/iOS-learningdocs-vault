---
title: 'searchDictationBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/searchdictationbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchdictationbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchdictationbehavior%28_%3A%29.json'
content_hash: 'sha256:9df21436ea6a7725'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchDictationBehavior(_:)

<sub>Instance Method</sub>

Configures the dictation behavior for any search fields configured by the searchable modifier.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated func searchDictationBehavior(_ dictationBehavior: TextInputDictationBehavior) -> some View

```

## Discussion

By default, search fields on visionOS will automatically start dictation when looking at the dictation button in the search field. You can change this behavior by providing a value of [preventDictation](../textinputdictationbehavior/preventdictation.md) to this modifier.

See the [TextInputDictationBehavior](../textinputdictationbehavior.md) type for more information on the available dictation behaviors.

## See Also

### Dictating text

- [TextInputDictationActivation](../textinputdictationactivation.md)
- [TextInputDictationBehavior](../textinputdictationbehavior.md)
