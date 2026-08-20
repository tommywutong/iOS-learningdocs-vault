---
title: 'TVML Catalog: Using TVML Templates'
apple_id: TP40016505
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: TVMLKit
published: '2017-06-06'
source_url: https://developer.apple.com/library/archive/samplecode/TVMLCatalog/Listings/Server_js_SlideshowController_js.html
archived_at: '2026-07-18T03:26:06.579480Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TVML Catalog: Using TVML Templates](TVML%20Catalog-%20Using%20TVML%20Templates.md)


[Next](Server-js-application.js.md)[Previous](Server-js-DocumentController.js.md)

# Server/js/SlideshowController.js

```
/*
See LICENSE.txt for this sample’s licensing information.

Abstract:
This function handles presenting the Slideshow API example.
*/

function SlideshowController({ documentLoader, documentURL: imageURLsString }) {
    const imageURLs = imageURLsString.split(/\s+/).map(documentLoader.prepareURL);
    Slideshow.start(imageURLs, { showSettings: false });
}

// Prevent the DocumentController to display loadingTemplate
SlideshowController.preventDefaultLoadingDocument = true;

registerAttributeName("slideshowImageURLs", SlideshowController);
```

[Next](Server-js-application.js.md)[Previous](Server-js-DocumentController.js.md)

