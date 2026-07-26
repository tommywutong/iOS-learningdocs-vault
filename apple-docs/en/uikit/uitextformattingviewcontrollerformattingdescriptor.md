---
title: UITextFormattingViewControllerFormattingDescriptor
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextformattingviewcontrollerformattingdescriptor
source_url: 'https://developer.apple.com/documentation/uikit/uitextformattingviewcontrollerformattingdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextformattingviewcontrollerformattingdescriptor.json'
content_hash: 'sha256:b26b29e46d3384e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextFormattingViewControllerFormattingDescriptor

<sub>Class</sub>

Object that represents current text formatting state. This can apply to formatting state of some selected range of text or currently applicable input formatting.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UITextFormattingViewControllerFormattingDescriptor : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Instance Properties

- [fonts](uitextformattingviewcontrollerformattingdescriptor/fonts.md)
- [formattingStyleKey](uitextformattingviewcontrollerformattingdescriptor/formattingstylekey.md)
- [highlights](uitextformattingviewcontrollerformattingdescriptor/highlights.md)
- [lineHeight](uitextformattingviewcontrollerformattingdescriptor/lineheight.md)
- [strikethroughPresent](uitextformattingviewcontrollerformattingdescriptor/strikethroughpresent.md)
- [textAlignments](uitextformattingviewcontrollerformattingdescriptor/textalignments.md)
- [textColors](uitextformattingviewcontrollerformattingdescriptor/textcolors.md)
- [textLists](uitextformattingviewcontrollerformattingdescriptor/textlists.md)
- [underlinePresent](uitextformattingviewcontrollerformattingdescriptor/underlinepresent.md)

### Instance Methods

- [init](uitextformattingviewcontrollerformattingdescriptor/init.md) — Initializes formatting descriptor with default property values.
- [initWithAttributes:](uitextformattingviewcontrollerformattingdescriptor/initwithattributes_.md) — Initializes formatting descriptor with attribute dictionary.
- [initWithString:range:](uitextformattingviewcontrollerformattingdescriptor/initwithstring_range_.md) — Initializes formatting descriptor with a string and selected range of string.

## See Also

### Classes

- [Component](uitextformattingviewcontroller/component.md) — Defines text formatting view component.
- [ComponentGroup](uitextformattingviewcontroller/componentgroup.md) — Defines grouping of text formatting components in view.
- [Configuration](uitextformattingviewcontroller/configuration-swift.class.md) — Text formatting view controller configuration object.
- [UITextFormattingViewControllerChangeValue](uitextformattingviewcontrollerchangevalue.md) — Describes text formatting change that is a result of user action. Contains type of change, any associated value that may be applicable to that change.
- [UITextFormattingViewControllerFormattingStyle](uitextformattingviewcontrollerformattingstyle.md) — Type that defines formatting style presented in text formatting view.
