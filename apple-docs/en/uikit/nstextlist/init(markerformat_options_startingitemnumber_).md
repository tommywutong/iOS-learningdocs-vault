---
title: 'init(markerFormat:options:startingItemNumber:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlist/init(markerformat:options:startingitemnumber:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlist/init(markerformat:options:startingitemnumber:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlist/init%28markerformat%3Aoptions%3Astartingitemnumber%3A%29.json'
content_hash: 'sha256:b1bddc8e418ff089'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextList](../nstextlist.md)

# init(markerFormat:options:startingItemNumber:)

<sub>Initializer</sub>

Returns a new text list with the format, options, and starting item number you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(markerFormat: NSTextList.MarkerFormat, options: NSTextList.Options = [], startingItemNumber: Int)
```

## Parameters

- `markerFormat` — One of the possible [MarkerFormat](markerformat-swift.struct.md) formats.

- `options` — One or more of the possible [Options](options.md) options.

- `startingItemNumber` — An integer that represents the stating item number.

## See Also

### Creating a text list

- [- initWithCoder:](<init(coder_).md>) — Initializes and returns a newly allocated text list item.
- [- initWithMarkerFormat:options:](<init(markerformat_options_).md>) — Returns an initialized text list.
