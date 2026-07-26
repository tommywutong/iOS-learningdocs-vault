---
title: AttributedTextFormatting.Transferable
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/attributedtextformatting/transferable
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformatting/transferable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformatting/transferable.json'
content_hash: 'sha256:b48ee99e92b8789a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AttributedTextFormatting](../attributedtextformatting.md)

# AttributedTextFormatting.Transferable

<sub>Structure</sub>

A transferable representation of an attributed string interpreted in a SwiftUI environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Transferable
```

## Overview

Use this type e.g. with drag and drop APIs or to create a [fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)](<../view/fileexporter(ispresented_item_contenttypes_defaultfilename_oncompletion_oncancellation_).md>).

```swift
struct RichTextEditorView: View {
    @State private var text: AttributedString = ""
    @Environment(\.self) private var environment
    @State var fileExporterIsPresented: Bool = false

    var body: some View {
        TextEditor(text: $text)
            .toolbar {
                Button("Save") {
                    fileExporterIsPresented = true
                }
            }
            .fileExporter(
                isPresented: $fileExporterIsPresented,
                item: AttributedTextFormatting.Transferable(text: text, in: environment)
            ) { result in
                handleResult(result)
            }
            .dropDestination(
                for: AttributedTextFormatting.Transferable.self
            ) { transferables, _ in
                text.replaceSelection(
                    &selection,
                    with: transferables.map {
                        AttributedString(transferable: $0, in: environment)
                    }.joined(separator: AttributedString("\n")))
                return true
            }
    }
}
```

To extract text the text after importing, use attributed string’s `Foundation/AttributedString/init(transferable:in:)`.

Supported content types include:

- [rtfd](../../uniformtypeidentifiers/uttype-swift.struct/rtfd.md)
- [rtf](../../uniformtypeidentifiers/uttype-swift.struct/rtf.md)

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [Transferable](../../coretransferable/transferable.md)

## Topics

### Initializers

- [init(text:in:)](<transferable/init(text_in_).md>) — Create a transferable representation of an attributed string as interpreted in a SwiftUI environment.
