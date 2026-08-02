---
title: Networking Programming Topics
apple_id: TP40012488
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NetworkingTopics/Articles/UsingSocketsandSocketStreams.html
archived_at: '2026-07-15T08:18:51.160875Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Networking Programming Topics](Introduction.md)


[Next](Resolving%20DNS%20Hostnames.md)[Previous](Introduction.md)

# Using Sockets and Socket Streams

This article explains how to work with sockets and socket streams at various levels, from POSIX through Foundation.

At almost every level of networking, software can be divided into two categories: clients (programs that connect to other apps) and services (programs that other apps connect to). At a high level, these lines are clear. Most programs written using high-level APIs are purely clients. At a lower level, however, the lines are often blurry.

Socket and stream programming generally falls into one of the following broad categories:

- Packet-based communication—Programs that operate on one packet at a time, listening for incoming packets, then sending packets in reply.

  With packet-based communication, the only differences between clients and servers are the contents of the packets that each program sends and receives, and (presumably) what each program does with the data. The networking code itself is identical.
- Stream-based clients—Programs that use TCP to send and receive data as two continuous streams of bytes, one in each direction.

  With stream-based communication, clients and servers are somewhat more distinct. The actual data handling part of clients and servers is similar, but the way that the program initially constructs the communication channel is very different.

This chapter is divided into sections based on the above tasks:

- [Choosing an API Family](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpinedomznknlte)—Describes how to decide which API family to use when writing networking code.
- [Writing a TCP-Based Client](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpinedomznknlti)—Describes how to make outgoing TCP connections to existing servers and services.
- [Writing a TCP-Based Server](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpinedomznknltq)—Describes how to listen for incoming TCP connections when writing servers and services.
- [Working with Packet-Based Sockets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpinedomznknltcmq)—Describes how to work with non-TCP protocols, such as UDP.

The API you choose for socket-based connections depends on whether you are making a connection to another host or receiving a connection from another host. It also depends on whether you are using TCP or some other protocol. Here are a few factors to consider:

- In OS X, if you already have networking code that is shared with non-Apple platforms, you can use POSIX C networking APIs and continue to use your networking code as-is (on a separate thread). If your program is based on a Core Foundation or Cocoa (Foundation) run loop, you can also use the Core Foundation `CFStream` API to integrate the POSIX networking code into your overall architecture on the main thread. Alternatively, if you are using Grand Central Dispatch (GCD), you can add a socket as a dispatch source.

  In iOS, POSIX networking is discouraged because it does not activate the cellular radio or on-demand VPN. Thus, as a general rule, you should separate the networking code from any common data processing functionality and rewrite the networking code using higher-level APIs.
- For daemons and services that listen on a port, or for non-TCP connections, use POSIX or Core Foundation (`CFSocket`) C networking APIs.
- For client code in Objective-C, use Foundation Objective-C networking APIs. Foundation defines high-level classes for managing URL connections, socket streams, network services, and other networking tasks. It is also the primary non-UI Objective-C framework in OS X and iOS, providing routines for run loops, string handling, collection objects, file access, and so on.
- For client code in C, use Core Foundation C networking APIs. The Core Foundation framework and the CFNetwork framework are two of the primary C-language frameworks in OS X and iOS. Together they define the functions and structures upon which the Foundation networking classes are built.

The way you make an outgoing connection depends on what programming language you are using, on the type of connection (TCP, UDP, and so forth), and on whether you are trying to share code with other (non-Mac, non-iOS) platforms.

