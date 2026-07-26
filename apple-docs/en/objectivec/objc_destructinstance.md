---
title: objc_destructInstance
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_destructinstance
source_url: 'https://developer.apple.com/documentation/objectivec/objc_destructinstance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_destructinstance.json'
content_hash: 'sha256:095f3515960f4596'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_destructInstance

<sub>Function</sub>

Destroys an instance of a class without freeing memory and removes any of its associated references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void *objc_destructInstance(id obj);
```

## Discussion

This method does nothing if `obj` is `nil`.

> [!important] Important
> The garbage collector does not call this function. As a result, if you edit this function, you should also edit finalize. That said, Core Foundation and other clients do call this function under garbage collection.

## See Also

### Instantiating Classes

- [class_createInstance](<class_createinstance(____).md>) — Creates an instance of a class, allocating memory for the class in the default malloc memory zone.
- [objc_constructInstance](objc_constructinstance.md) — Creates an instance of a class at the specified location.
