---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/TCPTransports_BSDSocketsTransport_swift.html
archived_at: '2026-07-18T03:26:00.409404Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](TCPTransports-NWTCPTransport.swift.md)[Previous](TCPTransports-SocketStreamTransport.swift.md)

# TCPTransports/BSDSocketsTransport.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Implements `TCPTransport` using BSD Sockets.
 */

import Foundation

/// An implementation of the `TCPTransport` protocol that uses BSD Sockets and
/// GCD to run the TCP connection. This type supports neither connect-by-name
/// nor TLS. Supporting these would be quite hard:
///
/// * On the connect-by-name front, see the discussion in
///   `init(name:address:useTLS:)` for details.
///
/// * Supporting TLS would require deep integration with Secure Transport, which
///   isn’t something I’ve even contemplate.
///
/// If you need either of these features, you’d be better off using
/// `SocketStreamTransport` or `StreamTaskTransport`.
///
/// For more information on how to to use this type, see the `TCPTransport`
/// protocol.

class BSDSocketsTransport : NSObject, TCPTransport {

    /// Creates an object that communicates over a BSD Socket connected to the
    /// supplied address.
    ///
    /// - important: BSD Sockets is not a good API for general-purpose networking
    ///   on Apple platforms because it doesn’t support connect-by-name
    ///   semantics.  Instead, you are required to resolve the DNS name into a
    ///   set of IP addresses (which can be a mixture of IPv4 and IPv6) and
    ///   connect to one of those addresses.  Doing this well is _very_ hard,
    ///   which is why we recommend that you prefer connect-by-name APIs, like
    ///   `URLSessionStreamTask` or CFSocketStream.
    ///
    ///   If you _do_ use this code directly you will have to wrap it in a
    ///   higher-level abstraction that implements [Happy
    ///   Eyeballs][HappyEyeballs].  Roughly, this involves:
    ///
    ///   1. Resolving your DNS name into a set of IP addresses
    ///
    ///   2. Connecting to each IP address in parallel
    ///
    ///   3. Using the first connection that works, and discarding the others
    ///
    ///   Alternatively, use a connect-by-name API and you get all (and more)
    ///   for free.
    ///
    /// - warning: If you use a synchronous DNS API, like `getaddrinfo`, you
    ///   must not call it on the main thread.
    ///
    /// [HappyEyeballs]: <https://en.wikipedia.org/wiki/Happy_Eyeballs>
    ///
    /// - Parameters:
    ///   - name: A name for the stream; not used internally, but handy while
    ///     debuging.
    ///   - address: The address to connect to, as a `sockaddr` wrapped in a `Data`.
    ///   - useTLS: You must supply false here; this type does not support TLS.
    ///   - queue: The queue on which to operate; delegate callbacks are called
    ///     on this queue.
    /// - Throws: If the supplied parameters are unsupported.

    required init(name: String, address: Data, useTLS: Bool, queue: DispatchQueue) throws {
        dispatchPrecondition(condition: .onQueue(queue))
        precondition(address.count >= MemoryLayout<sockaddr>.size)
        guard !useTLS else {
            throw BSDSocketsTransport.Error.tlsNotSupported
        }
        self.name = name
        self.address = address
        self.queue = queue
    }

    /// Creates an object that communicates over a BSD Socket connected to the
    /// supplied address (supplied in string for) and port.
    ///
    /// - warning: `numericAddress` is an IP address (either IPv4 or IPv6) not a
    ///   DNS name.  For a discussion as to why, see the documentation for
    ///   `init(name:address:useTLS:)`.
    ///
    /// - Parameters:
    ///   - numericAddress: An IP address in string form.
    ///   - port: The port number to connect to.
    ///   - useTLS: You must supply false here; this type does not support TLS.
    ///   - queue: The queue on which to operate; delegate callbacks are called
    ///     on this queue.
    /// - Throws: If the supplied parameters are unsupported.

