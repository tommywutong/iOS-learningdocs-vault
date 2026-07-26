---
title: makeSharedEvent()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/makesharedevent()
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makesharedevent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makesharedevent%28%29.json'
content_hash: 'sha256:1a807f13c562d6a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeSharedEvent()

<sub>Instance Method</sub>

Creates a new shared event instance that you can use to synchronize commands and resources across different GPU devices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeSharedEvent() -> (any MTLSharedEvent)?
```

## See Also

### Creating fences and events

- [- newFence](<makefence().md>) — Creates a new memory fence instance.
- [- newEvent](<makeevent().md>) — Creates a new event instance that you can use to synchronize commands and resources within the same GPU device.
- [- newSharedEventWithHandle:](<makesharedevent(handle_).md>) — Recreates a shared event from a handle.
