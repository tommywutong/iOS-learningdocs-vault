---
title: Code Loading Programming Topics
apple_id: 10000052i
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/Tasks/Componentizing.html
archived_at: '2026-07-15T07:16:29.926215Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Loading Programming Topics](Introduction%20to%20Dynamically%20Loading%20Code.md)


[Next](Creating%20Plug-in%20Architectures.md)[Previous](Creating%20Loadable%20Bundles.md)

# Building Applications with Multiple Bundles

There are several different reasons to build an application as multiple loadable bundles and several different ways to do it. This section describes how to use Cocoa to build an application in modular, dynamically loadable components.

Architecting a Cocoa application around multiple loadable bundles gives you several advantages:

- You can delay loading code until it is needed.
- You can modularize your application into pieces that can be developed and compiled independently.
- You can make your application extensible.

These goals can be met at two hierarchical levels—one for large-scale application organization and the other for small-scale features:

- To enable delayed (“lazy”) code loading and modularization, you can use multiple loadable bundles for large-scale application components such as preferences windows and document types.
- To enable extensibility, you can design a plug-in architecture. This way, you and other developers can easily add features without access to the application’s source code.

For more information about delayed loading and modularization, see [Lazy Bundle Loading](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tkljzhe3dgmy) and [Modularizing with Loadable Bundles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tkljzhe3dioa) in this section.

For information about designing and implementing plug-in architectures, see [Plug-in Architectures](Plug-in%20Architectures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3telkcineuiqsbivfa) and [Creating Plug-in Architectures](Creating%20Plug-in%20Architectures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tmlkdjjbeircdifba).

You may need to access instances of classes in a loadable bundle in potentially many places in your application. If you use a pointer to such objects directly, you need to check to see if the pointer has been initialized with an object before using it. This adds an extra step to using the object every time you use it and introduces the potential for hard-to-find mistakes such as sending messages to `nil` pointers.

You can avoid this complexity by just adding accessor methods for any instances loaded from a bundle. The accessor method performs all the necessary checks for you: if the object is already initialized, it just returns it; otherwise, it loads the bundle, initializes the object, and then returns it. The rest of your application code can then just use the accessor method to use the object and never has to worry if the object has been initialized yet or not.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tkljrgaydambzfvbecsscizcugri) is an example of an accessor method for an object initialized lazily from the principal class of a bundle. An explanation follows the listing.

__Listing 1__  Accessor method for an object initialized from a loadable bundle’s class

```objc
- (id)bundleObject
{
    if(!_bundleObject)                                                 // 1
    {
        NSString *bundlePath = [[[NSBundle mainBundle] builtInPlugInsPath]
                  stringByAppendingPathComponent:@"MyBundle.bundle"];  // 2
        NSBundle *bundle = [NSBundle bundleWithPath:bundlePath];       // 3

        if(bundle)
        {
            Class principalClass = [bundle principalClass];            // 4

            if(principalClass)
            {
                _bundleObject = [[principalClass alloc] init];         // 5
            }
        }
    }

    return _bundleObject;                                              // 6
}
```

Here’s what the code does:

1. Checks to see if the instance variable `_bundleObject` exists. If it already exists, the body of the `if` statement is skipped.
2. Finds the path for the bundle. In this example, the path is hard-coded, although in most applications it is specified in a more sophisticated manner.
3. Retrieves the NSBundle object corresponding to the bundle path. This message implicitly creates an NSBundle object if one does not already exist for the bundle.
4. If the NSBundle object is valid, gets the principal class of the bundle. This message lazily loads the bundle’s executable code if it has not yet been loaded.
5. If the principal class exists, the `_bundleObject` instance variable is allocated and initialized.
6. Finally, `_bundleObject` is returned. If the loading process failed, `_bundleObject` maintains a value of `nil`.

There are a number of reasons to modularize your application with loadable bundles. You may want to split up development work so that different application components can be rebuilt without recompiling the whole application. You may want to delay loading different application components. Or you may want to do both.

To accomplish these goals, you will likely want to do one of the following, or both:

- Separate code components into different bundles for easier division of development labor.
- Separate each main window and associated controller code into its own loadable bundle.

The next two sections describe how to perform these tasks.

To create loadable bundles for code components, you can either create a new Xcode project or add a target to an existing one. If your goal is division of development labor, you probably want a separate project for each bundle. If you just want to delay loading code, you can just add a new target to the application project.

In general, the process is as follows:

1. Create the bundle containing the code component.
2. Copy the bundle to the application bundle’s “plug-in” directory.
3. Write the application to load and use the code from the bundle.

The following subsections describe the specific steps you need to take to accomplish these tasks.

To create the loadable bundle, you need to first decide what code this bundle will contain, and what class you want to serve as the principal class—the entry point. Once you have figured out what you want the bundle to contain, you can build a bundle project or target.

The process for creating a Xcode project for a loadable bundle is described in [Creating Loadable Bundles](Creating%20Loadable%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tilkdjjbeircdifba).

Adding a new target to an existing project follows a similar pattern. Instead of creating a new project, however, perform the following steps to add a new target to an existing project:

