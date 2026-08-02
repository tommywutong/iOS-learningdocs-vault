---
title: Cocoa Scripting Guide
apple_id: TP40002164
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_glossary/SAppsGlossary.html
archived_at: '2026-07-15T07:18:50.817254Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Scripting Guide](Introduction%20to%20Cocoa%20Scripting%20Guide.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- __`'aete'` resource__

  A resource that serves as the traditional mechanism for providing scriptability information in a Carbon application. An `'aete'` resource can also be included in a Cocoa application to control how scriptability information is displayed in a dictionary viewer, by applications such as Script Editor and Xcode. Starting in OS X version 10.4, it is not needed for this purpose, for applications that supply their scriptability information in the sdef format.

- __Apple event__

  An interprocess message that can specify complex operations and data. An Apple event encapsulates a high-level task in a single package that can be passed across process boundaries, performed, and responded to with a reply event.

- __Apple Event Manager__

  The OS X API for creating and sending Apple events, and for receiving, extracting information from, and responding to them.

- __Apple event translator__

  A part of Cocoa scripting that uses scriptability information supplied by an application to evaluate an Apple event received by the application. In many cases, an Apple event is "translated" into a script command object that performs the action specified by the event.

- __AppleScript__

  A scripting language that makes possible direct control of scriptable applications and scriptable parts of the Mac OS. See also [Open Scripting Architecture (OSA)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvomjz).

- __AppleScript object model__

  A hierarchical structure that, for a given application, specifies the classes of objects a scripter can work with in scripts, the accessible properties of those objects, and the inheritance and containment relationships for those objects.

- __attribute__

  (1) In key-value coding (and in suite files), refers to a property that is a simple value, such as a scalar, string, or Boolean value, or to immutable objects such as `NSColor` and `NSNumber` objects. In a scripting definition file, the equivalent of an attribute is a property. A `graphic` object might have a `color` attribute (or property). (2) In AppleScript, one of the two main descriptor data types that make up an Apple event. Not commonly used by scriptable Cocoa applications. (3) In an XML file, a name/value pair that specifies a single property for an element.

- __class description__

  A scripting definition file (sdef) entry that describes a scriptable class, including its attributes and relationships and the KVC keys that Cocoa scripting uses to gain access to its values. When the sdef is loaded, the information is stored in an instance of `NSScriptClassDescription`.

- __Cocoa scripting__

  In the Cocoa application framework, the support for creating scriptable applications. Cocoa scripting includes classes, categories, and scriptability information, which together support much of AppleScript's Standard suite.

- __command description__

  A scripting definition file (sdef) entry that describes the characteristics of an AppleScript command, including argument names (if any), command result type (if any), AppleScript command name, and name of the Objective-C class Cocoa instantiates to perform the command. When the sdef is loaded, the information is stored in an instance of `NSScriptCommandDescription`.

- __element__

  (1) In a scripting definition file (or an AppleScript dictionary viewer), a characteristic of an object that refers to a contained collection of related objects. Synonymous with a key-value coding to-many relationship. A `document` object might have a `graphics` element (or to-many relationship). (2) In an XML file, such as a scripting definition file, a tag-delimited unit of data.

- __four-character code__

  Four bytes of data that can be expressed as a string of four characters in the Mac OS Roman encoding. Used to uniquely identify terms and other items in an application's scriptability information.

- __implicitly specified subcontainer__

  An object container that can be specified in an AppleScript script by context, rather than by an explicit reference. For example, explicitly specifying a `word` object in a `document` object might require this script reference: `fourth word of text of front document`. But if the application provides support for implicitly specifying the `text` container, the script reference can be simplified to this: `fourth word of front document`.

- __key__

  (1) In key-value coding, a string that identifies a property. (2) In property lists, the part of a key-value pair that identifies a value in the list.

- __key-value coding (KVC)__

  A mechanism (widely used in Cocoa) for accessing object properties indirectly by key. Cocoa scripting relies on KVC both to get and set properties of scriptable objects, and to identify the objects on which commands should operate.

- __keyword__

  A four-character code used by the Apple Event Manager to identify a specific descriptor within an Apple event. Cocoa applications don’t typically access the contents of individual Apple events directly, so they don’t work with keywords, although they can do so by using methods of [NSAppleEventDescriptor](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor) or by directly calling C functions of the Apple Event Manager.

- __KVC__

  See [key-value coding (KVC)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvomjt).

- __Model-View-Controller (MVC)__

  A design pattern that assigns objects in an application to one of three roles and recommends a distinct separation among model, view, and controller objects. This is one of the central design patterns for Cocoa applications.

- __MVC__

  See [Model-View-Controller (MVC)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvomju).

- __object containment hierarchy__

  The hierarchy of objects in a running application. AppleScript and Cocoa scripting depend on the object containment hierarchy to locate the objects on which to perform an operation. See also [AppleScript object model](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvomjx).

- __object-first command__

  A script command that invokes a specified method of each specified receiver. With an object-first command, objects perform the specified action on themselves. Compare [verb-first command](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvony).

