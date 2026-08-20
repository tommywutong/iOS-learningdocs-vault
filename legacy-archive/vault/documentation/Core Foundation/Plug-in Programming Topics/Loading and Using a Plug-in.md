---
title: Plug-in Programming Topics
apple_id: 10000128i
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2005-03-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPlugIns/Tasks/loading.html
archived_at: '2026-07-15T07:22:42.156926Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Plug-in Programming Topics](Introduction%20to%20Plug-ins.md)


[Next](Generating%20a%20UUID%20Programmatically.md)[Previous](Implementing%20a%20Plug-in.md)

# Loading and Using a Plug-in

The code example in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dkljrga4temjsfvbecssdiraumry) shows how a plug-in host can load and use a plug-in. It searches registered plug-ins for one that implements a test interface. If found, it invokes functions using the interface.

- `CFPlugInFindFactoriesForPlugInType` searches all the registered plug-ins and returns an array of all factories that can create the requested type.
- For each factory, `CFPlugInInstanceCreate` creates an instance of the test type and obtains a pointer to its `IUnknown` interface, if that exists.
- The `IUnknown` interface is tested to determine if it is the test interface. If it is, one of its functions is invoked and a flag is set to stop the search.

__Listing 1__  Loading and using a plug-in

```swift
Boolean foundInterface = false;

// Create a URL that points to the plug-in using a CFString path 'aPath'.
CFURLRef url =
    CFURLCreateWithFileSystemPath(NULL, aPath, kCFURLPOSIXPathStyle, TRUE);

// Create a CFPlugin using the URL.
// This causes the plug-in's types and factories to be registered with the system.
// The plug-in's code is not loaded unless it is using dynamic registration.
CFPlugInRef plugin = CFPlugInCreate(NULL, url);

if (!plugin)
{
    printf("Could not create CFPluginRef.\n");
}
else
{
    // Test whether this plug-in implements the Test type.
    CFArrayRef factories = CFPlugInFindFactoriesForPlugInType(kTestTypeID);

    // If there are factories for the requested type, attempt to
    // get the IUnknown interface.
    if (factories != NULL)
    {
        CFIndex factoryCount = CFArrayGetCount(factories);

        if (factoryCount <= 0)
        {
            printf("Could not find any factories.\n");
        }
        else
        {
            CFIndex index;

            for (index = 0;
                (index < factoryCount) && (!foundInterface);
                index++)
            {
                // Get the factory ID at the current index.
                CFUUIDRef factoryID =
                            CFArrayGetValueAtIndex(factories, index);
                // Use the factory ID to get an IUnknown interface.
                // The code for the PlugIn is loaded here.
                IUnknownVTbl **iunknown =
                    CFPlugInInstanceCreate(NULL, factoryID, kTestTypeID);
                // If this is an IUnknown interface,
                // query for the Test interface.
                if (iunknown)
                {
                    TestInterfaceStruct **interface = NULL;
                    (*iunknown)->QueryInterface(iunknown,
                                CFUUIDGetUUIDBytes(kTestInterfaceID),
                                (LPVOID *)(&interface));
                    // Finished with IUnknown.
                    (*iunknown)->Release(iunknown);

                    // If this is a Test interface, try to call its function.
                    if (interface)
                    {
                        (*interface)->fooMe(interface, TRUE);
                        (*interface)->fooMe(interface, FALSE);
                        // Finished with test interface.
                        // This causes the plug-in's code to be unloaded.
                        (*interface)->Release(interface);

                        foundInterface = true;
                    }
                }
                // end of iunknown
            }
            // end of index loop
        }
        // factoryCount > 0

        // Release the factories array.
        CFRelease(factories);
    }
    if (!foundInterface)
    {
        printf("Failed to get interface.\n");
    }
    // Release the CFPlugin -- memory for the plug-in is deallocated here.
    CFRelease(plugin);
}
```

[Next](Generating%20a%20UUID%20Programmatically.md)[Previous](Implementing%20a%20Plug-in.md)

