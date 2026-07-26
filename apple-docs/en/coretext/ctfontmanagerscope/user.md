---
title: user
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontmanagerscope/user
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagerscope/user'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagerscope/user.json'
content_hash: 'sha256:ad90eb629a6ec383'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFontManagerScope](../ctfontmanagerscope.md)

# user

<sub>Type Property</sub>

The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var user: CTFontManagerScope { get }
```

## See Also

### Constants

- [kCTFontManagerScopeNone](none.md) — No scope is defined.
- [kCTFontManagerScopeProcess](process.md) — The font is available to the current process for the duration of the process unless directly unregistered.
- [kCTFontManagerScopePersistent](persistent.md) — The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.
- [kCTFontManagerScopeSession](session.md) — The font is available to the current user session but won’t be available in subsequent sessions.
