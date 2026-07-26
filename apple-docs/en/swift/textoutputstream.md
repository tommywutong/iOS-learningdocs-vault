---
title: TextOutputStream
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/textoutputstream
source_url: 'https://developer.apple.com/documentation/swift/textoutputstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/textoutputstream.json'
content_hash: 'sha256:685114c83a48f695'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# TextOutputStream

<sub>Protocol</sub>

A type that can be the target of text-streaming operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol TextOutputStream
```

## Overview

You can send the output of the standard library’s `print(_:to:)` and `dump(_:to:)` functions to an instance of a type that conforms to the `TextOutputStream` protocol instead of to standard output. Swift’s `String` type conforms to `TextOutputStream` already, so you can capture the output from `print(_:to:)` and `dump(_:to:)` in a string instead of logging it to standard output.

```swift
var s = ""
for n in 1...5 {
    print(n, terminator: "", to: &s)
}
// s == "12345"
```

## Conforming to the TextOutputStream Protocol

To make your custom type conform to the `TextOutputStream` protocol, implement the required `write(_:)` method. Functions that use a `TextOutputStream` target may call `write(_:)` multiple times per writing operation.

As an example, here’s an implementation of an output stream that converts any input to its plain ASCII representation before sending it to standard output.

```swift
struct ASCIILogger: TextOutputStream {
    mutating func write(_ string: String) {
        let ascii = string.unicodeScalars.lazy.map { scalar in
            scalar == "\n"
              ? "\n"
              : scalar.escaped(asASCII: true)
        }
        print(ascii.joined(separator: ""), terminator: "")
    }
}
```

The `ASCIILogger` type’s `write(_:)` method processes its string input by escaping each Unicode scalar, with the exception of `"\n"` line returns. By sending the output of the `print(_:to:)` function to an instance of `ASCIILogger`, you invoke its `write(_:)` method.

```swift
let s = "Hearts ♡ and Diamonds ♢"
print(s)
// Prints "Hearts ♡ and Diamonds ♢"

var asciiLogger = ASCIILogger()
print(s, to: &asciiLogger)
// Prints "Hearts \u{2661} and Diamonds \u{2662}"
```

## Relationships

- **Inherited By**: [StringProtocol](stringprotocol.md)

- **Conforming Types**: [DefaultStringInterpolation](defaultstringinterpolation.md), [String](string.md), [Substring](substring.md)

## Topics

### Instance Methods

- [write(_:)](<textoutputstream/write(__).md>) — Appends the given string to the stream.

## See Also

### Streams

- [TextOutputStreamable](textoutputstreamable.md) — A source of text-streaming operations.
