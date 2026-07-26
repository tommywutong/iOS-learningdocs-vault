---
title: 'siriTipViewStyle(_:)'
framework: AppIntents
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, tvOS 16.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/siritipviewstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/siritipviewstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/siritipviewstyle%28_%3A%29.json'
content_hash: 'sha256:63f22c7de3b9537d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# siriTipViewStyle(_:)

<sub>Instance Method</sub>

Sets the given style for SiriTipView within the view hierarchy

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func siriTipViewStyle(_ style: SiriTipViewStyle) -> some View

```

## Parameters

- `style` — The style to set.

## Return Value

A view that uses the specified style on its child views.

## See Also

### App intents

- [appEntityIdentifier(_:)](<appentityidentifier(__).md>) — Associates a SwiftUI view with an app entity to make its content discoverable by Apple Intelligence and Siri.
- [appEntityIdentifier(forSelectionType:identifier:)](<appentityidentifier(forselectiontype_identifier_).md>) — Associates the items in a SwiftUI list view with app entities to make them discoverable by Apple Intelligence and Siri.
- [appEntityUIElements(_:)](<appentityuielements(__).md>) — Provides the system with additional context to make a custom view’s content discoverable by Apple Intelligence and Siri.
- [onAppIntentExecution(_:perform:)](<onappintentexecution(__perform_).md>) — Registers a handler to invoke in response to the specified app intent that your app receives.
- [shortcutsLinkStyle(_:)](<shortcutslinkstyle(__).md>) — Sets the given style for ShortcutsLinks within the view hierarchy
