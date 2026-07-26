---
title: 'focusedSceneValue(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/focusedscenevalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/focusedscenevalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/focusedscenevalue%28_%3A_%3A%29.json'
content_hash: 'sha256:e6ffedd22f14ffe3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# focusedSceneValue(_:_:)

<sub>Instance Method</sub>

Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func focusedSceneValue<T>(_ keyPath: WritableKeyPath<FocusedValues, T?>, _ value: T) -> some View

```

## Parameters

- `keyPath` — The key path to associate `value` with when adding it to the existing table of published focus values.

- `value` — The focus value to publish.

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of [focusedValue(_:_:)](<focusedvalue(____).md>) for values that must be visible regardless of where focus is located in the active scene. For example, if an app needs a command for moving focus to a particular text field in the sidebar, it could use this modifier to publish a button action that’s visible to command views as long as the scene is active, and regardless of where focus happens to be in it.

```swift
struct Sidebar: View {
    @FocusState var isFiltering: Bool

    var body: some View {
        VStack {
            TextField(...)
                .focused(when: $isFiltering)
                .focusedSceneValue(\.filterAction) {
                    isFiltering = true
                }
        }
    }
}

struct NavigationCommands: Commands {
    @FocusedValue(\.filterAction) var filterAction

    var body: some Commands {
        CommandMenu("Navigate") {
            Button("Filter in Sidebar") {
                filterAction?()
            }
        }
        .disabled(filterAction == nil)
    }
}

extension FocusedValues {
    @Entry var filterAction: (() -> Void)?
}
```

## See Also

### Exposing value types to focused views

- [focusedValue(_:)](<focusedvalue(__).md>) — Sets the focused value for the given object type.
- [focusedValue(_:_:)](<focusedvalue(____).md>) — Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [focusedSceneValue(_:)](<focusedscenevalue(__).md>) — Sets the focused value for the given object type at a scene-wide scope.
- [FocusedValues](../focusedvalues.md) — A collection of state exported by the focused scene or view and its ancestors.
