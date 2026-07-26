---
title: kCTFontPriorityDynamic
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontprioritydynamic
source_url: 'https://developer.apple.com/documentation/coretext/kctfontprioritydynamic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontprioritydynamic.json'
content_hash: 'sha256:5abe6f6593acc515'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontPriorityDynamic

<sub>Global Variable</sub>

Priority of fonts registered dynamically, not located in a standard location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCTFontPriorityDynamic: Int { get }
```

## Discussion

Dynamic fonts are either in [kCTFontManagerScopeUser](ctfontmanagerscope/user.md) or [kCTFontManagerScopeSession](ctfontmanagerscope/session.md).

## See Also

### Font Priority

- [kCTFontPrioritySystem](kctfontprioritysystem.md) — Priority of system fonts.
- [kCTFontPriorityNetwork](kctfontprioritynetwork.md) — Priority of network fonts.
- [kCTFontPriorityComputer](kctfontprioritycomputer.md) — Priority of computer local fonts.
- [kCTFontPriorityUser](kctfontpriorityuser.md) — Priority of local fonts.
- [kCTFontPriorityProcess](kctfontpriorityprocess.md) — Priority of fonts registered for the process.
