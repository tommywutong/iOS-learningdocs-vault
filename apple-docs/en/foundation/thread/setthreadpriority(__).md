---
title: 'setThreadPriority(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/thread/setthreadpriority(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/thread/setthreadpriority(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/setthreadpriority%28_%3A%29.json'
content_hash: 'sha256:3270f8b7be4b5ddb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# setThreadPriority(_:)

<sub>Type Method</sub>

Sets the current thread’s priority.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func setThreadPriority(_ p: Double) -> Bool
```

## Parameters

- `p` — The new priority, specified with a floating point number from 0.0 to 1.0, where 1.0 is highest priority.

## Return Value

[true](../../swift/true.md) if the priority assignment succeeded, [false](../../swift/false.md) otherwise.

## Discussion

The priorities in this range are mapped to the operating system’s priority values.

## See Also

### Prioritizing Thread Work

- [qualityOfService](qualityofservice.md)
- [QualityOfService](../qualityofservice.md) — Constants that indicate the nature and importance of work to the system.
- [+ threadPriority](<threadpriority().md>) — Returns the current thread’s priority.
- [threadPriority](threadpriority.md) — The receiver’s priority
