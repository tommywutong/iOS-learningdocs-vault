---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/TCPTransports_StreamTaskTransport_swift.html
archived_at: '2026-07-18T03:26:01.164688Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](TCPTransports-TCPTransport.swift.md)[Previous](TCPTransports-LineFraming.swift.md)

# TCPTransports/StreamTaskTransport.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Implements `TCPTransport` on a `URLSessionStreamTask`.
 */

import Foundation

/// An implementation of the `TCPTransport` protocol that uses a `URLSessionStreamTask`
/// to run the TCP connection. This type supports both connect-by-name and TLS.
/// Out of the box this type creates a stream task in the global shared session,
/// but it would be trivial to modify it to use some custom session.
///
/// Note that streams tasks do not give any indication of connection completion,
/// so you'll never see this type in the `.starting` state.
///
/// For more information on how to to use this type, see the `TCPTransport`
/// protocol.

class StreamTaskTransport : TCPTransport {

    /// Creates an object that will communicate over a stream task created by
    /// calling the stream task maker closure.
    ///
    /// The `streamTaskMaker` closure means that the client is in change of
    /// stream task creation, which is useful because it allows the client to
    /// manage the `URLSession` in which the streams are created.
    ///
    /// - Parameters:
    ///   - name: A name for the connection; not used internally, but handy while
    ///     debuging.
    ///   - use: Whether to enable TLS or not.
    ///   - queue: The queue on which to operate; delegate callbacks are called
    ///     on this queue.
    ///   - streamTaskMaker: A closure called to create the stream task for this
    ///     connection.  The resulting stream task is ‘owned‘ by this object.
    ///     You can’t go modifying it after the fact.  The stream task must not
    ///     be resumed; this object takes care of resuming it.

    required init(name: String, useTLS: Bool, queue: DispatchQueue, streamTaskMaker: @escaping () -> URLSessionStreamTask) {
        dispatchPrecondition(condition: .onQueue(queue))
        self.name = name
        self.useTLS = useTLS
        self.queue = queue
        self.streamTaskMaker = streamTaskMaker
    }

    /// Creates an object that will communicate with the specified host and
    /// port, optionally using TLS.
    ///
    /// - Parameters:
    ///   - hostName: The host name to connect to (can be an IP address, both IPv4 and IPv6).
    ///   - port: The port on which to connect.
    ///   - useTLS: Whether to enable TLS or not.
    ///   - queue: The queue on which to operate; delegate callbacks are called
    ///     on this queue.

    convenience init(hostName: String, port: Int, useTLS: Bool, queue: DispatchQueue) {
        dispatchPrecondition(condition: .onQueue(queue))
        self.init(name: "\(hostName):\(port)", useTLS: useTLS, queue: queue, streamTaskMaker: { () -> URLSessionStreamTask in
            return URLSession.shared.streamTask(withHostName: hostName, port: port)
        })
    }

    deinit {
        // If this assert fires you’ve released the last reference to this
        // transport without stopping it.
        switch self._state {
        case .initialised: break
        case .started:     fatalError()
        case .stopped:     break
        }
    }

    /// The value passed to the initialiser.

    let name: String

    /// The value passed to the initialiser.

    let useTLS: Bool

    /// The value passed to the initialiser.

    let queue: DispatchQueue

    /// The value passed to the initialiser.

    let streamTaskMaker: () -> URLSessionStreamTask

    /// See the comments associated with the `TCPTransport` protocol.

    weak var delegate: TCPTransportDelegate? = nil

    /// See the comments associated with the `TCPTransport` protocol.

    var transportState: TCPTransportState {
        return self._state.transportState
    }

    /// See the comments associated with the `TCPTransport` protocol.

    func start() {
        dispatchPrecondition(condition: .onQueue(queue))
        self.process(event: .start)
    }

    /// See the comments associated with the `TCPTransport` protocol.

    func send(message: String) {
        dispatchPrecondition(condition: .onQueue(queue))
        self.process(event: .send(message: message))
    }

    /// See the comments associated with the `TCPTransport` protocol.

    func stop() {
        dispatchPrecondition(condition: .onQueue(queue))
        self.process(event: .stop(error: nil, notify: false))
    }

    /// Errors returned by this module.
    ///
    /// - streamError: An error from the stream task; the actual error is saved as an associated value.
    /// - framingError: An error from the line unframer; the actual error is saved as an associated value.

    enum Error : Swift.Error {
        case streamTaskError(Swift.Error)
        case framingError(LineUnframer.Error)
    }

    /// The runtime state of this object.
    ///
    /// - important: This has a leading underscore so that the state event
    ///     functions don't actually access it via `state` or `self.state`.

