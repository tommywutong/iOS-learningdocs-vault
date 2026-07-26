---
title: 'setShared(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptsuiteregistry/setshared(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/setshared(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/setshared%28_%3A%29.json'
content_hash: 'sha256:fb3783c0a8c4c75d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# setShared(_:)

<sub>Type Method</sub>

Sets the single, shared instance of `NSScriptSuiteRegistry` to `registry`.

<sub>Mac Catalyst, macOS</sub>

```swift
class func setShared(_ registry: NSScriptSuiteRegistry)
```

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

### Getting and Setting the Shared Instance

- [+ sharedScriptSuiteRegistry](<shared().md>) — Returns the single, shared instance of `NSScriptSuiteRegistry`, creating it first if it doesn’t exist.
