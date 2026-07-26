---
title: 'init(screenSize:layers:label:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratemapdescriptor/init(screensize:layers:label:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/init(screensize:layers:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemapdescriptor/init%28screensize%3Alayers%3Alabel%3A%29.json'
content_hash: 'sha256:048e33c3bc7574cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMapDescriptor](../mtlrasterizationratemapdescriptor.md)

# init(screenSize:layers:label:)

<sub>Initializer</sub>

A convenience initializer that creates a rate map descriptor with a set of layer descriptors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(screenSize: MTLSize, layers: [MTLRasterizationRateLayerDescriptor], label: String? = nil)
```

## Parameters

- `screenSize` — The logical size, in pixels, of the viewport coordinate system.

- `layers` — An array of rate layer descriptors for the rate map’s layers.

- `label` — A string that identifies the resulting rate map.

## Return Value

A descriptor object whose [screenSize](screensize.md) and [label](label.md) properties are set to the provided values and whose rate map layers are set to the array you provided.

## See Also

### Creating rate map descriptors

- [init(screenSize:label:)](<init(screensize_label_).md>) — A convenience initializer that creates a rate map descriptor with a given size and identifier.
- [init(screenSize:layer:label:)](<init(screensize_layer_label_).md>) — A convenience initializer that creates a rate map descriptor with a single rate layer.
