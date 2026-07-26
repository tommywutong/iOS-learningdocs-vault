---
title: UIDocumentInteractionController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentinteractioncontroller
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontroller.json'
content_hash: 'sha256:ddc4c00499ddca7e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDocumentInteractionController

<sub>Class</sub>

A view controller that previews, opens, or prints files with a file format that your app can’t handle directly.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIDocumentInteractionController
```

## Overview

Use this class to present an appropriate user interface for previewing, opening, copying, or printing a specified file. For example, an email program might use this class to allow the user to preview attachments and open them in other apps.

After presenting its user interface, a document interaction controller handles all interactions needed to support file preview and menu display.

You can also use the delegate to participate in interactions occurring within the presented interface. For example, the delegate is notified when a file is about to be handed off to another application for opening. For a complete description of the methods you can implement in your delegate, see [UIDocumentInteractionControllerDelegate](uidocumentinteractioncontrollerdelegate.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIActionSheetDelegate](uiactionsheetdelegate.md)

## Topics

### Creating the document interaction controller

- [+ interactionControllerWithURL:](<uidocumentinteractioncontroller/init(url_)-8wb4p.md>) — Creates a document interaction controller with the specified URL.

### Handling document-related interactions

- [delegate](uidocumentinteractioncontroller/delegate.md) — The delegate you want to receive document interaction notifications.
- [UIDocumentInteractionControllerDelegate](uidocumentinteractioncontrollerdelegate.md) — A set of methods you can implement to respond to messages from a document interaction controller.

### Presenting and dismissing a document preview

- [- presentPreviewAnimated:](<uidocumentinteractioncontroller/presentpreview(animated_).md>) — Displays a full-screen preview of the target document.
- [- dismissPreviewAnimated:](<uidocumentinteractioncontroller/dismisspreview(animated_).md>) — Dismisses the currently active document preview.

### Presenting and dismissing menus

- [- presentOptionsMenuFromRect:inView:animated:](<uidocumentinteractioncontroller/presentoptionsmenu(from_in_animated_).md>) — Displays an options menu and anchors it to the specified location in the view.
- [- presentOptionsMenuFromBarButtonItem:animated:](<uidocumentinteractioncontroller/presentoptionsmenu(from_animated_).md>) — Displays an options menu and anchors it to the specified bar button item.
- [- presentOpenInMenuFromRect:inView:animated:](<uidocumentinteractioncontroller/presentopeninmenu(from_in_animated_).md>) — Displays a menu for opening the document and anchors that menu to the specified view.
- [- presentOpenInMenuFromBarButtonItem:animated:](<uidocumentinteractioncontroller/presentopeninmenu(from_animated_).md>) — Displays a menu for opening the document and anchors that menu to the specified bar button item.
- [- dismissMenuAnimated:](<uidocumentinteractioncontroller/dismissmenu(animated_).md>) — Dismisses the currently active menu.

### Accessing the target document’s attributes

- [URL](uidocumentinteractioncontroller/url.md) — The URL identifying the target file on the local filesystem.
- [UTI](uidocumentinteractioncontroller/uti.md) — The type of the target file.
- [name](uidocumentinteractioncontroller/name.md) — The name of the target file.
- [icons](uidocumentinteractioncontroller/icons.md) — The images associated with the target file.
- [annotation](uidocumentinteractioncontroller/annotation.md) — Custom property list information for the target file.

### Accessing the controller attributes

- [gestureRecognizers](uidocumentinteractioncontroller/gesturerecognizers.md) — The system-supplied gesture recognizers for presenting a document interaction controller.

### Initializers

- [init(URL:)](<uidocumentinteractioncontroller/init(url_)-39lrq.md>)

## See Also

### Documents and directories

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md) — Add unique elements to your app’s document launch scene.
- [Adding a document browser to your app](adding-a-document-browser-to-your-app.md) — Give people access to their local or remote documents from within your app.
- [Providing access to directories](providing-access-to-directories.md) — Use a document picker to access the content of a directory outside your app’s container.
- [Building an app with a document browser](building-an-app-with-a-document-browser.md) — Provide access to on-device and cloud files by adding a document browser to your app.
- [Building a document browser app for custom file formats](building-a-document-browser-app-for-custom-file-formats.md) — Implement a custom document file format to manage user interactions with files on different cloud storage providers.
- [UIDocumentViewController](uidocumentviewcontroller.md) — A view controller that manages and presents a document stored locally or in the cloud.
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) — A view controller for browsing and performing actions on documents that you store locally and in the cloud.
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) — A view controller that provides access to documents or destinations outside your app’s sandbox.