1. Open the application project in Xcode.
2. Choose New Target… from the Project menu.
3. Choose Bundle for the target type and click Next.
4. Give the target a name in the Target Name field.
5. Ensure that your project is selected in the Add To Project pop-up menu and click Finish.
6. In the project window, make sure the Files tab is selected.
7. Choose your target from the target pop-up menu.
8. Click the checkboxes next to all the files you want included in this bundle. Make sure you include `Cocoa.framework` in the Frameworks > Linked Frameworks group. Be sure not to include implementations that appear in your application.
9. Modify settings for the bundle target as described in [Modifying Target Settings](Creating%20Loadable%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tiljzhe3dana).

To copy loadable bundles to the application bundle, you add a copy build phase to the application target, which copies the loadable bundle to the application bundle’s “plug-ins” directory.

To set up a copy build phase, go through the following steps:

1. Add the built bundle to your project in the Files tab.
2. Click the Targets tab, and view the application target.
3. Under Build Phases in the target pane, choose the last build phase (usually Frameworks & Libraries). This tells Xcode where to put the next build phase.
4. Choose New Build Phase > New Copy Files Build Phase from the Project menu.
5. In the Copy Files pane, choose Plug-ins from the pop-up menu labeled “Where:”.
6. Click the Files tab in the main project pane.
7. Drag the bundle from the list of project files to the box labeled “Files:” in the Copy Files section of the target pane.

Now, when you build your application, the bundle is copied to the `PlugIns` directory of the application bundle, giving you easy access to it from your code. You can add additional bundles to the same copy phase for additional components.

The generalized process for loading bundles from the application’s `PlugIns` directory is the same as described in [Loading Bundles](Loading%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tglkdjjbeircdifba).

In applications that use a small number of bundles for large-scale application components, the easiest way to access the code is through a lazy accessor method. [Lazy Bundle Loading](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tkljzhe3dgmy) describes how to lazily instantiate an object from a bundle.

In many applications, a window is associated with some code to manage the window, typically a subclass of NSWindowController. NSWindowController provides built-in functionality to lazily load the window’s nib file. You can go a step further and lazily load the code for the NSWindowController subclass, which in turn may load the nib file.

In this situation, the nib file is packaged in a loadable bundle with the code for its associated window controller class. The application can then load the code for the window controller only when it is first needed and the window controller can load the nib file for the window only when it is needed.

This technique is especially useful for plug-in architectures, where each plug-in may be associated with a window. For example, each filter plug-in in a graphics application might have an associated window that is used to configure settings for the filter. This also applies to static situations as well, where large application components correspond to different windows—for example, a circuit layout window and a graph window in a circuit simulation application.

The process for building a bundle for a window and its associated code consists of these two steps:

1. Create the bundle containing the window and window controller code.
2. Write the application code to load and use the bundled window controller.

The following subsections describe this process in detail.

Building a bundle for a window and associated window controller is essentially the same as described in [Loading Bundles](Loading%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tglkdjjbeircdifba). In addition, you need to package a nib file in the bundle project containing a window and a window controller class associated with the window.

Once you have a new Cocoa bundle project, create the nib file and add it to your project:

1. Make sure your bundle project is open in Xcode.
2. Launch Interface Builder.
3. Choose New… from the File menu.
4. In the Starting Point window, choose Empty under the Cocoa group.
5. Choose Save As… from the File menu.
6. Navigate to _language_`.lproj/` in your bundle project’s directory, where _language_ is the language code for the nib file—for example, `English` or `en`.
7. Click Save.
8. In the Add File sheet, select the bundle target under Add to Targets, and click Add.

Next, create the window controller class:

1. Create an NSWindowController subclass.
2. Add any outlets and actions you want to add to the class.
3. Create source files for the class in your Xcode project.
4. Set the Custom Class for the File’s Owner proxy to your subclass.

Now you can create the window itself and hook everything up:

1. Add a new window object from the Cocoa-Windows palette and construct it with user interface elements.
2. Connect the `window` outlet of the File’s Owner to the newly created window and add any other connections you need to make between the controller and user interface elements.

Finally, write the code for the window controller class in Xcode. The one required method tells NSWindowController what nib file to use:

```objc
- (NSString *)windowNibName
{
    // Replace MyWindowController with the name of your window
    return @"MyWindowController";
}
```


As with other code components, window controller bundles are best accessed through lazy accessor methods. [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tkljrgaytcnzqfvbecssjjfbusry) shows the implementation for such a method.

__Listing 2__  Accessor method for bundled window controller

```objc
- (NSWindowController *)bundledWindowController
{
    // Assume _bundledWindowController is a private instance variable
    // of type id or NSWindowController *.
    if(!_bundledWindowController)
    {
        NSString *bundlePath = [[[NSBundle mainBundle] builtInPlugInsPath]
                         stringByAppendingPathComponent:@"MyBundle.bundle"];
        NSBundle *windowBundle = [NSBundle bundleWithPath:bundlePath];

        if(windowBundle)
        {
            Class windowControllerClass = [windowBundle principalClass];
            if(windowControllerClass)
            {
                _bundledWindowController = [[windowControllerClass
                                                              alloc] init];
            }
        }
    }

    return _bundledWindowController;
}
```

The rest of your application code should use the accessor method to refer to the object. For example, this line of code shows the window:

```
[[self bundledWindowController] showWindow:self];
```

Implicit in this example are potentially two lazy loading operations. First, the code for the window controller is loaded when the `principalClass` message is sent. Also, the window’s nib file is loaded when the `showWindow:` message is sent.

[Next](Creating%20Plug-in%20Architectures.md)[Previous](Creating%20Loadable%20Bundles.md)

