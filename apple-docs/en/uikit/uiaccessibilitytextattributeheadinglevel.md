---
title: UIAccessibilityTextAttributeHeadingLevel
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitytextattributeheadinglevel
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitytextattributeheadinglevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitytextattributeheadinglevel.json'
content_hash: 'sha256:63ce79eb30685ce5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityTextAttributeHeadingLevel

<sub>Global Variable</sub>

A key for specifying the heading level of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringKey const UIAccessibilityTextAttributeHeadingLevel;
```

## Overview

The value of this key is an [NSNumber](../foundation/nsnumber.md) object with a value that is a number in the range of `0` to `6`. Use `0` to indicate the absence of a specific heading level, and use other numbers to indicate the heading level.

## See Also

### Constants

- [UIAccessibilityTextAttributeCustom](uiaccessibilitytextattributecustom.md) — A key for specifying custom attributes to apply to the text.
- [UIAccessibilityTextAttributeContext](uiaccessibilitytextattributecontext.md)
