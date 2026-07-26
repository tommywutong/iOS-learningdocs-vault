---
title: resignCurrent()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/resigncurrent()
source_url: 'https://developer.apple.com/documentation/foundation/progress/resigncurrent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/resigncurrent%28%29.json'
content_hash: 'sha256:055f260d046daeb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# resignCurrent()

<sub>Instance Method</sub>

Restores the previous progress object to become the current progress object on the thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resignCurrent()
```

## Discussion

This method restores the current progress object to what it was before invoking [- becomeCurrentWithPendingUnitCount:](<becomecurrent(withpendingunitcount_).md>).

Use this method after building your tree of progress objects, as [Reporting Progress for Multiple Operations](../progress.md#Reporting-Progress-for-Multiple-Operations) describes.

## See Also

### Accessing the Current Progress Object

- [+ currentProgress](<current().md>) — Returns the progress instance, if any.
- [- becomeCurrentWithPendingUnitCount:](<becomecurrent(withpendingunitcount_).md>) — Sets the progress object as the current object of the current thread, and assigns the amount of work for the next suboperation progress object to perform.
- [performAsCurrent(withPendingUnitCount:using:)](<performascurrent(withpendingunitcount_using_).md>) — Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.
