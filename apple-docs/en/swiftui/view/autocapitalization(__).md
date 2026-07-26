---
title: 'autocapitalization(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/autocapitalization(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/autocapitalization(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/autocapitalization%28_%3A%29.json'
content_hash: 'sha256:92542312ad9b550a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# autocapitalization(_:)

<sub>Instance Method</sub>

Sets whether to apply auto-capitalization to this view.

> [!warning] Deprecated
> Use [textInputAutocapitalization(_:)](<textinputautocapitalization(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated func autocapitalization(_ style: UITextAutocapitalizationType) -> some View

```

## Parameters

- `style` — One of the autocapitalization modes defined in the [UITextAutocapitalizationType](../../uikit/uitextautocapitalizationtype.md) enumeration.

## Discussion

Use this method when you need to automatically capitalize words, sentences, or other text like proper nouns.

In example below, as the user enters text each word is automatically capitalized:

```swift
TextField("Last, First", text: $fullName)
    .autocapitalization(UITextAutocapitalizationType.words)
```

The [UITextAutocapitalizationType](../../uikit/uitextautocapitalizationtype.md) enumeration defines the available capitalization modes. The default is [UITextAutocapitalizationType.sentences](../../uikit/uitextautocapitalizationtype/sentences.md).

## See Also

### Text modifiers

- [disableAutocorrection(_:)](<disableautocorrection(__).md>) — Sets whether to disable autocorrection for this view. _(deprecated)_
