---
title: NSComparisonMethods
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscomparisonmethods
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonmethods'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonmethods.json'
content_hash: 'sha256:001083b52c264088'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Scripting Support](scripting-support.md)

# NSComparisonMethods

A collection of default comparison methods useful for performing specifier tests.

## Overview

If you have scriptable objects that need to perform comparisons for scripting purposes, you may need to implement some of the methods declared in NSScriptingComparisonMethods. The default implementation provided for many of these methods by `NSObject` is appropriate for objects that implement a single comparison method whose selector, signature, and description match the following:

```objc
- (NSComparisonResult)compare:(id)object;
```

This method should return `NSOrderedAscending` if the receiver is less than `object`, `NSOrderedDescending` if the receiver is greater than `object`, and `NSOrderedSame` if the receiver and `object` are equal. For example, `NSString` does not implement most of the methods declared in this informal protocol, but `NSString` objects still handle messages conforming to this protocol properly because `NSString` implements a `compare:` method that meets the necessary requirements. Cocoa also includes appropriate `compare:` method implementations for the `NSDate`, `NSDecimalNumber`, and `NSValue` classes.

## Topics

### Performing comparisons

- [doesContain(_:)](<../objectivec/nsobject-swift.class/doescontain(__).md>) — Returns a Boolean value that indicates whether the receiver contains a given object.
- [isCaseInsensitiveLike(_:)](<../objectivec/nsobject-swift.class/iscaseinsensitivelike(__).md>) — Returns a Boolean value that indicates whether receiver is considered to be “like” a given string when the case of characters in the receiver is ignored.
- [isEqual(to:)](<../objectivec/nsobject-swift.class/isequal(to_).md>) — Returns a Boolean value that indicates whether the receiver is equal to another given object.
- [isGreaterThan(_:)](<../objectivec/nsobject-swift.class/isgreaterthan(__).md>) — Returns a Boolean value that indicates whether the receiver is greater than another given object.
- [isGreaterThanOrEqual(to:)](<../objectivec/nsobject-swift.class/isgreaterthanorequal(to_).md>) — Returns a Boolean value that indicates whether the receiver is greater than or equal to another given object.
- [isLessThan(_:)](<../objectivec/nsobject-swift.class/islessthan(__).md>) — Returns a Boolean value that indicates whether the receiver is less than another given object.
- [isLessThanOrEqual(to:)](<../objectivec/nsobject-swift.class/islessthanorequal(to_).md>) — Returns a Boolean value that indicates whether the receiver is less than or equal to another given object.
- [isLike(_:)](<../objectivec/nsobject-swift.class/islike(__).md>) — Returns a Boolean value that indicates whether the receiver is “like” another given object.
- [isNotEqual(to:)](<../objectivec/nsobject-swift.class/isnotequal(to_).md>) — Returns a Boolean value that indicates whether the receiver is not equal to another given object.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

### NSObject Script Support

- [NSScriptingComparisonMethods](../objectivec/nsscriptingcomparisonmethods.md) — A collection of methods useful for comparing script objects.
- [NSScriptKeyValueCoding](../objectivec/nsscriptkeyvaluecoding.md) — A collection of methods that provide additional capabilities for working with key-value coding.
- [NSScriptObjectSpecifiers](nsscriptobjectspecifiers.md) — A collection of methods providing additional object specifier functionality.
- [NSScriptCoercionHandler](nsscriptcoercionhandler.md) — A mechanism for converting one kind of scripting data to another.
- [NSScriptExecutionContext](nsscriptexecutioncontext.md) — The context in which the current script command is executed.
