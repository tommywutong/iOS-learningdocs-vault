---
title: 'webScriptName(for:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/webscriptname(for:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webscriptname(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webscriptname%28for%3A%29.json'
content_hash: 'sha256:32ce4609256a9af9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webScriptName(for:)

<sub>Type Method</sub>

Returns the scripting environment name for a selector.

<sub>macOS</sub>

```swift
class func webScriptName(for selector: Selector!) -> String!
```

## Parameters

- `selector` — The selector.

## Return Value

The name used to represent the selector in the scripting environment.

## Discussion

It is your responsibility to ensure that the returned name is unique to the script invoking this method. If this method returns `nil` or you do not implement it, the default name for the selector is constructed as follows:

- A colon (”:”) in the Objective-C selector is replaced by an underscore (”_”).
- An underscore in the Objective-C selector is prefixed with a dollar sign (”$”).
- A dollar sign in the Objective-C selector is prefixed with another dollar sign.

The following table shows examples of how the default name is constructed:

| Objective-C selector | Default script name for selector |
|---|---|
| `setFlag:` | `setFlag_` |
| `setFlag:forKey:withAttributes:` | `setFlag_forKey_withAttributes_` |
| `propertiesForExample_Object:` | `propertiesForExample$_Object_` |
| `set_$_forKey:withDictionary:` | `set$_$$_$_forKey_withDictionary_` |

Since the default construction for a method name can be confusing depending on its Objective-C name, you should implement this method and return a more human-readable name.

## See Also

### Getting attributes

- [+ webScriptNameForKey:](<webscriptname(forkey_).md>) — Returns the scripting environment name for an attribute specified by a key.
- [+ isSelectorExcludedFromWebScript:](<isselectorexcluded(fromwebscript_).md>) — Returns whether a selector should be hidden from the scripting environment.
- [+ isKeyExcludedFromWebScript:](<iskeyexcluded(fromwebscript_).md>) — Returns whether a key should be hidden from the scripting environment.
