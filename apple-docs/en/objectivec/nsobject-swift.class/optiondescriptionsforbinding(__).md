---
title: 'optionDescriptionsForBinding(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/optiondescriptionsforbinding(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/optiondescriptionsforbinding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/optiondescriptionsforbinding%28_%3A%29.json'
content_hash: 'sha256:f4099ae0f68c7369'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# optionDescriptionsForBinding(_:)

<sub>Instance Method</sub>

Returns an array describing the options for the specified binding.

<sub>macOS</sub>

```swift
func optionDescriptionsForBinding(_ binding: NSBindingName) -> [NSAttributeDescription]
```

## Parameters

- `binding` — The name of a binding

## Return Value

Returns an array of [NSAttributeDescription](../../coredata/nsattributedescription.md) that describe the options for `binding`.

## Discussion

The [NSAttributeDescription](../../coredata/nsattributedescription.md) instances in the array are used by Interface Builder to build the options editor user interface of the bindings inspector.

- The option name displayed for the option in the bindings inspector is based on the value of the [NSAttributeDescription](../../coredata/nsattributedescription.md) method [name](../../coredata/nspropertydescription/name.md).
- The type of editor displayed for the option in the bindings inspector is based on the value of the  [NSAttributeDescription](../../coredata/nsattributedescription.md) method [attributeType](../../coredata/nsattributedescription/attributetype-swift.property.md).
- The default value displayed in the bindings inspector for the option is based on the value of the [NSAttributeDescription](../../coredata/nsattributedescription.md) method [defaultValue](../../coredata/nsattributedescription/defaultvalue.md).

## See Also

### Managing bindings

- [- valueClassForBinding:](<valueclassforbinding(__).md>) — Returns the class of the value that will be returned for the specified binding.
- [- bind:toObject:withKeyPath:options:](<bind(__to_withkeypath_options_).md>) — Establishes a binding between a given property of the receiver and the property of a given object specified by a given key path.
- [- infoForBinding:](<infoforbinding(__).md>) — Returns a dictionary describing the receiver’s `binding`.
- [NSBindingInfoKey](../../appkit/nsbindinginfokey.md)
- [- unbind:](<unbind(__).md>) — Removes a given binding between the receiver and a controller.
- [NSIsControllerMarker(_:)](<../../appkit/nsiscontrollermarker(__).md>) — Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.