    convenience init(numericAddress: String, port: Int, useTLS: Bool, queue: DispatchQueue) throws {
        dispatchPrecondition(condition: .onQueue(queue))
        // Convert the string to an address.  As we could be running on the main
        // thread and it’s not safe to call the DNS on the main thread, we
        // supply `AI_NUMERICHOST` and `AI_NUMERICSERV` to ensure this never
        // blocks waiting for the network.
        var hints = addrinfo()
        hints.ai_flags = AI_NUMERICHOST | AI_NUMERICSERV
        var addrList: UnsafeMutablePointer<addrinfo>? = nil
        let getaddrinfoResult = getaddrinfo(numericAddress, String(port), &hints, &addrList)
        guard getaddrinfoResult == 0 else {
            // We don’t include `getaddrinfoResult` in the error because with
            // `AI_NUMERICHOST` and `AI_NUMERICSERV set the only possible error
            // is that we need to talk to the DNS to resolve a name.
            throw BSDSocketsTransport.Error.numericAddressRequired
        }
        defer { freeaddrinfo(addrList) }
        let addr = Data(bytes: addrList!.pointee.ai_addr, count: Int(addrList!.pointee.ai_addrlen))
        try self.init(name: numericAddress, address: addr, useTLS: useTLS, queue: queue)
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

    let address: Data

    /// The value passed to the initialiser.

    let queue: DispatchQueue

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
    /// - tlsNotSupported: An error indicating an implementation limitation.
    /// - getaddrinfoError: An error from `getaddrinfo`; the actual error is saved as an associated value.
    /// - streamError: An error from the socket stream; the actual error is saved as an associated value.
    /// - framingError: An error from the line unframer; the actual error is saved as an associated value.

    enum Error : Swift.Error {
        case tlsNotSupported
        case numericAddressRequired
        case socketError(Int32)
        case framingError(LineUnframer.Error)
    }

    /// The runtime state of this object.
    ///
    /// - important: This has a leading underscore so that the state event
    ///     functions don't actually access it via `state` or `self.state`.

    private var _state: State = .initialised
}

extension BSDSocketsTransport {

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

    /// Holds the values meaningful in the `.starting` state.

    private struct Starting {

        /// The socket that’s currently doing an async `connect`.

        var socket: Int32

        /// A write source used to monitor the async connect.

        var writeSource: DispatchSourceWrite
    }

    /// Holds the values meaningful in the `.started` state.

    private struct Started {

        /// The socket.

        var socket: Int32

        /// A read source used to monitor for bytes available to be read.

        var readSource: DispatchSourceRead

        // A write source used to monitor for space available to write to.

        var writeSource: DispatchSourceWrite

        /// Set if there’s space available to write to.  This can be set for a
        /// long time if there’s no data waiting in the output buffer.  If this
        /// is set then the write source is suspended, to prevent it from firing
        /// continually.

        var hasSpaceAvailable: Bool

        /// Frames lines to send as data.

        var framer: LineFramer

        /// Unframes received data to parse out the lines.

        var unframer: LineUnframer

        /// Holds data that’s queued for output.

        var outputBuffer: Data

        /// Creates a value from the starting state.
        ///
        /// Note that the caller only has to supply a read source because it
        /// moves the write source over from the starting state.

