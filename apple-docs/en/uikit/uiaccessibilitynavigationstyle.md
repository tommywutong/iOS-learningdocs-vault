---
title: UIAccessibilityNavigationStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitynavigationstyle
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitynavigationstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitynavigationstyle.json'
content_hash: 'sha256:21961a16dcd4e7d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityNavigationStyle

<sub>Enumeration</sub>

Constants that describe how to navigate an object’s elements with an assistive app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
enum UIAccessibilityNavigationStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIAccessibilityNavigationStyleAutomatic](uiaccessibilitynavigationstyle/automatic.md) — The assistive technology automatically determines how the receiver’s elements should be navigated.
- [UIAccessibilityNavigationStyleSeparate](uiaccessibilitynavigationstyle/separate.md) — The receiver’s elements should be navigated as separate elements.
- [UIAccessibilityNavigationStyleCombined](uiaccessibilitynavigationstyle/combined.md) — The receiver’s elements should be combined and navigated as a single item.

### Initializers

- [init(rawValue:)](<uiaccessibilitynavigationstyle/init(rawvalue_).md>)

## See Also

### Navigating elements

- [UIAccessibilityContainer](uiaccessibilitycontainer.md) — Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [accessibilityActivationPoint](../objectivec/nsobject-swift.class/accessibilityactivationpoint.md)
- [accessibilityFocusedUIElement](../objectivec/nsobject-swift.class/accessibilityfocuseduielement.md)
- [accessibilityFrame](../objectivec/nsobject-swift.class/accessibilityframe.md)
- [accessibilityHitTest(_:)](<../objectivec/nsobject-swift.class/accessibilityhittest(__).md>)
- [accessibilityNavigationStyle](../objectivec/nsobject-swift.class/accessibilitynavigationstyle.md)
- [accessibilityPath](../objectivec/nsobject-swift.class/accessibilitypath.md)
- [UIAccessibilityZoomFocusChanged](<uiaccessibility/zoomfocuschanged(zoomtype_toframe_in_).md>) — Notifies the system when the app’s focus changes to a new location.
- [ZoomType](uiaccessibility/zoomtype.md) — The types of system Zoom that can be in effect.
- [UIGuidedAccessAccessibilityFeatureAssistiveTouch](uiguidedaccessaccessibilityfeature/assistivetouch.md) — The AssistiveTouch accessibility feature.
