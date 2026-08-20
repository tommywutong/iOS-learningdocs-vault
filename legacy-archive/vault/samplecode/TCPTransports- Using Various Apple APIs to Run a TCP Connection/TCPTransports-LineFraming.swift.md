---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/TCPTransports_LineFraming_swift.html
archived_at: '2026-07-18T03:26:00.619686Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](TCPTransports-StreamTaskTransport.swift.md)[Previous](TCPTransports-NWTCPTransport.swift.md)

# TCPTransports/LineFraming.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Frames and unframes lines.
 */

import Foundation

/// Takes an array of lines and frames them in the standard way used by Internet
/// protocols, that is, adding a CR LF at the end.
///
/// This cannot throw because, hey, you shouldn’t have given it bogus strings
/// in the first place.
///
/// - note: This is a method on a `struct` to match `LineUnframer`, which has to
///     maintain complex state.  It’s also possible to imagine a different type
///     of framer that needs to maintain state.

struct LineFramer {

    func data(for lines: [String]) -> Data {
        return lines.map { "\($0)\r\n" }.joined().data(using: .utf8)!
    }
}

/// Takes data and parses it looking for lines.
///
/// This has to maintain a buffer of data looking for line breaks.  You
/// initialise it with the maximum line length, measured in bytes of
/// UTF-8 encoded data.
///
/// Also, this will throw if it gets a malformed line, including:
///
/// * Code sequences that aren’t valid UTF-8
/// * The line is too long.

struct LineUnframer {

    init(maxLineLength: Int) {
        precondition(maxLineLength > 0)
        self.maxLineLength = maxLineLength
    }

    let maxLineLength: Int

    private enum State {
        case standard(Data)
        case expectingLF(Data)
        case error(Swift.Error)
    }

    private var state: State = .standard(Data())

    mutating func lines(for data: Data) throws -> [String] {
        if case .error(let error) = self.state {
            throw error
        }

        var result: [String] = []

        func extendLine(_ lineData: Data, _ bytes: [UInt8]) throws {
            if lineData.count + bytes.count > self.maxLineLength {
                throw Error(code: .lineTooLong, linesSoFar: result)
            }
            self.state = .standard(lineData + bytes)
        }

        for c in data {
            switch (self.state, c) {
            case (.expectingLF(let lineData), 10):
                guard let line = String(bytes: lineData, encoding: .utf8) else {
                    throw Error(code: .malformedUTF8, linesSoFar: result)
                }
                result.append(line)
                self.state = .standard(Data())
            case (.expectingLF(let lineData), let b):
                try extendLine(lineData, [13, b])
            case (.standard(let lineData), 13):
                self.state = .expectingLF(lineData)
            case (.standard(let lineData), let b):
                try extendLine(lineData, [b])
            case (.error, _):
                fatalError()
            }
        }
        return result
    }

    struct Error : Swift.Error, Equatable {
        enum Code {
        case lineTooLong
        case malformedUTF8
        }
        var code: Code
        var linesSoFar: [String]
        static func ==(lhs: Error, rhs: Error) -> Bool {
            return lhs.code == rhs.code && lhs.linesSoFar == rhs.linesSoFar
        }
    }
}
```

[Next](TCPTransports-StreamTaskTransport.swift.md)[Previous](TCPTransports-NWTCPTransport.swift.md)

