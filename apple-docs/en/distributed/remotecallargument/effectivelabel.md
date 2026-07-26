---
title: effectiveLabel
framework: Distributed
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/distributed/remotecallargument/effectivelabel
source_url: 'https://developer.apple.com/documentation/distributed/remotecallargument/effectivelabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/distributed/remotecallargument/effectivelabel.json'
content_hash: 'sha256:e5cec1b831ee5794'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Distributed](../../distributed.md) · [RemoteCallArgument](../remotecallargument.md)

# effectiveLabel

<sub>Instance Property</sub>

The effective label of this argument. This reflects the semantics of call sites of function declarations without explicit label definitions in Swift.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var effectiveLabel: String { get }
```

## Discussion

For example, for a method declared like `func hi(a: String)` the effective label is `a` while for a method like `func hi(a b: String)` or `func hi(_ b: String)` the label is the explicitly declared one, so `a` and `_` respectively.
