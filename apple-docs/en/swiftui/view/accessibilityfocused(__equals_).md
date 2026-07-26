---
title: 'accessibilityFocused(_:equals:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityfocused(_:equals:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityfocused(_:equals:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityfocused%28_%3Aequals%3A%29.json'
content_hash: 'sha256:ced2ddf0b64e0d37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityFocused(_:equals:)

<sub>Instance Method</sub>

Modifies this view by binding its accessibility element’s focus state to the given state value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityFocused<Value>(_ binding: AccessibilityFocusState<Value>.Binding, equals value: Value) -> some View where Value : Hashable

```

## Parameters

- `binding` — The state binding to register. When accessibility focus moves to the accessibility element of the modified view, SwiftUI sets the bound value to the corresponding match value. If you set the state value programmatically to the matching value, then accessibility focus moves to the accessibility element of the modified view. SwiftUI sets the value to `nil` if accessibility focus leaves the accessibility element associated with the modified view, and programmatically setting the value to `nil` dismisses focus automatically.

- `value` — The value to match against when determining whether the binding should change.

## Return Value

The modified view.

## See Also

### Controlling focus

- [accessibilityFocused(_:)](<accessibilityfocused(__).md>) — Modifies this view by binding its accessibility element’s focus state to the given boolean state value.
- [AccessibilityFocusState](../accessibilityfocusstate.md) — A property wrapper type that can read and write a value that SwiftUI updates as the focus of any active accessibility technology, such as VoiceOver, changes.
