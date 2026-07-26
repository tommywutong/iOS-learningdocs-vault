---
title: accessibilityLargeContentViewerEnabled
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/accessibilitylargecontentviewerenabled
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilitylargecontentviewerenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/accessibilitylargecontentviewerenabled.json'
content_hash: 'sha256:b410ad1e80faf434'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# accessibilityLargeContentViewerEnabled

<sub>Instance Property</sub>

Whether the Large Content Viewer is enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var accessibilityLargeContentViewerEnabled: Bool { get }
```

## Discussion

The system can automatically provide a large content view with [accessibilityShowsLargeContentViewer()](<../view/accessibilityshowslargecontentviewer().md>) or you can provide your own with [accessibilityShowsLargeContentViewer(_:)](<../view/accessibilityshowslargecontentviewer(__).md>).

While it is not necessary to check this value before adding a large content view, it may be helpful if you need to adjust the behavior of a gesture. For example, a button with a long press handler might increase its long press duration so the user can read the text in the large content viewer first.

## See Also

### Enlarging content

- [accessibilityShowsLargeContentViewer()](<../view/accessibilityshowslargecontentviewer().md>) — Adds a default large content view to be shown by the large content viewer.
- [accessibilityShowsLargeContentViewer(_:)](<../view/accessibilityshowslargecontentviewer(__).md>) — Adds a custom large content view to be shown by the large content viewer.
