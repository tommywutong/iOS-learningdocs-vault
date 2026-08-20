---
title: Cocoa Scripting Guide
apple_id: TP40002164
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_script_classes/SAppsScriptClasses.html
archived_at: '2026-07-15T07:18:51.250504Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Scripting Guide](Introduction%20to%20Cocoa%20Scripting%20Guide.md)


[Next](How%20Cocoa%20Applications%20Handle%20Apple%20Events.md)[Previous](Testing%2C%20Debugging%2C%20and%20Performance.md)

# Cocoa Scripting Classes and Categories

The tables in this chapter provide brief descriptions for the listed Cocoa scripting classes. The accompanying material provides information on when your application uses these classes, as well as hints on which ones you might need to subclass.

About thirty public classes in Cocoa's Foundation framework support the basic structure of Cocoa scripting. Several methods in the Application Kit framework add scriptability features for applications, windows, documents, and text objects. Together, this provides support for the AppleScript commands listed in [Summary of AppleScript Command Support](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delktk42q) (such as `get`, `set`, `move`, `delete`, and so on).

In many cases, Cocoa scripting creates and manipulates instances of these classes, such that your application needs only to respond when a method of a particular application object is invoked. That is, your application rarely needs to declare or instantiate any of the basic Cocoa scripting classes.

On the other hand, some applications will need to define subclasses of one or more of Cocoa scripting's command classes to provide support for operations specific to the application. Even in those cases, however, the application is not responsible for creating instances of the commands—Cocoa scripting does that, based on the scriptability information provided in the application's sdef file. The process of working with commands is described in detail in [Script Commands](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delkcijbueq2jjjcq).

There is one case where your application typically creates instances of Cocoa scripting classes. In object specifier methods for your scriptable classes, you'll create instances of the object specifier classes listed in [Table 9-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztiljzhe4domjy).

The following classes provide the base class for script commands, the context in which commands are executed, and the scriptability information associated with an application. Instances of these classes are created automatically by the Cocoa scripting, in a process described in [Script Commands Overview](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delktk42a). Except for `NSScriptCommand`, most applications will not need to subclass or even call methods of these classes.

__Table 9-1__  Scripting information and command classes

