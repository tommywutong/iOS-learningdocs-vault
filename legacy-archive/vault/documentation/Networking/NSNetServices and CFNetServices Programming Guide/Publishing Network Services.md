---
title: NSNetServices and CFNetServices Programming Guide
apple_id: TP40002736
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSNetServiceProgGuide/Articles/PublishingServices.html
archived_at: '2026-07-15T08:18:23.439660Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [NSNetServices and CFNetServices Programming Guide](About%20NSNetServices%20and%20CFNetServices.md)


[Next](Browsing%20for%20Network%20Services.md)[Previous](Foundation%20Network%20Services%20Architecture.md)

# Publishing Network Services

Bonjour enables dynamic discovery of network services on IP networks without a centralized directory server. The Foundation framework’s `NSNetService` class represents instances of Bonjour network services. This chapter describes the process for publishing Bonjour network services with `NSNetService`.

Bonjour network services use standard DNS information to advertise their existence to potential clients on a network. In Cocoa, the `NSNetService` class handles the details of service publication.

Typically, you use `NSNetService` to publish a service provided by a socket owned by the same process. However, because the `NSNetService` class does not use the socket in any way, you can also use the class to advertise on behalf of another process’s service, such as an FTP server process that has not yet been updated to support Bonjour. However, if you are creating an IP network service, you should include Bonjour publication code as part of its startup process.

Because network activity can sometimes take some time, `NSNetService` objects process publication requests asynchronously, delivering information through delegate methods. To use `NSNetService` correctly, your app must assign a delegate to each `NSNetService` instance it creates. Because the identity of the `NSNetService` object is passed as a parameter in delegate methods, you can use one delegate for multiple `NSNetService` objects.

Publishing a Bonjour network service takes four steps:

1. Set up a valid TCP listening socket (or a UDP data socket) for communication.
2. Initialize an `NSNetService` instance with name, type, domain, and port number, and assign a delegate to the object.
3. Publish the `NSNetService` instance.
4. Respond to messages sent to the `NSNetService` object’s delegate.

The following sections describe these steps in detail.

Bonjour network services require either a TCP listening socket or a UDP data socket.

If you already have existing networking code, you can continue using it as is, and provide its port number to Bonjour when you initialize the service.

If you don’t have existing networking code, use the CFSocket API:

- For TCP, use a `CFSocketRef` object to listen for incoming connections, then use `NSStream` or `CFStreamRef` object for the actual communication. For good examples of how to set up a network listener, see the _[RemoteCurrency](../../../samplecode/RemoteCurrency/RemoteCurrency.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrgy)_, _[CocoaEcho](../../../samplecode/CocoaEcho/CocoaEcho.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrqgm)_, and _[SimpleNetworkStreams](../../../samplecode/SimpleNetworkStreams/SimpleNetworkStreams.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojxhe)_ sample code projects.
- For UDP, use a `CFSocketRef` object for sending and receiving packets. For an example, see the _[UDPEcho](../../../samplecode/UDPEcho/UDPEcho.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnrwga)_ sample code project.

