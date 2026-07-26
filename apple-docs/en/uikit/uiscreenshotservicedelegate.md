---
title: UIScreenshotServiceDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreenshotservicedelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiscreenshotservicedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreenshotservicedelegate.json'
content_hash: 'sha256:be7f6c7b05654a12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIScreenshotServiceDelegate

<sub>Protocol</sub>

Methods you use to generate PDF data that accompanies a user-requested screenshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
@MainActor protocol UIScreenshotServiceDelegate : NSObjectProtocol
```

## Overview

When the user captures a screenshot of your app’s windows, UIKit calls the methods of this protocol to retrieve PDF data for those windows, and then it provides that data to the user. Adopt this protocol in a custom object of your app, and assign that object to the [UIScreenshotService](uiscreenshotservice.md) object associated with one of your window scenes. Use your custom delegate object to generate PDF content for the windows in the associated window-scene object.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing the PDF data

- [- screenshotService:generatePDFRepresentationWithCompletion:](<uiscreenshotservicedelegate/screenshotservice(__generatepdfrepresentationwithcompletion_).md>) — Generates a high-fidelity PDF version of the entire content in a given window scene.

## See Also

### Responding to screenshot requests

- [delegate](uiscreenshotservice/delegate.md) — The custom object you use to provide PDF data for a screenshot.
