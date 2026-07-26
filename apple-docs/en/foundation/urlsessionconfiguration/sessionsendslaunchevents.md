---
title: sessionSendsLaunchEvents
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/sessionsendslaunchevents
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/sessionsendslaunchevents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/sessionsendslaunchevents.json'
content_hash: 'sha256:c2609ebfbe5a6672'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# sessionSendsLaunchEvents

<sub>Instance Property</sub>

A Boolean value that indicates whether the app should be resumed or launched in the background when transfers finish.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sessionSendsLaunchEvents: Bool { get set }
```

## Discussion

For configuration objects created using the [+ backgroundSessionConfigurationWithIdentifier:](<background(withidentifier_).md>) method, you can use this property to control the launching behavior for an iOS app. This property is ignored for configuration objects created using other methods.

The default value of this property is [true](../../swift/true.md). When the value of this property is [true](../../swift/true.md), the system automatically wakes up or launches the iOS app in the background when the session’s tasks finish or require authentication. At that time, the system calls the app delegate’s [application(_:handleEventsForBackgroundURLSession:completionHandler:)](<../../uikit/uiapplicationdelegate/application(__handleeventsforbackgroundurlsession_completionhandler_).md>) method, providing it with the identifier of the session that needs attention. If your app had to be relaunched, you can use that identifier to create a new configuration and session object capable of servicing the tasks.

## See Also

### Supporting background transfers

- [discretionary](isdiscretionary.md) — A Boolean value that determines whether background tasks can be scheduled at the discretion of the system for optimal performance.
- [shouldUseExtendedBackgroundIdleMode](shoulduseextendedbackgroundidlemode.md) — A Boolean value that indicates whether TCP connections should be kept open when the app moves to the background. _(deprecated)_
