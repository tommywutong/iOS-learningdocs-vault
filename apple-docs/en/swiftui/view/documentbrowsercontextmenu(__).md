---
title: 'documentBrowserContextMenu(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.1+, iPadOS 18.1+, Mac Catalyst 18.1+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/documentbrowsercontextmenu(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/documentbrowsercontextmenu(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/documentbrowsercontextmenu%28_%3A%29.json'
content_hash: 'sha256:f3f81d8a2464ca3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# documentBrowserContextMenu(_:)

<sub>Instance Method</sub>

Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency func documentBrowserContextMenu(@ContentBuilder _ menu: @escaping ([URL]?) -> some View) -> some View

```

## Parameters

- `menu` — Items representing the content of the menu.

## Discussion

Add `documentBrowserContextMenu` modifier to [DocumentLaunchView](../documentlaunchview.md) to provide additional actions to the document browser items’ context menu. For example, a book editor application could have a “Favorite” button that marks user-chosen books as their favorite. The button enables when the user switches the browser into “Selection” mode.

```swift
import UniformTypeIdentifiers

struct BookEditor: View {

    var body: some View {
        DocumentLaunchView(for: [.book]) {
            NewDocumentButton("Start New Book")
        } onDocumentOpen: { url in
            BookEditor(url)
        }
        .documentBrowserContextMenu { selectedURLs in
            FavoriteBookButton(urls: selectedURLs)
        }
    }
}

struct FavoriteBookButton: View {
    var urls: [URL]?
    var body: some View {
        Button {
            updateFavorite(urls)
        } label: {
            Image(systemName: allFavorite(urls) ? "heart.fill" : "heart")
        }
    }

    func allFavorite(_ urls: [URL]?) -> Bool { ... }
    func updateFavorite(_ urls: [URL]?) { ... }
}

struct BookEditor: View {
    init(_ url: URL) { ... }
}

extension UTType {
    static let book = UTType(exportedAs: "com.example.bookEditor")
}
```

In the example above, the application stores a list of URLs to favorite books, and does not need to access the file on disk. In cases when an application wants to read the contents of the URL from the disk or associated metadata, it should call `URL.startAccessingSecurityScopedResource()` to gain access to the resource, and `URL.stopAccessingSecurityScopedResource()` to relinquish access when it is not needed.

The actions are displayed in the document browser navigation bar when a document browser is in Select mode, and also added to context menu for the file items.

## See Also

### Configuring the document launch experience

- [DocumentGroupLaunchScene](../documentgrouplaunchscene.md) — A launch scene for document-based applications.
- [documentLaunchTitle(_:)](<../scene/documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [documentLaunchSubtitle(_:)](<../scene/documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_
- [DocumentLaunchView](../documentlaunchview.md) — A view to present when launching document-related user experience.
- [documentLaunchTitle(_:)](<documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [documentLaunchSubtitle(_:)](<documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_
- [DocumentLaunchGeometryProxy](../documentlaunchgeometryproxy.md) — A proxy for access to the frame of the scene and its title view.
- [DefaultDocumentGroupLaunchActions](../defaultdocumentgrouplaunchactions.md) — The default actions for the document group launch scene and the document launch view.
- [NewDocumentButton](../newdocumentbutton.md) — A button that creates and opens new documents.
- [DefaultNewDocumentButtonLabel](../defaultnewdocumentbuttonlabel.md) — The default label used for a new document button. _(beta)_
- [DocumentCreationSource](../documentcreationsource.md) — Describes the source used to create a new document. _(beta)_
