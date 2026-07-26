---
title: 'discreteProgress(totalUnitCount:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/progress/discreteprogress(totalunitcount:)'
source_url: 'https://developer.apple.com/documentation/foundation/progress/discreteprogress(totalunitcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/discreteprogress%28totalunitcount%3A%29.json'
content_hash: 'sha256:d43815ae12e2dfed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# discreteProgress(totalUnitCount:)

<sub>Type Method</sub>

Creates and returns a progress instance with the specified unit count that isn’t part of any existing progress tree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func discreteProgress(totalUnitCount unitCount: Int64) -> Progress
```

## Parameters

- `unitCount` — The total number of units of work to assign to the progress instance.

## Return Value

A new progress instance with its containing progress object set to `nil.`

## Discussion

Use this method to create the top-level progress object that your custom classes return. The receiver of the returned progress object can add it to a progress tree using `Progress/addChild(_:withPendingUnitCount:)`.

You’re responsible for updating the progress count of the created progress object. You can invoke this method on one thread and then message the returned `NSProgress` on another thread. For example, you can capture the created progress instance in a block that you pass to [dispatch_async](../../dispatch/dispatch_async.md). In that block, you can invoke methods like [- becomeCurrentWithPendingUnitCount:](<becomecurrent(withpendingunitcount_).md>) or [- resignCurrent](<resigncurrent().md>), and set the [completedUnitCount](completedunitcount.md) or [cancelled](iscancelled.md) properties as your app finishes its work.

## See Also

### Creating Progress Objects

- [- initWithParent:userInfo:](<init(parent_userinfo_).md>) — Creates a new progress instance.
- [+ progressWithTotalUnitCount:](<init(totalunitcount_).md>) — Creates and returns a progress instance.
- [+ progressWithTotalUnitCount:parent:pendingUnitCount:](<init(totalunitcount_parent_pendingunitcount_).md>) — Creates a progress instance for the specified progress object with a unit count that’s a portion of the containing object’s total unit count.
