---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/TCPTransports_TCPTransport_swift.html
archived_at: '2026-07-18T03:26:01.319677Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](LICENSE.txt.md)[Previous](TCPTransports-StreamTaskTransport.swift.md)

# TCPTransports/TCPTransport.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Generic TCP transport API adopted by each concrete implementation.
 */

import Foundation

/// This protocol describes an object that can manage a TCP connection in some
/// unspecified way.  Concrete implementations might use BSD Sockets,
/// CFSocketStream, or whatever.
///
/// For the sake of simplicity this protocol defines that all work must be
/// confined to a single queue.  All methods must be called from that queue and
/// all delegate methods will be called back on that queue.  The sample as a
/// whole always uses the main queue, but you could take the code and use it in
/// a program that has other queues.
///
/// Another simplification is that this protocol does not implement flow control:
///
/// * On the read side, there’s no way to stop the transport from reading all
///   the data off the connection.
///
/// * On the write side, there’s no indication that data has backed up in the
///   send buffer, so if the client issues an unbounded number of sends then the
///   transport will buffer an unbounded amount of data
///
/// In the use case illustrated by this sample — a simple interactive chat app
/// based on a line-based protocol — this isn’t a problem. In other scenarios,
/// like sending a large file, this would be disasterous.  In that case you
/// won’t be able to use this protocol or its implementations directly.
///
/// This protocol sends and receives lines.  Each implementation is responsible
/// for framing those lines on the wire.  In fact, each implementation uses the
/// code in `LineFraming.swift` to frame the lines using the standard terminator
/// used in network protocols (CR LF). It would be relatively easy to change
/// this protocol to use some other message format (something encoded in binary)
/// and then change an implementation to use a different framing and
/// unframing type.  In fact, you could even make `TCPTransport` generic in that
/// type.  I didn’t do this because I was trying to keep things simple.

protocol TCPTransport : AnyObject {

    /// A dispatch queue to which the queue is confined.  Specifically:
    ///
    /// * The client must call any methods like `start()` and `stop()` on that
    ///   queue.
    ///
    /// * The object will call all delegate methods on that queue.
    ///
    /// This is typically under the client’s control, set via the initialiser
    /// function.  The transport typically uses this internally but that’s not
    /// required.

    var queue: DispatchQueue { get }

    /// A delegate object, methods on which are called to indicate events on the
    /// transport.

    var delegate: TCPTransportDelegate? { get set }

    /// A high-level summary of the state of the transport.

    var transportState: TCPTransportState { get }

    /// Starts the TCP connection; can only be called once, in the
    /// `.initialised` state.

    func start()

    /// Sends a message over the transport.  Can only be called in the
    /// `.started` state.
    ///
    /// - Parameter message: The message to sent, as a single line of text.

    func send(message: String)

    /// Stops the transport.  Can be called in any state, including the
    /// `.stopped` state.  Once the transport is stopped it cannot be restarted.
    ///
    /// - warning: If you start the transport you must ensure that it has
    ///   stopped before releasing your last reference to it.
    ///
    /// The stream stops in two different ways:
    ///
    /// * You calling this method
    ///
    /// * The stream stopping on its own, in which case it calls the
    ///   `didStop(transport:)` delegate callback
    ///
    /// As it’s safe to call `stop()` in the `.stopped` state, it’s a good idea
    /// to call `stop()` before releasing your primary reference.

    func stop()
}

/// The delegate protocol for `TCPTransport`.

protocol TCPTransportDelegate : AnyObject {

    /// Called after the transports has started, that is, when the TCP
    /// connection comes up.  The state will be `.started`.
    ///
    /// - Parameter transport: The associated transport object.

    func didStart(transport: TCPTransport)

    /// Called when a message arrives over the transport.  The state will be
    /// `.started`.
    ///
    /// - Parameters:
    ///   - message: The newly arrived message.
    ///   - transport: The associated transport object.

    func didReceive(message: String, transport: TCPTransport)

    /// Called when the transport stops of its own accord.  By the time this is
    /// called, the transport is in the `.stopped` state.  The associated error
    /// value should give you some indication as to why it stopped.  A nil value
    /// means it stopped because of EOF.
    ///
    /// - important: This is not called if the transport stops because you
    ///     called `.stop()`.
    ///
    /// - Parameter transport: The associated transport object.

    func didStop(transport: TCPTransport)
}

/// The possible transport states.
///
/// - initialised: The transport has been created by not started.
/// - starting: The transport is starting up, that is, the TCP connection is
///     connecting.
/// - started: The transport has started up, that is, the TCP connection is in
///     place.
/// - stopped: The transport has stopped.  If the error is nil the transport
///     stopped because either the client called `stop()` or an EOF on the TCP
///     connection. If the error is not nil, something went wrong with the TCP
///     connection.

enum TCPTransportState {
    case initialised
    case starting
    case started
    case stopped(Error?)
}
```

[Next](LICENSE.txt.md)[Previous](TCPTransports-StreamTaskTransport.swift.md)

