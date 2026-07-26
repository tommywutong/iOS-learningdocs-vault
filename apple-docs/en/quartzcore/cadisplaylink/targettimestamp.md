---
title: targetTimestamp
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 14.0+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cadisplaylink/targettimestamp
source_url: 'https://developer.apple.com/documentation/quartzcore/cadisplaylink/targettimestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cadisplaylink/targettimestamp.json'
content_hash: 'sha256:11318b1636f86919'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CADisplayLink](../cadisplaylink.md)

# targetTimestamp

<sub>Instance Property</sub>

The time interval that represents when the next frame displays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var targetTimestamp: CFTimeInterval { get }
```

## Discussion

You can use the target timestamp to cancel or pause long running processes that may overrun the available time between frames in order to maintain a consistent frame rate.

The following code shows how you can create a display link and register it with a run loop. The `step(``displayLink:)` function attempts to sum the square roots of all numbers up to [max](../../swift/int/max.md), but with each iteration checks the current time ([CACurrentMediaTime](<../cacurrentmediatime().md>)) against the [targetTimestamp](targettimestamp.md). If the time taken to complete the calculation is later than the target timestamp, the function breaks the loop:

```swift
func createDisplayLink() {
    let displayLink = CADisplayLink(target: self,
                                    selector: #selector(step))
    displayLink.add(to: .main,
                    forMode: .defaultRunLoopMode)
}
    
func step(displayLink: CADisplayLink) {
    var sqrtSum = 0.0
    for i in 0 ..< Int.max {
        sqrtSum += sqrt(Double(i))
        
        if (CACurrentMediaTime() >= displayLink.targetTimestamp) {
            print("break at i =", i)
            break
        }
    }
}
```

## See Also

### Configuring a Display Link

- [duration](duration.md) — The time interval between screen refresh updates.
- [preferredFrameRateRange](preferredframeraterange.md) — A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [preferredFramesPerSecond](preferredframespersecond.md) — A frequency your app prefers for frame updates, affecting how often the system invokes your delegate’s callback. _(deprecated)_
- [paused](ispaused.md) — A Boolean value that indicates whether the system suspends the display link’s notifications to the target.
- [timestamp](timestamp.md) — The time interval that represents when the last frame displayed.
- [frameInterval](frameinterval.md) — The number of frames that must pass before the display link notifies the target again. _(deprecated)_
