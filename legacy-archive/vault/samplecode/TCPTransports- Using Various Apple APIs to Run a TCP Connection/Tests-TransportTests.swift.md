---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/Tests_TransportTests_swift.html
archived_at: '2026-07-18T03:26:01.533526Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](Tests-LineFramingTests.swift.md)[Previous](Tests-TestServer.swift.md)

# Tests/TransportTests.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Tests for the various TCPTransport implementations.
 */

import XCTest
@testable import TCPTransports_iOS

class TransportTests : XCTestCase, TCPTransportDelegate {

    // MARK: - Server

    override class func setUp() {
        super.setUp()
        let server = TestServer()
        self.server = server
        server.start()
    }

    override class func tearDown() {
        self.server?.stop()
        self.server = nil
        super.tearDown()
    }

    // Note that the server is static, and set up by the class method, because
    // it can take a while for it to start up and we don’t want to pay that cost
    // for every test in this class.

    static var server: TestServer!

    // MARK: - Client

    override func setUp() {
        super.setUp()
        self.log = []
        self.linesToWrite = []
    }

    func run(interval: TimeInterval) {
        let deadline = Date(timeIntervalSinceNow: interval)
        while Date() < deadline {
            RunLoop.current.run(mode: .defaultRunLoopMode, before: deadline)
        }
    }

    var log: [String] = []
    var linesToWrite: [String] = []

    func didStart(transport: TCPTransport) {
        self.log.append("!B")
        for message in self.linesToWrite {
            transport.send(message: message)
        }
        self.linesToWrite = []
    }

    func didReceive(message: String, transport: TCPTransport) {
        self.log.append("!R-\(message)")
    }

    func didStop(transport: TCPTransport) {
        self.log.append("!E")
    }

    // MARK: - Null Tests

    func runNullTest(endpointTransport: Endpoint.Transport) {
        let port = TransportTests.server.port(for: .null)
        let endpoint = Endpoint(transport: endpointTransport, hostName: "127.0.0.1", port: port, useTLS: false)

        var transport: TCPTransport! = nil
        XCTAssertNoThrow(transport = try ConversationTransport.transport(for: endpoint))
        guard transport != nil else { return }

        transport.delegate = self
        transport.start()

        self.run(interval: 2.0)

        XCTAssertEqual(self.log, ["!B", "!E"])
    }

    func testNullSocketStream() {
        self.runNullTest(endpointTransport: .socketStream)
    }

    func testNullStreamTask() {
        self.runNullTest(endpointTransport: .streamTask)
    }

    func testNullBSDSockets() {
        self.runNullTest(endpointTransport: .bsdSockets)
    }

    func testNullNWTCPConnection() {
        // This test is a no-op if NWTCPConnection is not available.
        guard NWTCPTransport.isNWTCPConnectionAvailable else { return }
        self.runNullTest(endpointTransport: .nwTCPConnection)
    }

    // MARK: - Echo Tests

    func runEchoTest(endpointTransport: Endpoint.Transport) {
        let port = TransportTests.server.port(for: .echo)
        let endpoint = Endpoint(transport: endpointTransport, hostName: "127.0.0.1", port: port, useTLS: false)

        var transport: TCPTransport! = nil
        XCTAssertNoThrow(transport = try ConversationTransport.transport(for: endpoint))
        guard transport != nil else { return }

        self.linesToWrite = [
            "Hello",
            "Cruel",
            "World!"
        ]

        transport.delegate = self
        transport.start()

        self.run(interval: 2.0)

        transport.stop()

        // We don't get !E because we called `stop()` and `didStop(…)` is only
        // called when the stop comes from ‘below’.

        XCTAssertEqual(self.log, ["!B", "!R-Hello", "!R-Cruel", "!R-World!"])
    }

    func testEchoSocketStream() {
        self.runEchoTest(endpointTransport: .socketStream)
    }

    func testEchoStreamTask() {
        self.runEchoTest(endpointTransport: .streamTask)
    }

    func testEchoBSDSockets() {
        self.runEchoTest(endpointTransport: .bsdSockets)
    }

    func testEchoNWTCPConnection() {
        // This test is a no-op if NWTCPConnection is not available.
        guard NWTCPTransport.isNWTCPConnectionAvailable else { return }
        self.runEchoTest(endpointTransport: .nwTCPConnection)
    }

    // MARK: - Data Tests

