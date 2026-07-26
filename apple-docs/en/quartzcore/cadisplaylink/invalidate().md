---
title: invalidate()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, macOS 14.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cadisplaylink/invalidate()
source_url: 'https://developer.apple.com/documentation/quartzcore/cadisplaylink/invalidate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cadisplaylink/invalidate%28%29.json'
content_hash: 'sha256:4f17da13ecfd94e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CADisplayLink](../cadisplaylink.md)

# invalidate()

<sub>Instance Method</sub>

Removes the display link from all run loop modes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func invalidate()
```

## Discussion

When you remove the display link from all run loop mode, the system releases it. The display link also releases the target.

This method is thread safe, so you can call it from a thread separate to the one in which the display link runs.

## See Also

### Scheduling a Display Link to Send Notifications

- [- addToRunLoop:forMode:](<add(to_formode_).md>) — Registers the display link with a run loop.
- [- removeFromRunLoop:forMode:](<remove(from_formode_).md>) — Removes the display link from the run loop for the given mode.
