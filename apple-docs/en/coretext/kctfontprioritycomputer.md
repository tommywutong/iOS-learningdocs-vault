---
title: kCTFontPriorityComputer
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontprioritycomputer
source_url: 'https://developer.apple.com/documentation/coretext/kctfontprioritycomputer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontprioritycomputer.json'
content_hash: 'sha256:d9e68efa06297269'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontPriorityComputer

<sub>Global Variable</sub>

Priority of computer local fonts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCTFontPriorityComputer: Int { get }
```

## Discussion

Computer local fonts are located in `/Library/Fonts`.

## See Also

### Font Priority

- [kCTFontPrioritySystem](kctfontprioritysystem.md) — Priority of system fonts.
- [kCTFontPriorityNetwork](kctfontprioritynetwork.md) — Priority of network fonts.
- [kCTFontPriorityUser](kctfontpriorityuser.md) — Priority of local fonts.
- [kCTFontPriorityDynamic](kctfontprioritydynamic.md) — Priority of fonts registered dynamically, not located in a standard location.
- [kCTFontPriorityProcess](kctfontpriorityprocess.md) — Priority of fonts registered for the process.
