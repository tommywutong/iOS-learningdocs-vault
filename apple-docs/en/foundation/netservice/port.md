---
title: port
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.5+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/netservice/port
source_url: 'https://developer.apple.com/documentation/foundation/netservice/port'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/port.json'
content_hash: 'sha256:20d7ee0b6a85d415'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# port

<sub>Instance Property</sub>

The port on which the service is listening for connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var port: Int { get }
```

## Discussion

If the object was initialized by calling [- initWithDomain:type:name:port:](<init(domain_type_name_port_).md>) (whether by your code or by a browser object), then the value was set when the object was first initialized.

If the object was initialized by calling [- initWithDomain:type:name:](<init(domain_type_name_).md>), the value of this property is not valid (`-1`) until after the service has successfully been resolved (when `addresses` is non-`nil`).

> [!note] Backward Compatibility Note
> This became a property in OS X v10.9 and iOS 7, but the underlying getter method (`port`) has been available since this class was first introduced.

## See Also

### Using Network Services

- [- publish](<publish().md>) — Attempts to advertise the receiver’s on the network. _(deprecated)_
- [- publishWithOptions:](<publish(options_).md>) — Attempts to advertise the receiver on the network, with the given options. _(deprecated)_
- [- resolve](<resolve().md>) — Starts a resolve process for the service. _(deprecated)_
- [- resolveWithTimeout:](<resolve(withtimeout_).md>) — Starts a resolve process of a finite duration for the service. _(deprecated)_
- [- startMonitoring](<startmonitoring().md>) — Starts the monitoring of TXT-record updates for the receiver. _(deprecated)_
- [- stop](<stop().md>) — Halts a currently running attempt to publish or resolve a service. _(deprecated)_
- [- stopMonitoring](<stopmonitoring().md>) — Stops the monitoring of TXT-record updates for the receiver. _(deprecated)_
