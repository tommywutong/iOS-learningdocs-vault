---
title: 'makeSharedEvent(handle:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makesharedevent(handle:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makesharedevent(handle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makesharedevent%28handle%3A%29.json'
content_hash: 'sha256:d4e97dd69aceeef7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeSharedEvent(handle:)

<sub>Instance Method</sub>

Recreates a shared event from a handle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeSharedEvent(handle sharedEventHandle: MTLSharedEventHandle) -> (any MTLSharedEvent)?
```

## Parameters

- `sharedEventHandle` — An [MTLSharedEventHandle](../mtlsharedeventhandle.md) instance from another GPU device or process.

## Return Value

A new [MTLSharedEvent](../mtlsharedevent.md) instance if the method completed successfully; otherwise nil.

## See Also

### Creating fences and events

- [- newFence](<makefence().md>) — Creates a new memory fence instance.
- [- newEvent](<makeevent().md>) — Creates a new event instance that you can use to synchronize commands and resources within the same GPU device.
- [- newSharedEvent](<makesharedevent().md>) — Creates a new shared event instance that you can use to synchronize commands and resources across different GPU devices.
