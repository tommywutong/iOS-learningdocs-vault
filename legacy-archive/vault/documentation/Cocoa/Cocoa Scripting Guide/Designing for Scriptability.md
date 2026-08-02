---
title: Cocoa Scripting Guide
apple_id: TP40002164
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_design_apps/SAppsDesignApp.html
archived_at: '2026-07-15T07:18:50.785760Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Scripting Guide](Introduction%20to%20Cocoa%20Scripting%20Guide.md)


[Next](Implementing%20a%20Scriptable%20Application.md)[Previous](Overview%20of%20Cocoa%20Support%20for%20Scriptable%20Applications.md)

# Designing for Scriptability

This chapter provides high-level checklists for designing a new scriptable Cocoa application and adding scriptability to an existing application.

Whether you’re designing a Cocoa application from scratch or adding a new feature to an existing application, you go through a standard set of design steps, tailored to your experience, the systems you work with, and the project at hand. The process is no different when you’re designing for scriptability.

The following steps provide an outline for your design process, but are not intended to be comprehensive. However, links are provided to additional design information in this and other documents.

To design a new scriptable Cocoa application, consider using the following steps:

1. For your overall application design, work with the Model-View-Controller (MVC) design pattern, which is widely followed in Cocoa applications.

   Good scripting support generally calls for scripting the model, rather than the view layer. For more information, see [Concentrate Scriptable Behavior in Model Objects](Implementing%20a%20Scriptable%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztoljrga4dqmbwgy).

   Cocoa bindings and Core Data also work with the MVC design pattern. See [Interaction With Cocoa Bindings and Core Data](Overview%20of%20Cocoa%20Support%20for%20Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzwfvjvomjt) for more information.
