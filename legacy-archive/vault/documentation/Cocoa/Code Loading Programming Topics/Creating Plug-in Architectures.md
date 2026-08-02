---
title: Code Loading Programming Topics
apple_id: 10000052i
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/Tasks/UsingPlugins.html
archived_at: '2026-07-15T07:16:32.239753Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Loading Programming Topics](Introduction%20to%20Dynamically%20Loading%20Code.md)


[Next](Preventing%20Name%20Conflicts.md)[Previous](Building%20Applications%20with%20Multiple%20Bundles.md)

# Creating Plug-in Architectures

Many applications benefit from having a plug-in architecture—a way to extend the application with new features without changing the main application code. This section describes how to create a plug-in architecture for a Cocoa application.

The first step in implementing a plug-in architecture is deciding what form you want plug-ins to take. For guidelines on how to decide which mechanism you want to use, read [Plug-in Architecture Design](Plug-in%20Architectures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3teljzha3tsna).

The Cocoa architecture naturally supports three choices:

- Plug-ins implement a formal protocol
- Plug-ins implement some number of methods from an informal protocol
- Plug-ins inherit from an abstract or concrete base class

In all three cases, you provide a standard interface to plug-in developers, and they write plug-in principal classes to match the interface. The most convenient way to do this is to provide the interface as a framework for plug-in developers to link against.

The following sections describe how to publish the three different types of plug-in interfaces.

To use a plug-in protocol you define, the plug-in developer only needs the header file containing the protocol definition. The easiest way to publish the interface is to simply distribute this header.

A protocol header for a graphics filter plug-in might look something like Listing 1:

__Listing 1__  Formal protocol for a plug-in architecture

```objc
/*
   MyGreatImageApp
   Graphics Filter Interface version 0
   MyAppBitmapGraphicsFiltering.h
*/

#import <Cocoa/Cocoa.h>

@protocol MyGreatImageAppBitmapGraphicsFiltering

// Returns the version of the interface you're implementing.
// Return 0 here or future versions may look for features you don't have!
- (unsigned)interfaceVersion;

// Returns what to display in the Filter menu.
- (NSString *)menuItemString;

// The main worker bee: filters the bitmap and returns a modified version.
- (NSBitmapImageRep *)filteredImageRep:(NSBitmapImageRep *)imageRep;

// Returns the window controller for the settings configuration window.
- (NSWindowController *)configurationWindowController;

@end
```

Notice that this example includes a version method so the application can identify the version of the interface being used. If you are just distributing a header file, this is the best way to ensure that future versions of your application avoid sending messages to old plug-ins that they can’t handle. You can also query the plug-in for what messages it responds to, as described in [Validating Plug-ins](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tmljrgazdsmbz).

Using an informal protocol for a plug-in architecture is somewhat trickier than using a formal protocol. Because the plug-in developer can choose which methods to implement, your application has to check before using a method if the plug-in actually implements it. If some methods are optional and some are required, be sure to make this clear in the documentation for the interface.

You can distribute a single header file to define an informal protocol, just as with a formal protocol. Listing 2 is an alternate implementation of [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tmljrgaydemzufvbuuqskinbucra), using an informal protocol instead of a formal protocol, effectively making some methods optional. Like most informal protocols, this one is implemented as a category on NSObject.

__Listing 2__  Informal protocol for a plug-in architecture

```objc
/*
   MyGreatImageApp
   Graphics Filter Interface version 0
   MyAppBitmapGraphicsFiltering.h
*/

#import <Cocoa/Cocoa.h>

@interface NSObject(MyGreatImageAppBitmapGraphicsFiltering)

// REQUIRED
// Returns the version of the interface you're implementing.
// Return 0 here or future versions may look for features you don't have!
- (unsigned)interfaceVersion;

// OPTIONAL
// Returns what to display in the Filter menu. Defaults to the plug-in
// filename without the extension.
- (NSString *)menuItemString;

// REQUIRED
// The main worker bee: filters the bitmap and returns a modified version.
- (NSBitmapImageRep *)filteredImageRep:(NSBitmapImageRep *)imageRep;

// OPTIONAL
// Returns the window controller for the settings configuration window.
// If this method is not implemented, no Settings option is provided.
- (NSWindowController *)configurationWindowController;

@end
```


If you want to provide shared functionality to all plug-ins, you may want to provide a base class for plug-in principal classes to inherit from. For example, the OS X screen saver interface is provided as a framework containing the ScreenSaverView base class, which handles a number of management details for screen saver plug-ins. To distribute your base class, the best solution is to package it as a framework for plug-in developers to link against.

Listing 3 shows the interface for a hypothetical embedding plug-in architecture, and [Listing 4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tmljrgaydkojtfvbuuqscijauura) shows its implementation. Instead of a protocol, the interface is provided as a base class that provides some functionality, in this example a fairly simple subclass of NSView that returns version information, maintains a URL containing a data source, and draws a white background. Note that the class contains three reserved pointers. These allow the base class to add new member data without changing the size of the object, thus allowing the host application developer to add features without creating binary incompatibilities.

__Listing 3__  Base class interface for a plug-in architecture

```objc
#import <Cocoa/Cocoa.h>

@interface MyAppEmbeddingView : NSView
{
@private
    NSURL *_URL;
    void *_reserved1;
    void *_reserved2;
    void *_reserved3;
}

- (id)initWithFrame:(NSRect)frameRect URL:(NSURL)URL;
- (unsigned)interfaceVersion;
- (NSURL *)URL;
- (void)setURL:(NSURL *)URL;

@end
```


