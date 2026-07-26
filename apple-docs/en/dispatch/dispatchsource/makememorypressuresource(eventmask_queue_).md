---
title: 'makeMemoryPressureSource(eventMask:queue:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsource/makememorypressuresource(eventmask:queue:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/makememorypressuresource(eventmask:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/makememorypressuresource%28eventmask%3Aqueue%3A%29.json'
content_hash: 'sha256:009a974013858e55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSource](../dispatchsource.md)

# makeMemoryPressureSource(eventMask:queue:)

<sub>Type Method</sub>

Creates a new dispatch source object that monitors the system for changes in the memory pressure condition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func makeMemoryPressureSource(eventMask: DispatchSource.MemoryPressureEvent, queue: DispatchQueue? = nil) -> any DispatchSourceMemoryPressure
```

## Parameters

- `eventMask` — The set of events you want to monitor. For a list of possible values, see [MemoryPressureEvent](memorypressureevent.md).

- `queue` — The dispatch queue to use when executing the installed handlers.

## Return Value

A dispatch source object that conforms to the [DispatchSourceMemoryPressure](../dispatchsourcememorypressure.md) protocol.

## Discussion

After creating the dispatch source, use the methods of the [DispatchSourceProtocol](../dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [dispatch_activate](<../dispatchobject/activate().md>) method.

## See Also

### Creating a Memory Pressure Source

- [DispatchSourceMemoryPressure](../dispatchsourcememorypressure.md) — A dispatch source that monitors the system for changes in the memory pressure condition.
- [MemoryPressureEvent](memorypressureevent.md) — Memory pressure events.
