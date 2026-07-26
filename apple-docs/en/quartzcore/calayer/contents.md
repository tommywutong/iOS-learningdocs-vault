---
title: contents
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/contents
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/contents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/contents.json'
content_hash: 'sha256:3fc427c5cae4dda4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# contents

<sub>Instance Property</sub>

An object that provides the contents of the layer. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contents: Any? { get set }
```

## Discussion

The default value of this property is `nil`.

If you are using the layer to display a static image, you can set this property to the [CGImage](../../coregraphics/cgimage.md) containing the image you want to display. (In macOS 10.6 and later, you can also set the property to an [NSImage](../../appkit/nsimage.md) object.) Assigning a value to this property causes the layer to use your image rather than create a separate backing store.

If the layer object is tied to a view object, you should avoid setting the contents of this property directly. The interplay between views and layers usually results in the view replacing the contents of this property during a subsequent update.

## See Also

### Providing the layer’s content

- [contentsRect](contentsrect.md) — The rectangle, in the unit coordinate space, that defines the portion of the layer’s contents that should be used. Animatable.
- [contentsCenter](contentscenter.md) — The rectangle that defines how the layer contents are scaled if the layer’s contents are resized. Animatable.
- [- display](<display().md>) — Reloads the content of this layer.
- [- drawInContext:](<draw(in_).md>) — Draws the layer’s content using the specified graphics context.
