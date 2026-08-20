---
title: Interface Builder User Guide
apple_id: TP40005344
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/IB_UserGuide/BuildingaNibFile/BuildingaNibFile.html
archived_at: '2026-07-15T07:24:43.288363Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Interface Builder User Guide](Introduction.md)


[Next](Nib%20Objects.md)[Previous](Interface%20Builder%20Basic%20Concepts.md)

# Nib File Management

Nib files play an integral role in the development of your applications. They are a powerful type of resource that you use to store runtime objects and interface-related content. They are also the fundamental document type of the Interface Builder application.

Interface Builder 3.0 and later offer many options for creating and working with nib files themselves. Understanding these options can help save you time and effort during development. This chapter offers guidelines to help you create nib files that integrate well with your Xcode projects.

Files in the nib and xib formats play a very important role in the creation of applications. In their primary role, nib files simplify the code you have to write to create your application’s user interface. They provide a loadable set of objects that replace the code you would write to create windows, views, and other interface-related items. In some applications, nib files also provide a means to integrate these interface items with the existing objects in your application.

The nib and xib file formats themselves provide you with options for the development of your projects. Although they represent the same information, you use each type of file differently. The xib file format is preferred during development because it provides a SCM-friendly format, and because xib files can be compared with the diff command. At build time, Xcode automatically converts your project’s xib files to nib files so that they can be deployed with your application. If you have existing nib files, however, you can also continue saving to that same format.

Although the contents of a nib file can vary greatly in theory, in practice, there are usually a handful of standard configurations that developers include. The reason is that most developers use nib files for a very specific purpose: to load user interface items. This is particularly true for Carbon nib files, which can be used to store only user interface components, such as windows and menus. Nib files for other platforms offer more support for non interface components and for more complex configurations of your objects. For example, when you open a nib file for a Cocoa application, you might see any of the following items at the top level of the nib file:

- Window resources
- Menu resources (both menu bars and individual menus)
- Views
- Formatter objects
- Controller objects (view controllers, array controllers, object controllers, and so on)
- Core Data managed object contexts
- Program-specific custom objects
- Placeholder objects, including File’s Owner

Some of these objects must be at the top level of the nib file. For example, windows and menus must always be at the top level of a nib file. In addition, controller objects are almost always at the top level. This is because controller objects cannot be embedded inside windows, views, or menus. (Cells and formatters are special because they work in conjunction with a view or control to implement its appearance.) Most other view-based objects are typically situated inside a window or view, although they can appear at the top level of the nib file as well.

The following guidelines can help you create nib files that achieve your application design goals quickly and efficiently.

Most new projects in Xcode come with one or two preconfigured nib files. A mistake made by many developers who are new to Interface Builder is to place all of their application’s windows and menus in these one or two nib files. The reason for the mistake is often convenience. (The template project usually loads the preconfigured nib files automatically, which saves the developer from having to add more nib-loading code.) Unfortunately, relying on this convenience can often lead to diminished performance and added memory pressure on your application.

When a nib file is loaded into memory, it is an all-or-nothing endeavor. The nib-loading code has no way of knowing how many objects are in the file or which ones are important, so the entire file must be loaded into memory. From this in-memory data, individual objects are then instantiated. For Mac OS X and iOS applications, all of the objects in the nib file are instantiated right away so that outlet and action connections can be reestablished. If your application uses only some of the nib-file objects initially, having all of the objects in memory is a waste.

For all projects, it is better to design each nib file so that it contains only those objects that are needed immediately in a given situation. When loaded into memory, such a nib file uses the smallest amount of memory possible while still having everything it needs to get the job done. Here are some design choices to consider when organizing your nib files:

- For your application’s main nib file, include only your menu bar (or in the case of an iOS application, just the main window).
- For document nib files in Mac OS X, include only the document window and the objects (such as controllers) needed to display that window.
- For other nib files, focus the nib file on a key object, such as a single window or panel that you intend to display. All other objects in the nib file should then facilitate the immediate operation of that window or panel.
- For windows that change their embedded view hierarchies, if the hierarchy changes infrequently, consider storing any additional hierarchies in separate nib files. Load each view hierarchy only as it is used.

