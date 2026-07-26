---
title: 'navigationDocument(_:preview:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/navigationdocument(_:preview:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/navigationdocument(_:preview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/navigationdocument%28_%3Apreview%3A%29.json'
content_hash: 'sha256:2a464cb9d3c225c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# navigationDocument(_:preview:)

<sub>Instance Method</sub>

Configures the view’s document for purposes of navigation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func navigationDocument<D, I1, I2>(_ document: D, preview: SharePreview<I1, I2>) -> some View where D : Transferable, I1 : Transferable, I2 : Transferable

```

## Parameters

- `document` — The transferable content associated to the navigation title.

- `preview` — The preview of the document to use when sharing.

## Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the document. In macOS, this populates a proxy icon.

Refer to the [Configure your apps navigation titles](../configure-your-apps-navigation-titles.md) article for more information on navigation document modifiers.

## See Also

### Setting titles for navigation content

- [navigationTitle(_:)](<navigationtitle(__).md>) — Configures the view’s title for purposes of navigation, using a localized string resource.
- [navigationSubtitle(_:)](<navigationsubtitle(__).md>) — Configures the view’s subtitle for purposes of navigation, using a localized string resource.
- [navigationDocument(_:)](<navigationdocument(__).md>) — Configures the view’s document for purposes of navigation.
