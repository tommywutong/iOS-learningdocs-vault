---
title: 'suite(forAppleEventCode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptsuiteregistry/suite(forappleeventcode:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/suite(forappleeventcode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/suite%28forappleeventcode%3A%29.json'
content_hash: 'sha256:676a8c55b40f0745'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# suite(forAppleEventCode:)

<sub>Instance Method</sub>

Returns the name of the suite definition associated with the given four-character Apple event code, `code`.

<sub>Mac Catalyst, macOS</sub>

```swift
func suite(forAppleEventCode appleEventCode: FourCharCode) -> String?
```

## See Also

### Getting Suite Information

- [suiteNames](suitenames.md) — Returns the names of the suite definitions currently loaded by the application.
