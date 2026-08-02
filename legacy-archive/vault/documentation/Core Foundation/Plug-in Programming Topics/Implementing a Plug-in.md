---
title: Plug-in Programming Topics
apple_id: 10000128i
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2005-03-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPlugIns/Tasks/implementing.html
archived_at: '2026-07-15T07:22:41.476127Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Plug-in Programming Topics](Introduction%20to%20Plug-ins.md)


[Next](Loading%20and%20Using%20a%20Plug-in.md)[Previous](Defining%20Types%20and%20Interfaces.md)

# Implementing a Plug-in

This section details all of the steps necessary to actually implement a plug-in that supports the type declared in [Defining Types and Interfaces](Defining%20Types%20and%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dglkdjjbekscbifdq)

Now that we have a type and some interfaces, let's look at how a plug-in that supported this type would be implemented. First, consider the information property list for the plug-in in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3diljrgaydsobyfvbecssejbaukqq)

__Listing 1__  An Info.plist file for a plug-in

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDevelopmentRegion</key>
    <string>English</string>
    <key>CFBundleExecutable</key>
    <string>CFTestPlugin</string>
    <key>CFBundleIconFile</key>
    <string></string>
    <key>CFBundleIdentifier</key>
    <string>com.apple.yourcfbundle</string>
    <key>CFBundleInfoDictionaryVersion</key>
    <string>6.0</string>
    <key>CFBundlePackageType</key>
    <string>BNDL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFPlugInDynamicRegisterFunction</key>
    <string></string>
    <key>CFPlugInDynamicRegistration</key>
    <string>NO</string>
    <key>CFPlugInFactories</key>
    <dict>
        <key>68753A44-4D6F-1226-9C60-0050E4C00067</key>
        <string>MyFactoryFunction</string>
    </dict>
    <key>CFPlugInTypes</key>
    <dict>
        <key>D736950A-4D6E-1226-803A-0050E4C00067</key>
        <array>
            <string>68753A44-4D6F-1226-9C60-0050E4C00067</string>
        </array>
    </dict>
    <key>CFPlugInUnloadFunction</key>
    <string></string>
</dict>
</plist>
```

The information property list defines various aspects of the plug-in’s runtime behavior and contains optional static registration information for the various types the plug-in supports. For more information about static and dynamic registration, see [Plug-in Registration](Plug-in%20Registration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dclkdjjbeksscjbea)

In this example, the `CFBundleExecutable` key tells CFBundle the name of the executable and is used by the primitive code-loading API of bundles. The rest of the keys are specific to the plug-in model.

The `CFPlugInDynamicRegistration` key indicates whether this plug-in requires dynamic registration. In this example, static registration is used, so the dynamic registration key is set to `NO`.

The `CFPlugInFactories` key is used to statically register factory functions, and the `CFPlugInTypes` key is used to statically register the factories that can create each supported type.

When implementing a plug-in, you must provide

- the implementation for any factory functions registered for the plug-in
- implementations for all the functions in all the interfaces for any types supported by your plug-in
- an interface function table for each interface you implement
- the required COM functions, `QueryInterface`, `AddRef` and `Release`

[Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3diljrgaytcmzyfvbecssjifbeira) contains the code for a plug-in that implements the type `kTestTypeID` and its interface.

__Listing 2__  Example plug-in implementation

```c
 #include <CoreFoundation/CoreFoundation.h>
 #include "TestInterface.h"

// The UUID for the factory function.
#define kTestFactoryID (CFUUIDGetConstantUUIDWithBytes(NULL,
 0x68, 0x75, 0x3A, 0x44, 0x4D, 0x6F, 0x12, 0x26, 0x9C, 0x60,
0x00, 0x50, 0xE4, 0xC0, 0x00, 0x67))

// The layout for an instance of MyType.
typedef struct _MyType {
    TestInterfaceStruct *_testInterface;
    CFUUIDRef _factoryID;
    UInt32 _refCount;
 } MyType;

// Forward declaration for the IUnknown implementation.
static void _deallocMyType( MyType *this );

// Implementation of the IUnknown QueryInterface function.
static HRESULT myQueryInterface( void *this, REFIID iid, LPVOID *ppv )
{
    // Create a CoreFoundation UUIDRef for the requested interface.
    CFUUIDRef interfaceID = CFUUIDCreateFromUUIDBytes( NULL, iid );

    // Test the requested ID against the valid interfaces.
    if (CFEqual(interfaceID, kTestInterfaceID))
    {
        // If the TestInterface was requested, bump the ref count,
        // set the ppv parameter equal to the instance, and
        // return good status.
        ((MyType *)this)->_testInterface->AddRef( this );
        *ppv = this;
        CFRelease(interfaceID);
        return S_OK;
    }

    if (CFEqual(interfaceID, IUnknownUUID))
    {
        // If the IUnknown interface was requested, same as above.
        ((MyType *)this)->_testInterface->AddRef( this );
        *ppv = this;
        CFRelease( interfaceID );
        return S_OK;
    }

    // Requested interface unknown, bail with error.
    *ppv = NULL;
    CFRelease( interfaceID );
    return E_NOINTERFACE;
}

