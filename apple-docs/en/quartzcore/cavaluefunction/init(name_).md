---
title: 'init(name:)'
framework: Core Animation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/cavaluefunction/init(name:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/cavaluefunction/init(name:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cavaluefunction/init%28name%3A%29.json'
content_hash: 'sha256:36aa2558e4ff3785'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAValueFunction](../cavaluefunction.md)

# init(name:)

<sub>Initializer</sub>

Returns the value function object identified by the name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(name: CAValueFunctionName)
```

## Parameters

- `name` — The name of the value function.

## Return Value

A new `CAValueFunction` instance with the value function specified by the name.

## Discussion

The possible values for `name` are specified in [Rotate Value Functions](../rotate-value-functions.md), [Scale Value Functions](../scale-value-functions.md), and [Translate Functions](../translate-functions.md).
