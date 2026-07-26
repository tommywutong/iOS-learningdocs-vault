---
title: Presenting selected documents
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/presenting-selected-documents
source_url: 'https://developer.apple.com/documentation/uikit/presenting-selected-documents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/presenting-selected-documents.json'
content_hash: 'sha256:527b1d2989532aef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [Adding a document browser to your app](adding-a-document-browser-to-your-app.md)

# Presenting selected documents

<sub>Article</sub>

Display user-selected documents over your browser view controller.

## Overview

When the user selects one or more documents in the browser view controller, the system calls your delegate’s [- documentBrowser:didPickDocumentURLs:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didpickdocumenturls_).md>) method.

### Display documents with document view controllers

In your implementation of the [- documentBrowser:didPickDocumentURLs:](<uidocumentbrowserviewcontrollerdelegate/documentbrowser(__didpickdocumenturls_).md>) method, modally present a view controller to display the selected documents by calling the browser’s [- presentViewController:animated:completion:](<uiviewcontroller/present(__animated_completion_).md>) method.

The document view should fill the entire screen, but it can have its own split view controller, navigation controller, or tab controller, as appropriate. It remains onscreen as long as the user is interacting with the documents. To return to the browser, dismiss the document view controller.

## See Also

### Configuration

- [Setting up a document browser app](setting-up-a-document-browser-app.md) — Add a document browser view controller to your app.
- [Enabling document sharing](enabling-document-sharing.md) — Give users the ability to import and export documents from your app.
