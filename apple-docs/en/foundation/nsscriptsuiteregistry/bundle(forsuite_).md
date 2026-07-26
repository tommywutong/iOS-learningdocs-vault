---
title: 'bundle(forSuite:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptsuiteregistry/bundle(forsuite:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/bundle(forsuite:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/bundle%28forsuite%3A%29.json'
content_hash: 'sha256:c9ab9c96a1729452'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# bundle(forSuite:)

<sub>Instance Method</sub>

Returns the bundle containing the suite-definition property list (extension `.scriptSuite`) identified by `suiteName`.

<sub>Mac Catalyst, macOS</sub>

```swift
func bundle(forSuite suiteName: String) -> Bundle?
```

## See Also

### Getting Other Suite Information

- [- aeteResource:](<aeteresource(__).md>) — Returns an `NSData` object that contains data in `'aete'` resource format describing the scriptability information currently known to the application.
- [- appleEventCodeForSuite:](<appleeventcode(forsuite_).md>) — Returns the Apple event code associated with the suite named `suiteName`, such as `‘core’` for the Core suite.
