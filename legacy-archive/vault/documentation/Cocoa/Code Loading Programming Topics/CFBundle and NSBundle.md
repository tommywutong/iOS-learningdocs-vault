---
title: Code Loading Programming Topics
apple_id: 10000052i
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/Concepts/CFNSBundle.html
archived_at: '2026-07-15T07:16:26.298645Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Loading Programming Topics](Introduction%20to%20Dynamically%20Loading%20Code.md)


[Next](Multi-Bundle%20Applications.md)[Previous](Loadable%20Bundles%20in%20Cocoa.md)

# CFBundle and NSBundle

This concept describes the relationship between NSBundle, the Cocoa class for manipulating loadable bundles, and the Core Foundation CFBundle opaque type it is built upon. This material is important background for anyone planning to use loadable bundles in their application.

The Core Foundation CFBundle opaque type provides OS X’s base API for manipulating bundles. The CFBundle programming interface insulate developers from dealing directly with the specifics of things like executable format, resource-locating algorithms, and data extraction from the information property list.

The CFBundle opaque data type makes bundle resources and code available to your application. You initialize a CFBundle object with the location of a bundle and then access the bundle’s contents with the various CFBundle routines. The routines include support for

- dynamically loading and unloading executable code
- retrieving the location of localized and non-localized resources such as graphics, nib files, and character strings
- accessing localized and non-localized information property list values
- retrieving pointers to functions and data in the bundle executable

The dynamic loading routines handle all the details of interacting with the dynamic loaders for the supported executable formats so you don’t have to care about them. Loading and unloading code is a matter of initializing a CFBundle object for the desired bundle and using the functions `CFBundleLoadExecutable` and `CFBundleUnloadExecutable`.

In Cocoa applications, you should not use CFBundle routines to load and unload executable code, because CFBundle does not natively support the Objective-C runtime. NSBundle correctly loads Objective-C symbols into the runtime system, but there is no way to unload Cocoa bundles once loaded due to a runtime limitation. You can, however, create a CFBundle object for a Cocoa bundle and use the other CFBundle routines without trouble.

For detailed information about Core Foundation Bundles, including API reference, see the Core Foundation Programming Topic _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_.

NSBundle is the Cocoa class responsible for bundle management. Most of its methods invoke the corresponding CFBundle routines and are modeled after them. Note, however, that pointers to NSBundle objects cannot be cast to CFBundleRefs, unlike some other Core Foundation types and Foundation equivalents—they are _not_ toll-free bridged.

For most of its methods, NSBundle simply calls the appropriate CFBundle routine to do its work, but loading code is different. Because CFBundle does not handle Objective-C symbols, NSBundle has to use a different mechanism for loading code. NSBundle interacts with the Objective-C runtime system to correctly load and register all Cocoa classes and other executable code in the bundle executable file.

At the very least, Cocoa bundles contain a single class, the principal class, which serves as an entry point into a bundle. See [Loadable Bundles in Cocoa](Loadable%20Bundles%20in%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3dslkciffegskbjbaq) for a discussion of the principal class.

Because of a limitation in the Objective-C runtime system, NSBundle cannot unload executable code. Since CFBundle does not know about Objective-C symbols, do not use the CFBundle loading and unloading routines on NSBundle objects. You can, however, create a CFBundle object for a Cocoa bundle and use the other routines—unrelated to loading and unloading—without trouble.

[Next](Multi-Bundle%20Applications.md)[Previous](Loadable%20Bundles%20in%20Cocoa.md)

