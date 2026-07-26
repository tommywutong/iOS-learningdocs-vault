---
title: UIScreenshotService
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreenshotservice
source_url: 'https://developer.apple.com/documentation/uikit/uiscreenshotservice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreenshotservice.json'
content_hash: 'sha256:970e1948cecb783e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIScreenshotService

<sub>Class</sub>

An object that coordinates the creation of PDF screenshots of an app’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
@MainActor class UIScreenshotService
```

## Overview

When people take a screenshot of your app’s content, you work with a [UIScreenshotService](uiscreenshotservice.md) object to provide a PDF version of that screenshot. You don’t create a [UIScreenshotService](uiscreenshotservice.md) object directly. Instead, you retrieve the object from the [screenshotService](uiwindowscene/screenshotservice.md) property of your window scene and assign a delegate to it. Then when people take a screenshot, UIKit asks your delegate for the PDF data.

For information about how to provide the PDF data, see [UIScreenshotServiceDelegate](uiscreenshotservicedelegate.md).

> [!tip] Tip
> Beginning in iOS 17 and iPadOS 17, people have the option to share or save the generated full page screenshot as a PDF or an image.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Responding to screenshot requests

- [delegate](uiscreenshotservice/delegate.md) — The custom object you use to provide PDF data for a screenshot.
- [UIScreenshotServiceDelegate](uiscreenshotservicedelegate.md) — Methods you use to generate PDF data that accompanies a user-requested screenshot.

### Getting the current scene

- [windowScene](uiscreenshotservice/windowscene.md) — The window scene that contains the windows to capture in your PDF data.
