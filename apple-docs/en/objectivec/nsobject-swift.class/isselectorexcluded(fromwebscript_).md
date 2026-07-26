---
title: 'isSelectorExcluded(fromWebScript:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/isselectorexcluded(fromwebscript:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isselectorexcluded(fromwebscript:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/isselectorexcluded%28fromwebscript%3A%29.json'
content_hash: 'sha256:a3ea2200609712ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isSelectorExcluded(fromWebScript:)

<sub>Type Method</sub>

Returns whether a selector should be hidden from the scripting environment.

<sub>macOS</sub>

```swift
class func isSelectorExcluded(fromWebScript selector: Selector!) -> Bool
```

## Parameters

- `selector` — The selector.

## Return Value

[YES](../yes.md) if the selector specified by `aSelector` should be hidden from the scripting environment; otherwise, [NO](../no.md).

## Discussion

Only methods with valid parameters and return types are exported to the WebKit JavaScript environment. The valid types are Objective-C objects and scalars. The default value is [YES](../yes.md).

## See Also

### Getting attributes

- [+ webScriptNameForKey:](<webscriptname(forkey_).md>) — Returns the scripting environment name for an attribute specified by a key.
- [+ webScriptNameForSelector:](<webscriptname(for_).md>) — Returns the scripting environment name for a selector.
- [+ isKeyExcludedFromWebScript:](<iskeyexcluded(fromwebscript_).md>) — Returns whether a key should be hidden from the scripting environment.
