---
title: 'makeSignalSource(signal:queue:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsource/makesignalsource(signal:queue:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/makesignalsource(signal:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/makesignalsource%28signal%3Aqueue%3A%29.json'
content_hash: 'sha256:acbe51e8d5b589a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSource](../dispatchsource.md)

# makeSignalSource(signal:queue:)

<sub>Type Method</sub>

Creates a new dispatch source object that monitors the arrival of a UNIX signal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func makeSignalSource(signal: Int32, queue: DispatchQueue? = nil) -> any DispatchSourceSignal
```

## Parameters

- `signal` — The Unix signal number to monitor.

- `queue` — The dispatch queue to use when executing the installed handlers.

## Return Value

A dispatch source object that conforms to the [DispatchSourceSignal](../dispatchsourcesignal.md) protocol.

## Discussion

After creating the dispatch source, use the methods of the [DispatchSourceProtocol](../dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [dispatch_activate](<../dispatchobject/activate().md>) method.

## See Also

### Creating a Signal Source

- [DispatchSourceSignal](../dispatchsourcesignal.md) — A dispatch source that monitors the current process for UNIX signals.
