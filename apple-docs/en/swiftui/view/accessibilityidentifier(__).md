---
title: 'accessibilityIdentifier(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityidentifier(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityidentifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityidentifier%28_%3A%29.json'
content_hash: 'sha256:21bfe32d5aa36475'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityIdentifier(_:)

<sub>Instance Method</sub>

Uses the string you specify to identify the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityIdentifier(_ identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Discussion

Use this value for testing. It isn’t visible to the user.

## See Also

### Identifying elements

- [accessibilityIdentifier(_:isEnabled:)](<accessibilityidentifier(__isenabled_).md>) — Uses the string you specify to identify the view.
