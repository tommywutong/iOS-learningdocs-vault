---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/Tests_TestServer_swift.html
archived_at: '2026-07-18T03:26:01.435828Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](Tests-TransportTests.swift.md)[Previous](App-iOS-EndpointPicker.swift.md)

# Tests/TestServer.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A TCP server for runnings tests against.
 */

import Foundation

class TestServer : NSObject, NetServiceDelegate {

    override init() {
        self.subservers = [
            .null: NetService(domain: "", type: "_x-test-null._tcp.", name: "", port: 0),
            .echo: NetService(domain: "", type: "_x-test-echo._tcp.", name: "", port: 0),
            .data: NetService(domain: "", type: "_x-test-data._tcp.", name: "", port: 0)
        ]
    }

    func start() {
        for service in self.subservers.values {
            service.delegate = self
            service.publish(options: [.listenForConnections])
        }
        repeat {
            if self.subservers.values.first(where: { $0.port == -1 }) == nil {
                break
            }
            RunLoop.current.run(mode: .defaultRunLoopMode, before: .distantFuture)
        } while true
    }

    func stop() {
        for service in self.subservers.values {
            service.delegate = nil
            service.stop()
        }
        for connection in self.connections {
            connection.stop()
        }
        assert(self.connections.isEmpty)
    }

    enum Subserver {
        case null
        case echo
        case data
    }

    var data: Data = Data()

    private let subservers: [Subserver:NetService]

    func port(for subserver: Subserver) -> Int {
        return self.subservers[subserver]!.port
    }

    // MARK: - Net Service Callbacks

    func netServiceDidPublish(_ sender: NetService) {
        // do nothing
    }

    func netService(_ sender: NetService, didNotPublish errorDict: [String : NSNumber]) {
        // If we fail to publish a service the entire test fails.
        fatalError()
    }

    func netService(_ sender: NetService, didAcceptConnectionWith inputStream: InputStream, outputStream: OutputStream) {
        let subserver = self.subservers.first(where: { $0.1 == sender })!.0
        let newConnection: Connection
        switch subserver {
        case .null:
            newConnection = NullConnection(subserver: subserver, inputStream: inputStream, outputStream: outputStream)
        case .echo:
            newConnection = EchoConnection(subserver: subserver, inputStream: inputStream, outputStream: outputStream)
        case .data:
            newConnection = DataConnection(subserver: subserver, inputStream: inputStream, outputStream: outputStream, data: self.data)
        }
        self.connections.append(newConnection)
        newConnection.start(completionHandler: {
            let index = self.connections.index(where: { $0 == newConnection} )!
            self.connections.remove(at: index)
        })
    }

    private var connections: [Connection] = []
}

private class Connection : NSObject {

    let subserver: TestServer.Subserver
    let inputStream: InputStream
    let outputStream: OutputStream
    var streams: [Stream] { return [self.inputStream, self.outputStream] }

    required init(subserver: TestServer.Subserver, inputStream: InputStream, outputStream: OutputStream) {
        self.subserver = subserver
        self.inputStream = inputStream
        self.outputStream = outputStream
    }

    private var completionHandler: (() -> Void)!

    func start(completionHandler: @escaping () -> Void) {
        precondition(self.completionHandler == nil)
        self.completionHandler = completionHandler
    }

    func stop() {
        self.completionHandler?()
    }
}

private final class NullConnection : Connection {

    override func start(completionHandler: @escaping () -> Void) {
        super.start(completionHandler: completionHandler)
        for stream in self.streams {
            stream.open()
        }
        for stream in self.streams {
            stream.close()
        }
        self.stop()
    }
}

private final class EchoConnection : Connection, StreamDelegate {

    required init(subserver: TestServer.Subserver, inputStream: InputStream, outputStream: OutputStream) {
        self.outputBuffer = Data()
        self.hasSpaceAvailable = false
        super.init(subserver: subserver, inputStream: inputStream, outputStream: outputStream)
    }

    private var outputBuffer: Data
    private var hasSpaceAvailable: Bool

    override func start(completionHandler: @escaping () -> Void) {
        super.start(completionHandler: completionHandler)
        for stream in streams {
            stream.delegate = self
            stream.schedule(in: .current, forMode: .defaultRunLoopMode)
            stream.open()
        }
    }

