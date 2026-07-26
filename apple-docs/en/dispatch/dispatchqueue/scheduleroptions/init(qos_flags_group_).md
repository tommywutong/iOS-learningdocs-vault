---
title: 'init(qos:flags:group:)'
framework: Dispatch
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/scheduleroptions/init(qos:flags:group:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/scheduleroptions/init(qos:flags:group:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/scheduleroptions/init%28qos%3Aflags%3Agroup%3A%29.json'
content_hash: 'sha256:45b06a3e873ca7e0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchQueue](../../dispatchqueue.md) · [SchedulerOptions](../scheduleroptions.md)

# init(qos:flags:group:)

<sub>Initializer</sub>

Creates a dispatch queue scheduler options instance with the given options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], group: DispatchGroup? = nil)
```
