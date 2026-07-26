---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nstimezone/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nstimezone/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimezone/isequal%28to%3A%29.json'
content_hash: 'sha256:6aee45917bb7a77c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTimeZone](../nstimezone.md)

# isEqual(to:)

<sub>Instance Method</sub>

Indicates whether the receiver has the same name and data as the specified time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to aTimeZone: TimeZone) -> Bool
```

## Parameters

- `aTimeZone` — The time zone to compare with the receiver.

## Return Value

[true](../../swift/true.md) if `aTimeZone` and the receiver have the same name and data, otherwise [false](../../swift/false.md).
