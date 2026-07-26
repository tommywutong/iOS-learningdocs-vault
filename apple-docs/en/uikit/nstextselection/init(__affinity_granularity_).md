---
title: 'init(_:affinity:granularity:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselection/init(_:affinity:granularity:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselection/init(_:affinity:granularity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselection/init%28_%3Aaffinity%3Agranularity%3A%29.json'
content_hash: 'sha256:960ae16fe7e5c4da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelection](../nstextselection.md)

# init(_:affinity:granularity:)

<sub>Initializer</sub>

Creates a new text selection with the ranges, selection affinity, and granularity you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(_ textRanges: [NSTextRange], affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)
```

## Parameters

- `textRanges` — An array of text ranges.

- `affinity` — One of the available [Affinity](affinity-swift.enum.md) options.

- `granularity` — One of the available [Granularity](granularity-swift.enum.md) options.

## See Also

### Creating a text selection

- [- initWithLocation:affinity:](<init(__affinity_).md>) — Creates a new text selection with the location and selection affinity you provide.
- [- initWithRange:affinity:granularity:](<init(range_affinity_granularity_).md>) — Creates a new text selection with the range, selection affinity, and granularity you provide.
- [- initWithCoder:](<init(coder_).md>) — Creates a test selection from data in an unarchiver.
