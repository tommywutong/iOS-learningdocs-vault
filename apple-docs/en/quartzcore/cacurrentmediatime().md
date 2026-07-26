---
title: CACurrentMediaTime()
framework: Core Animation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cacurrentmediatime()
source_url: 'https://developer.apple.com/documentation/quartzcore/cacurrentmediatime()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cacurrentmediatime%28%29.json'
content_hash: 'sha256:036ecf560e3dde49'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CACurrentMediaTime()

<sub>Function</sub>

Returns the current absolute time, in seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func CACurrentMediaTime() -> CFTimeInterval
```

## Return Value

A `CFTimeInterval` derived by calling `mach_absolute_time()` and converting the result to seconds.

## See Also

### Animation Timing

- [CAMediaTimingFunction](camediatimingfunction.md) — A function that defines the pacing of an animation as a timing curve.
- [CAMediaTiming](camediatiming.md) — Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.
- [CADisplayLink](cadisplaylink.md) — A timer object that allows your app to synchronize its drawing to the refresh rate of the display.
- [CAMetalDisplayLink](cametaldisplaylink.md) — A class your Metal app uses to register for callbacks to synchronize its animations for a display.
- [Update](cametaldisplaylink/update.md) — Stores information about a single update from a Metal display link instance.
- [CAMetalDisplayLinkDelegate](cametaldisplaylinkdelegate.md) — A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.
