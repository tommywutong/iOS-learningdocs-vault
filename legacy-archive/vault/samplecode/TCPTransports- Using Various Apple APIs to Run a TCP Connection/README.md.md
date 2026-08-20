---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/README_md.html
archived_at: '2026-07-18T03:26:00.300314Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](TCPTransports-SocketStreamTransport.swift.md)[Previous](Tests-LineFramingTests.swift.md)

# README.md

```shell
# TCPTransports

TCPTransports shows how to use various Apple APIs to run a TCP connection, including:

* `CFSocketStream`, via the `NSStream` API (`Stream` in Swift)
* `NSURLSessionStreamTask` (`URLSessionStreamTask` in Swift)
* BSD Sockets
* `NWTCPConnection` (but see the *Caveats* section)

For those APIs that support TLS ([Transport Layer Security][refTLS], common known by its old name, *SSL*), you can choose whether to enable TLS on top of your TCP connection.

[refTLS]: <https://en.wikipedia.org/wiki/Transport_Layer_Security>


## Requirements

### Build

Xcode 9.3

The sample was built using Xcode 9.3 on macOS 10.13.4 with the iOS 11.3 SDK.  You should be able to open the project, select the *App-iOS* scheme, and choose *Product* > *Build*.

### Runtime

iOS 11.0 or later

Although the sample requires iOS 11, the basic techniques it shows should work on any version of any Apple platform that supports the TCP API in question.


## Packing List

The sample contains the following items:

* `README.md` — This file.

* `LICENSE.txt` — The standard sample code licence.

* `TCPTransports.xcodeproj` — An Xcode project for the program.

* `App-iOS` — A directory containing the iOS app code.

* `Model` — A directory containing the model-level code for the app.

* `TCPTransports` — A directory containing the TCP transport code; this is the beating heart of the sample and is discussed in detail below.

* `Tests` — A directory containing unit tests.

Of the directories listed above, the most important is `TCPTransports`, which contains:

* `TCPTransport.swift` — A protocol that forms the common interface between the app and the various transports.

* `LineFraming.swift` — Types that convert lines of text to `Data` (framing) and vice versa (unframing).

* `SocketStreamTransport.swift` — An implementation of `TCPTransport` that uses `CFSocketStream` via the `NSStream` API.

* `StreamTaskTransport.swift` — An implementation of `TCPTransport` that uses `NSURLSessionStreamTask`.

* `BSDSocketsTransport.swift` — An implementation of `TCPTransport` that uses BSD Sockets.

* `NWTCPTransport.swift` — An implementation of `TCPTransport` that uses `NWTCPConnection`.

The `App-iOS` directory contains:

* `Info.plist`, `LaunchScreen.storyboard`, `Localizable.strings` — Various boilerplate resources.

* `Main.storyboard` — The main storyboard for the app.

* `AppDelegate.swift` — The main app controller. This manages the endpoint picker and the active conversation.

* `EndpointPicker.swift` — The first view displayed by the app, which lets the user configure and connect a TCP connection.

* `ActiveConversation.swift` — A controller that binds together a conversation view controller and a conversation transport.

* `ConversationViewController.swift` — Displays a conversation and lets the user enter new messages.

The `Model` directory contains:

* `Endpoint.swift` — Describes how to make a TCP connection, that is, the transport, the host name and port to connect to, and whether to use TLS. This file also adds an initialiser to the conversation transport to create a conversation transport from an endpoint.

* `ConversationTransport.swift` — Binds together a TCP transport and a conversation, such that messages sent and received on the transport are reflected in the conversation.

* `Conversation.swift` — A ‘pure’ model type that holds a conversation.

* `Message.swift` — A ‘pure’ model type that holds a message within a conversation.


## Using the Sample

### Testing TCP

Testing a simple TCP connection is relatively straightforward. First, you need to set up a server. The easiest way to do that is to use the `nc` command on your Mac. For example:

    $ while true; do date; nc -c -l 12345; done

This prints the date and time, and then starts a server. Once a client connects the server will print any data it receives from the client as text, and send to the client any lines you enter in the terminal window. You can hit control-D to disconnect from the server side. If the client disconnects, this command will print the date and time and then start listening for connections again.  Hit control-C to stop the server completely.

You can then run the app as follows:

1. Build and run the app, either on the device or the simulator.

2. Enter the DNS name of the server into the *Host* field. If you’re running on the simulator and you’re running `nc` on the same Mac, you can leave this as 127.0.0.1. If you’re running on a real device, the best option is to use the local DNS name of your Mac, which you can find in the *Sharing* preferences panel (for example, if your computer is called *Guy Smiley’s iMac* the local DNS name will be shown as `Guy-Smileys-iMac.local`, although DNS names are case insensitive and traditionally entered in lower case, hence `guy-smileys-imac.local`).

3. Choose a transport from the list.

4. Tap *Connect*. This will display a conversation view, in which you can enter messages that are sent to the server, see messages received from the server, and disconnect (via the *Done* button).

### Testing with TLS Enabled

Testing with TLS enabled is a bit trickier.  You will need the following:

* A built copy of the [TLSTool][TLSTool] sample code

* A digital identity for your server’s local DNS name

[TLSTool]: <https://developer.apple.com/library/mac/samplecode/SC1236/>

**Note** If you don’t have a digital identity, you can generate one using the instructions in Technote 2326 [Creating Certificates for TLS Testing][tn2326]. You must also install and trust your certificate authority’s certificate on the client device, as explained in QA1948 [HTTPS and Test Servers][qa1948].

[tn2326]: <https://developer.apple.com/library/mac/technotes/tn2326/_index.html>

[qa1948]: <https://developer.apple.com/library/mac/#qa/qa1948/_index.html>

With these in place you can run your server as follows:

1. Move your copy of the built `TLSTool` executable into a directory that’s in your path.

2. Run your server using the following command:

        $ while true; do date; TLSTool s_server -cert guy-smileys-imac.local -accept 12345 -crlf; done

    where `guy-smileys-imac.local` is the name of the server’s digital identity in your keychain.  If you generate your server’s digital identity using the instructions in [TN2326][tn2326], this will match the local DNS name of your server.

3. Run the client as described above, but this time enable the *Use TLS* switch.

**IMPORTANT** When connecting over TLS make sure to not enter a trailing dot in the *Host* name field of the app (that is, enter `guy-smileys-imac.local` and not `guy-smileys-imac.local.`). This trailing dot can cause problems for TLS server trust evaluation.


## How it Works

Each instance of `TCPTransport` must be confined to a single dispatch queue. You are expected to supply this queue when you create the instance and then call methods on the instance from that queue. Moreover, delegate callbacks from that instance are executed on that queue.

This app always uses the main queue for this, but you could do differently in your app.

Unlike the actual TCP protocol, the `TCPTransport` protocol does not support flow control. Specifically:

* On the read side, there’s no way to stop the transport from reading all the data off the connection.

* On the write side, there’s no indication that data has backed up in the send buffer, so if the client issues an unbounded number of sends then the transport will buffer an unbounded amount of data

In the use case illustrated by this sample — a simple interactive chat app using a line-based protocol — this isn’t a problem. In other scenarios, like sending a large file, this would be disasterous.  In that case you won’t be able to use this protocol or its implementations directly.  You will have to come up with your own design as to how best to wrangle flow control.

The `TCPTransport` protocol works in terms of message lines.  Each implementation is responsible for framing those lines on the wire.  In fact, each implementation uses the code in `LineFraming.swift` to frame the lines using the standard terminator used in network protocols (CR LF). It would be relatively easy to change this protocol to use some other message format (something encoded in binary) and then change an implementation to use a different framing and unframing type.  In fact, you could even make `TCPTransport` generic in that type.  I didn’t do this because I was trying to keep things simple.

The implementations of `TCPTransport` use reasonable defaults and have no configuration. For example, they all set the `maxLineLength` property of `LineUnframer` to 1024. It would be relatively easy to make these defaults configurable but I chose to keep the code as simple as possible.

One specific instance of the above is TLS server trust evaluation, where each implementation uses the OS’s default ([RFC 2818][rfc2818]) server trust evaluation. Customising this is possible (see Technote 2232 [HTTPS Server Trust Evaluation][tn2232]) but I didn’t add support for that to promote both simplicity and security.

The implementations of `TCPTransport` are somewhat redundant. I could save a lot of code by having them all based of a common subclass. I chose not to do this for a couple of reasons:

* It makes it easier to study each class in isolation.

* It reduces coupling, making it easier for you to extract code out of this sample into your projects.

[rfc2818]: <http://www.ietf.org/rfc/rfc2818.txt>

[tn2232]: <https://developer.apple.com/library/ios/#technotes/tn2232/_index.html>


## Caveats

`NWTCPConnection` is only usable within a Network Extension provider (`NEProvider`) so you can’t use the `NWTCPTransport` in the context of this app. It’s included here to act as a starting point if you happen to be working on an `NEProvider` and need an example of how to use `NWTCPConnection`.

`BSDSocketsTransport` only supports connecting to an IP address. There’s an extensive doc comment for `BSDSocketsTransport(name:address:useTLS:queue:)` that explain why this is the case.

`BSDSocketsTransport` does not support TLS. It’s possible to do this — using Secure Transport for the TLS side of things — but that is a _lot_ of complex code for something we don’t recommend in the first place.


## Feedback

If you find any problems with this sample, or you’d like to suggest improvements, please [file a bug][bug] against it.

[bug]: <http://developer.apple.com/bugreporter/>


## Version History

1.0d1 (Sep 2017) was released to a small number of developers on a one-to-one basis.

1.0d2 (Sep 2017) was released to a small number of developers on a one-to-one basis.  It includes a few relatively minor code changes, lots of comment changes, and a large test suite.

1.0 (Apr 2018) was the first shipping release.

Share and Enjoy

Apple Developer Technical Support
Core OS/Hardware

23 Apr 2018

Copyright (C) 2018 Apple Inc. All rights reserved.
```

[Next](TCPTransports-SocketStreamTransport.swift.md)[Previous](Tests-LineFramingTests.swift.md)

