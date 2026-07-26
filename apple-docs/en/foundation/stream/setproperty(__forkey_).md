---
title: 'setProperty(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/stream/setproperty(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/stream/setproperty(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/setproperty%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:54aacf7570fef549'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# setProperty(_:forKey:)

<sub>Instance Method</sub>

Attempts to set the value of a given property of the receiver and returns a Boolean value that indicates whether the value is accepted by the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setProperty(_ property: Any?, forKey key: Stream.PropertyKey) -> Bool
```

## Parameters

- `property` — The value for `key`.

- `key` — The key for one of the receiver’s properties. See Constants for a description of the available property-key constants and expected values.

## Return Value

[true](../../swift/true.md) if the value is accepted by the receiver, otherwise [false](../../swift/false.md).

## See Also

### Configuring Streams

- [- propertyForKey:](<property(forkey_).md>) — Returns the receiver’s property for a given key.
- [delegate](delegate.md) — Sets the receiver’s delegate.
