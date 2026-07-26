---
title: 'waitForDrawable(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/waitfordrawable(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/waitfordrawable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/waitfordrawable%28_%3A%29.json'
content_hash: 'sha256:15073e265037c059'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# waitForDrawable(_:)

<sub>Instance Method</sub>

Schedules a wait operation on the command queue to ensure the display is no longer using a specific Metal drawable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func waitForDrawable(_ drawable: any MTLDrawable)
```

## Parameters

- `drawable` — [MTLDrawable](../mtldrawable.md) instance to signal.

## Discussion

Use this method to ensure the display is no longer using a [MTLDrawable](../mtldrawable.md) instance before executing any subsequent commands.

This method returns immediately and doesn’t perform any synchronization on the current thread. You are responsible for calling this method before committing any command buffers containing commands that target this drawable.

Call this method multiple times if you commit your command buffers to multiple command queues.
