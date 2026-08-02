---
title: Framework Programming Guide
apple_id: 10000183i
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/FrameworkAnatomy.html
archived_at: '2026-07-15T08:15:37.260791Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Framework Programming Guide](Introduction%20to%20Framework%20Programming%20Guide.md)


[Next](Framework%20Versions.md)[Previous](What%20are%20Frameworks.md)

# Anatomy of Framework Bundles

In OS X, shared resources are packaged using standard frameworks and umbrella frameworks. Both types of framework feature the same basic structure and can contain resources such as a shared library, nib files, image files, strings files, information property lists, documentation, header files, and so on. Umbrella frameworks add minor refinements to the standard framework structure, such as the ability to encompass other frameworks.

Frameworks are packaged in a bundle structure. The framework bundle directory ends with the `.framework` extension, and unlike most other bundle types, a framework bundle is presented to the user as a directory and not as a file. This openness makes it easy for developers to browse any header files and documentation included with the framework.

Framework bundles use a bundle structure different from the bundle structure used by applications. The structure for frameworks is based on an earlier bundle format, and allows for multiple versions of the framework code and header files to be stored inside the bundle. This type of bundle is known as a _versioned bundle_. Supporting multiple versions of a framework allows older applications to continue running even as the framework binary continues to evolve.

The system identifies a framework by the `.framework` extension on its directory name and by the `Resources` directory at the top level of the framework bundle. Inside the `Resources` directory is the `Info.plist` file that contains the bundle’s identifying information. The actual `Resources` directory does not have to reside physically at the top-level of the bundle. In fact, the system frameworks that come with OS X have a symbolic link to the framework’s `Resources` directory in this location. The link points to the most current version of the `Resources` directory, buried somewhere inside the bundle.

The contents of the `Resources` directory are similar to those for application bundles. (See “Anatomy of a Modern Bundle” in _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_ for more information.) Localized resources are put in language-specific subdirectories that end with the `.lproj` extension. These subdirectories hold strings, images, sounds, and interface definitions localized to the language and region represented by the directory. Nonlocalized resources reside at the top level of the `Resources` directory.

When you build a new framework project in Xcode, the build environment creates a versioned bundle structure for you automatically. Listing 1 shows the basic directory structure of the resulting bundle.

__Listing 1__  A simple framework bundle

```swift
MyFramework.framework/
    MyFramework  -> Versions/Current/MyFramework
    Resources    -> Versions/Current/Resources
    Versions/
        A/
            MyFramework
            Resources/
                English.lproj/
                    InfoPlist.strings
                Info.plist
        Current  -> A
```

In this listing, the `Versions` directory is the only real directory at the top level of the bundle. Both `MyFramework` and `Resources` are symbolic links to items in `Versions/A`. The reason for the symbolic links is that directory `Versions/A` contains the actual contents of the framework. It contains both the executable and the resources used by the framework.

Listing 1 shows that the top-level symbolic links don’t point directly to items inside the `Versions/A` directory. Instead, they point to items in the `Versions/Current` directory, which itself is a symbolic link to `Versions/A`. This additional level of indirection simplifies the process of changing the top-level links of frameworks with many resource types to point to a specific major version of the framework, because only one link, `Versions/Current`, needs to be updated.

Each real directory in `Versions` contains a specific _major version_ of the framework. Earlier major versions of the framework are needed by clients created when those versions were current at the time. New major versions of a framework are required only when changes in the framework’s dynamic shared library would prevent a program linked to it from running. Programs built using the earlier major version of the library must continue to use it, but programs in development should link against the current version of the library.

Listing 2 shows the MyFramework framework after a adding major revision to it.

__Listing 2__  A framework with multiple versions

```swift
MyFramework.framework/
    MyFramework  -> Versions/Current/MyFramework
    Resources    -> Versions/Current/Resources
    Versions/
        A/
            MyFramework
            Resources/
                English.lproj/
                    InfoPlist.strings
                Info.plist
        B/
            MyFramework
            Resources/
                English.lproj/
                    InfoPlist.strings
                Info.plist
        Current  -> B
```

Through the `Versions/Current` symbolic link, `MyFramework.framework/MyFramework` points to the dynamic shared library of the now current version of the framework, `Versions/B/MyFramework`. Because of the use of symbolic links, during a program’s link process, the linker finds the latest version of the framework’s library. This arrangement ensures that new programs are linked against the latest major version of the framework and that programs built with the earlier major version of the framework continue to work unchanged. For more on major and minor framework versions, and on versioning in general, see [Framework Versions](Framework%20Versions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tklkcineukq2birca). For more information on using dynamic libraries, see _[Dynamic Library Programming Topics](../../Developer%20Tools/Dynamic%20Library%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnrz)_.

Frameworks typically include more directories than just the `Resources` directory. For example, `Headers`, `Documentation`, and `Libraries`. Thus, adding a `Headers` directory to the example in [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tgljrgaydaobufvbecssgi5eumsq) would result in a framework like the one shown in Listing 3.

__Listing 3__  A framework with additional resource types

```swift
MyFramework.framework/
    Headers      -> Versions/Current/Headers
    MyFramework  -> Versions/Current/MyFramework
    Resources    -> Versions/Current/Resources
    Versions/
        A/
            Headers/
                MyHeader.h
            MyFramework
            Resources/
                English.lproj/
                    Documentation
                    InfoPlist.strings
                Info.plist
        B/
            Headers/
                MyHeader.h
            MyFramework
            Resources/
                English.lproj/
                    Documentation
                    InfoPlist.strings
                Info.plist
        Current  -> B
```

