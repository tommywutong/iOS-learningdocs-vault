---
title: 'init(range:affinity:granularity:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselection/init(range:affinity:granularity:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselection/init(range:affinity:granularity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselection/init%28range%3Aaffinity%3Agranularity%3A%29.json'
content_hash: 'sha256:0ed7a36d0eac3261'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelection](../nstextselection.md)

# init(range:affinity:granularity:)

<sub>Initializer</sub>

Creates a new text selection with the range, selection affinity, and granularity you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(range: NSTextRange, affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)
```

## Parameters

- `range` — The range of the selection.

- `affinity` — One of the available [Affinity](affinity-swift.enum.md) options.

- `granularity` — One of the available [Granularity](granularity-swift.enum.md) options.

## See Also

### Creating a text selection

- [- initWithLocation:affinity:](<init(__affinity_).md>) — Creates a new text selection with the location and selection affinity you provide.
- [- initWithRanges:affinity:granularity:](<init(__affinity_granularity_).md>) — Creates a new text selection with the ranges, selection affinity, and granularity you provide.
- [- initWithCoder:](<init(coder_).md>) — Creates a test selection from data in an unarchiver.
