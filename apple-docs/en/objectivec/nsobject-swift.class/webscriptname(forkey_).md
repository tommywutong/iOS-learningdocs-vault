---
title: 'webScriptName(forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/webscriptname(forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webscriptname(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webscriptname%28forkey%3A%29.json'
content_hash: 'sha256:9eb6488f6f44b769'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webScriptName(forKey:)

<sub>Type Method</sub>

Returns the scripting environment name for an attribute specified by a key.

<sub>macOS</sub>

```swift
class func webScriptName(forKey name: UnsafePointer<CChar>!) -> String!
```

## Parameters

- `name` — The name of the attribute.

## Return Value

The name used to represent the attribute in the scripting environment.

## See Also

### Getting attributes

- [+ webScriptNameForSelector:](<webscriptname(for_).md>) — Returns the scripting environment name for a selector.
- [+ isSelectorExcludedFromWebScript:](<isselectorexcluded(fromwebscript_).md>) — Returns whether a selector should be hidden from the scripting environment.
- [+ isKeyExcludedFromWebScript:](<iskeyexcluded(fromwebscript_).md>) — Returns whether a key should be hidden from the scripting environment.
