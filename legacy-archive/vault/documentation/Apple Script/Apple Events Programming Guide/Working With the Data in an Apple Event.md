---
title: Apple Events Programming Guide
apple_id: TP40001449
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/data_in_ae_aepg/data_in_ae_aepg.html
archived_at: '2026-07-15T05:19:29.232787Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Events Programming Guide](Introduction%20to%20Apple%20Events%20Programming%20Guide.md)


[Next](Responding%20to%20Apple%20Events.md)[Previous](Apple%20Event%20Dispatching.md)

# Working With the Data in an Apple Event

This chapter describes how your application gets various kinds of data from Apple events and the data structures that comprise them.

Your application responds to Apple events in the Apple event handlers it registers, or in routines your handlers call. Within a handler, you know that the passed Apple event matches the expected event class and event ID, although there can be some variation if the handler is registered with one or more wildcards. In either case, your handler has at least a general idea of what information the Apple event should contain. In the case of a wildcard handler, it can obtain information from the Apple event to identify the type more closely.

The parameters and attributes of an Apple event, as well as the data within an individual descriptor, are stored in a format that is opaque to your application. You use Apple Event Manager functions to extract the data you need from a received Apple event. To obtain data in a format your application can use, you typically follow a common series of steps:

1. You call a function that returns the descriptor for a high-level data structure you are interested in, such as an Apple event attribute or parameter. For example, you can call the `AEGetAttributeDesc` function to obtain the descriptor for an attribute, specifying the attribute by its keyword.
2. If the returned descriptor is a list, you use another function to iterate over the items in the list. For example, you can use `AEGetNthDesc` to get descriptors from a list by index.
3. Once you have obtained an individual descriptor, you use other functions to extract its data. For example, you can call `AEGetDescDataSize` to determine the size of the data in a descriptor and `AEGetDescData` to get the data.

Many of the functions for getting data from an Apple event are available in two forms:

- One that returns a copy of the descriptor for the data.
- One that returns a copy of the data in a buffer you have supplied.

For example, `AEGetParamDesc` returns a copy of the descriptor for a parameter, while `AEGetParamPtr` returns the data from an Apple event parameter in a specified buffer. You typically use the buffer form to extract data of fixed length or known maximum length, such as a result code. You use the descriptor form to extract data of variable length, such as a list of unknown length.

You can also use Apple Event Manager functions to get data from descriptors, descriptor lists, and Apple events. For example, you can use the `AESizeOfAttribute` function to get the size and descriptor type of an Apple event attribute from an Apple event. And you can use the `AESizeOfParam` function to get the size and descriptor type of an Apple event parameter from an Apple event or an Apple event record (type `AERecord`).

Where performance is critical, you can use `AECreateDescFromExternalPtr` to efficiently create a descriptor containing large amounts of data, and call `AEGetDescDataRange` to efficiently get data from a descriptor.

Other functions allow you to count the number of items in a descriptor list (`AECountItems`) or iterate through those descriptors (`AEGetNthPtr`or `AEGetNthDesc`).

This chapter provides examples of how to work with some of these functions, while [Functions for Working With Apple Event Data Structures](Selected%20Apple%20Event%20Manager%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgewugscei5deersg) lists these and other Apple Event Manager functions. For complete reference, see _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_.

_Coercion_ is the process of converting a descriptor and, if necessary, the data it contains, from one type to another. When your handler receives an Apple event, you typically use one or more of the functions `AEGetParamPtr`, `AEGetAttributePtr`, `AEGetParamDesc`, `AEGetAttributeDesc`, `AEGetNthPtr`, and `AEGetNthDesc` to get data from the Apple event. Each of these Apple Event Manager functions allows your application to specify a desired descriptor type for the resulting data. If the original data is of a different type, the Apple Event Manager attempts to coerce the data to the requested descriptor type. To prevent coercion and ensure that the descriptor type of the result is of the same type as the original, you specify `typeWildCard`for the desired type.

The following code snippet shows how to specify a desired descriptor type when calling the function `AEGetParamPtr`.

__Listing 4-1__  Getting and coercing an Apple event parameter

```
    DescType        returnedType;
    long            multResult;
    Size            actualSize;
    OSErr           err;

    err = AEGetParamPtr(
            theAppleEvent,// 1
            keyMultResult,// 2
            typeSInt32,// 3
            &returnedType,// 4
            &multResult,// 5
            sizeof(multResult),// 6
            &actualSize);// 7
```

Here’s a description of the parameters used in this call:

1. A pointer to the Apple event to get the parameter data from.
2. A keyword constant specifying the parameter to get the data from. In this example, the keyword is defined by the application and indicates a parameter containing the result of a multiplication operation.
3. A constant specifying the type to coerce the returned value to (if it isn’t already that type).
4. The address of a variable in which the function stores the actual type of the returned value, which may not match the requested type.
5. The address of a variable in which the function stores the returned data.
6. The maximum size of the returned data. The `AEGetParamPtr` function won’t return more data than you specify in this parameter.
7. The address of a variable in which the function stores the actual size of the requested data. If the returned value is greater than the amount your application allocated to store the returned data, you can increase the size of your buffer to this amount and call the function again. You can also choose to use the `AEGetParamDesc` function when your application doesn’t know the size of the data.