        init(starting: Starting, readSource: DispatchSourceRead) {
            self.socket = starting.socket
            self.readSource = readSource
            self.writeSource = starting.writeSource
            self.framer = LineFramer()
            self.unframer = LineUnframer(maxLineLength: 1024)
            self.outputBuffer = Data()
            self.hasSpaceAvailable = false
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
    /// - isReadable: The read source has fired.
    /// - isWritable: The write source has fired.  Note that in the `.starting`
    ///     state the write source is used to monitor the async connect, so this
    ///     event is expected in that state as well as the more standard
    ///     `.started` state.

    private enum Event {
        case start
        case send(message: String)
        case stop(error: Error?, notify: Bool)
        case isReadable
        case isWritable
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
        case (let _state, .stop(let error, let notify)):
            self._state = self.handleStop(error: error, notify: notify, state: _state)
        case (.started(let started), .isReadable):
            self._state = self.handleIsReadable(started: started)
        case (_, .isReadable):
            fatalError()
        case (.starting(let starting), .isWritable):
            self._state = self.handleOpenCompleted(starting: starting)
        case (.started(let started), .isWritable):
            self._state = self.handleIsWritable(started: started)
        case (_, .isWritable):
            fatalError()
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
    /// - Parameter body: The closure to call.  This is passed the current state
    ///     as a parameter but, unlike a state event function, is not able to
    ///     return a new state directly (although it can call `process(event:)`
    ///     if necessary).

    private func deferred(_ body: @escaping (State) -> Void) {
        dispatchPrecondition(condition: .onQueue(queue))
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

        // Create our socket.  If that fails, we go straight to the `.stopped` state.

        let fd: Int32
        do {
            fd = try BSDSocketsTransport.openSocket(connectedTo: self.address, shouldBlock: false)
        } catch let error as BSDSocketsTransport.Error {
            return self.handleStop(error: error, notify: true, state: .initialised)
        } catch {
            fatalError()
        }

        // Start a dispatch source to monitor the async connection.  This write
        // source ‘owns’ the socket and will close it when the source is
        // cancelled.

        let writeSource = DispatchSource.makeWriteSource(fileDescriptor: fd, queue: self.queue)
        writeSource.setEventHandler {
            dispatchPrecondition(condition: .onQueue(self.queue))
            self.process(event: .isWritable)
        }
        writeSource.setCancelHandler {
            let junk = close(fd)
            assert(junk == 0)
        }
        writeSource.resume()

        return .starting(Starting(socket: fd, writeSource: writeSource))
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
        var started = started
        let messageData = started.framer.data(for: [message])
        started.outputBuffer.append(messageData)
        return self.serviceOutput(started: started)
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

        // Clean up based on the current state.  Note that we don’t have to
        // close the socket here because it’s actually ‘owned‘ by the write
        // source, and thus is closed in the read source cancellation handler.
        // Also, if `hasSpaceAvailable` is set the write source is suspended so
        // we resume it before cancelling it.

        switch state {
        case .initialised:
            break
        case .starting(let starting):
            starting.writeSource.cancel()
        case .started(let started):
            started.readSource.cancel()
            if started.hasSpaceAvailable {
                started.writeSource.resume()
            }
            started.writeSource.cancel()
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

    /// The state event function for the `.openCompleted` event.  Called in the
    /// `.starting` state and transitions to the `.started` state if the
    /// connection was successful or the `.stopped` state othewise.
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

        // Use the traditional BSD Sockets approach to get the error from the
        // async connect.

        var connectError: Int32 = 0
        var connectErrorLen: socklen_t = socklen_t(MemoryLayout.size(ofValue: connectError))
        let getSockOptResult = getsockopt(starting.socket, SOL_SOCKET, SO_ERROR, &connectError, &connectErrorLen)
        if getSockOptResult < 0 {
            connectError = errno
        }
        guard connectError == 0 else {
            return self.handleStop(error: .socketError(connectError), notify: true, state: .starting(starting))
        }

        // The connect was successful, so let’s create the read source.

        let readSource = DispatchSource.makeReadSource(fileDescriptor: starting.socket, queue: self.queue)
        readSource.setEventHandler {
            dispatchPrecondition(condition: .onQueue(self.queue))
            self.process(event: .isReadable)
        }
        // The read source doesn’t need a cancel handler because the write
        // source takes care of cancellation.
        readSource.resume()

        // Finally, tell our delegate via a deferred callback.

        self.deferred { state in
            guard case .started = state else { return }
            self.delegate?.didStart(transport: self)
        }
        return .started(Started(starting: starting, readSource: readSource))
    }

    /// The state event function for the `.isReadable` event.  Called
    /// when the object is in the `.started` state and typically leaves the
    /// object in the same state (although with various associated values
    /// changed).
    ///
    /// This code is a little tricky because:
    ///
    /// * The read could fail with an error, which requires us to stop with that
    ///   error.
    ///
    /// * The read could indicate EOF, which also requires us to stop, this
    ///   time without an error.
    ///
    /// * The unframer can error, which requires us to stop with that error.
    ///
    /// * The unframer can generate multiple messages, which each have to
    ///   delivered to the delegate via a deferred closure.
    ///
    /// - Parameter started: The value associated with the `.started` state.
    /// - Returns: The new state.

    private func handleIsReadable(started: Started) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        var started = started

        // Do our read.

        let inputBufferCount = 2048
        var inputBuffer = Data(count: inputBufferCount)
        let (readError, bytesRead) = inputBuffer.withUnsafeMutableBytes { (bytes: UnsafeMutablePointer<UInt8>) -> (Int32, Int) in
            let readResult = read(started.socket, bytes, inputBufferCount)
            if readResult >= 0 {
                return (0, readResult)
            } else {
                return (errno, 0)
            }
        }

        // Handle the error and EOF cases.

        guard readError == 0 else {
            return self.handleStop(error: .socketError(readError), notify: true, state: .started(started))
        }
        guard bytesRead != 0 else {
            return self.handleStop(error: nil, notify: true, state: .started(started))
        }

        // If we received data, run it through the unframer.

        let messages: [String]
        inputBuffer.removeLast(inputBufferCount - bytesRead)
        do {
            messages = try started.unframer.lines(for: inputBuffer)
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
        return .started(started)
    }

    /// The state event function for the `.isWritable` event.  Called
    /// when the object is in the `.started` state and typically leaves the
    /// object in the same state (although with various associated values
    /// changed).  The heavy lifting is done in `serviceOutput(started:)`, which
    /// is responsible for writing buffer data to the output stream.
    ///
    /// - Parameter started: The value associated with the `.started` state.
    /// - Returns: The new state.

    private func handleIsWritable(started: Started) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        var started = started
        started.hasSpaceAvailable = true
        started.writeSource.suspend()
        return self.serviceOutput(started: started)
    }

    /// Services the output side of the connection, writing data to the socket
    /// if there’s data to write and space available.  Called when the object is
    /// in the `.started` state and typically leaves the object in the same
    /// state (although with various associated values changed).
    ///
    /// - Parameter started: The value associated with the `.started` state.
    /// - Returns: The new state.

    private func serviceOutput(started: Started) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        var started = started
        if started.hasSpaceAvailable && !started.outputBuffer.isEmpty {

            // It’s possible (although vanishingly unlikely in this particular
            // app) that our write could fill the socket’s send buffer, in which
            // case we will need to get another `.isWritable` event before it’s
            // safe to write.  To enable this we resume our dispatch source so
            // we get called back when there and, becasue these must be in sync,
            // clear the `hasSpaceAvailable` flag.

            started.hasSpaceAvailable = false
            started.writeSource.resume()

            // Write the actual data.

            let outputBufferCount = started.outputBuffer.count
            let (writeError, bytesWritten) = started.outputBuffer.withUnsafeBytes { (bytes: UnsafePointer<UInt8>) -> (Int32, Int) in
                let writeResult = write(started.socket, bytes, outputBufferCount)
                if writeResult >= 0 {
                    return (0, writeResult)
                } else {
                    return (errno, 0)
                }
            }

            // Handle the error and no progress cases.

            guard writeError == 0 else {
                return self.handleStop(error: .socketError(writeError), notify: true, state: .started(started))
            }
            guard bytesWritten != 0 else {
                return self.handleStop(error: nil, notify: true, state: .started(started))
            }

            // Calling `remove(first:)` corrupts the `Data`
            // <rdar://problem/34206043>. Even replacing it with a subrange
            // doesn’t work, so I built a new data from a sequence of bytes.

            // started.outputBuffer.removeFirst(bytesWritten)
            let remainderIndex = started.outputBuffer.startIndex + bytesWritten
            // started.outputBuffer = started.outputBuffer[remainderIndex...]
            started.outputBuffer = Data([UInt8](started.outputBuffer[remainderIndex...]))
        }
        return .started(started)
    }
}

extension BSDSocketsTransport {

