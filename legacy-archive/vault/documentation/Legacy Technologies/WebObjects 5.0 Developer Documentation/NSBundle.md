---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSBundle.html
archived_at: '2026-07-15T08:13:55.785984Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSBundle

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

An NSBundle represents a location in the file system that groups code and resources that can be used in a program. NSBundles locate program resources and assist in localization. You build a bundle in Project Builder using a Java WebObjects Application or Java WebObjects Framework project.

An NSBundle is an object that corresponds to a directory where related resources-including executable code-are stored. The directory, in essence, "__bundles__" a set of resources used by an application into convenient chunks, and the NSBundle object makes those resources available to the application. NSBundle can find requested resources in the directory. The term bundle refers both to the object and to the directory it represents.

Bundles are useful in a variety of contexts. Since bundles combine executable code with the resources used by that code, they facilitate installation and localization. NSBundles are also used to locate specific resources and to determine which classes are loaded.

Each resource in a bundle usually resides in its own file. Bundled resources include such things as:

- Images-GIF or JPEG images displayed on web pages
- Localized character strings

## Types of Bundles

NSBundle supports two types of bundles: application bundles and framework bundles.

### Application Bundles

An application bundle is a bundle that contains the resources needed to launch the application. Its extension is "`.woa`". To build an application bundle with Project Builder, use the Java WebObjects Application project type.

Every application has a single application bundle called the "main bundle". You obtain an NSBundle object corresponding to the main bundle with the [mainBundle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpnvqws3scovxgi3df) static method. This is typically the running application itself.

### Framework Bundles

A framework bundle is a bundle associated with a framework: a directory containing shared classes along with the resources that go with those classes, such as images and localized strings. A framework directory has a "`.framework`" extension. To build a framework bundle with Project Builder, use the Java WebObjects Framework project type.

You can get an NSBundle object associated with a framework by invoking the static method [bundleForName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpmj2w4zdmmvdg64somfwwk) specifying, as the argument, the name of the framework sans the "`.framework`" extension. Alternatively you can invoke the [bundleForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpmj2w4zdmmvdg64sdnrqxg4y) method specifying a class that's defined in the framework. To get all the framework bundles available to your application, you can invoke the [frameworkBundles](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpmzzgc3lfo5xxe22covxgi3dfom) static method.

## Bundle Availability

When an application starts up, it loads all of the bundles represented by class path components. If the class path contains multiple framework bundles with the same name, only the first one is loaded; the rest are ignored.

If you are unsure which bundles are loaded at startup, you can enable NSBundle debugging by setting the `NSBundleDebugEnabled` user default to `true`. NSBundle subsequently logs the paths to the bundles as it loads them.

## Localized Resources

If an application is to be used in more than one part of the world, its resources may need to be customized, or "localized," for language, country, or cultural region. An application may need, for example, to have separate Japanese, English, French, German, and Spanish versions of the images that label submit buttons.

Resources specific to a particular language are grouped together in a resource directory. This directory has the name of the language (in English) followed by a "`.lproj`" extension (for "language project"). The application mentioned above, for example, would have `Japanese.lproj`, `English.lproj`, `French.lproj`, `German.lproj`, and `Spanish.lproj` directories. The application also has a `Nonlocalized.lproj` directory, which contains resources shared by all locales.

It is good programming practice to ensure that if a resource appears in one language directory it also appears in all the others. Thus, `Icon.gif` in `French.lproj` should be the French counterpart to the Spanish `Icon.gif` in `Spanish.lproj`, and so on. However this discipline is not completely necessary. If `German.lproj` does not contain an `Icon.gif` resource, the `Icon.gif` resource in `Nonlocalized.lproj` will be used instead.

The server's locale determines which set of localized resources will actually be used by the application. NSBundle objects invoke the __java.util.Locale.getDefault__ method to determine the locale and chooses the localized resources accordingly.

## How Resources Appear on the File System

