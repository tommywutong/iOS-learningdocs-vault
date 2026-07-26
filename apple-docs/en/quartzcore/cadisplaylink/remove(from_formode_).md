---
title: 'remove(from:forMode:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, macOS 14.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/cadisplaylink/remove(from:formode:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/cadisplaylink/remove(from:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cadisplaylink/remove%28from%3Aformode%3A%29.json'
content_hash: 'sha256:7cfb14b1342ef7ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CADisplayLink](../cadisplaylink.md)

# remove(from:forMode:)

<sub>Instance Method</sub>

Removes the display link from the run loop for the given mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func remove(from runloop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `runloop` — The run loop you associate with the display link.

- `mode` — The run loop mode in which the display link is running.

## Discussion

The run loop releases the display link if it’s no longer associated with any run modes.

## See Also

### Scheduling a Display Link to Send Notifications

- [- addToRunLoop:forMode:](<add(to_formode_).md>) — Registers the display link with a run loop.
- [- invalidate](<invalidate().md>) — Removes the display link from all run loop modes.
