---
title: kCTFontPrioritySystem
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontprioritysystem
source_url: 'https://developer.apple.com/documentation/coretext/kctfontprioritysystem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontprioritysystem.json'
content_hash: 'sha256:705bd0eac583aa3d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontPrioritySystem

<sub>Global Variable</sub>

Priority of system fonts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCTFontPrioritySystem: Int { get }
```

## Discussion

System fonts are located in `/System/Library/Fonts`.

## See Also

### Font Priority

- [kCTFontPriorityNetwork](kctfontprioritynetwork.md) — Priority of network fonts.
- [kCTFontPriorityComputer](kctfontprioritycomputer.md) — Priority of computer local fonts.
- [kCTFontPriorityUser](kctfontpriorityuser.md) — Priority of local fonts.
- [kCTFontPriorityDynamic](kctfontprioritydynamic.md) — Priority of fonts registered dynamically, not located in a standard location.
- [kCTFontPriorityProcess](kctfontpriorityprocess.md) — Priority of fonts registered for the process.
