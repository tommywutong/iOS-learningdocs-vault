---
title: 'init(_:contentType:prepareDocumentURL:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/newdocumentbutton/init(_:contenttype:preparedocumenturl:)'
source_url: 'https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:preparedocumenturl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/newdocumentbutton/init%28_%3Acontenttype%3Apreparedocumenturl%3A%29.json'
content_hash: 'sha256:8ad31ac7607e9fb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NewDocumentButton](../newdocumentbutton.md)

# init(_:contentType:prepareDocumentURL:)

<sub>Initializer</sub>

Creates and opens new documents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ title: LocalizedStringResource, contentType: UTType, prepareDocumentURL: @escaping () async throws -> URL? = { nil })
```

## Parameters

- `contentType` — A content type of the document to create.

- `prepareDocumentURL` — A closure that is called when a user presses the button. At this point, you can present a document template picker or another UI that allows users to choose a theme, configuration, or a template to create a document from. Return a prepared document, or throw an error if document creation failed. Return `nil` to request creation of an empty document.

## Discussion

This initializer allows presenting a template picker, where a document can be prepopulated or preconfigured using a template.

```swift
@State private var isTemplatePickerPresented = false
@State private var documentCreationContinuation:
    CheckedContinuation<URL?, any Error>?

var body: some Scene {
    DocumentGroupLaunchScene("My Documents") {
        NewDocumentButton("Start Writing…")
        NewDocumentButton("Choose a Template") {
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
        CheckedContinuation<URL?, any Error>?
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

    private func makeMeetingMinutes() -> URL { ... }
    private func makeLetter() -> URL { ... }
}
```

## See Also

### Creating and opening a document

- [init(_:contentType:)](<init(__contenttype_).md>) — Creates and opens new documents.
