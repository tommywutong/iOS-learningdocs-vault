---
title: Cocoa Scripting Guide
apple_id: TP40002164
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_implement/SAppsImplement.html
archived_at: '2026-07-15T07:18:50.841899Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Scripting Guide](Introduction%20to%20Cocoa%20Scripting%20Guide.md)


[Next](Preparing%20a%20Scripting%20Definition%20File.md)[Previous](Designing%20for%20Scriptability.md)

# Implementing a Scriptable Application

This chapter lists the key steps for implementing a scriptable Cocoa application, with links to more detailed information where necessary.

Once you have completed one of the design phases described in [Designing for Scriptability](Designing%20for%20Scriptability.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzyfvbeeq2cineuuri), you use steps like the following to implement a scriptable Cocoa application:

1. For a new application, implementing scriptability should be an integral part of creating the application. That is, you’ll be creating scriptable classes, adding scripting accessor methods, and so on, as you implement other parts of the application.

   When you’re adding scriptability to an existing application, there is more opportunity for a staged or incremental approach. That is, you may want to test your approach by retrofitting one or a small number of classes, before extending it to the entire application.

   In either case, your work should include milestones to test each phase of scriptability, as spelled out in your test plan.
2. Cocoa follows the Model-View-Controller (MVC) design pattern, where model objects encapsulate and manipulate the data used by the application. You should generally support scriptability in your model objects, which tend to be more persistent. Although there may be some cases where you want to allow scripting of your view objects, keep in mind that scripts that operate on the user interface tend to be fragile, and they can also be less efficient.

   For more information, see [Concentrate Scriptable Behavior in Model Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztoljrga4dqmbwgy).
3. Provide an sdef file with the scriptability information for your application.

   For more information, see [Supply a Scripting Definition File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztolktk42a).
4. Maintain key-value coding (KVC) naming compliance for instance variables or accessor methods for scriptable properties and elements, based on the keys in your sdef file. Cocoa scripting support relies on this naming compliance.

   For details, see [Maintain KVC Compliance](Getting%20and%20Setting%20Properties%20and%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvona).
5. Include the sdef file in the Xcode project for your application, as described in [Add the Scripting Definition File to Your Xcode Project](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztoljrga4dcnzzg4).
6. Modify your application’s `Info.plist` file to turn on Cocoa scripting support and identify your sdef file, as described in [Turn On Scripting Support in Your Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztoljrga4dcmbugy).
7. Cocoa implements the `NSScriptCommand` class and a number of specific subclasses, such as `NSDeleteCommand`, `NSGetCommand`, `NSMoveCommand`, and `NSSetCommand`. However, for some commands implemented by Cocoa, your application may need to provide a different implementation.

   For information on how to do this, see [Steps for Implementing a New or Modified Script Command](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delktk4ytg).
8. Implement `objectSpecifier` methods for scriptable classes in your object model. These methods describe the object and point to its parent in the object containment hierarchy (with the application object generally serving as the outermost container). They are invoked by an instance of `NSGetCommand` when it works with your application to obtain the requested information.

   If you’ve created helper classes to add scriptability to an existing application, these classes also need to implement object specifier methods.

   For more information, see [Implement Object Specifier Methods for Scriptable Classes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztoljrga4dsnbwg4).
9. Implement any new script command subclasses your application requires.

   Many applications provide unique capabilities, such as rotating an image or converting between two audio formats. To make these features scriptable, you may need to define new script command classes that are subclasses of `NSScriptCommand` or one of the other command classes provided by Cocoa.

   For more information, see [Subclasses for Standard AppleScript Commands](Cocoa%20Scripting%20Classes%20and%20Categories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztiljrgazdenjvgq) and[Script Commands Overview](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delktk42a).
10. To take advantage of Cocoa scripting support that works with document and window classes, your application should use the Cocoa document architecture.

    For more information, see [Use the Document Architecture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztoljrga4dsmjqgu).
11. To take advantage of Cocoa scripting support that works with text, your application can take advantage of Cocoa's built-in support.

    For more information, see [Access the Text Suite](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztoljrgaydcobsga).
12. Throughout the implementation process, test your application according to the test plan you developed.

    For tips and suggestions, see [Testing, Debugging, and Performance](Testing%2C%20Debugging%2C%20and%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobrfvbeeq2kivcukqy).

