---
title: layer
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/layer
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/layer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/layer.json'
content_hash: 'sha256:beeff4ba3e784075'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# layer

<sub>Type Method</sub>

Creates and returns an instance of the layer object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) layer;
```

## Return Value

The initialized layer object or `nil` if initialization was not successful.

## Discussion

If you subclass `CALayer`, you may override this method and use it to provide an instance of your specific subclass.

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)

### Creating a layer

- [- init](<init().md>) — Returns an initialized `CALayer` object.
- [- initWithLayer:](<init(layer_).md>) — Override to copy or initialize custom fields of the specified layer.
- [+ layerWithRemoteClientId:](<init(remoteclientid_).md>) — Initializes a layer with a remote client ID.
