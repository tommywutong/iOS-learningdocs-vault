---
title: 'add(to:forMode:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, macOS 14.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/cadisplaylink/add(to:formode:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/cadisplaylink/add(to:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cadisplaylink/add%28to%3Aformode%3A%29.json'
content_hash: 'sha256:d918b86fa8d094a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CADisplayLink](../cadisplaylink.md)

# add(to:forMode:)

<sub>Instance Method</sub>

Registers the display link with a run loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func add(to runloop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `runloop` — The run loop to associate with the display link.

- `mode` — The mode in which to add the display link to the run loop.

## Discussion

You can associate a display link with multiple input modes. While the run loop is executing in a mode you specify, the display link notifies the target when the system requires new frames.

You can specify a custom mode or use one of the modes listed in [RunLoop](../../foundation/runloop.md).

The run loop retains the display link. To remove the display link from all run loops, call [- invalidate](<invalidate().md>).

## See Also

### Scheduling a Display Link to Send Notifications

- [- removeFromRunLoop:forMode:](<remove(from_formode_).md>) — Removes the display link from the run loop for the given mode.
- [- invalidate](<invalidate().md>) — Removes the display link from all run loop modes.
