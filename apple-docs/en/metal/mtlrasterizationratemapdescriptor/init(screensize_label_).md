---
title: 'init(screenSize:label:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratemapdescriptor/init(screensize:label:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/init(screensize:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemapdescriptor/init%28screensize%3Alabel%3A%29.json'
content_hash: 'sha256:719121662bd6ea83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMapDescriptor](../mtlrasterizationratemapdescriptor.md)

# init(screenSize:label:)

<sub>Initializer</sub>

A convenience initializer that creates a rate map descriptor with a given size and identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(screenSize: MTLSize, label: String? = nil)
```

## Parameters

- `screenSize` — The logical size, in pixels, of the viewport coordinate system.

- `label` — A string that identifies the resulting rate map.

## Return Value

A descriptor object whose [screenSize](screensize.md) and [label](label.md) properties are set to the provided values. You need to add at least one layer rate map to the descriptor.

## See Also

### Creating rate map descriptors

- [init(screenSize:layer:label:)](<init(screensize_layer_label_).md>) — A convenience initializer that creates a rate map descriptor with a single rate layer.
- [init(screenSize:layers:label:)](<init(screensize_layers_label_).md>) — A convenience initializer that creates a rate map descriptor with a set of layer descriptors.
