---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/TCPTransports_NWTCPTransport_swift.html
archived_at: '2026-07-18T03:26:00.690470Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](TCPTransports-LineFraming.swift.md)[Previous](TCPTransports-BSDSocketsTransport.swift.md)

# TCPTransports/NWTCPTransport.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Implements `TCPTransport` on a `NWTCPConnection`.
 */

import NetworkExtension

/// An implementation of the `TCPTransport` protocol that uses an `NWTCPConnection`
/// to run the TCP connection. This type supports both connect-by-name and TLS.
///
/// - important: This class will only work in the context of a Network Extension
///   provider because the only way to create an `NWTCPConnection` is via the
///   `NEProvider.createTCPConnection(to:enableTLS:tlsParameters:delegate:)`
///   method.  That means you can’t use it ‘out of the box’ here.  I’ve included
///   it here to act as a starting point if you happen to be working in that
///   context.
///
/// For more information on how to to use this type, see the `TCPTransport`
/// protocol.

class NWTCPTransport : TCPTransport {

    /// Creates an object that will communicate over an `NWTCPConnection`
    /// created by calling the connection maker closure.
    ///
    /// The `connectionMaker` closure means that the client is in charge of
    /// connection creation, which is useful because of the very limited
    /// circumstances under which `NWTCPConnection` is available.  See the
    /// documentation for the `NWTCPTransport` class for more information about
    /// this.
    ///
    ///
    /// - Parameters:
    ///   - name: A name for the connection; not used internally, but handy while
    ///     debuging.
    ///   - queue: The queue on which to operate; delegate callbacks are called
    ///     on this queue.
    ///   - connectionMaker: A closure called to create the `NWTCPConnection`
    ///     for this object.  The resulting `NWTCPConnection` is ‘owned‘ by this
    ///     object. You can’t go modifying it after the fact.

    required init(name: String, queue: DispatchQueue, connectionMaker: @escaping () -> NWTCPConnection) {
        dispatchPrecondition(condition: .onQueue(queue))
        self.name = name
        self.queue = queue
        self.connectionMaker = connectionMaker
    }

    /// Creates an object that will communicate with the specified host and
    /// port, optionally using TLS.
    ///
    /// - important: In the context of this sample this method will always throw
    ///   `nwTCPConnectionNotSupported`.  See the documentation for the
    ///   `NWTCPTransport` class for more information about this.
    ///
    /// - Parameters:
    ///   - hostName: The host name to connect to (can be an IP address, both IPv4 and IPv6).
    ///   - port: The port on which to connect.
    ///   - useTLS: Whether to enable TLS or not.
    ///   - queue: The queue on which to operate; delegate callbacks are called
    ///     on this queue.
    /// - Throws: Always, as discussed above.

    convenience init(hostName: String, port: Int, useTLS: Bool, queue: DispatchQueue) throws {
        guard NWTCPTransport.isNWTCPConnectionAvailable else {
            throw NWTCPTransport.Error.nwTCPConnectionNotSupported
        }
        self.init(name: hostName, queue: queue, connectionMaker: {
            let endpoint = NWHostEndpoint(hostname: hostName, port: String(port))
            return NWTCPTransport.makeNWTCPConnection(endpoint: endpoint, enableTLS: useTLS)
        })
    }

    deinit {
        // If this assert fires you’ve released the last reference to this
        // transport without stopping it.
        switch self._state {
        case .initialised: break
        case .starting:    fatalError()
        case .started:     fatalError()
        case .stopped:     break
        }
    }

    /// The value passed to the initialiser.

    let name: String

    /// The value passed to the initialiser.

    let queue: DispatchQueue

    /// The value passed to the initialiser.

    let connectionMaker: () -> NWTCPConnection

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
    /// - nwTCPConnectionNotSupported: Indicates that `NWTCPConnection` is not supported in this context.
    /// - connectionError: An error from the `NWTCPConnection`; the actual error is saved as an associated value.
    /// - framingError: An error from the line unframer; the actual error is saved as an associated value.

    enum Error : Swift.Error {
        case nwTCPConnectionNotSupported
        case connectionError(Swift.Error)
        case framingError(LineUnframer.Error)
    }

