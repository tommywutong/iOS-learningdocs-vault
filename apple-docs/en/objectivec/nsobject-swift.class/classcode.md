---
title: classCode
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/classcode
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/classcode.json'
content_hash: 'sha256:321f9f1284fbb5e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# classCode

<sub>Instance Property</sub>

The receiver’s Apple event type code, as stored in the `NSScriptClassDescription` object for the object’s class.

<sub>Mac Catalyst, macOS</sub>

```swift
var classCode: FourCharCode { get }
```

## Discussion

This property is used by Cocoa’s scripting support classes.

## See Also

### Scripting

- [className](classname.md) — A string containing the name of the class.
- [- copyScriptingValue:forKey:withProperties:](<copyscriptingvalue(__forkey_withproperties_).md>) — Creates and returns one or more scripting objects to be inserted into the specified relationship by copying the passed-in value and setting the properties in the copied object or objects.
- [- newScriptingObjectOfClass:forValueForKey:withContentsValue:properties:](<newscriptingobject(of_forvalueforkey_withcontentsvalue_properties_).md>) — Creates and returns an instance of a scriptable class, setting its contents and properties, for insertion into the relationship identified by the key.
- [scriptingProperties](scriptingproperties.md) — An `NSString`-keyed dictionary of the receiver’s scriptable properties.
- [- scriptingValueForSpecifier:](<scriptingvalue(for_).md>) — Given an object specifier, returns the specified object or objects in the receiving container.
