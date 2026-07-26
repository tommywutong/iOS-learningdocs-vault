---
title: DocumentCreationSource
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/documentcreationsource
source_url: 'https://developer.apple.com/documentation/swiftui/documentcreationsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentcreationsource.json'
content_hash: 'sha256:488b15ae97818f0a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DocumentCreationSource

<sub>Structure</sub>

Describes the source used to create a new document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct DocumentCreationSource
```

## Overview

On iOS, you can declare custom creation sources and use them in [NewDocumentButton](newdocumentbutton.md).

```swift
extension DocumentCreationSource {
    static let scanner: Self =
        DocumentCreationSource(id: "document-from-scanner")

    static let template: Self =
        DocumentCreationSource(id: "document-from-template")
}

DocumentGroupLaunchScene("Documents") {
    NewDocumentButton("Scan Document", source: .scanner)
    NewDocumentButton("New from Template", source: .template)
}
```

When a document is created, you can retrieve its source from [URLDocumentConfiguration](urldocumentconfiguration.md) or [FileDocumentConfiguration](filedocumentconfiguration.md):

```swift
DocumentGroup(newDocument: { MyDocument() }) { configuration in
    if configuration.creationSource == .template {
        TemplateSetupView()
    }
}
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a source

- [init(id:)](<documentcreationsource/init(id_).md>) — Creates a document creation source with the given identifier. _(beta)_

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
- [NewDocumentButton](newdocumentbutton.md) — A button that creates and opens new documents.
- [DefaultNewDocumentButtonLabel](defaultnewdocumentbuttonlabel.md) — The default label used for a new document button. _(beta)_
