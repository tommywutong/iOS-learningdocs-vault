---
title: Objective-C Runtime
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objective-c-runtime
source_url: 'https://developer.apple.com/documentation/objectivec/objective-c-runtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objective-c-runtime.json'
content_hash: 'sha256:61df2a7e2cf3522c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# Objective-C Runtime

<sub>API Collection</sub>

Describes the macOS Objective-C runtime library support functions and data structures.

## Overview

The Objective-C runtime is a runtime library that provides support for the dynamic properties of the Objective-C language, and as such is linked to by all Objective-C apps. Objective-C runtime library support functions are implemented in the shared library found at `/usr/lib/libobjc.A.dylib`.

You typically don’t need to use the Objective-C runtime library directly when programming in Objective-C. This API is useful primarily for developing bridge layers between Objective-C and other languages, or for low-level debugging.

The macOS implementation of the Objective-C runtime library is unique to the Mac. For other platforms, the GNU Compiler Collection provides a different implementation with a similar API. This document covers only the macOS implementation.

The low-level Objective-C runtime API is significantly updated in OS X version 10.5. Many functions and all existing data structures are replaced with new functions. The old functions and structures are deprecated in 32-bit and absent in 64-bit mode. The API constrains several values to 32-bit ints even in 64-bit mode—class count, protocol count, methods per class, ivars per class, arguments per method, sizeof(all arguments) per method, and class version number. In addition, the new Objective-C ABI (not described here) further constrains `sizeof(anInstance)` to 32 bits, and three other values to 24 bits—methods per class, ivars per class, and sizeof(a single ivar). Finally, the obsolete `NXHashTable` and `NXMapTable` are limited to 4 billion items.

> [!note] String encoding
> All `char *` in the runtime API should be considered to have UTF-8 encoding.

“Deprecated” below means “deprecated in OS X version 10.5 for 32-bit code, and disallowed for 64-bit code.”

### Who Should Read This Document

The document is intended for readers who might be interested in learning about the Objective-C runtime.

Because this isn’t a document about C, it assumes some prior acquaintance with that language. However, it doesn’t have to be an extensive acquaintance.

## Topics

### Working with Classes

- [class_getName](<class_getname(__).md>) — Returns the name of a class.
- [class_getSuperclass](<class_getsuperclass(__).md>) — Returns the superclass of a class.
- [class_setSuperclass](<class_setsuperclass(____).md>) — Sets the superclass of a given class. _(deprecated)_
- [class_isMetaClass](<class_ismetaclass(__).md>) — Returns a Boolean value that indicates whether a class object is a metaclass.
- [class_getInstanceSize](<class_getinstancesize(__).md>) — Returns the size of instances of a class.
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — Returns the `Ivar` for a specified instance variable of a given class.
- [class_getClassVariable](<class_getclassvariable(____).md>) — Returns the `Ivar` for a specified class variable of a given class.
- [class_addIvar](<class_addivar(__________).md>) — Adds a new instance variable to a class.
- [class_copyIvarList](<class_copyivarlist(____).md>) — Describes the instance variables declared by a class.
- [class_getIvarLayout](<class_getivarlayout(__).md>) — Returns a description of the `Ivar` layout for a given class.
- [class_setIvarLayout](<class_setivarlayout(____).md>) — Sets the `Ivar` layout for a given class.
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — Returns a description of the layout of weak `Ivar`s for a given class.
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — Sets the layout for weak `Ivar`s for a given class.
- [class_getProperty](<class_getproperty(____).md>) — Returns a property with a given name of a given class.
- [class_copyPropertyList](<class_copypropertylist(____).md>) — Describes the properties declared by a class.
- [class_addMethod](<class_addmethod(________).md>) — Adds a new method to a class with a given name and implementation.
- [class_getInstanceMethod](<class_getinstancemethod(____).md>) — Returns a specified instance method for a given class.
- [class_getClassMethod](<class_getclassmethod(____).md>) — Returns a pointer to the data structure describing a given class method for a given class.
- [class_copyMethodList](<class_copymethodlist(____).md>) — Describes the instance methods implemented by a class.
- [class_replaceMethod](<class_replacemethod(________).md>) — Replaces the implementation of a method for a given class.
- [class_getMethodImplementation](<class_getmethodimplementation(____).md>) — Returns the function pointer that would be called if a particular message were sent to an instance of a class.
- [class_getMethodImplementation_stret](<class_getmethodimplementation_stret(____).md>) — Returns the function pointer that would be called if a particular message were sent to an instance of a class.
- [class_respondsToSelector](<class_respondstoselector(____).md>) — Returns a Boolean value that indicates whether instances of a class respond to a particular selector.
- [class_addProtocol](<class_addprotocol(____).md>) — Adds a protocol to a class.
- [class_addProperty](<class_addproperty(________).md>) — Adds a property to a class.
- [class_replaceProperty](<class_replaceproperty(________).md>) — Replace a property of a class.
- [class_conformsToProtocol](<class_conformstoprotocol(____).md>) — Returns a Boolean value that indicates whether a class conforms to a given protocol.
- [class_copyProtocolList](<class_copyprotocollist(____).md>) — Describes the protocols adopted by a class.
- [class_getVersion](<class_getversion(__).md>) — Returns the version number of a class definition.
- [class_setVersion](<class_setversion(____).md>) — Sets the version number of a class definition.
- [objc_setFutureClass](1808430-objc_setfutureclass.md) — Used by CoreFoundation’s toll-free bridging.