__Listing 4__  Base class implementation for a plug-in architecture

```objc
#import "MyAppEmbeddingView.h"

@implementation MyAppEmbeddingView

- (id)initWithFrame:(NSRect)frameRect URL:(NSURL)URL
{
    self = [self initWithFrame:frameRect];
    [self setURL:URL];
    return self
}

- (unsigned)interfaceVersion
{
    return 0;
}

- (void)drawRect:(NSRect)rect
{
    NSEraseRect(rect);
}

- (NSURL *)URL
{
    return _URL;
}

- (void)setURL:(NSURL *)URL
{
    [URL retain];
    [_URL release];
    _URL = URL;
}

@end
```

Once you have finished your base class, you should package the compiled implementation with the header file in a framework for plug-in developers to use. To build a framework, use Xcode’s Cocoa Framework project template. Make sure you designate private and public header files as you intend in the Build Phases > Headers section of the Target Settings pane. For more information about building frameworks, see “Creating Frameworks and Libraries” in Xcode Help.

To use plug-ins, your application needs to go through this process:

1. Find available plug-ins in standard locations
2. Load the executable code for each plug-in
3. Validate conformance of each plug-in to the plug-in interface
4. Instantiate valid plug-ins

The specific details of finding, loading, and instantiating plug-ins are the same as described in [Loading Cocoa Bundles with NSBundle](Loading%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tgljzhe2dqoa). The additional step for plug-in architectures is to validate that each plug-in conforms to the interface you published for plug-in developers to use.

Validation is slightly different depending on whether your plug-in architecture uses a formal protocol, an informal protocol, or a base class.

For a formal protocol, you query the class to see if it implements the protocol. To be safe, you should also perform a reality check to see that it indeed implements the methods it claims to implement. [Listing 5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tmljrgazdsnbyfvbuuqshifduiri) shows the implementation for a method that checks if a plug-in’s principal class conforms to the `MyGreatImageAppBitmapFiltering` protocol defined in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tmljrgaydemzufvbuuqskinbucra), and additionally checks to make sure that it implements all the necessary instance methods.

__Listing 5__  Plug-in validation (formal protocol)

```objc
- (BOOL)plugInClassIsValid:(Class)plugInClass
{
    if([plugInClass
        conformsToProtocol:@protocol(MyGreatImageAppBitmapFiltering)])
    {
        if([plugInClass instancesRespondToSelector:
                        @selector(interfaceVersion)] &&
           [plugInClass instancesRespondToSelector:
                        @selector(menuItemString)] &&
           [plugInClass instancesRespondToSelector:
                        @selector(filteredImageRep)] &&
           [plugInClass instancesRespondToSelector:
                        @selector(configurationWindowController])
        {
            return YES;
        }
    }

    return NO;
}
```

For an informal protocol, you _must_ query the class to see which methods it implements. Typically, host application developers define certain methods as required, and others as optional, so a validation method should distinguish between the two properly. [Listing 6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tmljrgaztaojxfvbuuqsgircukrq) gives the implementation for an informal version of the plug-in validation method. The method makes sure that the plug-in implements all the required methods from the informal version of `MyGreatImageAppBitmapFiltering` given in [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tmljrgaydanrtfvbuuqsfi5duqra). You can check for optional methods as they are needed elsewhere in the application.

__Listing 6__  Plug-in validation (informal protocol)

```objc
- (BOOL)plugInClassIsValid:(Class)plugInClass
{
    if([plugInClass instancesRespondToSelector:
                    @selector(interfaceVersion)] &&
       [plugInClass instancesRespondToSelector:
                    @selector(filteredImageRep)])
    {
        return YES;
    }

    return NO;
}
```

A plug-in that inherits from a base class is the easiest to validate. You simply query the plug-in’s principal class to see if it is a subclass of the base class, as shown in [Listing 7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tmljrgaztcojrfvbuuqsgjbbegsa).

__Listing 7__  Plug-in validation (base class)

```objc
- (BOOL)plugInClassIsValid:(Class)plugInClass
{
    if([plugInClass isSubclassOfClass:[MyAppEmbeddingView class]])
    {
        return YES;
    }

    return NO;
}
```


[Listing 8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tmljrgazteobtfvbuuqsiinbeksq) is a slightly modified version of [Listing 1](Loading%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tgljrgaydoojsfvbegskgineusqq) that validates plug-ins before adding them, indicated by the margin comment `// Validation`. For a full description of how the code works, see the original version.

__Listing 8__  Implementation for plug-in loading methods

```objc
NSString *ext = @"plugin";
NSString *appSupportSubpath = @"Application Support/KillerApp/PlugIns";

// ...

- (void)loadAllPlugins
{
    NSMutableArray *instances;
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

    [bundlePaths addObjectsFromArray:[self allBundles]];

    pathEnum = [bundlePaths objectEnumerator];
    while(currPath = [pathEnum nextObject])
    {
        currBundle = [NSBundle bundleWithPath:currPath];
        if(currBundle)
        {
            currPrincipalClass = [currBundle principalClass];
            if(currPrincipalClass &&
               [self plugInClassIsValid:currPrincipalClass])  // Validation
            {
                currInstance = [[currPrincipalClass alloc] init];
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

[Next](Preventing%20Name%20Conflicts.md)[Previous](Building%20Applications%20with%20Multiple%20Bundles.md)

