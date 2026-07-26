---
title: CAMetalDisplayLink.Update
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametaldisplaylink/update
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/update'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldisplaylink/update.json'
content_hash: 'sha256:01b193ef5167184a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalDisplayLink](../cametaldisplaylink.md)

# CAMetalDisplayLink.Update

<sub>Class</sub>

Stores information about a single update from a Metal display link instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class Update
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Timing the Next Animation Frame

- [targetPresentationTimestamp](update/targetpresentationtimestamp.md) — The time the system estimates until the display of the next frame.

### Drawing the Next Frame

- [targetTimestamp](update/targettimestamp.md) — A deadline that indicates when your app needs to finish rendering to the drawable.
- [drawable](update/drawable.md) — The Metal drawable your app uses to render the next frame.

## See Also

### Animation Timing

- [CACurrentMediaTime](<../cacurrentmediatime().md>) — Returns the current absolute time, in seconds.
- [CAMediaTimingFunction](../camediatimingfunction.md) — A function that defines the pacing of an animation as a timing curve.
- [CAMediaTiming](../camediatiming.md) — Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.
- [CADisplayLink](../cadisplaylink.md) — A timer object that allows your app to synchronize its drawing to the refresh rate of the display.
- [CAMetalDisplayLink](../cametaldisplaylink.md) — A class your Metal app uses to register for callbacks to synchronize its animations for a display.
- [CAMetalDisplayLinkDelegate](../cametaldisplaylinkdelegate.md) — A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.
