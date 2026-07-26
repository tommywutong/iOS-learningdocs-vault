---
title: 'makeTimerSource(flags:queue:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsource/maketimersource(flags:queue:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/maketimersource(flags:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/maketimersource%28flags%3Aqueue%3A%29.json'
content_hash: 'sha256:633e2fc89940a3ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSource](../dispatchsource.md)

# makeTimerSource(flags:queue:)

<sub>Type Method</sub>

Creates a new dispatch source object for monitoring timer events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func makeTimerSource(flags: DispatchSource.TimerFlags = [], queue: DispatchQueue? = nil) -> any DispatchSourceTimer
```

## Parameters

- `flags` — Additional flags indicating the behavior of the timer. For a list of possible values, see [TimerFlags](timerflags.md).

- `queue` — The dispatch queue to which to execute the installed handlers.

## Return Value

A dispatch source object that conforms to the [DispatchSourceTimer](../dispatchsourcetimer.md) protocol.

## Discussion

After creating the dispatch source, use the methods of the [DispatchSourceProtocol](../dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [dispatch_activate](<../dispatchobject/activate().md>) method.

To schedule timers, use the methods of the [DispatchSourceTimer](../dispatchsourcetimer.md) protocol. You may schedule timers that fire once or fire multiple times. Each time the timer fires, the dispatch source calls your installed event handler.

## See Also

### Creating a Timer Source

- [DispatchSourceTimer](../dispatchsourcetimer.md) — A dispatch source that submits the event handler block based on a timer.
- [TimerFlags](timerflags.md) — Flags to use when configuring a timer dispatch source.
