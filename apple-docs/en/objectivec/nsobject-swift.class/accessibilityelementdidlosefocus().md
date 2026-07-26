---
title: accessibilityElementDidLoseFocus()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityelementdidlosefocus()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityelementdidlosefocus()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityelementdidlosefocus%28%29.json'
content_hash: 'sha256:1ffb48a3ef34be2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityElementDidLoseFocus()

<sub>Instance Method</sub>

Sent after an assistive technology has removed its virtual focus from an accessibility element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityElementDidLoseFocus()
```

## Discussion

Override `accessibilityElementDidLoseFocus` if you need to know when an assistive technology has removed its virtual focus from an accessibility element. Note that `accessibilityElementDidLoseFocus` is sent before [- accessibilityElementDidBecomeFocused](<accessibilityelementdidbecomefocused().md>).

## See Also

### Getting focus information

- [- accessibilityElementDidBecomeFocused](<accessibilityelementdidbecomefocused().md>) — Sent after an assistive technology has set its virtual focus on the accessibility element.
- [- accessibilityElementIsFocused](<accessibilityelementisfocused().md>) — Returns a Boolean value indicating whether an assistive technology is focused on the accessibility element.
- [- accessibilityAssistiveTechnologyFocusedIdentifiers](<accessibilityassistivetechnologyfocusedidentifiers().md>) — Returns a set of identifier keys indicating which assistive app has focus on the accessibility element.
