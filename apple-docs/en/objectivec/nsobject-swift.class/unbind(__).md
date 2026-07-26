---
title: 'unbind(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/unbind(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/unbind(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/unbind%28_%3A%29.json'
content_hash: 'sha256:cef5734e54ec1fd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# unbind(_:)

<sub>Instance Method</sub>

Removes a given binding between the receiver and a controller.

<sub>macOS</sub>

```swift
func unbind(_ binding: NSBindingName)
```

## Parameters

- `binding` — The name of a binding.

## See Also

### Managing bindings

- [- valueClassForBinding:](<valueclassforbinding(__).md>) — Returns the class of the value that will be returned for the specified binding.
- [- bind:toObject:withKeyPath:options:](<bind(__to_withkeypath_options_).md>) — Establishes a binding between a given property of the receiver and the property of a given object specified by a given key path.
- [- optionDescriptionsForBinding:](<optiondescriptionsforbinding(__).md>) — Returns an array describing the options for the specified binding.
- [- infoForBinding:](<infoforbinding(__).md>) — Returns a dictionary describing the receiver’s `binding`.
- [NSBindingInfoKey](../../appkit/nsbindinginfokey.md)
- [NSIsControllerMarker(_:)](<../../appkit/nsiscontrollermarker(__).md>) — Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.
