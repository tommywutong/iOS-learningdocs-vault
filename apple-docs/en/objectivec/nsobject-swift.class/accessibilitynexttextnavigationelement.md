---
title: accessibilityNextTextNavigationElement
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilitynexttextnavigationelement
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitynexttextnavigationelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilitynexttextnavigationelement.json'
content_hash: 'sha256:296a3b966f4a31d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityNextTextNavigationElement

<sub>Instance Property</sub>

An accessibility element that contains text that semantically follows this element’s text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor var accessibilityNextTextNavigationElement: Any? { get set }
```

## Discussion

Assistive technologies transition to these elements when navigating through text granularities, such as when using the VoiceOver Lines rotor.