2. Think about scripting very early in your design.

   When you first start defining the requirements for your application, consider the kinds of features you’ll want to make scriptable and how users might script those features to automate operations with your application. This can help provide insight into the overall goals for your application.

   You'll want the terms you specify to look natural in AppleScript's English-like grammar. Scripting terms won't necessarily be an exact match for the terminology you use within your application's code.

   _[Scripting Interface Guidelines](https://developer.apple.com/library/archive/technotes/tn2002/tn2106.html#//apple_ref/doc/uid/DTS10003199)_ supplies valuable information on how to provide a clean and consistent scripting interface for your application.
3. Work out the design for your AppleScript object model—the objects scripters will use in their scripts, and the inheritance and containment relationships between them.

   This includes identifying the scriptable properties of your scriptable classes and providing a set of keys to identify them. (You'll use this information later, in your sdef file, to provide the keys Cocoa scripting uses with key-value coding. However, in many cases, you won't need to specify keys explicitly—Cocoa can determine them automatically by applying its default rules to the property names.)

   For more information, see [Provide Keys for Key-Value Coding](Implementing%20a%20Scriptable%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztolktk4yq).
4. Determine which of the standard AppleScript commands your application will support. Cocoa provides support for most of the standard scripting commands, including `close`, `count`, `delete`, `duplicate`, `exists`, `get`, `make`, `move`, `open`, `print`, `quit`, `save`, and `set`, but your application has to do some work too.

   Scripters expect your application to support whichever of these commands make sense for it, and to make the commands work in standard ways. By meeting these expectations, you gain two kinds of leverage:

   - You can take advantage of scripters’ existing knowledge, so that your application’s scriptability is easier for them to understand and use (meaning fewer complaints and support calls).
   - Supporting a few commands can provide a lot of scriptability—for example, if you provide access through the `get` and `set` commands to five properties in each of the two most important classes in your application, that’s 20 scriptable operations—2 commands times 5 properties times 2 classes. In many cases, support for the `get` and `set` commands requires relatively little coding effort.
5. To support application-specific operations that can’t be handled by one of the Cocoa scripting command classes, define new script command subclasses for those operations.

   Keep in mind that you can often accomplish a goal with an existing command. For example, rather than define a new `rename` command, you can use the existing `set` command to set the `name` property of an object to the new name.

   For more information, see [Script Commands](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delkcijbueq2jjjcq).
6. Create the actual scripting definition file (sdef) for your application.

   This is listed as a design step because it is possible to define an sdef and actually compile scripts against it in a test or skeleton application before you’ve written code to support your scriptability. You can even let scripters in your target audience work with your application's terminology and provide feedback.

   Doing this step early can help immensely in refining your scripting support and ensuring that it is user-friendly for scripters. In addition, your AppleScript dictionary can serve as a useful design document for the entire application.

   Although you can wait to write your scripting terminology until you implement the application, writing it first will help to ensure consistency and usability. And during implementation, you don't need to implement support for your terminology all at once—you can do it incrementally as you become more familiar with the process.

   For information on creating an sdef file, see [Preparing a Scripting Definition File](Preparing%20a%20Scripting%20Definition%20File.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzzfvbeeq2cineuuri).
7. Design the application classes that will support scriptability. Make sure these classes support the scripting object model you have defined, including both inheritance and containment relationships.

   You must name the accessor methods for scriptable properties of these classes to match the keys you defined earlier, as described in [Maintain KVC Compliance](Getting%20and%20Setting%20Properties%20and%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvona).
8. Plan for testing.

   Your testing should include creation and regular execution of AppleScript scripts that exercise the application’s functionality. The ability to automate your testing and to more easily perform regression testing is one of the big gains of making your application scriptable.

   Performance represents another important area of testing for most applications. For a general introduction, see _[Performance Starting Point for OS X](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Performance/index.html#//apple_ref/doc/uid/TP30001082)_. For issues specific to scriptable applications, see [Performance Issues for Scriptability](Testing%2C%20Debugging%2C%20and%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobrfvjvomi).

   And of course, you should also plan for unit testing or other kinds of testing that you customarily use.

   For issues to cover in your test plan, see [Scriptability Test Plan](Testing%2C%20Debugging%2C%20and%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobrfvjvomq).

To add scriptability to an existing Cocoa application, consider using the following steps. (Some steps are abbreviated, where they repeat those found in [Designing a New Scriptable Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzyfuytcmzxgu3tq).)

1. If time allows, and especially if there are other reasons to redesign the application, consider a major redesign, following the steps described previously for designing a new scriptable application.
2. Experiment with creating a scripting definition file for your application.

   As noted previously, you can compile scripts against your terminology before you’ve written any code. That helps you identify the scripting objects and terminology you want to provide for scripters (your AppleScript object model), as well as the underlying application information you need to expose to support that terminology. It also helps determine the scale of the effort to make the application scriptable.
3. In classes containing information you want to make scriptable, make use of any instance variables or accessor methods that are already key-value coding compliant.

   If not, you can add KVC-compliant accessors to support scriptability. One convenient way to do this is through the use of an Objective-C category. This approach is most appropriate in the case where you are primarily making existing properties and elements scriptable. It can also be useful when you don't have free access to the existing code.
4. Consider designing scriptable “helper” classes to implement the object hierarchy you expose to scripters. These classes can maintain references to application objects that contain the actual information scripters will be working with.

   You can define helper classes from scratch, adding properties and relationships as needed to support your AppleScript object model. To access the underlying data, you have to invoke methods in existing classes—this is where you’re likely to find the most complexity in retrofitting an existing application.

   This approach is most appropriate in the case where you need to pull together properties from multiple application classes to represent one AppleScript object model class, or where a category won't work because you need to add new instance variables.
5. Determine which of the standard AppleScript commands your application will support and plan new script command subclasses for any additional commands that are needed.
6. Plan for testing, using both AppleScript scripts and other testing options available to you.

[Next](Implementing%20a%20Scriptable%20Application.md)[Previous](Overview%20of%20Cocoa%20Support%20for%20Scriptable%20Applications.md)

