---
title: 'init(parent:userInfo:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/progress/init(parent:userinfo:)'
source_url: 'https://developer.apple.com/documentation/foundation/progress/init(parent:userinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/init%28parent%3Auserinfo%3A%29.json'
content_hash: 'sha256:cea2aa91dc71bc18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# init(parent:userInfo:)

<sub>Initializer</sub>

Creates a new progress instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(parent parentProgressOrNil: Progress?, userInfo userInfoOrNil: [ProgressUserInfoKey : Any]? = nil)
```

## Parameters

- `parentProgressOrNil` — The containing [Progress](../progress.md) object, if any, to notify when reporting progress, or to consult when checking for cancellation. The only valid values are [+ currentProgress](<current().md>) or `nil`.

- `userInfoOrNil` — The optional user information dictionary for the progress object.

## Discussion

This is the designated initializer for the [Progress](../progress.md) class.

## See Also

### Creating Progress Objects

- [+ discreteProgressWithTotalUnitCount:](<discreteprogress(totalunitcount_).md>) — Creates and returns a progress instance with the specified unit count that isn’t part of any existing progress tree.
- [+ progressWithTotalUnitCount:](<init(totalunitcount_).md>) — Creates and returns a progress instance.
- [+ progressWithTotalUnitCount:parent:pendingUnitCount:](<init(totalunitcount_parent_pendingunitcount_).md>) — Creates a progress instance for the specified progress object with a unit count that’s a portion of the containing object’s total unit count.
