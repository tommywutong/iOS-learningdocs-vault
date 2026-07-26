---
title: delegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream/delegate
source_url: 'https://developer.apple.com/documentation/foundation/stream/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/delegate.json'
content_hash: 'sha256:8edc91a17699bb6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# delegate

<sub>Instance Property</sub>

Sets the receiver’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
unowned(unsafe) var delegate: (any StreamDelegate)? { get set }
```

## Parameters

- `delegate` — The delegate for the receiver.

## Discussion

By default, a stream is its own delegate, and subclasses of `NSInputStream` and `NSOutputStream` must maintain this contract. If you override this method in a subclass, passing `nil` must restore the receiver as its own delegate. Delegates are not retained.

To learn about delegates and delegation, read “Delegation” in Cocoa Fundamentals Guide.

## See Also

### Configuring Streams

- [- propertyForKey:](<property(forkey_).md>) — Returns the receiver’s property for a given key.
- [- setProperty:forKey:](<setproperty(__forkey_).md>) — Attempts to set the value of a given property of the receiver and returns a Boolean value that indicates whether the value is accepted by the receiver.
