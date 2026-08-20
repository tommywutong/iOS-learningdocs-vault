---
title: Interface Builder Plug-In Programming Guide
apple_id: TP40004323
resource_type: Guide
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/IBPlugInGuide/DesigningControlsViews/DesigningControlsViews.html
archived_at: '2026-07-15T07:24:30.627868Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Interface Builder Plug-In Programming Guide](Introduction.md)


[Next](The%20Plug-in%20Object.md)[Previous](Plug-in%20Quick%20Start.md)

# Preparing Your Custom Objects

As you develop your custom objects, there are some steps you can take to ensure that the integration of those objects into Interface Builder is a smooth process. In many situations, Interface Builder relies on your objects to provide the information needed to initiate certain actions. Wherever possible, Interface Builder relies on standard Cocoa protocols to get the information it needs, but some information, such as your object’s inspector class, must be obtained using custom methods.

This chapter provides you with the guidelines you should be following when designing your objects to ensure that they are compatible with Interface Builder later. Many of these guidelines apply to the code for your custom objects and not for the code you put into your plug-in. Some of them are relevant to your plug-in, however, and are called out as such.

Interface Builder uses several standard Cocoa protocols to interact with your objects. You must support these protocols to ensure your objects behave properly in the Interface Builder environment.

- Make sure your custom object is key-value observable (KVO). For more information, see _[Key-Value Observing Programming Guide](../../Cocoa/Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_.
- Make sure your custom object is key-value coding (KVC) compliant. For more information, see _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_.
- If your custom object has settable attributes, make sure it conforms to the `NSCoding` protocol so that those attributes can be archived and unarchived. For more information, see _[Archives and Serializations Programming Guide](../../Cocoa/Archives%20and%20Serializations%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2do2i)_.

These protocols make it possible for Interface Builder to offer features such as undo support, pasteboard support, and the automatic refreshing of inspector data for free to your plug-in. You should already be supporting these protocols in your custom code anyway and doing so should not be a significant burden.

If for some reason you cannot support these protocols directly in your object framework, you should at least add comparable support inside your plug-in. Simply create wrapper methods in your plug-in that mimic the behavior of the KVC, KVO, and archiving methods but call through to your object’s real accessors behind the scenes. While such a configuration is not optimal, it does provide the overall support Interface Builder needs.

Before Interface Builder can access any attributes of your custom objects, you must register those attributes in your plug-in code. One of the category methods you must implement for each of your custom objects is the `ibPopulateKeyPaths:` method. Interface Builder calls this method early on, passing it an array of mutable sets, each of which contains a specific type of attribute. To register your object’s design-time attributes, you add the key paths for those attributes to these sets.

Listing 3-1 shows a sample implementation of the `ibPopulateKeyPaths:` method for the cell of a control. In this case, the cell has two direct attributes: a title string and a font. The cell also has a pointer to its parent view, which in this case is the control that owns it. Because the parent view can also be manipulated in Interface Builder, it is added to the to-one relationship set.

__Listing 3-1__  Registering the attributes of a custom object

```objc
- (void)ibPopulateKeyPaths:(NSMutableDictionary *)keyPaths
{
    // Always call super.
    [super ibPopulateKeyPaths:keyPaths];

    // Add any custom attributes.
    [[keyPaths objectForKey:IBAttributeKeyPaths] addObjectsFromArray:
                [NSArray arrayWithObjects:@"title", @"font", nil]];
    [[keyPaths objectForKey:IBToOneRelationshipKeyPaths] addObjectsFromArray:
                [NSArray arrayWithObjects:@"parentView", nil]];
}
```

Interface Builder monitors the attributes you register using key-value observing notifications. Whenever a change occurs to one of your object’s attributes, Interface Builder performs several important tasks. First, it records the change with the current undo manager object. Second, if the change originated in the inspector window, it notifies the object that it should redisplay itself. (Conversely, if the change originated in the window, Interface Builder may notify the appropriate inspector object to refresh itself.)

For a detailed description of the `ibPopulateKeyPaths:` method and how you use it to register your properties, see the method description in _NSObject Interface Builder Kit Additions Reference_.

As you design your custom objects, there are some guidelines that, if followed, will make it easier for you to integrate those objects into Interface Builder. Many of these guidelines offer benefits beyond just Interface Builder integration, however, and should be considered in your design plans regardless.

When creating the setter methods for your object’s attributes, be sure that each setter method affects only its target attribute. Interface Builder makes extensive use of your object’s getter and setter methods to implement undo support. Creating cascading setter methods—that is, setter methods that call additional setter methods—creates extra work to manage the undo stack and may incur a performance penalty.

When implementing a custom object, always use the object’s setter and getter methods to access attributes instead of the underlying instance variable. Interface Builder implements undo support by monitoring all calls to your setter and getter methods through key-value observing. If you call your own getter and setter methods when responding to user actions, Interface Builder can make sure that those actions are recorded on the undo stack.

If changing an attribute affects the appearance of your view or control, be sure to call the `setNeedsDisplay:` method inside the corresponding setter method. Because Interface Builder manages the undo stack, it may call your setter methods at any time to undo or redo a change. If that happens, your object’s setter method may be the only chance it has to refresh the view.

Be aware that in order to make your views and controls interact with it, Interface builder defines additional methods on the `NSObject` and `NSView` classes. Interface Builder uses these methods extensively at runtime to discover information about a particular object. These methods are therefore some of the more important methods for you to implement in your plug-in. Rather than implement the Interface Builder-specific methods in your object’s main implementation file, you should always place them in a category that is defined only in your Interface Builder plug-in.

Once you have your objects designed, you need to package them in a framework that both your client applications and Interface Builder can use. The default Xcode project template for plug-ins includes a target for a custom framework. You can use this target or create one of your own and configure it for your objects. Frameworks are the cleanest way to distribute your custom objects both to your Interface Builder plug-in and to the applications that might use your objects. A framework also lets you maintain a single set of source files and build a single distributable binary package.

When building your framework, be sure to include your Interface Builder plug-in in the `Resources` directory of the framework. When the user loads a nib file, Interface Builder checks for any linked-in frameworks in the associated Xcode project. If those frameworks contain a bundle with an `.ibplugin` extension, Interface Builder automatically loads that plug-in before it opens the nib file.

A class description is a property-list file that enumerates the outlets and actions of your class and also provides other important information to Interface Builder. Class description files reside in your plug-in bundle and should be created from your plug-in’s Xcode project. When your plug-in is loaded, Interface Builder searches its `Resources` directory for any files with the `classdescription` filename extension and reads their contents. It uses the information in those files to configure the connections dialogs and inspector windows with the actions and outlets you specify.

The default Xcode project contains a class description file for you to modify. If your plug-in supports multiple objects, you can add additional class description files as needed. When creating new class description files, be sure to update your plug-in target’s Copy Bundle Resources build phase to include the new files.

Listing 3-2 shows a sample class description file for a custom view. This view has a single outlet used to set the object’s delegate and two action methods. The first action can be sent by any object but the second must be sent by a view, a condition Interface Builder enforces at design time.

__Listing 3-2__  Class description for a custom view

```
{
    ClassName = MyCustomView;
    SuperClass = NSView;
    Outlets = {
            delegate = id;
    };
    Actions = {
            "myCustomAction:" = id;
            "myOtherCustomAction:" = NSView;
    };
}
```

You should always provide a class description for each of your custom objects. Each class should have its own class description file and although the exact filename is not important, it is customary to name each class description file after the class it represents. Each class description file should contain the the class name and superclass name information at a minimum. If the class has outlets and actions, you should list those as well; otherwise, you may omit the corresponding sections entirely.

All objects that appear in the library should have some sort of descriptive information describing their purpose and behavior. When creating your plug-in, you associate this information with the library template objects containing your custom objects. Library object templates contain several attributes that not only describe the purpose of your custom object but also specify its location in the library. Table 3-1 lists the basic attributes and how you configure them.

__Table 3-1__  Library object template attributes

| Attribute | Description |
| `Label` | The name of your custom object. Names should be succinct yet descriptive. Avoid using class names and framework prefixes. |
| `Path` | The path to the group containing the object. If you do not specify path information, all objects appear as children of your plug-in. You can specify additional paths to group objects hierarchically. Paths start with a leading forward slash character and use additional forward slashes to separate hierarchical groups. For example, Cocoa uses the path `/Views & Cells/Buttons` to specify the group for button objects. Interface Builder automatically creates folders in the library window for any path names you specify and nests those folders under your plug-in. |
| `Summary` | A compact description of your object. Summary text should be no more than 8 to 12 words and should take the form “An _<object>_ for _<task>_.“ Summary descriptions appear in the item pane when descriptions are enabled. They are also used as the tool tip text whenever the user hovers the mouse over the corresponding item. |
| `Description` | A more complete description of your object. Descriptions should consist of 2 or 3 sentences describing your object’s purpose and behavior. These descriptions appear in the documentation pane of the library window when an item is selected. |
| `Scaling` | The scaling option for your custom object. This determines the technique used to scale your object from its iconic form in the library to its full-fledged form in a nib file. The Image Transformation option causes Interface Builder to scale a bitmap version of your library entry. The View Transformation option causes Interface Builder to send `setFrame:` messages to the actual view to create the animation. The Default mode chooses the mode that looks best for the given object. |
| `Rep. Class` | If you have multiple object templates that represent the same class, you should check this box on one of them, to indicate which template is used when the class is dragged from the classes portion of the library.  A good example is `NSButton`. There are many `NSButton` templates in the Cocoa library—a push button, a gradient button, several rounded buttons, and so on. When you switch to the Classes tab at the top of the library window and drag `NSButton` to the design surface, the beveled style is used because that template has the "Represented Class Template" checkbox selected. |

[Next](The%20Plug-in%20Object.md)[Previous](Plug-in%20Quick%20Start.md)

