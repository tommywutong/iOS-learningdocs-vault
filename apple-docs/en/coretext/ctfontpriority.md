---
title: CTFontPriority
framework: Core Text
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontpriority
source_url: 'https://developer.apple.com/documentation/coretext/ctfontpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontpriority.json'
content_hash: 'sha256:bf156549672e96c7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontPriority

<sub>Type Alias</sub>

The priority of font descriptors when resolving duplicates and sorting match results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CTFontPriority = UInt32
```

## Discussion

Use the values of this enumeration for [kCTFontPriorityAttribute](kctfontpriorityattribute.md).

## Topics

### Font Priority

- [kCTFontPrioritySystem](kctfontprioritysystem.md) — Priority of system fonts.
- [kCTFontPriorityNetwork](kctfontprioritynetwork.md) — Priority of network fonts.
- [kCTFontPriorityComputer](kctfontprioritycomputer.md) — Priority of computer local fonts.
- [kCTFontPriorityUser](kctfontpriorityuser.md) — Priority of local fonts.
- [kCTFontPriorityDynamic](kctfontprioritydynamic.md) — Priority of fonts registered dynamically, not located in a standard location.
- [kCTFontPriorityProcess](kctfontpriorityprocess.md) — Priority of fonts registered for the process.

## See Also

### Related Documentation

- [kCTFontPriorityAttribute](kctfontpriorityattribute.md) — The font priority used by font descriptors when resolving duplicates and sorting match results.

### Accessing Font Attributes

- [Font Attributes](font-attributes.md) — The keys for accessing font attributes from a font descriptor.
- [CTFontOrientation](ctfontorientation.md) — The intended rendering orientation of the font for obtaining glyph metrics.
- [CTFontFormat](ctfontformat.md) — The recognized format of the font.
