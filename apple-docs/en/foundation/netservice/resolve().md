---
title: resolve()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/netservice/resolve()
source_url: 'https://developer.apple.com/documentation/foundation/netservice/resolve()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/resolve%28%29.json'
content_hash: 'sha256:d13c8ff1f47f177a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# resolve()

<sub>Instance Method</sub>

Starts a resolve process for the service.

> [!warning] Deprecated
> Use [- resolveWithTimeout:](<resolve(withtimeout_).md>) instead.

<sub>tvOS, visionOS</sub>

```swift
func resolve()
```

## Discussion

Attempts to determine at least one address for the service. This method returns immediately, with success or failure indicated by the callbacks to the delegate.

In OS X v10.4, this method calls [- resolveWithTimeout:](<resolve(withtimeout_).md>) with a timeout value of `5`.

## See Also

### Related Documentation

- [addresses](addresses.md) — A read-only array containing `NSData` objects, each of which contains a socket address for the service. _(deprecated)_

### Using Network Services

- [- publish](<publish().md>) — Attempts to advertise the receiver’s on the network. _(deprecated)_
- [- publishWithOptions:](<publish(options_).md>) — Attempts to advertise the receiver on the network, with the given options. _(deprecated)_
- [- resolveWithTimeout:](<resolve(withtimeout_).md>) — Starts a resolve process of a finite duration for the service. _(deprecated)_
- [port](port.md) — The port on which the service is listening for connections. _(deprecated)_
- [- startMonitoring](<startmonitoring().md>) — Starts the monitoring of TXT-record updates for the receiver. _(deprecated)_
- [- stop](<stop().md>) — Halts a currently running attempt to publish or resolve a service. _(deprecated)_
- [- stopMonitoring](<stopmonitoring().md>) — Stops the monitoring of TXT-record updates for the receiver. _(deprecated)_