To create additional directories in your framework, you must add build phases to the appropriate target in Xcode. The Copy Files build phase lets you create directories and copy selected files into those directories. Table 1 lists some of the typical directories you might add to your framework.

__Table 1__  Standard directories for frameworks

| Directory | Description |
| `Headers` | Contains any public headers you want to make available to external developers. |
| `Documentation` | Contains HTML or PDF files describing the framework interfaces. Typically, documentation directories do not reside at the top level of your framework. Instead, they reside inside your language-specific resource directories. |
| `Libraries` | Contains any secondary dynamic libraries your framework requires. |

Frameworks require the same sort of configuration as any other type of bundle. In the information property list for your framework, you should include the keys listed in Table 2. Most of these keys are included automatically when you set up the framework properties in Xcode, but you must add some manually.

__Table 2__  Framework configuration keys

| Key | Description |
| `CFBundleName` | The framework display name |
| `CFBundleIdentifier` | The framework identifier (as a Java-style package name) |
| `CFBundleVersion` | The framework version |
| `CFBundleExecutable` | The framework shared library |
| `CFBundleSignature` | The framework signature |
| `CFBundlePackageType` | The framework package type (which is always `'FMWK'`) |
| `NSHumanReadableCopyright` | Copyright information for the framework |
| `CFBundleGetInfoString` | A descriptive string for the Finder |

Because frameworks are never associated with documents directly, you should never specify any document types. You may include display name information if you wish.

For more information on configuration and information property lists in general, see _[Runtime Configuration Guidelines](../Runtime%20Configuration%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3ta2i)_. For specific details about each of the keys in Table 2, read _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

The structure of an umbrella framework is similar to that of a standard framework, and applications do not distinguish between umbrella frameworks and standard frameworks when linking to them. However, two factors distinguish umbrella frameworks from other frameworks. The first is the manner in which they include header files. The second is the fact that they encapsulate subframeworks.

The purpose of an umbrella framework is to provide all the necessary interfaces for programming in a particular application environment. Umbrella frameworks hide the complex cross-dependencies among the many different pieces of system software. Thus you do not need to know what set of frameworks and libraries you must import to accomplish a particular task. Umbrella frameworks also make faster builds possible through the use of precompiled headers.

An umbrella framework simply includes and links with constituent subframeworks and other public frameworks. An umbrella framework encompasses all the technologies and APIs that define an application environment or a layer of system software. It also provides a layer of abstraction between what outside developers link their programs with and what Apple engineering provides as implementation.

A subframework is structurally a public framework that packages a specific Apple technology, such as Apple events, Quartz, or Open Transport. However, a subframework is public with restrictions. Although the APIs of subframeworks are public, Apple has put mechanisms in place to prevent developers from linking directly with subframeworks (see [Restrictions on Subframework Linking](Including%20Frameworks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2toljzg4ytioi)). A subframework always resides in an umbrella framework installed in `/System/Library/Frameworks`, and within this umbrella framework, its header files are exposed. 

Some umbrella frameworks include other umbrella frameworks; this is particularly the case with the umbrella frameworks for the Carbon and Cocoa application environments. For example, both Carbon and Cocoa (directly or indirectly) import and link with the Core Services umbrella framework (`CoreServices.framework`). This umbrella framework, in turn, imports and links with subframeworks such as Core Foundation.

The exact composition of the subframeworks within an umbrella framework is an internal implementation detail subject to change. By providing a level of indirection, umbrella frameworks insulate developers from these changes. Apple might restructure the subframeworks within an umbrella framework and might add, rename, or remove the header files within subframeworks. If you include the master header file for the subframework, these changes should not affect your programs.

Physically, umbrella frameworks have a similar structure to standard frameworks. One significant difference is the addition of a `Frameworks` directory to contain the subframeworks that make up the umbrella framework.

[Listing 4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tgljrgaytinjtfvbuqrcfinbegqq) shows a partial listing of the Core Services framework. (The contents of the subframeworks are not included since they are not referenced anyway.) As with standard frameworks, the top-level items are symbolic links to items deeper within the framework directory structure. In this case, the linked libraries and directories are located in folder `A` of the framework.

__Listing 4__  Structure of the Core Services umbrella framework

```swift
CoreServices.framework/
    CoreServices           -> Versions/Current/CoreServices
    CoreServices_debug     -> Versions/Current/CoreServices_debug
    CoreServices_profile   -> Versions/Current/CoreServices_profile
    Frameworks             -> Versions/Current/Frameworks
    Headers                -> Versions/Current/Headers
    Resources              -> Versions/Current/Resources
    Versions/
        A/
            CoreServices
            CoreServices_debug
            CoreServices_profile
            Frameworks/
                CarbonCore.framework
                CFNetwork.framework
                OSServices.framework
                SearchKit.framework
                WebServicesCore.framework
            Headers/
                Components.k.h
                CoreServices-gcc3.p
                CoreServices-gcc3.pp
                CoreServices.h
                CoreServices.p
                CoreServices.pp
                CoreServices.r
            Resources/
                Info-macos.plist
                version.plist
        Current             -> A
```

Unlike standard frameworks, the `Headers` directory of an umbrella framework contains a more limited set of header files. It does not contain a collection of the headers in its subframeworks. Instead, it contains only the master header file for the framework. When referring to an umbrella framework in your source files, you should include only the master header file. See [Including Frameworks](Including%20Frameworks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tolkciffeuqscjbfa) for more information.

[Next](Framework%20Versions.md)[Previous](What%20are%20Frameworks.md)

