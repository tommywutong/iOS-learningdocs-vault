---
title: Networking Overview
apple_id: TP40010220
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/Discovering,Browsing,AndAdvertisingNetworkServices/Discovering,Browsing,AndAdvertisingNetworkServices.html
archived_at: '2026-07-18T01:33:56.431355Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Networking Overview](About%20Networking.md)


[Next](Displaying%20Web%20and%20Multimedia%20Content.md)[Previous](Assessing%20Your%20Networking%20Needs.md)

# Discovering and Advertising Network Services

OS X and iOS provide four APIs for discovering and advertising network services:

- `NSNetService`—A high-level Objective-C API suitable for most app developers.
- `CFNetService`—A high-level C API suitable for use in Core Foundation code.
- DNS Service Discovery—A low-level C API suitable for cross-platform code. This API also offers more flexibility than the higher-level APIs.
- Game Kit framework—A high-level Objective-C API that provides peer-to-peer communication support for games, both locally (using infrastructure Wi-Fi and Bluetooth) and globally over the Internet.

In addition to these APIs, the Multipeer Connectivity Framework provides support for discovering and communicating with instances of your app and related apps on nearby devices using infrastructure Wi-Fi, peer-to-peer Wi-Fi, and either Bluetooth (for iOS) or Ethernet (for OS X).

As a rule, you should use Game Kit only for game-related peer-to-peer networking. For other peer-to-peer networking between iOS devices running iOS 7 and later, you should consider using the Multipeer Connectivity framework.

For compatibility with older versions of iOS, you can also write your own networking code and use `CFNetService` or `NSNetService` to advertise its availability.

A Bonjour service advertisement consists of three parts:

- Service name—This name must be unique to a particular instance of your program running on a particular computer.
- Service type—This must be the same for all instances of your program, and should be registered with the Internet Assigned Numbers Authority (IANA).
- Domain—If the domain value is empty, the host chooses the appropriate domains in which to publish or browse.

When an app browses for Bonjour services, it asks for services matching a particular type in a particular domain, and it gets back a list of matching service names. It should then present an appropriate UI to the user. When the user tells the app to connect to a particular service, the app should then connect to the service using a connect-to-service API. (If this is not possible for some reason, the app can pass the service’s hostname and port to a connect-by-name API or, if a connect-by-name API is not available, the app can ask Bonjour to resolve the hostname, and the app can then connect by IP address and port number.)

Bonjour zero-configuration networking lets you advertise network services, such as a printer or a document syncing service, on a network. There are three ways to publish a network service:

- For Objective-C and Core Foundation code, the recommended way is with the `CFNetServices` API.
- For portable C code that must run on operating systems other than iOS and OS X, the DNS Service Discovery C API is recommended.

You can publish a network service with the following steps:

