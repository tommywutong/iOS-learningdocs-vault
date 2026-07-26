---
title: 'findDisabled(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 26.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/finddisabled(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/finddisabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/finddisabled%28_%3A%29.json'
content_hash: 'sha256:34e9ecdf987e0888'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# findDisabled(_:)

<sub>Instance Method</sub>

Prevents find and replace operations in a text editor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func findDisabled(_ isDisabled: Bool = true) -> some View

```

## Parameters

- `isDisabled` — A Boolean value that indicates whether to disable the find and replace interface for a text editor.

## Return Value

A view that disables the find and replace interface.

## Discussion

Add this modifier to ensure that people can’t activate the find and replace interface for a [TextEditor](../texteditor.md):

```swift
TextEditor(text: $text)
    .findDisabled()
```

When you disable the find operation, you also implicitly disable the replace operation. If you want to only disable replace, use [replaceDisabled(_:)](<replacedisabled(__).md>) instead.

Using this modifer also prevents programmatic find and replace interface presentation using the [findNavigator(isPresented:)](<findnavigator(ispresented_).md>) method. Be sure to place the disabling modifier closer to the text editor for this to work:

```swift
TextEditor(text: $text)
    .findDisabled(isDisabled)
    .findNavigator(isPresented: $isPresented)
```

If you apply this modifer at multiple levels of a view hierarchy, the call closest to the text editor takes precedence. For example, people can activate find and replace for the first text editor in the following example, but not the second:

```swift
VStack {
    TextEditor(text: $text1)
        .findDisabled(false)
    TextEditor(text: $text2)
}
.findDisabled(true)
```

## See Also

### Searching for text in a view

- [findNavigator(isPresented:)](<findnavigator(ispresented_).md>) — Programmatically presents the find and replace interface for text editor views.
- [replaceDisabled(_:)](<replacedisabled(__).md>) — Prevents replace operations in a text editor.
- [FindContext](../findcontext.md) — The status of the find navigator for views which support text editing.
