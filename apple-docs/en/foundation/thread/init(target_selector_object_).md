---
title: 'init(target:selector:object:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/thread/init(target:selector:object:)'
source_url: 'https://developer.apple.com/documentation/foundation/thread/init(target:selector:object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/init%28target%3Aselector%3Aobject%3A%29.json'
content_hash: 'sha256:b9b2930e3dbc6a24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# init(target:selector:object:)

<sub>Initializer</sub>

Returns an `NSThread` object initialized with the given arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(target: Any, selector: Selector, object argument: Any?)
```

## Parameters

- `target` — The object to which the message specified by `selector` is sent.

- `selector` — The selector for the message to send to `target`. This selector must take only one argument and must not have a return value.

- `argument` — The single argument passed to the target. May be `nil`.

## Return Value

An `NSThread` object initialized with the given arguments.

## Discussion

The objects `target` and `argument` are retained during the execution of the detached thread. They are released when the thread finally exits.

## See Also

### Related Documentation

- [- start](<start().md>) — Starts the receiver.

### Initializing an NSThread Object

- [- init](<init().md>) — Returns an initialized `NSThread` object.
