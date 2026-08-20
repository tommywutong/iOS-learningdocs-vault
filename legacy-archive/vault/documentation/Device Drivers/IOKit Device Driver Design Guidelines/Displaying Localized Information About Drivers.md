---
title: IOKit Device Driver Design Guidelines
apple_id: TP30000694
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-08-14'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/InternationalizingDrivers/InternationalizingDrivers.html
archived_at: '2026-07-15T07:31:49.411321Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [IOKit Device Driver Design Guidelines](Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md)


[Next](Debugging%20Drivers.md)[Previous](Kernel-User%20Notification.md)

# Displaying Localized Information About Drivers

A frequently repeated fact in Darwin documentation is that a kernel extension is a bundle. What does this mean, and what are the implications?

A bundle is a directory with a strictly defined internal structure that (usually) contains executable code and the resources that support that code. A bundle on OS X is the primary form of packaging for executables in the file system. Applications and frameworks are bundles, as are all other loadable bundles such as kernel extensions. Although some executables are not bundles—most notably command-line tools, some libraries, and CFM-PEF applications—they are definitely in the minority. The Finder presents most bundles to users opaquely, as a file.

A bundle can be programmatically represented by a NSBundle object (for Cocoa code) or by a CFBundle opaque type (for all other application environments). The APIs of NSBundle and CFBundle permit your executable to access and manipulate the resources in the represented bundle.

Among the benefits that the bundle form of packaging brings to executables is internationalization. Internationalization is the mechanism by which executables on OS X store localized resources in bundles and access them in order to present them in a graphical user interface. Localized resources are those that have been translated and adapted to particular languages and locales; text, images, and sounds are among the resources that are frequently localized. OS X attempts to present those localizations that match a language preference of the user.

Device drivers and other kernel extensions occasionally need to have localized information displayed to users during tasks that require user input, such as configuration and installation. But you should remember that kernel extensions are a different breed of bundle. The executable code in these bundles is loaded into the kernel and kernel code, by definition, does not play a direct role in user interfaces. If a kernel extension contains localized resources for display, it must have a user-space agent to do the displaying for it. In many cases, the kernel extension will have a helper application or preference pane to present the localized user interface.

One might ask: why not put all localized resources in the helper application instead of the kernel extension? Doing so would seem to make it easier to locate the resources. That may be true when there is only one kernel extension per helper application. But typically a helper application is responsible for a family of kernel extensions, both current and anticipated products. If the application is to contain all localized resources, it must have prior knowledge of every kernel extension it might display information about. Because this is impractical, it makes more sense for a kernel extension to encapsulate its own localizations.

This section provides an overview of internationalizing kernel extensions and describes the special APIs and procedures that code in user space must use to access localized resources stored in these bundles.

Internationalizing your kernel extension is a fairly painless process. You need to set up your project files in a certain way and you may need to modify code. Of course, you must have localized resources to put into your project. This means someone must complete all necessary translations and adaptations of the following resources:

- Images (for example, the equivalent of a U.S. stop sign in other cultures)
- Sounds (for example, a recorded voice speaking a phrase)
- Long text files (for example, an HTML help file)
- Nib files (user-interface archives created by the Interface Builder application)
- Strings that appear in the user interface (for example, titles of buttons and text fields)

This section summarizes the steps you must follow to internationalize your kernel extension. For all single-file resources such as images, sounds, nib files, and help files, internationalization is a simple matter of putting the resource files in certain subdirectories of the kernel extension. In your user-space code, you may then have to use CFBundle (or NSBundle) APIs to obtain a path to a resource file in the current localization prior to loading that resource. The procedure for internationalizing user-interface strings is a bit more involved; this procedure is summarized in [Internationalizing Strings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombqfvbeeq2hizdemry).

If you looked at the internal structure of a simple internationalized kernel extension in the file system, you might see something like this:

```
MyDriver.kext/
    Contents/
        MacOS/              // contains kernel binary
        Resources/
            Logo.tiff           // non-localized resource
            en.lproj/
                Stop.tiff       // English-localized resource
            fr.lproj/
                Stop.tiff       // French-localized resource
```

As you can see, a bundle’s resources go (logically enough) in the `Resources` subdirectory of the bundle. Resources at the top level of `Resources` are non-localized and thus are displayed in the user interface regardless of the logged-in user’s language preference. Localized resources (the two image files named `Stop.tiff` in the above examples) are put in subdirectories of `Resources`; each of these directories has an extension of `.lproj` and a name that is either the English name of a major language or an ISO 639 abbreviation for a language (such as “en”). The name can also have a suffix that is an ISO 3166 abbreviation for locale (for example, “en_US” for U.S. English). When an application needs to display a localized resource, OS X gets the logged-in user’s language preferences—this is a sorted list of preferred languages set through the International pane of System Preferences—and goes down the list until it finds the first language matching one of the `.lproj` localization directories in the bundle. This is how the internationalization mechanism basically works.

