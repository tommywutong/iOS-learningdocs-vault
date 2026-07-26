---
title: 'navigationSubtitle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 16.0+, macOS 13.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/navigationsubtitle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/navigationsubtitle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/navigationsubtitle%28_%3A%29.json'
content_hash: 'sha256:0bed5e95d7542607'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# navigationSubtitle(_:)

<sub>Instance Method</sub>

Configures the view’s subtitle for purposes of navigation, using a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@export(implementation) nonisolated func navigationSubtitle(_ subtitleKey: LocalizedStringResource) -> some View

```

## Parameters

- `subtitleKey` — The key to a localized string to display.

## Discussion

A view’s navigation subtitle is used to provide additional contextual information alongside the navigation title. On macOS, the primary destination’s subtitle is displayed with the navigation title in the titlebar. On iOS and iPadOS, the subtitle is displayed with the navigation title in the navigation bar.

## See Also

### Setting titles for navigation content

- [navigationTitle(_:)](<navigationtitle(__).md>) — Configures the view’s title for purposes of navigation, using a localized string resource.
- [navigationDocument(_:)](<navigationdocument(__).md>) — Configures the view’s document for purposes of navigation.
- [navigationDocument(_:preview:)](<navigationdocument(__preview_).md>) — Configures the view’s document for purposes of navigation.
