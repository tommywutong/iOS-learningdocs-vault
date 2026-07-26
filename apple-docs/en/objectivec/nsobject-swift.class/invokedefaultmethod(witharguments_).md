---
title: 'invokeDefaultMethod(withArguments:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/invokedefaultmethod(witharguments:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/invokedefaultmethod(witharguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/invokedefaultmethod%28witharguments%3A%29.json'
content_hash: 'sha256:ef10b367c6f1df4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# invokeDefaultMethod(withArguments:)

<sub>Instance Method</sub>

Executes when a script attempts to invoke a method on an exposed object directly.

<sub>macOS</sub>

```swift
func invokeDefaultMethod(withArguments arguments: [Any]!) -> Any!
```

## Parameters

- `arguments` — The arguments to be passed to the default method.

## Return Value

The result of invoking the default method.

## See Also

### Invoking methods

- [- invokeUndefinedMethodFromWebScript:withArguments:](<invokeundefinedmethod(fromwebscript_witharguments_).md>) — Handles undefined method invocation from the scripting environment.