// Implementation of reference counting for this type.
// Whenever an interface is requested, bump the refCount for
// the instance. NOTE: returning the refcount is a convention
// but is not required so don’t rely on it.
static ULONG myAddRef( void *this )
{
    ((MyType *)this)->_refCount += 1;
    return ((MyType *)this)->_refCount;
}

// When an interface is released, decrement the refCount.
// If the refCount goes to zero, deallocate the instance.
static ULONG myRelease( void *this )
{
    ((MyType *)this)->_refCount -= 1;
    if (((MyType *)this)->_refCount == 0)
    {
        _deallocMyType( (MyType *)this );
        return 0;
    }
    return ((MyType *)this)->_refCount;
}

// The implementation of the TestInterface function.
static void myFooMe( void *this, Boolean flag )
{
    printf("myFooMe: instance 0x%x: I've been fooed.  %s\n",
            (unsigned)this, (flag ? "YES" : "NOPE"));
}

// The TestInterface function table.
static TestInterfaceStruct testInterfaceFtbl =
{
        NULL,               // Required padding for COM
        myQueryInterface,   // These three are the required COM functions
        myAddRef,
        myRelease,
        myFooMe
}; // Interface implementation

// Utility function that allocates a new instance.
static MyType *_allocMyType( CFUUIDRef factoryID )
{
    // Allocate memory for the new instance.
    MyType *newOne = (MyType *)malloc( sizeof(MyType) );

    // Point to the function table
    newOne->_testInterface = &testInterfaceFtbl;

    // Retain and keep an open instance refcount
    // for each factory.
    newOne->_factoryID = CFRetain( factoryID );
    CFPlugInAddInstanceForFactory( factoryID );

    // This function returns the IUnknown interface
    // so set the refCount to one.
    newOne->_refCount = 1;
    return newOne;
}

// Utility function that deallocates the instance
// when the refCount goes to zero.
static void _deallocMyType( MyType *this )
{
    CFUUIDRef factoryID = this->_factoryID;
    free(this);
    if (factoryID)
    {
        CFPlugInRemoveInstanceForFactory( factoryID );
        CFRelease( factoryID );
    }
}

// Implementation of the factory function for this type.
void *MyFactory(CFAllocatorRef allocator, CFUUIDRef typeID)
{
    // If correct type is being requested, allocate an
    // instance of TestType and return the IUnknown interface.
    if (CFEqual(typeID, kTestTypeID))
    {
        MyType *result = _allocMyType( kTestFactoryID );
        return result;
    }
    // If the requested type is incorrect, return NULL.
    return NULL;
}
```

As illustrated in [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3diljrgaytcmzyfvbecssjifbeira) the first step in implementing a plug-in is to define the UUID for the factory you are going to supply. This is the same UUID that was used in the `CFPlugInFactories` key in the information property list. Next, the data structure for instances of the `TestType` implementation is defined.

After defining the instance structure, you implement the IUnknown interface functions required for every plug-in. In this example, `QueryInterface`, relies on the fact that the first pointer in the instance structure is an interface, so returning a pointer to the `MyType` structure is the same as returning a pointer to a pointer to `TestInterface`. Types that implement more than one interface would be more complicated. In C++, this can be accomplished using multiple inheritance and static casting. In C, you would have to keep track of the interface pointers by hand.

After the IUnknown functions, there is the implementation for the `fooMe` function from `TestInterface`. In this example it just prints a message. Next comes the static definition of the actual `TestInterface` function table. This table is filled in with the IUnknown and `TestInterface` functions.

Following the function table are two utility functions that allow easy creation and freeing of `MyType` structures. The allocator fills in the pointer to the interface function table and sets the initial reference count to 1. It also takes care of registering the instance with the factory so plug-ins knows not to unload the plug-in’s code while there are still instances active. The deallocator function frees the memory for `MyType` and unregisters the instance from the factory.

Finally, there is the actual factory function that creates a new instance and returns a pointer to it. This pointer is also a pointer to the IUnknown interface. The `MyFactory` function must conform to the `CFPlugInFactoryFunction` prototype. Factory functions take allocators and type UUIDs as parameters.

[Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3diljrgaytcmzyfvbecssjifbeira) contains a lot of glue code that would be unnecessary for C++ developers using a compiler with built-in support for generating COM interface layouts. If you wish to implement CFPlugIns in C++, refer to the wealth of COM documentation by Microsoft and others.

[Next](Loading%20and%20Using%20a%20Plug-in.md)[Previous](Defining%20Types%20and%20Interfaces.md)

