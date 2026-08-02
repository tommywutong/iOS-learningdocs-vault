---
title: Xcode Workspace Guide
apple_id: TP40006920
resource_type: Guide
platform: iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeWorkspace/020-Project_Organization/project_organization.html
archived_at: '2026-07-15T07:30:11.783799Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Workspace Guide](Introduction.md)


[Next](File%20Management.md)[Previous](The%20Project%20Window.md)

# Project Organization

Some of the design decisions you make when you first set up a project—such as how many targets you need for your software development effort—affect your entire development experience. This chapter provides tips for partitioning and arranging the code and resources for a product as you develop with Xcode. It also describes some of the features Xcode provides that let you group information for rapid and easy access. For instance, you can save commonly accessed locations as bookmarks or in the favorites bar, or you can document project items by adding comments to them.

The following are some general guidelines for developing your software in Xcode. In subsequent sections, you’ll get more detailed information to flesh out these tips.

- Follow standard software development practice to factor your software into logical units of reasonable size, which you can implement as applications, shared libraries, tools, plug-ins, and so on. In Xcode, each of these products requires one target.
- Put together projects and targets based on how you answer the following sorts of questions:

  - How do the products interact?
  - How many individuals (or teams) will be working on each product?
  - Do the products use different source control systems?
  - Must the products run on different versions of the target platform?
- For smaller development tasks, it generally makes sense to keep targets for related products in a single project.
- For products that are reasonably separate, and especially if they are to be implemented by separate teams, use multiple projects.
- Use cross-project references when targets in one project need to depend on targets in other projects.
- Use the information in Build Locations to ensure that a target can access the build products of other targets when needed.

To develop software with Xcode, you are going to need at least one project, containing at least one target, and producing at least one product. Those are the basic structures you use for all your development.

Beyond that, there are no hard and fast rules for how you divide your work. For simple products or products that are closely tied together, you might use a single project with multiple targets. For large development tasks with many products, and especially with separate development teams, you’ll want to use multiple projects and targets, perhaps connected with cross-project dependencies.

The following sections provide additional information and tips on laying out your software.

In partitioning your software, many decisions depend on the scope of the design goal and the number of products it requires. For example, if you’re working alone on a simple application, you can create a project for the desired application type (such as a Cocoa or Carbon application) and get right to work. Here are some of the decisions you might face:

- If you decide to move some code to an internal library, you might add a target for the library.
- To take advantage of existing code in another project, you might choose to develop the existing code as a shared library and add a dependency so that the application project depends on the shared library project and makes use of its output.
- You might choose not to use a source code management (SCM) system, although even simple projects can sometimes benefit from such use.

Suppose, however, that you are working on a more complex software design, one that will be implemented by several individuals or development teams. Let’s say you are asked to create an application for an easy-to-use recording studio. You may already have components of this application, such as a shared library for presenting music tracks. As you refine the product specification, you identify other common tasks that might belong in a shared library, tool, or companion application. You determine that the main application should rely on Apple technologies to provide certain features, such as burning CDs or making the application scriptable.

Eventually, you identify a set of products to build, which gives you a good idea of the scope of the task. And that in turn can help you determine how to partition it into Xcode projects and targets.

You can help determine whether to put many or all your targets in one project by considering some of the trade-offs involved. Here are some of the advantages of combining multiple targets in one project:

