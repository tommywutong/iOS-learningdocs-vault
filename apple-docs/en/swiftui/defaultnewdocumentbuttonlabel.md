---
title: DefaultNewDocumentButtonLabel
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/defaultnewdocumentbuttonlabel
source_url: 'https://developer.apple.com/documentation/swiftui/defaultnewdocumentbuttonlabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/defaultnewdocumentbuttonlabel.json'
content_hash: 'sha256:215d7201d0deda18'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DefaultNewDocumentButtonLabel

<sub>Structure</sub>

The default label used for a new document button.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct DefaultNewDocumentButtonLabel
```

## Overview

You don’t use this type directly. Instead, [NewDocumentButton](newdocumentbutton.md) uses it automatically depending on how you create a button.

## Relationships

- **Conforms To**: [View](view.md)

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
- [DocumentCreationSource](documentcreationsource.md) — Describes the source used to create a new document. _(beta)_
