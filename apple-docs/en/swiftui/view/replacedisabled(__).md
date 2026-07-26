---
title: 'replaceDisabled(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 26.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/replacedisabled(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/replacedisabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/replacedisabled%28_%3A%29.json'
content_hash: 'sha256:62bbc89c2602f047'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# replaceDisabled(_:)

<sub>Instance Method</sub>

Prevents replace operations in a text editor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func replaceDisabled(_ isDisabled: Bool = true) -> some View

```

## Parameters

- `isDisabled` — A Boolean value that indicates whether text replacement in the find and replace interface is disabled.

## Return Value

A view that disables the replace feature of a find and replace interface.

## Discussion

Add this modifier to ensure that people can’t activate the replace feature of a find and replace interface for a [TextEditor](../texteditor.md):

```swift
TextEditor(text: $text)
    .replaceDisabled()
```

If you want to disable both find and replace, use the [findDisabled(_:)](<finddisabled(__).md>) modifier instead.

Using this modifer also disables the replace feature of a find and replace interface that you present programmatically using the [findNavigator(isPresented:)](<findnavigator(ispresented_).md>) method. Be sure to place the disabling modifier closer to the text editor for this to work:

```swift
TextEditor(text: $text)
    .replaceDisabled(isDisabled)
    .findNavigator(isPresented: $isPresented)
```

If you apply this modifer at multiple levels of a view hierarchy, the call closest to the text editor takes precedence. For example, people can activate find and replace for the first text editor in the following example, but only find for the second:

```swift
VStack {
    TextEditor(text: $text1)
        .replaceDisabled(false)
    TextEditor(text: $text2)
}
.replaceDisabled(true)
```

## See Also

### Searching for text in a view

- [findNavigator(isPresented:)](<findnavigator(ispresented_).md>) — Programmatically presents the find and replace interface for text editor views.
- [findDisabled(_:)](<finddisabled(__).md>) — Prevents find and replace operations in a text editor.
- [FindContext](../findcontext.md) — The status of the find navigator for views which support text editing.
