---
title: Extending Printing Dialogs
apple_id: TP30000979
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/Printing/Conceptual/ExtPrintingDialogs/PMPlugIn/PMPlugIn.html
archived_at: '2026-07-18T01:51:53.672993Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Extending Printing Dialogs](Introduction%20to%20Extending%20Printing%20Dialogs.md)


[Next](Document%20Revision%20History.md)[Previous](Utility%20Functions.md)

# Printing Plug-in Header Functions

All printing plug-ins—including printing dialog extensions—must implement the three functions defined in the `PMPluginHeader` interface. These functions perform reference counting and provide version information for the larger `PlugInIntfVTable` interface.

This appendix explains how to perform these tasks. You should be able to use this sample code in a real-world project with little or no modification.

Listing B-1 implements a function that retains (increments the reference count of) an instance of the `PlugInIntfVTable` interface.

__Listing B-1__  A retain function for the `PlugInIntfVTable` interface

```swift
static OSStatus MyPMPluginRetain (PMPlugInHeaderInterface* this)
{
    MyPDEInstance* instance = (MyPDEInstance*) this;// 1
    OSStatus result = noErr;

    if (instance != NULL) {
        ++instance->refCount;// 2
    }

    return result;
}
```

Here’s what the code in Listing B-1 does:

1. Defines a pointer to an instance of the `PlugInIntfVTable` interface. This is the same instance the query interface function supplied.
2. Increments the reference count for this instance.

Listing B-2 implements a function that releases (decrements the reference count of) an instance of the `PlugInIntfVTable` interface, and frees the instance if the reference count reaches zero.

__Listing B-2__  A release function for the `PlugInIntfVTable` interface

```swift
static OSStatus MyPMRelease (
    PMPlugInHeaderInterface** this
)

{
    MyPDEInstance* instance = (MyPDEInstance*) *this;
    ULONG refCount = 0;
    OSStatus result = noErr;

    *this = NULL;

    if(instance != NULL)
    {
        refCount = --instance->refCount;

        if (refCount == 0)
        {
            free (instance);
            MyFreeBundle();
            MyFreeTitle();
        }
    }

    return result;
}
```

Here’s what the code in Listing B-2 does:

1. Defines a pointer to an instance of the `PlugInIntfVTable` interface. This is the same instance the query interface function supplied.
2. Defines a variable for the updated reference count, and sets its default value to 0.
3. Clears the caller's instance pointer.
4. Decrements the reference count for this instance.
5. If the reference count is zero, deallocates storage for the instance.
6. Releases our bundle reference, in case the plug-in is being unloaded. For more information about `MyFreeBundle`, see the comments in the sample project that accompanies this book.

Listing B-3 implements a function that supplies API version information to the printing system.

__Listing B-3__  An API version function for the `PlugInIntfVTable` interface

```swift
static OSStatus MyPMPluginGetAPIVersion (
    PMPlugInHeaderInterface *this,
    PMPlugInAPIVersion *versionPtr// 1
)

{
    OSStatus result = noErr;

    versionPtr->buildVersionMajor = kPDEBuildVersionMajor;// 2
    versionPtr->buildVersionMinor = kPDEBuildVersionMinor;
    versionPtr->baseVersionMajor = kPDEBaseVersionMajor;
    versionPtr->baseVersionMinor = kPDEBaseVersionMinor;

    return result;
}
```

Here’s what the code in Listing B-3 does:

1. Receives the address of a structure that the caller uses for version control information.
2. Assigns four constant values to fields in the structure. The constants are defined in `PMPrintingDialogExtensions.h` for use in this function.

[Next](Document%20Revision%20History.md)[Previous](Utility%20Functions.md)

