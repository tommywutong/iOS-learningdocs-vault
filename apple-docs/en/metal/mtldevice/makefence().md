---
title: makeFence()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/makefence()
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makefence()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makefence%28%29.json'
content_hash: 'sha256:26dc83d8186bb9d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeFence()

<sub>Instance Method</sub>

Creates a new memory fence instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeFence() -> (any MTLFence)?
```

## See Also

### Creating fences and events

- [- newEvent](<makeevent().md>) — Creates a new event instance that you can use to synchronize commands and resources within the same GPU device.
- [- newSharedEvent](<makesharedevent().md>) — Creates a new shared event instance that you can use to synchronize commands and resources across different GPU devices.
- [- newSharedEventWithHandle:](<makesharedevent(handle_).md>) — Recreates a shared event from a handle.
