---
title: kCTFontPriorityProcess
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontpriorityprocess
source_url: 'https://developer.apple.com/documentation/coretext/kctfontpriorityprocess'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontpriorityprocess.json'
content_hash: 'sha256:b55b194faf0e6943'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontPriorityProcess

<sub>Global Variable</sub>

Priority of fonts registered for the process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCTFontPriorityProcess: Int { get }
```

## Discussion

Fonts registered for the process are in [kCTFontManagerScopeProcess](ctfontmanagerscope/process.md).

## See Also

### Font Priority

- [kCTFontPrioritySystem](kctfontprioritysystem.md) — Priority of system fonts.
- [kCTFontPriorityNetwork](kctfontprioritynetwork.md) — Priority of network fonts.
- [kCTFontPriorityComputer](kctfontprioritycomputer.md) — Priority of computer local fonts.
- [kCTFontPriorityUser](kctfontpriorityuser.md) — Priority of local fonts.
- [kCTFontPriorityDynamic](kctfontprioritydynamic.md) — Priority of fonts registered dynamically, not located in a standard location.
