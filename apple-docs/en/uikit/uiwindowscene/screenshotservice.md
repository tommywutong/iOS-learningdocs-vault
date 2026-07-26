---
title: screenshotService
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/screenshotservice
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/screenshotservice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/screenshotservice.json'
content_hash: 'sha256:73028240ba62ad40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# screenshotService

<sub>Instance Property</sub>

An object that generates a high-fidelity version of your app’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var screenshotService: UIScreenshotService? { get }
```

## Discussion

When you want to make your scene content available in PDF format, supply a delegate to the [UIScreenshotService](../uiscreenshotservice.md) object in this property. When the user takes a screenshot involving your scene, the screenshot service asks your delegate to provide the associated PDF data. Your delegate object must conform to the [UIScreenshotServiceDelegate](../uiscreenshotservicedelegate.md) protocol.

Provide PDF data for your app’s content whenever possible. Providing the data makes it easier and faster for the user to mark up that data later.

## See Also

### Providing a PDF version of your scene

- [UIScreenshotService](../uiscreenshotservice.md) — An object that coordinates the creation of PDF screenshots of an app’s content.
