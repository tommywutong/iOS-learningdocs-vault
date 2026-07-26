---
title: 'aeteResource(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptsuiteregistry/aeteresource(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/aeteresource(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/aeteresource%28_%3A%29.json'
content_hash: 'sha256:5622c055ea7665d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# aeteResource(_:)

<sub>Instance Method</sub>

Returns an `NSData` object that contains data in `'aete'` resource format describing the scriptability information currently known to the application.

<sub>Mac Catalyst, macOS</sub>

```swift
func aeteResource(_ languageName: String) -> Data?
```

## Discussion

This method is typically invoked to implement the `get aete` Apple event for an application that provides scriptability information in the script suite format. The `languageName` argument is the name of a language for which a localized resource directory (such as `English.lproj`) exists. This language indication specifies the set of `.scriptTerminology` files to be used to generate the data. `NSScriptSuiteRegistry` does not create an `'aete'` resource unless this method is called.

## See Also

### Getting Other Suite Information

- [- appleEventCodeForSuite:](<appleeventcode(forsuite_).md>) — Returns the Apple event code associated with the suite named `suiteName`, such as `‘core’` for the Core suite.
- [- bundleForSuite:](<bundle(forsuite_).md>) — Returns the bundle containing the suite-definition property list (extension `.scriptSuite`) identified by `suiteName`.