To learn why CFSocket is recommended, read [Using Sockets and Socket Streams](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/SocketsAndStreams/SocketsAndStreams.html#//apple_ref/doc/uid/TP40010220-CH203) in _[Networking Overview](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_.

For a more detailed overview of how to write a TCP- or UDP-based daemon, read Using Sockets and Socket Streams in _[Networking Programming Topics](../../Networking%20Internet/Networking%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdioby)_.

To initialize an `NSNetService` instance for publication, use the `initWithDomain:type:name:port:` method. This method sets up the instance with appropriate socket information and adds it to the current run loop.

The service type expresses both the application-layer protocol (FTP, HTTP, and so on) and the transport protocol (TCP or UDP). The format is as described in [Domain Naming Conventions](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Articles/domainnames.html#//apple_ref/doc/uid/TP40002460), for example, `_printer._tcp` for a printer over TCP.

The service name can be an arbitrary `NSString`, but the value must be no longer than 63 bytes in UTF-8 encoding. Because this is the name that should be presented to users, it should be human-readable and descriptive of the specific service instance. Consider letting the user override any default name that you provide.

One recommended approach is to use the computer name as the service name. If you pass the empty string (`@""`) for the service name parameter, the system automatically advertises your service using the computer name as the service name. For examples of other naming approaches, read _[Bonjour Overview](../../Cocoa/Bonjour%20Overview/About%20Bonjour.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyts2i)_.

If you need to construct the service name in a nonstandard way, you can retrieve the computer name yourself. In OS X on the desktop, you can obtain the computer name by calling the `SCDynamicStoreCopyComputerName` function from the System Configuration framework. In iOS, you can obtain the same information from the `name` property of the `UIDevice` class.

When publishing a service, you must also specify the domain in which the service should be published. Here are some common values:

- `@""`—Registers the service in the default set of domains. Pass this value unless you have a specific reason not to.
- `@"local"`—Registers the service _only_ on the local network. Pass this value if you need to prevent publishing your service over Back to My Mac or wide-area Bonjour.
- A user-specified domain—Registers the service in only the specified domain. To retrieve a list of existing domains, call the `searchForRegistrationDomains` method (as described in [Browsing for Domains](Browsing%20for%20Domains.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenzvfvjvony)) or allow the user to enter an arbitrary domain name.

Upon initialization, the `NSNetService` object is automatically scheduled on the current run loop with the default mode. If you want to schedule it on a different run loop or with a different mode, you can call the `removeFromRunLoop:forMode:` and `scheduleInRunLoop:forMode:` methods.

After the initialization is complete and valid, assign a delegate to the `NSNetService` object with the `setDelegate:` method. Finally, publish the service with the `publish` method, which returns immediately. Bonjour performs the publication asynchronously and returns results through delegate methods.

Listing 2-1 demonstrates the initialization and publication process for Bonjour network services. An explanation of the code follows it. For a good example of service publication, see the _[PictureSharing](../../../samplecode/PictureSharing/PictureSharing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanzrgi)_ sample code project in the Mac Developer Library.

__Listing 2-1__  Initializing and publishing a Bonjour network service

```
void myRegistrationFunction(uint16_t port) {
id delegateObject;      // Assume this exists.
NSNetService *service;

    service = [[NSNetService alloc] initWithDomain:@""// 1
                                    type:@"_music._tcp"
                                    name:@""
                                    port:port];
    if(service)
    {
        [service setDelegate:delegateObject];// 2
        [service publish];// 3
    }
    else
    {
        NSLog(@"An error occurred initializing the NSNetService object.");
    }
}
```

Here’s what the code does:

1. Initializes the `NSNetService` object. This example uses the default domain(s) for publication and a hypothetical TCP/IP music service.
2. Sets the delegate for the `NSNetService` object. This object handles all results from the `NSNetService` object, as described in [Implementing Delegate Methods for Publication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3tmlkcineugq2jivbq).
3. Publishes the service to the network.

To stop a service that is already running or is in the process of starting up, use the `stop` method.

`NSNetService` provides your app with publication status information by calling methods on its delegate. If you are publishing a service, your delegate object should implement the following methods:

- `netServiceWillPublish:`
- `netServiceDidPublish:`
- `netService:didNotPublish:`
- `netServiceDidStop:`

The `netServiceWillPublish:` method notifies the delegate that Bonjour is ready to publish the service. When this method is called, the service is not yet visible to the network, which means that publication may still fail. However, you can assume that the service is visible unless `NSNetService` calls your delegate’s `netService:didNotPublish:` method.

The `netServiceDidPublish:` method notifies the delegate that Bonjour has successfully published the service.

The `netService:didNotPublish:` method is called when publication fails for any reason. Your delegate's `netService:didNotPublish:` method should extract the type of error from the returned dictionary using the `NSNetServicesErrorCode` key and handle the error accordingly. For a complete list of possible errors, see _[NSNetService Class Reference](https://developer.apple.com/documentation/foundation/nsnetservice)_.

The `netServiceDidStop:` method gets called as a result of the `stop` message being sent to the `NSNetService` object. If this method gets called, the service is no longer published.

[Next](Browsing%20for%20Network%20Services.md)[Previous](Foundation%20Network%20Services%20Architecture.md)