    override func stop() {
        for stream in streams {
            stream.delegate = self
            stream.close()
        }
        super.stop()
    }

    func stream(_ aStream: Stream, handle eventCode: Stream.Event) {
        switch eventCode {
        case [.openCompleted]:
            break
        case [.hasBytesAvailable]:
            self.serviceInput()
        case [.hasSpaceAvailable]:
            self.hasSpaceAvailable = true
            self.serviceOutput()
        case [.endEncountered]:
            self.stop()
        case [.errorOccurred]:
            self.stop()
        default:
            fatalError()
        }
    }

    private func serviceInput() {
        // You wouldn’t want to do this in a real app because there’s no bound
        // to the amount of data that we’ll buffer in `outputBuffer`.  But for
        // server that exists solely to support tests, this is fine.
        let inputBufferCount = 2048
        var inputBuffer = [UInt8](repeating: 0, count: inputBufferCount)
        let bytesRead = self.inputStream.read(&inputBuffer, maxLength: inputBufferCount)
        if bytesRead > 0 {
            self.outputBuffer.append(contentsOf: inputBuffer[0..<bytesRead])
            self.serviceOutput()
        }
    }

    private func serviceOutput() {
        let outputBufferCount = self.outputBuffer.count
        guard self.hasSpaceAvailable && outputBufferCount != 0 else {
            return
        }
        let bytesWritten = self.outputBuffer.withUnsafeBytes { (bytes: UnsafePointer<UInt8>) in
            self.outputStream.write(bytes, maxLength: outputBufferCount)
        }
        if bytesWritten > 0 {
            self.outputBuffer = Data(bytes: [UInt8](self.outputBuffer[bytesWritten...]))
        }
    }
}

private final class DataConnection : Connection, StreamDelegate {

    required init(subserver: TestServer.Subserver, inputStream: InputStream, outputStream: OutputStream, data: Data) {
        self.outputBuffer = data
        self.hasSpaceAvailable = false
        super.init(subserver: subserver, inputStream: inputStream, outputStream: outputStream)
    }

    required init(subserver: TestServer.Subserver, inputStream: InputStream, outputStream: OutputStream) {
        self.outputBuffer = Data()
        self.hasSpaceAvailable = false
        super.init(subserver: subserver, inputStream: inputStream, outputStream: outputStream)
    }

    private var outputBuffer: Data
    private var hasSpaceAvailable: Bool

    override func start(completionHandler: @escaping () -> Void) {
        super.start(completionHandler: completionHandler)
        for stream in streams {
            stream.delegate = self
            stream.schedule(in: .current, forMode: .defaultRunLoopMode)
            stream.open()
        }
    }

    override func stop() {
        for stream in streams {
            stream.delegate = self
            stream.close()
        }
        super.stop()
    }

    func stream(_ aStream: Stream, handle eventCode: Stream.Event) {
        switch eventCode {
        case [.openCompleted]:
            break
        case [.hasBytesAvailable]:
            self.serviceInput()
        case [.hasSpaceAvailable]:
            self.hasSpaceAvailable = true
            self.serviceOutput()
        case [.endEncountered]:
            self.stop()
        case [.errorOccurred]:
            self.stop()
        default:
            fatalError()
        }
    }

    private func serviceInput() {
        // Read the input and throw it away.
        let inputBufferCount = 2048
        var inputBuffer = [UInt8](repeating: 0, count: inputBufferCount)
        _ = self.inputStream.read(&inputBuffer, maxLength: inputBufferCount)
    }

    private func serviceOutput() {
        let outputBufferCount = self.outputBuffer.count
        guard self.hasSpaceAvailable && outputBufferCount != 0 else {
            return
        }
        let bytesWritten = self.outputBuffer.withUnsafeBytes { (bytes: UnsafePointer<UInt8>) in
            self.outputStream.write(bytes, maxLength: outputBufferCount)
        }
        if bytesWritten > 0 {
            self.outputBuffer = Data(bytes: [UInt8](self.outputBuffer[bytesWritten...]))
        }
    }
}
```

[Next](Tests-TransportTests.swift.md)[Previous](App-iOS-EndpointPicker.swift.md)

