---
title: 'renameAction(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/renameaction(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/renameaction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/renameaction%28_%3A%29.json'
content_hash: 'sha256:e0f443ab0710fbe0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# renameAction(_:)

<sub>Instance Method</sub>

Sets a closure to run for the rename action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func renameAction(_ action: @escaping () -> Void) -> some View

```

## Parameters

- `action` — A closure to run when renaming.

## Return Value

A view that has the specified rename action.

## Discussion

Use this modifier in conjunction with the [RenameButton](../renamebutton.md) to implement standard rename interactions. A rename button receives its action from the environment. Use this modifier to customize the action provided to the rename button.

```swift
struct RowView: View {
    @State private var text = ""
    @FocusState private var isFocused: Bool

    var body: some View {
        TextField(text: $item.name) {
            Text("Prompt")
        }
        .focused($isFocused)
        .contextMenu {
            RenameButton()
            // ... your own custom actions
        }
        .renameAction { isFocused = true }
}
```

When the user taps the rename button in the context menu, the rename action focuses the text field by setting the `isFocused` property to true.

## See Also

### Renaming a document

- [RenameButton](../renamebutton.md) — A button that triggers a standard rename action.
- [rename](../environmentvalues/rename.md) — An action that activates the standard rename interaction.
- [RenameAction](../renameaction.md) — An action that activates a standard rename interaction.
