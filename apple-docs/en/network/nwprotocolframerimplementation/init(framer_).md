---
title: 'init(framer:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolframerimplementation/init(framer:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframerimplementation/init(framer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframerimplementation/init%28framer%3A%29.json'
content_hash: 'sha256:debc7de464bdee1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolFramerImplementation](../nwprotocolframerimplementation.md)

# init(framer:)

<sub>Initializer</sub>

Initializes your custom framing protocol for use in one connection attempt.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(framer: NWProtocolFramer.Instance)
```

## See Also

### Handling Instance Lifetime

- [start(framer:)](<start(framer_).md>) — Requests that your protocol set up its state and begin a handshake, if necessary.
- [StartResult](../nwprotocolframer/startresult.md) — Results that you send to indicate the disposition of your protocol after receiving the call to start.
- [wakeup(framer:)](<wakeup(framer_).md>) — Delivers a scheduled wakeup event.
- [stop(framer:)](<stop(framer_).md>) — Requests that your protocol send any final messages to close the connection.
- [cleanup(framer:)](<cleanup(framer_).md>) — Indicates that your protocol should clean up all allocations before being deallocated.
- [label](label.md) — A label defined by your custom protocol for use in debugging.
