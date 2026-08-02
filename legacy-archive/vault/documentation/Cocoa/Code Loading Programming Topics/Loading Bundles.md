---
title: Code Loading Programming Topics
apple_id: 10000052i
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/Tasks/LoadingBundles.html
archived_at: '2026-07-15T07:16:30.932274Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Loading Programming Topics](Introduction%20to%20Dynamically%20Loading%20Code.md)


[Next](Creating%20Loadable%20Bundles.md)[Previous](Plug-in%20Architectures.md)

# Loading Bundles

The NSBundle class provides methods for loading Cocoa bundles. This section describes the basics of bundle loading in a Cocoa application. Also covered are loading non-Cocoa bundles from a Cocoa application. This material is relevant for any developer using loadable bundles in their application.

The NSBundle class provides methods for loading executable code and resources from Cocoa bundles. It handles all the details of loading, including interacting with the Mach-O loader `dyld` and loading Objective-C symbols into the Objective-C runtime.

For information about using NSBundle to load non-code resources, see _[Resource Programming Guide](../Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_.

Loading Cocoa bundles consists of five basic steps:

1. Locate the bundle.
2. Create an NSBundle object to represent the bundle.
3. Load the bundle’s executable code.
4. Query the bundle for its principal class.
5. Instantiate an object of the principal class.

The following sections cover each of these steps in detail.

Your application can load bundles from any location, but if they are stored in standard locations you can use functions and methods provided by Cocoa to find them easily.

Loadable bundles that are packaged with your applications are typically included inside the application bundle in `Contents/PlugIns`. To retrieve the plug-in directory for the main application bundle, use NSBundle’s `builtInPlugInsPath` method.

This code fragment shows how to use NSBundle to retrieve an application’s plug-in directory, which may be named `PlugIns` or `Plug-ins` (the former supersedes the latter):

```
NSBundle *appBundle;
NSString *plugInsPath;

appBundle = [NSBundle mainBundle];
plugInsPath = [appBundle builtInPlugInsPath];
```

Although it is not the standard location, you can gain some convenience by storing loadable bundles in your application bundle’s `Resources` directory. Then you can use NSBundle’s `pathsForResourcesOfType:inDirectory:` method to find them. This code fragment finds all files and directories with the extension `.bundle` in the application’s `Resources/PlugIns` directory:

```
NSBundle *appBundle;
NSArray *bundlePaths;

appBundle = [NSBundle mainBundle];
bundlePaths = [appBundle pathsForResourcesOfType:@"bundle"
               inDirectory:@"PlugIns"];
```

Your application may also support bundles in application support directories within the `Library` directory in multiple domains: user-specific (`~/Library`), system-wide (`/Library`), network (`/Network/Library`). To search for these and other standard directories, use the `NSSearchPathForDirectoriesInDomains` function.

This code fragment creates an array of search paths for your application to find bundles, which you can then search for individual plug-ins:

```
NSString *appSupportSubpath = @"Application Support/KillerApp/PlugIns";
NSArray *librarySearchPaths;
NSEnumerator *searchPathEnum;
NSString *currPath;
NSMutableArray *bundleSearchPaths = [NSMutableArray array];

// Find Library directories in all domains except /System
librarySearchPaths = NSSearchPathForDirectoriesInDomains(
    NSLibraryDirectory, NSAllDomainsMask - NSSystemDomainMask, YES);

// Copy each discovered path into an array after adding
// the Application Support/KillerApp/PlugIns subpath
searchPathEnum = [librarySearchPaths objectEnumerator];
while(currPath = [searchPathEnum nextObject])
{
    [bundleSearchPaths addObject:
        [currPath stringByAppendingPathComponent:appSupportSubpath]];
}
```


To create an NSBundle object for a bundle you want to load, either allocate an object and use the `initWithPath:` initializer or use the convenience creation method `bundleWithPath:`. If an instance already exists for the bundle, both of these methods return the existing instance instead of creating a new one.

This code fragment retrieves the bundle located at `fullPath`:

```
NSString *fullPath; // Assume this exists.
NSBundle *bundle;

bundle = [NSBundle bundleWithPath:fullPath];
```


To load a bundle’s executable code, use NSBundle’s `load` method. This method returns `YES` if loading was successful or if the code had already been loaded, and `NO` otherwise.

This code fragment loads the code for the bundle at `fullPath`:

```
NSString *fullPath; // Assume this exists.
NSBundle *bundle;

bundle = [NSBundle bundleWithPath:fullPath];
[bundle load];
```


Every Cocoa bundle contains code for a principal class, which typically serves as an application’s entry point into a bundle. You retrieve a bundle’s principal class with NSBundle’s `principalClass` method, which loads the bundle if it is not already loaded. This code fragment retrieves the principal class for the bundle located at `fullPath`:

```
NSString *fullPath; // Assume this exists.
NSBundle *bundle;
Class principalClass;

bundle = [NSBundle bundleWithPath:fullPath];
principalClass = [bundle principalClass];
```

You can also retrieve class objects by name with the `classNamed:` method. This code fragment retrieves the class KillerAppController from the bundle at `fullPath`:

```
NSString *fullPath; // Assume this exists.
NSBundle *bundle;
Class someClass;

bundle = [NSBundle bundleWithPath:fullPath];
someClass = [bundle classNamed:@"KillerAppController"];
```


Once you have retrieved the principal class from a loadable bundle, you typically create an instance of the class to use in your application. (If the class provides all its functionality through class methods, this step is not necessary.) To do this, you use a `Class` variable in the same way you would use any class name.

This code fragment retrieves the principal class of the bundle at `fullPath` and creates an instance of the principal class:

```
NSString *fullPath; // Assume this exists.
NSBundle *bundle;
Class principalClass;
id instance;

bundle = [NSBundle bundleWithPath:fullPath];
principalClass = [bundle principalClass];
instance = [[principalClass alloc] init];
```


In most applications, the five steps of bundle loading take place during the startup process as it searches for and loads plug-ins. [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tgljrgaydoojsfvbegskgineusqq) shows the implementation for a pair of methods that locate bundles, create NSBundle objects, load their code, and find and instantiate the principal class of each discovered bundle. An explanation follows the listing.

__Listing 1__  Method implementations for loading bundles from various locations

```objc
NSString *ext = @"bundle";
NSString *appSupportSubpath = @"Application Support/KillerApp/PlugIns";

// ...

- (void)loadAllBundles
{
    NSMutableArray *instances;                                         // 1
    NSMutableArray *bundlePaths;
    NSEnumerator *pathEnum;
    NSString *currPath;
    NSBundle *currBundle;
    Class currPrincipalClass;
    id currInstance;

    bundlePaths = [NSMutableArray array];
    if(!instances)
    {
        instances = [[NSMutableArray alloc] init];
    }

    [bundlePaths addObjectsFromArray:[self allBundles]];               // 2

    pathEnum = [bundlePaths objectEnumerator];
    while(currPath = [pathEnum nextObject])
    {
        currBundle = [NSBundle bundleWithPath:currPath];               // 3
        if(currBundle)
        {
            currPrincipalClass = [currBundle principalClass];          // 4
            if(currPrincipalClass)
            {
                currInstance = [[currPrincipalClass alloc] init];      // 5
                if(currInstance)
                {
                    [instances addObject:[currInstance autorelease]];
                }
            }
        }
    }
}

- (NSMutableArray *)allBundles
{
    NSArray *librarySearchPaths;
    NSEnumerator *searchPathEnum;
    NSString *currPath;
    NSMutableArray *bundleSearchPaths = [NSMutableArray array];
    NSMutableArray *allBundles = [NSMutableArray array];

    librarySearchPaths = NSSearchPathForDirectoriesInDomains(
        NSLibraryDirectory, NSAllDomainsMask - NSSystemDomainMask, YES);

    searchPathEnum = [librarySearchPaths objectEnumerator];
    while(currPath = [searchPathEnum nextObject])
    {
        [bundleSearchPaths addObject:
            [currPath stringByAppendingPathComponent:appSupportSubpath]];
    }
    [bundleSearchPaths addObject:
        [[NSBundle mainBundle] builtInPlugInsPath]];

    searchPathEnum = [bundleSearchPaths objectEnumerator];
    while(currPath = [searchPathEnum nextObject])
    {
        NSDirectoryEnumerator *bundleEnum;
        NSString *currBundlePath;
        bundleEnum = [[NSFileManager defaultManager]
            enumeratorAtPath:currPath];
        if(bundleEnum)
        {
            while(currBundlePath = [bundleEnum nextObject])
            {
                if([[currBundlePath pathExtension] isEqualToString:ext])
                {
                 [allBundles addObject:[currPath
                           stringByAppendingPathComponent:currBundlePath]];
                }
            }
        }
    }

    return allBundles;
}
```

Here’s how the code works:

1. The `instances` array contains all the objects instantiated from the principal classes of the discovered bundles. This object is shown in the method for clarity, but would typically be an instance variable of a controller class.
2. The `loadAllBundles` method calls the `allBundles` method to retrieve all files ending with the extension `.bundle`. The `allBundles` method just enumerates through all the standard paths for loadable bundles (in the application bundle and in the user, local, and network `Library` directories).
3. For each returned path, an NSBundle object is created. If the file with a `.bundle` extension was not in fact a valid bundle, NSBundle returns `nil` and the rest of the iteration is skipped.
4. This line retrieves the principal class of the current bundle. Calling `principalClass` implicitly loads the code first.
5. Finally, the method instantiates the principal class. As long as `init` does not return `nil`, the new instance is added to the `instances` array. If you are writing an application with a plug-in architecture (as opposed to an application with a few known loadable bundles), you should perform some kind of validation on the plug-ins before creating an instance of the principal class.

In some instances, you may need to load non-Cocoa bundles from within a Cocoa application. You use the CFBundle routines in Core Foundation to load non-Cocoa bundles: `CFBundleCreate` to create CFBundle objects; `CFBundleLoadExecutable` to load the bundle’s executable code; and `CFBundleGetFunctionPointerForName` to look up the address of a loaded routine. See the Core Foundation Programming Topic _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_ for more information about these methods and other methods provided by CFBundle.

To integrate the code more cleanly with your Cocoa application, you can write a wrapper class to encapsulate the data and function pointers looked up through CFBundle.

[Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tgljrgazdambqfvbecssijfdeoqq) shows the interface for a Cocoa wrapper class for a CFBundle and [Listing 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tgljrgazdanjqfvbecsskizcuiqi) shows its implementation. An explanation follows each listing.

__Listing 2__  Loading and using code from a non-Cocoa bundle

```objc
#import <CoreFoundation/CoreFoundation.h>

typedef long (*DoSomethingPtr)(long);                                  // 1
typedef void (*DoSomethingElsePtr)(void);

@interface MyBundleWrapper : NSObject
{
    DoSomethingPtr doSomething;                                        // 2
    DoSomethingElsePtr doSomethingElse;

    CFBundleRef cfBundle;                                              // 3
}

- (long)doSomething:(long)arg;                                         // 4
- (void)doSomethingElse;

@end
```

The interface contains four elements:

1. Type definitions for function pointers, one for each function in the bundle
2. Function pointer instance variables
3. A `CFBundleRef` instance variable
4. Objective-C methods to wrap the C functions

__Listing 3__  Loading and using code from a non-Cocoa bundle

```objc
#import "MyBundleWrapper.h"

@implementation MyBundleWrapper

- (id)init
{
    NSString *bundlePath;
    NSURL *bundleURL;

    self = [super init];

    bundlePath = [[[NSBundle mainBundle] builtInPlugInsPath]           // 1
                    stringByAppendingPathComponent:@"MyCFBundle.bundle"];
    bundleURL = [NSURL fileURLWithPath:bundlePath];
    cfBundle = CFBundleCreate(kCFAllocatorDefault, (CFURLRef)bundleURL);

    return self;
}

- (void)dealloc
{
    CFRelease(cfBundle);
}

- (long)doSomething:(long)arg
{
    if(!doSomething)                                                   // 2
    {
        doSomething = CFBundleGetFunctionPointerForName(cfBundle,
                                           CFSTR("DoSomething"));
    }
    return doSomething(arg);                                           // 3
}

- (void)doSomethingElse
{
    if(!doSomethingElse)                                               // 2
    {
        doSomethingElse = CFBundleGetFunctionPointerForName(cfBundle,
                                           CFSTR("DoSomethingElse"));
    }
    doSomethingElse();                                                 // 3
}

@end
```

Here’s what the implementation does:

1. Initializes the `cfBundle` instance variable with a URL to the bundle in the application’s plug-ins directory. The bundle can reside anywhere on disk; the plug-ins directory is just the typical location for built-in loadable bundles.
2. When the method is called, lazily initializes the function pointer associated with the method. The call to `CFBundleGetFunctionPointerForName` implicitly loads the bundle’s executable code before looking up the function pointer.
3. Returns the value returned by the loaded function.

[Next](Creating%20Loadable%20Bundles.md)[Previous](Plug-in%20Architectures.md)

