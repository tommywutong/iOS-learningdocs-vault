---
title: 'accessibilityRespondsToUserInteraction(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityrespondstouserinteraction(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityrespondstouserinteraction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityrespondstouserinteraction%28_%3A%29.json'
content_hash: 'sha256:fe9ef156542cff83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityRespondsToUserInteraction(_:)

<sub>Instance Method</sub>

Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityRespondsToUserInteraction(_ respondsToUserInteraction: Bool = true) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Discussion

If this is not set, the value is inferred from the traits of the Accessibility element, the presence of Accessibility actions on the element, or the presence of gestures on the element or containing views.

## See Also

### Managing interactivity

- [accessibilityRespondsToUserInteraction(_:isEnabled:)](<accessibilityrespondstouserinteraction(__isenabled_).md>) — Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
