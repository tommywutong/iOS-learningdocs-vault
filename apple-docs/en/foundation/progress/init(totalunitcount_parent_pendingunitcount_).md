---
title: 'init(totalUnitCount:parent:pendingUnitCount:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/progress/init(totalunitcount:parent:pendingunitcount:)'
source_url: 'https://developer.apple.com/documentation/foundation/progress/init(totalunitcount:parent:pendingunitcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/init%28totalunitcount%3Aparent%3Apendingunitcount%3A%29.json'
content_hash: 'sha256:94624f638c21b6bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# init(totalUnitCount:parent:pendingUnitCount:)

<sub>Initializer</sub>

Creates a progress instance for the specified progress object with a unit count that’s a portion of the containing object’s total unit count.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(totalUnitCount unitCount: Int64, parent: Progress, pendingUnitCount portionOfParentTotalUnitCount: Int64)
```

## Parameters

- `unitCount` — The total number of units of work to assign to the progress instance.

- `parent` — The containing progress object for the created [Progress](../progress.md) object.

- `portionOfParentTotalUnitCount` — The unit count for the progress object.

## Discussion

Use this method to initialize a progress object with a specified containing progress object and unit count.

In many cases, you can precede code that does a substantial amount of work with an invocation of this method, then repeatedly set the [completedUnitCount](completedunitcount.md) or [cancelled](iscancelled.md) property in the loop that does the work.

You can invoke this method on one thread and then message the returned [Progress](../progress.md) on another thread. For example, you can capture the created progress instance in a block that you pass to [dispatch_async](../../dispatch/dispatch_async.md). In that block, you can invoke methods like [- becomeCurrentWithPendingUnitCount:](<becomecurrent(withpendingunitcount_).md>) or [- resignCurrent](<resigncurrent().md>), and set the [completedUnitCount](completedunitcount.md) or [cancelled](iscancelled.md) properties as your app finishes its work.

## See Also

### Creating Progress Objects

- [- initWithParent:userInfo:](<init(parent_userinfo_).md>) — Creates a new progress instance.
- [+ discreteProgressWithTotalUnitCount:](<discreteprogress(totalunitcount_).md>) — Creates and returns a progress instance with the specified unit count that isn’t part of any existing progress tree.
- [+ progressWithTotalUnitCount:](<init(totalunitcount_).md>) — Creates and returns a progress instance.
