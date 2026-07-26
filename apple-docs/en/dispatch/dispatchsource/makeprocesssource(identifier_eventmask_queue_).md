---
title: 'makeProcessSource(identifier:eventMask:queue:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsource/makeprocesssource(identifier:eventmask:queue:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/makeprocesssource(identifier:eventmask:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/makeprocesssource%28identifier%3Aeventmask%3Aqueue%3A%29.json'
content_hash: 'sha256:632c5ebb9ff97f6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSource](../dispatchsource.md)

# makeProcessSource(identifier:eventMask:queue:)

<sub>Type Method</sub>

Creates a new dispatch source object for monitoring the specified process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func makeProcessSource(identifier: pid_t, eventMask: DispatchSource.ProcessEvent, queue: DispatchQueue? = nil) -> any DispatchSourceProcess
```

## Parameters

- `identifier` — The process identifier of the process you want to monitor.

- `eventMask` — The set of events you want to monitor. For a list of possible values, see [ProcessEvent](processevent.md).

- `queue` — The dispatch queue to use when executing the installed handlers.

## Return Value

A dispatch source object that conforms to the [DispatchSourceProcess](../dispatchsourceprocess.md) protocol.

## Discussion

After creating the dispatch source, use the methods of the [DispatchSourceProtocol](../dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [dispatch_activate](<../dispatchobject/activate().md>) method.

## See Also

### Creating a Process Source

- [DispatchSourceProcess](../dispatchsourceprocess.md) — A dispatch source that monitors an external process for events.
- [ProcessEvent](processevent.md) — Events related to a process.
