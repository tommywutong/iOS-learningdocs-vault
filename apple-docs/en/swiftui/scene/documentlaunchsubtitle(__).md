---
title: 'documentLaunchSubtitle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/scene/documentlaunchsubtitle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/documentlaunchsubtitle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/documentlaunchsubtitle%28_%3A%29.json'
content_hash: 'sha256:3d7bbe61603a6a1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# documentLaunchSubtitle(_:)

<sub>Instance Method</sub>

Sets the subtitle displayed beneath the title on the document launch card.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated func documentLaunchSubtitle(_ subtitle: Text) -> some Scene

```

## Parameters

- `subtitle` — The subtitle to display.

## Discussion

Use this modifier to add descriptive text beneath the launch card title. Apply the modifier to a [DocumentGroupLaunchScene](../documentgrouplaunchscene.md) or any of its ancestors.

## See Also

### Configuring the document launch experience

- [DocumentGroupLaunchScene](../documentgrouplaunchscene.md) — A launch scene for document-based applications.
- [documentLaunchTitle(_:)](<documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [DocumentLaunchView](../documentlaunchview.md) — A view to present when launching document-related user experience.
- [documentLaunchTitle(_:)](<../view/documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [documentLaunchSubtitle(_:)](<../view/documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_
- [documentBrowserContextMenu(_:)](<../view/documentbrowsercontextmenu(__).md>) — Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [DocumentLaunchGeometryProxy](../documentlaunchgeometryproxy.md) — A proxy for access to the frame of the scene and its title view.
- [DefaultDocumentGroupLaunchActions](../defaultdocumentgrouplaunchactions.md) — The default actions for the document group launch scene and the document launch view.
- [NewDocumentButton](../newdocumentbutton.md) — A button that creates and opens new documents.
- [DefaultNewDocumentButtonLabel](../defaultnewdocumentbuttonlabel.md) — The default label used for a new document button. _(beta)_
- [DocumentCreationSource](../documentcreationsource.md) — Describes the source used to create a new document. _(beta)_
