---
title: 'invokeUndefinedMethod(fromWebScript:withArguments:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/invokeundefinedmethod(fromwebscript:witharguments:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/invokeundefinedmethod(fromwebscript:witharguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/invokeundefinedmethod%28fromwebscript%3Awitharguments%3A%29.json'
content_hash: 'sha256:e8d47f3b715ff541'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# invokeUndefinedMethod(fromWebScript:withArguments:)

<sub>Instance Method</sub>

Handles undefined method invocation from the scripting environment.

<sub>macOS</sub>

```swift
func invokeUndefinedMethod(fromWebScript name: String!, withArguments arguments: [Any]!) -> Any!
```

## Parameters

- `name` — The name of the undefined method.

- `arguments` — The arguments passed to the undefined method.

## Return Value

The result of invoking the undefined method.

## Discussion

This method is invoked when a script attempts to invoke a method not directly exported to the scripting environment. You should return the result of the invocation, converted appropriately for the scripting environment.

## See Also

### Invoking methods

- [- invokeDefaultMethodWithArguments:](<invokedefaultmethod(witharguments_).md>) — Executes when a script attempts to invoke a method on an exposed object directly.
