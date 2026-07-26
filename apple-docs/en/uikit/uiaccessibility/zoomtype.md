---
title: UIAccessibility.ZoomType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/zoomtype
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/zoomtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/zoomtype.json'
content_hash: 'sha256:a2542f3700e3a0b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# UIAccessibility.ZoomType

<sub>Enumeration</sub>

The types of system Zoom that can be in effect.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum ZoomType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIAccessibilityZoomTypeInsertionPoint](zoomtype/insertionpoint.md) — The system zoom type is the text insertion point.

### Initializers

- [init(rawValue:)](<zoomtype/init(rawvalue_).md>)

## See Also

### Navigating elements

- [UIAccessibilityContainer](../uiaccessibilitycontainer.md) — Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [accessibilityActivationPoint](../../objectivec/nsobject-swift.class/accessibilityactivationpoint.md)
- [accessibilityFocusedUIElement](../../objectivec/nsobject-swift.class/accessibilityfocuseduielement.md)
- [accessibilityFrame](../../objectivec/nsobject-swift.class/accessibilityframe.md)
- [accessibilityHitTest(_:)](<../../objectivec/nsobject-swift.class/accessibilityhittest(__).md>)
- [accessibilityNavigationStyle](../../objectivec/nsobject-swift.class/accessibilitynavigationstyle.md)
- [UIAccessibilityNavigationStyle](../uiaccessibilitynavigationstyle.md) — Constants that describe how to navigate an object’s elements with an assistive app.
- [accessibilityPath](../../objectivec/nsobject-swift.class/accessibilitypath.md)
- [UIAccessibilityZoomFocusChanged](<zoomfocuschanged(zoomtype_toframe_in_).md>) — Notifies the system when the app’s focus changes to a new location.
- [UIGuidedAccessAccessibilityFeatureAssistiveTouch](../uiguidedaccessaccessibilityfeature/assistivetouch.md) — The AssistiveTouch accessibility feature.
