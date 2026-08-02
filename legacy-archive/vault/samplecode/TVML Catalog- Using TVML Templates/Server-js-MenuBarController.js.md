---
title: 'TVML Catalog: Using TVML Templates'
apple_id: TP40016505
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: TVMLKit
published: '2017-06-06'
source_url: https://developer.apple.com/library/archive/samplecode/TVMLCatalog/Listings/Server_js_MenuBarController_js.html
archived_at: '2026-07-18T03:26:06.386430Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TVML Catalog: Using TVML Templates](TVML%20Catalog-%20Using%20TVML%20Templates.md)


[Next](Server-js-ModalController.js.md)[Previous](Server-js-ListController.js.md)

# Server/js/MenuBarController.js

```
/*
See LICENSE.txt for this sample’s licensing information.

Abstract:
This class handles presenting the Menu Bar template example.
*/

class MenuBarController extends DocumentController {

    fetchDocument(documentURL, loadingDocument) {
        this._documentLoader.fetch({
            url: documentURL,
            success: (menuBarDocument) => {
                const menuBarElem = menuBarDocument.getElementsByTagName("menuBar").item(0);
                menuBarElem.addEventListener("select", (event) => {
                    this.selectMenuItem(event.target);
                });

                // Pre-load the document for the initial focused menu item or first item,
                // before presenting the menuBarTemplate on navigation stack.
                // NOTE: Pre-loading is optional
                const initialMenuItemElem = this.findInitialMenuItem(menuBarElem);
                const initialMenuItemController = this.selectMenuItem(initialMenuItemElem, true, () => {
                    this.handleDocument(menuBarDocument, loadingDocument);
                });
            },
            error: (xhr) => {
                const alertDocument = createLoadErrorAlertDocument(documentURL, xhr, false);
                this.handleDocument(alertDocument, loadingDocument);
            }
        });
    }

    findInitialMenuItem(menuBarElem) {
        let highlightIndex = 0;
        const menuItemElems = menuBarElem.childNodes;
        for (let i = 0; i < menuItemElems.length; i++) {
            if (menuItemElems.item(i).hasAttribute("autoHighlight")) {
                highlightIndex = i;
                break;
            }
        }
        return menuItemElems.item(highlightIndex);
    }

    selectMenuItem(menuItemElem, isInitialItem, doneCallback) {
        const menuBarElem = menuItemElem.parentNode;
        const menuBarFeature = menuBarElem.getFeature("MenuBarDocument");
        const existingDocument = menuBarFeature.getDocument(menuItemElem);

        if (!existingDocument) {
            const controllerOptions = resolveControllerFromElement(menuItemElem);
            if (controllerOptions) {
                if (!isInitialItem) {
                    menuBarFeature.setDocument(createLoadingDocument(), menuItemElem);
                }
                controllerOptions.documentLoader = this._documentLoader;
                const controllerClass = controllerOptions.type;
                const controller = new controllerClass(controllerOptions);
                controller.handleDocument = (document) => {
                    if (isInitialItem) {
                        menuBarFeature.setDocument(document, menuItemElem);
                    } else {
                        // Force timeout to convey intent of displaying loading while the
                        // content is being loaded from server
                        setTimeout(function() {
                            // Override the presentation of controller since this controller
                            // is child of menuBar and doesn't get pushed on the navigation stack
                            menuBarFeature.setDocument(document, menuItemElem);
                        }, 1000);
                    }
                    doneCallback && doneCallback();
                };
            }
        }
    }

}

registerAttributeName('menuBarDocumentURL', MenuBarController);
```

[Next](Server-js-ModalController.js.md)[Previous](Server-js-ListController.js.md)

