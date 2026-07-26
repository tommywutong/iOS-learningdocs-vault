---
title: resume()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/checkedcontinuation/resume()
source_url: 'https://developer.apple.com/documentation/swift/checkedcontinuation/resume()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/checkedcontinuation/resume%28%29.json'
content_hash: 'sha256:63e45276a67aadf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CheckedContinuation](../checkedcontinuation.md)

# resume()

<sub>Instance Method</sub>

Resume the task awaiting the continuation by having it return normally from its suspension point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resume() where T == ()
```

## Discussion

A continuation must be resumed exactly once. If the continuation has already been resumed through this object, then the attempt to resume the continuation will trap.

After `resume` enqueues the task, control immediately returns to the caller. The task continues executing when its executor is able to reschedule it.
