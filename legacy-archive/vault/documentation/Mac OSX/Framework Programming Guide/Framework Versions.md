---
title: Framework Programming Guide
apple_id: 10000183i
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/VersionInformation.html
archived_at: '2026-07-15T08:15:39.208190Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Framework Programming Guide](Introduction%20to%20Framework%20Programming%20Guide.md)


[Next](Frameworks%20and%20Binding.md)[Previous](Anatomy%20of%20Framework%20Bundles.md)

# Framework Versions

You can create different versions of a framework based on the type of changes made to its dynamic shared library. There are two types of versions: major (or incompatible) and minor (or compatible) versions. Both have an impact on the programs linked to the framework, albeit in different ways.

A major version of a framework is also known as an incompatible version because it breaks compatibility with programs linked to a previous version of the framework’s dynamic shared library. Any such program running under the newer version of the framework is likely to experience runtime errors because of the changes made to the framework.

The following sections describe how you designate major version information in your framework and how the system uses that information to ensure applications can run.

Because all major versions of a framework are kept within the framework bundle, a program that is incompatible with the current version can still run against an older version if needed. The path of each major version encodes the version (see [Framework Bundle Structure](Anatomy%20of%20Framework%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tgljzhe4tema)). For example, the letter “A” in the path below indicates the major version of a hypothetical framework:

```
/System/Library/Frameworks/Boffo.framework/Versions/A/Boffo
```

When a program is built, the linker records this path in the program executable file. The dynamic link editor uses the path at runtime to find the compatible version of the framework’s library. Thus the major versioning scheme enables backward compatibility of a framework by including all major versions and recording the major version for each executable to run against.

You should make a new major version of a framework or dynamic shared library whenever you make changes that might break programs linked to it. The following changes might cause programs to break:

- Removing public interfaces, such as a class, function, method, or structure
- Renaming any public interfaces
- Changing the data layout of a structure
- Adding, changing, or reordering the instance variables of a class
- Adding virtual methods to a C++ class
- Reordering the virtual methods of a C++ class
- Changing C++ compilers or compiler versions
- Changing the signature of a public function or method

Changes to the signature of a function include changing the order, type, or number of parameters. The signature can also change by the addition or removal of `const` labels from the function or its parameters.

When you change the major version of a framework, you typically make the new version the “current” version. Xcode automatically generates a network of symbolic links to point to the current major version of a framework. See [Framework Bundle Structure](Anatomy%20of%20Framework%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tgljzhe4tema) for details.

Creating a major version of a framework is something that you should avoid whenever possible. Each new major version of a framework requires more storage space than a comparable minor version change. Adding new major versions is unnecessary in many cases.

Before you find yourself needing to create a new major version of your framework, consider the implementation of your framework carefully. The following list shows ways to incorporate features without requiring a new major version:

- Pad classes and structures with reserved fields. Whenever you add an instance variable to a public class, you must change the major version number because subclasses depend on the size of the superclass. However, you can pad a class and a structure by defining unused (“reserved”) instance variables and fields. Then, if you need to add instance variables to the class, you can instead define a whole new class containing the storage you need and have your reserved instance variable point to it.

  Keep in mind that padding the instance variables of frequently instantiated classes or the fields of frequently allocated structures has a cost in memory.
- Don’t publish class, function, or method names unless you want your clients to use them. You can freely change private interfaces because you can be sure no programs are using them. Declare any interfaces that may change in a private header.
- Don’t delete interfaces. If a method or function no longer has any useful work to perform, leave it in for compatibility purposes. Make sure it returns some reasonable value. Even if you add additional arguments to a method or function, leave the old form around if at all possible.
- 

  Remember that if you add interfaces rather than change or delete them, you don't have to change the major version number because the old interfaces still exist. The exception to this rule is instance variables.

While many of the preceding changes do not require the creation of a major version of your framework, most require changing the minor version information. See [Versioning Guidelines](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tkljzg4zdomq) for more information.

When you create a major version of a framework, Xcode takes care of most of the implementation details for you. All you need to do is specify the major-version designator. A popular convention for this designator is the letters of the alphabet, with each new version designator “incremented” from the previous one. However, you can use whatever convention is suitable for your needs, for example “2.0” or “Two”.

To set the major version information for a framework in Xcode, do the following:

1. Open your project in Xcode 2.4.
2. In the Groups & Files pane, select the target for your framework and open an inspector window.
3. Select the Build tab of the inspector window.
4. In the Packaging settings, set the value of the “Framework Version” setting to the designator for the new major version of your framework, for example, `B`..

You can also make major versions of standalone dynamic shared libraries (that is, libraries not contained within a framework bundle). The major version for a standalone library is encoded in the filename itself, as shown in the following example:

```
libMyLib.B.dylib
```

To make it easier to change the major version, you can create a symbolic link with the name `libMyLib.dylib` to point to the new major version of your library. Programs that use the library can refer to the symbolic link. When you need to change the major version, you can then update the link to point to a new library.

