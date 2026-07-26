---
title: finalizeForWebScript()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/finalizeforwebscript()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/finalizeforwebscript()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/finalizeforwebscript%28%29.json'
content_hash: 'sha256:4cceff2eb3115dbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# finalizeForWebScript()

<sub>Instance Method</sub>

Performs cleanup when the scripting environment is reset.

<sub>macOS</sub>

```swift
func finalizeForWebScript()
```

## Discussion

This method is invoked on objects exposed to the scripting environment just before the scripting environment is reset. After invocation, the receiving object will no longer be referenced by the scripting environment. Further references to `WebScriptObject` instances created by the exposed object will be invalid and may produce unpredictable results.
