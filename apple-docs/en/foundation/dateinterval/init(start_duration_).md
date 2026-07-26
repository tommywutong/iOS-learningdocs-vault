---
title: 'init(start:duration:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dateinterval/init(start:duration:)'
source_url: 'https://developer.apple.com/documentation/foundation/dateinterval/init(start:duration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateinterval/init%28start%3Aduration%3A%29.json'
content_hash: 'sha256:43ba3b2651403016'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateInterval](../dateinterval.md)

# init(start:duration:)

<sub>Initializer</sub>

Initializes an interval with the specified start date and duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(start: Date, duration: TimeInterval)
```

## Discussion

Precondition: `duration >= 0`

## See Also

### Creating a Date Interval

- [init()](<init().md>) — Initializes an interval with start and end dates set to the current date and the duration set to `0`.
- [init(start:end:)](<init(start_end_).md>) — Initializes an interval with the specified start and end date.
