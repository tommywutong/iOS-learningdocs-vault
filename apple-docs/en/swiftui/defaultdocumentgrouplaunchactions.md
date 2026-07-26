---
title: DefaultDocumentGroupLaunchActions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/defaultdocumentgrouplaunchactions
source_url: 'https://developer.apple.com/documentation/swiftui/defaultdocumentgrouplaunchactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/defaultdocumentgrouplaunchactions.json'
content_hash: 'sha256:d7d643ce2f32109a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DefaultDocumentGroupLaunchActions

<sub>Structure</sub>

The default actions for the document group launch scene and the document launch view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated struct DefaultDocumentGroupLaunchActions
```

## Overview

This `View` populates [DocumentGroupLaunchScene](documentgrouplaunchscene.md) and [DocumentLaunchView](documentlaunchview.md) with the default actions.

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating the default launch actions

- [init()](<defaultdocumentgrouplaunchactions/init().md>)

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
- [NewDocumentButton](newdocumentbutton.md) — A button that creates and opens new documents.
- [DefaultNewDocumentButtonLabel](defaultnewdocumentbuttonlabel.md) — The default label used for a new document button. _(beta)_
- [DocumentCreationSource](documentcreationsource.md) — Describes the source used to create a new document. _(beta)_
