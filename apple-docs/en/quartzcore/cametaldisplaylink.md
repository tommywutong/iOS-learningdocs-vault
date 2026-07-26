---
title: CAMetalDisplayLink
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametaldisplaylink
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldisplaylink'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldisplaylink.json'
content_hash: 'sha256:6916dd63b4b54c7c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAMetalDisplayLink

<sub>Class</sub>

A class your Metal app uses to register for callbacks to synchronize its animations for a display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CAMetalDisplayLink
```

## Overview

[CAMetalDisplayLink](cametaldisplaylink.md) instances are a specialized way to interact with variable-rate displays when you need more control over the timing window to render your app’s frames. Controlling the timing window and rendering delay for frames can help you achieve smoother frame rates and avoid visual artifacts.

> [!tip] Tip
> When working with less visually intensive apps or apps which don’t use Metal, use [CADisplayLink](cadisplaylink.md) to handle variable refresh rates.

Your app initializes a new Metal display link by providing a target [CAMetalLayer](cametallayer.md). Set this instance’s [delegate](cametaldisplaylink/delegate.md) property to an implementation that encodes the rendering work for Metal to perform. With a set delegate, synchronize the display with a run loop to perform rendering on by calling the [- addToRunLoop:forMode:](<cametaldisplaylink/add(to_formode_).md>) method.

Once you associate the display link with a run loop, the system calls the delegate’s [- metalDisplayLink:needsUpdate:](<cametaldisplaylinkdelegate/metaldisplaylink(__needsupdate_).md>) method to request new frames. This method receives update requests based on the [preferredFrameRateRange](cametaldisplaylink/preferredframeraterange.md) and [preferredFrameLatency](cametaldisplaylink/preferredframelatency.md) of the display link. The system makes a best effort to make callbacks at appropriate times. Your app should complete any commits to the Metal device’s [MTLCommandQueue](../metal/mtlcommandqueue.md) for rendering the display layer before calling [present()](<../metal/mtldrawable/present().md>) on a drawable element.

Your app can disable notifications by setting [paused](cametaldisplaylink/ispaused.md) to `true`. When your app finishes with a display link, call [- invalidate](<cametaldisplaylink/invalidate().md>)to remove it from all run loops and the target.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Display Link

- [- initWithMetalLayer:](<cametaldisplaylink/init(metallayer_).md>) — Creates a display link for Metal from a Core Animation layer.

### Configuring a Display Link

- [preferredFrameRateRange](cametaldisplaylink/preferredframeraterange.md) — A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [preferredFrameLatency](cametaldisplaylink/preferredframelatency.md) — The amount of time, in frames, your app requests to render a frame.
- [delegate](cametaldisplaylink/delegate.md) — An instance of a type your app implements that responds to the system’s callbacks.

### Registering for Callbacks

- [- addToRunLoop:forMode:](<cametaldisplaylink/add(to_formode_).md>) — Registers the display link with a run loop.

### Pausing Callbacks

- [paused](cametaldisplaylink/ispaused.md) — A Boolean value that indicates whether the system suspends the display link’s notifications to the target.

### Deregistering for callbacks

- [- removeFromRunLoop:forMode:](<cametaldisplaylink/remove(from_formode_).md>) — Removes a mode’s display link from a run loop.
- [- invalidate](<cametaldisplaylink/invalidate().md>) — Removes the display link from all run loops for all modes.

### Classes

- [Update](cametaldisplaylink/update.md) — Stores information about a single update from a Metal display link instance.

## See Also

### Animation Timing

- [CACurrentMediaTime](<cacurrentmediatime().md>) — Returns the current absolute time, in seconds.
- [CAMediaTimingFunction](camediatimingfunction.md) — A function that defines the pacing of an animation as a timing curve.
- [CAMediaTiming](camediatiming.md) — Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.
- [CADisplayLink](cadisplaylink.md) — A timer object that allows your app to synchronize its drawing to the refresh rate of the display.
- [Update](cametaldisplaylink/update.md) — Stores information about a single update from a Metal display link instance.
- [CAMetalDisplayLinkDelegate](cametaldisplaylinkdelegate.md) — A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.
