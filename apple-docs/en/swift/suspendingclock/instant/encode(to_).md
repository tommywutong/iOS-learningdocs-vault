---
title: 'encode(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/suspendingclock/instant/encode(to:)'
source_url: 'https://developer.apple.com/documentation/swift/suspendingclock/instant/encode(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/suspendingclock/instant/encode%28to%3A%29.json'
content_hash: 'sha256:d897375d5d402a80'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [SuspendingClock](../../suspendingclock.md) · [Instant](../instant.md)

# encode(to:)

<sub>Instance Method</sub>

Encodes this value into the given encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode(to encoder: any Encoder) throws
```

## Parameters

- `encoder` — The encoder to write data to.

## Discussion

If the value fails to encode anything, `encoder` will encode an empty keyed container in its place.

This function throws an error if any values are invalid for the given encoder’s format.
