---
title: 'contentCaptureProtected(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/compositorcontent/contentcaptureprotected(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/compositorcontent/contentcaptureprotected(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/compositorcontent/contentcaptureprotected%28_%3A%29.json'
content_hash: 'sha256:53509183137cacac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CompositorContent](../compositorcontent.md)

# contentCaptureProtected(_:)

<sub>Instance Method</sub>

Marks the view as a view that activates content protection during scene capture events, such as screenshots, screen recordings, screensharing, etc.

<sub>macOS, visionOS</sub>

```swift
nonisolated func contentCaptureProtected(_ isActive: Bool = true) -> some CompositorContent

```

## Parameters

- `isActive` — A Boolean value that specifies whether this view is protected when present on screen during scene capture.

## Discussion

The `contentCaptureProtected` modifier requires the [App-Protected Content](../../bundleresources/entitlements/com.apple.developer.protected-content.md) entitlement. For more information on how to apply for this entitlement, see [Building spatial experiences for business apps with enterprise APIs for visionOS](../../visionos/building-spatial-experiences-for-business-apps-with-enterprise-apis.md).

On visionOS, the system redacts the entire screen when a view marked with this modifier is present on screen, scene capture is active, and the app has the App Protected Content entitlement.
