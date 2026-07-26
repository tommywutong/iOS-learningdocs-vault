---
title: enter()
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchgroup/enter()
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchgroup/enter()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchgroup/enter%28%29.json'
content_hash: 'sha256:a637732dd13c4a97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchGroup](../dispatchgroup.md)

# enter()

<sub>Instance Method</sub>

Explicitly indicates that a block has entered the group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enter()
```

## Discussion

Calling this function in Objective-C increments the current count of outstanding tasks in the group. Using this function (with [dispatch_group_leave](<leave().md>)) allows your application to properly manage the task reference count if it explicitly adds and removes tasks from the group by a means other than using the [dispatch_group_async](../dispatch_group_async.md) function. A call to this function must be balanced with a call to [dispatch_group_leave](<leave().md>). You can use this function to associate a block with more than one group at the same time.

## See Also

### Updating the Group Manually

- [dispatch_group_leave](<leave().md>) — Explicitly indicates that a block in the group finished executing.
