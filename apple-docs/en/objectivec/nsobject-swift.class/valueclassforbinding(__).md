---
title: 'valueClassForBinding(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/valueclassforbinding(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/valueclassforbinding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/valueclassforbinding%28_%3A%29.json'
content_hash: 'sha256:575494828fd222df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# valueClassForBinding(_:)

<sub>Instance Method</sub>

Returns the class of the value that will be returned for the specified binding.

<sub>macOS</sub>

```swift
func valueClassForBinding(_ binding: NSBindingName) -> AnyClass?
```

## Parameters

- `binding` — The name of a binding.

## Return Value

The class of the value that will be returned for `binding`.

## Discussion

This method is used by Interface Builder to determine the appropriate transformers for a binding.

Implementation of this method is optional.

## See Also

### Managing bindings

- [- bind:toObject:withKeyPath:options:](<bind(__to_withkeypath_options_).md>) — Establishes a binding between a given property of the receiver and the property of a given object specified by a given key path.
- [- optionDescriptionsForBinding:](<optiondescriptionsforbinding(__).md>) — Returns an array describing the options for the specified binding.
- [- infoForBinding:](<infoforbinding(__).md>) — Returns a dictionary describing the receiver’s `binding`.
- [NSBindingInfoKey](../../appkit/nsbindinginfokey.md)
- [- unbind:](<unbind(__).md>) — Removes a given binding between the receiver and a controller.
- [NSIsControllerMarker(_:)](<../../appkit/nsiscontrollermarker(__).md>) — Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.