### Adding Classes

- [objc_allocateClassPair](<objc_allocateclasspair(______).md>) — Creates a new class and metaclass.
- [objc_disposeClassPair](<objc_disposeclasspair(__).md>) — Destroys a class and its associated metaclass.
- [objc_registerClassPair](<objc_registerclasspair(__).md>) — Registers a class that was allocated using [objc_allocateClassPair](<objc_allocateclasspair(______).md>).
- [objc_duplicateClass](<objc_duplicateclass(______).md>) — Used by Foundation’s Key-Value Observing.

### Instantiating Classes

- [class_createInstance](<class_createinstance(____).md>) — Creates an instance of a class, allocating memory for the class in the default malloc memory zone.

### Working with Instances

- [object_getIndexedIvars](<object_getindexedivars(__).md>) — Returns a pointer to any extra bytes allocated with a instance given object.
- [object_getIvar](<object_getivar(____).md>) — Reads the value of an instance variable in an object.
- [object_setIvar](<object_setivar(______).md>) — Sets the value of an instance variable in an object.
- [object_getClassName](<object_getclassname(__).md>) — Returns the class name of a given object.
- [object_getClass](<object_getclass(__).md>) — Returns the class of an object.
- [object_setClass](<object_setclass(____).md>) — Sets the class of an object.

### Obtaining Class Definitions

- [objc_getClassList](<objc_getclasslist(____).md>) — Obtains the list of registered class definitions.
- [objc_copyClassList](<objc_copyclasslist(__).md>) — Creates and returns a list of pointers to all registered class definitions.
- [objc_lookUpClass](<objc_lookupclass(__).md>) — Returns the class definition of a specified class.
- [objc_getClass](<objc_getclass(__).md>) — Returns the class definition of a specified class.
- [objc_getRequiredClass](<objc_getrequiredclass(__).md>) — Returns the class definition of a specified class.
- [objc_getMetaClass](<objc_getmetaclass(__).md>) — Returns the metaclass definition of a specified class.

### Working with Instance Variables

- [ivar_getName](<ivar_getname(__).md>) — Returns the name of an instance variable.
- [ivar_getTypeEncoding](<ivar_gettypeencoding(__).md>) — Returns the type string of an instance variable.
- [ivar_getOffset](<ivar_getoffset(__).md>) — Returns the offset of an instance variable.

### Associative References

- [objc_setAssociatedObject](<objc_setassociatedobject(________).md>) — Sets an associated value for a given object using a given key and association policy.
- [objc_getAssociatedObject](<objc_getassociatedobject(____).md>) — Returns the value associated with a given object for a given key.
- [objc_removeAssociatedObjects](<objc_removeassociatedobjects(__).md>) — Removes all associations for a given object.

### Working with Methods

- [method_getName](<method_getname(__).md>) — Returns the name of a method.
- [method_getImplementation](<method_getimplementation(__).md>) — Returns the implementation of a method.
- [method_getTypeEncoding](<method_gettypeencoding(__).md>) — Returns a string describing a method’s parameter and return types.
- [method_copyReturnType](<method_copyreturntype(__).md>) — Returns a string describing a method’s return type.
- [method_copyArgumentType](<method_copyargumenttype(____).md>) — Returns a string describing a single parameter type of a method.
- [method_getReturnType](<method_getreturntype(______).md>) — Returns by reference a string describing a method’s return type.
- [method_getNumberOfArguments](<method_getnumberofarguments(__).md>) — Returns the number of arguments accepted by a method.
- [method_getArgumentType](<method_getargumenttype(________).md>) — Returns by reference a string describing a single parameter type of a method.
- [method_getDescription](<method_getdescription(__).md>) — Returns a method description structure for a specified method. _(deprecated)_
- [method_setImplementation](<method_setimplementation(____).md>) — Sets the implementation of a method.
- [method_exchangeImplementations](<method_exchangeimplementations(____).md>) — Exchanges the implementations of two methods.

### Working with Libraries

- [objc_copyImageNames](<objc_copyimagenames(__).md>) — Returns the names of all the loaded Objective-C frameworks and dynamic libraries.
- [class_getImageName](<class_getimagename(__).md>) — Returns the name of the dynamic library a class originated from.
- [objc_copyClassNamesForImage](<objc_copyclassnamesforimage(____).md>) — Returns the names of all the classes within a specified library or framework.

### Working with Selectors