    /// The runtime state of this object.
    ///
    /// - important: This has a leading underscore so that the state event
    ///     functions don't actually access it via `state` or `self.state`.

    private var _state: State = .initialised
}

extension NWTCPTransport {

    /// Holds the runtime state of this object.  Each state maps to a state in
    /// `TCPTransportState` but many states have an associated value that holds
    /// all the values valid during that states.

    private enum State {
        case initialised
        case starting(Starting)
        case started(Started)
        case stopped(Error?)

        /// Returns the transport state associated with our state.

        var transportState: TCPTransportState {
            switch self {
            case .initialised: return .initialised
            case .starting: return .starting
            case .started: return .started
            case .stopped(let error): return .stopped(error)
            }
        }
    }

    private struct Starting {

        /// The `NWTCPConnection` itself.

        var connection: NWTCPConnection

        /// A reference to our observation of the `state` property of
        /// `connection`.

        var stateObservation: NSKeyValueObservation
    }

    /// Holds the values meaningful in the `.started` state.

    private struct Started {

        /// The `NWTCPConnection` itself.

        var connection: NWTCPConnection

        /// A reference to our observation of the `state` property of
        /// `connection`.

        var stateObservation: NSKeyValueObservation

        /// Frames lines to send as data.

        var framer: LineFramer

        /// Unframes received data to parse out the lines.

        var unframer: LineUnframer

        /// Creates a value from the starting state.

        init(starting: Starting) {
            self.connection = starting.connection
            self.stateObservation = starting.stateObservation
            self.framer = LineFramer()
            self.unframer = LineUnframer(maxLineLength: 1024)
        }
    }

    /// Events that trigger changes of state.
    ///
    /// - start: The client has called `start()`.
    /// - send: The client has called `send(message:)`.
    /// - stop: The client has called `stop()` (`notify` false) or something has
    ///     caused the stream to stop (`notify` true).  `error` will be nil if
    ///     the stop was orderly (either because the client called `stop()` or
    ///     because there was on EOF on the stream, or non-nil otherwise.
    /// - openCompleted: An open operation has completed.
    /// - readCompleted: A read operation has completed.

    private enum Event {
        case start
        case send(message: String)
        case stop(error: Error?, notify: Bool)
        case openCompleted
        case readCompleted(data: Data, error: Error?)
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
        case (.starting(let starting), .openCompleted):
            self._state = self.handleOpenCompleted(starting: starting)
        case (_, .openCompleted):
            fatalError()
        case (.started(let started), .readCompleted(let data, let error)):
            self._state = self.handleReadCompleted(data: data, error: error, started: started)
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
    /// This function is safe to call from any thread, and expected that it will
    /// be called on secondary threads courtesy of `NWTCPConnection` callbacks.
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
    /// from the `.initialised` state to the `.starting` state.
    ///
    /// - Returns: The new state.

