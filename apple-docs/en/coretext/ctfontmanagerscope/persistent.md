---
title: CTFontManagerScope.persistent
framework: Core Text
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontmanagerscope/persistent
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagerscope/persistent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagerscope/persistent.json'
content_hash: 'sha256:a7b2dd4645dd453a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFontManagerScope](../ctfontmanagerscope.md)

# CTFontManagerScope.persistent

<sub>Case</sub>

The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case persistent
```

## See Also

### Constants

- [kCTFontManagerScopeNone](none.md) — No scope is defined.
- [kCTFontManagerScopeProcess](process.md) — The font is available to the current process for the duration of the process unless directly unregistered.
- [kCTFontManagerScopeSession](session.md) — The font is available to the current user session but won’t be available in subsequent sessions.
- [kCTFontManagerScopeUser](user.md) — The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.
