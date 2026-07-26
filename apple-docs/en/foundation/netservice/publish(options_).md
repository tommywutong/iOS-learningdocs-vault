---
title: 'publish(options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.5+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/netservice/publish(options:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservice/publish(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/publish%28options%3A%29.json'
content_hash: 'sha256:e84cec303d74fc39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# publish(options:)

<sub>Instance Method</sub>

Attempts to advertise the receiver on the network, with the given options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func publish(options: NetService.Options = [])
```

## Parameters

- `options` — Options for the receiver. The supported options are described in [Options](options.md).

## Discussion

This method returns immediately, with success or failure indicated by the callbacks to the delegate.

## See Also

### Using Network Services

- [- publish](<publish().md>) — Attempts to advertise the receiver’s on the network. _(deprecated)_
- [- resolve](<resolve().md>) — Starts a resolve process for the service. _(deprecated)_
- [- resolveWithTimeout:](<resolve(withtimeout_).md>) — Starts a resolve process of a finite duration for the service. _(deprecated)_
- [port](port.md) — The port on which the service is listening for connections. _(deprecated)_
- [- startMonitoring](<startmonitoring().md>) — Starts the monitoring of TXT-record updates for the receiver. _(deprecated)_
- [- stop](<stop().md>) — Halts a currently running attempt to publish or resolve a service. _(deprecated)_
- [- stopMonitoring](<stopmonitoring().md>) — Stops the monitoring of TXT-record updates for the receiver. _(deprecated)_
