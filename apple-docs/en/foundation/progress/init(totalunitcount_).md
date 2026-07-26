---
title: 'init(totalUnitCount:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/progress/init(totalunitcount:)'
source_url: 'https://developer.apple.com/documentation/foundation/progress/init(totalunitcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/init%28totalunitcount%3A%29.json'
content_hash: 'sha256:3b1c0b86fe8f565e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# init(totalUnitCount:)

<sub>Initializer</sub>

Creates and returns a progress instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(totalUnitCount unitCount: Int64)
```

## Parameters

- `unitCount` — The total number of units of work to assign to the progress instance.

## Discussion

If a current progress object exists, the initializer uses it to set the value of the [totalUnitCount](totalunitcount.md) property.

In many cases, you can precede code that does a substantial amount of work with an invocation of this method, then repeatedly set the [completedUnitCount](completedunitcount.md) or [cancelled](iscancelled.md) property in the loop that does the work.

You can invoke this method on one thread and then message the returned [Progress](../progress.md) on another thread. For example, you can capture the created progress instance in a block that you pass to [dispatch_async](../../dispatch/dispatch_async.md). In that block, you can invoke methods like [- becomeCurrentWithPendingUnitCount:](<becomecurrent(withpendingunitcount_).md>) or [- resignCurrent](<resigncurrent().md>), and set the [completedUnitCount](completedunitcount.md) or [cancelled](iscancelled.md) properties as your app finishes its work.

## See Also

### Creating Progress Objects

- [- initWithParent:userInfo:](<init(parent_userinfo_).md>) — Creates a new progress instance.
- [+ discreteProgressWithTotalUnitCount:](<discreteprogress(totalunitcount_).md>) — Creates and returns a progress instance with the specified unit count that isn’t part of any existing progress tree.
- [+ progressWithTotalUnitCount:parent:pendingUnitCount:](<init(totalunitcount_parent_pendingunitcount_).md>) — Creates a progress instance for the specified progress object with a unit count that’s a portion of the containing object’s total unit count.