If the coercion fails, the `AEGetParamPtr` function returns the result code `errAECoercionFail`.

By default, the Apple Event Manager can coerce between many different data types, listed in [Table C-2](Default%20Coercion%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgmwvgvzr). To perform other coercions, such as those involving data types you have defined, you can provide your own coercion handlers. See [Writing and Installing Coercion Handlers](Writing%20and%20Installing%20Coercion%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhawueqkcirauur2c) for more information on working with coercion handlers.

Apple event parameters are keyword-specified descriptors. You can use the `AEGetParamDesc` function to get the descriptor for a parameter or to extract the descriptor list from a parameter; you can use `AEGetParamPtr` to get the data from the descriptor for a parameter. In general, use the former to extract data of variable length, and the latter to extract data of fixed length or known maximum length.

Listing 4-2 shows how to call `AEGetParamDesc` to extract a parameter descriptor from an Apple event such as an `open documents` event.

__Listing 4-2__  Getting a parameter as a descriptor

```
    AEDescList  docList;
    OSErr       myErr;

    myErr = AEGetParamDesc( theAppleEvent,// 1
                            keyDirectObject,// 2
                            typeAEList,// 3
                            &docList);// 4

    // Check the returned value from AEGetParamDesc for any error.
    // (Not shown.)
```

Here’s a description of the parameters used in this call:

1. A pointer to the Apple event to get the parameter descriptor from (obtained previously).
2. A constant specifying that the function should get the descriptor for the direct parameter.
3. A constant specifying that the descriptor should be returned as a descriptor list, coercing it if necessary. If the coercion fails, the function returns the result code `errAECoercionFail`.
4. The address of a variable in which the function stores the returned descriptor list.

See [Getting Data From a Descriptor List](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkobsfvbecqsfiffeosi) for details on working with a descriptor list.

The `AEGetParamDesc` function supplies a copy of the descriptor for the parameter, so you must dispose of it when you’re finished with it by calling the `AEDisposeDesc` function. For an example, see [Listing 4-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkobsfvbecqsfjjaucrq).

