---
title: accessibilityCustomActions
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilitycustomactions
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitycustomactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilitycustomactions.json'
content_hash: 'sha256:5203df97b6ec48b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityCustomActions

<sub>Instance Property</sub>

An array of custom actions to display along with the built-in actions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor var accessibilityCustomActions: [UIAccessibilityCustomAction]? { get set }
```

## Discussion

The array contains one or more `UIAccessibilityCustomAction` objects defining the supported actions. Assistive technologies, such as VoiceOver, display your custom actions to the user at appropriate times.
