---
title: filter
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransition/filter
source_url: 'https://developer.apple.com/documentation/quartzcore/catransition/filter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransition/filter.json'
content_hash: 'sha256:802cc2515470486e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransition](../catransition.md)

# filter

<sub>Instance Property</sub>

An optional Core Image filter object that provides the transition.

<sub>Mac Catalyst, macOS</sub>

```swift
var filter: Any? { get set }
```

## Discussion

If specified, the filter must support both [kCIInputImageKey](../../coreimage/kciinputimagekey.md) and [kCIInputTargetImageKey](../../coreimage/kciinputtargetimagekey.md) input keys, and the [kCIOutputImageKey](../../coreimage/kcioutputimagekey.md) output key.  The filter may optionally support the [kCIInputExtentKey](../../coreimage/kciinputextentkey.md) input key, which is set to a rectangle describing the region in which the transition should run. If `filter` does not support the required input and output keys the behavior is undefined.

Defaults to `nil`. When a transition filter is specified the [type](type.md) and [subtype](subtype.md) properties are ignored.

The [NSView](../../appkit/nsview.md) that contains the transitioning layer must have its [layerUsesCoreImageFilters](../../appkit/nsview/layerusescoreimagefilters.md) set to [true](../../swift/true.md).

The following code shows how you can transition between the two states of a [CATextLayer](../catextlayer.md) named `transitioningLayer`. When the layer is first created, its [backgroundColor](../calayer/backgroundcolor.md) is set to red and its [string](../catextlayer/string.md) property is set to `Red`. When the `runTransition()` function is called, a new [CATransition](../catransition.md) object is created and added to `transitioningLayer`, and the state of the layer is changed so that its background color is blue and its rendered text reads `Blue`.

The end result is that the transition animates from the red state to the blue state using a [CICopyMachineTransition](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/filter/ci/CICopyMachineTransition) transition.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    view.layerUsesCoreImageFilters = true
    
    view.layer = CALayer()
    
    transitioningLayer.frame = CGRect(x: 10, y: 10,
                                      width: 320, height: 160)
    
    view.layer!.addSublayer(transitioningLayer)
    
    // Initial "red" state
    transitioningLayer.backgroundColor = NSColor.red.cgColor
    transitioningLayer.string = "Red"
}
     
func runTransition() {
    let transition = CATransition()
    transition.duration = 2
    
    transition.filter = CIFilter(name: "CICopyMachineTransition")
    transitioningLayer.add(transition,
                           forKey: "transition")
    
    // Transition to "blue" state
    transitioningLayer.backgroundColor = NSColor.blue.cgColor
    transitioningLayer.string = "Blue"
}
```

### Special Considerations

This property is not supported on layers in iOS.
