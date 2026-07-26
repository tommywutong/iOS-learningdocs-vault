---
title: display()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/display()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/display()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/display%28%29.json'
content_hash: 'sha256:aa63c8b42d9cf74b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# display()

<sub>Instance Method</sub>

Reloads the content of this layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func display()
```

## Discussion

Do not call this method directly. The layer calls this method at appropriate times to update the layer’s content. If the layer has a delegate object, this method attempts to call the delegate’s [- displayLayer:](<../calayerdelegate/display(__).md>) method, which the delegate can use to update the layer’s contents. If the delegate does not implement the [- displayLayer:](<../calayerdelegate/display(__).md>) method, this method creates a backing store and calls the layer’s [- drawInContext:](<draw(in_).md>) method to fill that backing store with content. The new backing store replaces the previous contents of the layer.

Subclasses can override this method and use it to set the layer’s [contents](contents.md) property directly. You might do this if your custom layer subclass handles layer updates differently.

## See Also

### Providing the layer’s content

- [contents](contents.md) — An object that provides the contents of the layer. Animatable.
- [contentsRect](contentsrect.md) — The rectangle, in the unit coordinate space, that defines the portion of the layer’s contents that should be used. Animatable.
- [contentsCenter](contentscenter.md) — The rectangle that defines how the layer contents are scaled if the layer’s contents are resized. Animatable.
- [- drawInContext:](<draw(in_).md>) — Draws the layer’s content using the specified graphics context.
