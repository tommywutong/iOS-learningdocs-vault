---
title: threadPriority()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/threadpriority()
source_url: 'https://developer.apple.com/documentation/foundation/thread/threadpriority()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/threadpriority%28%29.json'
content_hash: 'sha256:01adeef0e8bf9d41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# threadPriority()

<sub>Type Method</sub>

Returns the current thread’s priority.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func threadPriority() -> Double
```

## Return Value

The current thread’s priority, which is specified by a floating point number from 0.0 to 1.0, where 1.0 is highest priority.

## Discussion

The priorities in this range are mapped to the operating system’s priority values. A “typical” thread priority might be 0.5, but because the priority is determined by the kernel, there is no guarantee what this value actually will be.

## See Also

### Prioritizing Thread Work

- [qualityOfService](qualityofservice.md)
- [QualityOfService](../qualityofservice.md) — Constants that indicate the nature and importance of work to the system.
- [threadPriority](threadpriority.md) — The receiver’s priority
- [+ setThreadPriority:](<setthreadpriority(__).md>) — Sets the current thread’s priority.
