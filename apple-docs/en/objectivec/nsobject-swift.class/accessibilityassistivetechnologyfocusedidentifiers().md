---
title: accessibilityAssistiveTechnologyFocusedIdentifiers()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityassistivetechnologyfocusedidentifiers()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityassistivetechnologyfocusedidentifiers()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityassistivetechnologyfocusedidentifiers%28%29.json'
content_hash: 'sha256:7f0909d4b9b23ca8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityAssistiveTechnologyFocusedIdentifiers()

<sub>Instance Method</sub>

Returns a set of identifier keys indicating which assistive app has focus on the accessibility element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<UIAccessibility.AssistiveTechnologyIdentifier>?
```

## See Also

### Getting focus information

- [- accessibilityElementDidBecomeFocused](<accessibilityelementdidbecomefocused().md>) — Sent after an assistive technology has set its virtual focus on the accessibility element.
- [- accessibilityElementDidLoseFocus](<accessibilityelementdidlosefocus().md>) — Sent after an assistive technology has removed its virtual focus from an accessibility element.
- [- accessibilityElementIsFocused](<accessibilityelementisfocused().md>) — Returns a Boolean value indicating whether an assistive technology is focused on the accessibility element.
