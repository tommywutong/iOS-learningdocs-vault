---
title: needsDisplayOnBoundsChange
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/needsdisplayonboundschange
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/needsdisplayonboundschange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/needsdisplayonboundschange.json'
content_hash: 'sha256:e142d7126a8c851e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# needsDisplayOnBoundsChange

<sub>Instance Property</sub>

A Boolean indicating whether the layer contents must be updated when its bounds rectangle changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var needsDisplayOnBoundsChange: Bool { get set }
```

## Discussion

When this property is set to [true](../../swift/true.md), the layer automatically calls its [- setNeedsDisplay](<setneedsdisplay().md>) method whenever its [bounds](bounds.md) property changes. The default value of this property is [false](../../swift/false.md).

## See Also

### Updating layer display

- [- setNeedsDisplay](<setneedsdisplay().md>) — Marks the layer’s contents as needing to be updated.
- [- setNeedsDisplayInRect:](<setneedsdisplay(__).md>) — Marks the region within the specified rectangle as needing to be updated.
- [- displayIfNeeded](<displayifneeded().md>) — Initiates the update process for a layer if it is currently marked as needing an update.
- [- needsDisplay](<needsdisplay().md>) — Returns a Boolean indicating whether the layer has been marked as needing an update.
- [+ needsDisplayForKey:](<needsdisplay(forkey_).md>) — Returns a Boolean indicating whether changes to the specified key require the layer to be redisplayed.
