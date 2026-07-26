---
title: NSTextContentManager.EnumerationOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontentmanager/enumerationoptions
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanager/enumerationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanager/enumerationoptions.json'
content_hash: 'sha256:da0496b68be85581'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentManager](../nstextcontentmanager.md)

# NSTextContentManager.EnumerationOptions

<sub>Structure</sub>

Values that control the order in which the framework enumerates text elements.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct EnumerationOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating text element provider enumeration options

- [init(rawValue:)](<enumerationoptions/init(rawvalue_).md>) — Creates a new text element provider with the provided raw value.

### Accessing the enumeration setting

- [NSTextContentManagerEnumerationOptionsReverse](enumerationoptions/reverse.md) — Returns whether enumerations start from the end of the text element.

## See Also

### Customizing and validating text elements

- [delegate](delegate.md) — The delegate for the content manager object.
- [NSTextContentManagerDelegate](../nstextcontentmanagerdelegate.md) — The optional methods that delegates of content manager objects implement for customizing or validating text elements.