1. Create a socket to listen for connections to the service. See Writing a TCP-Based Server in _[Networking Programming Topics](../../Networking%20Internet/Networking%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdioby)_ for the recommended way to listen for connections on a network socket.
2. Create a service object, providing the port of your socket, the domain (usually an empty string), and the service type string of your choosing:

   - With Foundation, initialize an `NSNetService` object with the [initWithDomain:type:name:port:](https://developer.apple.com/documentation/foundation/nsnetservice/1413364-initwithdomain) method.
   - With Core Foundation, create a `CFNetServiceRef` object with the [CFNetServiceCreate](https://developer.apple.com/documentation/cfnetwork/1426628-cfnetservicecreate) function.
   - With the DNS Service Discovery API, call [DNSServiceRegister](https://developer.apple.com/documentation/dnssd/1804733-dnsserviceregister) to return a `DNSServiceRef` object.
3. Assign a delegate or callback:

   - With Foundation, assign a delegate to the `NSNetService` object with the [delegate](https://developer.apple.com/documentation/foundation/netservice/1410296-delegate) method.
   - With Core Foundation, assign a client callback to the `CFNetServiceRef` object with the [CFNetServiceSetClient](https://developer.apple.com/documentation/cfnetwork/1426447-cfnetservicesetclient) function.
   - With the DNS Service Discovery API, you should pass a client callback (and, optionally, a pointer to a context object of your choosing) in your call to `DNSServiceRegister`. At this point, you are done except for handling callbacks when they occur.
4. Schedule or reschedule the service, if necessary:

   - With Foundation, the service is automatically scheduled on the current run loop in the default mode. If you need to schedule the object on another run loop or in a different mode, you should unschedule it and reschedule it at this point.
   - With Core Foundation, you _must_ schedule the `CFNetServicesRef` object on a run loop by calling [CFNetServiceScheduleWithRunLoop](https://developer.apple.com/documentation/cfnetwork/1426730-cfnetserviceschedulewithrunloop).
   - With the DNS Service Discovery API, call `DNSServiceSetDispatchQueue` to schedule the service on a dispatch queue. (If you must support an OS prior to OS X v10.7, see the _[SRVResolver](../../../samplecode/SRVResolver/SRVResolver.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnrsgu)_ sample code project for an example of how to use DNS Service Discovery without Grand Central Dispatch.)
5. Publish the service, if necessary:

   - With Foundation, publish the service by calling the [publish](https://developer.apple.com/documentation/foundation/netservice/1416480-publish) method.
   - With Core Foundation, publish the service by calling [CFNetServiceRegisterWithOptions](https://developer.apple.com/documentation/cfnetwork/1426790-cfnetserviceregisterwithoptions).
   - With the DNS Service Discovery API, no further action is necessary; the service was already published when you called `DNSServiceRegister`.

After your service is published, you can listen for connections on your socket and set up input and output streams when a connection is made.

The process for finding and resolving a network service is as simple as the process for publishing one. To browse for network services in Objective-C, create an instance of the [NSNetServiceBrowser](https://developer.apple.com/documentation/foundation/netservicebrowser) class and assign it a delegate. Then, call the [searchForServicesOfType:inDomain:](https://developer.apple.com/documentation/foundation/netservicebrowser/1417565-searchforservices) method on the service browser. The [netServiceBrowser:didFindService:moreComing:](https://developer.apple.com/documentation/foundation/nsnetservicebrowserdelegate/1417979-netservicebrowser) delegate method is called once for every service found.

To connect to a service, first stop the browsing by calling [stop](https://developer.apple.com/documentation/foundation/nsnetservicebrowser/1414528-stop) (unless you have a specific reason to keep browsing), then call the [getInputStream:outputStream:](https://developer.apple.com/documentation/foundation/netservice/1418325-getinputstream) method on the [NSNetService](https://developer.apple.com/documentation/foundation/netservice) object that represents the service. The address of the service is resolved automatically.

You can also use the [CFStreamCreatePairWithSocketToNetService](https://developer.apple.com/documentation/cfnetwork/1426794-cfstreamcreatepairwithsockettone) function with a [CFNetServiceRef](https://developer.apple.com/documentation/cfnetwork/cfnetservice) object to connect to a Bonjour service.

You may need to resolve a network service manually to provide the service’s address to an API that does not accept network service names. To resolve a network service in Objective-C, first stop the browsing by calling [stop](https://developer.apple.com/documentation/foundation/nsnetservicebrowser/1414528-stop) (unless you have a specific reason to keep browsing), then call the [resolveWithTimeout:](https://developer.apple.com/documentation/foundation/netservice/1416564-resolve) method on the `NSNetService` object that represents the service.

The [netServiceDidResolveAddress:](https://developer.apple.com/documentation/foundation/netservicedelegate/1408457-netservicedidresolveaddress) method is called on the service’s delegate when the service’s address has been resolved. You can then access the service’s hostname with the [hostName](https://developer.apple.com/documentation/foundation/nsnetservice/1413300-hostname) method or its address information with the [addresses](https://developer.apple.com/documentation/foundation/netservice/1408528-addresses) method. To avoid unnecessary network traffic, you should also call [stop](https://developer.apple.com/documentation/foundation/netservice/1408827-stop) on the `NSNetService` object as soon as it returns a set of addresses.

The Multipeer Connectivity Framework provides a layer on top of Bonjour that lets you communicate with apps running on nearby devices (over infrastructure Wi-Fi, peer-to-peer Wi-Fi, and either Bluetooth (for iOS) or Ethernet (for OS X) without having to write lots of networking code specific to your app.

With Multipeer Connectivity, your app advertises its availability. It can then discover other instances of your app (or other apps that share the same service type) running on nearby devices, and can invite those nearby peers to join a session. If they accept the invitation, your app can send messages and files to one or more of the connected peers with just a single method call.

If you need stream-based communication, your app can open a unidirectional stream to any connected peer (which can also open a unidirectional stream back to your app in response).

Finally, Multipeer Connectivity provides the ability to share small amounts of data (such as the user’s screen name) outside the context of a session, if desired, allowing you to provide the user with information that he or she can use when choosing peers to invite into a session.

Multipeer Connectivity—Read _[Multipeer Connectivity Framework Reference](https://developer.apple.com/documentation/multipeerconnectivity)_ and the _[MultipeerGroupChat](../../../samplecode/MultipeerGroupChat/MultipeerGroupChat.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnrzge)_ sample code project.

Game Kit—Read _[Game Center Programming Guide](../../Networking%20Internet/Game%20Center%20Programming%20Guide/About%20Game%20Center.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmbu)_, _[Game Kit Framework Reference](https://developer.apple.com/documentation/gamekit)_, and the _[GKRocket](../../../samplecode/GKRocket/GKRocket.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnzug4)_ and _[GKTank](../../../samplecode/GKTank/GKTank.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojrha)_ sample code projects.

`NSNetService`—Read _[NSNetServices and CFNetServices Programming Guide](../../Networking/NSNetServices%20and%20CFNetServices%20Programming%20Guide/About%20NSNetServices%20and%20CFNetServices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomzw)_, _[NSNetServiceBrowser Class Reference](https://developer.apple.com/documentation/foundation/nsnetservicebrowser)_, _[NSNetServiceBrowserDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate)_, and _[NSNetServiceDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/netservicedelegate)_. For sample code, see the _[RemoteCurrency](../../../samplecode/RemoteCurrency/RemoteCurrency.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrgy)_ sample code project.

`CFNetService`—Read _[NSNetServices and CFNetServices Programming Guide](../../Networking/NSNetServices%20and%20CFNetServices%20Programming%20Guide/About%20NSNetServices%20and%20CFNetServices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomzw)_ and _CFNetServices Reference_.

DNS Service Discovery—Read _[DNS Service Discovery Programming Guide](../../Networking/DNS%20Service%20Discovery%20Programming%20Guide/Introduction%20to%20DNS%20Service%20Discovery.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnru)_ and _[DNS Service Discovery C Reference](https://developer.apple.com/documentation/dnssd/dns_service_discovery_c)_.

[Next](Displaying%20Web%20and%20Multimedia%20Content.md)[Previous](Assessing%20Your%20Networking%20Needs.md)

