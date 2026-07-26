---
title: accessibilityTextInputResponderBlock
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.1+, iPadOS 18.1+, Mac Catalyst 18.1+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilitytextinputresponderblock
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitytextinputresponderblock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilitytextinputresponderblock.json'
content_hash: 'sha256:b04d1c8bb44a4395'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityTextInputResponderBlock

<sub>Instance Property</sub>

The block to use to handle text input calls to a backing view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor var accessibilityTextInputResponderBlock: AXUITextInputReturnBlock? { get set }
```

## Discussion

If your accessibility element represents a view that supports text operations using the [UITextInput](../../uikit/uitextinput.md) protocol, use this property to forward `UITextInput` calls to your backing view.
