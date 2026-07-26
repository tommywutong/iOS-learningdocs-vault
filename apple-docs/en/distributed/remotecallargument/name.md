---
title: name
framework: Distributed
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/remotecallargument/name
source_url: 'https://developer.apple.com/documentation/distributed/remotecallargument/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/remotecallargument/name.json'
content_hash: 'sha256:9986b0d6205aef5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [RemoteCallArgument](../remotecallargument.md)

# name

<sub>Instance Property</sub>

The internal name of parameter this argument is accessible as in the function body. It is not part of the functions API and may change without breaking the target identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let name: String
```

## Discussion

If the method did not declare an explicit `label`, it is used as the `effectiveLabel`.
