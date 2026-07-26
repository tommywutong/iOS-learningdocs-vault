---
title: 'init(location:end:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextrange/init(location:end:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextrange/init(location:end:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextrange/init%28location%3Aend%3A%29.json'
content_hash: 'sha256:2b2fa1244bfd2924'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextRange](../nstextrange.md)

# init(location:end:)

<sub>Initializer</sub>

Creates a new text range with the starting and ending locations you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init?(location: any NSTextLocation, end endLocation: (any NSTextLocation)?)
```

## Parameters

- `location` — The starting location.

- `endLocation` — The ending location, or `nil` for an empty range.

## Discussion

Returns an empty range when `endLocation` is `nil`.

## See Also

### Creating a text range

- [- initWithLocation:](<init(location_).md>) — Creates a new text range at the location you specify.
