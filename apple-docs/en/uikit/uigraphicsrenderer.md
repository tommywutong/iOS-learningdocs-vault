---
title: UIGraphicsRenderer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsrenderer
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderer.json'
content_hash: 'sha256:009bf6895af8dcaf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsRenderer

<sub>Class</sub>

An abstract base class for creating graphics renderers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UIGraphicsRenderer
```

## Overview

Don’t use [UIGraphicsRenderer](uigraphicsrenderer.md) directly. Instead, either use one of the concrete subclasses ([UIGraphicsImageRenderer](uigraphicsimagerenderer.md) or [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md)), or create your own subclass.

Graphics renderers provide memory-efficient management of Core Graphics contexts. Core Graphics contexts represent the drawing environment and backing store for 2D Graphics. As you reuse a graphics renderer, it in turn reuses Core Graphics contexts.

### Subclassing notes

You can’t use [UIGraphicsRenderer](uigraphicsrenderer.md) directly, but if the concrete subclasses ([UIGraphicsPDFRenderer](uigraphicspdfrenderer.md) and [UIGraphicsImageRenderer](uigraphicsimagerenderer.md)) don’t provide the functionality you require, you can create your own subclass.

Consider creating a subclass any time you need to create multiple Core Graphics contexts, each with the same dimensions and attributes, and one of the concrete subclasses ([UIGraphicsPDFRenderer](uigraphicspdfrenderer.md) or [UIGraphicsImageRenderer](uigraphicsimagerenderer.md)) doesn’t provide the functionality you require.

To create a subclass of [UIGraphicsRenderer](uigraphicsrenderer.md), first import the appropriate submodule or header, as shown in the following code.

**Swift**

```swift
import UIKit.UIGraphicsRendererSubclass
```

**Objective-C**

```objc
#import <UIKit/UIGraphicsRendererSubclass.h>
```

A graphics renderer manages a pool of Core Graphics contexts that are reused with repeated uses of the renderer. The renderer creates these [CGContext](../coregraphics/cgcontext.md) objects using the [+ contextWithFormat:](<uigraphicsrenderer/context(with_).md>) class method, and then wraps each of them in an instance of the class returned by the [+ rendererContextClass](<uigraphicsrenderer/renderercontextclass().md>) class method. You must therefore override these two methods in your graphics renderer subclass.

To perform drawing actions on a Core Graphics context, call the [- runDrawingActions:completionActions:error:](<uigraphicsrenderer/rundrawingactions(__completionactions_).md>) method, providing two blocks. Both of these blocks have a [UIGraphicsRendererContext](uigraphicsrenderercontext.md) argument, providing access to a Core Graphics context.

It is recommended that you create a public method on your renderer subclass that internally wraps the [- runDrawingActions:completionActions:error:](<uigraphicsrenderer/rundrawingactions(__completionactions_).md>) method. This is how the rendering methods operate on the concrete subclasses, for example the [- imageWithActions:](<uigraphicsimagerenderer/image(actions_).md>) method on [UIGraphicsImageRenderer](uigraphicsimagerenderer.md).

Each time the [- runDrawingActions:completionActions:error:](<uigraphicsrenderer/rundrawingactions(__completionactions_).md>) method is called, the renderer calls the [+ prepareCGContext:withRendererContext:](<uigraphicsrenderer/prepare(__with_).md>) method with the [CGContext](../coregraphics/cgcontext.md) and [UIGraphicsRendererContext](uigraphicsrenderercontext.md) as arguments. Override the [+ prepareCGContext:withRendererContext:](<uigraphicsrenderer/prepare(__with_).md>) method to apply the [UIGraphicsRendererContext](uigraphicsrenderercontext.md) configuration to the underlying [CGContext](../coregraphics/cgcontext.md) before the renderer invokes the drawing actions.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIGraphicsImageRenderer](uigraphicsimagerenderer.md), [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a graphics renderer

- [- initWithBounds:](<uigraphicsrenderer/init(bounds_).md>) — Creates a new graphics renderer with the specified bounds and a default format.
- [- initWithBounds:format:](<uigraphicsrenderer/init(bounds_format_).md>) — Creates a new graphics renderer with the given bounds and format.

### Configuring the renderer

- [allowsImageOutput](uigraphicsrenderer/allowsimageoutput.md) — A Boolean value specifying whether the renderer can create output images.
- [format](uigraphicsrenderer/format.md) — The format used to create the graphics renderer.

### Running the drawing actions

- [- runDrawingActions:completionActions:error:](<uigraphicsrenderer/rundrawingactions(__completionactions_).md>) — Performs drawing actions on a Core Graphics context that the renderer prepares.
- [UIGraphicsDrawingActions](uigraphicsdrawingactions.md) — A closure that executes a set of drawing instructions that the renderer applies to the Core Graphics context.

### Managing graphics contexts

- [+ contextWithFormat:](<uigraphicsrenderer/context(with_).md>) — Creates a Core Graphics context configured according to the supplied format object.
- [+ prepareCGContext:withRendererContext:](<uigraphicsrenderer/prepare(__with_).md>) — Applies the configuration specified in the renderer context to the Core Graphics context.
- [+ rendererContextClass](<uigraphicsrenderer/renderercontextclass().md>) — Specifies the drawing context class used by this graphics renderer.

## See Also

### Graphics contexts

- [UIGraphicsRendererContext](uigraphicsrenderercontext.md) — The base class for the drawing environments for graphics renderers.
- [UIGraphicsRendererFormat](uigraphicsrendererformat.md) — A set of drawing attributes that represents the configuration of a graphics renderer context.
- [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) — A graphics renderer for creating Core Graphics-backed images.
- [UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md) — The drawing environment for an image renderer.
- [UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md) — A set of drawing attributes that represents the configuration of an image renderer context.
- [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md) — A graphics renderer for creating PDFs.
- [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md) — The drawing environment for a PDF renderer.
- [UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md) — A set of drawing attributes that represents the configuration of a PDF renderer context.
