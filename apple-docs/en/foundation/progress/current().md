---
title: current()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/current()
source_url: 'https://developer.apple.com/documentation/foundation/progress/current()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/current%28%29.json'
content_hash: 'sha256:b1a9f37b86f20946'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# current()

<sub>Type Method</sub>

Returns the progress instance, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func current() -> Progress?
```

## Return Value

The progress instance for the current thread, if any.

## Discussion

If you invoke [- becomeCurrentWithPendingUnitCount:](<becomecurrent(withpendingunitcount_).md>) on the current thread, this method returns the progress instance.

Use this per-thread [+ currentProgress](<current().md>) value to allow code that performs work to report useful progress even when it’s widely separated from the code that actually presents progress information to the user, and without requiring layers of intervening code to pass around an [Progress](../progress.md) instance.

To ensure that you report progress in known units of work, you typically work with a suboperation progress object that you create by calling [+ discreteProgressWithTotalUnitCount:](<discreteprogress(totalunitcount_).md>).

## See Also

### Accessing the Current Progress Object

- [- becomeCurrentWithPendingUnitCount:](<becomecurrent(withpendingunitcount_).md>) — Sets the progress object as the current object of the current thread, and assigns the amount of work for the next suboperation progress object to perform.
- [performAsCurrent(withPendingUnitCount:using:)](<performascurrent(withpendingunitcount_using_).md>) — Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.
- [- resignCurrent](<resigncurrent().md>) — Restores the previous progress object to become the current progress object on the thread.
