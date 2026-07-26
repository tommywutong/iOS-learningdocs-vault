---
title: MTLDispatchType.concurrent
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldispatchtype/concurrent
source_url: 'https://developer.apple.com/documentation/metal/mtldispatchtype/concurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldispatchtype/concurrent.json'
content_hash: 'sha256:13d64640e554ca57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDispatchType](../mtldispatchtype.md)

# MTLDispatchType.concurrent

<sub>Case</sub>

Sets a command encoder to dispatch encoded commands concurrently during your pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case concurrent
```

## Discussion

If you encode multiple commands that access a single resource, you’re responsible for synchronizing the memory operations to that resource. For more information, see [Resource synchronization](../resource-synchronization.md).

## See Also

### Execution dispatch types

- [MTLDispatchTypeSerial](serial.md) — Sets a command encoder to dispatch encoded commands serially during your pass.
