---
title: Code Loading Programming Topics
apple_id: 10000052i
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/Concepts/AboutLoadableBundles.html
archived_at: '2026-07-15T07:16:25.808646Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Loading Programming Topics](Introduction%20to%20Dynamically%20Loading%20Code.md)


[Next](Loadable%20Bundles%20in%20Cocoa.md)[Previous](Introduction%20to%20Dynamically%20Loading%20Code.md)

# About Loadable Bundles

Loadable bundles are packages of executable code and related resources that can be loaded at runtime. This flexibility allows you to design highly modular, customizable, and extensible applications. After reading this document, you will understand how loadable bundles are structured and when you should use them.

OS X uses a directory structure called a _bundle_ throughout the system for packaging executable code and associated resources. The bundle directory, in essence, “bundles” a set of resources in a discrete package. Resources include such things as Interface Builder nib files, images, sounds, and localized character strings. Because code and associated resources are in one place in the file system, installation, uninstallation, and other forms of software management are easier.

Bundles come in several varieties: applications, frameworks, and loadable bundles. This document deals specifically with _loadable bundles_, which contain code that can be loaded at runtime, freeing you from a number of limitations of static compilation. Architecting your application around loadable bundles affords you a number of advantages:

- You can delay loading code until it is needed and in some cases unload code when it is no longer needed.
- You can divide your application into pieces that can be compiled independently, allowing you to more easily divide up development work and test different versions of different components with each other.
- You can make your application extensible by designing a plug-in architecture. This way, you or third-party developers can easily add new features without recompiling the whole application or even having access to its source code.

Unloading is limited to applications that do not use the Cocoa runtime environment. At the time of this writing, the Objective-C runtime does not support unloading Objective-C symbols, so Cocoa bundles, once loaded, cannot be unloaded.

OS X defines the extension `.bundle` to identify loadable bundles. You can also define your own extension (and associated icon) for a particular type of bundle.

Kernel extensions are a type of loadable bundle that the system bundle routines recognize and handle appropriately (although their internal structure is different from other loadable bundles). These bundles have an extension of `.kext`. The Kernel Manager, which claims kernel extensions as a document type, dynamically loads them into the kernel environment. This document does not deal with kernel extensions further. To learn more, see the [Darwin Documentation](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000422).

For more information about bundles, see _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_. For detailed information about how OS X loads and executes code, see _Mach-O Runtime Architecture_.

Fundamentally, loadable bundles let you load code and bind symbols at runtime. In practice, they can help you meet three related needs:

- Delayed (“lazy”) linking and loading
- Modularity of code components
- Application extensibility

Large, complex applications perform a variety of tasks. Usually, the user does not need to perform all of the available tasks in a given session of use. This means that chunks of application code, sometimes significant pieces, are loaded into memory but are never used.

You can avoid unnecessary loading of code by partitioning your application into loadable bundles consisting of logically related code. By also including accessor functions or methods for these pieces of code, you can seamlessly reference the objects without directly checking if the code has been loaded or not—these checks take place implicitly in the accessor methods.

Lazy loading can take a hierarchical form, with large application pieces at the top level and more specific features below. Specific features typically take the form of plug-ins, as described in [Application Extensibility](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3dqljzhe4dmna).

There are several ways to modularize your application into logically separate code components. The basic way to modularize your code is to split it into multiple source files—all nontrivial applications are built this way. The next level of complexity is a framework, which contains executable code, headers, and possibly other resources in a directory package. With a little extra work, you can also use loadable bundles as a unit of modularity.

Although not every situation calls for modularization via loadable bundles, you gain a number of benefits by putting in the extra work. When the codebase is split into multiple bundles, each bundle can be developed and tested independently of the others to an even greater extent than frameworks. Because the bundle contains dynamically loaded executable code, the other parts of the application can be agnostic of function addresses, object addresses, and even what class a referenced object belongs to, as long as it knows enough about the class to use it. Different versions of different code components can be tested without recompiling the application—you can combine different components just by dragging icons in the Finder.

