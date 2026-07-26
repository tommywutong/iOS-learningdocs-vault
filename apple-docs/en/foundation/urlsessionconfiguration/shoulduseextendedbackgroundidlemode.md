---
title: shouldUseExtendedBackgroundIdleMode
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（18.4 起废弃）, iPadOS 9.0+（18.4 起废弃）, Mac Catalyst 13.1+（18.4 起废弃）, macOS 10.11+（15.4 起废弃）, tvOS 9.0+（18.4 起废弃）, visionOS 1.0+（2.4 起废弃）, watchOS 2.0+（11.4 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlsessionconfiguration/shoulduseextendedbackgroundidlemode
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/shoulduseextendedbackgroundidlemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/shoulduseextendedbackgroundidlemode.json'
content_hash: 'sha256:5eeb69293ddee736'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# shouldUseExtendedBackgroundIdleMode

<sub>Instance Property</sub>

A Boolean value that indicates whether TCP connections should be kept open when the app moves to the background.

> [!warning] Deprecated
> Not supported

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var shouldUseExtendedBackgroundIdleMode: Bool { get set }
```

## Discussion

In addition to requesting that the connection be kept open, setting this value to [true](../../swift/true.md) asks the system to delay reclaiming the connection when the app moves to the background.

## See Also

### Related Documentation

- [Networking and Multitasking](https://developer.apple.com/library/archive/technotes/tn2277/_index.html#//apple_ref/doc/uid/DTS40010841)

### Supporting background transfers

- [sessionSendsLaunchEvents](sessionsendslaunchevents.md) — A Boolean value that indicates whether the app should be resumed or launched in the background when transfers finish.
- [discretionary](isdiscretionary.md) — A Boolean value that determines whether background tasks can be scheduled at the discretion of the system for optimal performance.