Every scriptable application must provide a definition of its scriptability information—the terminology available for use in scripts that target the application, as well as the implementation information used to support that terminology. This information includes a set of keys for the scriptable properties accessible in the application through key-value coding (described in [Provide Keys for Key-Value Coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztolktk4yq)).

If you developed an sdef file during the design phase, you've already completed this step. If not, see [Preparing a Scripting Definition File](Preparing%20a%20Scripting%20Definition%20File.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzzfvbeeq2cineuuri) for a description of the steps you take to create an sdef file and add scriptability information to it.

For information on working with the older scriptability format, see [Script Suite and Script Terminology Files](Script%20Suite%20and%20Script%20Terminology%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2dclkcijbueq2jjjcq).

The Model-View-Controller (MVC) paradigm is one of the central design patterns for Cocoa applications. MVC assigns objects in an application to one of three roles and recommends that you try to maintain a separation among objects of different roles.

- Model objects encapsulate the data and basic behaviors of the application; ideally, they have no explicit connection to the user interface.
- View objects present data to the user; they know how to display and possibly edit data, but typically do not encapsulate any data that is not specific to displaying or editing.
- Controller objects act as an intermediary, coordinating the exchange of data between the model and view objects.

Generally, the objects that you make scriptable should be model objects. The most efficient way for a script to perform a task generally involves modifying the model and is often not the same as the best way for a user to do the same task through the user interface (or view). This is consistent with how AppleScript works, and Cocoa accordingly gears its scripting support to the model layer.

A script should not require the user’s involvement, unless it is intended more as a macro than as a form of batch processing. In a macro-like script, the user must prepare things for the script (such as opening a window and creating or selecting certain objects), and then invoke it. If you anticipate that your application will be scripted for this purpose, you may want to provide scriptable behavior to the appropriate nonmodel objects, such as windows and selections. If so, be sure to confine your scripting support in nonmodel objects to those specific purposes.

Recall that key-value coding (KVC) is a mechanism for accessing object properties indirectly by key, where a key is just a string that represents a property name (such as `"xPosition"` for the horizontal coordinate of a graphic object). Cocoa scripting relies on KVC, both for finding the specified objects for a command to operate on and for getting and setting values in the specified objects.

Your application provides keys for its scriptable properties and elements in `class` definitions in its sdef file. The property and element names themselves serve as keys, unless you specify a different key explicitly. Cocoa scripting adjusts the key names as necessary according to the following rules, which are consistent with standard Cocoa naming conventions for accessors:

- For single-word property names, the name becomes the key. For example, an sdef property named `"width"` would result in a key of `"width"`.
- For multiple-word property names, Cocoa capitalizes each word of the name except the first word, then removes any spaces. For example, an sdef property named `"desktop position"` would result in a key of `"desktopPosition"`.
- For element names, Cocoa specifies a key by making a plural from the name. For example, `"word"` results in a key of `"words"` and `"document"` results in `"documents"`.

You can override the default naming conventions to specify arbitrary key values where necessary. For example, suppose you want a scripter to be able to use `color` in a script, but your application refers to the underlying property as `foregroundColor` (as in the `NSTextStorage` class). You can specify `"foregroundColor"` as the key for the `"color"` property by adding a `cocoa key` entry to the sdef `property` definition:

```
<property name="color" code="colr" ...
    <cocoa key="foregroundColor"/>
```

To support getting and setting scriptable properties and elements in your application, you define accessor methods that match the keys in your sdef, as described in [Maintain KVC Compliance](Getting%20and%20Setting%20Properties%20and%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvona). For additional information on default naming and working with keys, see [Cocoa Elements](Preparing%20a%20Scripting%20Definition%20File.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzxfuytcnbxgazta).

Once you have created an sdef file, you'll need to add it to the Xcode project for your application. Place the file in the project folder (or other appropriate location) and use Project > Add to Project, which also lets you add the sdef file to application targets. Adding the sdef file to the project automatically adds it to the Copy Bundle Resources build phase, so it will be included in the application.

To turn on Cocoa’s built-in scripting support, you add the following key to your application's `Info.plist` file:

```
    <key>NSAppleScriptEnabled</key>
    <string>YES</string>
```

To provide your application's scriptability information through an sdef file, you add a second key to the property list to specify the sdef file. Here's the entry for the Sketch application:

```
    <key>OSAScriptingDefinition</key>
    <string>Sketch.sdef</string>
```