    private var _state: State = .initialised
}

extension StreamTaskTransport {

    /// Holds the runtime state of this object.  Each state maps to a state in
    /// `TCPTransportState` but many states have an associated value that holds
    /// all the values valid during that states.
    ///
    /// - note: Stream task have no notion of a ‘did connect’ event, so there’s
    ///     no ‘starting’ state here.

    private enum State {
        case initialised
        case started(Started)
        case stopped(Error?)

        /// Returns the transport state associated with our state.

        var transportState: TCPTransportState {
            switch self {
            case .initialised: return .initialised
            case .started: return .started
            case .stopped(let error): return .stopped(error)
            }
        }
    }

    /// Holds the values meaningful in the `.started` state.

    private struct Started {

        /// The stream task itself.

        var streamTask: URLSessionStreamTask

        /// Frames lines to send as data.

        var framer: LineFramer

        /// Unframes received data to parse out the lines.

        var unframer: LineUnframer
    }

    /// Events that trigger changes of state.
    ///
    /// - start: The client has called `start()`.
    /// - send: The client has called `send(message:)`.
    /// - stop: The client has called `stop()` (`notify` false) or something has
    ///     caused the stream to stop (`notify` true).  `error` will be nil if
    ///     the stop was orderly (either because the client called `stop()` or
    ///     because there was on EOF on the stream, or non-nil otherwise.
    /// - readCompleted: A read operation has completed.

    private enum Event {
        case start
        case send(message: String)
        case readCompleted(data: Data, isEOF: Bool)
        case stop(error: Error?, notify: Bool)
    }

    /// Processes an event in the state machine.  All the heavy lifting here is
    /// done in state event functions, which take the state as a parameter and
    /// return a new state as the function result.

    private func process(event: Event) {
        dispatchPrecondition(condition: .onQueue(queue))

        switch (self._state, event) {
        case (.initialised, .start):
            self._state = self.handleStart()
        case (_, .start):
            fatalError()
        case (.started(let started), .send(let message)):
            self._state = self.handleSend(message: message, started: started)
        case (_, .send):
            fatalError()
        case (.started(let started), .readCompleted(let data, let isEOF)):
            self._state = self.handleReadCompleted(data: data, isEOF: isEOF, started: started)
        case (_, .readCompleted):
            fatalError()
        case (let _state, .stop(let error, let notify)):
            self._state = self.handleStop(error: error, notify: notify, state: _state)
        }
    }

    /// Runs the supplied closure after the current state machine event has
    /// completed.  This is primarily used to post delegate events from a
    /// a state event function.
    ///
    /// - warning: It is critical that the closure check the current state
    ///     before acting.  It’s quite possible for some intervening event to
    ///     change the state to invalidate the resaon why the closure was
    ///     scheduled in the first place.
    ///
    /// This function is safe to call from any context and can, in fact, be
    /// called on a secondary thread (the thread running the `URLSession`’s
    /// delegate queue) courtesy of the stream task completion closures.
    ///
    /// - Parameter body: The closure to call.  This is passed the current state
    ///     as a parameter but, unlike a state event function, is not able to
    ///     return a new state directly (although it can call `process(event:)`
    ///     if necessary).

    private func deferred(_ body: @escaping (State) -> Void) {
        self.queue.async {
            dispatchPrecondition(condition: .onQueue(self.queue))
            body(self._state)
        }
    }

    /// The state event function for the `.start` event.  Transitions the object
    /// from the `.initialised` state to the `.started` state.
    ///
    /// There’s a couple of things to note here:
    ///
    /// * Stream task have no notion of a ‘did connect’ event, so we transition
    ///     straight from `.initialised` to `.started` no ‘starting’ state here.
    ///
    /// * We can’t call the delegate directly here because we _return_ the new
    ///     state, so the new state isn’t applied until we return.  If we called
    ///     the delegate directly, it would see us in the wrong state.
    ///
    ///     Instead we defer the delegate callback via a deferred closure.  That
    ///     must check the state to make sure we haven’t failed in the interim.
    ///
    /// - Returns: The new state.

