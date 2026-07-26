---
title: Error
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/error
source_url: 'https://developer.apple.com/documentation/swift/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/error.json'
content_hash: 'sha256:c9e79ac8b9b20086'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Error

<sub>Protocol</sub>

A type representing an error value that can be thrown.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Error : Sendable
```

## Overview

Any type that declares conformance to the `Error` protocol can be used to represent an error in Swift’s error handling system. Because the `Error` protocol has no requirements of its own, you can declare conformance on any custom type you create.

## Using Enumerations as Errors

Swift’s enumerations are well suited to represent simple errors. Create an enumeration that conforms to the `Error` protocol with a case for each possible error. If there are additional details about the error that could be helpful for recovery, use associated values to include that information.

The following example shows an `IntParsingError` enumeration that captures two different kinds of errors that can occur when parsing an integer from a string: overflow, where the value represented by the string is too large for the integer data type, and invalid input, where nonnumeric characters are found within the input.

```swift
enum IntParsingError: Error {
    case overflow
    case invalidInput(Character)
}
```

The `invalidInput` case includes the invalid character as an associated value.

The next code sample shows a possible extension to the `Int` type that parses the integer value of a `String` instance, throwing an error when there is a problem during parsing.

```swift
extension Int {
    init(validating input: String) throws {
        // ...
        let c = _nextCharacter(from: input)
        if !_isValid(c) {
            throw IntParsingError.invalidInput(c)
        }
        // ...
    }
}
```

When calling the new `Int` initializer within a `do` statement, you can use pattern matching to match specific cases of your custom error type and access their associated values, as in the example below.

```swift
do {
    let price = try Int(validating: "$100")
} catch IntParsingError.invalidInput(let invalid) {
    print("Invalid character: '\(invalid)'")
} catch IntParsingError.overflow {
    print("Overflow error")
} catch {
    print("Other error")
}
// Prints "Invalid character: '$'"
```

## Including More Data in Errors

Sometimes you may want different error states to include the same common data, such as the position in a file or some of your application’s state. When you do, use a structure to represent errors. The following example uses a structure to represent an error when parsing an XML document, including the line and column numbers where the error occurred:

```swift
struct XMLParsingError: Error {
    enum Kind {
        case invalidCharacter
        case mismatchedTag
        case internalError
    }

    let line: Int
    let column: Int
    let kind: Kind
}

func parse(_ source: String) throws -> XMLDoc {
    // ...
    throw XMLParsingError(line: 19, column: 5, kind: .mismatchedTag)
    // ...
}
```

Once again, use pattern matching to conditionally catch errors. Here’s how you can catch any `XMLParsingError` errors thrown by the `parse(_:)` function:

```swift
do {
    let xmlDoc = try parse(myXMLData)
} catch let e as XMLParsingError {
    print("Parsing error: \(e.kind) [\(e.line):\(e.column)]")
} catch {
    print("Other error: \(error)")
}
// Prints "Parsing error: mismatchedTag [19:5]"
```

## Relationships

- **Inherits From**: [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

- **Inherited By**: [DistributedActorSystemError](../distributed/distributedactorsystemerror.md)

- **Conforming Types**: [CancellationError](cancellationerror.md), [DecodingError](decodingerror.md), [DistributedActorCodingError](../distributed/distributedactorcodingerror.md), [EncodingError](encodingerror.md), [ExecuteDistributedTargetError](../distributed/executedistributedtargeterror.md), [LocalTestingDistributedActorSystemError](../distributed/localtestingdistributedactorsystemerror.md), [Never](never.md), [ValidationError](unicode/utf8/validationerror.md), [Kind](unicode/utf8/validationerror/kind-swift.struct.md)

## Topics

### Describing an Error

- [localizedDescription](error/localizeddescription.md) — Retrieve the localized description for this error.

## See Also

### Errors

- [Result](result.md) — A value that represents either a success or a failure, including an associated value in each case.
