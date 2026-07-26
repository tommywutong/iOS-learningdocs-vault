---
title: Customizing the document browser
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/customizing-the-browser
source_url: 'https://developer.apple.com/documentation/uikit/customizing-the-browser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/customizing-the-browser.json'
content_hash: 'sha256:1ccbde8dc9f6d171'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [Adding a document browser to your app](adding-a-document-browser-to-your-app.md)

# Customizing the document browser

<sub>Article</sub>

Customize the document browser’s look and behavior.

## Overview

You can set the browser’s appearance, create document thumbnails, and modify the browser’s behavior.

### Set the browser’s appearance

Change the browser’s appearance by setting the [browserUserInterfaceStyle](uidocumentbrowserviewcontroller/browseruserinterfacestyle-swift.property.md) property. The document browser view controller supports white, light, and dark appearances.

### Create document thumbnails or icons

The system automatically provides thumbnails or icons for supported document types. If your app uses a custom or third-party document type, you can create a Thumbnail extension for that type. For more information, see [QLThumbnailProvider](../quicklookthumbnailing/qlthumbnailprovider.md).

If you don’t provide a Thumbnail extension, the system can create a document icon based on your app icon. To enable automatic icon creation, go to the Project navigator, choose the target, click Info, and then do the following:

1. Declare support for the document’s Uniform Type Identifier in the Document Type section.
2. For any custom document types that you create, export the Uniform Type Identifier in the Exported Type Identifiers section.
3. For any third-party document types used by your app, import the Uniform Type Identifier in the Imported Type Identifiers section.

For more information, see [Set the supported document types](setting-up-a-document-browser-app.md#Set-the-supported-document-types).

Your app’s icon only appears in the Files app or document browser when all of the following are true:

- The system doesn’t automatically provide a thumbnail for the Uniform Type Identifier.
- The system doesn’t already provide an icon for the Uniform Type Identifier.
- The user hasn’t installed a Thumbnail extension for the Uniform Type Identifier.
- Your app both declares document type support for the Uniform Type Identifier and declares it as an exported or imported type.

### Add document previews

The system automatically provides previews for supported document types. If your app uses a custom or third-party document type, you can create a Preview extension for that type.

For more information, see [Quick Look](../quartz/quick-look.md).

### Modify the browser’s behavior

You can control the following behaviors:

- The type of documents the browser opens
- Whether the browser opens multiple files at the same time
- Whether the browser creates new documents

#### Set allowed document types

You set the list of allowed document types when you create the browser. Pass an array of Uniform Type Identifier strings to the [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) class’s [- initForOpeningFilesWithContentTypes:](<uidocumentbrowserviewcontroller/init(foropeningfileswithcontenttypes_).md>) method. If you pass `nil`, the browser uses the document types specified by the [CFBundleDocumentTypes](../bundleresources/information-property-list/cfbundledocumenttypes.md) key in the app’s `Info.plist` file.

For detailed instructions on setting the [CFBundleDocumentTypes](../bundleresources/information-property-list/cfbundledocumenttypes.md) key, see [Set the supported document types](setting-up-a-document-browser-app.md#Set-the-supported-document-types).

The following example programmatically creates a document browser for `.txt` files:

```swift
let browser = UIDocumentBrowserViewController(forOpeningFilesWithContentTypes: ["public.plain-text"])
```

#### Enable multiple document selection

By default, users can select only one item at a time. To enable multiple document selection, set the document browser’s [allowsPickingMultipleItems](uidocumentbrowserviewcontroller/allowspickingmultipleitems.md) property to [true](../swift/true.md).

#### Enable new document creation

To let users create new documents, you must do the following:

- Set the browser’s [allowsDocumentCreation](uidocumentbrowserviewcontroller/allowsdocumentcreation.md) property to [true](../swift/true.md) (the default value).
- Implement the [UIDocumentBrowserViewControllerDelegate](uidocumentbrowserviewcontrollerdelegate.md) object’s [- documentBrowser:didRequestDocumentCreationWithHandler:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didrequestdocumentcreationwithhandler_).md>) method.

After these steps are completed, the system automatically includes an Add button (+) in the document browser’s navigation bar.

When the user taps the Add button, the system calls the [- documentBrowser:didRequestDocumentCreationWithHandler:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didrequestdocumentcreationwithhandler_).md>) method. In your implementation, you can present a custom user interface, where users can configure the document. For example, you might show a list of document templates.

Create a new document and save it to a temporary location. As soon as the document is saved, call the provided `importHandler`. To confirm the request, pass in the document’s temporary URL and the import mode ([UIDocumentBrowserImportModeCopy](uidocumentbrowserviewcontroller/importmode/copy.md) or [UIDocumentBrowserImportModeMove](uidocumentbrowserviewcontroller/importmode/move.md)). To cancel the request, pass `nil` and [UIDocumentBrowserImportModeNone](uidocumentbrowserviewcontroller/importmode/none.md).

> [!important] Important
> You must always call the `importHandler`. If you can’t create a new document, pass `nil` for the URL and [UIDocumentBrowserImportModeNone](uidocumentbrowserviewcontroller/importmode/none.md) for the import mode.

## See Also

### Customization

- [Adding custom actions and activities](adding-custom-actions-and-activities.md) — Add custom document browser actions, activities, and bar items.
