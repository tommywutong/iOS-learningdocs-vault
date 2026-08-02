---
title: Porting to Mac OS X from Windows Win32 API
apple_id: 10000190i
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2011-01-05'
source_url: https://developer.apple.com/library/archive/documentation/Porting/Conceptual/win32porting/Articles/networking.html
archived_at: '2026-07-18T01:51:00.224885Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting to Mac OS X from Windows Win32 API](Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API.md)


[Next](Using%20Text%20in%20Mac%20OS%20X.md)[Previous](Multiprocessing.md)

# Networking in Mac OS X

In most cases, networking means communicating with remote locations over the Internet, and that's what this document is largely about. If that's not what you're interested in, check "Related Subjects" toward the end of this document.

The rest of this document will talk about the various Mac OS X APIs that enable you to connect to and communicate with remote locations on the Internet:

- the BSD Sockets API, which gives you full access to UNIX-style sockets, for low-level access to networking functions.
- `CFSocket`, an Apple API that uses BSD sockets, but enables the handling of multiple socket connections within one thread.
- `CFNetwork`, an Apple API that simplifies the process of transmitting and receiving HTTP messages.

Before reading about these APIs, you first need to understand a concept called _run loops_.

Many socket-based programs are designed around the use of threads. For these programs, Apple provides similar functionality to facilitate porting the code to Mac OS X. Code using BSD sockets should require only minor changes to compile and run under Mac OS X.

One of the complexities of socket use involves the use of separate threads to handle the exchange of data. In a server environment, where hundreds of sockets are open simultaneously, the code that checks all these threads for activity may cause a significant performance hit. In addition, with threads, data synchronization is often an issue, and locks are often required to guarantee that only one thread has access to a given global variable at a time.

For such situations, Apple provides _run loops_, which behave like the message loop in a Win32 application. You can use run loops to handle various input sources, including sockets. Each thread of execution has exactly one run loop, which can handle multiple input sources. When you add an input source (for example, a socket) to a thread's run loop, you must also hand it a callback function that is to be called whenever the input source needs attention.

Event-driven code is more complex than code using blocking threads, but it delivers the highest network performance. When you use a run loop to handle multiple sockets in the same thread, you avoid the data synchronization problems associated with a multiple-thread solution. The `CFSocket` API contains routines that hand off the servicing of a socket to the thread's run loop.

The following sections describe the three networking APIs you have available to you. The two higher-level APIs, `CFNetwork` and `CFSocket`, are both built on top of the third API, BSD Sockets. Each API is most useful in certain situations, so you need to decide which one to use. Documentation for these APIs resides in several places; see "For Further Information" at the end of this document for details.

BSD Sockets is the traditional UNIX API for connecting to other system processes and resources that reside on the Internet. If your Win32 code uses the Winsock API (which is itself based on BSD Sockets) for synchronous communication, you should have little trouble porting it to the Mac OS X implementation of BSD Sockets. The BSD Sockets API includes such procedures as `socket`, `bind`, `listen`, `accept`, `connect`, `read`, `write`, and `close`.

