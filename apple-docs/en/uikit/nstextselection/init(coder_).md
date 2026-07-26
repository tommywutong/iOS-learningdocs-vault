---
title: 'init(coder:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselection/init(coder:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselection/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselection/init%28coder%3A%29.json'
content_hash: 'sha256:431e602ce28475cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelection](../nstextselection.md)

# init(coder:)

<sub>Initializer</sub>

Creates a test selection from data in an unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?(coder: NSCoder)
```

## Parameters

- `coder` — A coder that subclasses [NSCoder](../../foundation/nscoder.md).

## See Also

### Creating a text selection

- [- initWithLocation:affinity:](<init(__affinity_).md>) — Creates a new text selection with the location and selection affinity you provide.
- [- initWithRange:affinity:granularity:](<init(range_affinity_granularity_).md>) — Creates a new text selection with the range, selection affinity, and granularity you provide.
- [- initWithRanges:affinity:granularity:](<init(__affinity_granularity_).md>) — Creates a new text selection with the ranges, selection affinity, and granularity you provide.