    private func handleStart() -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        let streamTask = self.streamTaskMaker()
        if self.useTLS {
            streamTask.startSecureConnection()
        }
        streamTask.resume()
        self.deferred { state in
            guard case .started = state else { return }
            self.delegate?.didStart(transport: self)
        }
        return self.setupRead(started: Started(
            streamTask: streamTask,
            framer: LineFramer(),
            unframer: LineUnframer(maxLineLength: 1024)
        ))
    }

    /// The state event function for the `.send` event.  Called when the object
    /// is in the `.started` state and typically leaves the object in the same
    /// state (although with various associated values changed).
    ///
    /// - Parameters:
    ///   - message: The message to be sent.
    ///   - started: The value associated with the `.started` state.
    /// - Returns: The new state.

    private func handleSend(message: String, started: Started) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        let started = started
        let messageData = started.framer.data(for: [message])
        started.streamTask.write(messageData, timeout: 60.0) { (error) in
            if let error = error {
                self.deferred { _ in
                    self.process(event: .stop(error: .streamTaskError(error), notify: true))
                }
            }
        }
        return .started(started)
    }

    /// The state event function for the `.stop` event.  Can be called in any
    /// state and transitions the object to the `.stopped` state.
    ///
    /// - Parameters:
    ///   - error: If not nil, this holds the error that caused the
    ///     transition; if nil, the transition was not due to an error (it was
    ///     either triggered by the client calling `stop()` or by EOF on the
    ///     network).
    ///   - notify: If true, the client is notified of the stop via the
    ///     `didStop(transport:)` delegate callback.
    ///   - state: The current state.
    /// - Returns: The new state.

    private func handleStop(error: Error?, notify: Bool, state: State) -> State {
        dispatchPrecondition(condition: .onQueue(queue))

        // If we’re already stopped, do nothing.

        if case .stopped = state { return state }

        // Clean up based on the current state.

        switch state {
        case .initialised:
            break
        case .started(let started):
            started.streamTask.closeRead()
            started.streamTask.closeWrite()
        case .stopped:
            fatalError()
        }

        // Set up a delegate callback, if required.

        if notify {
            self.deferred { _ in
                // We don't need to check the state here because the check above
                // means that only one person can ever schedule this delegate
                // callback.  Moreover, if it was scheduled it needs to be
                // called.
                self.delegate?.didStop(transport: self)
            }
        }
        return .stopped(error)
    }

    /// The state event function for the `.readCompleted` event.  Called when
    /// the object is in the `.started` state and typically leaves the object in
    /// the same state (although with various associated values changed).
    ///
    /// This code is a little tricky because:
    ///
    /// * The unframer can error, which will stop the stream.
    ///
    /// * The unframer can generate multiple messages, which each have to
    ///   delivered to the delegate via a deferred closure.
    ///
    /// * The stream task could be at EOF, which generates a `.stop` event.
    ///   This can’t be issued directly because there could be messages in front
    ///   of it. Rather, the stop event has to be deferred until after the
    ///   message delivery is done.
    ///
    /// - Parameters:
    ///   - data: The data that was read; may be empty.
    ///   - isEOF: True if this is the last data that can be read.
    ///   - started: The value associated with the `.started` state.
    /// - Returns: The new state.

    private func handleReadCompleted(data: Data, isEOF: Bool, started: Started) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        var started = started

        // If we received data, run it through the unframer.

        let messages: [String]
        do {
            messages = try started.unframer.lines(for: data)
        } catch let error as LineUnframer.Error {
            return self.handleStop(error: Error.framingError(error), notify: true, state: .started(started))
        } catch {
            fatalError()
        }

        // Schedule the delivery of the messages to the delegate.  When each of
        // deferred closures run they have to check the state of the object to
        // ensure it hasn't stopped in the meantime.

        for message in messages {
            self.deferred { state in
                guard case .started = state else { return }
                self.delegate?.didReceive(message: message, transport: self)
            }
        }

        // If we’re at EOF, schedule a `.stop` event to shut things down.   If
        // not, we set up the next read.  Both of these have to return an
        // appropriate new state.

        if isEOF {
            self.deferred { state in
                guard case .started = state else { return }
                self.process(event: .stop(error: nil, notify: true))
            }
            return .started(started)
        } else {
            return self.setupRead(started: started)
        }
    }

    /// Starts a read request on the stream task.  Called when the object is in
    /// the `.started` state and leaves the object in the same state.
    ///
    /// - Parameters:
    ///   - started: The value associated with the `.started` state.
    /// - Returns: The new state.

    private func setupRead(started: Started) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        started.streamTask.readData(ofMinLength: 1, maxLength: 2048, timeout: 60) { (data, isEOF, error) in
            self.deferred { state in
                guard case .started = state else { return }
                if let error = error {
                    self.process(event: .stop(error: .streamTaskError(error), notify: true))
                } else {
                    self.process(event: .readCompleted(data: data ?? Data(), isEOF: isEOF))
                }
            }
        }
        return .started(started)
    }
}
```

[Next](TCPTransports-TCPTransport.swift.md)[Previous](TCPTransports-LineFraming.swift.md)

