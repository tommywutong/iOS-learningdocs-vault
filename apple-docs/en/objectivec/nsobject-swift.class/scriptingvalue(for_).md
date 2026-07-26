---
title: 'scriptingValue(for:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/scriptingvalue(for:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/scriptingvalue(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/scriptingvalue%28for%3A%29.json'
content_hash: 'sha256:9af75f6339bdb279'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# scriptingValue(for:)

<sub>Instance Method</sub>

Given an object specifier, returns the specified object or objects in the receiving container.

<sub>macOS</sub>

```swift
func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?
```

## Parameters

- `objectSpecifier` — An object specifier to be evaluated.

## Return Value

The specified object or objects in the receiving container.

## Discussion

This method might successfully return an object, an array of objects, or `nil`, depending on the kind of object specifier. Because `nil` is a valid return value, failure is signaled by invoking the object specifier’s `setEvaluationError:` method before returning.

## Discussion

You can override this method to customize the evaluation of object specifiers without requiring that the scripting container make up indexes for contained objects that don’t naturally have indexes (as can be the case if you implement [- indicesOfObjectsByEvaluatingObjectSpecifier:](<indicesofobjects(byevaluatingobjectspecifier_).md>) instead).

Your override of this method doesn’t need to also invoke any of the `NSScriptCommand` error signaling methods, though it can, to record very specific information. The `NSUnknownKeySpecifierError` and `NSInvalidIndexSpecifierError` numbers are special, in that Cocoa may continue evaluating an outer specifier if they’re encountered, for the convenience of scripters.

## See Also

### Scripting

- [classCode](classcode.md) — The receiver’s Apple event type code, as stored in the `NSScriptClassDescription` object for the object’s class.
- [className](classname.md) — A string containing the name of the class.
- [- copyScriptingValue:forKey:withProperties:](<copyscriptingvalue(__forkey_withproperties_).md>) — Creates and returns one or more scripting objects to be inserted into the specified relationship by copying the passed-in value and setting the properties in the copied object or objects.
- [- newScriptingObjectOfClass:forValueForKey:withContentsValue:properties:](<newscriptingobject(of_forvalueforkey_withcontentsvalue_properties_).md>) — Creates and returns an instance of a scriptable class, setting its contents and properties, for insertion into the relationship identified by the key.
- [scriptingProperties](scriptingproperties.md) — An `NSString`-keyed dictionary of the receiver’s scriptable properties.
