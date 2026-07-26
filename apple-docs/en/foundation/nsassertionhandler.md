---
title: NSAssertionHandler
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsassertionhandler
source_url: 'https://developer.apple.com/documentation/foundation/nsassertionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsassertionhandler.json'
content_hash: 'sha256:ae6b7f88adf336e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSAssertionHandler

<sub>Class</sub>

An object that logs an assertion to the console.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSAssertionHandler
```

## Overview

`NSAssertionHandler` objects are automatically created to handle false assertions. Assertion macros, such as `NSAssert` and `NSCAssert`, are used to evaluate a condition, and if the condition evaluates to false, the macros pass a string to an `NSAssertionHandler` object describing the failure. Each thread has its own `NSAssertionHandler` object. When invoked, an assertion handler prints an error message that includes the method and class (or function) containing the assertion and raises an `NSInternalInconsistencyException`.

You create assertions only using the assertion macros—you rarely need to invoke `NSAssertionHandler` methods directly. The macros for use inside methods and functions send [handleFailureInMethod:object:file:lineNumber:description:](nsassertionhandler/handlefailureinmethod_object_file_linenumber_description_.md) and [handleFailureInFunction:file:lineNumber:description:](nsassertionhandler/handlefailureinfunction_file_linenumber_description_.md) messages respectively to the current assertion handler. The assertion handler for the current thread is obtained using the [currentHandler](nsassertionhandler/current.md) class method. See doc:nsassertionhandlerkey if you need to customize the behavior of [NSAssertionHandler](nsassertionhandler.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling Assertion Failures

- [currentHandler](nsassertionhandler/current.md) — Returns the `NSAssertionHandler` object associated with the current thread.
