---
title: nw_release
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_release
source_url: 'https://developer.apple.com/documentation/network/nw_release'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_release.json'
content_hash: 'sha256:c1b633eb7ce25653'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_release

<sub>Function</sub>

Releases a reference count on a Network.framework object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
void nw_release(void *obj);
```

## See Also

### Related Documentation

- [os_release](../os/os_release-c.func.md)

### Memory Management

- [nw_retain](nw_retain.md) — Adds a reference count to a Network.framework object.
- [nw_object_t](nw_object_t.md) — The generic type for objects in the Network framework.
