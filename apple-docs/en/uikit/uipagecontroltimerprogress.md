---
title: UIPageControlTimerProgress
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipagecontroltimerprogress
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontroltimerprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontroltimerprogress.json'
content_hash: 'sha256:34c68fa135e945c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPageControlTimerProgress

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UIPageControlTimerProgress
```

## Relationships

- **Inherits From**: [UIPageControlProgress](uipagecontrolprogress.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [- initWithPreferredDuration:](<uipagecontroltimerprogress/init(preferredduration_).md>) — Creates a time interval progress with a specified preferred duration.

### Instance Properties

- [delegate](uipagecontroltimerprogress/delegate.md) — An object that defines the delegate of the page control progress.
- [running](uipagecontroltimerprogress/isrunning.md) — Returns YES if the timer is currently active.
- [preferredDuration](uipagecontroltimerprogress/preferredduration.md) — The preferred duration for the time interval progress, used when there is no custom page duration set for the current page. The preferred duration must be greater than 0.0
- [resetsToInitialPageAfterEnd](uipagecontroltimerprogress/resetstoinitialpageafterend.md) — Determines if the page control should loop back to page 0 after the last page. Default is NO.

### Instance Methods

- [- durationForPage:](<uipagecontroltimerprogress/duration(forpage_).md>) — Returns the duration for the specified page, and `preferredDuration` when there is no custom duration set for the specified page.
- [- pauseTimer](<uipagecontroltimerprogress/pausetimer().md>) — Pause the timer if it is active.
- [- resumeTimer](<uipagecontroltimerprogress/resumetimer().md>) — Resume the timer if it is not currently active.
- [- setDuration:forPage:](<uipagecontroltimerprogress/setduration(__forpage_).md>) — Sets a custom duration for the specified page. Set 0.0 to remove the custom duration for the specified page.

## See Also

### Configuring page progress

- [progress](uipagecontrol/progress.md) — An object that defines the progress of the page control. Default is nil.
- [UIPageControlProgress](uipagecontrolprogress.md)
- [UIPageControlProgressDelegate](uipagecontrolprogressdelegate.md)
- [UIPageControlTimerProgressDelegate](uipagecontroltimerprogressdelegate.md)
