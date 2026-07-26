---
title: objectForWebScript
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/objectforwebscript
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/objectforwebscript'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/objectforwebscript.json'
content_hash: 'sha256:80aeaab219ee5f50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# objectForWebScript

<sub>Instance Property</sub>

Returns an object that exposes the plug-in’s scripting interface.

<sub>macOS</sub>

```swift
var objectForWebScript: Any! { get }
```

## Return Value

An object representing the plug-in’s scripting interface.

## Discussion

The methods of the object are exposed to the script environment. Messages sent to the returned object will be invoked in the scripting environment. See the WebScripting Protocol Reference informal protocol for more details.
