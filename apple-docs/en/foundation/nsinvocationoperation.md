---
title: NSInvocationOperation
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsinvocationoperation
source_url: 'https://developer.apple.com/documentation/foundation/nsinvocationoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinvocationoperation.json'
content_hash: 'sha256:68a35d55ecbccc29'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSInvocationOperation

<sub>Class</sub>

An operation that manages the execution of a single encapsulated task specified as an invocation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface NSInvocationOperation : NSOperation
```

## Overview

The [NSInvocationOperation](nsinvocationoperation.md) class is a concrete subclass of [Operation](operation.md) that you use to initiate an operation that consists of invoking a selector on a specified object. This class implements a non-concurrent operation.

For more information on concurrent versus non-concurrent operations, see [Operation](operation.md).

## Relationships

- **Inherits From**: [Operation](operation.md)

## Topics

### Initialization

- [initWithTarget:selector:object:](nsinvocationoperation/initwithtarget_selector_object_.md) — Returns an `NSInvocationOperation` object initialized with the specified target and selector.
- [initWithInvocation:](nsinvocationoperation/initwithinvocation_.md) — Returns an `NSInvocationOperation` object initialized with the specified invocation object.

### Getting Attributes

- [invocation](nsinvocationoperation/invocation.md) — The receiver’s invocation object.
- [result](nsinvocationoperation/result.md) — The result of the invocation or method.

### Constants

- [Result Exceptions](result-exceptions.md) — Names of exceptions raised by `NSInvocationOperation` if there is an error when calling the [result](nsinvocationoperation/result.md) method.

## See Also

### Operations

- [OperationQueue](operationqueue.md) — A queue that regulates the execution of operations.
- [Operation](operation.md) — An abstract class that represents the code and data associated with a single task.
- [BlockOperation](blockoperation.md) — An operation that manages the concurrent execution of one or more blocks.
