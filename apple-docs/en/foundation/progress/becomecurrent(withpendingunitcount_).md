---
title: 'becomeCurrent(withPendingUnitCount:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/progress/becomecurrent(withpendingunitcount:)'
source_url: 'https://developer.apple.com/documentation/foundation/progress/becomecurrent(withpendingunitcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/becomecurrent%28withpendingunitcount%3A%29.json'
content_hash: 'sha256:c9c71e3f70df1e3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# becomeCurrent(withPendingUnitCount:)

<sub>Instance Method</sub>

Sets the progress object as the current object of the current thread, and assigns the amount of work for the next suboperation progress object to perform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func becomeCurrent(withPendingUnitCount unitCount: Int64)
```

## Parameters

- `unitCount` — The number of units of work for the next progress object that initializes when you invoke [- initWithParent:userInfo:](<init(parent_userinfo_).md>) in the current thread with this progress object as the containing progress object. The number represents the portion of work to perform in relation to the total number of units of work, which is the value of the progress object’s [totalUnitCount](totalunitcount.md) property. The units of work for this parameter must be the same units of work in the progress object’s [totalUnitCount](totalunitcount.md) property.

## Discussion

Use this method to build a tree of progress objects, as [Reporting Progress for Multiple Operations](../progress.md#Reporting-Progress-for-Multiple-Operations) describes.

## See Also

### Accessing the Current Progress Object

- [+ currentProgress](<current().md>) — Returns the progress instance, if any.
- [performAsCurrent(withPendingUnitCount:using:)](<performascurrent(withpendingunitcount_using_).md>) — Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.
- [- resignCurrent](<resigncurrent().md>) — Restores the previous progress object to become the current progress object on the thread.
