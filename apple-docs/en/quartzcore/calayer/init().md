---
title: init()
framework: Core Animation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/init()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/init%28%29.json'
content_hash: 'sha256:09605585dad5758d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# init()

<sub>Initializer</sub>

Returns an initialized `CALayer` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init()
```

## Return Value

An initialized `CALayer` object.

## Discussion

This is the designated initializer for layer objects that are not in the presentation layer.

## See Also

### Creating a layer

- [- initWithLayer:](<init(layer_).md>) — Override to copy or initialize custom fields of the specified layer.
- [+ layerWithRemoteClientId:](<init(remoteclientid_).md>) — Initializes a layer with a remote client ID.