    func runNoCRLFTest(endpointTransport: Endpoint.Transport) {
        let port = TransportTests.server.port(for: .data)
        let endpoint = Endpoint(transport: endpointTransport, hostName: "127.0.0.1", port: port, useTLS: false)

        var transport: TCPTransport! = nil
        XCTAssertNoThrow(transport = try ConversationTransport.transport(for: endpoint))
        guard transport != nil else { return }

        // Note the lack of the trailing CR LF.
        TransportTests.server.data = "Hello\r\nCruel\r\nWorld!".data(using: .utf8)!

        transport.delegate = self
        transport.start()

        self.run(interval: 2.0)

        transport.stop()

        // We don't get "!E" because we called `stop()` and `didStop(…)` is only
        // called when the stop comes from ‘below’.
        //
        // We don't get the "!R-World!" because it’s missing its trailing CR LF.

        XCTAssertEqual(self.log, ["!B", "!R-Hello", "!R-Cruel"])
    }

    func testNoCRLFSocketStream() {
        self.runNoCRLFTest(endpointTransport: .socketStream)
    }

    func testNoCRLFStreamTask() {
        self.runNoCRLFTest(endpointTransport: .streamTask)
    }

    func testNoCRLFBSDSockets() {
        self.runNoCRLFTest(endpointTransport: .bsdSockets)
    }

    func testNoCRLFNWTCPConnection() {
        // This test is a no-op if NWTCPConnection is not available.
        guard NWTCPTransport.isNWTCPConnectionAvailable else { return }
        self.runNoCRLFTest(endpointTransport: .nwTCPConnection)
    }

    func runLongLineTest(endpointTransport: Endpoint.Transport, extractFramingError: (Error) -> LineUnframer.Error?) {
        let port = TransportTests.server.port(for: .data)
        let endpoint = Endpoint(transport: endpointTransport, hostName: "127.0.0.1", port: port, useTLS: false)

        var transport: TCPTransport! = nil
        XCTAssertNoThrow(transport = try ConversationTransport.transport(for: endpoint))
        guard transport != nil else { return }

        // Note the lack of the trailing CR LF.
        TransportTests.server.data = "Hello\r\nCruel\r\n".data(using: .utf8)! +
            Data(repeating: 0x65, count: 1204) +
            "\r\nWorld!".data(using: .utf8)!

        transport.delegate = self
        transport.start()

        self.run(interval: 2.0)

        transport.stop()

        // We do get "!E" because the error came from ‘below’ and hence
        // `didStop(…)` is called.
        //
        // We don't get the "!R-Hello" and "!R-Cruel" because the framing error
        // is detected in the first chunk of data and that triggers the failure.
        // However, those lines are available in the error itself.
        //
        // - note: In theory the data could be split across multiple chunks in
        //   which case we might get one or maybe even two lines before seeing
        //   the framing error.  In practice this doesn’t happen. If the test
        //   starts failing in this way, I’ll have to revise this code to be
        //   smarter (look for lines in the log and then not expect those lines
        //   in the `linesSoFar`).

        XCTAssertEqual(self.log, ["!B", "!E"])
        switch transport.transportState {
        case .stopped(let error):
            if let error = error, let framingError = extractFramingError(error) {
                XCTAssertTrue(framingError.code == .lineTooLong)
                XCTAssertTrue(framingError.linesSoFar == ["Hello", "Cruel"])
            } else {
                XCTAssertTrue(false)
            }
        default:
            XCTAssertTrue(false)
        }
    }

    func testLongLineSocketStream() {
        self.runLongLineTest(endpointTransport: .socketStream, extractFramingError: { error in
            switch error {
            case SocketStreamTransport.Error.framingError(let framingError):
                return framingError
            default:
                return nil
            }
        })
    }

    func testLongLineStreamTask() {
        self.runLongLineTest(endpointTransport: .streamTask, extractFramingError: { error in
            switch error {
            case StreamTaskTransport.Error.framingError(let framingError):
                return framingError
            default:
                return nil
            }
        })
    }

    func testLongLineBSDSockets() {
        self.runLongLineTest(endpointTransport: .bsdSockets, extractFramingError: { error in
            switch error {
            case BSDSocketsTransport.Error.framingError(let framingError):
                return framingError
            default:
                return nil
            }
        })
    }

    func testLongLineNWTCPConnection() {
        // This test is a no-op if NWTCPConnection is not available.
        guard NWTCPTransport.isNWTCPConnectionAvailable else { return }
        self.runLongLineTest(endpointTransport: .nwTCPConnection, extractFramingError: { error in
            switch error {
            case NWTCPTransport.Error.framingError(let framingError):
                return framingError
            default:
                return nil
            }
        })
    }
}
```

[Next](Tests-LineFramingTests.swift.md)[Previous](Tests-TestServer.swift.md)

