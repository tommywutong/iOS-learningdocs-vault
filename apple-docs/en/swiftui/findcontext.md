---
title: FindContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/findcontext
source_url: 'https://developer.apple.com/documentation/swiftui/findcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/findcontext.json'
content_hash: 'sha256:ede91b85d204a9a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FindContext

<sub>Structure</sub>

The status of the find navigator for views which support text editing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct FindContext
```

## Overview

Views which support text editing can use this information to implement a a find navigator that is controlled using the modifiers used for controlling the find navigator throughout the rest of SwiftUI.

For example, the following shows a minimal find navigator implementation driven by the find context which falls back to local state if no `isPresented` binding is provided:

```swift
struct FindNavigatorDrivenTextInput: View {
    @State var text: String = ""
    @State var showFindNavigator = false
    @Environment(\.findContext) var findContext
    var body: some View {
        MyTextInputView(text: $text)
            .overlay(alignment: .topTrailing) {
                if let context = findContext &&
                    context.isPresented?.wrappedValue ?? showFindNavigator
                {
                    HStack {
                        FindInputView(text: text)
                        if context.allowedOperations == .findAndReplace {
                            ReplaceInputView(text: $text)
                        }
                        Button("Close") {
                            context.isPresented?.wrappedValue = false
                            showFindNavigator = false
                        }
                    }
                } else {
                    Button("Show Find Navigator") {
                        context.isPresented?.wrappedValue = true
                        showFindNavigator = true
                    }
                }
            }
    }
}
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [isPresented](findcontext/ispresented.md) — A binding controlling if the find navigator is presented, or nil if no binding has been provided via the [findNavigator(isPresented:)](<view/findnavigator(ispresented_).md>) modifier.
- [supportsReplace](findcontext/supportsreplace.md) — If the find navigators in this context should support replacing.

## See Also

### Searching for text in a view

- [findNavigator(isPresented:)](<view/findnavigator(ispresented_).md>) — Programmatically presents the find and replace interface for text editor views.
- [findDisabled(_:)](<view/finddisabled(__).md>) — Prevents find and replace operations in a text editor.
- [replaceDisabled(_:)](<view/replacedisabled(__).md>) — Prevents replace operations in a text editor.
