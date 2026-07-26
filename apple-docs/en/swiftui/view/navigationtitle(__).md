---
title: 'navigationTitle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/navigationtitle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/navigationtitle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/navigationtitle%28_%3A%29.json'
content_hash: 'sha256:8c90ba61f08cada7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# navigationTitle(_:)

<sub>Instance Method</sub>

Configures the view’s title for purposes of navigation, using a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func navigationTitle(_ titleResource: LocalizedStringResource) -> some View

```

## Parameters

- `titleResource` — The key to a localized string to display.

## Discussion

A view’s navigation title is used to visually display the current navigation state of an interface. On iOS and watchOS, when a view is navigated to inside of a navigation view, that view’s title is displayed in the navigation bar. On iPadOS, the primary destination’s navigation title is reflected as the window’s title in the App Switcher. Similarly on macOS, the primary destination’s title is used as the window title in the titlebar, Windows menu and Mission Control.

Refer to the [Configure your apps navigation titles](../configure-your-apps-navigation-titles.md) article for more information on navigation title modifiers.

## See Also

### Setting titles for navigation content

- [navigationSubtitle(_:)](<navigationsubtitle(__).md>) — Configures the view’s subtitle for purposes of navigation, using a localized string resource.
- [navigationDocument(_:)](<navigationdocument(__).md>) — Configures the view’s document for purposes of navigation.
- [navigationDocument(_:preview:)](<navigationdocument(__preview_).md>) — Configures the view’s document for purposes of navigation.
