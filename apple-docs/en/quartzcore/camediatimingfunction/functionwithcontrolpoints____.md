---
title: 'functionWithControlPoints::::'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/camediatimingfunction/functionwithcontrolpoints::::'
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatimingfunction/functionwithcontrolpoints::::'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatimingfunction/functionwithcontrolpoints%3A%3A%3A%3A.json'
content_hash: 'sha256:1349715c0c4ef21a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMediaTimingFunction](../camediatimingfunction.md)

# functionWithControlPoints::::

<sub>Type Method</sub>

Creates and returns a new instance of `CAMediaTimingFunction` timing function modeled as a cubic Bézier curve using the specified control points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) functionWithControlPoints:(float) c1x :(float) c1y :(float) c2x :(float) c2y;
```

## Parameters

- `c1x` — A floating point number representing the x position of the c1 control point.

- `c1y` — A floating point number representing the y position of the c1 control point.

- `c2x` — A floating point number representing the x position of the c2 control point.

- `c2y` — A floating point number representing the y position of the c2 control point.

## Return Value

A new instance of `CAMediaTimingFunction` with the timing function specified by the provided control points.

## Discussion

The end points of the Bézier curve are automatically set to (0.0,0.0) and (1.0,1.0). The control points defining the Bézier curve are: [(0.0,0.0), (`c1x`,`c1y`), (`c2x`,`c2y`), (1.0,1.0)].

## See Also

### Creating Timing Functions

- [+ functionWithName:](<init(name_).md>) — Creates and returns a new instance of `CAMediaTimingFunction` configured with the predefined timing function specified by `name`.
- [- initWithControlPoints::::](<init(controlpoints_______).md>) — Returns an initialized timing function modeled as a cubic Bézier curve using the specified control points.