- [sel_getName](<sel_getname(__).md>) — Returns the name of the method specified by a given selector.
- [sel_registerName](<sel_registername(__).md>) — Registers a method with the Objective-C runtime system, maps the method name to a selector, and returns the selector value.
- [sel_getUid](<sel_getuid(__).md>) — Registers a method name with the Objective-C runtime system.
- [sel_isEqual](<sel_isequal(____).md>) — Returns a Boolean value that indicates whether two selectors are equal.

### Working with Protocols

- [objc_getProtocol](<objc_getprotocol(__).md>) — Returns a specified protocol.
- [objc_copyProtocolList](<objc_copyprotocollist(__).md>) — Returns an array of all the protocols known to the runtime.
- [objc_allocateProtocol](<objc_allocateprotocol(__).md>) — Creates a new protocol instance.
- [objc_registerProtocol](<objc_registerprotocol(__).md>) — Registers a newly created protocol with the Objective-C runtime.
- [protocol_addMethodDescription](<protocol_addmethoddescription(__________).md>) — Adds a method to a protocol.
- [protocol_addProtocol](<protocol_addprotocol(____).md>) — Adds a registered protocol to another protocol that is under construction.
- [protocol_addProperty](<protocol_addproperty(____________).md>) — Adds a property to a protocol that is under construction.
- [protocol_getName](<protocol_getname(__).md>) — Returns the name of a protocol.
- [protocol_isEqual](<protocol_isequal(____).md>) — Returns a Boolean value that indicates whether two protocols are equal.
- [protocol_copyMethodDescriptionList](<protocol_copymethoddescriptionlist(________).md>) — Returns an array of method descriptions of methods meeting a given specification for a given protocol.
- [protocol_getMethodDescription](<protocol_getmethoddescription(________).md>) — Returns a method description structure for a specified method of a given protocol.
- [protocol_copyPropertyList](<protocol_copypropertylist(____).md>) — Returns an array of the properties declared by a protocol.
- [protocol_getProperty](<protocol_getproperty(________).md>) — Returns the specified property of a given protocol.
- [protocol_copyProtocolList](<protocol_copyprotocollist(____).md>) — Returns an array of the protocols adopted by a protocol.
- [protocol_conformsToProtocol](<protocol_conformstoprotocol(____).md>) — Returns a Boolean value that indicates whether one protocol conforms to another protocol.

### Working with Properties

- [property_getName](<property_getname(__).md>) — Returns the name of a property.
- [property_getAttributes](<property_getattributes(__).md>) — Returns the attribute string of a property.
- [property_copyAttributeValue](<property_copyattributevalue(____).md>) — Returns the value of a property attribute given the attribute name.
- [property_copyAttributeList](<property_copyattributelist(____).md>) — Returns an array of property attributes for a given property.

### Using Objective-C Language Features

- [objc_enumerationMutation](<objc_enumerationmutation(__).md>) — Inserted by the compiler when a mutation is detected during a foreach iteration.
- [objc_setEnumerationMutationHandler](<objc_setenumerationmutationhandler(__).md>) — Sets the current mutation handler.
- [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) — Creates a pointer to a function that calls the specified block when the method is called.
- [imp_getBlock](<imp_getblock(__).md>) — Returns the block associated with an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>).
- [imp_removeBlock](<imp_removeblock(__).md>) — Disassociates a block from an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>), and releases the copy of the block that was created.
- [objc_loadWeak](<objc_loadweak(__).md>) — Loads the object referenced by a weak pointer and returns it.
- [objc_storeWeak](<objc_storeweak(____).md>) — Stores a new value in a `__weak` variable.

### Class-Definition Data Structures

- [Method](method.md) — An opaque type that represents a method in a class definition.
- [Ivar](ivar.md) — An opaque type that represents an instance variable.
- [Category](category.md) — An opaque type that represents a category.
- [objc_property_t](objc_property_t.md) — An opaque type that represents an Objective-C declared property.
- [IMP](imp.md) — A pointer to the start of a method implementation.
- [objc_method_description](objc_method_description.md) — Defines an Objective-C method.
- [objc_cache](objc_cache.md) — Performance optimization for method calls. Contains pointers to recently used methods.
- [objc_property_attribute_t](objc_property_attribute_t.md) — Defines a property attribute.

### Instance Data Types

- [objc_object](objc_object.md) — Represents an instance of a class.
- [objc_super](objc_super-swift.struct.md) — Specifies the superclass of an instance.

### Associative References

- [objc_AssociationPolicy](objc_associationpolicy.md) — Type to specify the behavior of an association.

## See Also

### Related Documentation

- [Objective-C Runtime Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008048)

### Reference

- [Objective-C Structures](objective-c-structures.md)
- [Objective-C Constants](objective-c-constants.md)
- [Objective-C Functions](objective-c-functions.md)
- [Objective-C Data Types](objective-c-data-types.md)
- [Objective-C Macros](objective-c-macros.md)
- [Objective-C Enumerations](objective-c-enums.md)
