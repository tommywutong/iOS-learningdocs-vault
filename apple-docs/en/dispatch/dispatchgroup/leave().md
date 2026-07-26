---
title: leave()
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchgroup/leave()
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchgroup/leave()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchgroup/leave%28%29.json'
content_hash: 'sha256:f9ad1fbd761d38eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchGroup](../dispatchgroup.md)

# leave()

<sub>Instance Method</sub>

Explicitly indicates that a block in the group finished executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func leave()
```

## Discussion

Calling this function decrements the current count of outstanding tasks in the group. Using this function (with [dispatch_group_enter](<enter().md>)) allows your application to properly manage the task reference count if it explicitly adds and removes tasks from the group by a means other than using the [dispatch_group_async](../dispatch_group_async.md) function.

A call to this function must balance a call to [dispatch_group_enter](<enter().md>). It is invalid to call it more times than [dispatch_group_enter](<enter().md>), which would result in a negative count.

## See Also

### Updating the Group Manually

- [dispatch_group_enter](<enter().md>) — Explicitly indicates that a block has entered the group.
