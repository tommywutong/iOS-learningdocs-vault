---
title: PhysicalMetric
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/physicalmetric
source_url: 'https://developer.apple.com/documentation/swiftui/physicalmetric'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/physicalmetric.json'
content_hash: 'sha256:5196b02f87b5a83d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PhysicalMetric

<sub>Structure</sub>

Provides access to a value in points that corresponds to the specified physical measurement.

<sub>visionOS</sub>

```swift
@propertyWrapper @frozen struct PhysicalMetric<Value>
```

## Overview

Use this property wrapper inside a [View](view.md) or a type that inherits a `View`’s environment, like a [ViewModifier](viewmodifier.md). Its value will be the equivalent in points of the physical measurement of length you specify.

For example, to have a variable that contains the amount of points corresponding to one meter, you can do the following:

```swift
struct MyView: View {
    @PhysicalMetric(from: .meters)
    var twoAndAHalfMeters = 2.5
    …
}
```

Using this wrapper for a property of a type not associated with a scene’s view contents, like an  [App](app.md) or a [Scene](scene.md), is unsupported.

## Compensating for World Scaling

Starting with apps built against the visionOS 2.0 SDK, the default behavior of `PhysicalMetric` is to produce values that match the distances used by `RealityView`s in the same scene, by scaling its returned values to match the world scaling of the current scene. Previously, the values were not scaled, and they were suitable for measuring distances and lengths within the user’s surroundings, outside of any scene. Unscaled values could produce unexpected behavior if used in conjunction with `RealityView`s within the scene.

To modify the behavior of `PhysicalMetric` and obtain unscaled values, use the [transformEnvironment(_:transform:)](<view/transformenvironment(__transform_).md>) modifier, transforming the [physicalMetrics](environmentvalues/physicalmetrics.md) key path, to edit the converter used by `PhysicalMetric` within the modified views to use a new [WorldScalingCompensation](worldscalingcompensation.md) mode. For example:

```swift
struct RulerView: View {
    @PhysicalMetric(from: .meters)
    var oneMeter = 1

    var body: some View {
        /* implement a size-accurate ruler */
    }
}

struct ContentView: View {
    var body: some View {
        RulerView()
            .transformEnvironment(\.physicalMetrics) { metrics in
                metrics = metrics.worldScalingCompensation(.unscaled)
            }
    }
}
```

> [!info] See Also
> [PhysicalMetricsConverter](physicalmetricsconverter.md)

> [!info] See Also
> [WorldScalingCompensation](worldscalingcompensation.md)

## Relationships

- **Conforms To**: [DynamicProperty](dynamicproperty.md)

## Topics

### Creating a metric

- [init(wrappedValue:from:)](<physicalmetric/init(wrappedvalue_from_).md>) — Creates a value that maps the specified point, whose dimensions are specified in physical length measurements in the given unit, to the corresponding value in points in the associated scene.

### Getting the value

- [wrappedValue](physicalmetric/wrappedvalue.md) — A value in points in the coordinate system of the associated scene.

## See Also

### Measuring a view

- [GeometryReader](geometryreader.md) — A container view that defines its content as a function of its own size and coordinate space.
- [GeometryReader3D](geometryreader3d.md) — A container view that defines its content as a function of its own size and coordinate space.
- [GeometryProxy](geometryproxy.md) — A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [GeometryProxy3D](geometryproxy3d.md) — A proxy for access to the size and coordinate space of the container view.
- [coordinateSpace(_:)](<view/coordinatespace(__).md>) — Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [CoordinateSpace](coordinatespace.md) — A resolved coordinate space created by the coordinate space protocol.
- [CoordinateSpaceProtocol](coordinatespaceprotocol.md) — A frame of reference within the layout system.
- [PhysicalMetricsConverter](physicalmetricsconverter.md) — A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.
