---
title: kCTFontPriorityNetwork
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontprioritynetwork
source_url: 'https://developer.apple.com/documentation/coretext/kctfontprioritynetwork'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontprioritynetwork.json'
content_hash: 'sha256:2484c166e44c78bb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontPriorityNetwork

<sub>Global Variable</sub>

Priority of network fonts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCTFontPriorityNetwork: Int { get }
```

## Discussion

Network fonts are located in `/Network/Library/Fonts`.

## See Also

### Font Priority

- [kCTFontPrioritySystem](kctfontprioritysystem.md) — Priority of system fonts.
- [kCTFontPriorityComputer](kctfontprioritycomputer.md) — Priority of computer local fonts.
- [kCTFontPriorityUser](kctfontpriorityuser.md) — Priority of local fonts.
- [kCTFontPriorityDynamic](kctfontprioritydynamic.md) — Priority of fonts registered dynamically, not located in a standard location.
- [kCTFontPriorityProcess](kctfontpriorityprocess.md) — Priority of fonts registered for the process.
