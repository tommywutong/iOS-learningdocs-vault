---
title: 'draw(_:in:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayerdelegate/draw(_:in:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayerdelegate/draw(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayerdelegate/draw%28_%3Ain%3A%29.json'
content_hash: 'sha256:7cdca9eb436f81e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayerDelegate](../calayerdelegate.md)

# draw(_:in:)

<sub>Instance Method</sub>

Tells the delegate to implement the display process using the layer’s context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func draw(_ layer: CALayer, in ctx: CGContext)
```

## Parameters

- `layer` — The layer whose contents need to be drawn.

- `ctx` — The graphics context to use for drawing. The graphics context incorporates the appropriate scale factor for drawing to the target screen.

## Discussion

The [- drawLayer:inContext:](<draw(__in_).md>) method is called when the layer is marked for its content to be reloaded, typically with the [- setNeedsDisplay](<../calayer/setneedsdisplay().md>) method. It is not called if the delegate implements the [- displayLayer:](<display(__).md>) method. You can use the context to draw vectors, such as curves and lines, or images with the [draw(_:in:byTiling:)](<../../coregraphics/cgcontext/draw(__in_bytiling_).md>) method.

The following code shows how you can create a class named `LayerDelegate` that implements [CALayerDelegate](../calayerdelegate.md) and sets it as a layer’s (named `sublayer`) delegate. When [- setNeedsDisplay](<../calayer/setneedsdisplay().md>) is called on `sublayer`, the delegate’s [- drawLayer:inContext:](<draw(__in_).md>) method draws an ellipse fitting the bounding box of the layer using the [boundingBoxOfClipPath](../../coregraphics/cgcontext/boundingboxofclippath.md) function.

```swift
let delegate = LayerDelegate()
    
lazy var sublayer: CALayer = {
    let layer = CALayer()
    
    layer.delegate = self.delegate
    
    return layer
}()
    
// sublayer.setNeedsDisplay()
    
class LayerDelegate: NSObject, CALayerDelegate {
    func draw(_ layer: CALayer, in ctx: CGContext) {
        ctx.addEllipse(in: ctx.boundingBoxOfClipPath)
        ctx.strokePath()
    }
}
```

> [!important] Important
> This method is not called if the delegate implements [- displayLayer:](<display(__).md>).

## See Also

### Providing the Layer’s Content

- [- displayLayer:](<display(__).md>) — Tells the delegate to implement the display process.
- [- layerWillDraw:](<layerwilldraw(__).md>) — Notifies the delegate of an imminent draw.
