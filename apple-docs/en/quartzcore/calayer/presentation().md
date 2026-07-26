---
title: presentation()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/presentation()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/presentation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/presentation%28%29.json'
content_hash: 'sha256:00257bcb122c0d6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# presentation()

<sub>Instance Method</sub>

Returns a copy of the presentation layer object that represents the state of the layer as it currently appears onscreen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func presentation() -> Self?
```

## Return Value

A copy of the current presentation layer object.

## Discussion

The layer object returned by this method provides a close approximation of the layer that is currently being displayed onscreen. While an animation is in progress, you can retrieve this object and use it to get the current values for those animations.

The [sublayers](sublayers.md), [mask](mask.md), and [superlayer](superlayer.md) properties of the returned layer return the corresponding objects from the presentation tree (not the model tree). This pattern also applies to any read-only layer methods. For example, the [- hitTest:](<hittest(__).md>) method of the returned object queries the layer objects in the presentation tree.

## See Also

### Accessing related layer objects

- [- modelLayer](<model().md>) — Returns the model layer object associated with the receiver, if any.
