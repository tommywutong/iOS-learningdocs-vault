---
title: displayIfNeeded()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/displayifneeded()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/displayifneeded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/displayifneeded%28%29.json'
content_hash: 'sha256:fdacc97649a66355'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# displayIfNeeded()

<sub>Instance Method</sub>

Initiates the update process for a layer if it is currently marked as needing an update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func displayIfNeeded()
```

## Discussion

You can call this method as needed to force an update to your layer’s contents outside of the normal update cycle. Doing so is generally not needed, though. The preferred way to update a layer is to call [- setNeedsDisplay](<setneedsdisplay().md>) and let the system update the layer during the next cycle.

## See Also

### Updating layer display

- [- setNeedsDisplay](<setneedsdisplay().md>) — Marks the layer’s contents as needing to be updated.
- [- setNeedsDisplayInRect:](<setneedsdisplay(__).md>) — Marks the region within the specified rectangle as needing to be updated.
- [needsDisplayOnBoundsChange](needsdisplayonboundschange.md) — A Boolean indicating whether the layer contents must be updated when its bounds rectangle changes.
- [- needsDisplay](<needsdisplay().md>) — Returns a Boolean indicating whether the layer has been marked as needing an update.
- [+ needsDisplayForKey:](<needsdisplay(forkey_).md>) — Returns a Boolean indicating whether changes to the specified key require the layer to be redisplayed.
