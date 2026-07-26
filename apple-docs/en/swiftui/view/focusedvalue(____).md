---
title: 'focusedValue(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/focusedvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/focusedvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/focusedvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:4930ee250e87d187'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# focusedValue(_:_:)

<sub>Instance Method</sub>

Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func focusedValue<Value>(_ keyPath: WritableKeyPath<FocusedValues, Value?>, _ value: Value) -> some View

```

## Parameters

- `keyPath` — The key path to associate `value` with when adding it to the existing table of exported focus values.

- `value` — The focus value to export.

## Return Value

A modified representation of this view.

## See Also

### Exposing value types to focused views

- [focusedValue(_:)](<focusedvalue(__).md>) — Sets the focused value for the given object type.
- [focusedSceneValue(_:)](<focusedscenevalue(__).md>) — Sets the focused value for the given object type at a scene-wide scope.
- [focusedSceneValue(_:_:)](<focusedscenevalue(____).md>) — Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
- [FocusedValues](../focusedvalues.md) — A collection of state exported by the focused scene or view and its ancestors.