If an Apple event parameter contains an object specifier, your handler should use the `AEResolve` function, other Apple Event Manager functions, and your own application-defined functions to resolve the object specifier—that is, to locate the Apple event object in your application that the specifier describes. For more information, see [“Resolving and Creating Object Specifier Records”](https://developer.apple.com/documentation/mac/IAC/IAC-231.html#HEADING231-0) in [Inside Macintosh: Interapplication Communication](https://developer.apple.com/documentation/mac/IAC/IAC-2.html).

To get the descriptor for an attribute or to get the data from an attribute you use routines that are similar to those you use with parameters: the `AEGetAttributePtr` and `AEGetAttributeDesc` functions.

For example, Listing 4-3 shows how to use `AEGetAttributePtr` to get the data from the `keyEventSourceAttr` attribute of an Apple event.

__Listing 4-3__  Getting a value from an attribute

```
    DescType        returnedType;
    AEEventSource   sourceOfAE;
    Size            actualSize;
    OSErr           myErr;

myErr = AEGetAttributePtr( theAppleEvent,// 1
                            keyEventSourceAttr,// 2
                            typeShortInteger,// 3
                            &returnedType,// 4
                            (void *) &sourceOfAE,// 5
                            sizeof (sourceOfAE),// 6
                            &actualSize);// 7

    // Check the returned value from AEGetParamDesc for any error.
    // (Not shown.)
```

Here’s a description of the parameters used in this call:

1. A pointer to the Apple event to get the attribute data from (obtained previously).
2. A constant specifying the attribute from which to get the data.
3. A constant specifying that the data should be returned as a short integer.
4. The address of a variable in which the function stores the type of the actual descriptor returned.
5. The address of a variable in which the function stores the requested data. If the data is not already a short integer, the Apple Event Manager coerces it as necessary. The value should equal one of the event source constant values described in [Event Source Constants](Selected%20Apple%20Event%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgiwugsceizbeer2f).

   If you allocate a buffer for this parameter, it’s up to you to free it when you are finished with it.
6. The size of the return buffer.
7. The address of a variable in which the function stores the actual size of the returned data after coercion has taken place. You can check this value to make sure you got all the data.

Because the data within a descriptor is opaque, you use Apple Event Manager functions to extract it. In some cases, such as the example shown in Listing 4-3, the data is of known type and size, or can be coerced to a known type, and you can store it in a variable of that type.

It is common, however, for a descriptor to contain data, such as text or an image, of unknown size. In situations of that type, you can call the `AEGetDescDataSize` function to find out how much memory you will need to store the data, allocate a buffer of that size, then call `AEGetDescData` to get the actual data from the descriptor. The code snippet in Listing 4-4 shows how you might use these functions to get data into a buffer.

__Listing 4-4__  Determining the size, then obtaining descriptor data

```
    Size dataSize = AEGetDescDataSize(desc);// 1
    UInt8* buffer = malloc(dataSize);// 2
    if (buffer)
    {
        OSErr err = AEGetDescData(desc, buffer, dataSize);// 3

        // If no error, use the data.// 4

        free(buffer);// 5
    }
```

Here’s a description of what this code does:

1. Calls an Apple Event Manager function to get the data size for the descriptor.
2. Creates a buffer of that size.
3. Calls an Apple Event Manager function to get the data from the descriptor into the buffer.
4. If no error occurred in getting the data, your application can use it as needed.
5. Frees the allocated buffer.

Alternatively, you can do the following:

1. Call the `AEGetParamPtr` function (shown in [Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkobsfvbecqsgjjfeiri)), passing a size of zero for the maximum size (line 6 in the listing).
2. Get the actual size value returned by `AEGetParamPtr`.
3. Allocate a buffer of that size.
4. Call `AEGetParamPtr` again to get the data into the buffer.
5. If you allocated memory for the buffer, free it when you are finished with it.

To get descriptors and their data from a descriptor list, you can call the `AECountItems` function to get the number of descriptors in the list, then set up a loop that calls `AEGetNthDesc` or `AEGetNthPtr` to get the data from each descriptor.

For example, an `open documents` event contains a direct parameter that specifies a list of documents to open. The parameter contains a descriptor list in which each descriptor specifies an alias to a file to open. Listing 4-5 shows how you can extract the descriptor list from the parameter, determine the number of items it contains, and extract each descriptor from the list.

__Listing 4-5__  Getting a descriptor list and its items

```
    AEDescList  docList;
    FSRef       theFSRef;
    long        index;
    long        count = 0;
    OSErr       err;

    err = AEGetParamDesc(theAppleEvent, keyDirectObject,
                         typeAEList, &docList);// 1

    err = AECountItems(&docList, &count);// 2

    for(index = 1; index <= count; index++)// 3
    {
        err = AEGetNthPtr(&docList, index, typeFSRef,
                        NULL, NULL, &theFSRef,
                        sizeof(theFSRef), NULL);// 4

        // Call routine to open document with current reference.// 5
    }
```

Here’s a description of what this code does:

1. Calls `AEGetParamDesc` to obtain, in the variable `docList`, a copy of the descriptor list from the direct parameter of the Apple event. Passes the constant `keyDirectObject` to identify the direct parameter and the constant `typeAEList` to indicate the desired descriptor type. (`theAppleEvent` is a pointer to the Apple event, obtained previously, to get the parameter descriptor from).
2. Calls `AECountItems`, passing the previously obtained descriptor list, to get the number of items in the list.
3. Sets up a loop based on the count.
4. Calls `AEGetNthPtr` to obtain the indexed descriptor from the list. Passes `typeFSRef` to indicate the descriptor should be coerced to a file system reference, if necessary (otherwise the returned value will be a file alias). Passes the address of the variable `theFSRef` as a buffer to store the reference.

   Passes `NULL` for the fourth and fifth parameters, indicating the keyword and descriptor type of the returned item aren’t needed.

   Also passes `NULL` for the last parameter, indicating the actual size of the returned data isn’t required. (If the returned size is larger than the size of the buffer you provided, you know that you didn’t get all of the data for the descriptor.)
5. Here you would call your own routine to open a document specified by the extracted file system reference.

For a more complete version of this code, including simple error handling, see [Listing 5-5](Responding%20to%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqgywugrkhinbuqrch).

If you create a descriptor, you must dispose of it when you are finished with it to prevent memory leaks. For example, when you extract a descriptor using the `AEGetParamDesc`, `AEGetAttributeDesc`, `AEGetNthDesc`, or `AEGetKeyDesc` function, you get a copy of the descriptor. You call the `AEDisposeDesc` function to dispose of your copy, thereby deallocating the memory used by its data.

Listing 4-6 shows how to dispose of a descriptor list returned by `AEGetParamDesc`.

__Listing 4-6__  Disposing of a descriptor list obtained from the direct object of an Apple event

```
AEDescList  docList;
OSErr       err;
err = AEGetParamDesc(theAppleEvent, keyDirectObject, typeAEList, &docList);

// Check for error, then perform operations on the descriptor list here.

AEDisposeDesc(&docList);
```

You can safely call `AEDisposeDesc` on a null descriptor (but not on a null pointer!) A _null descriptor_ is one that has been initialized as shown in the following code snippet.

```
AEDesc      someDesc = { typeNull, 0L };

// Code to obtain a descriptor, which may fail.

// Safe to dispose, whether or not previous code succeeded.
AEDisposeDesc(&someDesc);
```

You can perform the same initialization using the `AEInitializeDesc` function, as shown in this code snippet.

```
    AEDesc      someDesc;

    AEInitializeDesc(&someDesc);
```

When you obtain a copy of a descriptor with one of the buffer-based functions, such as `AEGetAttributePtr` or `AEGetNthPtr`, the data is copied into a buffer provided by your application. You must then free any allocated memory when finished with the buffer.

[Next](Responding%20to%20Apple%20Events.md)[Previous](Apple%20Event%20Dispatching.md)

