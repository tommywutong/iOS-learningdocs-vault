---
title: DocumentLaunchView
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/documentlaunchview
source_url: 'https://developer.apple.com/documentation/swiftui/documentlaunchview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentlaunchview.json'
content_hash: 'sha256:b69a1e46282dc96b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DocumentLaunchView

<sub>Structure</sub>

A view to present when launching document-related user experience.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated struct DocumentLaunchView<Actions, DocumentView> where Actions : View, DocumentView : View
```

## Overview

> [!important] Important
> To create new documents, set [UISupportsDocumentBrowser](../bundleresources/information-property-list/uisupportsdocumentbrowser.md) to `YES` in your app’s information property list. Without this key, document creation doesn’t work.

Configure `DocumentLaunchView` to open and display files and trigger custom actions.

For example, an application that offers writing books can present the `DocumentLaunchView` as its launch view:

```swift
public import UniformTypeIdentifiers

struct BookEditorLaunchView: View {

    var body: some View {
        DocumentLaunchView(for: [.book]) {
            NewDocumentButton("Start New Book")
        } onDocumentOpen: { url in
            BookEditor(url)
        }
    }
}

struct BookEditor: View {
    init(_ url: URL) { }
}

extension UTType {
    static let book = UTType(exportedAs: "com.example.bookEditor")
}
```

> [!note] Note
> An alternative to `DocumentLaunchView` is a scene variant of this API: [DocumentGroupLaunchScene](documentgrouplaunchscene.md). If the app definition contains `DocumentGroup` scenes, consider using a `DocumentGroupLaunchScene` instead of this view.

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a launch view with a background view

- [init(_:for:_:onDocumentOpen:)](<documentlaunchview/init(__for___ondocumentopen_).md>) — Creates a view to present when launching document-related user experiences using a localized title and custom actions.
- [init(_:for:_:onDocumentOpen:background:)](<documentlaunchview/init(__for___ondocumentopen_background_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background view.
- [init(_:for:_:onDocumentOpen:background:backgroundAccessoryView:)](<documentlaunchview/init(__for___ondocumentopen_background_backgroundaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and a background accessory view.
- [init(_:for:_:onDocumentOpen:background:backgroundAccessoryView:overlayAccessoryView:)](<documentlaunchview/init(__for___ondocumentopen_background_backgroundaccessoryview_overlayaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and accessory views.
- [init(_:for:_:onDocumentOpen:background:overlayAccessoryView:)](<documentlaunchview/init(__for___ondocumentopen_background_overlayaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background view, and an overlay accessory view.
- [init(_:for:_:onDocumentOpen:backgroundAccessoryView:)](<documentlaunchview/init(__for___ondocumentopen_backgroundaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background accessory view.
- [init(_:for:_:onDocumentOpen:backgroundAccessoryView:overlayAccessoryView:)](<documentlaunchview/init(__for___ondocumentopen_backgroundaccessoryview_overlayaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, and accessory views.
- [init(_:for:_:onDocumentOpen:overlayAccessoryView:)](<documentlaunchview/init(__for___ondocumentopen_overlayaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, and an overlay accessory view.

### Creating a launch view with a background style

- [init(_:for:backgroundStyle:_:onDocumentOpen:)](<documentlaunchview/init(__for_backgroundstyle___ondocumentopen_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, and a background style.
- [init(_:for:backgroundStyle:_:onDocumentOpen:backgroundAccessoryView:)](<documentlaunchview/init(__for_backgroundstyle___ondocumentopen_backgroundaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and a background accessory view.
- [init(_:for:backgroundStyle:_:onDocumentOpen:backgroundAccessoryView:overlayAccessoryView:)](<documentlaunchview/init(__for_backgroundstyle___ondocumentopen_backgroundaccessoryview_overlayaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and accessory views.
- [init(_:for:backgroundStyle:_:onDocumentOpen:overlayAccessoryView:)](<documentlaunchview/init(__for_backgroundstyle___ondocumentopen_overlayaccessoryview_).md>) — Creates a view to present when launching document-related user experiences using a localized title, custom actions, a background style, and an overlay accessory view.

### Displaying the launch view

- [body](documentlaunchview/body.md) — The body of the view.

## See Also

### Configuring the document launch experience

- [DocumentGroupLaunchScene](documentgrouplaunchscene.md) — A launch scene for document-based applications.
- [documentLaunchTitle(_:)](<scene/documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [documentLaunchSubtitle(_:)](<scene/documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_
- [documentLaunchTitle(_:)](<view/documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [documentLaunchSubtitle(_:)](<view/documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_
- [documentBrowserContextMenu(_:)](<view/documentbrowsercontextmenu(__).md>) — Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [DocumentLaunchGeometryProxy](documentlaunchgeometryproxy.md) — A proxy for access to the frame of the scene and its title view.
- [DefaultDocumentGroupLaunchActions](defaultdocumentgrouplaunchactions.md) — The default actions for the document group launch scene and the document launch view.
- [NewDocumentButton](newdocumentbutton.md) — A button that creates and opens new documents.
- [DefaultNewDocumentButtonLabel](defaultnewdocumentbuttonlabel.md) — The default label used for a new document button. _(beta)_
- [DocumentCreationSource](documentcreationsource.md) — Describes the source used to create a new document. _(beta)_
