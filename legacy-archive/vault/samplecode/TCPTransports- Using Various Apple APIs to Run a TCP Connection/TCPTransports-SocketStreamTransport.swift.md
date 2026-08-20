---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/TCPTransports_SocketStreamTransport_swift.html
archived_at: '2026-07-18T03:26:00.960874Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](TCPTransports-BSDSocketsTransport.swift.md)[Previous](README.md.md)

# TCPTransports/SocketStreamTransport.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Implements `TCPTransport` on a CFSocketStream.
 */

import Foundation

/// An implementation of the `TCPTransport` protocol that uses a CFSocketStream
/// to run the TCP connection. Out of the box this type supports both
/// connect-by-name and TLS. You could also easily modify it to support
/// connecting to a Bonjour service, working over a bound pair of streams, and
/// so on.
///
/// For more information on how to to use this type, see the `TCPTransport`
/// protocol.

class SocketStreamTransport : NSObject, TCPTransport {

    /// Creates an object that will communicate over streams created by calling
    /// the stream maker closure.
    ///
    /// The `streamMaker` closure means that this object can work with any type
    /// of CFStream.  So, although the primary focus is CFSocketStream, it’s
    /// possible to use the object with, say, a bound pair of streams.  That
    /// comes in handy for testing as well.
    ///
    /// - Parameters:
    ///   - name: A name for the stream; not used internally, but handy while
    ///     debuging.
    ///   - queue: The queue on which to operate; delegate callbacks are called
    ///     on this queue.
    ///   - streamMaker: A closure called to create the streams for this
    ///     connection.  The resulting streams are ‘owned‘ by this object. You
    ///     can’t go modifying them after the fact.  The streams must not be
    ///     opened; this object takes care of opening and closing them.

