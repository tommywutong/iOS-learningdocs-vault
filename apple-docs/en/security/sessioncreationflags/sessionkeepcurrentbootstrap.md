---
title: sessionKeepCurrentBootstrap
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sessioncreationflags/sessionkeepcurrentbootstrap
source_url: 'https://developer.apple.com/documentation/security/sessioncreationflags/sessionkeepcurrentbootstrap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sessioncreationflags/sessionkeepcurrentbootstrap.json'
content_hash: 'sha256:03146a6bdcb6104f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SessionCreationFlags](../sessioncreationflags.md)

# sessionKeepCurrentBootstrap

<sub>Type Property</sub>

The caller has allocated sub-bootstrap.

<sub>Mac Catalyst, macOS</sub>

```swift
static var sessionKeepCurrentBootstrap: SessionCreationFlags { get }
```

## Discussion

If you create a subset port on your own, you can force

the [SessionCreate](<../sessioncreate(____).md>) function to use it by passing this flag in the `flags` parameter. However, you can’t supersede a prior call that way; only a single [SessionCreate](<../sessioncreate(____).md>) call is allowed for each session.
