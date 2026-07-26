---
title: 'property(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/stream/property(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/stream/property(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/property%28forkey%3A%29.json'
content_hash: 'sha256:c53adac3a54f65ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# property(forKey:)

<sub>Instance Method</sub>

Returns the receiver’s property for a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func property(forKey key: Stream.PropertyKey) -> Any?
```

## Parameters

- `key` — The key for one of the receiver’s properties. See Constants for a description of the available property-key constants and associated values.

## Return Value

The receiver’s property for the key `key`.

## See Also

### Configuring Streams

- [- setProperty:forKey:](<setproperty(__forkey_).md>) — Attempts to set the value of a given property of the receiver and returns a Boolean value that indicates whether the value is accepted by the receiver.
- [delegate](delegate.md) — Sets the receiver’s delegate.
