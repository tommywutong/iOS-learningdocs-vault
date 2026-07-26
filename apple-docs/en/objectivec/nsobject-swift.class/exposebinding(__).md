---
title: 'exposeBinding(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/exposebinding(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/exposebinding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/exposebinding%28_%3A%29.json'
content_hash: 'sha256:0152f5ede78b518d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# exposeBinding(_:)

<sub>Type Method</sub>

Exposes the specified `binding`, advertising its availability.

<sub>macOS</sub>

```swift
class func exposeBinding(_ binding: NSBindingName)
```

## Parameters

- `binding` — The key path for the property to be exposed.

## Discussion

The bound property will be accessed using key-value-coding compliant methods. This method is typically invoked in the class’s `initialize` implementation.

Bindings exposed using `exposeBinding` will be exposed automatically in [exposedBindings](exposedbindings.md) unless that method explicitly filters them out, for example in subclasses.

## See Also

### Exposing bindings

- [exposedBindings](exposedbindings.md) — Returns an array containing the bindings exposed by the receiver.
