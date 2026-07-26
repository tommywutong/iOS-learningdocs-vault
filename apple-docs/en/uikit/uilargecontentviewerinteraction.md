---
title: UILargeContentViewerInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilargecontentviewerinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentviewerinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentviewerinteraction.json'
content_hash: 'sha256:147d4bc99cd48183'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILargeContentViewerInteraction

<sub>Class</sub>

An interaction that enables a gesture to present the large content viewer for cases when supporting the largest dynamic type sizes isn’t appropriate.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UILargeContentViewerInteraction
```

## Overview

Don’t use the large content viewer as a replacement for proper Dynamic Type support. For example, Dynamic Type allows items in a list to grow or shrink vertically to accommodate the user’s preferred font size. Rely on the large content viewer only in situations where items must remain small due to unavoidable design constraints. For example, buttons in a tab bar remain small to leave more room for the main app content.

For more information about allowing your app’s content to adjust to varying font sizes, see [Add Dynamic Type support](creating-self-sizing-table-view-cells.md#Add-Dynamic-Type-support) and the [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/accessibility/overview/text-size-and-weight/).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Creating large content viewer interactions

- [- initWithDelegate:](<uilargecontentviewerinteraction/init(delegate_).md>) — Creates an interaction object with the specified delegate.

### Customizing large content viewer interactions

- [delegate](uilargecontentviewerinteraction/delegate.md) — An object that can fine-tune the large content viewer interactions, especially in the presence of other gesture recognizers.
- [gestureRecognizerForExclusionRelationship](uilargecontentviewerinteraction/gesturerecognizerforexclusionrelationship.md) — A gesture recognizer that you can use to set up simultaneous recognition or failure relationships with other gesture recognizers.

### Detecting the large content viewer

- [enabled](uilargecontentviewerinteraction/isenabled.md) — A Boolean value that indicates whether the large content viewer is enabled on the device.
- [UILargeContentViewerInteractionEnabledStatusDidChangeNotification](uilargecontentviewerinteraction/enabledstatusdidchangenotification.md) — A notification the system posts when it enables or disables the large content viewer.

## See Also

### Content viewer

- [UILargeContentViewerInteractionDelegate](uilargecontentviewerinteractiondelegate.md) — An object that customizes the behavior of the large content viewer interactions.
- [UILargeContentViewerItem](uilargecontentvieweritem.md) — Methods that provide details about how to display your custom content in the large content viewer.
