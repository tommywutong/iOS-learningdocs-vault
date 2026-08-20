---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/Tests_LineFramingTests_swift.html
archived_at: '2026-07-18T03:26:01.380139Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](README.md.md)[Previous](Tests-TransportTests.swift.md)

# Tests/LineFramingTests.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Tests for the line framing code.
 */

import XCTest
@testable import TCPTransports_iOS

class LineFramingTests : XCTestCase {

    func testFramer() {
        let framer = LineFramer()
        XCTAssertEqual(framer.data(for: []), "".data(using: .utf8)!)
        XCTAssertEqual(framer.data(for: [""]), "\r\n".data(using: .utf8)!)
        XCTAssertEqual(framer.data(for: ["", ""]), "\r\n\r\n".data(using: .utf8)!)
        XCTAssertEqual(framer.data(for: ["abc", ""]), "abc\r\n\r\n".data(using: .utf8)!)
        XCTAssertEqual(framer.data(for: ["", "def"]), "\r\ndef\r\n".data(using: .utf8)!)
        XCTAssertEqual(framer.data(for: ["abc", "def"]), "abc\r\ndef\r\n".data(using: .utf8)!)
        XCTAssertEqual(framer.data(for: ["abc", "def", "hij"]), "abc\r\ndef\r\nhij\r\n".data(using: .utf8)!)
        XCTAssertEqual(framer.data(for: ["abc", "", "hij"]), "abc\r\n\r\nhij\r\n".data(using: .utf8)!)
    }

    func testUnframer() {
        func test(_ chunks: [String], maxLineLength: Int = 1024) -> [String] {
            var unframer = LineUnframer(maxLineLength: maxLineLength)
            return chunks.map {
                try! (unframer.lines(for: $0.data(using: .utf8)!)).joined(separator: "/")
            }
        }
        XCTAssertEqual(test([]), [])
        XCTAssertEqual(test(["abc"]), [""])   // no lines because no CR LF
        XCTAssertEqual(test(["abc\r\ndef\r\n"]), ["abc/def"])
        XCTAssertEqual(test(["abc\r\n", "def\r\n"]), ["abc", "def"])
        XCTAssertEqual(test(["a", "b", "c", "\r", "\n", "d", "e", "f", "\r", "\n"]), ["", "", "", "", "abc", "", "", "", "", "def"])
        XCTAssertEqual(test(["abc\rdef\r\n"]), ["abc\rdef"])            // 'naked' CR doesn't get lost
        XCTAssertEqual(test(["abc\r", "def\r\n"]), ["", "abc\rdef"])

        XCTAssertEqual(test(["1234\r\n"], maxLineLength: 4), ["1234"])
        XCTAssertEqual(test(["12", "34\r\n"], maxLineLength: 4), ["", "1234"])
        XCTAssertEqual(test(["12", "34", "\r\n"], maxLineLength: 4), ["", "", "1234"])

        XCTAssertEqual(test(["AB\r\n1234\r\n"], maxLineLength: 4), ["AB/1234"])
        XCTAssertEqual(test(["AB\r\n12", "34\r\n"], maxLineLength: 4), ["AB", "1234"])
        XCTAssertEqual(test(["AB\r\n12", "34", "\r\n"], maxLineLength: 4), ["AB", "", "1234"])
    }

    func testUnframerError() {
        func test(_ chunks: [String], _ expected: [String], _ expectedError: LineUnframer.Error) -> Bool {
            var unframer = LineUnframer(maxLineLength: 4)
            var actual: [String] = []
            var actualError: LineUnframer.Error? = nil
            for chunk in chunks {
                do {
                    actual.append(try unframer.lines(for: chunk.data(using: .utf8)!).joined(separator: "/"))
                } catch let error as LineUnframer.Error {
                    actualError = error
                    break
                } catch {
                    NSLog("error: %@", "\(error)")
                    return false
                }
            }
            guard actualError != nil else {
                NSLog("no error!")
                return false
            }
            guard actual == expected else {
                NSLog("expected: %@", expected)
                NSLog("actual: %@", actual)
                return false
            }
            guard actualError! == expectedError else {
                NSLog("expected: %@", "\(expectedError)")
                NSLog("actual: %@", "\(actualError!)")
                return false
            }
            return true
        }
        XCTAssertTrue(test(["12345"], [], .init(code: .lineTooLong, linesSoFar: [])))
        XCTAssertTrue(test(["12345\r\n"], [], .init(code: .lineTooLong, linesSoFar: [])))
        XCTAssertTrue(test(["12345\r\nef\r\n"], [], .init(code: .lineTooLong, linesSoFar: [])))
        XCTAssertTrue(test(["123", "45"], [""], .init(code: .lineTooLong, linesSoFar: [])))
        XCTAssertTrue(test(["ab\r\ncd\r\n12345"], [], .init(code: .lineTooLong, linesSoFar: ["ab", "cd"])))
        XCTAssertTrue(test(["ab\r\ncd\r\n12345\r\nef\r\n"], [], .init(code: .lineTooLong, linesSoFar: ["ab", "cd"])))

        XCTAssertTrue(test(["AB\r\n", "12345"], ["AB"], .init(code: .lineTooLong, linesSoFar: [])))
        XCTAssertTrue(test(["AB\r\n", "12345\r\n"], ["AB"], .init(code: .lineTooLong, linesSoFar: [])))
        XCTAssertTrue(test(["AB\r\n", "12345\r\nef\r\n"], ["AB"], .init(code: .lineTooLong, linesSoFar: [])))
        XCTAssertTrue(test(["AB\r\n", "123", "45"], ["AB", ""], .init(code: .lineTooLong, linesSoFar: [])))
        XCTAssertTrue(test(["AB\r\n", "ab\r\ncd\r\n12345"], ["AB"], .init(code: .lineTooLong, linesSoFar: ["ab", "cd"])))
        XCTAssertTrue(test(["AB\r\n", "ab\r\ncd\r\n12345\r\nef\r\n"], ["AB"], .init(code: .lineTooLong, linesSoFar: ["ab", "cd"])))

        XCTAssertTrue(test(["1234\r\r\n"], [], .init(code: .lineTooLong, linesSoFar: [])))
    }
}
```

[Next](README.md.md)[Previous](Tests-TransportTests.swift.md)

