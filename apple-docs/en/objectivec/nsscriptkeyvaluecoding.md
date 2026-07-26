---
title: NSScriptKeyValueCoding
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsscriptkeyvaluecoding
source_url: 'https://developer.apple.com/documentation/objectivec/nsscriptkeyvaluecoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsscriptkeyvaluecoding.json'
content_hash: 'sha256:50206522990001db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# NSScriptKeyValueCoding

<sub>API Collection</sub>

A collection of methods that provide additional capabilities for working with key-value coding.

## Overview

Cocoa scripting takes advantage of key-value coding to get and set information in scriptable objects. The methods in this category provide additional capabilities for working with key-value coding, including getting and setting key values by index in multi-value keys and coercing (or converting) a key value. Additional methods allow the implementer of a scriptable container class to provide fast access to elements that are being referenced by name and unique ID.

Because Cocoa scripting invokes [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>) and [- mutableArrayValueForKey:](<nsobject-swift.class/mutablearrayvalue(forkey_).md>), changes to model objects made by AppleScript scripts are observable using automatic key-value observing.

> [!note] Note
> In OS X 10.3 and earlier, Cocoa scripting did not invoke [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>) or [- mutableArrayValueForKey:](<nsobject-swift.class/mutablearrayvalue(forkey_).md>), so automatic key-value observing notification was not always done for model object changes caused by scripts. Starting in macOS 10.4, for backward binary compatibility, if it is overridden, Cocoa invokes the now-deprecated method [- takeValue:forKey:](<nsobject-swift.class/takevalue(__forkey_).md>) instead of [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>).

## Topics

### Indexed access

- [- insertValue:atIndex:inPropertyWithKey:](<nsobject-swift.class/insertvalue(__at_inpropertywithkey_).md>) — Inserts an object at the specified index in the collection specified by the passed key.
- [- removeValueAtIndex:fromPropertyWithKey:](<nsobject-swift.class/removevalue(at_frompropertywithkey_).md>) — Removes the object at the specified index from the collection specified by the passed key.
- [- replaceValueAtIndex:inPropertyWithKey:withValue:](<nsobject-swift.class/replacevalue(at_inpropertywithkey_withvalue_).md>) — Replaces the object at the specified index in the collection specified by the passed key.
- [- valueAtIndex:inPropertyWithKey:](<nsobject-swift.class/value(at_inpropertywithkey_).md>) — Retrieves an indexed object from the collection specified by the passed key.

### Access by name, key, or ID

- [- insertValue:inPropertyWithKey:](<nsobject-swift.class/insertvalue(__inpropertywithkey_).md>) — Inserts an object in the collection specified by the passed key.
- [- valueWithName:inPropertyWithKey:](<nsobject-swift.class/value(withname_inpropertywithkey_).md>) — Retrieves a named object from the collection specified by the passed key.
- [- valueWithUniqueID:inPropertyWithKey:](<nsobject-swift.class/value(withuniqueid_inpropertywithkey_).md>) — Retrieves an object by ID from the collection specified by the passed key.

### Coercion

- [- coerceValue:forKey:](<nsobject-swift.class/coercevalue(__forkey_).md>) — Uses type info from the class description and `NSScriptCoercionHandler` to attempt to convert `value` for `key` to the proper type, if necessary.

### Constants

- [NSScriptKeyValueCoding Exception Names](nsscriptkeyvaluecoding-exception-names.md) — Exceptions raised by key-value coding methods.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)

### Key-Value Coding

- [NSKeyValueBindingCreation](nskeyvaluebindingcreation.md) — A set of methods that you can use to create and remove bindings between view objects and controllers, or between controllers and model objects.
- [NSKeyValueCoding](nskeyvaluecoding.md) — A mechanism by which you can access the properties of an object indirectly by name or key.
- [NSScriptKeyValueCoding Exception Names](nsscriptkeyvaluecoding-exception-names.md) — Exceptions raised by key-value coding methods.
