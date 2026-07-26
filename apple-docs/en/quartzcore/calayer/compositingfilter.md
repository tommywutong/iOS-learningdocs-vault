---
title: compositingFilter
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/compositingfilter
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/compositingfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/compositingfilter.json'
content_hash: 'sha256:f4ef4cc16ea6fffe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# compositingFilter

<sub>Instance Property</sub>

A CoreImage filter used to composite the layer and the content behind it. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var compositingFilter: Any? { get set }
```

## Discussion

The default value of this property is `nil`, which causes the layer to use source-over compositing. Although you can use any Core Image filter as a layer’s compositing filter, for best results, use those in the [CICategoryCompositeOperation](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP30000136-SW71) category.

In macOS, it is possible to modify the filter’s parameters after attaching it to the layer but you must use the layer’s [setValue(_:forKeyPath:)](<../../objectivec/nsobject-swift.class/setvalue(__forkeypath_).md>) method to do so. For example, to change the `inputRadius` parameter of the filter, you could use code similar to the following:

**Swift**

```swift
let layer = CALayer()
         
if let filter = CIFilter(name:"CIGaussianBlur") {
    filter.name = "myFilter"
    layer.backgroundFilters = [filter]
    layer.setValue(1,
                   forKeyPath: "backgroundFilters.myFilter.inputRadius")
}
```

**Objective-C**

```objc
CIFilter *filter = ...;
CALayer *layer = ...;
 
layer.compositingFilter = filter;
[layer setValue:[NSNumber numberWithInt:1] forKeyPath:@"compositingFilter.inputRadius"];
```

Changing the inputs of the [CIFilter](../../coreimage/cifilter-swift.class.md) object directly after it is attached to the layer causes undefined behavior.

The following code shows how to create two overlapping text layers, background and foreground. Addition compositing is used to composite the foreground over the background.

```swift
view.layer = CALayer()
view.layerUsesCoreImageFilters = true
     
let background = CATextLayer()
background.string = "background"
background.foregroundColor = NSColor.gray.cgColor
background.backgroundColor = NSColor.darkGray.cgColor
background.alignmentMode = kCAAlignmentCenter
background.fontSize = 96
background.frame = CGRect(x: 10, y: 10, width: 640, height: 160)
     
let foreground = CATextLayer()
foreground.string = "foreground"
foreground.foregroundColor = NSColor.lightGray.cgColor
foreground.backgroundColor = NSColor.darkGray.cgColor
foreground.alignmentMode = kCAAlignmentCenter
foreground.fontSize = 48
foreground.opacity = 0.5
foreground.frame = CGRect(x: 20, y: 20, width: 600, height: 60)
foreground.masksToBounds = false
     
if let compositingFilter = CIFilter(name: "CIAdditionCompositing") {
    foreground.compositingFilter = compositingFilter
}
     
view.layer?.addSublayer(background)
background.addSublayer(foreground)
```

The following figure shows the result: the identical background colors of the two layers are added together so that a brighter gray is produced where the layers overlap.

![Addition compositing filter](../../../../attachments/ba62dee32ae5c8adc2b876a77ce9cc6a/media-2851428@2x.png)

The following figure shows the default result when the foreground layer’s compositing filter is `nil` or [CISourceOverCompositing](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/filter/ci/CISourceOverCompositing).

![Default compositing filter](../../../../attachments/fd131a516078b5fb2eca0d9be9f8cf33/media-2851429@2x.png)

### Special Considerations

This property is not supported on layers in iOS.

## See Also

### Layer filters

- [filters](filters.md) — An array of Core Image filters to apply to the contents of the layer and its sublayers. Animatable.
- [backgroundFilters](backgroundfilters.md) — An array of Core Image filters to apply to the content immediately behind the layer. Animatable.
- [minificationFilter](minificationfilter.md) — The filter used when reducing the size of the content.
- [minificationFilterBias](minificationfilterbias.md) — The bias factor used by the minification filter to determine the levels of detail.
- [magnificationFilter](magnificationfilter.md) — The filter used when increasing the size of the content.
