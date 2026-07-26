---
title: extensionContext
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/extensioncontext
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/extensioncontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/extensioncontext.json'
content_hash: 'sha256:13b968130d71db9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# extensionContext

<sub>Instance Property</sub>

Returns the extension context of the view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var extensionContext: NSExtensionContext? { get }
```

## Discussion

The view controller can check this property to see if it participates in an extension request. If no extension context is set for the current view controller, the system walks up the view controller hierarchy to find a parent view controller that has a non `nil` `extensionContext` value.
