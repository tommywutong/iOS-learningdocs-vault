---
title: Framework Programming Guide
apple_id: 10000183i
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Tasks/CreatingFrameworks.html
archived_at: '2026-07-15T08:15:42.600733Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Framework Programming Guide](Introduction%20to%20Framework%20Programming%20Guide.md)


[Next](Initializing%20a%20Framework%20at%20Runtime.md)[Previous](Guidelines%20for%20Creating%20Frameworks.md)

# Creating a Framework

Once you decide that you need to create a framework for your code, you can do so easily with Xcode. As you add major versions to the framework, you also need to be able to maintain your projects. The following sections show you how perform both of these tasks.

From Xcode, choose File > New Project to create your project. Follow the prompts to select the type of framework you want and where you want to put your project directory.

The default templates that come with Xcode let you specify whether you want to create a Carbon or Cocoa framework. The type of framework you choose determines which default files are generated for you. If you do not want to include Carbon or Cocoa headers in your framework, you can remove any references to them after you create your project.

When you create a new framework, there are several configuration options you may want to modify. These options make it easier to distribute your framework to customers and guarantee its compatibility after future development cycles. Table 1 lists some of the options you should set for your framework.

__Table 1__  Framework configuration options

| Option | Description |
| Framework identifier | A Java-style package identifier that uniquely identifies the framework to the system. You should always set this option. To set this option in Xcode 2.4, open an inspector window for your framework target, select the Properties tab, and modify the Identifier field. |
| Framework version | The current major revision of the framework. See [Major Versions](Framework%20Versions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tkljzg42tani) for more information. In Xcode 2.4, set this value for your framework target using the Framework Version build setting. |
| Current version | The current revision of the framework. In Xcode 2.4, set this value for your framework target using the Current Library Version build setting. See [Minor Versions](Framework%20Versions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tkljrgaytkmzr) for more information. |
| Compatibility version | The most recent revision of the framework that includes changes to the public interfaces. In Xcode 2.4, set this value for your framework target using the Compatibility Version build setting. See [Minor Versions](Framework%20Versions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tkljrgaytkmzr) for more information. |
| Exported symbols | The list of framework symbols you want to export to other programs. In Xcode 2.4, specify a file containing your exported symbols for your framework target using the Exported Symbols File build settings. To specify a file containing the symbols to hide, use the Unexported Symbols File build setting instead. See [Exporting Your Framework Interface](Exporting%20Your%20Framework%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dalkcijbuuskdivbq) for more information. |
| Installation path | The directory name in which your framework should ultimately be installed. In Xcode 2.4, set this value for your framework target using the Installation Directory build setting. See [Installing Your Framework](Installing%20Your%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dclkcijbugrscjjaq) for a list of standard locations. |
| Preferred address | For frameworks being deployed in OS X v10.3.9 and earlier, specify the preferred memory address to use for prebinding operations. This value is not needed when deploying a framework in 10.4 and later. See [Frameworks and Prebinding](Frameworks%20and%20Binding.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tmljrga3dqoju) for information on how to set the preferred address of a framework. |

When you build a framework, Xcode places it in the `build` subdirectory of your project directory by default. Although you can tell Xcode to install your framework in its final deployment location, during development you may want to leave it where it is. If you do, you may need to tell test applications where to find your framework.

If your framework project contains additional targets for test applications, then Xcode builds those applications in the same folder as your framework. Test applications built alongside your framework find that framework automatically because of their proximity to it. However, if you build your test applications into a different build directory, those applications may be unable to find your framework unless you tell them where to find it.

The usual way for an application to find a framework is to look in the standard locations (see [Installing Your Framework](Installing%20Your%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dclkcijbugrscjjaq)). However, you may not want to reinstall your framework every time you make changes to it. In that case, you can tell your test applications exactly where to find the framework using the `DYLD_FRAMEWORK_PATH` environment variable. Adding this variable to your executable tells `dyld` where to look for additional frameworks if it doesn’t find what it needs in the standard locations. The following steps show you how to set this variable in Xcode.

1. Open your application project in Xcode.
2. In the Groups & Files pane, open the Executables group, select the executable to configure, open its Info window, and click Arguments.
3. Add an entry to the environment variables list.
4. Set the name of the environment variable to `DYLD_FRAMEWORK_PATH`.
5. Set the value of the variable to the full pathname of the directory containing your framework.

   To specify multiple framework directories, separate the pathnames with a colon. For example, you could have a value such as the following value on this line: `/Users/lynn/MyFrameworks:/Volumes/Keylime/MyOtherFrameworks`.

If you need to distribute a private framework with an application, the preferred solution is to embed the framework in your application bundle. Embedding a framework inextricably links the framework to the application and ensures that the application always has the correct version of the framework needed to operate. Embedding the framework also makes it clear to other developers that they should not ever link to that framework.

To embed a framework in an application, there are several steps you must take:

- You must configure the build phases of your application target to put the framework in the correct location.
- You must configure the framework target’s installation directory, which tells the framework where it will live.
- You must configure the application target so that it references the framework in its installation directory.

It is possible to build and embed a framework in an application using a single Xcode project or multiple projects. Using a single Xcode project is somewhat easier because it requires less configuration to get both the framework and application to build. For multi-project setups, however, once the two projects are configured to build properly, the configuration steps for embedding the framework are essentially the same as those for a single Xcode project.

