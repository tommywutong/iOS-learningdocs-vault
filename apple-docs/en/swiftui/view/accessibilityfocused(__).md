---
title: 'accessibilityFocused(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityfocused(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityfocused(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityfocused%28_%3A%29.json'
content_hash: 'sha256:91c9374bdce693fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityFocused(_:)

<sub>Instance Method</sub>

Modifies this view by binding its accessibility element’s focus state to the given boolean state value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityFocused(_ condition: AccessibilityFocusState<Bool>.Binding) -> some View

```

## Parameters

- `condition` — The accessibility focus state to bind. When accessibility focus moves to the accessibility element of the modified view, the focus value is set to `true`. If the value is set to `true` programmatically, then accessibility focus will move to accessibility element of the modified view. The value will be set to `false` if accessibility focus leaves the accessibility element of the modified view, and accessibility focus will be dismissed automatically if the value is set to `false` programmatically.

## Return Value

The modified view.

## See Also

### Controlling focus

- [accessibilityFocused(_:equals:)](<accessibilityfocused(__equals_).md>) — Modifies this view by binding its accessibility element’s focus state to the given state value.
- [AccessibilityFocusState](../accessibilityfocusstate.md) — A property wrapper type that can read and write a value that SwiftUI updates as the focus of any active accessibility technology, such as VoiceOver, changes.
