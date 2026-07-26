---
title: 'display(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayerdelegate/display(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayerdelegate/display(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayerdelegate/display%28_%3A%29.json'
content_hash: 'sha256:b47d6ea414e6b9ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayerDelegate](../calayerdelegate.md)

# display(_:)

<sub>Instance Method</sub>

Tells the delegate to implement the display process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func display(_ layer: CALayer)
```

## Parameters

- `layer` — The layer whose contents need updating.

## Discussion

The [- displayLayer:](<display(__).md>) delegate method is called when the layer is marked for its content to be reloaded, typically initiated by the [- setNeedsDisplay](<../calayer/setneedsdisplay().md>) method. The typical technique for updating is to set the layer’s `contents` property.

The following code shows how you can create a class named `LayerDelegate` that implements [CALayerDelegate](../calayerdelegate.md) and sets it as a layer’s (named `sublayer`) delegate. When [- setNeedsDisplay](<../calayer/setneedsdisplay().md>) is called on `sublayer`, the delegate’s [- displayLayer:](<display(__).md>) replaces its contents with a specified image.

```swift
let delegate = LayerDelegate()
     
lazy var sublayer: CALayer = {
    let layer = CALayer()
    
    layer.delegate = self.delegate
    
    return layer
}()
     
// When `sublayer.setNeedsDisplay()` is called, `sublayer.contents` are updated.
     
class LayerDelegate: NSObject, CALayerDelegate {
    func display(_ layer: CALayer) {
        layer.contents = UIImage(named: "rabbit.png")?.cgImage
    }
}
```

## See Also

### Providing the Layer’s Content

- [- drawLayer:inContext:](<draw(__in_).md>) — Tells the delegate to implement the display process using the layer’s context.
- [- layerWillDraw:](<layerwilldraw(__).md>) — Notifies the delegate of an imminent draw.
