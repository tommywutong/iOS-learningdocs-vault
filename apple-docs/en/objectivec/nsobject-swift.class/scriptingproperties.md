---
title: scriptingProperties
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/scriptingproperties
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/scriptingproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/scriptingproperties.json'
content_hash: 'sha256:05969da5ad5b9a94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# scriptingProperties

<sub>Instance Property</sub>

An `NSString`-keyed dictionary of the receiver’s scriptable properties.

<sub>Mac Catalyst, macOS</sub>

```swift
var scriptingProperties: [String : Any]? { get set }
```

## Discussion

An `NSString`-keyed dictionary of the receiver’s scriptable properties, including all of those that are declared as Attributes and ToOneRelationships in the `.scriptSuite` property list entries for the class and its scripting superclasses, with the exception of ones keyed by “scriptingProperties.” Each key in the dictionary must be identical to the key for an Attribute or ToOneRelationship. The values of the dictionary must be Objective-C objects that are convertible to `NSAppleEventDescriptor` objects.

## See Also

### Scripting

- [classCode](classcode.md) — The receiver’s Apple event type code, as stored in the `NSScriptClassDescription` object for the object’s class.
- [className](classname.md) — A string containing the name of the class.
- [- copyScriptingValue:forKey:withProperties:](<copyscriptingvalue(__forkey_withproperties_).md>) — Creates and returns one or more scripting objects to be inserted into the specified relationship by copying the passed-in value and setting the properties in the copied object or objects.
- [- newScriptingObjectOfClass:forValueForKey:withContentsValue:properties:](<newscriptingobject(of_forvalueforkey_withcontentsvalue_properties_).md>) — Creates and returns an instance of a scriptable class, setting its contents and properties, for insertion into the relationship identified by the key.
- [- scriptingValueForSpecifier:](<scriptingvalue(for_).md>) — Given an object specifier, returns the specified object or objects in the receiving container.
