---
title: 'focusedSceneValue(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/focusedscenevalue(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/focusedscenevalue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/focusedscenevalue%28_%3A%29.json'
content_hash: 'sha256:023aa14bebfaf74f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# focusedSceneValue(_:)

<sub>Instance Method</sub>

Sets the focused value for the given object type at a scene-wide scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func focusedSceneValue<T>(_ object: T?) -> some View where T : AnyObject, T : Observable

```

## Discussion

> [!important] Important
> This initializer only accepts objects conforming to the `Observable` protocol. For reading environment objects that conform to `ObservableObject`, use `focusedObject(_:)`, instead.

To read this value, use the `FocusedValue` property wrapper.

## See Also

### Exposing value types to focused views

- [focusedValue(_:)](<focusedvalue(__).md>) — Sets the focused value for the given object type.
- [focusedValue(_:_:)](<focusedvalue(____).md>) — Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [focusedSceneValue(_:_:)](<focusedscenevalue(____).md>) — Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
- [FocusedValues](../focusedvalues.md) — A collection of state exported by the focused scene or view and its ancestors.