Most uses of loadable bundles arise from the need for application extensibility. You can define a _plug-in architecture_ if you want your application to be extensible, either internally within your organization or by third-party developers. A plug-in architecture defines an interface through which a properly constructed loadable bundle, called a _plug-in_, can add functionality. Examples of plug-ins are screen saver modules, preference panes, Interface Builder palettes, Adobe Photoshop graphics filters, and iTunes music visualizers.

Using loadable bundles does not come “for free,” although both Cocoa and Core Foundation provide rich API support in this regard. If you are trying to decide whether or not to use loadable bundles, keep in mind the following costs:

- Loadable bundles, unlike application bundles and frameworks, must be explicitly loaded at runtime. If you need code reusability but not dynamic loading, frameworks often are a better choice.
- In Cocoa, loadable bundles cannot be used as a memory management scheme for large portions of code, because Cocoa bundles cannot be unloaded.
- Defining a plug-in architecture requires careful validation of plug-in modules.
- Allowing external plug-in code in your application comes with stability and security issues.

However, if your application needs delayed loading, more dynamic modularity than frameworks can provide, or extensibility, use loadable bundles.

A bundle directory contains a hierarchy of resources and executable code, each in its appropriate place. A typical bundle directory hierarchy looks like [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3dqljzhaytemrnijbusskcifcem).

__Listing 1__  The directory layout of a typical loadable bundle

```
- MyLoadableBundle
    Contents/
        Info.plist
        MacOS/
            MyLoadableBundle
        Resources/
            Lizard.jpg
            MyLoadableBundle.icns
            English.lproj/
                MyLoadableBundle.nib
                InfoPlist.strings
            Japanese.lproj/
                MyLoadableBundle.nib
                InfoPlist.strings
```

Every bundle directory contains one item, the `Contents` directory. `Contents` contains two files present in every bundle, `Info.plist` and `PkgInfo`, as well as the `MacOS` directory, which contains executable code, and the `Resources` directory, which contains all non-code resources. More complex bundles may contain additional directories such as `Frameworks`, `PlugIns`, `SharedFrameworks`, and `SharedSupport`—all the features supported by full-fledged application packages.

The `Info.plist` file, or _information property list_, is an XML property list containing key-value pairs of information about the bundle. System routines allow the bundle executable to read these attributes at runtime. You are free to store any application-defined data in the information property list as well. Xcode provides a user interface for editing information property lists and includes all required keys by default.

Information property list keys can be localized by adding corresponding entries to the `InfoPlist.strings` files contained in language directories (such as `Japanese.lproj`) in the `Resources` directory.

The most relevant information property list keys for loadable bundles are:

- `CFBundleExecutable`: the name of the executable, typically the same as the bundle directory without the extension
- `CFBundleIdentifier`: the globally unique identifier for the bundle, in reverse-DNS order, such as `com.apple.screensaver.Flurry`
- `CFBundleName`: the short display name of the bundle, used as a human-readable identifier (should be localized)
- `CFBundleDisplayName`: the display name of the bundle, used to represent the bundle in the Finder unless overridden by the user (should be localized)

For a full description of all the standard `Info.plist` keys, see Property List Key Reference.

The `MacOS` directory contains the Mach-O executable code for a loadable bundle. The name of the executable inside this directory is typically the same as the bundle directory without its extension and is the same as the value for the `CFBundleExecutable` key in the information property list. Certain types of bundles may lack executable code. Loadable bundles, applications, and most other types of bundles, however, need it by their nature.

The `Resources` directory contains all resources associated with a bundle, such as sounds, images, Interface Builder nib files, and localized strings. Localized resources are contained within _language_`.lproj` directories. You can create subdirectories in `Resources` to organize types of resources if you like.

For more detailed information about information property lists, see [Information Property Lists](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPRuntimeConfig/Articles/ConfigFiles.html#//apple_ref/doc/uid/20002091).

[Next](Loadable%20Bundles%20in%20Cocoa.md)[Previous](Introduction%20to%20Dynamically%20Loading%20Code.md)

