---
title: isDiscretionary
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/isdiscretionary
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/isdiscretionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/isdiscretionary.json'
content_hash: 'sha256:4a8b836e21344382'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# isDiscretionary

<sub>Instance Property</sub>

A Boolean value that determines whether background tasks can be scheduled at the discretion of the system for optimal performance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isDiscretionary: Bool { get set }
```

## Discussion

For configuration objects created using the [+ backgroundSessionConfigurationWithIdentifier:](<background(withidentifier_).md>) method, use this property to give the system control over when transfers should occur. This property is ignored for configuration objects created using other methods.

When transferring large amounts of data, you are encouraged to set the value of this property to [true](../../swift/true.md). Doing so lets the system schedule those transfers at times that are more optimal for the device. For example, the system might delay transferring large files until the device is plugged in and connected to the network via Wi-Fi. The default value of this property is [false](../../swift/false.md).

The session object applies the value of this property only to transfers that your app starts while it is in the foreground. For transfers started while your app is in the background, the system always starts transfers at its discretion—in other words, the system assumes this property is [true](../../swift/true.md) and ignores any value you specified.

## See Also

### Supporting background transfers

- [sessionSendsLaunchEvents](sessionsendslaunchevents.md) — A Boolean value that indicates whether the app should be resumed or launched in the background when transfers finish.
- [shouldUseExtendedBackgroundIdleMode](shoulduseextendedbackgroundidlemode.md) — A Boolean value that indicates whether TCP connections should be kept open when the app moves to the background. _(deprecated)_