- Use `NSStream` for outgoing connections in Objective-C.

  If you are connecting to a specific host, create a `CFHost` object (_not_ `NSHost`—they are not toll-free bridged), then use [CFStreamCreatePairWithSocketToHost](https://developer.apple.com/documentation/corefoundation/1539739-cfstreamcreatepairwithsockettoho) or [CFStreamCreatePairWithSocketToCFHost](https://developer.apple.com/documentation/cfnetwork/1426831-cfstreamcreatepairwithsockettocf) to open a socket connected to that host and port and associate a pair of `CFStream` objects with it. You can then cast these to an `NSStream` object.

  You can also use the [CFStreamCreatePairWithSocketToNetService](https://developer.apple.com/documentation/cfnetwork/1426794-cfstreamcreatepairwithsockettone) function with a [CFNetServiceRef](https://developer.apple.com/documentation/cfnetwork/cfnetservice) object to connect to a Bonjour service. Read [Discovering and Advertising Network Services](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/Discovering,Browsing,AndAdvertisingNetworkServices/Discovering,Browsing,AndAdvertisingNetworkServices.html#//apple_ref/doc/uid/TP40010220-CH9) in _[Networking Overview](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_ for more information.
- Use `CFStream` for outgoing connections in C.

  If you are writing code that cannot include Objective-C, use the `CFStream` API. It integrates more easily with other Core Foundation APIs than `CFSocket`, and enables the cellular hardware on iOS (where applicable), unlike lower-level APIs. You can use [CFStreamCreatePairWithSocketToHost](https://developer.apple.com/documentation/corefoundation/1539739-cfstreamcreatepairwithsockettoho) or [CFStreamCreatePairWithSocketToCFHost](https://developer.apple.com/documentation/cfnetwork/1426831-cfstreamcreatepairwithsockettocf) to open a socket connected to a given host and port and associate a pair of `CFStream` objects with it.

  You can also use the [CFStreamCreatePairWithSocketToNetService](https://developer.apple.com/documentation/cfnetwork/1426794-cfstreamcreatepairwithsockettone) function to connect to a Bonjour service. Read [Discovering and Advertising Network Services](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/Discovering,Browsing,AndAdvertisingNetworkServices/Discovering,Browsing,AndAdvertisingNetworkServices.html#//apple_ref/doc/uid/TP40010220-CH9) in _[Networking Overview](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_ for more information.
- Use POSIX calls if cross-platform portability is required.

  If you are writing networking code that runs exclusively in OS X and iOS, you should generally avoid POSIX networking calls, because they are harder to work with than higher-level APIs. However, if you are writing networking code that must be shared with other platforms, you can use the POSIX networking APIs so that you can use the same code everywhere.

  Never use synchronous POSIX networking APIs on the main thread of a GUI application. If you use synchronous networking calls in a GUI application, you must do so on a separate thread.

The subsections below describe the use of `NSStream`. Except where noted, the `CFStream` API has functions with similar names, and behaves similarly.

To learn more about the POSIX socket API, read the UNIX Socket FAQ at [http://developerweb.net/](http://developerweb.net/).

As a rule, the recommended way to establish a TCP connection to a remote host is with streams. Streams automatically handle many of the challenges that TCP connections present. For example, streams provide the ability to connect by hostname, and in iOS, they automatically activate a device’s cellular modem or on-demand VPN when needed (unlike `CFSocket` or BSD sockets). Streams are also a more Cocoa-like networking interface than lower-level protocols, behaving in a way that is largely compatible with the Cocoa file stream APIs.

The way you obtain input and output streams for a host depends on whether you used service discovery to discover the host:

- If you already know the DNS name or IP address of the remote host, obtain Core Foundation read (input) and write (output) streams with the [CFStreamCreatePairWithSocketToHost](https://developer.apple.com/documentation/corefoundation/1539739-cfstreamcreatepairwithsockettoho) function. You can then take advantage of the toll-free bridge between `CFStream` and `NSStream` to cast your [CFReadStreamRef](https://developer.apple.com/documentation/corefoundation/cfreadstream) and [CFWriteStreamRef](https://developer.apple.com/documentation/corefoundation/cfwritestreamref) objects to [NSInputStream](https://developer.apple.com/documentation/foundation/inputstream) and [NSOutputStream](https://developer.apple.com/documentation/foundation/nsoutputstream) objects.
- If you discovered the host by browsing for network services with a `CFNetServiceBrowser` object, you obtain input and output streams for the service with the [CFStreamCreatePairWithSocketToNetService](https://developer.apple.com/documentation/cfnetwork/1426794-cfstreamcreatepairwithsockettone) function. Read [Discovering and Advertising Network Services](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/Discovering,Browsing,AndAdvertisingNetworkServices/Discovering,Browsing,AndAdvertisingNetworkServices.html#//apple_ref/doc/uid/TP40010220-CH9) in _[Networking Overview](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_ for more information.

After you have obtained your input and output streams, you should retain them immediately if you are not using automatic reference counting. Then cast them to `NSInputStream` and `NSOutputStream` objects, set their delegate objects (which should conform to the [NSStreamDelegate](https://developer.apple.com/documentation/foundation/nsstreamdelegate) protocol), schedule them on the current run loop, and call their [open](https://developer.apple.com/documentation/foundation/stream/1411963-open) methods.

When the [stream:handleEvent:](https://developer.apple.com/documentation/foundation/streamdelegate/1410079-stream) method is called on the `NSOutputStream` object’s delegate and the _streamEvent_ parameter’s value is [NSStreamEventHasSpaceAvailable](https://developer.apple.com/documentation/foundation/stream/event/1416046-hasspaceavailable), call [write:maxLength:](https://developer.apple.com/documentation/foundation/nsoutputstream/1410720-write) to send data. This method returns the number of bytes written or a negative number on error. If fewer bytes were written than you tried to send, you must queue up the remaining data and send it after the delegate method gets called again with an `NSStreamEventHasSpaceAvailable` event. If an error occurs, you should call [streamError](https://developer.apple.com/documentation/foundation/stream/1416359-streamerror) to find out what went wrong.

When the [stream:handleEvent:](https://developer.apple.com/documentation/foundation/streamdelegate/1410079-stream) method is called on your `NSInputStream` object’s delegate and the _streamEvent_ parameter’s value is [NSStreamEventHasBytesAvailable](https://developer.apple.com/documentation/foundation/stream/event/1409613-hasbytesavailable), your input stream has received data that you can read with the [read:maxLength:](https://developer.apple.com/documentation/foundation/inputstream/1411544-read) method. This method returns the number of bytes read, or a negative number on error.

If fewer bytes were read than you need, you must queue the data and wait until you receive another stream event with additional data. If an error occurs, you should call [streamError](https://developer.apple.com/documentation/foundation/stream/1416359-streamerror) to find out what went wrong.

If the other end of the connection closes the connection:

- Your connection delegate’s `stream:handleEvent:` method is called with `streamEvent` set to `NSStreamEventHasBytesAvailable`. When you read from that stream, you get a length of zero (`0`).
- Your connection delegate’s `stream:handleEvent:` method is called with `streamEvent` set to [NSStreamEventEndEncountered](https://developer.apple.com/documentation/foundation/nsstreamevent/nsstreameventendencountered).

When either of these two events occurs, the delegate method is responsible for detecting the end-of-file condition and cleaning up.

To close your connection, unschedule it from the run loop, set the connection’s delegate to `nil` (the delegate is unretained), close both of the associated streams with the [close](https://developer.apple.com/documentation/foundation/nsstream/1410399-close) method, and then release the streams themselves (if you are not using ARC) or set them to `nil` (if you are). By default, this closes the underlying socket connection. There are two situations in which you must close it yourself, however:

- If you previously set the [kCFStreamPropertyShouldCloseNativeSocket](https://developer.apple.com/documentation/corefoundation/kcfstreampropertyshouldclosenativesocket) to `kCFBooleanFalse` by calling [setProperty:forKey:](https://developer.apple.com/documentation/foundation/nsstream/1412045-setproperty) on the stream.
- If you created the streams based on an existing BSD socket by calling [CFStreamCreatePairWithSocket](https://developer.apple.com/documentation/corefoundation/1539642-cfstreamcreatepairwithsocket).

  By default, streams created from an existing native socket do not close their underlying socket. However, you can enable automatic closing by setting the [kCFStreamPropertyShouldCloseNativeSocket](https://developer.apple.com/documentation/corefoundation/kcfstreampropertyshouldclosenativesocket) to `kCFBooleanTrue` with the [setProperty:forKey:](https://developer.apple.com/documentation/foundation/nsstream/1412045-setproperty) method.

To learn more, read [Setting Up Socket Streams](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Articles/NetworkStreams.html#//apple_ref/doc/uid/20002277) in _[Stream Programming Guide](../../Cocoa/Stream%20Programming%20Guide/Introduction%20to%20Stream%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dq2i)_, _[Using NSStreams For A TCP Connection Without NSHost](https://developer.apple.com/library/archive/qa/qa1652/_index.html#//apple_ref/doc/uid/DTS40008977)_, or see the _[SimpleNetworkStreams](../../../samplecode/SimpleNetworkStreams/SimpleNetworkStreams.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojxhe)_ and _[RemoteCurrency](../../../samplecode/RemoteCurrency/RemoteCurrency.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrgy)_ sample code projects.

As mentioned previously, a server and a client are similar once the connection is established. The main difference is that clients make outgoing connections, whereas servers create a _listening socket_ (sometimes listen socket)—a socket that listens for incoming connections—then accept connections on that socket. After that, each resulting connection behaves just like a connection you might make in a client.

The API you should choose for your server depends primarily on whether you are trying to share the code with other (non-Mac, non-iOS) platforms. There are only two APIs that provide the ability to listen for incoming network connections: the Core Foundation socket API and the POSIX (BSD) socket API. Higher-level APIs cannot be used for accepting incoming connections.

- If you are writing code for OS X and iOS exclusively, use POSIX networking calls to set up your network sockets. Then, use GCD or `CFSocket` to integrate the sockets into your run loop.
- Use pure POSIX networking code with a POSIX-based run loop ([select](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/select.2.html#//apple_ref/doc/man/2/select)) if cross-platform portability with non-Apple platforms is required.

  If you are writing networking code that runs exclusively in OS X and iOS, you should generally avoid POSIX networking calls because they are harder to work with than higher level APIs. However, if you are writing networking code that must be shared with other platforms, you can use the POSIX networking APIs so that you can use the same code everywhere.
- Never use `NSSocketPort` or `NSFileHandle` for general socket communication. For details, see [Do Not Use NSSocketPort (OS X) or NSFileHandle for General Socket Communication](../../Networking%20Internet%20Web/Networking%20Overview/Avoiding%20Common%20Networking%20Mistakes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqnbnknltg) in _[Networking Overview](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_.

The following sections describe how to use these APIs to listen for incoming connections.

To use Core Foundation APIs to listen for incoming connections, you must do the following:

1. Add appropriate includes:

```c
#include <CoreFoundation/CoreFoundation.h>
#include <sys/socket.h>
#include <netinet/in.h>
```
2. Create socket objects (returned as a [CFSocketRef](https://developer.apple.com/documentation/corefoundation/cfsocketref) object) with the [CFSocketCreate](https://developer.apple.com/documentation/corefoundation/1543527-cfsocketcreate) or [CFSocketCreateWithNative](https://developer.apple.com/documentation/corefoundation/1543295-cfsocketcreatewithnative) function. Specify [kCFSocketAcceptCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/1541536-acceptcallback) as the `callBackTypes` parameter value. Provide a pointer to a [CFSocketCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallback) callback function as the _callout_ parameter value.

```
CFSocketRef myipv4cfsock = CFSocketCreate(
    kCFAllocatorDefault,
    PF_INET,
    SOCK_STREAM,
    IPPROTO_TCP,
    kCFSocketAcceptCallBack, handleConnect, NULL);
CFSocketRef myipv6cfsock = CFSocketCreate(
    kCFAllocatorDefault,
    PF_INET6,
    SOCK_STREAM,
    IPPROTO_TCP,
    kCFSocketAcceptCallBack, handleConnect, NULL);
```
3. Bind a socket with the [CFSocketSetAddress](https://developer.apple.com/documentation/corefoundation/1542729-cfsocketsetaddress) function. Provide a `CFData` object containing a `sockaddr` struct that specifies information about the desired port and family.

```
struct sockaddr_in sin;

memset(&sin, 0, sizeof(sin));
sin.sin_len = sizeof(sin);
sin.sin_family = AF_INET; /* Address family */
sin.sin_port = htons(0); /* Or a specific port */
sin.sin_addr.s_addr= INADDR_ANY;

CFDataRef sincfd = CFDataCreate(
    kCFAllocatorDefault,
    (UInt8 *)&sin,
    sizeof(sin));

CFSocketSetAddress(myipv4cfsock, sincfd);
CFRelease(sincfd);

struct sockaddr_in6 sin6;

memset(&sin6, 0, sizeof(sin6));
sin6.sin6_len = sizeof(sin6);
sin6.sin6_family = AF_INET6; /* Address family */
sin6.sin6_port = htons(0); /* Or a specific port */
sin6.sin6_addr = in6addr_any;

CFDataRef sin6cfd = CFDataCreate(
    kCFAllocatorDefault,
    (UInt8 *)&sin6,
    sizeof(sin6));

CFSocketSetAddress(myipv6cfsock, sin6cfd);
CFRelease(sin6cfd);
```
4. Begin listening on a socket by adding the socket to a run loop.

   Create a run-loop source for a socket with the [CFSocketCreateRunLoopSource](https://developer.apple.com/documentation/corefoundation/1542740-cfsocketcreaterunloopsource) function. Then, add the socket to a run loop by providing its run-loop source to the [CFRunLoopAddSource](https://developer.apple.com/documentation/corefoundation/1543356-cfrunloopaddsource) function.

```
CFRunLoopSourceRef socketsource = CFSocketCreateRunLoopSource(
    kCFAllocatorDefault,
    myipv4cfsock,
    0);

CFRunLoopAddSource(
    CFRunLoopGetCurrent(),
    socketsource,
    kCFRunLoopDefaultMode);

CFRunLoopSourceRef socketsource6 = CFSocketCreateRunLoopSource(
    kCFAllocatorDefault,
    myipv6cfsock,
    0);

CFRunLoopAddSource(
    CFRunLoopGetCurrent(),
    socketsource6,
    kCFRunLoopDefaultMode);
```

After this, you can access the underlying BSD socket descriptor with the [CFSocketGetNative](https://developer.apple.com/documentation/corefoundation/1543617-cfsocketgetnative) function.

When you are through with the socket, you must close it by calling [CFSocketInvalidate](https://developer.apple.com/documentation/corefoundation/1542010-cfsocketinvalidate).

In your listening socket’s callback function (`handleConnect` in this case), you should check to make sure the value of the _callbackType_ parameter is [kCFSocketAcceptCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/1541536-acceptcallback), which means that a new connection has been accepted. In this case, the _data_ parameter of the callback is a pointer to a [CFSocketNativeHandle](https://developer.apple.com/documentation/corefoundation/cfsocketnativehandle) value (an integer socket number) representing the socket.

To handle the new incoming connections, you can use the `CFStream`, `NSStream`, or `CFSocket` APIs. The stream-based APIs are strongly recommended.

To do this:

1. Create read and write streams for the socket with the [CFStreamCreatePairWithSocket](https://developer.apple.com/documentation/corefoundation/1539642-cfstreamcreatepairwithsocket) function.
2. Cast the streams to an `NSInputStream` object and an `NSOutputStream` object if you are working in Cocoa.
3. Use the streams as described in [Writing a TCP-Based Client](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpinedomznknlti).

For more information, see _[CFSocket Reference](https://developer.apple.com/documentation/corefoundation/cfsocket-rg7)_. For sample code, see the _[RemoteCurrency](../../../samplecode/RemoteCurrency/RemoteCurrency.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrgy)_ and _[WiTap](../../../samplecode/WiTap/WiTap.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydomzsge)_ sample code projects.

POSIX networking is fairly similar to the `CFSocket` API, except that you have to write your own run-loop-handling code.

Here are the basic steps for creating a POSIX-level server:

1. Create a socket by calling [socket](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/socket.2.html#//apple_ref/doc/man/2/socket). For example:

```
int ipv4_socket = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
int ipv6_socket = socket(PF_INET6, SOCK_STREAM, IPPROTO_TCP);
```
2. Bind it to a port.

   - If you have a specific port in mind, use that.
   - If you don’t have a specific port in mind, pass zero for the port number, and the operating system will assign you an ephemeral port. (If you are going to advertise your service with Bonjour, you should almost always use an ephemeral port.)

   For example:

```
    struct sockaddr_in sin;
    memset(&sin, 0, sizeof(sin));
    sin.sin_len = sizeof(sin);
    sin.sin_family = AF_INET; // or AF_INET6 (address family)
    sin.sin_port = htons(0);
    sin.sin_addr.s_addr= INADDR_ANY;

    if (bind(listen_sock, (struct sockaddr *)&sin, sizeof(sin)) < 0) {
        // Handle the error.
    }
```
3. If you are using an ephemeral port, call `getsockname` to find out what port you are using. You can then register this port with Bonjour. For example:

```
    socklen_t len = sizeof(sin);
    if (getsockname(listen_sock, (struct sockaddr *)&sin, &len) < 0) {
        // Handle error here
    }
    // You can now get the port number with ntohs(sin.sin_port).
```
4. Call `listen` to begin listening for incoming connections on that port.

The next steps depend on whether you intend to use pure POSIX socket code or a higher level abstraction.

Call [CFSocketCreateWithNative](https://developer.apple.com/documentation/corefoundation/1543295-cfsocketcreatewithnative). Then follow the directions in [Listening with Core Foundation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpinedomznknlts), beginning at step 3.

GCD allows you to perform operations asynchronously, and provides an event queue mechanism for determining when to read data from the socket. After creating the listening socket, a GCD-based server should:

1. Call `dispatch_source_create` to create a dispatch source for the listening socket, specifying `DISPATCH_SOURCE_TYPE_READ` as the source type.
2. Call `dispatch_source_set_event_handler` (or `dispatch_source_set_event_handler_f` and `dispatch_set_context`) to set a handler that gets called whenever a new connection arrives on the socket.
3. When the listen socket handler is called (upon a new connection), it should:

   - Call [accept](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/accept.2.html#//apple_ref/doc/man/2/accept). This function fills a new `sockaddr` structure with information about the connection and returns a new socket for that connection.

     If desired, call `ntohl(my_sockaddr_obj.sin_addr.s_addr)` to determine the client’s IP address.
   - Call `dispatch_source_create` to create a dispatch source for the client socket, specifying `DISPATCH_SOURCE_TYPE_READ` as the source type.
   - Call `setsockopt` to set the `SO_NOSIGPIPE` flag on the socket.
   - Call `dispatch_source_set_event_handler` (or `dispatch_source_set_event_handler_f` and `dispatch_set_context`) to set a handler that gets called whenever the state of the connection changes.
4. In the client socket handler, call `dispatch_async` or `dispatch_async_f` and pass a block that calls [read](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/read.2.html#//apple_ref/doc/man/2/read) on the socket to grab any new data, then handle that data appropriately. This block can also send responses by calling [write](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/write.2.html#//apple_ref/doc/man/2/write) on the socket.

1. Create a file descriptor set and add new sockets to that set as new connections come in.

```
fd_set incoming_connections;
memset(&incoming_connections, 0, sizeof(incoming_connections));
```
2. If you need to perform actions periodically on your networking thread, construct a `timeval` structure for the `select` timeout.

```
    struct timeval tv;
    tv.tv_sec = 1; /* 1 second timeout */
    tv.tv_usec = 0; /* no microseconds. */
```

   It is important to choose a timeout that is reasonable. Short timeout values bog down the system by causing your process to run more frequently than is necessary. Unless you are doing something very unusual, your `select` loop should not wake more than a few times per second, at most, and on iOS, you should try to avoid doing this at all. For alternatives, read [Avoid POSIX Sockets and CFSocket on iOS Where Possible](../../Networking%20Internet%20Web/Networking%20Overview/Avoiding%20Common%20Networking%20Mistakes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqnbnknlte) in _[Networking Overview](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_.

   If you do not need to perform periodic actions, pass `NULL`.
3. Call `select` in a loop, passing _two separate copies_ of that file descriptor set (created by calling `FD_COPY`) for the read and write descriptor sets. The `select` system call modifies these descriptor sets, clearing any descriptors that are not ready for reading or writing.

   For the `timeout` parameter, pass the `timeval` structure you created earlier. Although OS X and iOS do not modify this structure, some other operating systems replace this value with the amount of time remaining. Thus, for cross-platform compatibility, you must reset this value each time you call `select`.

   For the `nfds` parameter, pass a number that is one higher than the highest-numbered file descriptor that is actually in use.
4. Read data from sockets, calling `FD_ISSET` to determine if a given socket has pending data.

   Write data to calling `FD_ISSET` to determine if a given socket has room for new data.

   Maintain appropriate queues for incoming and outgoing data.

As an alternative to the POSIX [select](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/select.2.html#//apple_ref/doc/man/2/select) function, the BSD-specific [kqueue](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/kqueue.2.html#//apple_ref/doc/man/2/kqueue) API can also be used to handle socket events.

To learn more about POSIX networking, read the [socket](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/socket.2.html#//apple_ref/doc/man/2/socket), [listen](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/listen.2.html#//apple_ref/doc/man/2/listen), [FD_SET](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/FD_SET.2.html#//apple_ref/doc/man/2/FD_SET), and [select](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/select.2.html#//apple_ref/doc/man/2/select) manual pages.

The recommended way to send and receive UDP packets is by combining the POSIX API and either the `CFSocket` or GCD APIs. To use these APIs, you must perform the following steps:

1. Create a socket by calling [socket](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/socket.2.html#//apple_ref/doc/man/2/socket).
2. Bind the socket by calling [bind](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/bind.2.html#//apple_ref/doc/man/2/bind). Provide a `sockaddr` struct that specifies information about the desired port and family.
3. Connect the socket by calling [connect](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/connect.2.html#//apple_ref/doc/man/2/connect) (optional).

   Note that a connected UDP socket is not a connection in the purest sense of the word. However, it provides two advantages over an unconnected socket. First, it removes the need to specify the destination address every time you send a new message. Second, your app _may_ receive errors when a packet cannot be delivered. This error delivery is not guaranteed with UDP, however; it is dependent on network conditions that are beyond your app’s control.

From there, you can work with the connection in three ways:

- If you are using GCD for run loop integration (recommended), create a dispatch source by calling `dispatch_source_create`. Assign an event handler to the dispatch source. Optionally assign a cancellation handler. Finally, pass the dispatch source to the `dispatch_resume` function to begin handling events.
- If you are using `CFSocket` for integration, this technique is somewhat more complicated, but makes it easier to interface your code with some Cocoa APIs. However, `CFSocket` objects use a single object to represent a connection (much like sockets at the POSIX layer), whereas most Cocoa APIs are designed to interface with stream-based APIs that use separate objects for sending and receiving. As a result, some Cocoa APIs that expect read or write streams may be difficult to use in conjunction with `CFSocketRef` objects.

  To use `CFSocket`:

  1. Create an object to use for managing the connection. If you are writing Objective-C code, this can be a class. If you are writing pure C code, this should be a Core Foundation object, such as a mutable dictionary.
  2. Create a context object to describe that object.

```
CFSocketContext ctxt;

ctxt.version = 0;
ctxt.info = my_context_object;
ctxt.retain = CFRetain;
ctxt.release = CFRelease;
ctxt.copyDescription = NULL;
```
  3. Create a `CFSocket` object ([CFSocketRef](https://developer.apple.com/documentation/corefoundation/cfsocketref)) for the `CFSocketNativeHandle` object by calling [CFSocketCreateWithNative](https://developer.apple.com/documentation/corefoundation/1543295-cfsocketcreatewithnative).

     Be sure to set (at minimum) the [kCFSocketDataCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/kcfsocketdatacallback) flag in your `callBackTypes` parameter value. _Do not_ set the [kCFSocketAcceptCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/1541536-acceptcallback) flag.

     You’ll also need to provide a pointer to a [CFSocketCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallback) callback function as the _callout_ parameter value.

     For example:

```
CFSocketRef connection = CFSocketCreateWithNative(kCFAllocatorDefault,
    sock,
    kCFSocketDataCallBack,
    handleNetworkData,
    &ctxt);
```
  4. Tell Core Foundation that it is allowed to close the socket when the underlying Core Foundation object is invalidated.

```
CFOptionFlags sockopt = CFSocketGetSocketFlags(connection);

sockopt |= kCFSocketCloseOnInvalidate | kCFSocketAutomaticallyReenableReadCallBack;
CFSocketSetSocketFlags(connection, sockopt);
```
  5. Create an event source for the socket and schedule it on your run loop.

```
CFRunLoopSourceRef socketsource = CFSocketCreateRunLoopSource(
    kCFAllocatorDefault,
    connection,
    0);

CFRunLoopAddSource(CFRunLoopGetCurrent(), socketsource, kCFRunLoopDefaultMode);
```

  Whenever new data becomes available, the data handler callback gets called. In your callback, if the value of the _callbackType_ parameter is [kCFSocketConnectCallBack](https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype/1542373-connectcallback), check the _data_ parameter passed into the callback. If it is `NULL`, you have connected to the host. You can then send data using the [CFSocketSendData](https://developer.apple.com/documentation/corefoundation/1543414-cfsocketsenddata) function.

  When you are finished with the socket, close and invalidate it by calling the [CFSocketInvalidate](https://developer.apple.com/documentation/corefoundation/1542010-cfsocketinvalidate) function.

  At any point, you can also access the underlying BSD socket by calling the [CFSocketGetNative](https://developer.apple.com/documentation/corefoundation/1543617-cfsocketgetnative) function.

  For more information, see _[CFSocket Reference](https://developer.apple.com/documentation/corefoundation/cfsocket-rg7)_. For sample code, see the _[UDPEcho](../../../samplecode/UDPEcho/UDPEcho.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnrwga)_ sample code project.
- If you are using pure POSIX sockets, use the [select](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/select.2.html#//apple_ref/doc/man/2/select) system call to wait for data, then use the [read](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/read.2.html#//apple_ref/doc/man/2/read) and [write](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/write.2.html#//apple_ref/doc/man/2/write) system calls to perform I/O. To learn more about sending and receiving UDP packets with the POSIX socket API, read the UNIX Socket FAQ at [http://developerweb.net/](http://developerweb.net/).

Sometimes when working with socket-based streams (`NSInputStream`, `NSOutputStream`, `CFReadStream`, or `CFWriteStream`), you may need to obtain the underlying socket handle associated with a stream. For example, you might want to find out the IP address and port number for each end of the stream with [getsockname](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/getsockname.2.html#//apple_ref/doc/man/2/getsockname) and [getpeername](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/getpeername.2.html#//apple_ref/doc/man/2/getpeername), or set socket options with [setsockopt](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/setsockopt.2.html#//apple_ref/doc/man/2/setsockopt).

To obtain the native socket handle for an input stream, call the following method:

```objc
-(int) socknumForNSInputStream: (NSStream *)stream
{
    int sock = -1;
    NSData *sockObj = [stream propertyForKey:
               (__bridge NSString *)kCFStreamPropertySocketNativeHandle];
    if ([sockObj isKindOfClass:[NSData class]] &&
         ([sockObj length] == sizeof(int)) ) {
        const int *sockptr = (const int *)[sockObj bytes];
        sock = *sockptr;
    }
    return sock;
}
```

You can do the same thing with an output stream, but you only need to do this with one or the other because the input and output streams for a given connection always share the same underlying native socket.

[Next](Resolving%20DNS%20Hostnames.md)[Previous](Introduction.md)

