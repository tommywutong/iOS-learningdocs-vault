---
title: Images
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/images
source_url: 'https://developer.apple.com/documentation/swiftui/images'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/images.json'
content_hash: 'sha256:11783d2a6c782ec8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Images

<sub>API Collection</sub>

Add images and symbols to your app’s user interface.

## Overview

Display images, including [SF Symbols](../design/human-interface-guidelines/sf-symbols.md), images that you store in an asset catalog, and images that you store on disk, using an [Image](image.md) view.

![](../../../attachments/4fb32811fff960a104407b1f3b81a0f0/images-hero@2x.png)

For images that take time to retrieve — for example, when you load an image from a network endpoint — load the image asynchronously using [AsyncImage](asyncimage.md). You can instruct that view to display a placeholder during the load operation.

For design guidance, see [Images](../design/human-interface-guidelines/images.md) in the Human Interface Guidelines.

## Topics

### Creating an image

- [Image](image.md) — A view that displays an image.

### Configuring an image

- [Fitting images into available space](fitting-images-into-available-space.md) — Adjust the size and shape of images in your app’s user interface by applying view modifiers.
- [imageScale(_:)](<view/imagescale(__).md>) — Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [imageScale](environmentvalues/imagescale.md) — The image scale for this environment.
- [Scale](image/scale.md) — A scale to apply to vector images relative to text.
- [Orientation](image/orientation.md) — The orientation of an image.
- [ResizingMode](image/resizingmode.md) — The modes that SwiftUI uses to resize an image to fit within its containing view.

### Loading images asynchronously

- [AsyncImage](asyncimage.md) — A view that asynchronously loads and displays an image.
- [AsyncImagePhase](asyncimagephase.md) — The current phase of the asynchronous image loading operation.

### Setting a symbol variant

- [symbolVariant(_:)](<view/symbolvariant(__).md>) — Makes symbols within the view show a particular variant.
- [symbolVariants](environmentvalues/symbolvariants.md) — The symbol variant to use in this environment.
- [SymbolVariants](symbolvariants.md) — A variant of a symbol.

### Managing symbol effects

- [symbolEffect(_:options:isActive:)](<view/symboleffect(__options_isactive_).md>) — Returns a new view with a symbol effect added to it.
- [symbolEffect(_:options:value:)](<view/symboleffect(__options_value_).md>) — Returns a new view with a symbol effect added to it.
- [symbolEffectsRemoved(_:)](<view/symboleffectsremoved(__).md>) — Returns a new view with its inherited symbol image effects either removed or left unchanged.
- [SymbolEffectTransition](symboleffecttransition.md) — Creates a transition that applies the Appear, Disappear, DrawOn or DrawOff symbol animation to symbol images within the inserted or removed view hierarchy.

### Setting symbol rendering modes

- [symbolRenderingMode(_:)](<view/symbolrenderingmode(__).md>) — Sets the rendering mode for symbol images within this view.
- [symbolRenderingMode](environmentvalues/symbolrenderingmode.md) — The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.
- [SymbolRenderingMode](symbolrenderingmode.md) — A symbol rendering mode.
- [SymbolColorRenderingMode](symbolcolorrenderingmode.md) — A method of filling a layer in a symbol image.
- [SymbolVariableValueMode](symbolvariablevaluemode.md) — A method of rendering the variable value of a symbol image.

### Rendering images from views

- [ImageRenderer](imagerenderer.md) — An object that creates images from SwiftUI views.

## See Also

### Views

- [View fundamentals](view-fundamentals.md) — Define the visual elements of your app using a hierarchy of views.
- [View configuration](view-configuration.md) — Adjust the characteristics of views in a hierarchy.
- [View styles](view-styles.md) — Apply built-in and custom appearances and behaviors to different types of views.
- [Animations](animations.md) — Create smooth visual updates in response to state changes.
- [Text input and output](text-input-and-output.md) — Display formatted text and get text input from the user.
- [Controls and indicators](controls-and-indicators.md) — Display values and get user selections.
- [Menus and commands](menus-and-commands.md) — Provide space-efficient, context-dependent access to commands and controls.
- [Shapes](shapes.md) — Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](drawing-and-graphics.md) — Enhance your views with graphical effects and customized drawings.