    required init(name: String, queue: DispatchQueue, streamMaker: @escaping () -> (inputStream: InputStream, outputStream: OutputStream)) {
        dispatchPrecondition(condition: .onQueue(queue))
        self.name = name
        self.queue = queue
        self.streamMaker = streamMaker
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
        self.init(name: "\(hostName):\(port)", queue: queue, streamMaker: { () -> (inputStream: InputStream, outputStream: OutputStream) in
            let streams = Stream.streamsToHost(name: hostName, port: port)
            if useTLS {
                // When dealing with CFSocketStream you only need to set
                // properties on to one stream in the pair, in this case the
                // input stream.
                let success = streams.inputStream.setProperty([:] as NSDictionary, forKey: Stream.PropertyKey(kCFStreamPropertySSLSettings as String))
                assert(success)
            }
            return streams
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

    let streamMaker: () -> (inputStream: InputStream, outputStream: OutputStream)

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
    /// - streamError: An error from the socket stream; the actual error is saved as an associated value.
    /// - framingError: An error from the line unframer; the actual error is saved as an associated value.
    /// - unknownError: The socket stream failed without giving us a useful error.

    enum Error : Swift.Error {
        case streamError(Swift.Error)
        case framingError(LineUnframer.Error)
        case unknownError
    }

    /// The runtime state of this object.
    ///
    /// - important: This has a leading underscore so that the state event
    ///     functions don't actually access it via `state` or `self.state`.

    private var _state: State = .initialised
}

extension SocketStreamTransport {

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

        /// The stream pair.

        var streams: (inputStream: InputStream, outputStream: OutputStream)

        /// The remaining set of subevents that must occur before we can
        /// transition from `.starting` to `.started`.

        var remainingOpenSubevents: Set<OpenSubevent>

        /// Whether a `.hasBytesAvailable` event was delivered while the streams
        /// were opening.

        var hasBytesAvailable: Bool

        /// Whether a `.hasSpaceAvailable` event was delivered while the streams
        /// were opening.

        var hasSpaceAvailable: Bool

        /// Creates a value with the supplies input streams and defaults for
        /// everything else.

        init(streams: (inputStream: InputStream, outputStream: OutputStream)) {
            self.streams = streams
            self.remainingOpenSubevents = [.inputStream, .outputStream, .hasSpaceAvailable]
            self.hasBytesAvailable = false
            self.hasSpaceAvailable = false
        }
    }

    /// Holds the values meaningful in the `.started` state.

    private struct Started {

        /// The stream pair.

        var streams: (inputStream: InputStream, outputStream: OutputStream)

        /// True if we’ve received a `.hasBytesAvailable` event but haven’t read
        /// any bytes yet.

        var hasBytesAvailable: Bool

        /// True if we’ve received a `.hasSpaceAvailable` event but haven’t
        /// written any bytes yet.

        var hasSpaceAvailable: Bool

        /// Frames lines to send as data.

        var framer: LineFramer

        /// Unframes received data to parse out the lines.

        var unframer: LineUnframer

        /// Holds data that’s queued for output.

        var outputBuffer: Data

        /// Creates a value from the starting state.

        init(starting: Starting) {
            self.streams = starting.streams
            self.hasBytesAvailable = starting.hasBytesAvailable
            self.hasSpaceAvailable = starting.hasSpaceAvailable
            self.framer = LineFramer()
            self.unframer = LineUnframer(maxLineLength: 1024)
            self.outputBuffer = Data()
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
    /// - openCompleted: An `.openCompleted` event has come up from the stream.
    /// - hasBytesAvailable: An `.hasBytesAvailable` event has come up from the stream.
    /// - hasSpaceAvailable: An `.hasSpaceAvailable` event has come up from the stream.

    private enum Event {
        case start
        case send(message: String)
        case stop(error: Error?, notify: Bool)
        case openCompleted(stream: Stream)
        case hasBytesAvailable
        case hasSpaceAvailable
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
        case (.starting(let starting), .openCompleted(let stream)):
            let subevent: OpenSubevent = (stream == starting.streams.inputStream) ? .inputStream : .outputStream
            self._state = self.handleOpenCompleted(subevent: subevent, starting: starting)
        case (_, .openCompleted):
            fatalError()

        case (.starting(let starting), .hasSpaceAvailable):
            self._state = self.handleOpenCompleted(subevent: .hasSpaceAvailable, starting: starting)
        case (.started(let started), .hasSpaceAvailable):
            self._state = self.handleHasSpaceAvailable(started: started)
        case (_, .hasSpaceAvailable):
            fatalError()

        case (.starting(let starting), .hasBytesAvailable):
            self._state = self.handleHasBytesAvailable(starting: starting)
        case (.started(let started), .hasBytesAvailable):
            self._state = self.handleHasBytesAvailable(started: started)
        case (_, .hasBytesAvailable):
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
        let streams = self.streamMaker()
        CFReadStreamSetDispatchQueue(streams.inputStream, self.queue)
        CFWriteStreamSetDispatchQueue(streams.outputStream, self.queue)
        for stream in [streams.inputStream, streams.outputStream] {
            stream.delegate = self
            stream.open()
        }
        return .starting(Starting(streams: streams))
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

        func close(streams: (inputStream: InputStream, outputStream: OutputStream)) {
            for stream in [streams.inputStream, streams.outputStream] {
                stream.delegate = nil
                stream.close()
            }
        }

        // Clean up based on the current state.

        switch state {
        case .initialised:
            break
        case .starting(let starting):
            close(streams: starting.streams)
        case .started(let started):
            close(streams: started.streams)
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

    /// Subevents associated with the `handleOpenCompleted` stream event function.
    ///
    /// - inputStream: A `.openCompleted` event occured on the input stream.
    /// - outputStream: A `.openCompleted` event occured on the output stream.
    /// - hasSpaceAvailable: A `.hasBytesAvailable` event occured on the output
    ///     stream while we were still in the `.starting` state.

    private enum OpenSubevent {
        case inputStream
        case outputStream
        case hasSpaceAvailable
    }

    /// The state event function for the `.openCompleted` event.  Called in
    /// the `.starting` state and can either return the `.starting` state or
    /// transition us to the `.started` state.
    ///
    /// There's three interesting edge cases here.  The first is that we don’t
    /// just wait for the two `.openCompleted` events, we also wait to get a
    /// `.hasSpaceAvailable` event on the output stream.  This is necessary
    /// because, when TLS is enabled, the TLS context isn’t set up when you get
    /// the `.openCompleted` events, so you have to wait for
    /// `.hasSpaceAvailable` event if you want to do TLS server trust
    /// evaluation.
    ///
    /// The second complexity relates the delegate callback.  We can’t call the
    /// delegate directly here because we _return_ the new state, so the new
    /// state isn’t applied until we return.  If we called the delegate
    /// directly, it would see us in the wrong state.
    ///
    /// Instead we defer the delegate callback via a deferred closure.  That
    /// must check the state to make sure we haven’t failed in the interim.
    ///
    /// Finally, if a `.hasSpaceAvailable` event arrived while we were waiting
    /// for the opens to complete, we have to process that event.  We can’t do
    /// that directly in our deferred closure because the delegate callback
    /// might have change the state.  So we issue a second deferred closure,
    /// check the state, and then issue process the event.
    ///
    /// Note that the reverse is also possible (a `.hasBytesAvailable` event on
    /// the input stream while we’re still waiting for the `.openCompleted` and
    /// `.hasSpaceAvailable` events on the output stream) but we don’t need to
    /// handle it because we know there’s no output data waiting to be written
    /// because it’s not legal for the client to call `send(message:)` until
    /// we’ve called `didStart(transport:)`.
    ///
    /// - Parameters:
    ///   - subevent: The specific subevent that occured.
    ///   - starting: The value associated with the `.starting` state.
    /// - Returns: The new state.

    private func handleOpenCompleted(subevent: OpenSubevent, starting: Starting) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        var starting = starting
        starting.remainingOpenSubevents.remove(subevent)
        if subevent == .hasSpaceAvailable {
            starting.hasSpaceAvailable = true
        }
        guard starting.remainingOpenSubevents.isEmpty else {
            return .starting(starting)
        }
        let notifyHasBytesAvailable = starting.hasBytesAvailable
        self.deferred { state in
            guard case .started = state else { return }
            self.delegate?.didStart(transport: self)
            if notifyHasBytesAvailable {
                self.deferred { (state) in
                    guard case .started = state else { return }
                    self.process(event: .hasBytesAvailable)
                }
            }
        }
        return .started(Started(starting: starting))
    }

    /// The state event function for the `.hasBytesAvailable` event in the
    /// edge case where `.hasBytesAvailable` is issued while the object is still
    /// in the `.starting` state.  This just records the event and leaves us in
    /// the `.starting` state.
    ///
    /// - Parameter started: The value associated with the `.starting` state.
    /// - Returns: The new state.

    private func handleHasBytesAvailable(starting: Starting) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        var starting = starting
        starting.hasBytesAvailable = true
        return .starting(starting)
    }

    /// The state event function for the `.hasSpaceAvailable` event.  Called
    /// when the object is in the `.started` state and typically leaves the
    /// object in the same state (although with various associated values
    /// changed).  The heavy lifting is done in `serviceOutput(started:)`, which
    /// is responsible for writing buffer data to the output stream.
    ///
    /// - Parameter started: The value associated with the `.started` state.
    /// - Returns: The new state.

    private func handleHasSpaceAvailable(started: Started) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        var started = started
        started.hasSpaceAvailable = true
        return self.serviceOutput(started: started)
    }

    /// The state event function for the `.hasBytesAvailable` event.  Called
    /// when the object is in the `.started` state and typically leaves the
    /// object in the same state (although with various associated values
    /// changed).  The heavy lifting is done in `serviceInput(started:)`, which
    /// is responsible for reading data from the input stream.
    ///
    /// - Parameter started: The value associated with the `.started` state.
    /// - Returns: The new state.

    private func handleHasBytesAvailable(started: Started) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        var started = started
        started.hasBytesAvailable = true
        return self.serviceInput(started: started)
    }

    /// Services the output stream, writing data to the stream if there’s data
    /// to write and space available.  Called when the object is in the
    /// `.started` state and typically leaves the object in the same state
    /// (although with various associated values changed).
    ///
    /// - Parameter started: The value associated with the `.started` state.
    /// - Returns: The new state.

    private func serviceOutput(started: Started) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        var started = started
        if started.hasSpaceAvailable && !started.outputBuffer.isEmpty {
            started.hasSpaceAvailable = false

            let outputBufferCount = started.outputBuffer.count
            let bytesWritten = started.outputBuffer.withUnsafeBytes { (bytes: UnsafePointer<UInt8>) in
                started.streams.outputStream.write(bytes, maxLength: outputBufferCount)
            }
            // We specifically don’t look for a negative value here (indicating
            // an error) because that will be delivered via the `.errorOccurred`
            // event.
            if bytesWritten > 0 {

                // Calling `remove(first:)` corrupts the `Data`
                // <rdar://problem/34206043>. Even replacing it with a subrange
                // doesn’t work, so I built a new data from a sequence of bytes.

                // started.outputBuffer.removeFirst(bytesWritten)
                let remainderIndex = started.outputBuffer.startIndex + bytesWritten
                // started.outputBuffer = started.outputBuffer[remainderIndex...]
                started.outputBuffer = Data([UInt8](started.outputBuffer[remainderIndex...]))
            }
        }
        return .started(started)
    }

    /// Services the input stream, read data from the stream, unframing it into
    /// lines, and passing any lines up to the delegate via the
    /// `didReceive(message:transport:)` callback.  Called when the object is in
    /// the `.started` state and typically leaves the object in the same state
    /// (although with various associated values changed).
    ///
    /// This is some of the trickiest code in this file because:
    ///
    /// * The unframer can error, which will stop the stream.
    ///
    /// * The unframer can generate multiple messages, which each have to
    ///   delivered to the delegate via a deferred closure.
    ///
    /// - Parameter started: The value associated with the `.started` state.
    /// - Returns: The new state.

    private func serviceInput(started: Started) -> State {
        dispatchPrecondition(condition: .onQueue(queue))
        var started = started

        // We always do a read, so we always clear `hasBytesAvailable`.  If
        // there were cases where we didn’t read — for example, if our buffer
        // was full — we’d only clear `hasBytesAvailable` on the code path where
        // we do that read.

        started.hasBytesAvailable = false

        // Do our read.

        let inputBufferCount = 2048
        var inputBuffer = Data(count: inputBufferCount)
        let bytesRead = inputBuffer.withUnsafeMutableBytes { (bytes: UnsafeMutablePointer<UInt8>) in
            started.streams.inputStream.read(bytes, maxLength: inputBufferCount)
        }

        // If we received data, run it through the unframer.
        //
        // We specifically don’t look for a negative value here (indicating an
        // error) because that will be delivered via the `.errorOccurred` event.

        let messages: [String]
        if bytesRead > 0 {
            inputBuffer.removeLast(inputBufferCount - bytesRead)
            do {
                messages = try started.unframer.lines(for: inputBuffer)
            } catch let error as LineUnframer.Error {
                return self.handleStop(error: Error.framingError(error), notify: true, state: .started(started))
            } catch {
                fatalError()
            }
        } else {
            messages = []
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
}

extension SocketStreamTransport : StreamDelegate {

    func stream(_ stream: Stream, handle eventCode: Stream.Event) {
        dispatchPrecondition(condition: .onQueue(queue))

        // Just route all of the events into our state machine.

        switch eventCode {
        case [.openCompleted]:
            self.process(event: .openCompleted(stream: stream))
        case [.hasSpaceAvailable]:
            self.process(event: .hasSpaceAvailable)
        case [.hasBytesAvailable]:
            self.process(event: .hasBytesAvailable)
        case [.endEncountered]:
            self.process(event: .stop(error: nil, notify: true))
        case [.errorOccurred]:
            fallthrough
        default:
            let error = stream.streamError.flatMap( { Error.streamError($0)} ) ?? Error.unknownError
            self.process(event: .stop(error: error, notify: true))
        }
    }
}

private extension Stream {

    /// Creates a socket stream pair that will connect to a host and port.
    ///
    /// This is a wrapper around
    /// `getStreamsToHost(withName:port:inputStream:outputStream:)` to make it
    /// much more Swift friendly.
    ///
    /// - Parameters:
    ///   - hostname: The host to connect to.
    ///   - port: The port on that host.
    /// - Returns: A socket stream pair that will connect to that host and port.

    static func streamsToHost(name hostname: String, port: Int) -> (inputStream: InputStream, outputStream: OutputStream) {
        var inStream: InputStream? = nil
        var outStream: OutputStream? = nil
        Stream.getStreamsToHost(withName: hostname, port: port, inputStream: &inStream, outputStream: &outStream)
        return (inStream!, outStream!)
    }
}
```

[Next](TCPTransports-BSDSocketsTransport.swift.md)[Previous](README.md.md)

