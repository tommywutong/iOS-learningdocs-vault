---
title: 'addChild(_:withPendingUnitCount:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/progress/addchild(_:withpendingunitcount:)-9yrs3'
source_url: 'https://developer.apple.com/documentation/foundation/progress/addchild(_:withpendingunitcount:)-9yrs3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/addchild%28_%3Awithpendingunitcount%3A%29-9yrs3.json'
content_hash: 'sha256:fbb5fe575e8fe80f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# addChild(_:withPendingUnitCount:)

<sub>Instance Method</sub>

Adds a process object as a suboperation of a progress tree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addChild(_ child: Progress, withPendingUnitCount inUnitCount: Int64)
```

## Parameters

- `child` — The progress instance to add to the progress tree.

- `inUnitCount` — The number of units of work for the new suboperation to complete.

## Discussion

You assign the suboperation a portion of the receiver’s total unit count according to `inUnitCount`.
