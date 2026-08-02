---
title: 'TVML Catalog: Using TVML Templates'
apple_id: TP40016505
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: TVMLKit
published: '2017-06-06'
source_url: https://developer.apple.com/library/archive/samplecode/TVMLCatalog/Listings/Server_js_ModalController_js.html
archived_at: '2026-07-18T03:26:06.428649Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TVML Catalog: Using TVML Templates](TVML%20Catalog-%20Using%20TVML%20Templates.md)


[Next](Server-js-DocumentController.js.md)[Previous](Server-js-MenuBarController.js.md)

# Server/js/ModalController.js

```
/*
See LICENSE.txt for this sample’s licensing information.

Abstract:
This class handles presenting the Alert template examples.
*/

class ModalController extends DocumentController {

    handleDocument(document) {
        navigationDocument.presentModal(document);
    }

    handleEvent(event) {
        const targetElem = event.target;
        if (targetElem.tagName !== 'description') {
            navigationDocument.dismissModal();
        }
        else {
            super.handleEvent(event);
        }
    }

}

// Prevent parent DocumentController from displaying the loadingTemplate
ModalController.preventDefaultLoadingDocument = true;

registerAttributeName('modalDocumentURL', ModalController);
```

[Next](Server-js-DocumentController.js.md)[Previous](Server-js-MenuBarController.js.md)

