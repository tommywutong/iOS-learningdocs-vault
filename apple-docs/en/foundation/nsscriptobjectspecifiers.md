---
title: NSScriptObjectSpecifiers
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptobjectspecifiers
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifiers.json'
content_hash: 'sha256:9c03d9f04a5a40f5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Scripting Support](scripting-support.md)

# NSScriptObjectSpecifiers

A collection of methods providing additional object specifier functionality.

## Overview

These methods allow scriptable objects to provide a fully specified object specifier to themselves within an app. They also enable containers of objects to perform their own specifier evaluation.

For a comprehensive treatment of object specifiers, including sample code, see [Object Specifiers](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_object_specifiers/SAppsObjectSpecifiers.html#//apple_ref/doc/uid/TP40002164-CH3) in [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

## Topics

### Working with object specifiers

- [objectSpecifier](../objectivec/nsobject-swift.class/objectspecifier.md) — Returns an object specifier for the receiver.
- [indicesOfObjects(byEvaluatingObjectSpecifier:)](<../objectivec/nsobject-swift.class/indicesofobjects(byevaluatingobjectspecifier_).md>) — Returns the indices of the specified container objects.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

### NSObject Script Support

- [NSComparisonMethods](nscomparisonmethods.md) — A collection of default comparison methods useful for performing specifier tests.
- [NSScriptingComparisonMethods](../objectivec/nsscriptingcomparisonmethods.md) — A collection of methods useful for comparing script objects.
- [NSScriptKeyValueCoding](../objectivec/nsscriptkeyvaluecoding.md) — A collection of methods that provide additional capabilities for working with key-value coding.
- [NSScriptCoercionHandler](nsscriptcoercionhandler.md) — A mechanism for converting one kind of scripting data to another.
- [NSScriptExecutionContext](nsscriptexecutioncontext.md) — The context in which the current script command is executed.