    private func handleStart() -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        let connection = self.connectionMaker()
        let stateObservation = connection.observe(\NWTCPConnection.state, changeHandler: self.connectionStateDidChange)
        return .starting(Starting(connection: connection, stateObservation: stateObservation))
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
        started.connection.write(messageData) { (error) in
            if let error = error {
                self.deferred { _ in
                    self.process(event: .stop(error: .connectionError(error), notify: true))
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
        case .starting(let starting):
            starting.connection.cancel()
            starting.stateObservation.invalidate()
        case .started(let started):
            started.connection.cancel()
            started.stateObservation.invalidate()
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

    /// The state event function for the `.openCompleted` event.  Transitions the object
    /// from the `.staring` state to the `.started` state.
    ///
    /// Note that we can’t call the delegate directly here because we _return_
    /// the new state, so the new state isn’t applied until we return.  If we
    /// called the delegate directly, it would see us in the wrong state.
    ///
    /// Instead we defer the delegate callback via a deferred closure.  That
    /// must check the state to make sure we haven’t failed in the interim.
    ///
    /// - Parameter starting: The value associated with the `.starting` state.
    /// - Returns: The new state.

    private func handleOpenCompleted(starting: Starting) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        self.deferred { state in
            guard case .started = state else { return }
            self.delegate?.didStart(transport: self)
        }
        return self.setupRead(started: Started(starting: starting))
    }

    /// The state event function for the `.readCompleted` event.  Called when
    /// the object is in the `.started` state and typically leaves the object in
    /// the same state (although with various associated values changed).
    ///
    /// This code is a little tricky because:
    ///
    /// * The unframer can error, which will stop the connection.
    ///
    /// * The unframer can generate multiple messages, which each have to
    ///   delivered to the delegate via a deferred closure.
    ///
    /// - Parameters:
    ///   - data: The data that was read.
    ///   - started: The value associated with the `.started` state.
    /// - Returns: The new state.

    private func handleReadCompleted(data: Data, error: Error?, started: Started) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        var started = started

        // Run the data through the unframer.

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

        // Set up the next read or, if we got an error (which might indicate an
        // EOF), schedule a `.stop` event to shut things down.  Both of these
        // have to return an appropriate new state.

        if let error = error {
            self.deferred { state in
                guard case .started = state else { return }
                self.process(event: .stop(error: error.isEOF ? nil : error, notify: true))
            }
            return .started(started)
        } else {
            return self.setupRead(started: started)
        }
    }

    /// Starts a read request on the stream task.  Called when the object is in
    /// the `.started` state and leaves the object in the same state.
    ///
    /// - Parameter started: The value associated with the `.started` state.
    /// - Returns: The new state.

    private func setupRead(started: Started) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        started.connection.readMinimumLength(1, maximumLength: 2048) { (data, error) in
            // The documentation for NWTCPConnection is very vague about the
            // semantics of the callback parameters but here’s how it breaks
            // down:
            //
            // * It’s possible for both `data` and `error` to be non-nil, indicating
            //   we read some data and then got an error.
            //
            // * EOF is signalled by `ENOTCONN` (which is less than ideal both that's another
            //   story).
            //
            // This design means that we have to pass the error along with the
            // `.readCompleted` event and then `handleReadCompleted(…)` has to
            // look at the error after processing the data.
            assert( (error != nil) || (data != nil) )
            self.deferred { state in
                guard case .started = state else { return }
                self.process(event: .readCompleted(data: data ?? Data(), error: error.flatMap { Error.connectionError($0) } ))
            }
        }
        return .started(started)
    }

    /// This is a KVO observation callback for the `state` property on the
    /// `NWTCPConnection`. It’s only goal is to trigger the transition from our
    /// `.starting` state to the `.started` state by watching for the
    /// connection’s state going to `.connected`.  The disconnect transition is
    /// not handled this way because we always have a permanent outstanding read
    /// request, and that read request will fail with an error if we disconnect.

    private func connectionStateDidChange(_: NWTCPConnection, _: NSKeyValueObservedChange<NWTCPConnectionState>) {
        self.deferred { (state) in
            guard case .starting(let starting) = state else { return }
            if starting.connection.state == .connected {
                self.process(event: .openCompleted)
            }
        }
    }
}

extension NWTCPTransport.Error {

    /// Returns true if the error should be treated as an EOF.  As things
    /// currently stand, `NWTCPConnection` signals EOF via the `ENOTCONN` error
    /// code.

    fileprivate var isEOF: Bool {
        if case .connectionError(let errorObj as NSError) = self, errorObj.domain == NSPOSIXErrorDomain, errorObj.code == ENOTCONN {
            return true
        } else {
            return false
        }
    }
}

extension NWTCPTransport {

    /// This value is always false, indicating that `NWTCPConnection` is not available in this
    /// context.  See the documentation for the `NWTCPTransport` class for more
    /// information about this.

    static let isNWTCPConnectionAvailable = false

    /// This method is a placeholder that you can replace with real code if you
    /// want to use `NWTCPTransport` in an environment where `NWTCPConnection`
    /// is supported. See the documentation for the `NWTCPTransport` class for
    /// more information about this.
    ///
    /// - Parameters:
    ///   - endpoint: The endpoint to connect to.
    ///   - enableTLS: Whether to enable TLS or not.
    /// - Returns: An connection object.

    static func makeNWTCPConnection(endpoint: NWHostEndpoint, enableTLS: Bool) -> NWTCPConnection {
        fatalError()
    }
}
```

[Next](TCPTransports-LineFraming.swift.md)[Previous](TCPTransports-BSDSocketsTransport.swift.md)

