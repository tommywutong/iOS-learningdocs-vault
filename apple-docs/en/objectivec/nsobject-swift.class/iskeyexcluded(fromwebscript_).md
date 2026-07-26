---
title: 'isKeyExcluded(fromWebScript:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/iskeyexcluded(fromwebscript:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/iskeyexcluded(fromwebscript:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/iskeyexcluded%28fromwebscript%3A%29.json'
content_hash: 'sha256:2b7a403fba21c1be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isKeyExcluded(fromWebScript:)

<sub>Type Method</sub>

Returns whether a key should be hidden from the scripting environment.

<sub>macOS</sub>

```swift
class func isKeyExcluded(fromWebScript name: UnsafePointer<CChar>!) -> Bool
```

## Parameters

- `name` — The name of the attribute.

## Return Value

[YES](../yes.md) if the attribute specified by `name` should be hidden from the scripting environment; otherwise, [NO](../no.md).

## Discussion

The default value is [YES](../yes.md).

## See Also

### Getting attributes

- [+ webScriptNameForKey:](<webscriptname(forkey_).md>) — Returns the scripting environment name for an attribute specified by a key.
- [+ webScriptNameForSelector:](<webscriptname(for_).md>) — Returns the scripting environment name for a selector.
- [+ isSelectorExcludedFromWebScript:](<isselectorexcluded(fromwebscript_).md>) — Returns whether a selector should be hidden from the scripting environment.
