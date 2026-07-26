---
title: 'init(text:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/texteditor/init(text:)'
source_url: 'https://developer.apple.com/documentation/swiftui/texteditor/init(text:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/texteditor/init%28text%3A%29.json'
content_hash: 'sha256:455aa56198818caf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextEditor](../texteditor.md)

# init(text:)

<sub>Initializer</sub>

Creates a plain text editor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(text: Binding<String>)
```

## Parameters

- `text` — A [Binding](../binding.md) to the variable containing the text to edit.

## Discussion

Use a [TextEditor](../texteditor.md) instance to create a view in which users can enter and edit long-form text.

In this example, the text editor renders gray text using the 13 point Helvetica Neue font with 5 points of spacing between each line:

```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."

    var body: some View {
        TextEditor(text: $fullText)
            .foregroundColor(Color.gray)
            .font(.custom("HelveticaNeue", size: 13))
            .lineSpacing(5)
    }
}
```

You can define the styling for the text within the view, including the text color, font, and line spacing. You define these styles by applying standard view modifiers to the view.

The default text editor doesn’t support rich text, such as styling of individual elements within the editor’s view. The styles you set apply globally to all text in the view.
