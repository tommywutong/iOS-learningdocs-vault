---
title: 'layoutSublayers(of:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayerdelegate/layoutsublayers(of:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayerdelegate/layoutsublayers(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayerdelegate/layoutsublayers%28of%3A%29.json'
content_hash: 'sha256:fa7c9ed8986e12b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayerDelegate](../calayerdelegate.md)

# layoutSublayers(of:)

<sub>Instance Method</sub>

Tells the delegate a layer’s bounds have changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func layoutSublayers(of layer: CALayer)
```

## Parameters

- `layer` — The layer that requires layout of its sublayers.

## Discussion

The [- layoutSublayersOfLayer:](<layoutsublayers(of_).md>) method is called when a layer’s bounds have changed and its sublayers may need rearranging, for example by changing its frame’s size. You can implement this method if you need precise control over the layout of your layer’s sublayers.

The following code shows how you can create a class named `LayerDelegate` that implements `CALayerDelegate` and sets it as a layer’s (named `sublayer`) delegate. When the layer’s size changes, the delegate’s [- layoutSublayersOfLayer:](<layoutsublayers(of_).md>) iterates over all of the sublayers of `sublayer` and resizes them to fit within it.

```swift
let delegate = LayerDelegate()
    
lazy var sublayer: CALayer = {
    let layer = CALayer()
    
    layer.addSublayer(CALayer())
    layer.sublayers?.first?.backgroundColor = UIColor.blue.cgColor
    
    layer.delegate = self.delegate
    
    return layer
}()
    
// sublayer.frame = CGRect(x: 0, y: 0, width: 510, height: 510)
    
class LayerDelegate: NSObject, CALayerDelegate {
    func layoutSublayers(of layer: CALayer) {
        layer.sublayers?.forEach {
            $0.frame = layer.bounds
        }
    }
}
```
