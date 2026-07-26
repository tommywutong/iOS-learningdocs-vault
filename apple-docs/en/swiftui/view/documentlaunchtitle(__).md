---
title: 'documentLaunchTitle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/documentlaunchtitle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/documentlaunchtitle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/documentlaunchtitle%28_%3A%29.json'
content_hash: 'sha256:12c0cfe37a22ecdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# documentLaunchTitle(_:)

<sub>Instance Method</sub>

Sets the title displayed on the document launch card.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated func documentLaunchTitle(_ title: Text) -> some View

```

## Parameters

- `title` — The title to display.

## Discussion

Use this modifier to override the default launch-card title, which is the application name. Apply the modifier to a [DocumentLaunchView](../documentlaunchview.md) or any of its ancestors.

## See Also

### Configuring the document launch experience

- [DocumentGroupLaunchScene](../documentgrouplaunchscene.md) — A launch scene for document-based applications.
- [documentLaunchTitle(_:)](<../scene/documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [documentLaunchSubtitle(_:)](<../scene/documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_
- [DocumentLaunchView](../documentlaunchview.md) — A view to present when launching document-related user experience.
- [documentLaunchSubtitle(_:)](<documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_
- [documentBrowserContextMenu(_:)](<documentbrowsercontextmenu(__).md>) — Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [DocumentLaunchGeometryProxy](../documentlaunchgeometryproxy.md) — A proxy for access to the frame of the scene and its title view.
- [DefaultDocumentGroupLaunchActions](../defaultdocumentgrouplaunchactions.md) — The default actions for the document group launch scene and the document launch view.
- [NewDocumentButton](../newdocumentbutton.md) — A button that creates and opens new documents.
- [DefaultNewDocumentButtonLabel](../defaultnewdocumentbuttonlabel.md) — The default label used for a new document button. _(beta)_
- [DocumentCreationSource](../documentcreationsource.md) — Describes the source used to create a new document. _(beta)_
