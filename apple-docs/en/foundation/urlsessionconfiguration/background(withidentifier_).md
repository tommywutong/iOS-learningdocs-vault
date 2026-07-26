---
title: 'background(withIdentifier:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionconfiguration/background(withidentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/background(withidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/background%28withidentifier%3A%29.json'
content_hash: 'sha256:e31e624b0f97e333'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# background(withIdentifier:)

<sub>Type Method</sub>

Creates a session configuration object that allows HTTP and HTTPS uploads or downloads to be performed in the background.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func background(withIdentifier identifier: String) -> URLSessionConfiguration
```

## Parameters

- `identifier` — The unique identifier for the configuration object. This parameter must not be `nil` or an empty string.

## Return Value

A configuration object that causes the system to perform upload and download tasks in a separate process.

## Discussion

Use this method to initialize a configuration object suitable for transferring data files while the app runs in the background. A session configured with this object hands control of the transfers over to the system, which handles the transfers in a separate process. In iOS, this configuration makes it possible for transfers to continue even when the app itself is suspended or terminated.

If an iOS app is terminated by the system and relaunched, the app can use the same `identifier` to create a new configuration object and session and to retrieve the status of transfers that were in progress at the time of termination. This behavior applies only for normal termination of the app by the system. If the user terminates the app from the multitasking screen, the system cancels all of the session’s background transfers. In addition, the system does not automatically relaunch apps that were force quit by the user. The user must explicitly relaunch the app before transfers can begin again.

You can configure an background session to schedule transfers at the discretion of the system for optimal performance using the [discretionary](isdiscretionary.md) property. When transferring large amounts of data, you are encouraged to set the value of this property to [true](../../swift/true.md). For an example of using the background configuration, see [Downloading files in the background](../downloading-files-in-the-background.md).

## See Also

### Creating a session configuration object

- [defaultSessionConfiguration](default.md) — A default session configuration object.
- [ephemeralSessionConfiguration](ephemeral.md) — A session configuration that uses no persistent storage for caches, cookies, or credentials.
- [- init](<init().md>) — Creates an empty session configuration. _(deprecated)_
- [+ new](<new().md>) — Creates an empty session configuration. _(deprecated)_
