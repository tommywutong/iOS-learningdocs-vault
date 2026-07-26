---
title: CAMetalDisplayLinkDelegate
framework: Core Animation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametaldisplaylinkdelegate
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldisplaylinkdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldisplaylinkdelegate.json'
content_hash: 'sha256:6a2a108c38583608'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAMetalDisplayLinkDelegate

<sub>Protocol</sub>

A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CAMetalDisplayLinkDelegate
```

## Overview

Your app responds to the system on behalf of a [CAMetalDisplayLink](cametaldisplaylink.md) with this protocol. Implement a type that adopts the protocol and assign an instance of it to a display link’s [delegate](cametaldisplaylink/delegate.md) property.

## Topics

### Receiving Display Updates

- [- metalDisplayLink:needsUpdate:](<cametaldisplaylinkdelegate/metaldisplaylink(__needsupdate_).md>) — A method the system calls to notify your app when it plans to update the display.

## See Also

### Animation Timing

- [CACurrentMediaTime](<cacurrentmediatime().md>) — Returns the current absolute time, in seconds.
- [CAMediaTimingFunction](camediatimingfunction.md) — A function that defines the pacing of an animation as a timing curve.
- [CAMediaTiming](camediatiming.md) — Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.
- [CADisplayLink](cadisplaylink.md) — A timer object that allows your app to synchronize its drawing to the refresh rate of the display.
- [CAMetalDisplayLink](cametaldisplaylink.md) — A class your Metal app uses to register for callbacks to synchronize its animations for a display.
- [Update](cametaldisplaylink/update.md) — Stores information about a single update from a Metal display link instance.
