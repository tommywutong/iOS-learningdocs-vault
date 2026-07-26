---
title: 'init(_:affinity:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselection/init(_:affinity:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselection/init(_:affinity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselection/init%28_%3Aaffinity%3A%29.json'
content_hash: 'sha256:7e6986038196be4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelection](../nstextselection.md)

# init(_:affinity:)

<sub>Initializer</sub>

Creates a new text selection with the location and selection affinity you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(_ location: any NSTextLocation, affinity: NSTextSelection.Affinity)
```

## Parameters

- `location` — The text location

- `affinity` — One of the possible [Affinity](affinity-swift.enum.md) options.

## See Also

### Creating a text selection

- [- initWithRange:affinity:granularity:](<init(range_affinity_granularity_).md>) — Creates a new text selection with the range, selection affinity, and granularity you provide.
- [- initWithRanges:affinity:granularity:](<init(__affinity_granularity_).md>) — Creates a new text selection with the ranges, selection affinity, and granularity you provide.
- [- initWithCoder:](<init(coder_).md>) — Creates a test selection from data in an unarchiver.
