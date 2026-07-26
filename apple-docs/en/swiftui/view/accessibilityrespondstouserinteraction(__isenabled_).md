---
title: 'accessibilityRespondsToUserInteraction(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityrespondstouserinteraction(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityrespondstouserinteraction(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityrespondstouserinteraction%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:da22197e1fe0735b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityRespondsToUserInteraction(_:isEnabled:)

<sub>Instance Method</sub>

Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityRespondsToUserInteraction(_ respondsToUserInteraction: Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Parameters

- `respondsToUserInteraction` — Whether the view responds to user interaction.

- `isEnabled` — If true the accessibility interaction state is applied; otherwise the accessibility interaction state is unchanged.

## Discussion

If this is not set, the value is inferred from the traits of the Accessibility element, the presence of Accessibility actions on the element, or the presence of gestures on the element or containing views.

## See Also

### Managing interactivity

- [accessibilityRespondsToUserInteraction(_:)](<accessibilityrespondstouserinteraction(__).md>) — Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
