---
title: 'bind(_:to:withKeyPath:options:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/bind(_:to:withkeypath:options:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/bind(_:to:withkeypath:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/bind%28_%3Ato%3Awithkeypath%3Aoptions%3A%29.json'
content_hash: 'sha256:156f10fcaf707c2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# bind(_:to:withKeyPath:options:)

<sub>Instance Method</sub>

Establishes a binding between a given property of the receiver and the property of a given object specified by a given key path.

<sub>macOS</sub>

```swift
func bind(_ binding: NSBindingName, to observable: Any, withKeyPath keyPath: String, options: [NSBindingOption : Any]? = nil)
```

## Parameters

- `binding` — The key path for a property of the receiver previously exposed using the [+ exposeBinding:](<exposebinding(__).md>) method.

- `observable` — The bound-to object.

- `keyPath` — A key path to a property reachable from `observableController`. The elements in the path must be key-value observing compliant (see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i)).

- `options` — A dictionary containing options for the binding, such as placeholder objects or an `NSValueTransformer` identifier as described in Constants. This value is optional—pass `nil` to specify no options.

## See Also

### Managing bindings

- [- valueClassForBinding:](<valueclassforbinding(__).md>) — Returns the class of the value that will be returned for the specified binding.
- [- optionDescriptionsForBinding:](<optiondescriptionsforbinding(__).md>) — Returns an array describing the options for the specified binding.
- [- infoForBinding:](<infoforbinding(__).md>) — Returns a dictionary describing the receiver’s `binding`.
- [NSBindingInfoKey](../../appkit/nsbindinginfokey.md)
- [- unbind:](<unbind(__).md>) — Removes a given binding between the receiver and a controller.
- [NSIsControllerMarker(_:)](<../../appkit/nsiscontrollermarker(__).md>) — Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.
