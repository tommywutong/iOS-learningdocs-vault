---
title: progress
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progressreporting/progress
source_url: 'https://developer.apple.com/documentation/foundation/progressreporting/progress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressreporting/progress.json'
content_hash: 'sha256:cd03fec5b5a2b424'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressReporting](../progressreporting.md)

# progress

<sub>Instance Property</sub>

The progress object returned by the class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var progress: Progress { get }
```

## Discussion

The progress object is usually setup at class initialization time and updated as work is completed. The [progress](progress.md) property is set only once. If another progress object is needed the caller should create a new instance of the custom class to represent the work.

### Special Considerations

The [progress](progress.md) property is only set once.
