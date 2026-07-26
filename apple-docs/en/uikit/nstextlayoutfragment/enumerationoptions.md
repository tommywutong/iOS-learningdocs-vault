---
title: NSTextLayoutFragment.EnumerationOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutfragment/enumerationoptions
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment/enumerationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment/enumerationoptions.json'
content_hash: 'sha256:81c2a52d5c082152'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutFragment](../nstextlayoutfragment.md)

# NSTextLayoutFragment.EnumerationOptions

<sub>Structure</sub>

Values that describe options for enumerating text layout fragments.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct EnumerationOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating a layout fragment enumeration

- [init(rawValue:)](<enumerationoptions/init(rawvalue_).md>) — Creates an instance of the enumeration with the provided unsigned integer value.

### Layout fragment characteristics

- [NSTextLayoutFragmentEnumerationOptionsEnsuresExtraLineFragment](enumerationoptions/ensuresextralinefragment.md) — Synthesize the extra line fragment when necessary.
- [NSTextLayoutFragmentEnumerationOptionsEnsuresLayout](enumerationoptions/ensureslayout.md) — When enumerating, tell the layout fragments to layout their contents.
- [NSTextLayoutFragmentEnumerationOptionsEstimatesSize](enumerationoptions/estimatessize.md) — When enumerating, tell the layout fragments to estimate their size.
- [NSTextLayoutFragmentEnumerationOptionsReverse](enumerationoptions/reverse.md) — Causes the enumeration to start from the last element.

## See Also

### Accessing and updating the text

- [- enumerateTextElementsFromLocation:options:usingBlock:](<../nstextelementprovider/enumeratetextelements(from_options_using_).md>) — Enumerates text elements starting at the text location you provide.
- [- locationFromLocation:withOffset:](<../nstextelementprovider/location(__offsetby_).md>) — Returns a new location from location with offset you provide.
- [- replaceContentsInRange:withTextElements:](<../nstextelementprovider/replacecontents(in_with_).md>) — Replaces the characters specified by range with the text elements you provide.
