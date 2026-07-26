---
title: label
framework: Distributed
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/remotecallargument/label
source_url: 'https://developer.apple.com/documentation/distributed/remotecallargument/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/remotecallargument/label.json'
content_hash: 'sha256:41bd535e3bc31513'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [RemoteCallArgument](../remotecallargument.md)

# label

<sub>Instance Property</sub>

The “argument label” of the argument. The label is the name visible name used in external calls made to this target, e.g. for `func hello(label name: String)` it is `label`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let label: String?
```

## Discussion

If no label is specified (i.e. `func hi(name: String)`), the `label`, value is empty, however `effectiveLabel` is equal to the `name`.

In most situations, using `effectiveLabel` is more useful to identify the user-visible name of this argument.
