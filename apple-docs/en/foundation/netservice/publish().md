---
title: publish()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/netservice/publish()
source_url: 'https://developer.apple.com/documentation/foundation/netservice/publish()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/publish%28%29.json'
content_hash: 'sha256:4d41cbbe2fdf15b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# publish()

<sub>Instance Method</sub>

Attempts to advertise the receiver’s on the network.

> [!warning] Deprecated
> Use nw_connection_t or nw_listener_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func publish()
```

## Discussion

This method returns immediately, with success or failure indicated by the callbacks to the delegate. This is equivalent to calling [- publishWithOptions:](<publish(options_).md>) with the default options (`0`).

## See Also

### Using Network Services

- [- publishWithOptions:](<publish(options_).md>) — Attempts to advertise the receiver on the network, with the given options. _(deprecated)_
- [- resolve](<resolve().md>) — Starts a resolve process for the service. _(deprecated)_
- [- resolveWithTimeout:](<resolve(withtimeout_).md>) — Starts a resolve process of a finite duration for the service. _(deprecated)_
- [port](port.md) — The port on which the service is listening for connections. _(deprecated)_
- [- startMonitoring](<startmonitoring().md>) — Starts the monitoring of TXT-record updates for the receiver. _(deprecated)_
- [- stop](<stop().md>) — Halts a currently running attempt to publish or resolve a service. _(deprecated)_
- [- stopMonitoring](<stopmonitoring().md>) — Stops the monitoring of TXT-record updates for the receiver. _(deprecated)_
