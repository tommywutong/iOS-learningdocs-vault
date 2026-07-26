---
title: 'accessibilityValue(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityvalue(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityvalue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityvalue%28_%3A%29.json'
content_hash: 'sha256:395626266b8353c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityValue(_:)

<sub>Instance Method</sub>

Adds a textual description of the value that the view contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityValue(_ valueResource: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Discussion

Use this method to describe the value represented by a view, but only if that’s different than the view’s label. For example, for a slider that you label as “Volume” using accessibilityLabel(), you can provide the current volume setting, like “60%”, using accessibilityValue().

## See Also

### Describing values

- [accessibilityValue(_:isEnabled:)](<accessibilityvalue(__isenabled_).md>) — Adds a textual description of the value that the view contains.