`CFSocket` provides a high-level API that uses BSD sockets to communicate with a remote Internet location, while also providing a configurable mechanism (using callback routines and the current thread's run loop) for automatically handling the data that the remote Internet location returns. For example you can:

- configure a `CFSocket` to automatically read incoming data or to call the callback routine when data is available to be read,
- configure a callback to be disabled or automatically reenabled after it has been triggered,
- manually enable or disable a callback,
- make the network connection in the background,

You will probably want to use the `CFSocket` API if your current networking code uses Winsock in its asynchronous mode.

CFNetwork is a high-level networking API that makes it easy to create, send, and receive the kinds of messages that are commonly exchanged between clients and servers. It currently includes support for HTTP messages; support for other protocols (including SMTP, LDAP, and FTP) is planned for the future.

CFNetwork has functions for

- sending and receiving both HTTP requests and HTTP responses.
- getting and setting the various components of an HTTP message (for example, `CFHTTPMessageSetBody`, `CFHTTPMessageGetResponseStatusCode`).
- getting information about the message itself (for example, getting the message's HTTP version).
- creating HTTP streams for sending HTTP messages and receiving the response to them.

The following list gives you an idea of how to work with CFNetwork by showing you the routines you would use to create and send an HTTP request message.

- creating messages

  - create an HTTP request with `CFHTTPMessageCreateRequest`
  - set the message body with `CFHTTPMessageSetBody`
  - set the header with `CFHTTPMessageSetHeaderFieldValue`
  - verify the correctness of the headers by calling `CFHTTPMessageIsHeaderComplete`
  - serialize the message by calling `CFHTTPMessageCopySerializedMessage`
- sending messages

  - use `CFReadStreamCreateForHTTPRequest` to create an HTTP stream for transmitting an already created HTTP request message
  - Note: you can also send a message using a `CFSocket` or a BSD socket (discussed below)
- message cleanup

  - use `CFRelease` to dispose of the original message and its serialized version
- stream cleanup

  - close the stream using `CFReadStreamClose`
  - guarantee that the stream never uses its callback function by calling `CFReadStreamSetClient` with `NULL` arguments
  - prevent the stream from calling the existing callback using `CFReadStreamUnscheduleFromRunLoop`
  - release the reference on the stream using `CFRelease`

Networking means different things to different people. The subsections below introduce two network-related resources you may find of interest. Pointers to relevant documentation are given in "For Further Information," below.

This framework is used system-wide to allow various system resources to be configured under program control. In the context of networking, you might use this framework to configure network settings for the user and to change them automatically as network services are added and removed.

Apple's Rendezvous technology, first made available in Mac OS X version 10.2 (Jaguar), enables both wireless and wire-connected computers, peripherals, and consumer devices to automatically connect to an ad hoc network. If you are interested in building this technology into your application, `CFNetwork` includes a Network Services API, `CFNetServices`, for doing so.

Network Services (also called `CFNetServices`) makes it possible for you to register your network service, along with a human-readable name and all the information needed to connect to your service. You can also create a network service browser, which enables you to browse for other registered services that you can connect to.

If your interest in networking relates to writing software to communicate with associated networking hardware (for example, device drivers for a network interface card), you need to know about the I/O Kit. This is a collection of frameworks, libraries, tools, and other resources for creating device drivers for Mac OS X. The I/O Kit uses an object-oriented approach and is designed to make the creation of device drivers faster and easier.

Most of the documentation for Mac OS X's networking APIs is contained in header files, man pages, and books on UNIX network programming. See the notes below for help on accessing these forms of documentation.

|  |  |
| --- | --- |
| CFRunLoop documentation in header file | CFRunLoop.h |
| BSD Sockets | See the man pages for individual commands.  One recommended book on the subject is _UNIX Network Programming, Network APIs: Sockets and XTI, Volume 1, 2nd Edition_, by W. Richard Stevens, published by Prentice Hall, ISBN 0-13-490012-X. |
| Microsoft Winsock 2.2 API documentation (includes "Deviation from BSD Sockets" section) | [ftp://ftp.microsoft.com/bussys/winsock/winsock2/WSAPI22.DOC](ftp://ftp.microsoft.com/bussys/winsock/winsock2/WSAPI22.DOC) |
| CFSocket documentation in header file | `CFSocket.h` |
| CFNetwork documentation | _[CFNetwork Programming Guide](../../Networking/CFNetwork%20Programming%20Guide/Introduction%20to%20CFNetwork%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzs)_ |
| CFNetwork documentation in header files | `CFNetwork.h`, `CFHTTPMessage.h`, `CFHTTPStream.h`, `CFSocketStream.h`, and `CFNetServices.h` |
| Release Notes for CFNetwork and CFNetServices in Mac OS X v10.2 | _[CFNetwork Framework Release Notes](https://developer.apple.com/library/archive/releasenotes/Networking/RN-CFNetwork/index.html#//apple_ref/doc/uid/TP40000990)_ |
| Hardware & Drivers Documentation | [Guides > Hardware & Drivers](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP40003576) |
| I/O Kit Fundamentals book | _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ |
| Networking sessions at WWDC 2002 | \* session 808--Managing I/O: CFRunLoop and CFStream \* session 803--Mac OS X Networking Overview \* session 805--Introducing CFNetwork  available for purchase at [http://developer.apple.com/adctv/](https://developer.apple.com/adctv/) |

[Next](Using%20Text%20in%20Mac%20OS%20X.md)[Previous](Multiprocessing.md)

