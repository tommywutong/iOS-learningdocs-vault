---
title: NetService
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/netservice
source_url: 'https://developer.apple.com/documentation/foundation/netservice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice.json'
content_hash: 'sha256:36152eb1242e0eae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NetService

<sub>Class</sub>

A network service that broadcasts its availability using multicast DNS.

> [!warning] Deprecated
> Use nw_connection_t or nw_listener_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class NetService
```

## Overview

The [NetService](netservice.md) class represents a network service, either one your application publishes or is a client of. This class and the [NetServiceBrowser](netservicebrowser.md) class use multicast DNS to convey information about network services to and from your application. The API of [NetService](netservice.md) provides a convenient way to publish the services offered by your application and to resolve the socket address for a service.

The types of services you access using [NetService](netservice.md) are the same types that you access directly using BSD sockets. HTTP and FTP are two services commonly provided by systems. (For a list of common services and the ports used by those services, see the file `/etc/services`.) Applications can also define their own custom services to provide specific data to clients.

You can use the [NetService](netservice.md) class as either a publisher of a service or a client of a service. If your application publishes a service, your code must acquire a port and prepare a socket to communicate with clients. Once your socket is ready, you use the [NetService](netservice.md) class to notify clients that your service is ready. If your application is the client of a network service, you can either create an [NetService](netservice.md) object directly (if you know the exact host and port information) or use an [NetServiceBrowser](netservicebrowser.md) object to browse for services.

To publish a service, initialize your [NetService](netservice.md) object with the service name, domain, type, and port information. All of this information must be valid for the socket created by your application. Once initialized, call the [- publish](<netservice/publish().md>) method to broadcast your service information to the network.

When connecting to a service, use the [NetServiceBrowser](netservicebrowser.md) class to locate the service on the network and obtain the corresponding [NetService](netservice.md) object. Once you have the object, call the [- resolveWithTimeout:](<netservice/resolve(withtimeout_).md>) method to verify that the service is available and ready for your application. If it is, the [addresses](netservice/addresses.md) property provides the socket information you can use to connect to the service.

The methods of [NetService](netservice.md) operate asynchronously so your application is not impacted by the speed of the network. All information about a service is returned to your application through the [NetService](netservice.md) object’s delegate. You must provide a delegate object to respond to messages and to handle errors appropriately.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating Network Services

- [- initWithDomain:type:name:](<netservice/init(domain_type_name_).md>) — Returns the receiver, initialized as a network service of a given type and sets the initial host information. _(deprecated)_
- [- initWithDomain:type:name:port:](<netservice/init(domain_type_name_port_).md>) — Initializes the receiver for publishing a network service of type `type` at the socket location specified by `domain`, `name`, and `port`. _(deprecated)_

### Configuring Network Services

- [+ dataFromTXTRecordDictionary:](<netservice/data(fromtxtrecord_).md>) — Returns an `NSData` object representing a TXT record formed from a given dictionary. _(deprecated)_
- [+ dictionaryFromTXTRecordData:](<netservice/dictionary(fromtxtrecord_).md>) — Returns a dictionary representing a TXT record given as an `NSData` object. _(deprecated)_
- [addresses](netservice/addresses.md) — A read-only array containing `NSData` objects, each of which contains a socket address for the service. _(deprecated)_
- [domain](netservice/domain.md) — A string containing the domain for this service. _(deprecated)_
- [includesPeerToPeer](netservice/includespeertopeer.md) — Specifies whether to also publish, resolve, or monitor this service over peer-to-peer Bluetooth and Wi-Fi, if available. _(deprecated)_
- [- getInputStream:outputStream:](<netservice/getinputstream(__outputstream_).md>) — Creates a pair of input and output streams for the receiver and returns a Boolean value that indicates whether they were retrieved successfully. _(deprecated)_
- [name](netservice/name.md) — A string containing the name of this service. _(deprecated)_
- [type](netservice/type.md) — The type of the published service. _(deprecated)_
- [- TXTRecordData](<netservice/txtrecorddata().md>) — Returns the TXT record for the receiver. _(deprecated)_
- [- setTXTRecordData:](<netservice/settxtrecord(__).md>) — Sets the TXT record for the receiver, and returns a Boolean value that indicates whether the operation was successful. _(deprecated)_
- [delegate](netservice/delegate.md) — The delegate for the receiver. _(deprecated)_

### Managing Run Loops

- [- scheduleInRunLoop:forMode:](<netservice/schedule(in_formode_).md>) — Adds the service to the specified run loop. _(deprecated)_
- [- removeFromRunLoop:forMode:](<netservice/remove(from_formode_).md>) — Removes the service from the given run loop for a given mode. _(deprecated)_

### Using Network Services

- [- publish](<netservice/publish().md>) — Attempts to advertise the receiver’s on the network. _(deprecated)_
- [- publishWithOptions:](<netservice/publish(options_).md>) — Attempts to advertise the receiver on the network, with the given options. _(deprecated)_
- [- resolve](<netservice/resolve().md>) — Starts a resolve process for the service. _(deprecated)_
- [- resolveWithTimeout:](<netservice/resolve(withtimeout_).md>) — Starts a resolve process of a finite duration for the service. _(deprecated)_
- [port](netservice/port.md) — The port on which the service is listening for connections. _(deprecated)_
- [- startMonitoring](<netservice/startmonitoring().md>) — Starts the monitoring of TXT-record updates for the receiver. _(deprecated)_
- [- stop](<netservice/stop().md>) — Halts a currently running attempt to publish or resolve a service. _(deprecated)_
- [- stopMonitoring](<netservice/stopmonitoring().md>) — Stops the monitoring of TXT-record updates for the receiver. _(deprecated)_

### Obtaining the DNS Hostname

- [hostName](netservice/hostname.md) — A string containing the DNS hostname for this service. _(deprecated)_

### Constants

- [NSNetServices Errors](nsnetservices-errors.md) — If an error occurs, the delegate error-handling methods return a dictionary with the following keys.
- [ErrorCode](netservice/errorcode-swift.enum.md) — These constants identify errors that can occur when accessing net services.
- [Options](netservice/options.md) — These constants specify options for a network service.

## See Also

### Local Network Services

- [NetServiceDelegate](netservicedelegate.md) — The interface a net service uses to inform its delegate about the state of the service it offers.
- [NSBonjourServices](../bundleresources/information-property-list/nsbonjourservices.md) — Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../bundleresources/information-property-list/nslocalnetworkusagedescription.md) — A message that tells people why the app is requesting access to the local network.