    /// This helper function does the standard BSD Sockets open and connect
    /// dance, handling all the wacky errors and edge cases.
    ///
    /// - Parameters:
    ///   - address: The address to connect to,
    ///   - shouldBlock: True if the connection should be blocking.
    /// - Returns: A socket that either connect (blocking) or connecting (non-blocking).
    /// - Throws: An BSD Sockets error if anything goes wrong.

    private static func openSocket(connectedTo address: Data, shouldBlock: Bool) throws -> Int32 {

        // Open a stream socket for the appropriate family.

        let family = address.withUnsafeBytes { (sa: UnsafePointer<sockaddr>) in
            sa.pointee.sa_family
        }
        var shouldClose = true
        let fd = socket(Int32(family), SOCK_STREAM, 0)
        guard fd >= 0 else {
            throw BSDSocketsTransport.Error.socketError(errno)
        }
        defer {
            if shouldClose {
                let junk = close(fd)
                assert(junk == 0)
            }
        }

        // Set it to non-blocking if requested.

        if !shouldBlock {
            let fcntlResult = fcntl(fd, F_SETFL, O_NONBLOCK)
            guard fcntlResult >= 0 else {
                throw BSDSocketsTransport.Error.socketError(errno)
            }
        }

        // Start the connection.  Ain’t BSD Sockets grand!

        let saLen = socklen_t(address.count)
        let connectError = address.withUnsafeBytes { (sa: UnsafePointer<sockaddr>) -> Int32 in
            let isNegative = connect(fd, sa, saLen) < 0
            switch (shouldBlock, isNegative, errno) {
            case (true,  false, _):           return 0
            case (false, true,  EINPROGRESS): return 0
            case (false, false, _):           return ENOTTY     // shouldn’t be possible
            case (_,     _,     let error):   return error
            }
        }
        guard connectError == 0 else {
            throw BSDSocketsTransport.Error.socketError(connectError)
        }

        // In the successful case mark the socket as not to be closed by the
        // `defer` statement above and then return it.

        shouldClose = false
        return fd
    }
}
```

[Next](TCPTransports-NWTCPTransport.swift.md)[Previous](TCPTransports-SocketStreamTransport.swift.md)

