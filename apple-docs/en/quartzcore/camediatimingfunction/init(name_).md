---
title: 'init(name:)'
framework: Core Animation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/camediatimingfunction/init(name:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatimingfunction/init(name:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatimingfunction/init%28name%3A%29.json'
content_hash: 'sha256:1d24c5653ab3b1c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMediaTimingFunction](../camediatimingfunction.md)

# init(name:)

<sub>Initializer</sub>

Creates and returns a new instance of `CAMediaTimingFunction` configured with the predefined timing function specified by `name`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(name: CAMediaTimingFunctionName)
```

## Parameters

- `name` — The timing function to use as specified in [Predefined Timing Functions](../predefined-timing-functions.md).

## Return Value

A new instance of `CAMediaTimingFunction` with the timing function specified by `name`.

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)

### Creating Timing Functions

- [- initWithControlPoints::::](<init(controlpoints_______).md>) — Returns an initialized timing function modeled as a cubic Bézier curve using the specified control points.