An object specifier locates a scriptable object or objects within the containment hierarchy in which they reside.

When a script statement targets an application, the application may need to return a reply. For example, the result of a `get` command is an object or a list of objects. When Cocoa returns these objects in the reply Apple event, it does not return pointers to Objective-C objects, it returns object specifiers.

To obtain the object specifiers, Cocoa sends `objectSpecifier` messages to the objects to be returned. Therefore, for any class of object that is part of your containment hierarchy of scriptable objects, you must implement the `objectSpecifier` method. This method is declared in `NSScriptObjectSpecifiers`, a category on [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) that implements a version that just returns `nil`.

For more information, including code examples, see [Object Specifiers](Object%20Specifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmznknltc).

The [NSApplication](https://developer.apple.com/documentation/appkit/nsapplication), [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument), [NSDocumentController](https://developer.apple.com/documentation/appkit/nsdocumentcontroller), [NSWindow](https://developer.apple.com/documentation/appkit/nswindow), and [NSWindowController](https://developer.apple.com/documentation/appkit/nswindowcontroller) classes form the basic structure for the Cocoa document architecture. Together with the terminology defined in the Standard suite, these classes provide direct support for the standard AppleScript document scripting model, including classes such as `application`, `document`, and `window`. When you use these classes to implement a document-based application, that application automatically supports a number of scripting features.

For example, the `NSApplication`, `NSDocument`, and `NSWindow` classes are KVC-compliant for standard scriptable properties. `NSApplication` provides methods for accessing the application's documents as an ordered list. The `NSDocument` class provides support for the `close`, `print`, and `save` commands by implementing the `handleCloseScriptCommand:`, `handlePrintScriptCommand:`, and `handleSaveScriptCommand:` methods. `NSWindowScripting` also implements default versions of these methods, which in many cases pass control to the window's document. It also implements methods for scriptable access to window attributes, such as the close box, title bar, and so on.

Applications that take advantage of Cocoa’s document architecture put themselves in a better position to support scripting generally. A document in Cocoa applications typically owns and manages one or more model objects of the application. It therefore provides a hub for scripted access to the model objects in your application, which are the ones that load and save data.

Table 3-1 lists Cocoa classes that correspond to AppleScript classes in the Standard suite, along with attributes and relationships (properties and elements) used by those classes.

__Table 3-1__  Standard suite attributes and relationships

| Objective-C and AppleScript class | Attributes (script term, if different) | Relationships |
| [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject)  Implements the `item` AppleScript class. For any scriptable Objective-C class that inherits from `NSObject`, the AppleScript class it implements inherits from the `item` class (and inherits the `class` property and the `properties` property). | class name (`class`), properties |  |
| [NSApplication](https://developer.apple.com/documentation/appkit/nsapplication)  Implements the `application` AppleScript class. | name, active flag (`frontMost`), version | documents, windows (both accessible as ordered relationship) |
| [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument)  Implements the `document` AppleScript class. | location of the document's on-disk representation (`path`); last component of filename (`name`); edited flag (`modified`) |  |
| [NSWindow](https://developer.apple.com/documentation/appkit/nswindow)  Implements the `window` AppleScript class. | title (`name`); various binary-state attributes: closeable, floating, miniaturized, modal, resizable, titled, visible, zoomable | document |

The Text suite defines terminology that allows scripts to request or select textual elements at different levels of granularity: character, word, paragraph, or entire body of text. The `NSTextStorage` class, provided by the Application Kit, defines a corresponding set of methods for getting and setting scriptable properties of `NSTextStorage` objects.

To gain access to this text scripting support, use an `NSTextStorage` object as the content for one of your scriptable classes. The TextEdit sample code (available at `<Xcode>/Examples/AppKit/TextEdit`) demonstrates a scriptable application that supports text scripting, as well as scripting support for printing.

Table 3-2 lists Cocoa classes for working with text, along with attributes and relationships used by those classes.

__Table 3-2__  Text Suite Attributes and Relationships

| Class | Attributes (script term, if different) | Relationships |
| [NSTextStorage](https://developer.apple.com/documentation/uikit/nstextstorage) | font name (`name`), font size (`size`), foreground color (`color`) | attribute runs, characters, paragraphs, text, words |

[Next](Preparing%20a%20Scripting%20Definition%20File.md)[Previous](Designing%20for%20Scriptability.md)

