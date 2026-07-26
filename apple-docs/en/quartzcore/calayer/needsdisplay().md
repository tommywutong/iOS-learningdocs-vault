---
title: needsDisplay()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/needsdisplay()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/needsdisplay()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/needsdisplay%28%29.json'
content_hash: 'sha256:b9d448f5633401a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# needsDisplay()

<sub>Instance Method</sub>

Returns a Boolean indicating whether the layer has been marked as needing an update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func needsDisplay() -> Bool
```

## Return Value

[true](../../swift/true.md) if the layer needs to be updated.

## See Also

### Updating layer display

- [- setNeedsDisplay](<setneedsdisplay().md>) — Marks the layer’s contents as needing to be updated.
- [- setNeedsDisplayInRect:](<setneedsdisplay(__).md>) — Marks the region within the specified rectangle as needing to be updated.
- [needsDisplayOnBoundsChange](needsdisplayonboundschange.md) — A Boolean indicating whether the layer contents must be updated when its bounds rectangle changes.
- [- displayIfNeeded](<displayifneeded().md>) — Initiates the update process for a layer if it is currently marked as needing an update.
- [+ needsDisplayForKey:](<needsdisplay(forkey_).md>) — Returns a Boolean indicating whether changes to the specified key require the layer to be redisplayed.