| Class | Description |
| [NSScriptSuiteRegistry](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry) | A shared instance of this class loads and registers the scriptability information associated with an application, whether from sdef files or the older script suite and script terminology files. Provides methods to get loaded suites, class descriptions, and command descriptions, but applications rarely call these methods. |
| [NSClassDescription](https://developer.apple.com/documentation/foundation/nsclassdescription) | Abstract class that provides the interface for querying the properties of a class. Instantiated by the global instance of `NSScriptSuiteRegistry` when it loads the application's scriptability information. |
| [NSScriptClassDescription](https://developer.apple.com/documentation/foundation/nsscriptclassdescription) | A subclass of `NSClassDescription` that represents a description of a scriptable class in a script suite. Provides methods to get attributes, relationships, supported commands, and related information for a scriptable class. Instantiated by the global instance of `NSScriptSuiteRegistry` when it loads the application's scriptability information. |
| [NSScriptCommandDescription](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription) | A subclass of [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) that represents a definition of a command supported by a suite. Provides methods to get command class and return and argument types for a script command class. Instantiated by the global instance of `NSScriptSuiteRegistry` when it loads the application's scriptability information. |
| [NSScriptCommand](https://developer.apple.com/documentation/foundation/nsscriptcommand) | Encapsulates an AppleScript command sent to an application as an Apple event. Uses its methods to evaluate object references (receivers and arguments) and execute the command. Cocoa scripting subclasses for the major AppleScript commands are described in [Table 9-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztilkcijbuoq2bifca). You can create your own subclasses to handle operations specific to your application. For more information, see [Object-first Versus Verb-first Script Commands](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delktk4yq). |
| [NSScriptExecutionContext](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext) | Represents the context in which an AppleScript command is executed and tracks global state related to that command. You do not need to subclass this class. |

`NSScriptObjectSpecifier`, an abstract class. Instances of these classes—object specifiers—know how to evaluate themselves within the context of a container object specifier. Some of these classes represent relative or logical tests performed with object specifiers (particularly `NSWhoseSpecifier` objects).

These are among the few classes provided by Cocoa scripting that your application routinely instantiates. It does so when creating object specifiers. You shouldn’t need to subclass these classes, but you will need to implement some of the methods in the described categories, particularly in providing object specifier methods for your scriptable objects. For detailed information, see [Object Specifiers](Object%20Specifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmznknltc).

__Table 9-2__  Object specifiers and related classes

| Class or category | Description |
| [NSScriptObjectSpecifier](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier) | An abstract parent class for subclasses that represent AppleScript references. An object specifier knows how to evaluate itself (to actual objects) in the context of a container specifier. |
| [NSIndexSpecifier](https://developer.apple.com/documentation/foundation/nsindexspecifier) | A subclass of `NSScriptObjectSpecifier` for object specifiers that specify an object in a collection by index. Though scripters typically specify one-based items, an index specifier, which typically locates objects within an array that correspond to the specified items, uses zero-based values. |
| [NSMiddleSpecifier](https://developer.apple.com/documentation/foundation/nsmiddlespecifier) | A subclass of `NSScriptObjectSpecifier` for object specifiers that specify the middle object in a collection. |
| [NSNameSpecifier](https://developer.apple.com/documentation/foundation/nsnamespecifier) | A subclass of `NSScriptObjectSpecifier` for object specifiers that specify an object in a collection by name. |
| [NSPositionalSpecifier](https://developer.apple.com/documentation/foundation/nspositionalspecifier) | A subclass of [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) for object specifiers that represent an insertion point by reference to a point before or after another object, or at the beginning or end of a collection. It contains an object specifier that represents the object referred to for position. |
| [NSPropertySpecifier](https://developer.apple.com/documentation/foundation/nspropertyspecifier) | A subclass of `NSScriptObjectSpecifier` for object specifiers that represent an attribute or relationship of an object. |
| [NSRandomSpecifier](https://developer.apple.com/documentation/foundation/nsrandomspecifier) | A subclass of `NSScriptObjectSpecifier` for object specifiers that specify an arbitrary object in a collection. |
| [NSRangeSpecifier](https://developer.apple.com/documentation/foundation/nsrangespecifier) | A subclass of `NSScriptObjectSpecifier` for object specifiers that specify a range of objects in a collection by indexes. Though scripters typically specify a one-based range of items, a range specifier, which typically locates objects within an array that correspond to the specified items, uses zero-based values. |
| [NSRelativeSpecifier](https://developer.apple.com/documentation/foundation/nsrelativespecifier) | A subclass of `NSScriptObjectSpecifier` for object specifiers that specify the position of an object in relation to another object. |
| [NSUniqueIDSpecifier](https://developer.apple.com/documentation/foundation/nsuniqueidspecifier) | A subclass of `NSScriptObjectSpecifier` for object specifiers that specify an object in a collection by unique ID. |
| [NSWhoseSpecifier](https://developer.apple.com/documentation/foundation/nswhosespecifier) | A subclass of `NSScriptObjectSpecifier` for object specifiers that specify an object in a collection that matches a specified condition defined by a Boolean expression. |
| `NSScriptObjectSpecifiers` | Category on [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) that defines methods that scriptable objects can implement to provide a fully specified object specifier to themselves within an application, and to perform their own specifier evaluation. |
| [NSLogicalTest](https://developer.apple.com/documentation/foundation/nslogicaltest) | A subclass of `NSScriptWhoseTest` for objects that represent the Boolean operations `AND`, `OR`, and `NOT`; used with one or more instances of `NSSpecifierTest`. |
| [NSSpecifierTest](https://developer.apple.com/documentation/foundation/nsspecifiertest) | A subclass of `NSScriptWhoseTest` for objects that represent a comparison between two objects (which can be object references before being evaluated) using a given comparison method. |
| [NSScriptWhoseTest](https://developer.apple.com/documentation/foundation/nsscriptwhosetest) | An abstract class for objects that represent Boolean expressions (qualifiers) involving object specifiers (also called `whose` clauses, as in `every word whose color is blue`). |
| `NSComparisonMethods` | Category on [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) that defines a set of default comparison methods useful for the comparisons in `NSSpecifierTest`. |
| `NSScriptingComparisonMethods` | Category on [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) that defines a set of additional comparison methods you may need to implement for comparisons in cases where the correct way to compare two objects for scripting is different from the correct way to compare objects otherwise. |

The following perform essential functions related to scripting. For information on the use of these classes, see [Key-Value Coding and Cocoa Scripting](Getting%20and%20Setting%20Properties%20and%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvooi) and [Coercion](Getting%20and%20Setting%20Properties%20and%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvoni).

__Table 9-3__  Scripting utilities

| Class or category | Description |
| [NSScriptCoercionHandler](https://developer.apple.com/documentation/foundation/nsscriptcoercionhandler) | A shared instance of this class coerces object values to objects of another class, using information supplied by classes who register with it. Coercions frequently are required during key-value coding. For more information, see [Coercion](Getting%20and%20Setting%20Properties%20and%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvoni). |
| `NSScriptKeyValueCoding` | Category on [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) that defines additions to the implementation of key-value coding related to scripting, such as getting and setting key values by index in collections and coercing (or converting) a key value. |

The following classes implement standard AppleScript commands. They are all subclasses of `NSScriptCommand`, which is described in [Table 9-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztilkdjjbeisseirda). Your application can create a subclass of one of these classes to replace the default behavior, or to selectively modify that behavior in some circumstances. In most cases, the default behavior should be sufficient.

For more information on working with commands, see [Script Commands](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delkcijbueq2jjjcq).

__Table 9-4__  Subclasses for standard script commands

| Class | Description |
| [NSCloneCommand](https://developer.apple.com/documentation/foundation/nsclonecommand) | Copies the specified scriptable object or objects (such as words, paragraphs, images, and so on) and inserts them in the specified location. This class handles the `duplicate` AppleScript command. |
| [NSCloseCommand](https://developer.apple.com/documentation/foundation/nsclosecommand) | Closes the specified scriptable object or objects—typically a document or window. |
| [NSCountCommand](https://developer.apple.com/documentation/foundation/nscountcommand) | Counts the number of items of a specified class in the specified object container (such as the number of rectangles in a document). |
| [NSCreateCommand](https://developer.apple.com/documentation/foundation/nscreatecommand) | Creates the specified scriptable object (such as a document or graphic), optionally supplying the new object with the specified attributes. This class handles the `make` AppleScript command. |
| [NSDeleteCommand](https://developer.apple.com/documentation/foundation/nsdeletecommand) | Deletes the specified scriptable object or objects. |
| [NSExistsCommand](https://developer.apple.com/documentation/foundation/nsexistscommand) | Determines whether a specified scriptable object, such as a word, paragraph, or image, exists. |
| [NSGetCommand](https://developer.apple.com/documentation/foundation/nsgetcommand) | Gets the specified value or object from the specified scriptable object. For related information, see [Getting and Setting Properties and Elements](Getting%20and%20Setting%20Properties%20and%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvomi). |
| [NSMoveCommand](https://developer.apple.com/documentation/foundation/nsmovecommand) | Moves the specified scriptable object or objects. For related information, see [Modifying a Standard Command](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delktk4ytc). |
| [NSQuitCommand](https://developer.apple.com/documentation/foundation/nsquitcommand) | Quits the specified application. |
| [NSSetCommand](https://developer.apple.com/documentation/foundation/nssetcommand) | Sets one or more attributes or relationships of the specified scriptable object to one or more values. For related information, see [Getting and Setting Properties and Elements](Getting%20and%20Setting%20Properties%20and%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvomi). |

You can use the following classes to directly manipulate Apple events and the data structures they contain. However, you can make your application scriptable with little or no direct use of these classes.

__Table 9-5__  Classes for manipulating Apple events

| Class | Description |
| [NSAppleEventDescriptor](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor) | Represents a descriptor, the basic building block for Apple events. Descriptors can consist of arbitrarily nested lists of other descriptors. Every Apple event is itself a descriptor and is made up of descriptors. For information on the underlying structure of descriptors, see [Building an Apple Event](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/building_aes_aepg/building_aes_aepg.html#//apple_ref/doc/uid/TP40001449-CH203) in _[Apple Events Programming Guide](../../Apple%20Script/Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_. |
| [NSAppleEventManager](https://developer.apple.com/documentation/foundation/nsappleeventmanager) | Provides access to a small set of Apple Event Manager features. Used primarily for directly registering Apple event handlers and for suspending and resuming Apple events (described in [Suspending and Resuming Apple Events and Script Commands](How%20Cocoa%20Applications%20Handle%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgiztsljrgeztinzxha)). For background information, see _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_ and _[Apple Events Programming Guide](../../Apple%20Script/Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_. |
| [NSAppleScript](https://developer.apple.com/documentation/foundation/nsapplescript) | Provides the ability to load, compile, and execute scripts. |

[Next](How%20Cocoa%20Applications%20Handle%20Apple%20Events.md)[Previous](Testing%2C%20Debugging%2C%20and%20Performance.md)

