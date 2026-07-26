---
title: 'accessibilityHint(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityhint(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityhint(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityhint%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:8cb33e5c7e35bff8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityHint(_:isEnabled:)

<sub>Instance Method</sub>

Communicates to the user what happens after performing the view’s action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityHint(_ hint: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Parameters

- `hint` — The accessibility hint to apply.

- `isEnabled` — If true the accessibility hint is applied; otherwise the accessibility hint is unchanged.

## Discussion

Provide a hint in the form of a brief phrase, like “Purchases the item” or “Downloads the attachment”.

## See Also

### Offering hints

- [accessibilityHint(_:)](<accessibilityhint(__).md>) — Communicates to the user what happens after performing the view’s action.
