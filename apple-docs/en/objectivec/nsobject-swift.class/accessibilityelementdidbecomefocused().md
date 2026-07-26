---
title: accessibilityElementDidBecomeFocused()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityelementdidbecomefocused()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityelementdidbecomefocused()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityelementdidbecomefocused%28%29.json'
content_hash: 'sha256:35e9181467afa891'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityElementDidBecomeFocused()

<sub>Instance Method</sub>

Sent after an assistive technology has set its virtual focus on the accessibility element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityElementDidBecomeFocused()
```

## Discussion

Override `accessibilityElementDidBecomeFocused` if you need to know when an assistive technology has set its virtual focus on an accessibility element.

## See Also

### Getting focus information

- [- accessibilityElementDidLoseFocus](<accessibilityelementdidlosefocus().md>) — Sent after an assistive technology has removed its virtual focus from an accessibility element.
- [- accessibilityElementIsFocused](<accessibilityelementisfocused().md>) — Returns a Boolean value indicating whether an assistive technology is focused on the accessibility element.
- [- accessibilityAssistiveTechnologyFocusedIdentifiers](<accessibilityassistivetechnologyfocusedidentifiers().md>) — Returns a set of identifier keys indicating which assistive app has focus on the accessibility element.
