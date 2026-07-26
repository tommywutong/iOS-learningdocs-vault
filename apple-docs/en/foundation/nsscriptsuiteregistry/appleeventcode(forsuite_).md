---
title: 'appleEventCode(forSuite:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptsuiteregistry/appleeventcode(forsuite:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/appleeventcode(forsuite:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/appleeventcode%28forsuite%3A%29.json'
content_hash: 'sha256:efae4b608ee76697'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# appleEventCode(forSuite:)

<sub>Instance Method</sub>

Returns the Apple event code associated with the suite named `suiteName`, such as `‘core’` for the Core suite.

<sub>Mac Catalyst, macOS</sub>

```swift
func appleEventCode(forSuite suiteName: String) -> FourCharCode
```

## See Also

### Related Documentation

- [- suiteForAppleEventCode:](<suite(forappleeventcode_).md>) — Returns the name of the suite definition associated with the given four-character Apple event code, `code`.

### Getting Other Suite Information

- [- aeteResource:](<aeteresource(__).md>) — Returns an `NSData` object that contains data in `'aete'` resource format describing the scriptability information currently known to the application.
- [- bundleForSuite:](<bundle(forsuite_).md>) — Returns the bundle containing the suite-definition property list (extension `.scriptSuite`) identified by `suiteName`.
