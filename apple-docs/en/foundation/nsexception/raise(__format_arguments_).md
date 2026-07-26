---
title: 'raise(_:format:arguments:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexception/raise(_:format:arguments:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexception/raise(_:format:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexception/raise%28_%3Aformat%3Aarguments%3A%29.json'
content_hash: 'sha256:73709aeb7b5ee609'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSException](../nsexception.md)

# raise(_:format:arguments:)

<sub>Type Method</sub>

Creates and raises an exception with the specified name, reason, and arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func raise(_ name: NSExceptionName, format: String, arguments argList: CVaListPointer)
```

## Parameters

- `name` — The name of the exception.

- `format` — A human-readable message string (that is, the exception reason) with conversion specifications for the variable arguments in `argList`.

- `argList` — Variable information to be inserted into the formatted exception reason (in the manner of `vprintf`).

## Discussion

The user-defined dictionary of the generated object is `nil`.

## See Also

### Creating and Raising an NSException Object

- [- initWithName:reason:userInfo:](<init(name_reason_userinfo_).md>) — Initializes and returns a newly allocated exception object.
- [- raise](<raise().md>) — Raises the receiver, causing program flow to jump to the local exception handler.