- Indexing works across all targets. Indexing information is required to access classes in the class browser, view symbols in the Project Symbols smart group, and to take full advantage of code completion. It is also necessary to use Command–double-click to jump to a definition and to use symbolic counterparts.
- You can easily set up dependencies between targets in the project.
- Anyone using the project has access to all its files.
- If your computer has multiple CPUs or you have access to additional computers on your network, you can use parallel builds or distributed builds to improve the build time of a large project. See [Building in Parallel](../Xcode%20Project%20Management%20Guide/Building%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojtfvjvomjr) and [Reducing Build Times](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeBuildSystem/800-Reducing_Build_Times/bs_speed_up_build.html#//apple_ref/doc/uid/TP40002695) for details.

Here are some of the disadvantages of putting all your targets in one project:

- All of the code is visible to any individuals or teams using the project, even if they’re working on only one target or a small subset of the overall project.
- The project size may become unwieldy; this can cause Xcode to take a long time to perform operations such as indexing.
- All targets must use the same SCM system.
- All targets must build using the same SDK.
- You can’t use the Xcode debugger to debug two executables in one project at the same time.

There are also trade-offs in breaking up a software product into multiple projects and targets. Here are some of the advantages of using multiple projects:

- You can use the project as a unit for dividing work among different individuals or teams. The separate projects allow you to segregate the code (for example, to limit access to confidential information).
- Each project can be of a more manageable size, and Xcode can perform indexing, building, and other operations more quickly.
- If projects need to share outputs, they can build into a common directory, as described in Build Locations.
- You can use cross-project references to build other projects needed by the current project.
- Each project can use source code stored in a different SCM system. However, if individuals have physical access to other projects, it is still possible to look at SCM information from multiple projects that use the same SCM system.
- Each project can use different SDKs.
- Each project can define a separate list of build configurations.
- You can use the debugger to debug two or more executables at the same time, one in each project. This is useful when products communicate directly or otherwise interact.

Here are some of the disadvantages of having multiple projects and targets:

- You don’t have cross-project indexing, and thus you have access only to symbols that are specifically exposed by other projects. This means, for example, that you can’t automatically look up definitions in other projects unless you have physical access to them (not just to their end products).

  Similarly, you cannot take full advantage of other features that depend on indexing. That includes using code completion, using Command–double-click to jump to a definition, refactoring, and using symbolic counterparts.
- Management of many smaller projects is likely to incur additional overhead. For example, to set up a target that depends on other targets in multiple projects, you must first set up cross-project references.

  Similarly, use of multiple projects may require additional communication between teams.
- For an individual working on multiple projects, it may become unwieldy to switch between many open projects. This problem, however, may be alleviated by using the Organizer (see [Using the Organizer](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeProjectManagement/140-Using_the_Organizer/using_the_organizer.html#//apple_ref/doc/uid/TP40006917-CH279) for details).
- Individual projects are smaller and are less likely to be able to take advantage of distributed builds.

Decisions about how to partition projects and their targets affect the design of your entire software development effort. It is also important that your work in a project be organized and accessible to you. Particularly in larger projects, the number of files can be daunting. To help arrange files into manageable chunks, Xcode lets you group them.

A _group_ lets you collect related files together. A static group lets you group an arbitrary set of file, folder, and framework references in your project. A smart group, on the other hand, lets you group together files fitting a particular pattern or rule. This section shows you how to group files using static groups and smart groups.

In the Groups & Files list, static groups look like folders, but don’t have to correspond to folders on the file system. You can instead arrange files into groups that make sense to you while working on them in Xcode. For example, in a project containing multiple targets, your project could store all the nib files in one folder and all the implementation files in another folder on the file system. And in the Groups & Files list, you could group the files according to target; that is, the nib files and implementation files for target A would be in one group, the nib files and implementation files for target B would be in another group, and so on. A group doesn’t affect how a target is built.

You can create a static group in any of the following ways:

- Create an empty group. Choose Project > New Group and type the name for the group.
- Create a group from existing items. Select the items you want to group and choose Project > Group.
- Create a group based on an existing directory structure. Choose Project > Add to Project. Then select the folder, and select “Recursively create groups for added folders.”

You can add files to a group at any time by dragging the file icons to the group’s folder in the Groups & Files list. A line appears to indicate where you are moving the files. Xcode automatically expands groups as you drag items to them.

When you remove a group from your project, you can choose whether to remove the files in that group from the project or simply ungroup the files.

- To remove a group and the project’s references to the files in that group, select the group, and press Delete.
- To remove a group and keep the files it contains, select the group and choose Ungroup from its shortcut menu.

Smart groups are also represented by folder icons in the Groups & Files list; however, they are colored purple to distinguish them from static groups. As mentioned earlier, smart groups group files that adhere to a common pattern or rule. For example, you could define a smart group to collect all implementation files ending in `.m` or `.c`. When you make a change to your project that alters the set of files matching a smart group’s rule—for example, adding a `.c` file—the smart group automatically updates to reflect the change. You do not need to add files to a smart group yourself. In fact, Xcode does not allow you to drag files to a smart group.

To create a smart group, choose Project > New Smart Group. Then choose one of the following options:

- __Simple Filter Smart Group.__ Creates a smart group that collects files whose names contain a specified string.
- __Simple Regular Expression Smart Group.__ Creates a smart group that uses a regular expression to specify the pattern that filenames must follow.

Xcode adds a smart group of the selected type to your project and brings up the Smart Group Info window, which allows you to configure the group. Xcode provides templates for each type of smart group; it uses these templates to configure new smart groups with a default set of options. For example, the default Simple Filter Smart Group collects all files with `*.nib` in their name. The default Simple Regular Expression Smart Group collects all C, C++, Objective-C, Objective-C++, Java, and AppleScript implementation files in your project.

To configure a smart group, select the group in the Groups & Files list and open the Smart Group Info window, shown in Figure 2-1.

__Figure 2-1__  Smart Group Info window

!

Here is what the Smart Group Info window contains:

- __Name field.__ The name of the smart group. By default, this is set to the type of the smart group, for example, “Simple Filter Smart Group.”
- __Image.__ The icon used for the smart group in the project window. The default image for a smart group is the purple folder icon, but you can also use a custom image to represent your smart group. To change the icon, click the Choose button and navigate to the image file to use.
- __Start From menu.__ Specifies the directory from which the smart group starts its search for matching files; by default, this is the project folder. If the Recursively option is selected, the smart group also searches through subdirectories of that folder.
- __Using Pattern field.__ The actual pattern that files must match in order to be included in the smart group. As mentioned, this pattern can be either a simple string that the smart group filters on or a regular expression, depending on the setting of the options beneath the field. For examples of each of these, look at the smart group templates. The Simple Filter Smart Group template uses the pattern `*.nib`. Any files with `.nib` in their name are included in this smart group. The Simple Regular Expression Smart Group, on the other hand, uses the regular expression `\.(c|cpp|C|CPP|m|mm|java|sh|scpt)$` to collect all implementation files ending in any one of these suffixes, regardless of the case of the filename and extension. For more information on regular expressions, see the POSIX specification.
- __Save For menu.__ Determines the scope for which this smart group is defined. You can have the smart group appear in all your projects, or you can specify that the smart group be specific to the current project.

As you learned in [The Project Window](The%20Project%20Window.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnrvfvjvomi), you have two ways to view the contents of your project. You can view the groups and files in your project in outline view to see a hierarchical representation of your project layout. Or you can view the groups and files in your project as a simple list, in the detail view. The detail view presents a flat list of all the files contained in the group selected in the Groups & Files list. For example, if you select your project in the Groups & Files list, the detail view shows all the files in the project. If you select an individual file in the Groups & Files list, only that file is displayed in the detail view. To view the contents of a group in the detail view, select that group in the Groups & Files list. See [The Detail View](The%20Project%20Window.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnrvfvjvomq) for more information about the detail view.

In any project, there are locations that you find yourself accessing again and again: files that you edit frequently, headers that you browse, even smart groups that you use often. Xcode lets you save locations that you access frequently and provides ways for you to jump to these locations. This section describes how to take advantage of bookmarks and the favorites bar to provide quick access to project contents.

The _favorites bar_ in the project window lets you save frequently accessed items and return to them quickly. To show the favorites bar, choose View > Layout > Show Favorites Bar.

To add an item to the favorites bar, simply drag it to the favorites bar in the project window. You can save any of the same locations you can bookmark, including files, documentation, URLs, and so forth. In addition, you can add smart groups and static groups to the favorites bar. The Groups & Files list can get quite long as you reveal the contents of more and more groups, scrolling the items at the bottom of the list out of view. You can add groups—including any of the built-in smart groups—to the favorites bar to quickly jump to that group in the Groups & Files list.

To reorder items in the favorites bar, drag them to the desired location; dragging an item off of the favorites bar removes the item from the favorites bar. To rename an item in the favorites bar, Option-click the item and type the new name. This changes the name of the entry in the favorites bar; it does not affect the name of the actual item that the entry represents.

To open a saved location, click it in the favorites bar. If the item in the favorites bar is a container, such as a group or folder, it is a pop-up menu that you use to navigate through the contents. Each of the items in the favorites bar serves as a proxy for the actual item. Thus, Control-clicking the item brings up the item shortcut menu, which allows you to perform operations appropriate for the selected item.

Another way that Xcode lets you navigate your project and provide easy access to the information you need is with bookmarks. If you have files or locations in your project that you access often, you can bookmark them and return to those locations at any time simply by opening the bookmark.

To create a bookmark, select the location you want to bookmark and choose Edit > Add to Bookmarks.

Xcode automatically names some bookmarks. For items such as symbols, Xcode prompts you for the name of the bookmark; you can enter a name to help you remember which location the bookmark indicates, or you can use the name Xcode assigns. You can bookmark project files, documentation, URLs, and so forth.

You can see the bookmarks in your project in several ways:

- __Bookmarks smart group.__ Select the Bookmarks group in the Groups & Files list to see the bookmarks in the detail view. The detail view shows the name and file of all the bookmarks in your project. If the editor pane is open, selecting a bookmark opens that location in the editor. Otherwise, you can double-click the bookmark to open the bookmarked location in a separate editor window.
- __Bookmarks window.__ To open this window, double-click the Bookmarks smart group. You can see all bookmarks in your project in this window; double-click any of these bookmarks to open the location.
- __Bookmarks menu.__ This pop-up menu resides in the navigation bar of the text editor. It contains the bookmarks for the current file. Choose any bookmarked location from this menu to open it in the editor, as described in [A Tour of the Text Editor](The%20Text%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnzzfvjvomjw).

To help you keep track of your project contents, you can write comments and associate them with any of the items in your project. Xcode remembers these comments across sessions. In this way, you can document your project and its components, keep design notes, or track improvements you still wish to make. This is especially useful if you are working with large or complex projects that have many pieces, or if you are working with a team of developers and have multiple people modifying the project.

For example, imagine a large project containing targets that build a suite of applications, a framework used by each of those applications, a command-line tool for debugging, and a handful of plug-ins for the applications. With such a large number of targets it might be hard to keep track of exactly what each of the products created by those targets does. To make it easier to remember what each of them does, you could add a short description of the product that it creates to the target’s comments. This also aids others who may be working on the project with you; if they can read the comments, they can quickly get up to speed with the project and easily learn about changes made by other members of the development team.

To add comments to a project item:

1. Select that item in the Groups & Files list or in the detail view and open its Info window.
2. Click Comments to open the Comments pane.

   This pane contains a single text field into which you can type any information you wish. To add comments, click in the Comments field and type your entry. You can also link to additional resources from the Comments pane; hypertext links, email addresses and other URLs are actionable in this field.

You can add comments to any project item except smart groups, including projects, targets, files, and executables. You can view comments you have added to project items in the detail view and you can search the content of those comments using the search field. If the Comments column is not already visible, use the shortcut menu of the detail view header to display it.

The General pane of Xcode preferences lets you control general environment settings for the Xcode application, such as your project window configuration and windowing preferences. Figure 2-2 shows the General pane.

__Figure 2-2__  General preferences pane

!

Here is what the pane contains:

- __Layout.__ This menu lets you choose the project window configuration for all projects. See [Project Window Layouts](The%20Project%20Window.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnrvfvjvoni) for a description of the available layouts.
- __Editing.__ These options control Xcode’s windowing policy for editor windows. See [A Tour of the Text Editor](The%20Text%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnzzfvjvomjw) to learn more about the Xcode editor. The options are:

  - __Open counterparts in same editor.__ Specifies how Xcode displays files when jumping to a related header or source file, or to a related symbol definition or declaration. If this option is selected, Xcode opens file and symbol counterparts in the current editor window; otherwise, it opens a separate editor to display the counterpart. [Opening Header Files and Other Related Files](File%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnzxfvjvona) describes how to jump to a file’s or symbol’s counterpart.
  - __Automatically open/close attached editor.__ Specifies when Xcode shows or hides the editor pane attached to the project, Build Results, Project Find, or Debugger windows. If this option is selected, Xcode automatically shows the attached editor for a window when you select an editable item. See [Using Text Editor Panes](The%20Text%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnzzfvjvomjx) for more information on attached editors.
- __Workspace.__

  - __Reopen projects on Xcode launch.__ Specifies whether Xcode reopens the projects that were open when it last quit.
  - __Restore state of auxiliary windows.__ Specifies whether Xcode restores the state of the windows in projects upon opening them.

[Next](File%20Management.md)[Previous](The%20Project%20Window.md)

