---
title: Images and PDF
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/images-and-pdf
source_url: 'https://developer.apple.com/documentation/uikit/images-and-pdf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/images-and-pdf.json'
content_hash: 'sha256:72c68d9be789711c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# Images and PDF

<sub>API Collection</sub>

Create and manage images, including those that use bitmap and PDF formats.

## Topics

### Representations

- [UIImage](uiimage.md) — An object that manages image data in your app.
- [SymbolConfiguration](uiimage/symbolconfiguration-swift.class.md) — An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.
- [Configuration](uiimage/configuration-swift.class.md) — A configuration object that contains the traits that the system uses when selecting the current image variant.

### Image creation

- [Supporting HDR images in your app](supporting-hdr-images-in-your-app.md) — ​ Load, display, edit, and save HDR images using SwiftUI and Core Image. ​
- [UIImageJPEGRepresentation](<uiimage/jpegdata(compressionquality_).md>) — Returns a data object that contains the image in JPEG format.
- [UIImagePNGRepresentation](<uiimage/pngdata().md>) — Returns a data object that contains the specified image in PNG format.

### Photo album

- [UIImageWriteToSavedPhotosAlbum](<uiimagewritetosavedphotosalbum(________).md>) — Adds the specified image to the user’s Camera Roll album.
- [UISaveVideoAtPathToSavedPhotosAlbum](<uisavevideoatpathtosavedphotosalbum(________).md>) — Adds the movie from the specified path to the user’s Camera Roll album.
- [UIVideoAtPathIsCompatibleWithSavedPhotosAlbum](<uivideoatpathiscompatiblewithsavedphotosalbum(__).md>) — Returns a Boolean value that indicates whether the specified video is compatible to save to the user’s Camera Roll album.

### PDF creation

- [UIGraphicsBeginPDFContextToData](<uigraphicsbeginpdfcontexttodata(______).md>) — Creates a PDF graphics context that targets the specified mutable data object.
- [UIGraphicsBeginPDFContextToFile](<uigraphicsbeginpdfcontexttofile(______).md>) — Creates a PDF graphics context that targets a file at the specified path.
- [UIGraphicsEndPDFContext](<uigraphicsendpdfcontext().md>) — Closes a PDF graphics context and pops it from the current context stack.
- [UIGraphicsBeginPDFPage](<uigraphicsbeginpdfpage().md>) — Marks the beginning of a new page in a PDF context and configures it using default values.
- [UIGraphicsBeginPDFPageWithInfo](<uigraphicsbeginpdfpagewithinfo(____).md>) — Marks the beginning of a new page in a PDF context and configures it using the specified custom values.
- [UIGraphicsGetPDFContextBounds](<uigraphicsgetpdfcontextbounds().md>) — Returns the current page bounds.
- [UIGraphicsAddPDFContextDestinationAtPoint](<uigraphicsaddpdfcontextdestinationatpoint(____).md>) — Creates a jump destination in the current page.
- [UIGraphicsSetPDFContextDestinationForRect](<uigraphicssetpdfcontextdestinationforrect(____).md>) — Links a rectangular area on the current page to the specified jump destination.
- [UIGraphicsSetPDFContextURLForRect](<uigraphicssetpdfcontexturlforrect(____).md>) — Links a rectangular area on the current page to the specified URL.

### PDF screenshots

- [UIScreenshotService](uiscreenshotservice.md) — An object that coordinates the creation of PDF screenshots of an app’s content.

## See Also

### Graphics, drawing, and printing

- [Drawing](drawing.md) — Configure your app’s drawing environment using colors, renderers, draw paths, strings, and shadows.
- [Printing](printing.md) — Display the system print panels and manage the printing process.
