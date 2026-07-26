---
title: NSKeyValueBindingCreation
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nskeyvaluebindingcreation
source_url: 'https://developer.apple.com/documentation/objectivec/nskeyvaluebindingcreation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nskeyvaluebindingcreation.json'
content_hash: 'sha256:a353c1304b60fd90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# NSKeyValueBindingCreation

<sub>API Collection</sub>

A set of methods that you can use to create and remove bindings between view objects and controllers, or between controllers and model objects.

## Overview

The [NSKeyValueBindingCreation](nskeyvaluebindingcreation.md) informal protocol also provides a means for a view subclass to advertise the bindings that it exposes. The protocol is implemented by [NSObject](nsobject-swift.class.md) and its methods can be overridden by view and controller subclasses.

When a new binding is created it relates the receiver’s binding (for example, a property of the view object) to a property of the observable object specified by a key path. When the value of the specified property of the observable object changes, the receiver is notified using the key-value observing mechanism. A binding also specifies binding options that can further customize how the observing and the observed objects interact.

Bindings are considered to be a property of the object which is bound, and all information related to bindings should be owned by the object. All standard bindings on AppKit objects (views, cells, table columns, controllers) unbind their bindings automatically when they are deallocated, but if you create key-value bindings for other kind of objects, you need to make sure that you remove those bindings before deallocation (observed objects have weak references to their observers, so controllers/model objects might continue referencing and messaging the objects that were bound to them).

Bindings between objects are typically established in Interface Builder using the Bindings inspector. However, there are times it must be done programmatically, such as when establishing a binding between objects in different nib files.

`NSView` subclasses can expose additional key-value-coding/key-value-observing compliant properties as bindings by calling the class method [+ exposeBinding:](<nsobject-swift.class/exposebinding(__).md>) for each of the properties. This is typically done in the class’s `initialize` method. By exposing the bindings that an object supports and creating an Interface Builder palette, you can make instances of your own classes bindable in Interface Builder.

## Topics

### Exposing bindings

- [+ exposeBinding:](<nsobject-swift.class/exposebinding(__).md>) — Exposes the specified `binding`, advertising its availability.
- [exposedBindings](nsobject-swift.class/exposedbindings.md) — Returns an array containing the bindings exposed by the receiver.

### Managing bindings

- [- valueClassForBinding:](<nsobject-swift.class/valueclassforbinding(__).md>) — Returns the class of the value that will be returned for the specified binding.
- [- bind:toObject:withKeyPath:options:](<nsobject-swift.class/bind(__to_withkeypath_options_).md>) — Establishes a binding between a given property of the receiver and the property of a given object specified by a given key path.
- [- optionDescriptionsForBinding:](<nsobject-swift.class/optiondescriptionsforbinding(__).md>) — Returns an array describing the options for the specified binding.
- [- infoForBinding:](<nsobject-swift.class/infoforbinding(__).md>) — Returns a dictionary describing the receiver’s `binding`.
- [NSBindingInfoKey](../appkit/nsbindinginfokey.md)
- [- unbind:](<nsobject-swift.class/unbind(__).md>) — Removes a given binding between the receiver and a controller.
- [NSIsControllerMarker(_:)](<../appkit/nsiscontrollermarker(__).md>) — Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.

### Constants

- [NSBindingName](../appkit/nsbindingname.md) — Values that specify a binding for certain methods.
- [NSBindingOption](../appkit/nsbindingoption.md)
- [Binding Dictionary Keys](binding-dictionary-keys.md) — The following values are used as keys in the dictionary returned by [- infoForBinding:](<nsobject-swift.class/infoforbinding(__).md>)

## See Also

### Related Documentation

- [Cocoa Bindings Reference](https://developer.apple.com/library/archive/documentation/Cocoa/Reference/CocoaBindingsRef/CocoaBindingsRef.html#//apple_ref/doc/uid/10000189i)
- [Cocoa Bindings Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167i)

### Key-Value Coding

- [NSKeyValueCoding](nskeyvaluecoding.md) — A mechanism by which you can access the properties of an object indirectly by name or key.
- [NSScriptKeyValueCoding](nsscriptkeyvaluecoding.md) — A collection of methods that provide additional capabilities for working with key-value coding.
- [NSScriptKeyValueCoding Exception Names](nsscriptkeyvaluecoding-exception-names.md) — Exceptions raised by key-value coding methods.
