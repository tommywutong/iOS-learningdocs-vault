---
title: DocumentLaunchGeometryProxy
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/documentlaunchgeometryproxy
source_url: 'https://developer.apple.com/documentation/swiftui/documentlaunchgeometryproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentlaunchgeometryproxy.json'
content_hash: 'sha256:5391f57c0b43f37c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DocumentLaunchGeometryProxy

<sub>Structure</sub>

A proxy for access to the frame of the scene and its title view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct DocumentLaunchGeometryProxy
```

## Topics

### Getting the geometry

- [frame](documentlaunchgeometryproxy/frame.md) — Frame of the document launch interface.
- [titleViewFrame](documentlaunchgeometryproxy/titleviewframe.md) — Frame of the title view within the interface.

## See Also

### Configuring the document launch experience

- [DocumentGroupLaunchScene](documentgrouplaunchscene.md) — A launch scene for document-based applications.
- [documentLaunchTitle(_:)](<scene/documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [documentLaunchSubtitle(_:)](<scene/documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_
- [DocumentLaunchView](documentlaunchview.md) — A view to present when launching document-related user experience.
- [documentLaunchTitle(_:)](<view/documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [documentLaunchSubtitle(_:)](<view/documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_
- [documentBrowserContextMenu(_:)](<view/documentbrowsercontextmenu(__).md>) — Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [DefaultDocumentGroupLaunchActions](defaultdocumentgrouplaunchactions.md) — The default actions for the document group launch scene and the document launch view.
- [NewDocumentButton](newdocumentbutton.md) — A button that creates and opens new documents.
- [DefaultNewDocumentButtonLabel](defaultnewdocumentbuttonlabel.md) — The default label used for a new document button. _(beta)_
- [DocumentCreationSource](documentcreationsource.md) — Describes the source used to create a new document. _(beta)_
