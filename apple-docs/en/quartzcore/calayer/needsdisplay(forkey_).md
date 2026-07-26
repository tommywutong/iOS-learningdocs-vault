---
title: 'needsDisplay(forKey:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/needsdisplay(forkey:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/needsdisplay(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/needsdisplay%28forkey%3A%29.json'
content_hash: 'sha256:04a7a74f308c227e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# needsDisplay(forKey:)

<sub>Type Method</sub>

Returns a Boolean indicating whether changes to the specified key require the layer to be redisplayed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func needsDisplay(forKey key: String) -> Bool
```

## Parameters

- `key` — A string that specifies an attribute of the layer.

## Return Value

[true](../../swift/true.md) if the layer requires a redisplay.

## Discussion

Subclasses can override this method and return [true](../../swift/true.md) if the layer should be redisplayed when the value of the specified attribute changes. Animations changing the value of the attribute also trigger redisplay.

The default implementation of this method returns [false](../../swift/false.md).

## See Also

### Related Documentation

- [+ defaultActionForKey:](<defaultaction(forkey_).md>) — Returns the default action for the current class.
- [+ defaultValueForKey:](<defaultvalue(forkey_).md>) — Specifies the default value associated with the specified key.

### Updating layer display

- [- setNeedsDisplay](<setneedsdisplay().md>) — Marks the layer’s contents as needing to be updated.
- [- setNeedsDisplayInRect:](<setneedsdisplay(__).md>) — Marks the region within the specified rectangle as needing to be updated.
- [needsDisplayOnBoundsChange](needsdisplayonboundschange.md) — A Boolean indicating whether the layer contents must be updated when its bounds rectangle changes.
- [- displayIfNeeded](<displayifneeded().md>) — Initiates the update process for a layer if it is currently marked as needing an update.
- [- needsDisplay](<needsdisplay().md>) — Returns a Boolean indicating whether the layer has been marked as needing an update.
