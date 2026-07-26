---
title: NSAttributedString.EnumerationOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/enumerationoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/enumerationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/enumerationoptions.json'
content_hash: 'sha256:e07b15e656b3717a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# NSAttributedString.EnumerationOptions

<sub>Structure</sub>

Options for enumerating attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct EnumerationOptions
```

## Overview

These constants describe the options available to the [- enumerateAttribute:inRange:options:usingBlock:](<enumerateattribute(__in_options_using_).md>) and [- enumerateAttributesInRange:options:usingBlock:](<enumerateattributes(in_options_using_).md>) methods.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Getting the enumeration options

- [NSAttributedStringEnumerationReverse](enumerationoptions/reverse.md) — Causes the enumeration to occur in reverse.
- [NSAttributedStringEnumerationLongestEffectiveRangeNotRequired](enumerationoptions/longesteffectiverangenotrequired.md) — If `NSAttributedStringEnumerationLongestEffectiveRangeNotRequired` option is supplied, then the longest effective range computation is not performed; the blocks may be invoked with consecutive attribute runs that have the same value.

### Creating an enumeration option

- [init(rawValue:)](<enumerationoptions/init(rawvalue_).md>)
- [NSAttributedStringEnumerationReverse](enumerationoptions/reverse.md) — Causes the enumeration to occur in reverse.
- [NSAttributedStringEnumerationLongestEffectiveRangeNotRequired](enumerationoptions/longesteffectiverangenotrequired.md) — If `NSAttributedStringEnumerationLongestEffectiveRangeNotRequired` option is supplied, then the longest effective range computation is not performed; the blocks may be invoked with consecutive attribute runs that have the same value.

## See Also

### Getting attributes for a range of text

- [- attributesAtIndex:effectiveRange:](<attributes(at_effectiverange_).md>) — Returns the attributes for the character at the specified index.
- [- attributesAtIndex:longestEffectiveRange:inRange:](<attributes(at_longesteffectiverange_in_).md>) — Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.
- [- attribute:atIndex:effectiveRange:](<attribute(__at_effectiverange_).md>) — Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [- attribute:atIndex:longestEffectiveRange:inRange:](<attribute(__at_longesteffectiverange_in_).md>) — Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [- enumerateAttribute:inRange:options:usingBlock:](<enumerateattribute(__in_options_using_).md>) — Executes the specified closure or block for each range of a particular attribute in the attributed string.
- [- enumerateAttributesInRange:options:usingBlock:](<enumerateattributes(in_options_using_).md>) — Executes the specified closure or block for each range of attributes in the attributed string.
