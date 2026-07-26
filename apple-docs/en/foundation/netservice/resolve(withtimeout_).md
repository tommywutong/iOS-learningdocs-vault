---
title: 'resolve(withTimeout:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/netservice/resolve(withtimeout:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservice/resolve(withtimeout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/resolve%28withtimeout%3A%29.json'
content_hash: 'sha256:1deba30466b360b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# resolve(withTimeout:)

<sub>Instance Method</sub>

Starts a resolve process of a finite duration for the service.

> [!warning] Deprecated
> Use nw_connection_t or nw_listener_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func resolve(withTimeout timeout: TimeInterval)
```

## Parameters

- `timeout` — The maximum number of seconds to attempt a resolve. A value of 0.0 indicates no timeout and a resolve process of indefinite duration.

## Discussion

During the resolve period, the service sends [- netServiceDidResolveAddress:](<../netservicedelegate/netservicedidresolveaddress(__).md>) to the delegate for each address it discovers that matches the service parameters. Once the timeout is hit, the service sends [- netServiceDidStop:](<../netservicedelegate/netservicedidstop(__).md>) to the delegate. If no addresses resolve during the timeout period, the service sends [- netService:didNotResolve:](<../netservicedelegate/netservice(__didnotresolve_).md>) to the delegate.

## See Also

### Related Documentation

- [addresses](addresses.md) — A read-only array containing `NSData` objects, each of which contains a socket address for the service. _(deprecated)_

### Using Network Services

- [- publish](<publish().md>) — Attempts to advertise the receiver’s on the network. _(deprecated)_
- [- publishWithOptions:](<publish(options_).md>) — Attempts to advertise the receiver on the network, with the given options. _(deprecated)_
- [- resolve](<resolve().md>) — Starts a resolve process for the service. _(deprecated)_
- [port](port.md) — The port on which the service is listening for connections. _(deprecated)_
- [- startMonitoring](<startmonitoring().md>) — Starts the monitoring of TXT-record updates for the receiver. _(deprecated)_
- [- stop](<stop().md>) — Halts a currently running attempt to publish or resolve a service. _(deprecated)_
- [- stopMonitoring](<stopmonitoring().md>) — Stops the monitoring of TXT-record updates for the receiver. _(deprecated)_
