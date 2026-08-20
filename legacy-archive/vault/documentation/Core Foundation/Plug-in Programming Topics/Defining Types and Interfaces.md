---
title: Plug-in Programming Topics
apple_id: 10000128i
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2005-03-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPlugIns/Tasks/defining.html
archived_at: '2026-07-15T07:22:40.901309Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Plug-in Programming Topics](Introduction%20to%20Plug-ins.md)


[Next](Implementing%20a%20Plug-in.md)[Previous](Plug-in%20Registration.md)

# Defining Types and Interfaces

Your first task as a plug-in host developer is to define the types and interfaces the host supports.

To define a type, all you really need is a UUID. To create a UUID for a plug-in you typically use the command line utility `uuidgen`. If you need to generate UUIDs programmatically you can do so using the functions defined in `CFUUID.h` (see [Generating a UUID Programmatically](Generating%20a%20UUID%20Programmatically.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dmlkdjjbekscbifdq)). In the case of types and factories, you need the UUID in two forms, the hexadecimal representation for the header file, and the ASCII representation for the information property list. The standard format for UUIDs represented in ASCII is a string punctuated by hyphens, for example: `D736950A-4D6E-1226-803A-0050E4C00067`. The hex representation looks, as you might expect, like a list of numerical values preceded by `0x`. For example, `0xD7, 0x36, 0x95, 0x0A, 0x4D, 0x6E, 0x12, 0x26, 0x80, 0x3A, 0x00, 0x50, 0xE4, 0xC0, 0x00, 0x67`.

In addition to its UUID, an important bit of information about a type is what interfaces the type is expected to implement and which—if any—are optional. This information is not needed at runtime and is not expressed as code in the header, but should be expressed as a comment, just to be clear.

To define an interface you need a UUID for the interface and a structure for the function table for that interface. This means you have to define the function pointers and expected behavior for each function in the interface.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dgljrgaytambtfvbecsshifaumrq) shows the contents of a header file that declares a type and the interface used to implement the type. This header is typically created by the plug-in host developer and made available to plug-in writers.

__Listing 1__  Defining a type and interface

```c
#include <CoreFoundation/CoreFoundation.h>

// Define the UUID for the type.
#define kTestTypeID (CFUUIDGetConstantUUIDWithBytes(NULL, 0xD7, 0x36, 0x95, 0x0A,
0x4D, 0x6E, 0x12, 0x26, 0x80, 0x3A, 0x00, 0x50, 0xE4, 0xC0, 0x00, 0x67))

// Define the UUID for the interface.
// TestType objects must implement TestInterface.
#define kTestInterfaceID (CFUUIDGetConstantUUIDWithBytes(NULL, 0x67, 0x66, 0xE9,
0x4A, 0x4D, 0x6F, 0x12, 0x26, 0x9E, 0x9D, 0x00, 0x50, 0xE4, 0xC0, 0x00, 0x67))

// The function table for the interface.
typedef struct TestInterfaceStruct
{
    IUNKNOWN_C_GUTS;
    void (*fooMe)( void *this, Boolean flag );
} TestInterfaceStruct;
```

Notice that the structure that defines the interface’s function table includes `IUNKNOWN_C_GUTS` as its first element. This macro—shown in [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dgljrgaytcmrtfvbeeq2giveuurq)—expands into the structure definition for the COM IUnknown interface. The COM specification requires that all interfaces inherit from IUnknown. Practically speaking, this means every interface function table must begin with three functions—`QueryInterface`, `AddRef`, and `Release`. This also means that any interface can be treated polymorphically as an IUnknown interface. At runtime, the host uses `QueryInterface` to find and gain access to all other interfaces the type supports. `AddRef` and `Release` are used for reference counting.

__Listing 2__  The IUnknown interface in C

```
#define IUNKNOWN_C_GUTS \
 void *_reserved; \
 HRESULT (STDMETHODCALLTYPE *QueryInterface) \
            (void *thisPointer, REFIID iid, LPVOID *ppv); \
 ULONG (STDMETHODCALLTYPE *AddRef)(void *thisPointer); \
 ULONG (STDMETHODCALLTYPE *Release)(void *thisPointer)
```

In C++ , using a compiler that supports COM, this would be accomplished by deriving your interface class from the IUnknown class. [Listing 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dgljrgaytcobqfvbecssjinceeqi) shows what the IUnknown interface would look like in C++.

__Listing 3__  The IUnknown interface in C++

```
interface IUnknown
{
    virtual HRESULT __stdcall QueryInterface(const IID& iid
                                    void **ppv) = 0;
    virtual ULONG __stdcall AddRef() = 0;
    virtual ULONG __stdcall Release() = 0;
}
```

Finally, notice that the function `fooMe` in `TestInterfaceStruct` takes a `this` argument as its first parameter. This is not required, but it is a nice thing to do to assist plug-in writers. By passing a `this` pointer to each interface function, you allow the plug-in writer to implement in C++ and to have access to the plug-in object when the function executes in any language.

[Next](Implementing%20a%20Plug-in.md)[Previous](Plug-in%20Registration.md)

