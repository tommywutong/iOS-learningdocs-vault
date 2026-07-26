---
title: value
framework: Distributed
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/remotecallargument/value
source_url: 'https://developer.apple.com/documentation/distributed/remotecallargument/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/remotecallargument/value.json'
content_hash: 'sha256:a0f09ebfc515a3eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [RemoteCallArgument](../remotecallargument.md)

# value

<sub>Instance Property</sub>

The value of the argument being passed to the call. As `RemoteCallArgument` is always used in conjunction with `recordArgument` and populated by the compiler, this Value will generally conform to a distributed actor system’s `SerializationRequirement`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let value: Value
```
