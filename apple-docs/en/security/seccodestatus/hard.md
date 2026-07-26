---
title: hard
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccodestatus/hard
source_url: 'https://developer.apple.com/documentation/security/seccodestatus/hard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodestatus/hard.json'
content_hash: 'sha256:b91867b95737b207'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecCodeStatus](../seccodestatus.md)

# hard

<sub>Type Property</sub>

The code prefers to be denied access to resources if gaining access would invalidate it.

<sub>Mac Catalyst, macOS</sub>

```swift
static var hard: SecCodeStatus { get }
```

## Discussion

This bit can not be cleared on running code; it can only be set. It is undefined whether code that has the hard flag set but that starts out with the valid bit cleared (that is, it’s already invalid) will still be denied access to a resource that would invalidate it if it were still valid. That is, the code may or may not get access to such a resource while being invalid.
