---
title: 'displayLink(withTarget:selector:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（27.0 起废弃）, iPadOS 4.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiscreen/displaylink(withtarget:selector:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/displaylink(withtarget:selector:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/displaylink%28withtarget%3Aselector%3A%29.json'
content_hash: 'sha256:68dc5d1f58611c3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# displayLink(withTarget:selector:)

<sub>Instance Method</sub>

Returns a display link object for the current screen.

> [!warning] Deprecated
> Use the equivalent display link API on UIWindowScene

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func displayLink(withTarget target: Any, selector sel: Selector) -> CADisplayLink?
```

## Parameters

- `target` — An object to be notified when the screen should be updated.

- `sel` — The method of `target` to call. This selector must have the following signature: ```objc - (void)selector:(CADisplayLink *)sender; ```

## Return Value

A newly constructed display link object.

## Discussion

You use display link objects to synchronize your drawing code to the screen’s refresh rate. The newly constructed display link retains the target.

## See Also

### Getting a display link

- [maximumFramesPerSecond](maximumframespersecond.md) — The maximum number of frames per second a screen can render.
