---
title: Bundle Programming Guide
apple_id: 10000123i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/AccessingaBundlesContents/AccessingaBundlesContents.html
archived_at: '2026-07-15T07:22:12.149477Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Bundle Programming Guide](Introduction.md)


[Next](Document%20Packages.md)[Previous](Bundle%20Structures.md)

# Accessing a Bundle’s Contents

When writing bundle-based code, you never use string constants to refer to the location of files in your bundle. Instead, you use the [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) class or [CFBundleRef](https://developer.apple.com/documentation/corefoundation/cfbundle) opaque type to obtain the path to the file you want. The reason is that the path to the desired file can vary depending on the user’s native language and the bundle’s supported localizations. By letting the bundle determine the location of the file, you are always assured of loading the correct file.

This chapter shows you how to use the `NSBundle` class and `CFBundleRef` opaque type to locate files and obtain other information about your bundle. Although these types are not directly interchangeable, they provide comparable features. And at least in Objective-C applications, you can use whichever type suits your needs.

Before you can access a bundle’s resources, you must first obtain an appropriate [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) object or [CFBundleRef](https://developer.apple.com/documentation/corefoundation/cfbundle) opaque type. The following sections outline the different ways you can get a reference to one of these types.

The main bundle is the bundle that contains the code and resources for the running application. If you are an application developer, this is the most commonly used bundle. The main bundle is also the easiest to retrieve because it does not require you to provide any information.

To get the main bundle in a Cocoa application, call the [mainBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/clm/NSBundle/mainBundle) class method of the `NSBundle` class, as shown in Listing 3-1.

__Listing 3-1__  Getting a reference to the main bundle using Cocoa

```
NSBundle* mainBundle;

// Get the main bundle for the app.
mainBundle = [NSBundle mainBundle];
```

If you are writing a C-based application, you can use the [CFBundleGetMainBundle](https://developer.apple.com/documentation/corefoundation/1537085-cfbundlegetmainbundle) function to retrieve the main bundle for your application, as shown in Listing 3-2.

__Listing 3-2__  Getting a reference to the main bundle using Core Foundation

```
CFBundleRef mainBundle;

// Get the main bundle for the app
mainBundle = CFBundleGetMainBundle();
```

When getting the main bundle, it is still a good idea to make sure the value you get back represents a valid bundle. When retrieving the main bundle from any application, the returned value might be `NULL` in the following situations:

- If a program is not bundled, attempting to get the main bundle might return a `NULL` value. The bundle code may try to create a main bundle to represent your program’s contents, but doing so is not possible in all cases.
- If the agent that launched the program did not specify the full path to the program's executable in the `argv` parameters, the main bundle value might be `NULL`. Bundles rely on either the path to the executable being in `argv[0]` or the presence of the executable's path in the `PATH` environment variable. If neither of these is present, the bundle routines might not be able to find the main bundle directory. Programs launched by `xinetd` often experience this problem when `xinetd` changes the current directory to `/`.

If you want to access a bundle other than the main bundle, you can create an appropriate bundle object if you know the path to the bundle directory. Creating a bundle by path is useful in situations where you are defining frameworks or other loadable bundles and know in advance where those bundles will be located.

To obtain the bundle at a specific path using Cocoa, call the [bundleWithPath:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/clm/NSBundle/bundleWithPath:) class method of the `NSBundle` class. (You can also use the [initWithPath:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/initWithPath:) instance method to initialize a new bundle object.) This method takes a string parameter representing the full path to the bundle directory. Listing 3-3 shows an example that accesses a bundle in a local directory.

__Listing 3-3__  Locating a Cocoa bundle using its path

```
NSBundle* myBundle;

// Obtain a reference to a loadable bundle.
myBundle = [NSBundle bundleWithPath:@"/Library/MyBundle.bundle"];
```

To obtain the bundle at a specific path using Core Foundation, call the [CFBundleCreate](https://developer.apple.com/documentation/corefoundation/1537154-cfbundlecreate) function. When specifying the path location in Core Foundation, you must do so using a `CFURLRef` type. Listing 3-4 shows an example that takes the fixed directory from the preceding example, converts it to a URL, and uses that URL to access the bundle.

__Listing 3-4__  Locating a Core Foundation bundle using its path

```
CFURLRef bundleURL;
CFBundleRef myBundle;

// Make a CFURLRef from the CFString representation of the
// bundle’s path.
bundleURL = CFURLCreateWithFileSystemPath(
                kCFAllocatorDefault,
                CFSTR("/Library/MyBundle.bundle"),
                kCFURLPOSIXPathStyle,
                true );

// Make a bundle instance using the URLRef.
myBundle = CFBundleCreate( kCFAllocatorDefault, bundleURL );

// You can release the URL now.
CFRelease( bundleURL );

// Use the bundle...

// Release the bundle when done.
CFRelease( myBundle );
```


Even if you do not know the exact path to a bundle, you can still search for it in some known location. For example, an application with a `PlugIns` directory might want to get a list of all the bundles in that directory. Once you have the path to the directory, you can use the appropriate routines to iterate that directory and return any bundles.

The simplest way to find all of the bundles in a specific directory is to use the [CFBundleCreateBundlesFromDirectory](https://developer.apple.com/documentation/corefoundation/1537125-cfbundlecreatebundlesfromdirecto) function. This function returns new `CFBundleRef` types for all of the bundles in a given directory. Listing 3-5 shows how you would use this function to retrieve all of the plug-ins in the application’s `PlugIns` directory.

__Listing 3-5__  Obtaining bundle references for a set of plug-ins

```
CFBundleRef mainBundle = CFBundleGetMainBundle();
CFURLRef plugInsURL;
CFArrayRef bundleArray;

// Get the URL to the application’s PlugIns directory.
plugInsURL = CFBundleCopyBuiltInPlugInsURL(mainBundle);

// Get the bundle objects for the application’s plug-ins.
bundleArray = CFBundleCreateBundlesFromDirectory( kCFAllocatorDefault,
                    plugInsURL, NULL );

// Release the CF objects when done with them.
CFRelease( plugInsURL );
CFRelease( bundleArray );
```


Locating bundles using a bundle identifier is an efficient way to locate bundles that were previously loaded into memory. A bundle identifier is the string assigned to the `CFBundleIdentifier` key in the bundle’s `Info.plist` file. This string is typically formatted using reverse-DNS notation so as to prevent name space conflicts with developers in other companies. For example, a Finder plug-in from Apple might use the string `com.apple.Finder.MyGetInfoPlugin` as its bundle identifier. Rather than passing a pointer to a bundle object around your code, clients that need a reference to a bundle can simply use the bundle identifier to retrieve it.

To retrieve a bundle using a bundle identifier in Cocoa, call the [bundleWithIdentifier:](https://developer.apple.com/documentation/foundation/bundle/1411929-init) class method of the `NSBundle` class, as shown in Listing 3-6.

__Listing 3-6__  Locating a bundle using its identifier in Cocoa

```
NSBundle* myBundle = [NSBundle bundleWithIdentifier:@"com.apple.myPlugin"];
```

Listing 3-7 shows how to retrieve a bundle using its bundle identifier in Core Foundation.

__Listing 3-7__  Locating a bundle using its identifier in Core Foundation

```
CFBundleRef requestedBundle;

 // Look for a bundle using its identifier
 requestedBundle = CFBundleGetBundleWithIdentifier(
        CFSTR("com.apple.Finder.MyGetInfoPlugIn") );
```

Remember that you can only use a bundle identifier to locate a bundle that has already been opened. For example, you could use this technique to open the main bundle and bundles for all statically linked frameworks. You could not use this technique to get a reference to a plug-in that had not yet been loaded.

If you are writing a Cocoa application, you can obtain a list of bundles related to the application by calling the [allBundles](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/clm/NSBundle/allBundles) and [allFrameworks](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/clm/NSBundle/allFrameworks) class methods of `NSBundle`. These methods create an array of `NSBundle` objects corresponding to the bundles or frameworks currently in use by your application. You can use these methods as convenience functions rather than maintain a collection of loaded bundles yourself.

The [bundleForClass:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/clm/NSBundle/bundleForClass:) class method is another way get related bundle information in a Cocoa application. This method returns the bundle in which a particular class is defined. Again, this method is mostly for convenience so that you do not have to retain a pointer to an `NSBundle` object that you may use only occasionally.

If you have a reference to a bundle object, you can use that object to determine the location of resources inside the bundle. Cocoa and Core Foundation both provide different ways of locating resources inside a bundle. In addition, you should understand how those frameworks look for resource files within your bundle so as to make sure you put files in the right places at build time.

As long as you use an [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) object or a [CFBundleRef](https://developer.apple.com/documentation/corefoundation/cfbundle) opaque type to locate resources, your bundle code need never concern itself with how resources are retrieved from a bundle. Both `NSBundle` and `CFBundleRef` retrieve the appropriate language-specific resource automatically based on the available user settings and bundle configuration. However, you still have to put all those language-specific resources into your bundle, so knowing how they are retrieved is important.

The bundle programming interfaces follow a specific search algorithm to locate resources within the bundle. Global resources have the highest priority, followed by region- and language-specific resources. When considering region- and language-specific resources, the algorithm takes into account both the settings for the current user and development region information in the bundle’s `Info.plist` file.

First, the bundle determines which localization to use for the application as a whole. If a `.lproj` folder exists for the preferred language, that localization is used. Otherwise, the bundle searches for an `.lproj` folder matching the next preferred language, and so on, until one is found. If there is no localization for a preferred language, the bundle chooses the development language localization.

Then the bundle searches for the resource in the following order:

1. Global (nonlocalized) resources
2. Region-specific localized resources (based on the user’s region preferences)
3. [Language-specific localized resources](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Internationalization.html#//apple_ref/doc/uid/TP40008195-CH23) (based on the user’s language preferences)
4. Development language resources (as specified by the `CFBundleDevelopmentRegion` in the bundle’s `Info.plist` file.)

Because global resources take precedence over language-specific resources, there should _never_ be both a global and localized version of a given resource. If a global version of a resource exists, language-specific versions of the same resource are never returned. The reason for this precedence is performance. If localized resources were searched first, the bundle routines might search needlessly in several localized resource directories before discovering the global resource.

In iOS 4.0 and later, it is possible to mark individual resource files as usable only on a specific type of device. This capability simplifies the code you have to write for Universal applications. Rather than creating separate code paths to load one version of a resource file for iPhone and a different version of the file for iPad, you can let the bundle-loading routines choose the correct file. All you have to do is name your resource files appropriately.

To associate a resource file with a particular device, you add a custom modifier string to its filename. The inclusion of this modifier string yields filenames with the following format:

_<basename>__<device>_`.`_<filename_extension>_

The _<basename>_ string represents the original name of the resource file. It also represents the name you use when accessing the file from your code. Similarly, the _<filename_extension>_ string is the standard filename extension used to identify the type of the file. The _<device>_ string is a case-sensitive string that can be one of the following values:

- `~ipad` - The resource should be loaded on iPad devices only.
- `~iphone` - The resource should be loaded on iPhone or iPod touch devices only.

You can apply device modifiers to any type of resource file. For example, suppose you have an image named `MyImage.png`. To specify different versions of the image for iPad and iPhone, you would create resource files with the names `MyImage~ipad.png` and `MyImage~iphone.png` and include them both in your bundle. To load the image, you would continue to refer to the resource as `MyImage.png` in your code and let the system choose the appropriate version, as shown here:

```
UIImage* anImage = [UIImage imageNamed:@"MyImage.png"];
```

On an iPhone or iPod touch device, the system loads the `MyImage~iphone.png` resource file, while on iPad, it loads the `MyImage~ipad.png` resource file. If a device-specific version of a resource is not found, the system falls back to looking for a resource with the original filename, which in the preceding example would be an image named `MyImage.png`.

In order to locate a resource file in a bundle, you need to know the name of the file, its type, or a combination of the two. Filename extensions are used to identify the type of a file; therefore, it is important that your resource files include the appropriate extensions. If you used custom subdirectories in your bundle to organize resource files, you can speed up the search by providing the name of the subdirectory that contains the desired file.

Even if you do not have a bundle object, you can still search for resources in directories whose paths you know. Both Core Foundation and Cocoa provide API for searching for files using only path-based information. (For example, in Cocoa you can use the [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) object to enumerate the contents of directories and test for the existence of files.) However, if you plan to retrieve more than one resource file, it is always faster to use a bundle object. Bundle objects cache search information as they go, so subsequent searches are usually faster.

If you have an `NSBundle` object, you can use the following methods to find the location of resources in that bundle:

- [pathForResource:ofType:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/pathForResource:ofType:)
- [pathForResource:ofType:inDirectory:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/pathForResource:ofType:inDirectory:)
- [pathForResource:ofType:inDirectory:forLocalization:](https://developer.apple.com/documentation/foundation/bundle/1413471-path)
- [pathsForResourcesOfType:inDirectory:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/pathsForResourcesOfType:inDirectory:)
- [pathsForResourcesOfType:inDirectory:forLocalization:](https://developer.apple.com/documentation/foundation/bundle/1416940-paths)

Suppose you have placed an image called `Seagull.jpg` in your application’s main bundle. Listing 3-8 shows you how to retrieve the path for this image file from the application’s main bundle.

__Listing 3-8__  Finding a single resource file using `NSBundle`

```
NSBundle* myBundle = [NSBundle mainBundle];
NSString* myImage = [myBundle pathForResource:@"Seagull" ofType:@"jpg"];
```

If you wanted to look for all image resources in your top-level resource directory, instead of looking for just a single resource, you could use the `pathsForResourcesOfType:inDirectory:` method or one of its equivalents, as shown in Listing 3-9

__Listing 3-9__  Finding multiple resources using `NSBundle`

```
NSBundle* myBundle = [NSBundle mainBundle];
NSArray* myImages = [myBundle pathsForResourcesOfType:@"jpg"
                              inDirectory:nil];
```


If you have a `CFBundleRef` opaque type, you can use the following methods to find the location of resources in that bundle:

- [CFBundleCopyResourceURL](https://developer.apple.com/documentation/corefoundation/1537117-cfbundlecopyresourceurl)
- [CFBundleCopyResourceURLInDirectory](https://developer.apple.com/documentation/corefoundation/1537138-cfbundlecopyresourceurlindirecto)
- [CFBundleCopyResourceURLsOfType](https://developer.apple.com/documentation/corefoundation/1537121-cfbundlecopyresourceurlsoftype)
- [CFBundleCopyResourceURLsOfTypeInDirectory](https://developer.apple.com/documentation/corefoundation/1537140-cfbundlecopyresourceurlsoftypein)
- [CFBundleCopyResourceURLsOfTypeForLocalization](https://developer.apple.com/documentation/corefoundation/1537162-cfbundlecopyresourceurlsoftypefo)

Suppose you have placed an image called `Seagull.jpg` in your application’s main bundle. Listing 3-10 shows you how to search for this image by name and type using the Core Foundation function `CFBundleCopyResourceURL`. In this case, the code looks for the file named “Seagull” with the file type (filename extension) of “jpg” in the bundle’s resource directory.

__Listing 3-10__  Finding a single resource using a `CFBundleRef`

```
    CFURLRef    seagullURL;

    // Look for a resource in the main bundle by name and type.
    seagullURL = CFBundleCopyResourceURL( mainBundle,
                    CFSTR("Seagull"),
                    CFSTR("jpg"),
                    NULL );
```

Suppose that instead of searching for one image file, you wanted to get the names of all image files in a directory called `BirdImages`. You could load all of the JPEGs in the directory using the function `CFBundleCopyResourceURLsOfType`, as shown in Listing 3-11.

__Listing 3-11__  Finding multiple resources using a `CFBundleRef`

```
    CFArrayRef  birdURLs;

    // Find all of the JPEG images in a given directory.
    birdURLs = CFBundleCopyResourceURLsOfType( mainBundle,
                    CFSTR("jpg"),
                    CFSTR("BirdImages") );
```


Once you have a reference to a resource file, you can load its contents and use it in your application. The steps you must take to load and use resource files depends on the type of resource, and as such is not covered in this document. For detailed information about loading and using resources, see _[Resource Programming Guide](../../Cocoa/Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_.

With a valid bundle object, you can retrieve the path to the top-level bundle directory as well as paths to many of its subdirectories. Using the available interfaces to retrieve directory paths insulates your code from having to know the exact structure of the bundle or its location in the system. It also allows you to use the same code on different platforms. For example, you could use the same code to retrieve resources from an iOS application or a Mac app, which have different bundle structures.

To get the path to the top-level bundle directory using Cocoa, you use the [bundlePath](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/bundlePath) method of the corresponding `NSBundle` object. You can also use the [builtInPlugInsPath](https://developer.apple.com/documentation/foundation/nsbundle/1408900-builtinpluginspath), `[resourcePath](../../../../LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSBundle.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstij2w4zdmmuxxezltn52xey3fkbqxi2a)`, [sharedFrameworksPath](https://developer.apple.com/documentation/foundation/bundle/1417226-sharedframeworkspath), and [sharedSupportPath](https://developer.apple.com/documentation/foundation/nsbundle/1411609-sharedsupportpath) methods to obtain the paths for key subdirectories of the bundle. These methods return path information using an `NSString` object, which you can pass directly to most other `NSBundle` methods or convert to an `NSURL` object as needed.

Core Foundation also defines functions for retrieving several different internal bundle directories. To get the path of the bundle itself, you can use the [CFBundleCopyBundleURL](https://developer.apple.com/documentation/corefoundation/1537142-cfbundlecopybundleurl) function. You can also use the [CFBundleCopyBuiltInPlugInsURL](https://developer.apple.com/documentation/corefoundation/1537106-cfbundlecopybuiltinpluginsurl), [CFBundleCopyResourcesDirectoryURL](https://developer.apple.com/documentation/corefoundation/1537113-cfbundlecopyresourcesdirectoryur), [CFBundleCopySharedFrameworksURL](https://developer.apple.com/documentation/corefoundation/1537159-cfbundlecopysharedframeworksurl), and [CFBundleCopySupportFilesDirectoryURL](https://developer.apple.com/documentation/corefoundation/1537118-cfbundlecopysupportfilesdirector) functions to obtain the locations of key subdirectories of the bundle. Core Foundation always returns bundle paths as a `CFURLRef` opaque type. You can use this type to extract a `CFStringRef` type that you can then pass to other Core Foundation routines.

One file that every bundle should contain is an [information property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) (`Info.plist`) file. This file is an XML-based text file that contains specific types of key-value pairs. These key-value pairs specify information about the bundle, such as its ID string, version number, development region, type, and other important properties. (See _[Runtime Configuration Guidelines](../../Mac%20OSX/Runtime%20Configuration%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3ta2i)_ for the list of keys you can include in this file.) Bundles may also include other types of configuration data, mostly organized in XML-based property lists.

The `NSBundle` class provides the [objectForInfoDictionaryKey:](https://developer.apple.com/documentation/foundation/nsbundle/1408696-objectforinfodictionarykey) and [infoDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/infoDictionary) methods for retrieving information from the `Info.plist` file. The `objectForInfoDictionaryKey:` method returns the localized value for a key and is the preferred method to call. The `infoDictionary` method returns an `NSDictionary` with all of the keys from the property list; however, it does not return any localized values for these keys. For more information, see the _[NSBundle Class Reference](https://developer.apple.com/documentation/foundation/nsbundle)_.

Core Foundation also offers functions for retrieving specific pieces of data from a bundle’s information property list file, including the bundle’s ID string, version, and development region. You can retrieve the localized value for a key using the [CFBundleGetValueForInfoDictionaryKey](https://developer.apple.com/documentation/corefoundation/1537102-cfbundlegetvalueforinfodictionar) function. You can also retrieve the entire dictionary of non-localized keys using [CFBundleGetInfoDictionary](https://developer.apple.com/documentation/corefoundation/1537165-cfbundlegetinfodictionary). For more information about these and related functions, see _[CFBundle Reference](https://developer.apple.com/documentation/corefoundation/cfbundle-s0a)_.

Listing 3-12 demonstrates how to retrieve the bundle’s version number from the information property list using Core Foundation functions. Though the value in the information property list may be written as a string, for example “2.1.0b7”, the value is returned as an unsigned long integer.

__Listing 3-12__  Obtaining the bundle’s version

```
    // This is the ‘vers’ resource style value for 1.0.0
    #define kMyBundleVersion1 0x01008000

    UInt32  bundleVersion;

    // Look for the bundle’s version number.
    bundleVersion = CFBundleGetVersionNumber( mainBundle );

    // Check the bundle version for compatibility with the app.
    if (bundleVersion < kMyBundleVersion1)
        return (kErrorFatalBundleTooOld);
```

Listing 3-13 shows you how to retrieve arbitrary values from the information property list using the `CFBundleGetInfoDictionary` function. The resulting information property list is an instance of the standard Core Foundation type [CFDictionaryRef](https://developer.apple.com/documentation/corefoundation/cfdictionaryref). For more information about retrieving information from a Core Foundation dictionary, see _[CFDictionary Reference](https://developer.apple.com/documentation/corefoundation/cfdictionary)_.

__Listing 3-13__  Retrieving information from a bundle’s information property list

```
    CFDictionaryRef bundleInfoDict;
    CFStringRef     myPropertyString;

    // Get an instance of the non-localized keys.
    bundleInfoDict = CFBundleGetInfoDictionary( myBundle );

    // If we succeeded, look for our property.
    if ( bundleInfoDict != NULL ) {
        myPropertyString = CFDictionaryGetValue( bundleInfoDict,
                    CFSTR("MyPropertyKey") );
    }
```

It is also possible to obtain an instance of a bundle’s information dictionary without a bundle object. To do this you use either the Core Foundation function [CFBundleCopyInfoDictionaryInDirectory](https://developer.apple.com/documentation/corefoundation/1537135-cfbundlecopyinfodictionaryindire) or the Cocoa [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) class. This can be useful for searching the information property lists of a set of bundles without first creating bundle objects.

The key to loading code from an external bundle is finding an appropriate entry point into the bundle’s executable file. As with other plug-in schemes, this requires some coordination between the application developer and the plug-in developer. You can publish a custom API for bundles to implement or define a formal plug-in interface. In either case, once you have an appropriate bundle or plug-in, you use the `NSBundle` class (or the `CFBundleRef` opaque type) to access the functions or classes implemented by the external code.

For additional information about loading and unloading code, see _[Code Loading Programming Topics](../../Cocoa/Code%20Loading%20Programming%20Topics/Introduction%20to%20Dynamically%20Loading%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2te2i)_.

If you are working in C, C++, or even in [Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43), you can publish your interface as a set of C-based symbols, such as function pointers and global variables. Using the Core Foundation functions, you can load references to those symbols from a bundle’s executable file.

You can retrieve symbols using any of several functions. To retrieve function pointers, call either [CFBundleGetFunctionPointerForName](https://developer.apple.com/documentation/corefoundation/1537143-cfbundlegetfunctionpointerfornam) or [CFBundleGetFunctionPointersForNames](https://developer.apple.com/documentation/corefoundation/1537109-cfbundlegetfunctionpointersforna). To retrieve a pointer to a global variable, call [CFBundleGetDataPointerForName](https://developer.apple.com/documentation/corefoundation/1537120-cfbundlegetdatapointerforname) or [CFBundleGetDataPointersForNames](https://developer.apple.com/documentation/corefoundation/1537150-cfbundlegetdatapointersfornames). For example, suppose a loadable bundle defines the function shown in Listing 3-14.

__Listing 3-14__  An example function for a loadable bundle

```
    // Add one to the incoming value and return it.
    long addOne(short number)
    {
        return ( (long)number + 1 );
    }
```

Given a `CFBundleRef` opaque type, you would need to search for the desired function before you could use it in your code. Listing 3-15 shows a code fragment that illustrates this process. In this example, the `myBundle` variable is a `CFBundleRef` opaque type pointing to the bundle.

__Listing 3-15__  Finding a function in a loadable bundle

```
// Function pointer.
AddOneFunctionPtr addOne = NULL;

// Value returned from the loaded function.
long result = 0;

// Get a pointer to the function.
addOne = (void*)CFBundleGetFunctionPointerForName(
            myBundle, CFSTR("addOne") );

    // If the function was found, call it with a test value.
if (addOne)
{
    // This should add 1 to whatever was passed in
    result = addOne ( 23 );
}
```


If you are writing a Cocoa application, you can load the code for an entire class using the methods of [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle). The `NSBundle` methods for loading a class are for use with Objective-C classes only and cannot be used to load classes written in C++ or other object-oriented languages.

If a loadable bundle defines a principal class, you can load it using the [principalClass](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/principalClass) method of `NSBundle`. The `principalClass` method uses the `NSPrincipalClass` key of the bundle’s `Info.plist` file to identify and load the desired class. Using the principal class alleviates the need to agree on specific naming conventions for external classes, instead letting you focus on the behavior of those interfaces. For example, you might use an instance of the principal class as a factory for creating other relevant objects.

If you want to load an arbitrary class from a loadable bundle, call the [classNamed:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/classNamed:) method of `NSBundle`. This method searches the bundle for a class matching the name you specify. If the class exists in the bundle, the method returns the corresponding `Class` object, which you can then use to [create instances](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) of the class.

Listing 3-16 shows you a sample method for loading a bundle’s principal class.

__Listing 3-16__  Loading the principal class of a bundle

```objc
- (void)loadBundle:(NSString*)bundlePath
{
    Class exampleClass;
    id newInstance;
    NSBundle *bundleToLoad = [NSBundle bundleWithPath:bundlePath];
    if (exampleClass = [bundleToLoad principalClass])
    {
        newInstance = [[exampleClass alloc] init];
        // [newInstance doSomething];
    }
}
```

For more information about the methods of the `NSBundle` class, see _[NSBundle Class Reference](https://developer.apple.com/documentation/foundation/nsbundle)_.

In macOS v10.5 and later, you can unload the code associated with an `NSBundle` object using the [unload](https://developer.apple.com/documentation/foundation/nsbundle/1412388-unload) method. You might use this technique to free up memory in an application by removing plug-ins or other loadable bundles that you no longer need.

If you used Core Foundation to load your bundle, you can use the [CFBundleUnloadExecutable](https://developer.apple.com/documentation/corefoundation/1537149-cfbundleunloadexecutable) function to unload it. If your bundle might be unloaded, you need to ensure that string constants are handled correctly by setting an appropriate compiler flag.

When you compile a bundle with a minimum deployment target of macOS v10.2 (or later), the compiler automatically switches to generating strings that are truly constant in response to `CFSTR("...")`. The compiler also generates these constant strings if you compile with the flag `-fconstant-cfstrings`. Constant strings have many benefits and should be used when possible, however if you reference constant strings after the executable containing them is unloaded, the references will be invalid and will cause a crash. This might happen even if the strings have been retained, for example, as a result of being put in data structures, retained directly, and, in some cases, even copied. Rather than trying to make sure all such references are cleaned up at unload time (and some references might be created within the libraries, making them hard to track), it is best to compile unloadable bundles with the flag `-fno-constant-cfstrings`.

[Next](Document%20Packages.md)[Previous](Bundle%20Structures.md)

