---
title: 'init(layer:)'
framework: Core Animation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/init(layer:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/init(layer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/init%28layer%3A%29.json'
content_hash: 'sha256:cd246c99432878ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# init(layer:)

<sub>Initializer</sub>

Override to copy or initialize custom fields of the specified layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(layer: Any)
```

## Parameters

- `layer` — The layer from which custom fields should be copied.

## Return Value

A layer instance with any custom instance variables copied from `layer`.

## Discussion

This initializer is used to create shadow copies of layers, for example, for the [- presentationLayer](<presentation().md>) method. Using this method in any other situation will produce undefined behavior. For example, do not use this method to initialize a new layer with an existing layer’s content.

If you are implementing a custom layer subclass, you can override this method and use it to copy the values of instance variables into the new object. Subclasses should always invoke the superclass implementation.

This method is the designated initializer for layer objects in the presentation layer.

## See Also

### Creating a layer

- [- init](<init().md>) — Returns an initialized `CALayer` object.
- [+ layerWithRemoteClientId:](<init(remoteclientid_).md>) — Initializes a layer with a remote client ID.
