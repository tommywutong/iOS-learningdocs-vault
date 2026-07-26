---
title: 'init(info:domainDimension:domain:rangeDimension:range:callbacks:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgfunction/init(info:domaindimension:domain:rangedimension:range:callbacks:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfunction/init(info:domaindimension:domain:rangedimension:range:callbacks:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfunction/init%28info%3Adomaindimension%3Adomain%3Arangedimension%3Arange%3Acallbacks%3A%29.json'
content_hash: 'sha256:dcb0623578d0e434'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFunction](../cgfunction.md)

# init(info:domainDimension:domain:rangeDimension:range:callbacks:)

<sub>Initializer</sub>

Creates a Core Graphics function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(info: UnsafeMutableRawPointer?, domainDimension: Int, domain: UnsafePointer<CGFloat>?, rangeDimension: Int, range: UnsafePointer<CGFloat>?, callbacks: UnsafePointer<CGFunctionCallbacks>)
```

## Parameters

- `info` — A pointer to user-defined storage for data that you want to pass to your callbacks. You need to make sure that the data persists for as long as it’s needed, which can be beyond the scope in which the Core Graphics function is used.

- `domainDimension` — The number of inputs.

- `domain` — An array of (`2*domainDimension`) floats used to specify the valid intervals of input values. For each k from `0` to `(domainDimension - 1)`, `domain[2*k]` must be less than or equal to `domain[2*k+1]`, and the `k`th input value will be clipped to lie in the interval `domain[2*k] ≤ input[k] ≤ domain[2*k+1]`. If this parameter is `NULL`, then the input values are not clipped.

- `rangeDimension` — The number of outputs.

- `range` — An array of `(2*rangeDimension)` floats that specifies the valid intervals of output values. For each `k` from `0` to `(rangeDimension - 1)`, `range[2*k]` must be less than or equal to `range[2*k+1]`, and the `k`th output value will be clipped to lie in the interval `range[2*k] ≤ output[k] ≤ range[2*k+1]`. 	If this parameter is `NULL`, then the output values are not clipped.

- `callbacks` — A pointer to a callback function table. This table should contain pointers to the callbacks you provide to implement the semantics of this Core Graphics function.	 Core Graphics makes a copy of your table, so, for example, you could safely pass in a pointer to a structure on the stack.

## Return Value

The new Core Graphics function. In Objective-C, you’re responsible for releasing this object using [CGFunctionRelease](../cgfunctionrelease.md).