A bundle's resources are stored in a directory named `Resources` within the bundle directory on the file system. Within the `Resources` directory are all of the language directories except `Nonlocalized.lproj`. The non-localized resources in the `Nonlocalized.lproj` directory are mapped into the top level of the `Resources` directory on the file system.

For example, suppose the NSBundle resources are organized as shown below:

> ```
> Listing
> 0-1 Resource organization example
> English.lproj
>     Edit.wo
>         Edit.html
>         Edit.wod
>         Edit.woo
> Nonlocalized.lproj
>     Edit.wo
>         Edit.html
>         Edit.wod
>         Edit.woo
>     Images
>         Icon.gif
>         Background.jpeg
>     Main.wo
>         Main.html
>         Main.wod
>         Main.woo
> ```

These resources appear on the file system as:

> ```
> Listing
> 0-2 How the resources appear on the file
> system
> Resources
>     Edit.wo
>         Edit.html
>         Edit.wod
>         Edit.woo
>     Images
>         Icon.gif
>         Background.jpeg
>     Main.wo
>         Main.html
>         Main.wod
>         Main.woo
>     English.lproj
>         Edit.wo
>             Edit.html
>             Edit.wod
>             Edit.woo
> ```

## Determining Available Resources

NSBundle provides two methods to determine the resources it contains: [resourcePathsForResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxeutfonxxk4tdmvzq) and [resourcePathsForLocalizedResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxetdpmnqwy2l2mvsfezltn52xey3fom). These methods return _resource paths_, or paths specified according to NSBundle's resource organization, not the resource organization as it appears on the file system. For example, the resource path to the `Background.jpeg` resource in [Listing 0-1](#apple-infeircci5dus) is `Nonlocalized.lproj/Images/Background.jpeg`.

### resourcePathsForResources

