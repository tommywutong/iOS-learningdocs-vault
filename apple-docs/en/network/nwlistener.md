---
title: NWListener
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwlistener
source_url: 'https://developer.apple.com/documentation/network/nwlistener'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener.json'
content_hash: 'sha256:233fe9da23a65aac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWListener

<sub>Class</sub>

An object you use to listen for incoming network connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class NWListener
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Listeners

- [init(using:on:)](<nwlistener/init(using_on_).md>) — Initializes a network listener, with an optional local port.
- [start(queue:)](<nwlistener/start(queue_).md>) — Registers for listening, and sets the queue on which all listener events are delivered.
- [stateUpdateHandler](nwlistener/stateupdatehandler.md) — A handler that receives listener state updates.
- [State](nwlistener/state-swift.enum.md) — States indicating whether a listener is able to accept incoming connections.
- [port](nwlistener/port.md) — The port on which the listener can accept connections.
- [cancel()](<nwlistener/cancel().md>) — Stops listening for inbound connections.

### Receiving Connections

- [newConnectionHandler](nwlistener/newconnectionhandler.md) — A handler that receives inbound connections.
- [newConnectionLimit](nwlistener/newconnectionlimit.md) — The remaining number of inbound connections to deliver before rejecting connections.
- [InfiniteConnectionLimit](nwlistener/infiniteconnectionlimit.md) — A static value to indicate that inbound connections should not be limited.

### Advertising Bonjour Services

- [NSBonjourServices](../bundleresources/information-property-list/nsbonjourservices.md) — Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../bundleresources/information-property-list/nslocalnetworkusagedescription.md) — A message that tells people why the app is requesting access to the local network.
- [service](nwlistener/service-swift.property.md) — A Bonjour service that advertises the listener on the local network.
- [Service](nwlistener/service-swift.struct.md) — A description used to advertise the Bonjour service that a listener provides.
- [serviceRegistrationUpdateHandler](nwlistener/serviceregistrationupdatehandler.md) — A handler that receives updates for the service endpoint being advertised.
- [ServiceRegistrationChange](nwlistener/serviceregistrationchange.md) — Changes to how a network listener’s service is advertised.

### Inspecting Listeners

- [parameters](nwlistener/parameters.md) — The parameters used to initialize the listener.
- [queue](nwlistener/queue.md) — The queue on which listener events are delivered.

### Initializers

- [init(applicationService:using:)](<nwlistener/init(applicationservice_using_).md>)
- [init(launchd:using:)](<nwlistener/init(launchd_using_).md>) _(deprecated)_
- [init(launchdSocketKey:parameters:)](<nwlistener/init(launchdsocketkey_parameters_).md>)
- [init(service:using:)](<nwlistener/init(service_using_).md>)

### Instance Properties

- [newConnectionGroupHandler](nwlistener/newconnectiongrouphandler.md)
- [state](nwlistener/state-swift.property.md)

## See Also

### Connections and Listeners

- [NWConnection](nwconnection.md) — A bidirectional data connection between a local endpoint and a remote endpoint.
- [NWBrowser](nwbrowser.md) — An object you use to browse for available network services.
- [NWConnectionGroup](nwconnectiongroup.md) — An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- [NWEthernetChannel](nwethernetchannel.md) — An object you use to send and receive custom Ethernet frames.
