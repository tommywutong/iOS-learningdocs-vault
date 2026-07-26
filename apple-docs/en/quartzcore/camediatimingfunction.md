---
title: CAMediaTimingFunction
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/camediatimingfunction
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatimingfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatimingfunction.json'
content_hash: 'sha256:58e71e09d9f08a6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAMediaTimingFunction

<sub>Class</sub>

A function that defines the pacing of an animation as a timing curve.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CAMediaTimingFunction
```

## Overview

`CAMediaTimingFunction` represents one segment of a function that defines the pacing of an animation as a timing curve. The function maps an input time normalized to the range `[0,1]` to an output time also in the range `[0,1]`.

You can create a media timing function by supplying your own cubic Bézier curve control points using the [- initWithControlPoints::::](<camediatimingfunction/init(controlpoints_______).md>) method or by using one of the predefined timing functions.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating Timing Functions

- [+ functionWithName:](<camediatimingfunction/init(name_).md>) — Creates and returns a new instance of `CAMediaTimingFunction` configured with the predefined timing function specified by `name`.
- [- initWithControlPoints::::](<camediatimingfunction/init(controlpoints_______).md>) — Returns an initialized timing function modeled as a cubic Bézier curve using the specified control points.

### Accessing the Control Points

- [- getControlPointAtIndex:values:](<camediatimingfunction/getcontrolpoint(at_values_).md>) — Returns the control point for the specified index.

### Constants

- [Predefined Timing Functions](predefined-timing-functions.md) — Constants that specify system-provided timing functions, used by [+ functionWithName:](<camediatimingfunction/init(name_).md>).

### Initializers

- [init(coder:)](<camediatimingfunction/init(coder_).md>)

## See Also

### Animation Timing

- [CACurrentMediaTime](<cacurrentmediatime().md>) — Returns the current absolute time, in seconds.
- [CAMediaTiming](camediatiming.md) — Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.
- [CADisplayLink](cadisplaylink.md) — A timer object that allows your app to synchronize its drawing to the refresh rate of the display.
- [CAMetalDisplayLink](cametaldisplaylink.md) — A class your Metal app uses to register for callbacks to synchronize its animations for a display.
- [Update](cametaldisplaylink/update.md) — Stores information about a single update from a Metal display link instance.
- [CAMetalDisplayLinkDelegate](cametaldisplaylinkdelegate.md) — A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.
