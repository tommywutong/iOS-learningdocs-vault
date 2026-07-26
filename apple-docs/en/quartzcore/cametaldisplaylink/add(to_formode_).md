---
title: 'add(to:forMode:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/cametaldisplaylink/add(to:formode:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/add(to:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldisplaylink/add%28to%3Aformode%3A%29.json'
content_hash: 'sha256:86921a714236d0da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalDisplayLink](../cametaldisplaylink.md)

# add(to:forMode:)

<sub>Instance Method</sub>

Registers the display link with a run loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func add(to runloop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `runloop` — A run loop instance the method associates with the display link.

- `mode` — A run loop mode for the display link.

## Discussion

You can associate the display link with any of the [RunLoop](../../foundation/runloop.md) modes, multiple input modes, or a custom mode. When the run loop is in `mode`, the display link notifies its delegate when the system prepares the next frame.

You can remove the display link from a run loop by calling [- removeFromRunLoop:forMode:](<remove(from_formode_).md>), or from all run loops with [- invalidate](<invalidate().md>).
