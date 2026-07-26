---
title: 'asyncAfterUnsafe(wallDeadline:qos:flags:execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/asyncafterunsafe(walldeadline:qos:flags:execute:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/asyncafterunsafe(walldeadline:qos:flags:execute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/asyncafterunsafe%28walldeadline%3Aqos%3Aflags%3Aexecute%3A%29.json'
content_hash: 'sha256:0176c779efe7d57b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# asyncAfterUnsafe(wallDeadline:qos:flags:execute:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func asyncAfterUnsafe(wallDeadline: DispatchWallTime, qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], execute work: @escaping () -> Void)
```
