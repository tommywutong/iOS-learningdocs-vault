---
title: autoconnect()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/connectablepublisher/autoconnect()
source_url: 'https://developer.apple.com/documentation/combine/connectablepublisher/autoconnect()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/connectablepublisher/autoconnect%28%29.json'
content_hash: 'sha256:6d234f2b1db4925c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [ConnectablePublisher](../connectablepublisher.md)

# autoconnect()

<sub>Instance Method</sub>

Automates the process of connecting or disconnecting from this connectable publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func autoconnect() -> Publishers.Autoconnect<Self>
```

## Return Value

A publisher which automatically connects to its upstream connectable publisher.

## Discussion

Use [autoconnect()](<autoconnect().md>) to simplify working with [ConnectablePublisher](../connectablepublisher.md) instances, such as [Timer.TimerPublisher](../../foundation/timer/timerpublisher.md) in the Foundation framework.

In the following example, the [publish(every:tolerance:on:in:options:)](<../../foundation/timer/publish(every_tolerance_on_in_options_).md>) operator creates a [Timer.TimerPublisher](../../foundation/timer/timerpublisher.md), which is a [ConnectablePublisher](../connectablepublisher.md). As a result, subscribers don’t receive any values until after a call to [connect()](<connect().md>). For convenience when working with a single subscriber, the [autoconnect()](<autoconnect().md>) operator performs the [connect()](<connect().md>) call when attached to by the subscriber.

```swift
cancellable = Timer.publish(every: 1, on: .main, in: .default)
    .autoconnect()
    .sink { date in
        print ("Date now: \(date)")
    }
```
