---
title: CAMediaTiming
framework: Core Animation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/camediatiming
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatiming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatiming.json'
content_hash: 'sha256:541a6893476f3415'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAMediaTiming

<sub>Protocol</sub>

Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CAMediaTiming
```

## Overview

Absolute time is defined as mach time converted to seconds. The [CACurrentMediaTime](<cacurrentmediatime().md>) function is provided as a convenience for getting the current absolute time.

The conversion from parent time to local time has two stages:

1. Conversion to “active local time.” This includes the point at which the object appears in the parent object’s timeline and how fast it plays relative to the parent.
2. Conversion from “active local time” to “basic local time.” The timing model allows for objects to repeat their basic duration multiple times and, optionally, to play backwards before repeating.

## Relationships

- **Conforming Types**: [CAAnimation](caanimation.md), [CAAnimationGroup](caanimationgroup.md), [CABasicAnimation](cabasicanimation.md), [CAEAGLLayer](caeagllayer.md), [CAEmitterCell](caemittercell.md), [CAEmitterLayer](caemitterlayer.md), [CAGradientLayer](cagradientlayer.md), [CAKeyframeAnimation](cakeyframeanimation.md), [CALayer](calayer.md), [CAMetalLayer](cametallayer.md), [CAOpenGLLayer](caopengllayer.md), [CAPropertyAnimation](capropertyanimation.md), [CAReplicatorLayer](careplicatorlayer.md), [CAScrollLayer](cascrolllayer.md), [CAShapeLayer](cashapelayer.md), [CASpringAnimation](caspringanimation.md), [CATextLayer](catextlayer.md), [CATiledLayer](catiledlayer.md), [CATransformLayer](catransformlayer.md), [CATransition](catransition.md)

## Topics

### Animation Start Time

- [beginTime](camediatiming/begintime.md) — Specifies the begin time of the receiver in relation to its parent object, if applicable.
- [timeOffset](camediatiming/timeoffset.md) — Specifies an additional time offset in active local time.

### Repeating Animations

- [repeatCount](camediatiming/repeatcount.md) — Determines the number of times the animation will repeat.
- [repeatDuration](camediatiming/repeatduration.md) — Determines how many seconds the animation will repeat for.

### Duration and Speed

- [duration](camediatiming/duration.md) — Specifies the basic duration of the animation, in seconds.
- [speed](camediatiming/speed.md) — Specifies how time is mapped to receiver’s time space from the parent time space.

### Playback Modes

- [autoreverses](camediatiming/autoreverses.md) — Determines if the receiver plays in the reverse upon completion.
- [fillMode](camediatiming/fillmode.md) — Determines if the receiver’s presentation is frozen or removed once its active duration has completed.

### Constants

- [Fill Modes](fill-modes.md) — These constants determine how the timed object behaves once its active duration has completed. They are used with the [fillMode](camediatiming/fillmode.md) property.

## See Also

### Animation Timing

- [CACurrentMediaTime](<cacurrentmediatime().md>) — Returns the current absolute time, in seconds.
- [CAMediaTimingFunction](camediatimingfunction.md) — A function that defines the pacing of an animation as a timing curve.
- [CADisplayLink](cadisplaylink.md) — A timer object that allows your app to synchronize its drawing to the refresh rate of the display.
- [CAMetalDisplayLink](cametaldisplaylink.md) — A class your Metal app uses to register for callbacks to synchronize its animations for a display.
- [Update](cametaldisplaylink/update.md) — Stores information about a single update from a Metal display link instance.
- [CAMetalDisplayLinkDelegate](cametaldisplaylinkdelegate.md) — A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.
