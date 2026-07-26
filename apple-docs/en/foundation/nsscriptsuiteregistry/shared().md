---
title: shared()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptsuiteregistry/shared()
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/shared()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/shared%28%29.json'
content_hash: 'sha256:670061a68527dd25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# shared()

<sub>Type Method</sub>

Returns the single, shared instance of `NSScriptSuiteRegistry`, creating it first if it doesn’t exist.

<sub>Mac Catalyst, macOS</sub>

```swift
class func shared() -> NSScriptSuiteRegistry
```

## Discussion

If it creates an instance, and if the application provides scriptability information in the script suite format, the method loads suite definitions in all frameworks and other bundles that the application currently imports or includes; if information is provided in the sdef format, the method loads information only from the specified sdef file. If in reading scriptability information an exception is `raised` because of parsing errors, it handles the exception by printing a line of information to the console.

## See Also

### Related Documentation

- [- loadSuiteWithDictionary:fromBundle:](<loadsuite(with_from_).md>) — Loads the suite definition encapsulated in `dictionary`; previously, this suite definition was parsed from a `.scriptSuite` property list contained in a framework or in `bundle`.

### Getting and Setting the Shared Instance

- [+ setSharedScriptSuiteRegistry:](<setshared(__).md>) — Sets the single, shared instance of `NSScriptSuiteRegistry` to `registry`.
