---
title: Drawing
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/drawing
source_url: 'https://developer.apple.com/documentation/uikit/drawing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/drawing.json'
content_hash: 'sha256:9f3ca9ef5a60ed07'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# Drawing

<sub>API Collection</sub>

Configure your app’s drawing environment using colors, renderers, draw paths, strings, and shadows.

## Topics

### UI updates

- [UIUpdateLink](uiupdatelink.md) — An object you use to observe, participate in, and affect the UI update process.
- [UIUpdateInfo](uiupdateinfo.md) — An object that contains detailed information about the current UI update state.
- [UIUpdateActionPhase](uiupdateactionphase.md) — An object that defines specific phases of the UI update process.

### Color

- [UIColor](uicolor.md) — An object that stores color data and sometimes opacity.

### Graphics contexts

- [UIGraphicsRenderer](uigraphicsrenderer.md) — An abstract base class for creating graphics renderers.
- [UIGraphicsRendererContext](uigraphicsrenderercontext.md) — The base class for the drawing environments for graphics renderers.
- [UIGraphicsRendererFormat](uigraphicsrendererformat.md) — A set of drawing attributes that represents the configuration of a graphics renderer context.
- [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) — A graphics renderer for creating Core Graphics-backed images.
- [UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md) — The drawing environment for an image renderer.
- [UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md) — A set of drawing attributes that represents the configuration of an image renderer context.
- [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md) — A graphics renderer for creating PDFs.
- [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md) — The drawing environment for a PDF renderer.
- [UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md) — A set of drawing attributes that represents the configuration of a PDF renderer context.

### Paths

- [UIBezierPath](uibezierpath.md) — A path that consists of straight and curved line segments that you can render in your custom views.
- [UIRectFill](<uirectfill(__).md>) — Fills the specified rectangle with the current color.
- [UIRectFillUsingBlendMode](<uirectfillusingblendmode(____).md>) — Fills a rectangle with the current fill color using the specified blend mode.
- [UIRectFrame](<uirectframe(__).md>) — Draws a frame around the inside of the specified rectangle.
- [UIRectFrameUsingBlendMode](<uirectframeusingblendmode(____).md>) — Draws a frame around the inside of a rectangle using the specified blend mode.

### Strings

- [NSStringDrawingContext](nsstringdrawingcontext.md) — An object that manages metrics for drawing attributed strings.
- [NSStringDrawingOptions](nsstringdrawingoptions.md) — Constants that specify the rendering options for drawing a string.
- [UIBaselineAdjustment](uibaselineadjustment.md) — Vertical adjustment options.

### Shadows

- [NSShadow](nsshadow.md) — An object you use to specify attributes to create and style a drop shadow during drawing operations.

### Graphics context primitives

- [UIGraphicsGetCurrentContext](<uigraphicsgetcurrentcontext().md>) — Returns the current graphics context.
- [UIGraphicsPushContext](<uigraphicspushcontext(__).md>) — Makes the specified graphics context the current context.
- [UIGraphicsPopContext](<uigraphicspopcontext().md>) — Removes the current graphics context from the top of the stack, restoring the previous context.
- [UIGraphicsBeginImageContextWithOptions](<uigraphicsbeginimagecontextwithoptions(______).md>) — Creates a bitmap-based graphics context with the specified options. _(deprecated)_
- [UIRectClip](<uirectclip(__).md>) — Modifies the current clipping path by intersecting it with the specified rectangle.

### Primitive type conversions

- [cgAffineTransform(for:)](<../foundation/nscoder/cgaffinetransform(for_).md>) — Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [cgPoint(for:)](<../foundation/nscoder/cgpoint(for_).md>) — Returns a Core Graphics point structure corresponding to the data in a given string.
- [cgRect(for:)](<../foundation/nscoder/cgrect(for_).md>) — Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [cgSize(for:)](<../foundation/nscoder/cgsize(for_).md>) — Returns a Core Graphics size structure corresponding to the data in a given string.
- [cgVector(for:)](<../foundation/nscoder/cgvector(for_).md>) — Returns a Core Graphics vector corresponding to the data in a given string.
- [string(for:)](<../foundation/nscoder/string(for_)-6yx6n.md>) — Returns a string formatted to contain the data from an affine transform.
- [string(for:)](<../foundation/nscoder/string(for_)-6ix86.md>) — Returns a string formatted to contain the data from a point.
- [string(for:)](<../foundation/nscoder/string(for_)-4qz0a.md>) — Returns a string formatted to contain the data from a rectangle.
- [string(for:)](<../foundation/nscoder/string(for_)-2f1xb.md>) — Returns a string formatted to contain the data from a size data structure.
- [string(for:)](<../foundation/nscoder/string(for_)-4omzv.md>) — Returns a string formatted to contain the data from a vector data structure.

## See Also

### Graphics, drawing, and printing

- [Images and PDF](images-and-pdf.md) — Create and manage images, including those that use bitmap and PDF formats.
- [Printing](printing.md) — Display the system print panels and manage the printing process.
