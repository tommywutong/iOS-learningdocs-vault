---
title: AVCaptureDeskViewApplication
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 16.1+, macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeskviewapplication
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeskviewapplication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeskviewapplication.json'
content_hash: 'sha256:60ad547f22857b1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureDeskViewApplication

<sub>Class</sub>

An object that programmatically presents Desk View.

<sub>Mac Catalyst, macOS</sub>

```swift
class AVCaptureDeskViewApplication
```

## Overview

Use this class to programmatically launch Desk View from your app. You can optionally customize the presentation and specifiy an action to take afterward.

> [!note] Note
> Desk View is available in iOS 16 and later on iPhone 11 and later, excluding iPhone SE, for use with a Mac running macOS 13 and later.

The following example shows how to configure and present Desk View with a completion handler:

```swift
let deskView = AVCaptureDeskViewApplication()
let configuration = AVCaptureDeskViewApplication.LaunchConfiguration()

// Use the previously set frame.
configuration.mainWindowFrame = .zero

// Execute the completion handler when the user starts Desk View.
configuration.requiresSetUpModeCompletion = true

// Launch Desk View with a configuration and completion handler.
deskView.present(launchConfiguration: configuration) { error in
    // Perform error handling and additional tasks.
}
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Presenting the Desk View app

- [- presentWithCompletionHandler:](<avcapturedeskviewapplication/present(completionhandler_).md>) — Launches Desk View with no additional configuration and then performs a completion handler if you specify it.
- [- presentWithLaunchConfiguration:completionHandler:](<avcapturedeskviewapplication/present(launchconfiguration_completionhandler_).md>) — Launches Desk View with the configuration and completion handler that you specify.
- [LaunchConfiguration](avcapturedeskviewapplication/launchconfiguration.md) — An object that configures how to present Desk View.

## See Also

### Continuity Camera

- [Supporting Continuity Camera in your tvOS app](../avkit/supporting-continuity-camera-in-your-tvos-app.md) — Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- [Supporting Continuity Camera in your macOS app](supporting-continuity-camera-in-your-macos-app.md) — Enable high-quality photo and video capture by using an iPhone camera as an external capture device.
