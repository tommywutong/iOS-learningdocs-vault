---
title: NewDocumentButton
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/newdocumentbutton
source_url: 'https://developer.apple.com/documentation/swiftui/newdocumentbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/newdocumentbutton.json'
content_hash: 'sha256:882fa33fb254bda2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NewDocumentButton

<sub>Structure</sub>

A button that creates and opens new documents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct NewDocumentButton<Label> where Label : View
```

## Overview

Use a new document button to give people the option to create documents in your app. In the following example, there are two new document buttons, both support [Text](text.md) labels. When the user taps or clicks the first button, the system creates a new document in the directory currently open in the document browser. The second button presents a template picker, where a document can be prepopulated or preconfigured using a template.

```swift
@State private var isTemplatePickerPresented = false
@State private var documentCreationContinuation:
    CheckedContinuation<TextDocument?, any Error>?

var body: some Scene {
    DocumentGroupLaunchScene("My Documents") {
        NewDocumentButton(Text("Start Writing…"))
        NewDocumentButton(Text("Choose a Template"), for: TextDocument.self) {
            try await withCheckedThrowingContinuation { continuation in
                documentCreationContinuation = continuation
                isTemplatePickerPresented = true
            }
        }
        .fullScreenCover(isPresented: $isTemplatePickerPresented) {
            TemplatePicker(
                continuation: $documentCreationContinuation
            )
        }
    }

    DocumentGroup(newDocument: TextDocument()) { configuration in
        MyDocumentView(document: configuration.$document))
    }
}

struct TemplatePicker: View {
    @Binding var continuation:
        CheckedContinuation<TextDocument?, any Error>?
    @Environment(\.dismiss) var dismiss

    var body: some View {
        VStack {
            Text("Choose a template")
                .font(.title)
            Button("Meeting minutes") {
                let document = makeMeetingMinutes()
                documentCreationContinuation?.resume(returning: document)
                dismiss()
            }
            Button("Letter") {
                let document = makeLetter()
                documentCreationContinuation?.resume(returning: document)
                dismiss()
            }
            Button("Cancel") {
                documentCreationContinuation?.resume(throwing: CancellationError())
                dismiss()
            }
        }
    }

    private func makeMeetingMinutes() -> TextDocument { ... }
    private func makeLetter() -> TextDocument { ... }
}

struct TextDocument: FileDocument { ... }
```

If you don’t provide a custom label, the system provides a button with the default “Create Document” label.

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating and opening a document

- [init(_:contentType:)](<newdocumentbutton/init(__contenttype_).md>) — Creates and opens new documents.
- [init(_:contentType:prepareDocumentURL:)](<newdocumentbutton/init(__contenttype_preparedocumenturl_).md>) — Creates and opens new documents.

### Creating and opening a document with a creation source

- [init(_:contentType:source:)](<newdocumentbutton/init(__contenttype_source_).md>) — Creates and opens new documents, tagging them with a creation source. _(beta)_
- [init(_:contentType:source:_:)](<newdocumentbutton/init(__contenttype_source___).md>) — Creates and opens new URL-based documents from a template picker. _(beta)_
- [init(_:contentType:source:prepareDocumentURL:)](<newdocumentbutton/init(__contenttype_source_preparedocumenturl_).md>) — Creates and opens new URL-based documents from a template picker. _(beta)_

### Deprecated

- [init(_:for:contentType:prepareDocument:)](<newdocumentbutton/init(__for_contenttype_preparedocument_).md>) _(deprecated)_

## See Also

### Configuring the document launch experience

- [DocumentGroupLaunchScene](documentgrouplaunchscene.md) — A launch scene for document-based applications.
- [documentLaunchTitle(_:)](<scene/documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [documentLaunchSubtitle(_:)](<scene/documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_
- [DocumentLaunchView](documentlaunchview.md) — A view to present when launching document-related user experience.
- [documentLaunchTitle(_:)](<view/documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [documentLaunchSubtitle(_:)](<view/documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_
- [documentBrowserContextMenu(_:)](<view/documentbrowsercontextmenu(__).md>) — Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [DocumentLaunchGeometryProxy](documentlaunchgeometryproxy.md) — A proxy for access to the frame of the scene and its title view.
- [DefaultDocumentGroupLaunchActions](defaultdocumentgrouplaunchactions.md) — The default actions for the document group launch scene and the document launch view.
- [DefaultNewDocumentButtonLabel](defaultnewdocumentbuttonlabel.md) — The default label used for a new document button. _(beta)_
- [DocumentCreationSource](documentcreationsource.md) — Describes the source used to create a new document. _(beta)_
