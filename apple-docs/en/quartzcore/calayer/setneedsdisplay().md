---
title: setNeedsDisplay()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/setneedsdisplay()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/setneedsdisplay()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/setneedsdisplay%28%29.json'
content_hash: 'sha256:273e86474f00bc62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# setNeedsDisplay()

<sub>Instance Method</sub>

Marks the layer’s contents as needing to be updated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setNeedsDisplay()
```

## Discussion

Calling this method causes the layer to recache its content. This results in the layer potentially calling either the [- displayLayer:](<../calayerdelegate/display(__).md>) or [- drawLayer:inContext:](<../calayerdelegate/draw(__in_).md>) method of its delegate. The existing content in the layer’s [contents](contents.md) property is removed to make way for the new content.

## See Also

### Updating layer display

- [- setNeedsDisplayInRect:](<setneedsdisplay(__).md>) — Marks the region within the specified rectangle as needing to be updated.
- [needsDisplayOnBoundsChange](needsdisplayonboundschange.md) — A Boolean indicating whether the layer contents must be updated when its bounds rectangle changes.
- [- displayIfNeeded](<displayifneeded().md>) — Initiates the update process for a layer if it is currently marked as needing an update.
- [- needsDisplay](<needsdisplay().md>) — Returns a Boolean indicating whether the layer has been marked as needing an update.
- [+ needsDisplayForKey:](<needsdisplay(forkey_).md>) — Returns a Boolean indicating whether changes to the specified key require the layer to be redisplayed.
