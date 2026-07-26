---
title: NSException
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexception
source_url: 'https://developer.apple.com/documentation/foundation/nsexception'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexception.json'
content_hash: 'sha256:2d3613684372cbb7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSException

<sub>Class</sub>

An object that represents a special condition that interrupts the normal flow of program execution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSException
```

## Overview

Use [NSException](nsexception.md) to implement exception handling. An exception is a special condition that interrupts the normal flow of program execution. Each application can interrupt the program for different reasons. For example, one application might interpret saving a file in a directory that is write-protected as an exception. In this sense, the exception is equivalent to an error. Another application might interpret the user’s key-press (for example, Control-C) as an exception: an indication that a long-running process should abort.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Creating and Raising an NSException Object

- [+ raise:format:arguments:](<nsexception/raise(__format_arguments_).md>) — Creates and raises an exception with the specified name, reason, and arguments.
- [- initWithName:reason:userInfo:](<nsexception/init(name_reason_userinfo_).md>) — Initializes and returns a newly allocated exception object.
- [- raise](<nsexception/raise().md>) — Raises the receiver, causing program flow to jump to the local exception handler.

### Querying an NSException Object

- [name](nsexception/name-swift.property.md) — A string used to uniquely identify the receiver.
- [reason](nsexception/reason-swift.property.md) — A string containing a “human-readable” reason for the receiver.
- [userInfo](nsexception/userinfo-swift.property.md) — A dictionary containing application-specific data pertaining to the receiver.

### Getting Exception Stack Frames

- [callStackReturnAddresses](nsexception/callstackreturnaddresses.md) — The call return addresses related to a raised exception.
- [callStackSymbols](nsexception/callstacksymbols.md) — An array containing the current call stack symbols.

### Related Types

- [NSUncaughtExceptionHandler](nsuncaughtexceptionhandler.md) — The type for uncaught exception handler functions.
- [NSExceptionName](nsexceptionname.md)

### Functions

- [NSGetUncaughtExceptionHandler](<nsgetuncaughtexceptionhandler().md>) — Returns the top-level error handler.
- [NSSetUncaughtExceptionHandler](<nssetuncaughtexceptionhandler(__).md>) — Changes the top-level error handler.

### Initializers

- [init(coder:)](<nsexception/init(coder_).md>)
