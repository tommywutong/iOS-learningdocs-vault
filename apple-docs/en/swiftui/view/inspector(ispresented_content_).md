---
title: 'inspector(isPresented:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/inspector(ispresented:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/inspector(ispresented:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/inspector%28ispresented%3Acontent%3A%29.json'
content_hash: 'sha256:3cc8c1fe5a8697f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# inspector(isPresented:content:)

<sub>Instance Method</sub>

Inserts an inspector at the applied position in the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
nonisolated func inspector<V>(isPresented: Binding<Bool>, @ContentBuilder content: () -> V) -> some View where V : View

```

## Parameters

- `isPresented` — A binding to `Bool` controlling the presented state.

- `content` — The inspector content.

## Discussion

Apply this modifier to declare an inspector with a context-dependent presentation. For example, an inspector can present as a trailing column in a horizontally regular size class, but adapt to a sheet in a horizontally compact size class.

```swift
struct ShapeEditor: View {
    @State var presented: Bool = false
    var body: some View {
        MyEditorView()
            .inspector(isPresented: $presented) {
                TextTraitsInspectorView()
            }
    }
}
```

> [!note] Note
> Trailing column inspectors have their presentation state restored by the framework.

> [!info] See Also
> [InspectorCommands](../inspectorcommands.md) for including the default inspector commands and keyboard shortcuts.

## See Also

### Presenting an inspector

- [inspectorColumnWidth(_:)](<inspectorcolumnwidth(__).md>) — Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.
- [inspectorColumnWidth(min:ideal:max:)](<inspectorcolumnwidth(min_ideal_max_).md>) — Sets a flexible, preferred width for the inspector in a trailing-column presentation.
