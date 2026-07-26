---
title: 'documentBrowser(_:didPickDocumentURLs:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（12.0 起废弃）, iPadOS 11.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didpickdocumenturls:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didpickdocumenturls:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_%3Adidpickdocumenturls%3A%29.json'
content_hash: 'sha256:137d19f39d3c168d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewControllerDelegate](../uidocumentbrowserviewcontrollerdelegate.md)

# documentBrowser(_:didPickDocumentURLs:)

<sub>Instance Method</sub>

Tells the delegate that the user has selected one or more documents.

> [!warning] Deprecated
> Use [- documentPicker:didPickDocumentsAtURLs:](<../uidocumentpickerdelegate/documentpicker(__didpickdocumentsat_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func documentBrowser(_ controller: UIDocumentBrowserViewController, didPickDocumentURLs documentURLs: [URL])
```

## Parameters

- `controller` — The current document browser.

- `documentURLs` — An array of URLs for the selected documents. If the document browser’s [allowsPickingMultipleItems](../uidocumentbrowserviewcontroller/allowspickingmultipleitems.md) property is [true](../../swift/true.md), the array contains one or more URLs. If [false](../../swift/false.md), it contains only a single URL.

## Discussion

Implement this method to process the documents selected by the user. Typically, you create a view controller to display the selected documents, then present that view modally, like in the following example.

```swift
// Did Select Documents
func documentBrowser(_ controller: UIDocumentBrowserViewController,
                     didPickDocumentURLs documentURLs: [URL]) {
    
    assert(controller.allowsPickingMultipleItems == false)
    
    assert(documentURLs.count > 0,
           "*** We received an empty array of documents ***")
    
    assert(documentURLs.count <= 1,
           "*** We received more than one document ***")
    
    guard let url = documentURLs.first else {
        fatalError("*** No URL Found! ***")
    }
    
    openDocument(controller, forFileURL: url)
}

private func openDocument(_ controller: UIDocumentBrowserViewController,
                          forFileURL url: URL) {
    
    let doc = // Create a UIDocument subclass for the selected URL.

    let editor = // Create a view controller to edit the document.

    // Optionally, set up a transition controller here...
        
    doc.open { (success) in
        guard success else {
            // Handle the error here...
        }
        
        // Present the document
        controller.present(editor, animated: true, completion: nil)
    }
}
```
