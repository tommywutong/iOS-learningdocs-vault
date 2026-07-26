---
title: exposedBindings
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/exposedbindings
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/exposedbindings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/exposedbindings.json'
content_hash: 'sha256:654db8417a60320f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# exposedBindings

<sub>Instance Property</sub>

Returns an array containing the bindings exposed by the receiver.

<sub>macOS</sub>

```swift
var exposedBindings: [NSBindingName] { get }
```

## Return Value

An array containing the bindings exposed by the receiver.

## Discussion

A subclass can override this method to remove bindings that are exposed by a superclass that are not appropriate for the subclass.

## See Also

### Exposing bindings

- [+ exposeBinding:](<exposebinding(__).md>) — Exposes the specified `binding`, advertising its availability.
