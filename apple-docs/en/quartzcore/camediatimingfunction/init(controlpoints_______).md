---
title: 'init(controlPoints:_:_:_:)'
framework: Core Animation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/camediatimingfunction/init(controlpoints:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatimingfunction/init(controlpoints:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatimingfunction/init%28controlpoints%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ecdcf4272ded24c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMediaTimingFunction](../camediatimingfunction.md)

# init(controlPoints:_:_:_:)

<sub>Initializer</sub>

Returns an initialized timing function modeled as a cubic Bézier curve using the specified control points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float)
```

## Parameters

- `c1x` — A floating point number representing the x position of the c1 control point.

- `c1y` — A floating point number representing the y position of the c1 control point.

- `c2x` — A floating point number representing the x position of the c2 control point.

- `c2y` — A floating point number representing the y position of the c2 control point.

## Return Value

An instance of `CAMediaTimingFunction` with the timing function specified by the provided control points.

## Discussion

The end points of the Bézier curve are automatically set to (0.0,0.0) and (1.0,1.0). The control points defining the Bézier curve are: [(0.0,0.0), (`c1x`,`c1y`), (`c2x`,`c2y`), (1.0,1.0)].

## See Also

### Creating Timing Functions

- [+ functionWithName:](<init(name_).md>) — Creates and returns a new instance of `CAMediaTimingFunction` configured with the predefined timing function specified by `name`.
