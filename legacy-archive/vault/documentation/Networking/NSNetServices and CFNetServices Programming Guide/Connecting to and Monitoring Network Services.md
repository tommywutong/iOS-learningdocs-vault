---
title: NSNetServices and CFNetServices Programming Guide
apple_id: TP40002736
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSNetServiceProgGuide/Articles/ResolvingServices.html
archived_at: '2026-07-15T08:18:24.171929Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [NSNetServices and CFNetServices Programming Guide](About%20NSNetServices%20and%20CFNetServices.md)


[Next](Using%20CFNetServices.md)[Previous](Browsing%20for%20Network%20Services.md)

# Connecting to and Monitoring Network Services

This chapter describes how to connect to a Bonjour-advertised service. There are two occasions when you might need to connect to a Bonjour service:

- You have just browsed for services, and the user has chosen one.
- You have saved information about a service for later use, and you have explicitly initialized an instance of the [NSNetService](https://developer.apple.com/documentation/foundation/netservice) class with that information.

In either case, the way you connect to the service is the same. There are three ways to connect to a service, listed in order of preference:

- Using a stream-based connect-to-service method such as [getInputStream:outputStream:](https://developer.apple.com/documentation/foundation/netservice/1418325-getinputstream).
- Connecting by hostname.
- Connecting by IP address.

These techniques are described in the sections that follow. In addition, the section [Persisting a Bonjour Service](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3tqlktk44a) describes how to properly store information about a service for later reuse, and the section [Monitoring a Bonjour Service](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3tqlktk4zq) explains how a Bonjour service can provide additional information that clients can passively monitor without connecting to the service.

If you are connecting using Foundation’s raw TCP stream API (as opposed to a higher-level API, such as `NSURLConnection`), the most straightforward way to connect to a service is with a connect-to-service API, such as [getInputStream:outputStream:](https://developer.apple.com/documentation/foundation/netservice/1418325-getinputstream).

This method provides a reference to an input stream (`NSInputStream`) and an output stream (`NSOutputStream`), both of which you may access synchronously or asynchronously. To interact asynchronously, you must schedule the streams in the current run loop and assign them a delegate object. These streams provide a general-purpose means of communicating with TCP-based network services that is not tied to any specific protocol (such as HTTP).

Listing 4-1 demonstrates how to connect to a network service (`NSNetService`) using streams. Note that if you require only one of the two streams, you should pass `NULL` for the other parameter so that you do not get the other stream back. For a complete example of service resolution using `NSStream` objects, see the _[PictureSharing](../../../samplecode/PictureSharing/PictureSharing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanzrgi)_ sample code project in the Mac Developer Library.

__Listing 4-1__  Connecting to a resolved Bonjour network service

```objc
#import <sys/socket.h>
#import <netinet/in.h>

// ...

NSNetService *service;  // Assume this exists. For instance, you may
                        // have received it from an NSNetServiceBrowser
                        // delegate callback.

NSInputStream *istream = nil;
NSOutputStream *ostream = nil;

[service getInputStream:&istream outputStream:&ostream];
if (istream && ostream)
{
    // Use the streams as you like for reading and writing.
}
else
{
    NSLog(@"Failed to acquire valid streams");
}
```


If you are connecting to a Bonjour service using a higher-level API such as `NSURLConnection`, you should connect using the service’s hostname.

You can obtain the hostname for a Bonjour service by resolving the service and then calling the [hostName](https://developer.apple.com/documentation/foundation/nsnetservice/1413300-hostname) method on the `NSNetService` object. Then, pass that hostname and port to the appropriate API, just as you would any other hostname.

When Bonjour resolves a service, it does two things:

- Looks up the service name information to get a hostname and port number.
- Looks up the hostname to provide a set of IP addresses.

Because resolution can take time, especially if the service is unavailable, `NSNetService` resolves asynchronously, providing information to your app through a delegate object.

To resolve and use an `NSNetService` instance, your app must do four things:

1. Obtain an `NSNetService` instance through initialization or service discovery.
2. Resolve the service.
3. Respond to messages sent to the object’s delegate about addresses or errors.
4. Use the resulting addresses or hostname to connect to the service.

You can obtain an `NSNetService` object representing the service you want to connect to in one of two ways:

- Use `NSNetServiceBrowser` to discover services.
- Initialize a new `NSNetService` object with the name, type, and domain of a service that is known to exist, usually saved from a previous browsing session.

For information about service browsing, see [Browsing for Network Services](Browsing%20for%20Network%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3tolkcineuerkiincq).

To create an `NSNetService` object for resolution rather than publication, use the `initWithDomain:type:name:` method.

Once you have an `NSNetService` object to resolve, assign it a delegate and use the `resolveWithTimeout:` method to asynchronously resolve the service. When resolution is complete, the delegate receives a `netServiceDidResolveAddress:` message upon success or a `netService:didNotResolve:` message if an error occurred. Because the delegate receives the identity of the `NSNetService` object as part of the delegate method, one delegate can serve multiple `NSNetService` objects.

Listing 4-2 demonstrates how to initialize and resolve an `NSNetService` object for a hypothetical music-sharing service. The code initializes the object with the name `serviceName`, with the type `_music._tcp`, and with the link-local suffix `local.`. It then assigns it a delegate and asks it to resolve the name into socket addresses.

__Listing 4-2__  Resolving network services with NSNetService

```
id delegateObject = [[NetServiceResolutionDelegate alloc] init]; // Defined below
NSString *serviceName = ...;
NSNetService *service;

service = [[NSNetService alloc] initWithDomain:@"local." type:@"_music._tcp"
                                name:serviceName];
[service setDelegate:delegateObject];
[service resolveWithTimeout:5.0];
```


`NSNetService` returns resolution results to its delegate. If you are resolving a service, your delegate object should implement the following methods:

- `netServiceDidResolveAddress:`
- `netService:didNotResolve:`

Assuming that you are connecting by hostname, you can request that information as soon as your delegate’s `netServiceDidResolveAddress:` is first called. Be careful, though, because this method can be called more than once. (The reason is explained further in [Connecting to a Bonjour Service by IP Address](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3tqlktk42a).)

If resolution fails for any reason, the `netService:didNotResolve:` method is called. If the delegate receives a `netService:didNotResolve:` message, you should extract the type of error from the returned dictionary using the `NSNetServicesErrorCode` key and handle the error accordingly. For a list of possible errors, see _[NSNetService Class Reference](https://developer.apple.com/documentation/foundation/nsnetservice)_.

Listing 4-3 shows the interface for a class that acts as a delegate for multiple `NSNetService` objects, and Listing 4-4 shows its implementation. You can use this code as a starting point for more sophisticated tracking of resolved services.

__Listing 4-3__  Interface for an `NSNetService` delegate object used when resolving the service

```objc
#import <Foundation/Foundation.h>

@interface NetServiceResolutionDelegate : NSObject <NSNetServiceDelegate>
{
    // Keeps track of services handled by this delegate
    NSMutableArray *services;
}

// Other methods
- (BOOL)addressesComplete:(NSArray *)addresses
        forServiceType:(NSString *)serviceType;
- (void)handleError:(NSNumber *)error withService:(NSNetService *)service;

@end
```


__Listing 4-4__  Implementation for an `NSNetService` delegate object (resolution)

```objc
#import "NetServiceResolutionDelegate.h"

@implementation NetServiceResolutionDelegate

- (id)init
{
    self = [super init];
    if (self) {
        services = [[NSMutableArray alloc] init];
    }
    return self;
}

// Sent when addresses are resolved
- (void)netServiceDidResolveAddress:(NSNetService *)netService
{
    // Make sure [netService addresses] contains the
    // necessary connection information
    if ([self addressesComplete:[netService addresses]
            forServiceType:[netService type]]) {
        [services addObject:netService];
    }
}

// Sent if resolution fails
- (void)netService:(NSNetService *)netService
        didNotResolve:(NSDictionary *)errorDict
{
    [self handleError:[errorDict objectForKey:NSNetServicesErrorCode] withService:netService];
    [services removeObject:netService];
}

// Verifies [netService addresses]
- (BOOL)addressesComplete:(NSArray *)addresses
        forServiceType:(NSString *)serviceType
{
    // Perform appropriate logic to ensure that [netService addresses]
    // contains the appropriate information to connect to the service
    return YES;
}

// Error handling code
- (void)handleError:(NSNumber *)error withService:(NSNetService *)service
{
    NSLog(@"An error occurred with service %@.%@.%@, error code = %d",
        [service name], [service type], [service domain], [error intValue]);
    // Handle error here
}

@end
```


In networking, it is not possible to have perfect knowledge about the state of the world. All you can know with certainty is what packets you have already received. As a result, your app might think that a service is available when it isn’t, or it might think a service is not available when it is.

Because failing to show a valid service is a bigger problem for the user than showing a stale service, Bonjour deliberately errs on the side of assuming that a service is still available. This means that there are many ways a service can go away without your app immediately being aware of it:

- A device can be abruptly switched off, or the power can fail.
- A device can be unplugged from a wired network.
- A device can move out of a wireless base station’s range.
- Packet loss can prevent the “goodbye” packet from reaching its destination.

As a result, although Bonjour generally discovers new services within a few seconds, if a service goes away, the disappearance of the service may not be discovered until your app tries to connect to it and gets no response.

You should not assume that just because the Bonjour APIs report a discovered service, the service is guaranteed to be available when the software tries to access it. All discovery means is that at some time in the recent past, Bonjour received packets indicating that the service did exist, not that the service necessarily exists right now.

To minimize the impact of stale records:

- Don’t cancel resolving prematurely. Allow resolution to continue until the app successfully connects or the user cancels the attempt. An actively running service resolution serves as a hint to Bonjour that the named service does not seem to be responding.
- If service resolution returns a result but the client is unable to open a TCP connection to it within 5–10 seconds, low-level C clients should call [DNSServiceReconfirmRecord](https://developer.apple.com/documentation/dnssd/1804726-dnsservicereconfirmrecord). This call tells Bonjour that the named service is not responding and that Bonjour's cache data for the service may be stale. [Listing 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3tqlktk44q) shows an example of how to use the `DNSServiceReconfirmRecord` function.

Following these rules helps Bonjour remove stale services from browse lists faster.

__Listing 4-5__  Example of calling DNSServiceReconfirmRecord

```
            // serviceName should be in the form
            // "name.service.protocol.domain.".  For example:
            // "MyLaptop._ftp._tcp.local."
            NSString *serviceName = ...;
            NSString *              serviceName;
            NSArray *               serviceNameComponents;
            NSUInteger              serviceNameComponentsCount;
            serviceNameComponents = [serviceName componentsSeparatedByString:@"."];
            serviceNameComponentsCount = [serviceNameComponents count];
            if ( (serviceNameComponentsCount >= 5) && ([serviceNameComponents[serviceNameComponentsCount - 1] length] == 0) ) {
                protocol = [serviceNameComponents[2] lowercaseString];
                if ( [protocol isEqual:@"_tcp"] || [protocol isEqual:@"_udp"] ) {
                    fullname = [[serviceNameComponents subarrayWithRange:NSMakeRange(1, serviceNameComponentsCount - 1)] componentsJoinedByString:@"."];
                    retVal = EXIT_SUCCESS;
                    NSMutableData *     recordData;

                    recordData = [[NSMutableData alloc] init];
                    for (NSString * label in serviceNameComponents) {
                        const char *    labelStr;
                        uint8_t         labelStrLen;

                        labelStr = [label UTF8String];
                        if (strlen(labelStr) >= 64) {
                            fprintf(stderr, "%s: label too long: %s\n", getprogname(), labelStr);
                            retVal = EXIT_FAILURE;
                            break;
                        } else {
                            // cast is safe because of length check
                            labelStrLen = (uint8_t) strlen(labelStr);

                            [recordData appendBytes:&labelStrLen length:sizeof(labelStrLen)];
                            [recordData appendBytes:labelStr length:labelStrLen];
                        }
                    }

                    if ( (retVal == EXIT_SUCCESS) && ([recordData length] >= 256) ) {
                        fprintf(stderr, "%s: record data too long\n", getprogname());
                        retVal = EXIT_FAILURE;
                    }

                    if (retVal == EXIT_SUCCESS) {
                        err = DNSServiceReconfirmRecord(
                            0,
                            interfaceIndex,
                            [fullname UTF8String],
                            kDNSServiceType_PTR,
                            kDNSServiceClass_IN,
                            // cast is safe because of recordData length check above
                            (uint16_t) [recordData length],
                            [recordData bytes]
                        );
                        if (err != kDNSServiceErr_NoError) {
                            fprintf(stderr, "%s: reconfirm record error: %d\n", getprogname(), (int) err);
                            retVal = EXIT_FAILURE;
                        }
                    }
                }
            }
```


As a rule, you should not resolve a service to an IP address and port number unless you are doing something very unusual. In the dynamic world of modern networking, IP addresses can change at any time. Further, a given Bonjour service can have more than one IP address, and not all of them may be reachable. By connecting using hostnames, you avoid these problems. For more information, read [Avoid Resolving DNS Names Before Connecting to a Host](../../Networking%20Internet%20Web/Networking%20Overview/Avoiding%20Common%20Networking%20Mistakes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqnbnknltema) in _[Networking Overview](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_.

In the rare instances when connecting by IP address is required, you can do so by following the steps for resolving a Bonjour service in [Connecting by Name](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3tqlktk43q) and then using the IP addresses instead of the hostname. There are a few caveats, however:

- If you are working with IP addresses directly, be sure to perform resolution every time you use a service, because although the service name is a persistent property, the socket information (IP addresses and port number) can change from session to session.

  In particular, never store the IP address information long-term. If a user browses for a service and saves that service, such as in a printer chooser, store only the service name, type, and domain. When it is time to connect, these values can be resolved into the relevant IP address and port number. See [Persisting a Bonjour Service](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3tqlktk44a) for more information.
- The `netServiceDidResolveAddress:` method tells the delegate that the `NSNetService` object has added an address to its list of addresses for the service. However, more addresses may be added. For example, in systems that support both IPv4 and IPv6, `netServiceDidResolveAddress:` may be called two or more times—once for the IPv4 address and again for the IPv6 address.

  In this delegate method, be sure that all the required connection information is present before attempting to connect to the service. If some of the information is missing, `netServiceDidResolveAddress:` will be called later. If multiple addresses are returned from resolving a service, try to connect to each one before giving up.

If your app needs to persistently store a reference to a Bonjour service, such as in a printer chooser, store only the service name, type, and domain. By persisting only the domain, type, and name information, you ensure that your app can find the relevant service even if its IP addresses or port number has changed.

When you connect to the service later, initialize an [NSNetService](https://developer.apple.com/documentation/foundation/netservice) object with this information by calling its [initWithDomain:type:name:](https://developer.apple.com/documentation/foundation/nsnetservice/1417615-initwithdomain) method.

After you have initialized the service object, connect to the service by calling the [getInputStream:outputStream:](https://developer.apple.com/documentation/foundation/netservice/1418325-getinputstream) method or by passing the result of a [hostName](https://developer.apple.com/documentation/foundation/nsnetservice/1413300-hostname) call to a connect-by-name function or method, as described earlier in this chapter. When you do this, Bonjour automatically resolves the hostname or domain, type, and name values into the current IP addresses and port number for the service.

In some situations, an app may need to know certain information about a Bonjour service without needing to maintain a connection to that service. For example, a chat program might let the user specify a status (idle, away, and so on). Other users on the network should be able to learn this new information quickly, without each machine needing to constantly poll every other machine.

To support the dissemination of such information, Bonjour lets each service provide an arbitrary DNS `TXT` record with additional information. If you want to use this functionality in your app, you must do the following:

__When publishing a service,__ call the [setTXTRecordData:](https://developer.apple.com/documentation/foundation/netservice/1410648-settxtrecord) method to set or update the data associated with the service. This data must be encoded according to section 3.3.14 of RFC 1035.

The most straightforward way to generate compliant data is by calling [dataFromTXTRecordDictionary:](https://developer.apple.com/documentation/foundation/netservice/1413150-data) with an [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) object. In that dictionary, store _only_ the key-value pairs that you want to make available to any app that is browsing for your service.

__When browsing for services, do the following:__

- Call the [startMonitoring](https://developer.apple.com/documentation/foundation/nsnetservice/1411486-startmonitoring) method to start monitoring the `TXT` record associated with a given service.

- Implement the [netService:didUpdateTXTRecordData:](https://developer.apple.com/documentation/foundation/netservicedelegate/1413199-netservice) method to receive notification whenever a service’s `TXT` record changes.

  You can either process the resulting data yourself or call [dictionaryFromTXTRecordData:](https://developer.apple.com/documentation/foundation/netservice/1408164-dictionary) to obtain an [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) object containing the provided key-value pairs (often from a previous call to [dataFromTXTRecordDictionary:](https://developer.apple.com/documentation/foundation/netservice/1413150-data)).
- Call the [stopMonitoring](https://developer.apple.com/documentation/foundation/netservice/1413861-stopmonitoring) method when you no longer want to receive notifications about changes to a particular service.

For more details, see the documentation for the methods mentioned above.

[Next](Using%20CFNetServices.md)[Previous](Browsing%20for%20Network%20Services.md)

