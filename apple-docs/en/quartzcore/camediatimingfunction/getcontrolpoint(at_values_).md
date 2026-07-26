---
title: 'getControlPoint(at:values:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/camediatimingfunction/getcontrolpoint(at:values:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatimingfunction/getcontrolpoint(at:values:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatimingfunction/getcontrolpoint%28at%3Avalues%3A%29.json'
content_hash: 'sha256:b574e5c5609f01ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMediaTimingFunction](../camediatimingfunction.md)

# getControlPoint(at:values:)

<sub>Instance Method</sub>

Returns the control point for the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func getControlPoint(at idx: Int, values ptr: UnsafeMutablePointer<Float>)
```

## Parameters

- `idx` — An integer specifying the index of the control point to return.

- `ptr` — A pointer to an array that, upon return, will contain the x and y values of the specified point.

## Discussion

The value of `index` must be between 0 and 3.
