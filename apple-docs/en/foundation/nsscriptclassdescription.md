---
title: NSScriptClassDescription
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptclassdescription
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription.json'
content_hash: 'sha256:b21574d0de30e73c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSScriptClassDescription

<sub>Class</sub>

A scriptable class that a macOS app supports.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSScriptClassDescription
```

## Overview

A scriptable application provides scriptability information that describes the commands and objects scripters can use in scripts that target the application. That includes information about the classes those scriptable objects are created from.

An application’s scriptability information is collected automatically by an instance of [NSScriptSuiteRegistry](nsscriptsuiteregistry.md). The registry object creates an `NSScriptClassDescription` for each class it finds and caches these objects in memory. Cocoa scripting uses registry information in handling scripting requests that target the application.

A class description instance stores the name, attributes, relationships, and supported commands for a class. For example, a scriptable `document` class for a drawing application might support attributes such as `file` and `file type`, relationships such as collections of `circles`, `rectangles`, and `lines`, and commands such as `align` and `rotate`.

As with many of the classes in Cocoa’s built-in scripting support, your application may never need to directly work with instances of `NSScriptClassDescription`. However, one case where you might need access to a class description is if you override `objectSpecifier` in a scriptable class. For information on how to do this, see [Object Specifiers](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_object_specifiers/SAppsObjectSpecifiers.html#//apple_ref/doc/uid/TP40002164-CH3) in [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

Another case where your application may need access to class description information is if you override `indicesOfObjectsByEvaluatingWithContainer:count:` in a specifier class.

Although you can subclass `NSScriptClassDescription`, it is unlikely that you would need to do so, or even to create instances of it.

## Relationships

- **Inherits From**: [NSClassDescription](nsclassdescription.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a Script Class Description

- [- initWithSuiteName:className:dictionary:](<nsscriptclassdescription/init(suitename_classname_dictionary_).md>) — Initializes and returns a newly allocated instance of `NSScriptClassDescription`.

### Getting a Script Class Description

- [+ classDescriptionForClass:](<nsscriptclassdescription/init(for_).md>) — Returns the class description for the specified class or, if it is not scriptable, for the first superclass that is.
- [- classDescriptionForKey:](<nsscriptclassdescription/forkey(__).md>) — Returns the class description instance for the class type of the specified attribute or relationship.
- [superclassDescription](nsscriptclassdescription/superclass.md) — Returns the class description instance for the superclass of the receiver’s class.

### Getting basic information about the script class

- [className](nsscriptclassdescription/classname.md) — Returns the name of the class the receiver describes, as provided at initialization time.
- [defaultSubcontainerAttributeKey](nsscriptclassdescription/defaultsubcontainerattributekey.md) — Returns the value of the `DefaultSubcontainerAttribute` entry of the class dictionary from which the receiver was instantiated.
- [implementationClassName](nsscriptclassdescription/implementationclassname.md) — Returns the name of the Objective-C class instantiated to implement the scripting class.
- [- isLocationRequiredToCreateForKey:](<nsscriptclassdescription/islocationrequiredtocreate(forkey_).md>) — Returns a Boolean value indicating whether an insertion location must be specified when creating a new object in the specified to-many relationship of the receiver.
- [suiteName](nsscriptclassdescription/suitename.md) — Returns the name of the receiver’s suite.

### Getting and comparing Apple event codes

- [appleEventCode](nsscriptclassdescription/appleeventcode.md) — Returns the Apple event code associated with the receiver’s class.
- [- appleEventCodeForKey:](<nsscriptclassdescription/appleeventcode(forkey_).md>) — Returns the Apple event code for the specified attribute or relationship in the receiver.
- [- matchesAppleEventCode:](<nsscriptclassdescription/matchesappleeventcode(__).md>) — Returns a Boolean value indicating whether a primary or secondary Apple event code in the receiver matches the passed code.

### Getting attribute and relationship information

- [- hasOrderedToManyRelationshipForKey:](<nsscriptclassdescription/hasorderedtomanyrelationship(forkey_).md>) — Returns a Boolean value indicating whether the described class has an ordered to-many relationship identified by the specified key.
- [- hasPropertyForKey:](<nsscriptclassdescription/hasproperty(forkey_).md>) — Returns a Boolean value indicating whether the described class has a property identified by the specified key.
- [- hasReadablePropertyForKey:](<nsscriptclassdescription/hasreadableproperty(forkey_).md>) — Returns a Boolean value indicating whether the described class has a readable property identified by the specified key.
- [- hasWritablePropertyForKey:](<nsscriptclassdescription/haswritableproperty(forkey_).md>) — Returns a Boolean value indicating whether the described class has a writable property identified by the specified key.
- [- keyWithAppleEventCode:](<nsscriptclassdescription/key(withappleeventcode_).md>) — Given an Apple event code that identifies a property or element class, returns the key for the corresponding attribute, one-to-one relationship, or one-to-many relationship.
- [- typeForKey:](<nsscriptclassdescription/type(forkey_).md>) — Returns the name of the declared type of the attribute or relationship identified by the passed key.

### Getting command information

- [- selectorForCommand:](<nsscriptclassdescription/selector(forcommand_).md>) — Returns the selector associated with the receiver for the specified command description.
- [- supportsCommand:](<nsscriptclassdescription/supportscommand(__).md>) — Returns a Boolean value indicating whether the receiver or any superclass supports the specified command.

## See Also

### Script Dictionary Description

- [NSScriptSuiteRegistry](nsscriptsuiteregistry.md) — The top-level repository of scriptability information for an app at runtime.
- [NSClassDescription](nsclassdescription.md) — An abstract class that provides the interface for querying the relationships and properties of a class.
- [NSScriptCommandDescription](nsscriptcommanddescription.md) — A script command that a macOS app supports.
