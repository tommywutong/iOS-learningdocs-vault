---
title: undefinedKeyException
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexceptionname/undefinedkeyexception
source_url: 'https://developer.apple.com/documentation/foundation/nsexceptionname/undefinedkeyexception'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexceptionname/undefinedkeyexception.json'
content_hash: 'sha256:3c627d05f36dd92a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExceptionName](../nsexceptionname.md)

# undefinedKeyException

<sub>Type Property</sub>

Raised when a key value coding operation fails.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let undefinedKeyException: NSExceptionName
```

## Discussion

`userInfo` keys are described in [NSUndefinedKeyException userInfo Keys](../../objectivec/nsundefinedkeyexception-userinfo-keys.md).

## See Also

### Type Properties

- [NSCharacterConversionException](characterconversionexception.md) — `NSString` raises an `NSCharacterConversionException` if a string cannot be represented in a file-system or string encoding.
- [NSDecimalNumberDivideByZeroException](decimalnumberdividebyzeroexception.md) — The exception raised on divide by zero.
- [NSDecimalNumberExactnessException](decimalnumberexactnessexception.md) — The exception raised if there is an exactness error.
- [NSDecimalNumberOverflowException](decimalnumberoverflowexception.md) — The exception raised on overflow.
- [NSDecimalNumberUnderflowException](decimalnumberunderflowexception.md) — The exception raised on underflow.
- [NSDestinationInvalidException](destinationinvalidexception.md) — Name of an exception that occurs when an internal assertion fails and implies an unexpected condition within the distributed objects.
- [NSFileHandleOperationException](filehandleoperationexception.md) — Raised by `NSFileHandle` if attempts to determine file-handle type fail or if attempts to read from a file or channel fail.
- [NSGenericException](genericexception.md) — A generic name for an exception.
- [NSInternalInconsistencyException](internalinconsistencyexception.md) — Name of an exception that occurs when an internal assertion fails and implies an unexpected condition within the called code.
- [NSInvalidArchiveOperationException](invalidarchiveoperationexception.md) — The name of the exception raised by `NSKeyedArchiver` if there is a problem creating an archive.
- [NSInvalidArgumentException](invalidargumentexception.md) — Name of an exception that occurs when you pass an invalid argument to a method, such as a `nil` pointer where a non-`nil` object is required.
- [NSInvalidReceivePortException](invalidreceiveportexception.md) — Name of an exception that occurs when the receive port of an `NSConnection` has become invalid.
- [NSInvalidSendPortException](invalidsendportexception.md) — Name of an exception that occurs when the send port of an `NSConnection` has become invalid.
- [NSInvalidUnarchiveOperationException](invalidunarchiveoperationexception.md) — The name of the exception raised by `NSKeyedArchiver` if there is a problem extracting an archive.
- [NSInvocationOperationCancelledException](invocationoperationcancelledexception.md) — The name of the exception raised if the [result](../nsinvocationoperation/result.md) method is called after the operation was cancelled.