Using a single Xcode project for both your application and framework target simplifies the required setup. Once you create your project, you simply add two targets to it: one for your application and one for your framework. (Because both targets reside in the same project, there are no problems finding source files from either target at build time.) After that, you simply configure your framework and application targets with the proper runtime information for embedding.

The configuration for your framework target involves telling it where it will be installed. The framework needs this information so that it can find the resources it needs. Because frameworks are typically installed in fixed locations, you normally specify the full path to the appropriate frameworks directory. When you embed a framework inside a bundle, however, the location of the framework is not fixed, so you have to use the `@executable_path` placeholder to let the framework know its location is relative to the current executable.

1. Open an inspector for your framework target and select the Build tab.
2. Set the value of the Installation Directory build setting to `@executable_path/../Frameworks`.

At build time, Xcode builds your framework and puts the results in the build directory. Before the application can use the framework, however, you must configure the application target as follows:

- You need to copy the framework into the application’s bundle.
- You need to link the application against the framework.
- You need to create a build dependency between the framework and application.

The following steps show you how to configure your application target.

1. In the Group & Files pane, open your application target to view its current build phases.
2. Drag your framework product (located in the Products folder) to the existing Link Binary With Libraries build phase of your application target. This causes the application to link against your framework.
3. Add a new Copy Files Build Phase to the application target. (This phase will be used to install the framework in the application bundle.)
4. Select the new build phase and open an inspector window.
5. In the General tab of the inspector window, set the destination for the build phase to “Frameworks”.
6. Drag your framework product to the new build phase.
7. Select the application target again and open the inspector window.
8. In the General tab of the inspector window, add your framework as a dependency for the application. Adding this dependency causes Xcode to build the framework target before building the application target.

The build dependency you establish in the application target causes the framework to be built before the application. This is important because it guarantees that a built version of your framework will be available to link against and to embed in the application. Because of this dependency, you can set the active target of your Xcode project to your application and leave it there. Building the application now builds the framework and copies it to the application bundle directory, creating the necessary linkage between the two.

If you already have separate Xcode projects for your framework and application, you can take advantage of Xcode’s cross-project references to embed the framework in your application. Cross-project references are a convenient way to create relationships between two separate Xcode projects. To set up a cross-project reference between your application and framework, you would do the following:

1. In your application project, choose Project > Add to Project and select your framework’s `.xcodeproj` file. Xcode adds the framework project and displays its products in the Groups & Files pane of your application project.
2. Modify the Build Products Path setting for both the application and framework targets so that they use the same build directory. You need to modify each target in their original Xcode project file.
3. In your application project, modify the Header Search Paths setting of the application target by adding the directories containing any framework header files.

Once you have configured your Xcode projects to build properly, you can proceed with the configuration steps needed to embed the framework in your application. The remaining configuration steps for the framework and application targets are identical to the ones described in [Using a Single Xcode Project For Both Targets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tqlktk4yq). Your framework’s installation directory must be configured to be relative to the executable path of the application. SImilarly, the application target must copy the framework to its bundle and set up the necessary linkage and dependencies. The only difference is that you must configure each target in its own Xcode project.

After the release of a framework, you should consider how to manage your Xcode project for future releases. When you update an existing framework, the type of changes you make determines the best way to proceed with your project files. For example, major changes may warrant the copying of your project files and the maintenance of separate projects, one for each major version. On the other hand, minor changes can be folded into your existing Xcode project.

If you are making minor changes to your framework, there is no need to create a new Xcode project for your framework. However, you should always update the “current version” and “compatibility version” values associated with your framework. These values make it possible for the dynamic linker to determine if linking a program to your framework is possible.

For more information on how to update the minor version information of your framework and on the types of changes that constitute a minor version update, see [Minor Versions](Framework%20Versions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tkljrgaytkmzr).

The process for updating the major version of a framework is more difficult than the process for minor versions. The recommended way to create a new major version is to make a duplicate version of your entire Xcode project folder and continue developing from there. The old project files should be archived and used to perform legacy builds. However, active development should continue with the new project.

Once you have a new project folder, you need to make several modifications to the Xcode project to identify the project as a major version. Select your framework target and open the Inspector window. In the Build pane, modify the following build options:

- Increment the value of the Framework Version build setting to the next sequential value.
- Increment the value of the Current Library Version build setting.
- Update the value of the Compatibility Version build setting to match the updated Current Library Version.
- Update any build settings whose path information includes the framework major version designator. For example, if you have a Copy Files build phase based on the product directory, you may need to update that path. Or make sure the paths are specified using the framework’s `Current` symbolic link.
- In the Properties pane of the framework target Info window, update the version number that gets stored in your framework’s information property list.

Once you make the changes to your code, you can build the framework target. What you get is a new framework bundle containing only the new major version.

During installation, if a version of your framework does not already exist on the target system, have the installer copy your framework bundle over as is. However, if an existing version of the framework is present, have the installer copy the contents of your new framework directory to the old directory. Your installer script must replace symbolic links in the old framework bundle with ones that point to the new version of the framework. However, copying over the new major version should leave any old versions intact. This permits existing applications to continue running while newer versions use the updated framework.

You may also want the installer to remove any header files or documentation for outdated versions of your framework. This step is optional and is left to your discretion. However, it is recommended to prevent developers from accidentally including an outdated set of header files, or viewing older documentation, during development.

For more information on major versions of frameworks, see [Major Versions](Framework%20Versions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tkljzg42tani).

[Next](Initializing%20a%20Framework%20at%20Runtime.md)[Previous](Guidelines%20for%20Creating%20Frameworks.md)

