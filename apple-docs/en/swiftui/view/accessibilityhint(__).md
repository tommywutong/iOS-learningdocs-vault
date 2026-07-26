---
title: 'accessibilityHint(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityhint(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityhint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityhint%28_%3A%29.json'
content_hash: 'sha256:a8d37e59fa210471'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityHint(_:)

<sub>Instance Method</sub>

Communicates to the user what happens after performing the view’s action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityHint(_ hint: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Discussion

Provide a hint in the form of a brief phrase, like “Purchases the item” or “Downloads the attachment”.

## See Also

### Offering hints

- [accessibilityHint(_:isEnabled:)](<accessibilityhint(__isenabled_).md>) — Communicates to the user what happens after performing the view’s action.
