---
title: 'makeUserDataReplaceSource(queue:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsource/makeuserdatareplacesource(queue:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/makeuserdatareplacesource(queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/makeuserdatareplacesource%28queue%3A%29.json'
content_hash: 'sha256:9f4c333e03fca2cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSource](../dispatchsource.md)

# makeUserDataReplaceSource(queue:)

<sub>Type Method</sub>

Creates a new dispatch source object that you use to track custom app data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func makeUserDataReplaceSource(queue: DispatchQueue? = nil) -> any DispatchSourceUserDataReplace
```

## Parameters

- `queue` — The dispatch queue to use when executing the installed handlers.

## Return Value

A dispatch source object that conforms to the [DispatchSourceUserDataReplace](../dispatchsourceuserdatareplace.md) protocol.

## Discussion

After creating the dispatch source, use the methods of the [DispatchSourceProtocol](../dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [dispatch_activate](<../dispatchobject/activate().md>) method.

## See Also

### Creating a Custom Source

- [makeUserDataAddSource(queue:)](<makeuserdataaddsource(queue_).md>) — Creates a new dispatch source object that you use to coalesce custom app data using an AND operator.
- [makeUserDataOrSource(queue:)](<makeuserdataorsource(queue_).md>) — Creates a new dispatch source object that you use to coalesce custom app data using an OR operator.
- [DispatchSourceUserDataAdd](../dispatchsourceuserdataadd.md) — A dispatch source that coalesces data you provide using an AND operation.
- [DispatchSourceUserDataOr](../dispatchsourceuserdataor.md) — A dispatch source that coalesces data you provide using an OR operation.
- [DispatchSourceUserDataReplace](../dispatchsourceuserdatareplace.md) — A dispatch source that replaces any pending data with the new value you provide.