- __object specifier__

  Locates a scriptable object within an application’s containment hierarchy. Cocoa scripting makes use of object specifiers to find objects in your application while executing a script command and to return information requested by a script. See also [object containment hierarchy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvomjy).

- __Open Scripting Architecture (OSA)__

  Provides a standard and extensible mechanism for interapplication communication in OS X. Implemented by a number of OS X frameworks and subframeworks, including the AE framework (which implements the Apple Event Manager) and the OpenScripting framework. Also includes the AppleScript component, which implements the AppleScript language.

- __property__

  (1) In a scripting definition file, a characteristic of a class that has a single value and is identified by a label. Synonymous with a key-value coding (KVC) attribute or to-one relationship. A window's `name` property would be equivalent to a KVC attribute, while its `document` property would be equivalent to a KVC to-one relationship. (2) In KVC, can refer to any of the three different kinds of object values that KVC can access: attributes, to-one relationships, and to-many relationships.

- __receivers__

  The object or objects in an application designated to receive an AppleScript command.

- __receivers specifier__

  In a script command object, the object specifier that specifies the objects in the application that should receive an command.

- __reference__

  In an AppleScript script, the part of a script statement that identifies an object. Constructions such as `first rectangle` and `document "My Notes"` are references. Cocoa scripting provides built-in support for AppleScript's standard reference forms, listed in [Table 6-1](Object%20Specifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmznknlte).

- __required events__

  Certain Apple events that all Mac apps that present a graphical user interface should be able to respond to. These events can be sent by the Mac OS, as well as by other applications and by users executing scripts. They include the `open application`, `open documents`, `print documents`, `open contents`, `reopen`, and `quit` events.

- __scriptability information__

  Formally lays out the AppleScript object model for an application and maps it to application objects. Scriptability information specifies the terminology available for use in scripts that target the application. It also provides information, used by AppleScript and by Cocoa, about how support for that terminology is implemented in the application. See also [scripting definition format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvomi), [script suite format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvomjw).

- __scriptable application__

  An application that makes its operations and data available in response to Apple events, which are AppleScript messages.

- __script command object__

  An object that encapsulates all the information needed to perform an AppleScript command. Cocoa scripting creates script command objects in response to Apple events received by the application. A script command object is instantiated from `NSScriptCommand` or from one of its subclasses—either those provided by Cocoa scripting to handle standard AppleScript commands, or those defined by your application to perform its unique operations.

- __scripting definition file__

  A file in the scripting definition format that provides the scriptability information for an application. A scripting definition file has the extension `.sdef` and is also called an _sdef file_ or simply an _sdef_. Compare [script suite file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvona), [script terminology file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvomy).

- __scripting definition format__

  An XML-based format that describes a set of scriptability terms and the commands, classes, constants, and other information used to support an application's scriptability. This format was introduced in OS X version 10.2 and is used natively by Cocoa scripting starting in OS X version 10.4. Also called _sdef format_. Compare [script suite format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvomjw).

- __script suite file__

  A property list file, in a specific format, that describes scriptable classes in terms of their attributes, relationships, and supported commands and that has the extension `.scriptSuite`. Script suite files, together with corresponding script terminology files, declare the scriptability information for a scriptable application. See also [script terminology file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvomy).

- __script suite format__

  A format for providing scriptability information in the form of property list files, consisting of a script suite file together with a corresponding script terminology file. Compare [scripting definition format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvomi).

- __script terminology file__

  A property list file, in a specific format, that provides AppleScript terminology—the English-like words and phrases a scripter can use in a script—for the class and command descriptions in the corresponding script suite file. A script terminology file has the extension `.scriptTerminology`. Together with a corresponding script suite file, it declares the scriptability information for a scriptable application. See also [script suite file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvona).

- __sdef__

  See [scripting definition file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvomjv).

- __Standard suite__

  The scriptability information for a set of standard AppleScript terms that scriptable applications should support if possible. The Standard suite contains commands such as `count`, `delete`, `duplicate`, and `make`, and classes such as `application`, `document`, and `window`. Cocoa scripting provides a great deal of automatic support for the Standard suite.

- __suite__

  Within an application's scriptability information, terms associated with related operations. For example, operations involving text, graphics, or databases are generally collected into separate text, graphics, and database suites.

- __to-many relationship__

  In key-value coding (and in suite files), a property whose value is a collection of related objects. In a scripting definition file, represented by an `element` element.

- __to-one relationship__

  In key-value coding (and in suite files), a property whose value has properties of its own. In a scripting definition file, represented by a `property` element.

- __top-level specifier__

  In a nested object specifier, an object that has no container specifier. It represents the outermost container in the containment hierarchy. In most cases, the application object is the top-level specifier.

- __verb-first command__

  A script command that invokes its `performDefaultImplementation` method. With a verb-first command, a single method performs the action (or verb) on any number of objects. Compare [object-first command](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvonq).

[Previous](Document%20Revision%20History.md)

