---
title: OpenDocumentAction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/opendocumentaction
source_url: 'https://developer.apple.com/documentation/swiftui/opendocumentaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/opendocumentaction.json'
content_hash: 'sha256:63447198224fc42e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# OpenDocumentAction

<sub>Structure</sub>

An action that presents an existing document.

<sub>macOS</sub>

```swift
@MainActor struct OpenDocumentAction
```

## Overview

Use the [openDocument](environmentvalues/opendocument.md) environment value to get the instance of this structure for a given [Environment](environment.md). Then call the instance to present an existing document. You call the instance directly because it defines a [callAsFunction(at:)](<opendocumentaction/callasfunction(at_).md>) method that Swift calls when you call the instance.

For example, you can create a button that opens the document at the specified URL:

```swift
struct OpenDocumentButton: View {
    var url: URL
    @Environment(\.openDocument) private var openDocument

    var body: some View {
        Button(url.deletingPathExtension().lastPathComponent) {
            Task {
                do {
                    try await openDocument(at: url)
                } catch {
                    // Handle error
                }
            }
        }
    }
}
```

The above example uses a `do-catch` statement to handle any errors that the open document action might throw. It also places the action inside a task and awaits the result because the action operates asynchronously.

To present an existing document, your app must define a [DocumentGroup](documentgroup.md) that handles the content type of the specified file. For a document that’s already open, the system brings the existing window to the front. Otherwise, the system opens a new window.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Calling the action

- [callAsFunction(at:)](<opendocumentaction/callasfunction(at_).md>) — Opens the document at the specified file URL.

## See Also

### Opening a document programmatically

- [newDocument](environmentvalues/newdocument.md) — An action in the environment that presents a new document.
- [openDocument](environmentvalues/opendocument.md) — An action in the environment that presents an existing document.
