---
title: 'loadSuites(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptsuiteregistry/loadsuites(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/loadsuites(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/loadsuites%28from%3A%29.json'
content_hash: 'sha256:cab191e7b02209ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# loadSuites(from:)

<sub>Instance Method</sub>

Loads the suite definitions in bundle `aBundle`, invoking [- loadSuiteWithDictionary:fromBundle:](<loadsuite(with_from_).md>) for each suite found.

<sub>Mac Catalyst, macOS</sub>

```swift
func loadSuites(from bundle: Bundle)
```

## Discussion

If errors occur while method is parsing a suite-definition file, the method logs error messages to the console.

## See Also

### Loading Suites

- [- loadSuiteWithDictionary:fromBundle:](<loadsuite(with_from_).md>) — Loads the suite definition encapsulated in `dictionary`; previously, this suite definition was parsed from a `.scriptSuite` property list contained in a framework or in `bundle`.