You can create the internal localization structure of your bundle by hand, but it is more convenient to let the Project Builder application do much of the work for you. The procedure is fairly straightforward. In Project Builder:

1. Create a group for localized and non-localized resources.

   Click the Files tab. Choose New Group from the Project menu and name the new group. (Go ahead, name it “Resources”.)
2. Add a resource to the group.

   Choose Add Files from the Project menu. In the browser, locate and select a file containing a sound, image, text, or other resource. When this file appears in the Files pane of Project Builder, drag it into the Resources group, if necessary.
3. Mark the localization attribute of the file.

   1. Select the file and choose Show Info from the Project menu.
   2. From the Localization & Platforms pop-up list, select Add Localized Variant.
   3. In the sheet that next appears, either select a language name from the combo box or, if the localization is for some other language, type the ISO 639 abbreviation in the text field. Click OK.
   4. If you later decide the resource should not be localized, select it and choose Make Global from the Localization & Platforms pop-up list.

Complete the above procedure for every resource, localized and non-localized, that you want included in your project. When you build the project, Project Builder will create an `.lproj` directory for each localization and put all resources designated for that localization in the directory. The name and extension of the resource file must be exactly the same for each localization.

If an application gets the localized strings for its user interface from a nib file, you need only store localized nib files in each `.lproj` directory of the kernel extension to internationalize them. However, if an application is to display localized strings for a kernel extension _programmatically_, you need to have a strings file in each `.lproj` directory of the kernel extension. A strings file is so-called because its extension is `.strings`; the conventional name before the extension is `Localizable`, but this is not a requirement.

The format of a strings file is a simple key-value pairing for each string entry; the entry is terminated by a semicolon and a carriage return (that is, one entry per line). The key is a string in the development language; the value is the localized string. Between the key and the value is an equal sign. For example:

```
/* a comment */
/* "key" = "value"; */
"Yes" = "Oui";
"The same text in English" = "Le meme texte en francais";
```

Once you’ve created a localized strings file, put it in the appropriate `.lproj` directory (as described in [Creating and Populating the Localization Directories](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombqfvbeeq2eifdeisa)). The next step is to modify the code of the application to display the localized string. At each point where a localized string is needed, use the macro `CFCopyLocalizedString` (and variants) if you are using CFBundle APIs; if you are using Cocoa’s NSBundle, use the `NSLocalizedString` macro (and variants) instead. In the simplest version of the macro, you specify two parameters: the key and a comment. For example:

```
CFStringRef locstr = CFCopyLocalizedString(CFSTR("Yes"), CFSTR("");
```

If the logged-in user’s language preference is French, the variable `locstr` holds the value of “Oui”. The comment is there for a particular reason. Instead of creating a strings file from scratch, you can put all required `CFCopyLocalizedString` (or `NSLocalizedString`) calls in your application code first. In the comment parameter, give any instructions to the translator for the string. Then run the `genstrings` command-line utility on your source-code file to generate a strings file. You can then give a copy of the generated file to the translator for each localization.

If you’re responsible for the user-space code that must display your kernel extension’s localized information, you’ll need to get the path to your KEXT. CFBundle and NSBundle require a path to a bundle to create a bundle object, which you need to programmatically access the resources of the bundle.

The solution to this is to pass the `CFBundleIdentifier` of your KEXT to a special KEXT Manager function to obtain the bundle path. The KEXT Manager defines the following function for this purpose (in `IOKit.framework/Headers/kext/KextManager.h`):

```
CFURLRef KextManagerCreateURLForBundleIdentifier(
    CFAllocatorRef allocator,
    CFStringRef    bundleIdentifier);
```

The `KextManagerCreateURLForBundleIdentifier` function returns a CFURLRef object representing the path to any KEXT currently installed in `/System/Library/Extensions` identified by the passed-in `CFBundleIdentifier`. For the CFAllocatorRef parameter, you can obtain the current default allocator with a call to `CFAllocatorGetDefault`.

Once you have the path to the kernel extension (as a CFURLRef object), you can create a bundle object (CFBundleRef) from it using the following CFBundle function:

```
CF_EXPORT
CFBundleRef CFBundleCreate(CFAllocatorRef allocator, CFURLRef bundleURL);
```

You can make the bundle object the subsequent target of calls for returning localized resources, such as strings, images, and icons.

[Next](Debugging%20Drivers.md)[Previous](Kernel-User%20Notification.md)

