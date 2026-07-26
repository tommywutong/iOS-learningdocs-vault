---
title: AVCaptureDeskViewApplication.LaunchConfiguration
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 16.1+, macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration.json'
content_hash: 'sha256:a85f6125a8e7d2bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeskViewApplication](../avcapturedeskviewapplication.md)

# AVCaptureDeskViewApplication.LaunchConfiguration

<sub>Class</sub>

An object that configures how to present Desk View.

<sub>Mac Catalyst, macOS</sub>

```swift
class LaunchConfiguration
```

## Overview

Use this object to specify the frame for Desk View when it launches, and when to execute the completion handler. You can specify whether to perform the completion handler as soon as Desk View is visible to the user, or only after they start Desk View.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Customizing the presentation

- [mainWindowFrame](launchconfiguration/mainwindowframe.md) — The frame for Desk View after it launches.
- [requiresSetUpModeCompletion](launchconfiguration/requiressetupmodecompletion.md) — A Boolean value that specifies whether the system requires the user to complete setup mode before it executes the completion handler.

## See Also

### Presenting the Desk View app

- [- presentWithCompletionHandler:](<present(completionhandler_).md>) — Launches Desk View with no additional configuration and then performs a completion handler if you specify it.
- [- presentWithLaunchConfiguration:completionHandler:](<present(launchconfiguration_completionhandler_).md>) — Launches Desk View with the configuration and completion handler that you specify.
