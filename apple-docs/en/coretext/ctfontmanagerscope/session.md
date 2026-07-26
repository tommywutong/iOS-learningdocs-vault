---
title: CTFontManagerScope.session
framework: Core Text
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontmanagerscope/session
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagerscope/session'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagerscope/session.json'
content_hash: 'sha256:e07f5042990f9f2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFontManagerScope](../ctfontmanagerscope.md)

# CTFontManagerScope.session

<sub>Case</sub>

The font is available to the current user session but won’t be available in subsequent sessions.

<sub>macOS</sub>

```swift
case session
```

## See Also

### Constants

- [kCTFontManagerScopeNone](none.md) — No scope is defined.
- [kCTFontManagerScopeProcess](process.md) — The font is available to the current process for the duration of the process unless directly unregistered.
- [kCTFontManagerScopePersistent](persistent.md) — The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.
- [kCTFontManagerScopeUser](user.md) — The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.