If you already have large nib files, you can use Interface Builder’s refactoring tools to break them into several smaller nib files. For information on how to use Interface Builder’s refactoring tools, see [Refactoring Your Nib Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmjrfvjvomjz). For information about how to load nib files explicitly from your code, see _[Resource Programming Guide](../../Cocoa/Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_.

In Cocoa and Cocoa Touch nib files, the File’s Owner placeholder object provides the key link between your application and the objects in the nib file. When you load the nib file, you must provide the nib-loading routine with a pointer to the object that should become the File’s Owner. As part of the loading process, the nib-loading code automatically recreates any connections between the object you specify and the nib file objects that have connections to the File’s Owner.

As you design the architecture of your application, it is important to consider which objects you want to manage your nib files. The presence of only one File’s Owner placeholder object is not without good reason. It is usually best to have a single object coordinate the loading and management of a nib file and its contents. This single point of contact provides the desired barrier between your application’s data model and the visual elements used to present that data model and is at the heart of model-view-controller design.

Beyond the File’s Owner object, you can create additional controller objects directly in your nib file to manage subsets of the nib file. Using multiple controllers in this way lets you compartmentalize the window’s behavior into more manageable chunks. For example, if your window has multiple panes of disparate information, you could create separate controller objects to manage each pane. Each controller would continue to go through the File’s Owner to obtain additional information.

In iOS applications, it is also possible to include placeholder objects besides File’s Owner in your nib file. These additional placeholder objects are almost always used to represent navigation controllers and other view controllers already in use by your application. The presence of these additional placeholder objects does not diminish the role of File’s Owner though. The File’s Owner object is still responsible for coordinating the overall behavior of the nib file’s contents.

The objects at the top level of a nib file represent the main objects of interest to your application. Although technically you can place almost any object at the top level of a nib file, in most cases, doing so is rarely practical or necessary. Most applications use nib files to load a particular piece of the user interface, usually a window or menu. For Carbon applications, windows and menus are the only thing you can include at the top level of a nib file.

In addition to windows and menus, nib files for Cocoa and Cocoa Touch applications can include controller objects and formatters at the top level. Creating these objects from the nib file is often more convenient than creating them programmatically. And if their entire purpose is to manage the objects inside the nib file, it is also more practical to include them as part of the nib file.

The nib file format is the original file format supported by early versions of Interface Builder. The nib format is still used today as the deployment format for object resources you load into your application at runtime. In Interface Builder 3.0, the nib format was expanded to include some additional design-time information. This updated version of the nib format is still backwards compatible with the nib-loading infrastructure but is not compatible with older versions of Interface Builder.

The xib file format was introduced in Interface Builder 3.0 as a development-time format and was conceived as a way to provide tighter integration with your Xcode projects, particularly in the areas of SCM support, diff support, and refactoring. Xcode automatically converts files in the xib format to the nib format at build time.

Because there are two supported file formats for Interface Builder documents, you have to choose which format to use for your own projects. If you’re developing for iOS, the choice is easy—you must use the xib file format for your project. For Mac OS X, you may use either the xib or nib file format. In almost every case, you should use the xib format. The nib format is recommended for a project only if the project target is an Interface Builder plug-in that depends on itself.

Interface Builder 3.0 and later fully supports opening nib files created with Interface Builder 2.5.x and earlier. Nib files created or modified with Interface Builder 3.2 and later can’t be opened with Interface Builder 2.5.x and earlier.

Because nib files can store user-visible strings, their contents must be localized along with the rest of your application during the localization process. Because nib files are external to your code, however, the localization process is straightforward. Like other resource types, you can store localized versions of your nib files in language-specific project directories of your application bundle.

For more information about the localization process for nib files, see [Localization](Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmjtfvjvomi).

To create a nib file in Interface builder, choose File > New. Interface Builder displays the template chooser for creating your nib file. From this panel, you select the target platform and the starting template you want to use.

The starting templates simplify the nib creation process by providing you with preconfigured nib files that you would use in typical situations. The templates also provide you with objects that are configured correctly for the target platform. Each application platform has subtle differences, both in what the nib file can contain and in the supported frameworks. For example, the Cocoa Touch platform supports classes from the UIKit framework while the Cocoa platform supports classes from the AppKit framework. The platform you choose therefore determines what content shows up in the library and inspectors.

The template chooser also includes nib templates for use with the IB SDK. These nib files are Cocoa nib files that you use to create Interface Builder plug-ins, which are add-on modules used to extend the set of objects in the library. For more information on how to create plug-ins, see _[Interface Builder Plug-In Programming Guide](../Interface%20Builder%20Plug-In%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmrt)_.

After creating a new nib file, the next step is to add your custom objects to it. For information about the objects you can include in nib files, see [Nib Objects](Nib%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmjsfvjvomi).

When you are ready to save your Interface Builder document, choose File > Save from the menu. If you are working on a version 2.x nib file, Interface Builder transparently upgrades it to version 3.x. For the iOS platform, you must save your nib file using the version 3.x xib file format (`.xib` extension). For the Mac OS X platform, you can save your document using one of two file formats:

- Version 3.x development-time format (`.xib` extension)
- Version 3.x deployment format (`.nib` extension)

Depending on the situation and your needs, you may find yourself using one or both of these formats for a given project. For guidance on which format to choose for your project, see [Choosing the Best File Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmjrfvjvomy) and the following sections.

The development-time xib file format is a text-based flat-file format introduced in Interface Builder 3.0. This format was added to make it easier to check Interface Builder documents in and out of source-control systems. Files of this type have a `.xib` extension and can be used only within the Xcode and Interface Builder environments. You cannot load `.xib` files at runtime from your application code. Instead, when you build your Xcode project, Xcode compiles this format down into a deployable nib file and adds that file to your project bundle.

The xib file format is the default format for Interface Builder. You should use this format for any new (or existing) projects you are developing using version 3.0 or later of Xcode and Interface Builder. To save a file using the xib format, do the following:

1. Choose File > Save (or File > Save As) to display the Save panel.
2. Select the XIB 3.x format from the File Type pop-up menu.
3. Click Save.

The deployment nib file format provides compatibility with, and facilitates the direct modification of, existing nib files. You might use this format when modifying a nib file for an existing project or when creating nib files for an Interface Builder plug-in that depends on itself.

Interface Builder supports version 3.x of the deployment format. The 3.x version is a more modern format supported by Interface Builder 3.0 and later. This format supports new objects that are available only in Interface Builder 3.0 and later.

To save a file using the deployment nib file format, do the following:

1. Choose File > Save (or File > Save As) to display the Save panel.
2. Select the NIB 3.x format from the File Type pop-up menu.
3. Click Save.

To view the image and sound resources contained in your Xcode project, use the media tab of the Library window. This tab displays your Xcode project’s custom resources and some of the common resources available in the system. The contents of this tab are essentially read-only and intended as a way to browse your project resources without having to go back to Xcode.

Views that support image and sound resources usually provide a configurable attribute in their inspector window for selecting the appropriate file from the media browser. You can also integrate image and sound resources directly into your nib file using the following techniques.

- Drag an image from the media browser and drop it onto a window to create an image view configured with that image.
- Drag an image from the media browser and drop it onto a toolbar, button bar, or tab bar (depending on the platform) to create a new item for that view.
- Drag an image from the media browser and drop it onto a control to assign that image to that control’s cell (where applicable).

Although you can reference image and sound resources from your nib file, those resources are still stored outside of the nib file itself. Interface Builder gets the list of available resources from the Xcode project associated with your nib file. Therefore, if you want to use image and sound resources in your nib files, add them to your Xcode project.

In addition to your project resources, the Cocoa and Cocoa Touch platforms make some standard system images available for applications to use. These images are displayed in the Media browser by default but you can also refer to these images by name. The reference documentation for the associated platform lists the constants containing the name strings you use to access them. In nearly all cases, the names used by Interface Builder are a shortened version of the constant name. For example, in Cocoa applications, Interface Builder uses the string “NSBonjour” to represent the image identified by the `NSImageNameBonjour` constant. For a list of constants you can use in Cocoa applications, see _[NSImage Class Reference](https://developer.apple.com/documentation/appkit/nsimage)_. For Cocoa Touch applications, these constants are spread across several classes in _[UIKit Framework Reference](https://developer.apple.com/documentation/uikit)_.

When in doubt about whether a control supports image or sound resources, check the inspector window. If a control includes an image or sound field as one of its attributes, then you can assign the appropriate resource to it. (For example, you can assign both an image and sound resource to a push button control in Cocoa.) In addition to typing the resource name in the appropriate field, the inspector window typically includes a drop-down list that includes the known resources from your Xcode project.

It is a common mistake for developers to use their application’s main nib file to store several unrelated windows and controller objects. A better design pattern is to use several smaller nib files, each containing only the objects and controllers needed to implement a single window or interface. Smaller nib files promote better efficiency and a smaller memory footprint for your application. If your application already has large nib files, however, breaking up those files by hand is difficult, tedious, and error-prone. To help with the process, Interface Builder provides a refactoring tool to do the job for you.

To use Interface Builder’s refactoring tool, open the nib file you want to refactor and choose File > Decompose Interface. Interface Builder iterates through the file’s contents to build a map of the object relationships in the nib file. The tool looks at connected outlets, actions, bindings, and at the window and view hierarchies. From that map, it then identifies distinct, unrelated groups of objects and creates new nib files for each distinct group. The command does not change the contents of your original nib file.

If you want to adapt an existing iPhone user interface for iPad, you can use one of Interface Builder’s Create commands to create a new iPad document. Conversely, to adapt an existing iPad interface for iPhone and iPod touch, you can use a Create command to create a new iPhone document. The Create commands are intended to help you get started designing a new interface; they do not exactly replicate the existing interface. After creating an iPhone version of an iPad user interface, for example, you still need to modify the new interface for the target device.

To use this feature, open the nib file you want to convert and choose one of the two Create commands in the File menu. Interface Builder creates an untitled document according to the command you choose. If you choose File > Create iPad Version, the new document contains an iPhone/iPod touch interface without autosizing the views. If you choose File > Create iPad Version Using Autosizing Masks, Interface Builder respects the current autosizing settings in the views being converted. Two complementary Create commands exist for iPad documents.

[Next](Nib%20Objects.md)[Previous](Interface%20Builder%20Basic%20Concepts.md)

