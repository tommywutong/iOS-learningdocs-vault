---
title: 'documentBrowser(_:didRequestDocumentCreationWithHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didrequestdocumentcreationwithhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didrequestdocumentcreationwithhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_%3Adidrequestdocumentcreationwithhandler%3A%29.json'
content_hash: 'sha256:6c84a4f7d9bb534e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewControllerDelegate](../uidocumentbrowserviewcontrollerdelegate.md)

# documentBrowser(_:didRequestDocumentCreationWithHandler:)

<sub>Instance Method</sub>

Asks the delegate to create a new document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func documentBrowser(_ controller: UIDocumentBrowserViewController, didRequestDocumentCreationWithHandler importHandler: @escaping (URL?, UIDocumentBrowserViewController.ImportMode) -> Void)
```

## Parameters

- `controller` — The current document browser.

- `importHandler` — A block that takes the following parameters: - **urlToImport** — The URL of the document’s initial, temporary location. - **importMode** — The mode used when importing the document. For a list of import modes, see [ImportMode](../uidocumentbrowserviewcontroller/importmode.md).

## Discussion

Implement this method to create new documents for the user:

1. (Optional) Display any controls the user needs to configure the document.
2. Create a new document and save it to a temporary location. If you use a [UIDocument](../uidocument.md) subclass to create the document, you must close it before calling the `importHandler` block. Always open a new document in your [- documentBrowser:didImportDocumentAtURL:toDestinationURL:](<documentbrowser(__didimportdocumentat_todestinationurl_).md>) method.
3. Call the provided `importHandler` block. To confirm the request, pass in the document’s temporary URL and the import mode ([UIDocumentBrowserImportModeCopy](../uidocumentbrowserviewcontroller/importmode/copy.md) or [UIDocumentBrowserImportModeMove](../uidocumentbrowserviewcontroller/importmode/move.md)). To cancel the request, pass `nil` and [UIDocumentBrowserImportModeNone](../uidocumentbrowserviewcontroller/importmode/none.md).
4. Implement the [- documentBrowser:didImportDocumentAtURL:toDestinationURL:](<documentbrowser(__didimportdocumentat_todestinationurl_).md>) method. In this method, open the document at the destination URL. You must use either a [UIDocument](../uidocument.md) subclass, or a file presenter and file coordination.
5. Modally present this document to the user.

> [!important] Important
> You must always call the import handler. If you cannot create a new document, pass `nil` for the URL and [UIDocumentBrowserImportModeNone](../uidocumentbrowserviewcontroller/importmode/none.md) for the import mode.

The following example shows a possible implementation of the  [- documentBrowser:didRequestDocumentCreationWithHandler:](<documentbrowser(__didrequestdocumentcreationwithhandler_).md>) method.

```swift
// Create New Document
func documentBrowser(_ controller: UIDocumentBrowserViewController, didRequestDocumentCreationWithHandler importHandler: @escaping (URL?, UIDocumentBrowserViewController.ImportMode) -> Void) {
        
    let doc = // Create a new UIDocument... 
    let url = // Get a temporary URL...
    
    // Create a new document in a temporary location
    doc.save(to: url, for: .forCreating) { (saveSuccess) in
        
        // Make sure the document saved successfully
        guard saveSuccess else {            
            // Cancel document creation
            importHandler(nil, .none)
            return
        }
        
        // Close the document.
        doc.close(completionHandler: { (closeSuccess) in
            
            // Make sure the document closed successfully
            guard closeSuccess else {                
                // Cancel document creation
                importHandler(nil, .none)
                return
            }
            
            // Pass the document's temporary URL to the import handler.
            importHandler(url, .move)
        })
    }
}
```

After the `importHandler` block is called, the document browser asynchronously imports the document into its final destination. When possible, the document browser imports to the currently open directory. When there is no currently open directory (for example, when the Recents tab is open), it uses the default directory.

Users can set the default directory in Settings. For more information, see [Setting up a document browser app](../setting-up-a-document-browser-app.md).

When the import is complete, the browser calls one of the following delegate methods:

- **On success.** [- documentBrowser:didImportDocumentAtURL:toDestinationURL:](<documentbrowser(__didimportdocumentat_todestinationurl_).md>)
- **On failure.** [- documentBrowser:failedToImportDocumentAtURL:error:](<documentbrowser(__failedtoimportdocumentat_error_).md>)

The document browser enables the Add button (+) only when both of the following are true:

- The [allowsDocumentCreation](../uidocumentbrowserviewcontroller/allowsdocumentcreation.md) property is set to [true](../../swift/true.md) (the default value).
- The document browser delegate implements the [- documentBrowser:didRequestDocumentCreationWithHandler:](<documentbrowser(__didrequestdocumentcreationwithhandler_).md>) method.

> [!note] Note
> The document browser cannot create new documents if you do not implement this delegate method.

## See Also

### Creating new documents

- [ImportMode](../uidocumentbrowserviewcontroller/importmode.md) — The document browser’s import modes.
- [- documentBrowser:didImportDocumentAtURL:toDestinationURL:](<documentbrowser(__didimportdocumentat_todestinationurl_).md>) — Tells the delegate that a document has been successfully imported.
- [- documentBrowser:failedToImportDocumentAtURL:error:](<documentbrowser(__failedtoimportdocumentat_error_).md>) — Tells the delegate that the document browser failed to import the specified document.