Within a major version of a framework, you can also designate the current minor version. Minor versions are also referred to as “compatible versions” because they retain compatibility with the applications linked to the framework. Minor versions don’t change the existing public interfaces of the framework. Instead, they add new interfaces or modify the implementation of the framework in ways that provide new behavior without changing the old behavior.

Within any major version of the framework, only one minor version at a time exists. Subsequent minor versions simply overwrite the previous one. This differs from the major version scheme, in which multiple major versions coexist in the framework bundle.

The following sections describe how you designate minor version information in your framework and how the system uses that information to ensure applications can run.

Frameworks employ two separate numbers to track minor version information. The _current version_ number tracks individual builds of your framework and is mostly for internal use by your team. You can use this number to track a group of changes to your framework and you can increment it as often as seems appropriate. A typical example would be to increment this number each time you build and distribute your framework to your internal development and testing teams.

The _compatibility version_ number of your framework is more important because it marks changes to your framework’s public interfaces. When you make certain kinds of changes to public interfaces, you should set the compatibility version to match the current version of your framework. Thus, the compatibility version typically lags behind the current version. Only when your framework’s public interfaces change do the two numbers match up.

Remember that not all changes to your framework’s public interfaces can be matched by incrementing the compatibility version. Some changes may require that you release a new major version of your framework. See [Versioning Guidelines](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tkljzg4zdomq) for a summary of the changes you can make for each version.

You should update the version information of your framework when you make any of the following changes:

- Add a class
- Add methods to an Objective-C class
- Add non-virtual methods to a C++ class
- Add public structures
- Add public functions
- Fix bugs that do not change your public interfaces
- Make enhancements that do not change your public interfaces

Any time you change the public interfaces of your framework, you must update its compatibility version number. If your changes are restricted to bug fixes or enhancements that do not affect the framework’s public interfaces, you do not need to update the compatibility version number.

When a program is linked with a framework during development, the linker records the compatibility version of the development framework in the program’s executable file. At runtime, the dynamic link editor compares that version against the compatibility version of the framework installed on the user’s system. If the value recorded in the program file is greater than the value in the user’s framework, the user’s framework is too old and cannot be used.

Cases where a framework is too old are uncommon, but not impossible. For example, it can happen when the user is running a version of OS X older than the version required by the software. When such an incompatibility occurs, the dynamic link editor stops launching the application and reports an error to the console.

To run an application on earlier versions of a framework, you must link the application against the earliest version of the framework it supports. Xcode provides support for linking against earlier versions of the OS X frameworks. This feature lets you link against specific versions of OS X version 10.1 and later. For more information, see _[SDK Compatibility Guide](../../Developer%20Tools/SDK%20Compatibility%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2i)_.

If you are developing a framework, you need to increment your current version and compatibility version numbers at appropriate times. You set both of these numbers from within Xcode. The linking options for Xcode framework projects include options to specify the current and compatibility version of your framework. To set these numbers for a specific target, do the following:

1. Open your project in Xcode 2.4.
2. In the Groups & Files pane, select the target for your framework and open an inspector window.
3. Select the Build tab of the inspector window.
4. In the Linking settings, set the value of the “Current Library Version” setting to the current version of your framework.
5. Update the “Compatibility version” option as needed to reflect significant changes to your framework. (See [Compatibility Version Numbers at Runtime](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tkljrgaydcmzq) for more information.)

Whenever you change the code in your framework, you should also modify the configuration information in your framework project to reflect the changes. For simple changes, such as bug fixes and most new interfaces, you may need to increment only the minor version numbers associated with your framework. For more extensive changes, you must create a new major version of your framework.

Table 1 lists the types of changes you can make to your framework code and the corresponding configuration changes you must make to your project file. Most changes that require a major or minor version update occur because the changes affect public interfaces.

__Table 1__  Making changes to a framework

| Version type | Changes Allowed | What to do |
| Major version | Remove interfaces (classes, functions, methods, and so on). Rename interfaces. Change the layout of a class or structure. Add, change, or reorder instance variables of a class. Add or reorder virtual methods in a C++ class. Change the signature of a function or method. Changing C++ compilers or compiler versions. | You must change the major version designator for your project. Build your framework and incorporate the new version into your existing framework directory structure. |
| Minor version (public interface changes) | Add a C++ or Objective-C class. Add methods to an Objective-C class. Add non-virtual methods to a C++ class. Add structures. Add functions. | Increment your current version number and set your compatibility version number to match. Build your framework. |
| Minor version (no public interface changes) | Fix bugs that do not affect programmatic interfaces. Make enhancements that do not affect your programmatic interfaces. Change interfaces used only internally to the framework. | Increment your current version number. Do not change the compatibility version number. |

If you don’t change the framework’s major version number when you need to, programs linked to it may fail in unpredictable ways. Conversely, if you change the major version number when you didn’t need to, you clutter up the system with unnecessary framework versions.

Because major versions can be very disruptive to development, it is best to avoid them if possible. [Avoiding Major Version Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tkljrgaytimzx) describes techniques you can use to make major changes without releasing a new major version of your framework.

[Next](Frameworks%20and%20Binding.md)[Previous](Anatomy%20of%20Framework%20Bundles.md)

