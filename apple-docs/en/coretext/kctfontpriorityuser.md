---
title: kCTFontPriorityUser
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontpriorityuser
source_url: 'https://developer.apple.com/documentation/coretext/kctfontpriorityuser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontpriorityuser.json'
content_hash: 'sha256:5caf6419d4851bf1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontPriorityUser

<sub>Global Variable</sub>

Priority of local fonts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCTFontPriorityUser: Int { get }
```

## Discussion

Local fonts are located in user’s `Library/Fonts`.

## See Also

### Font Priority

- [kCTFontPrioritySystem](kctfontprioritysystem.md) — Priority of system fonts.
- [kCTFontPriorityNetwork](kctfontprioritynetwork.md) — Priority of network fonts.
- [kCTFontPriorityComputer](kctfontprioritycomputer.md) — Priority of computer local fonts.
- [kCTFontPriorityDynamic](kctfontprioritydynamic.md) — Priority of fonts registered dynamically, not located in a standard location.
- [kCTFontPriorityProcess](kctfontpriorityprocess.md) — Priority of fonts registered for the process.
