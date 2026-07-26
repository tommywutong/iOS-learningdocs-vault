---
title: 'init(name:reason:userInfo:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexception/init(name:reason:userinfo:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexception/init(name:reason:userinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexception/init%28name%3Areason%3Auserinfo%3A%29.json'
content_hash: 'sha256:8214e1bbbef06a86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSException](../nsexception.md)

# init(name:reason:userInfo:)

<sub>Initializer</sub>

Initializes and returns a newly allocated exception object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(name aName: NSExceptionName, reason aReason: String?, userInfo aUserInfo: [AnyHashable : Any]? = nil)
```

## Parameters

- `aName` — The name of the exception.

- `aReason` — A human-readable message string summarizing the reason for the exception.

- `aUserInfo` — A dictionary containing user-defined information relating to the exception

## Return Value

The created `NSException` object or `nil` if the object couldn’t be created.

## Discussion

This is the designated initializer.

## See Also

### Creating and Raising an NSException Object

- [+ raise:format:arguments:](<raise(__format_arguments_).md>) — Creates and raises an exception with the specified name, reason, and arguments.
- [- raise](<raise().md>) — Raises the receiver, causing program flow to jump to the local exception handler.
