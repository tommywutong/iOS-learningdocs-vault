---
title: 'performAsCurrent(withPendingUnitCount:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/progress/performascurrent(withpendingunitcount:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/progress/performascurrent(withpendingunitcount:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/performascurrent%28withpendingunitcount%3Ausing%3A%29.json'
content_hash: 'sha256:dc9a36be807b547a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# performAsCurrent(withPendingUnitCount:using:)

<sub>Instance Method</sub>

Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func performAsCurrent<ReturnType>(withPendingUnitCount unitCount: Int64, using work: () throws -> ReturnType) rethrows -> ReturnType
```

## Parameters

- `unitCount` — The number of units of work to increment for the current progress object. This number represents the portion of work that is complete in relation to the total number of units of work for the current thread’s progress object. The units of work for this parameter must be the same units of work as the current progress object’s [totalUnitCount](totalunitcount.md) property.

- `work` — A block that wraps the work you specify to complete for incrementing the current progress.

## Return Value

The return type and value of the block that you specify for the `work` parameter.

## Discussion

Use this function as a convenience method to wrap an existing method or block to increment the current progress object. This function retrieves the current progress object, does the work you specify in the work block, and returns the value from that block. When the block is complete, this function increments the current progress object. This function is the same as calling [- becomeCurrentWithPendingUnitCount:](<becomecurrent(withpendingunitcount_).md>), doing the work you specify in the block, and calling [- resignCurrent](<resigncurrent().md>).

## See Also

### Accessing the Current Progress Object

- [+ currentProgress](<current().md>) — Returns the progress instance, if any.
- [- becomeCurrentWithPendingUnitCount:](<becomecurrent(withpendingunitcount_).md>) — Sets the progress object as the current object of the current thread, and assigns the amount of work for the next suboperation progress object to perform.
- [- resignCurrent](<resigncurrent().md>) — Restores the previous progress object to become the current progress object on the thread.
