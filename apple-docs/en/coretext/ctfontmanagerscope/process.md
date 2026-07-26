---
title: CTFontManagerScope.process
framework: Core Text
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontmanagerscope/process
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagerscope/process'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagerscope/process.json'
content_hash: 'sha256:1a6f8367662f4776'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFontManagerScope](../ctfontmanagerscope.md)

# CTFontManagerScope.process

<sub>Case</sub>

The font is available to the current process for the duration of the process unless directly unregistered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case process
```

## See Also

### Constants

- [kCTFontManagerScopeNone](none.md) — No scope is defined.
- [kCTFontManagerScopePersistent](persistent.md) — The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.
- [kCTFontManagerScopeSession](session.md) — The font is available to the current user session but won’t be available in subsequent sessions.
- [kCTFontManagerScopeUser](user.md) — The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.
