---
title: 'TVML Catalog: Using TVML Templates'
apple_id: TP40016505
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: TVMLKit
published: '2017-06-06'
source_url: https://developer.apple.com/library/archive/samplecode/TVMLCatalog/Listings/Server_js_DocumentController_js.html
archived_at: '2026-07-18T03:26:06.199523Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TVML Catalog: Using TVML Templates](TVML%20Catalog-%20Using%20TVML%20Templates.md)


[Next](Server-js-SlideshowController.js.md)[Previous](Server-js-ModalController.js.md)

# Server/js/DocumentController.js

```
/*
See LICENSE.txt for this sample’s licensing information.

Abstract:
This class handles fetching and presenting simple templates.
*/

// Registry of attribute name used to define the URL to template (e.g. documentURL or menuBarDocumentURL)
// to controller type (e.g. DocumentController or MenuBarController)
const attributeToController = {};
const attributeKeys = [];

function registerAttributeName(type, func) {
    attributeToController[type] = func;
    attributeKeys.push(type);
}

function resolveControllerFromElement(elem) {
    for (let key of attributeKeys) {
        if (elem.hasAttribute(key)) {
            return {
                type: attributeToController[key],
                documentURL: elem.getAttribute(key)
            };
        }
    }
}

class DocumentController {

    constructor({ documentLoader, documentURL, loadingDocument }) {
        this.handleEvent = this.handleEvent.bind(this);
        this._documentLoader = documentLoader;
        this.fetchDocument(documentURL, loadingDocument);
    }

    fetchDocument(documentURL, loadingDocument) {
        this._documentLoader.fetch({
            url: documentURL,
            success: (document) => {
                // Add the event listener for document
                this.setupDocument(document);
                // Allow subclass to do custom handling for this document
                this.handleDocument(document, loadingDocument);
            },
            error: (xhr) => {
                const alertDocument = createLoadErrorAlertDocument(documentURL, xhr, false);
                this.handleDocument(alertDocument, loadingDocument);
            }
        });
    }

    setupDocument(document) {
        document.addEventListener("select", this.handleEvent);
        document.addEventListener("play", this.handleEvent);
    }

    handleDocument(document, loadingDocument) {
        if (loadingDocument) {
            navigationDocument.replaceDocument(document, loadingDocument);
        } else {
            navigationDocument.pushDocument(document);
        }
    }

    handleEvent(event) {
        const targetElem = event.target;
        let controllerOptions = resolveControllerFromElement(targetElem);
        if (controllerOptions) {
            const controllerClass = controllerOptions.type;
            if (!controllerClass.preventDefaultLoadingDocument) {
                let loadingDocument = createLoadingDocument();
                navigationDocument.pushDocument(loadingDocument);
                controllerOptions.loadingDocument = loadingDocument;
            }
            controllerOptions.event = event;
            controllerOptions.documentLoader = this._documentLoader;
            // Create the subsequent controller based on the atribute and its value. Controller would handle its presentation.
            new controllerClass(controllerOptions);
        }
        else if (targetElem.tagName === 'description') {
            // Handle description tag, if no URL was specified
            const body = targetElem.textContent;
            const alertDocument = createDescriptiveAlertDocument('', body);
            navigationDocument.presentModal(alertDocument);
        }
        return createLoadingDocument();
    }
}

registerAttributeName('documentURL', DocumentController);
```

[Next](Server-js-SlideshowController.js.md)[Previous](Server-js-ModalController.js.md)

