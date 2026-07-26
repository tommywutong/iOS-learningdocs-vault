---
title: UITextFormattingViewControllerChangeValue
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextformattingviewcontrollerchangevalue
source_url: 'https://developer.apple.com/documentation/uikit/uitextformattingviewcontrollerchangevalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextformattingviewcontrollerchangevalue.json'
content_hash: 'sha256:06462ca953a951e5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextFormattingViewControllerChangeValue

<sub>Class</sub>

Describes text formatting change that is a result of user action. Contains type of change, any associated value that may be applicable to that change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UITextFormattingViewControllerChangeValue : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Instance Properties

- [changeType](uitextformattingviewcontrollerchangevalue/changetype.md) — Type of change.
- [color](uitextformattingviewcontrollerchangevalue/color.md) — Any color value that may be associated with the change. For example, this property will be available if user has changed text color.
- [font](uitextformattingviewcontrollerchangevalue/font.md) — Any font that may be associated with the change. For example, this property will be available in case of font typography settings change or new font selection.
- [formattingStyleKey](uitextformattingviewcontrollerchangevalue/formattingstylekey.md) — On formatting style change, use this property to determine selected style.
- [highlight](uitextformattingviewcontrollerchangevalue/highlight.md) — Text highlight associated with the `UITextFormattingViewControllerHighlightChangeType`. If property is nil for `UITextFormattingViewControllerHighlightChangeType`, it indicates highlight has been removed.
- [numberValue](uitextformattingviewcontrollerchangevalue/numbervalue.md) — Any number value that may be associated with the change. For example, if case of font point size change, this property will reflect new point size.
- [textAlignment](uitextformattingviewcontrollerchangevalue/textalignment.md) — Text alignment associated with the `UITextFormattingViewControllerTextAlignmentChangeType`.
- [textList](uitextformattingviewcontrollerchangevalue/textlist.md) — Text list style associated with the `UITextFormattingViewControllerTextListChangeType`. If property is nil for `UITextFormattingViewControllerTextListChangeType`, it indicates text list has been removed.

## See Also

### Classes

- [Component](uitextformattingviewcontroller/component.md) — Defines text formatting view component.
- [ComponentGroup](uitextformattingviewcontroller/componentgroup.md) — Defines grouping of text formatting components in view.
- [Configuration](uitextformattingviewcontroller/configuration-swift.class.md) — Text formatting view controller configuration object.
- [UITextFormattingViewControllerFormattingDescriptor](uitextformattingviewcontrollerformattingdescriptor.md) — Object that represents current text formatting state. This can apply to formatting state of some selected range of text or currently applicable input formatting.
- [UITextFormattingViewControllerFormattingStyle](uitextformattingviewcontrollerformattingstyle.md) — Type that defines formatting style presented in text formatting view.