The __resourcePathsForResources__ method takes two arguments: a subdirectory and an extension. The method returns an NSArray containing resource path strings for the resources in the specified subdirectory that have the specified extension. If you specify `null` for the subdirectory, the method returns the resource paths for the resources starting from the top level. If you specify `null` for the extension, the method will not filter resources according to their extension. [Table 0-2](#apple-infeissbi5duc) shows examples of invoking __resourcePathsForResources__ with various parameters for the bundle depicted in [Listing 0-1](#apple-infeircci5dus).

__Table 0-2 Results from invoking resourcePathsForResources.__

| __extension__ | __subdirectory__ | __Result__ |
| `null` | `null` | { "English.lproj/Edit.wo/Edit.html", "English.lproj/Edit.wo/Edit.wod", "English.lproj/Edit.wo/Edit.woo", "English.lproj/Images/Icon.gif", "Nonlocalized.lproj/Edit.wo/Edit.html", "Nonlocalized.lproj/Edit.wo/Edit.wod", "Nonlocalized.lproj/Edit.wo/Edit.woo", Nonlocalized.lproj/Images/Icon.gif", "Nonlocalized.lproj/Images/Background.jpeg", "Nonlocalized.lproj/Main.wo/Main.html", "Nonlocalized.lproj/Main.wo/Main.wod", "Nonlocalized.lproj/Main.wo/Main.woo" } |
| `"gif"` | `null` | { "English.lproj/Images/Icon.gif", "Nonlocalized.lproj/Images/Icon.gif" } |
| null | `"English.lproj"` | `{ "English.lproj/Edit.wo/Edit.html", "English.lproj/Edit.wo/Edit.wod", "English.lproj/Edit.wo/Edit.woo", "English.lproj/Images/Icon.gif" }` |
| `"gif"` | `"English.lproj"` | `{ "English.lproj/Images/Icon.gif" }` |

### resourcePathsForLocalizedResources

The [resourcePathsForLocalizedResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxetdpmnqwy2l2mvsfezltn52xey3fom) method returns an NSArray of resource paths to resources that are appropriate for the current locale. If a resource appears in more than one language directory, this method chooses whether to include it in the array based on the following criteria:

- If the resource appears in the language directory for the current locale, the method includes its path in the results array.
- If the resource appears in Nonlocalized.lproj but not in the current locale's language directory, the method includes its path in the results array.
- If the resource doesn't appear in `Nonlocalized.lproj` or the current locale's language directory the method does not include its path in the results array.

The __resourcePathsForLocalizedResources__method also takes the _extension_ and _subdirectory_ arguments that allow you to filter the result array based on the extension or subdirectory. [Table 0-3](#apple-infeiq2jijbem) shows examples of invoking __resourcePathsForLocalizedResources__ with various parameters for the bundle depicted in [Listing 0-1](#apple-infeircci5dus).

__Table 0-3 Results of invoking resourcePathsForLocalizedResources__

| __extension__ | __subdirectory__ | __Result__ |
| `null` | `null` | { "English.lproj/Edit.wo/Edit.html", "English.lproj/Edit.wo/Edit.wod", "English.lproj/Edit.wo/Edit.woo", "Nonlocalized.lproj/Images/Icon.gif", "Nonlocalized.lproj/Images/Background.jpeg", "Nonlocalized.lproj/Main.wo/Main.html", "Nonlocalized.lproj/Main.wo/Main.wod", "Nonlocalized.lproj/Main.wo/Main.woo" } |
| `"html"` | `null` | { "English.lproj/Edit.wo/Edit.html", "Nonlocalized.lproj/Main.wo/Main.html" } |
| null | `"Edit.wo"` | `{ "English.lproj/Edit.wo/Edit.html", "English.lproj/Edit.wo/Edit.wod", "English.lproj/Edit.wo/Edit.woo" }` |
| `"html"` | `"Edit.wo"` | `{ "English.lproj/Edit.wo/Edit.html" }` |

### resourcePathsForDirectories

NSBundle also includes a method called [resourcePathsForDirectories](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxerdjojswg5dpojuwk4y) that returns the directories containing resources. It also takes the _extension_ and _subdirectory_ parameters. [Table 0-4](#apple-infeiskbjbcum) shows examples of invoking __resourcePathsForDirectories__ with various parameters for the bundle depicted in [Listing 0-1](#apple-infeircci5dus).

__Table 0-4 Results of invoking resourcePathsForDirectories__

| __extension__ | __subdirectory__ | __Result__ |
| `null` | `null` | { "English.lproj/Edit.wo", "English.lproj/Images", "Nonlocalized.lproj/Edit.wo", "Nonlocalized.lproj/Images", "Nonlocalized.lproj/Main.wo" } |
| `"wo"` | `null` | { "Nonlocalized.lproj/Main.wo", "Nonlocalized.lproj/Edit.wo", "English.lproj/Edit.wo" } |
| null | `"English.lproj"` | `{ "English.lproj/Edit.wo", "English.lproj/Images" }` |
| `"wo"` | `"English.lproj"` | `{ "English.lproj/Edit.wo" }` |

## Accessing NSBundle Resources

NSBundle provides two methods to access resources: [bytesForResourcePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxwe6lumvzum33skjsxg33vojrwkudborua) and [inputStreamForResourcePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxws3tqov2fg5dsmvqw2rtpojjgk43povzggzkqmf2gq). Both methods require a single argument: a full resource path as returned by the [resourcePathsForResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxeutfonxxk4tdmvzq) and [resourcePathsForLocalizedResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxetdpmnqwy2l2mvsfezltn52xey3fom) methods. The __bytesForResourcePath__ method returns a byte array containing data for the resource specified by the path. The __inputStreamForResourcePath__ returns an java.io.InputStream for the resource specified by the path.

Sometimes you want to access a localized resource without specifying the full resource path. For example, if you might want to get the `Icon.gif` resource appropriate for the current locale. To do this, you invoke [resourcePathForLocalizedResourceNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2cgn5zey33dmfwgs6tfmrjgk43povzggzkomfwwkza) to determine the full resource path for the localized resource and, in turn, invoke [bytesForResourcePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxwe6lumvzum33skjsxg33vojrwkudborua) or [inputStreamForResourcePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxws3tqov2fg5dsmvqw2rtpojjgk43povzggzkqmf2gq) with the full path.

The __resourcePathForLocalizedResourceNamed__ method first searches the current locale's language directory for the resource then the `Nonlocalized.lproj` directory. If it finds the resource, it returns the resource's path. Otherwise it returns `null`. You can specify a subdirectory for the method to search in. For example, if the current locale is English, and the resources are organized as shown in [Listing 0-1](#apple-infeircci5dus), and you invoke __resourcePathForLocalizedResourceNamed__ for the "`Edit.html`" resource in the "`Edit.wo`" subdirectory, the method returns "`English.lproj/Edit.wo/Edit.html`". If the current locale is German, the method returns "`Nonlocalized.lproj/Edit.wo/Edit.html`".

## Method Types

---

> **Accessing resources**
>
> : [bytesForResourcePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxwe6lumvzum33skjsxg33vojrwkudborua): [inputStreamForResourcePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxws3tqov2fg5dsmvqw2rtpojjgk43povzggzkqmf2gq)
>
> **Finding bundles**
>
> : [frameworkBundles](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpmzzgc3lfo5xxe22covxgi3dfom): [bundleForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpmj2w4zdmmvdg64sdnrqxg4y): [bundleForName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpmj2w4zdmmvdg64somfwwk): [mainBundle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpnvqws3scovxgi3df)
>
> **Getting resource paths**
>
> : [resourcePathsForDirectories](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxerdjojswg5dpojuwk4y): [resourcePathForLocalizedResourceNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2cgn5zey33dmfwgs6tfmrjgk43povzggzkomfwwkza): [resourcePathsForLocalizedResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxetdpmnqwy2l2mvsfezltn52xey3fom): [resourcePathsForResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxeutfonxxk4tdmvzq)
>
> **Getting bundle class information**
>
> : [bundleClassPackageNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxwe5lomrwgkq3mmfzxgudbmnvwcz3fjzqw2zlt): [bundleClassNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxwe5lomrwgkq3mmfzxgttbnvsxg)
>
> **Getting bundle attributes**
>
> : [isFramework](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxws42gojqw2zlxn5zgw): [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxw4ylnmu): [principalClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxa4tjnzrws4dbnrbwyyltom): [properties](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxa4tpobsxe5djmvzq)
>
> **Methods inherited from Object**
>
> : [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxi32torzgs3th)
>
> **Deprecated methods**
>
> : [allBundles](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpmfwgyqtvnzsgyzlt): [allFrameworks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpmfwgyrtsmfwwk53pojvxg): [bundlePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxwe5lomrwgkudborua): [bundleWithPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpmj2w4zdmmvlws5dikbqxi2a): [infoDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxws3tgn5cgsy3unfxw4ylspe): [load](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxwy33bmq): [pathForResource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxaylunbdg64ssmvzw65lsmnsq): [pathsForResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxaylunbzum33skjsxg33vojrwk4y): [resourcePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2a)

## Static Methods

---

### allBundles

`public synchronized static NSArray allBundles()`

Deprecated in the Java Foundation framework. Don't use this method. The only non-framework bundle that an application can access without deprecated API is the main bundle. Use [mainBundle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpnvqws3scovxgi3df) instead. Returns an array containing all the non-framework bundles available to the application.

---

### allFrameworks

`public static NSArray allFrameworks()`

Deprecated in the Java Foundation framework. Don't use this method. Use [frameworkBundles](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpmzzgc3lfo5xxe22covxgi3dfom) instead.

Returns an array containing the bundles for all the frameworks included in the application.

---

### bundleForClass

`public synchronized static NSBundle bundleForClass(Class aClass)`

Returns the bundle containing the class _aClass_.

---

### bundleForName

`public synchronized static NSBundle bundleForName(String name)`

Returns the bundle with the specified name. See [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxw4ylnmu) for more information about how the name relates to the bundle on the file system.

---

### bundleWithPath

`public static NSBundle bundleWithPath(String path)`

Deprecated in the Java Foundation framework. Don't use this method. To access a bundle that was loaded when the application started, use [bundleForName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpmj2w4zdmmvdg64somfwwk) or [bundleForClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgqtvnzsgyzjpmj2w4zdmmvdg64sdnrqxg4y).

Returns an NSBundle that corresponds to the specified directory _path_ or returns `null` if _path_ does not identify an accessible bundle directory.

If the bundle object for the specified directory doesn't already exists, this method creates the returned bundle.

---

### frameworkBundles

`public synchronized static NSArray frameworkBundles()`

Returns an array containing the bundles for all the frameworks included in the application.

---

### mainBundle

`public static NSBundle mainBundle()`

Returns the application's main bundle. In general, the main bundle corresponds to an application file package or application wrapper: a directory that bears the name of the application and is marked by a "`.woa`" extension.

---

## Instance Methods

---

### bundleClassNames

`public NSArray bundleClassNames()`

Returns an array containing the names of all the receiver's classes.

---

### bundleClassPackageNames

`public NSArray bundleClassPackageNames()`

Returns an array containing the names of all the packages containing the receiver's classes.

---

### bundlePath

`public String bundlePath()`

Deprecated in the Java Foundation framework. Don't use this method. You should not need to know the file system path to the bundle directory.

Returns the full file system path name of the receiver's bundle directory.

---

### bytesForResourcePath

`public byte[] bytesForResourcePath(String resourcePath)`

Returns a byte array containing the data for the resource specified by _resourcePath_. The resource path must be specified relative to the top level of the resources hierarchy, that is, the directory containing the language subdirectories. Note that the resource path for a resource is not the same as its file system path. See ["Determining Available Resources" (page 26)](#apple-infeiscjirbem) for more information about resource paths.

---

### infoDictionary

`public NSDictionary infoDictionary()`

Deprecated in the Java Foundation framework. Don't use this method.

Returns a dictionary that contains information about the receiver. This information is extracted from the property list associated with the bundle. The `CustomInfo.plist` file is a source file for the bundle's property list.

---

### inputStreamForResourcePath

`public java.io.InputStream inputStreamForResourcePath(String resourcePath)`

Returns an input stream for the resource specified by _resourcePath_. The resource path must be specified relative to the top level of the resources hierarchy, that is, the directory containing the language subdirectories. Note that the resource path for a resource is not the same as its file system path. See ["Determining Available Resources" (page 26)](#apple-infeiscjirbem) for more information about resource paths.

---

### isFramework

`public boolean isFramework()`

Returns whether the receiver represents a framework or not.

---

### load

`public boolean load()`

Deprecated in the Java Foundation framework. Don't use this method. Dynamic loading is no longer supported. Returns `true` if the bundle was loaded at application startup, otherwise returns `false`.

---

### name

`public String name()`

Returns the name of the bundle. If the bundle is a Java WebObjects Application, this method returns the name of the directory containing the application without the "`.woa`" extension. If the bundle is a Java WebObjects Framework, this method returns the name of the directory containing the framework without the "`.framework`" extension.

---

### pathForResource

`public String pathForResource( String name, String extension)`

Deprecated in the Java Foundation framework. Don't use this method. Use [resourcePathForLocalizedResourceNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2cgn5zey33dmfwgs6tfmrjgk43povzggzkomfwwkza) instead.

Returns the full file system path name for the resource identified by _name_ with the specified file extension. If the _extension_ argument is `null` or an empty string (""), the resource sought is identified by _name_, with any (or no) extension. The method first looks for a non-localized resource in the immediate bundle directory; if the resource is not there, it looks for the resource in the language-specific "`.lproj`" directory (the local language is determined by user defaults).

`public String pathForResource( String name, String extension, String bundlePath)`

Deprecated in the Java Foundation framework. Don't use this method. Use [resourcePathForLocalizedResourceNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2cgn5zey33dmfwgs6tfmrjgk43povzggzkomfwwkza) instead.

Returns the full file system path name for the resource identified by _name_, with the specified file name extension, and residing in the directory _bundlePath_; returns `null` if no matching resource file exists in the bundle. The argument _bundlePath_ must be a valid bundle directory or __null__. The argument _extension_ can be an empty string or `null`; in either case the pathname returned is the first one encountered with _name_, regardless of the extension. The method searches in this order:

- `<main bundle path>/Resources/bundlePath/name.extension`
- `<main bundle path>/Resources/bundlePath/<language.lproj>/name.extension`
- `<main bundle path>/bundlePath/name.extension`
- `<main bundle path>/bundlePath/<language.lproj>/name.extension`

The order of language directories searched corresponds to the user's preferences. If _bundlePath_ is `null`, the same search order as described above is followed, minus _bundlePath_.

|  |
| --- |
| __Note:__ These methods search for resources based on the resource organization on the file system, not the internal NSBundle resource organization as described in the [NSBundle](#apple-infeiq2diveuq) class description. Specifically, these methods do not support the "`Nonlocalized.lproj`" directory. Also, the methods do not "drill-down" into the subdirectories of the specified bundle path (except for the `language.lproj` subdirectories). |

---

### pathsForResources

`public NSArray pathsForResources( String extension, String bundlePath)`

Deprecated in the Java Foundation framework. Don't use this method. Use [resourcePathsForResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxeutfonxxk4tdmvzq) instead. Returns an array containing file system path names for all bundle resources having the specified file name extension and residing in the directory _bundlePath_; returns an empty array if no matching resource files are found. This method provides a means for dynamically discovering bundle resources. The argument _bundlePath_ must be a valid bundle directory or __null__. The _extension_ argument can be an empty string or `null`; if you specify either of these for _extension_, all bundle resources are returned. Although there is no guaranteed search order, all of the following directories will be searched:

- `<main bundle path>/Resources/bundlePath/name.extension`
- `<main bundle path>/Resources/bundlePath/<language.lproj>/name.extension`
- `<main bundle path>/bundlePath/name.extension`
- `<main bundle path>/bundlePath/<language.lproj>/name.extension`

The language directories searched corresponds to the current locale. If _bundlePath_ is __null__, the same search order as described above is followed, minus _bundlePath_.

|  |
| --- |
| __Note:__ This method searches for resources based on the resource organization on the file system, not the internal NSBundle resource organization as described in the [NSBundle](#apple-infeiq2diveuq) class description. Specifically, these methods do not support the "`Nonlocalized.lproj`" directory. Also, the methods do not "drill-down" into the subdirectories of the specified bundle path (except for the `language.lproj` subdirectories). |

---

### principalClass

`public Class principalClass()`

Returns the NSBundle's principal class. The principal class is responsible for ensuring that all classes in the framework are properly initialized. The NSBundle determines its principal class based on the bundle's property list. The property list represents a dictionary; the principle class is the value obtained using the key `NSPrincipalClass`. If the principal class is not specified in the property list, the method returns `null`. If you create a framework that needs to be initialized using a principal class, you must specify the class name in the `CustomInfo.plist` file, a source file for the bundle's property list. For example, if your principal class is `myPackage.myPrincipalClass`, your `CustomInfo.plist` file should look like:
> ```
> {
>     NSPrincipalClass = myPackage.myPrincipalClass;
> }
> ```

---

### properties

`public java.util.Properties properties()`

Returns the receiver's properties. These properties are located in the `Properties` file in the `Resources` subdirectory of the directory corresponding to the receiver. See the [NSBundle](NSProperties.md#apple-infeiq2diveuq) class for more information about the `Properties` file.

---

### resourcePath

`public String resourcePath()`

Deprecated in the Java Foundation framework. Don't use this method. Resources are now accessed using the [bytesForResourcePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxwe6lumvzum33skjsxg33vojrwkudborua) and [inputStreamForResourcePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxws3tqov2fg5dsmvqw2rtpojjgk43povzggzkqmf2gq) methods.

Returns the full file system path name of the receiving bundle's subdirectory containing resources.

|  |
| --- |
| __Note:__ In the Java Foundation Framework, the term _resource path_ refers to the full specification of the location of a resource in an NSBundle. In previous versions of the Foundation Framework, the term _resource path_ referred to the file system path to the directory containing a bundle's resources. |

---

### resourcePathsForDirectories

`public NSArray resourcePathsForDirectories(String extension, String subdirectory)`

Returns an array containing the resource paths of all the directories with the specified extension beneath the specified subdirectory. If _extension_ is `null`, the method includes directories regardless of extension. If _subdirectory_ is `null`, the method returns directories beneath the top level directory (the one containing the language directories). For examples of how this method is used, see ["Determining Available Resources" (page 26)](#apple-infeiscjirbem).

__See Also:__ [resourcePathsForResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxeutfonxxk4tdmvzq), [resourcePathsForLocalizedResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxetdpmnqwy2l2mvsfezltn52xey3fom)

---

### resourcePathForLocalizedResourceNamed

`public String resourcePathForLocalizedResourceNamed(String name, String subdirectory)`

Returns the resource path for the localized resource with the specified name within the specified subdirectory. This method determines the resource path based on the current locale. See ["Accessing NSBundle Resources" (page 29)](#apple-infeissdifdum) for more information about how this method chooses the resource path it returns.

If _subdirectory_ is `null`, the method returns a resource path for a localized resource at the language directory level.

__See Also:__ [resourcePathsForLocalizedResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxetdpmnqwy2l2mvsfezltn52xey3fom), [resourcePathsForResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxeutfonxxk4tdmvzq), [resourcePathsForDirectories](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxerdjojswg5dpojuwk4y)

---

### resourcePathsForLocalizedResources

`public NSArray resourcePathsForLocalizedResources(String extension, String subdirectory)`

Returns an array containing the resource paths for all of the receiver's resources that are appropriate for the current locale, have the specified file extension, and lie within the specified subdirectory. See ["Determining Available Resources" (page 26)](#apple-infeiscjirbem) for more information about how this method chooses the resource paths it returns.

If _extension_ is `null`, the method includes localized resources regardless of extension. If _subdirectory_ is `null`, the method returns localized resources beneath the top level directory (the one containing the language directories).

__See Also:__ [resourcePathsForResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxeutfonxxk4tdmvzq), [resourcePathsForDirectories](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxerdjojswg5dpojuwk4y)

---

### resourcePathsForResources

`public NSArray resourcePathsForResources(String extension, String subdirectory)`

Returns an array containing the resource paths of all of the receiver's resources that have the specified file extension and lie within the specified subdirectory. For examples of how this method is used, see ["Determining Available Resources" (page 26)](#apple-infeiscjirbem).

If _extension_ is `null`, the method includes resources regardless of extension. If _subdirectory_ is `null`, the method returns resources beneath the top level directory (the one containing the language directories).

__See Also:__ [resourcePathsForLocalizedResources](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxetdpmnqwy2l2mvsfezltn52xey3fom), [resourcePathsForDirectories](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2dtizxxerdjojswg5dpojuwk4y)

---

### toString

`public String toString()`

Returns a string representation of the receiver including its class name (NSBundle or a subclass), its [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxw4ylnmu), its path, the names of its packages (as returned by [bundleClassPackageNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxwe5lomrwgkq3mmfzxgudbmnvwcz3fjzqw2zlt)), and the number of classes it contains.

---

## Notifications

---

### BundleDidLoadNotification

`public static String BundleDidLoadNotification`

### LoadedClassesNotification

`public static final String LoadedClassesNotification`

Description forthcoming.

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
