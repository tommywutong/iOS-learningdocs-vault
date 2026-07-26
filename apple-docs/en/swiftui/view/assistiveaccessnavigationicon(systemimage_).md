---
title: 'assistiveAccessNavigationIcon(systemImage:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/assistiveaccessnavigationicon(systemimage:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/assistiveaccessnavigationicon(systemimage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/assistiveaccessnavigationicon%28systemimage%3A%29.json'
content_hash: 'sha256:d10ec8c66bed1586'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# assistiveAccessNavigationIcon(systemImage:)

<sub>Instance Method</sub>

Configures the view’s icon for purposes of navigation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func assistiveAccessNavigationIcon(systemImage: String) -> some View

```

## Parameters

- `systemImage` — The system symbol to display.

## Discussion

In an Assistive Access scene on iOS and iPadOS, the icon is displayed adjacent to the navigation title. Otherwise, the icon is unused.

## See Also

### Using assistive access

- [accessibilityAssistiveAccessEnabled](../environmentvalues/accessibilityassistiveaccessenabled.md) — A Boolean value that indicates whether Assistive Access is in use.
- [AssistiveAccess](../assistiveaccess.md) — A scene that presents an interface appropriate for Assistive Access on iOS and iPadOS. On other platforms, this scene is unused.
- [assistiveAccessNavigationIcon(_:)](<assistiveaccessnavigationicon(__).md>) — Configures the view’s icon for purposes of navigation.
