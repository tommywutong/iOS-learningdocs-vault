---
title: Apple Events Programming Guide
apple_id: TP40001449
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/coercions_aepg/coercions_aepg.html
archived_at: '2026-07-15T05:19:29.203727Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Events Programming Guide](Introduction%20to%20Apple%20Events%20Programming%20Guide.md)


[Next](Testing%20and%20Debugging%20Apple%20Event%20Code.md)[Previous](Creating%20and%20Sending%20Apple%20Events.md)

# Writing and Installing Coercion Handlers

_Coercion_ is the process of converting a descriptor and the data it contains from one type to another. When coercing between types, by definition the descriptor type is changed to the new type. However, if the underlying data representation is the same, data conversion is not required.

Functions that perform coercions are referred to as _coercion handlers_. The Mac OS provides default coercion handlers to convert between many different descriptor types. Default handlers can, for example, convert aliases to file system specifications, integers to Boolean data types, and characters to numeric data types. These handlers may be implemented by the Apple Event Manager, the Open Scripting framework, or other frameworks. [Table C-2](Default%20Coercion%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgmwvgvzr) lists descriptor types and the available default coercions.

You can also provide your own coercion handlers to perform coercions that the default handlers don’t support. This chapter describes how to write coercion handlers and how to install them so that they are available to your application.

For many of the Apple Event Manager functions that your application uses to extract data from an Apple event, you can specify a desired descriptor type for the returned data. If the original data is of a different type, the Apple Event Manager attempts to coerce the data to the requested descriptor type. For more information on functions that let you specify a desired descriptor type, see [Coercing Data From an Apple Event](Working%20With%20the%20Data%20in%20an%20Apple%20Event.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkobsfvbecqshireesqq).

Coercion handling works by a process that is similar to the one described previously for dispatching Apple events to Apple event handlers:

- You write coercion handler functions to coerce data between types that your application works with but that are not handled by a default coercion handler.
- Your application registers coercion handlers with the Apple Event Manager for all the descriptor data types it can convert between. A handler may handle just one type of coercion or multiple types. To specify multiple types, you use the constant `typeWildCard`.
- The Apple Event Manager creates an application coercion handler dispatch table for your application. The dispatch table maps the descriptor types your application can coerce to the coercion handlers it provides.

  The Apple Event Manager also creates a system coercion dispatch handler, described below, for the default coercion handlers.
- When the Apple Event Manager needs to perform a coercion in your application, it goes through these steps until the coercion is handled:

  - It looks for a coercion handler in your application coercion dispatch table.
  - It looks for a coercion handler in your system coercion dispatch table, which includes the default coercions described in [Table C-2](Default%20Coercion%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrrgmwvgvzr).
  - If it can’t find an appropriate coercion handler, it returns the result code `errAECoercionFail`.

Although your application can have both a system coercion dispatch table and an application dispatch table, you should generally install all coercion handlers in the application coercion dispatch table. For Carbon applications running in Mac OS 8 or Mac OS 9, a handler in the system coercion dispatch table could reside in the system heap, where it would be available to other applications. However, your application should not install a handler in a system coercion dispatch table with the goal that the handler will get called when other applications perform coercions—this won’t necessarily work in Mac OS 8 or Mac OS 9 and will not work in Mac OS X.

When you write a coercion handler, it must do the following things:

- Validate the information passed to it so that it has a reasonable chance of success.
- Gain access to the information to be coerced.
- Convert the information to the specified type.
- Create a new descriptor of the specified type.

There are two types of coercion handlers. The first, which matches the format defined for the `AECoerceDescProcPtr` data type, expects the caller to pass a descriptor containing the data to be coerced. The second, which matches the format defined for the `AECoercePtrProcPtr` data type, expects the caller to pass a a pointer to the data to be coerced. These data types are described in _[Apple Event Manager Reference](https://developer.apple.com/documentation/applicationservices/apple_event_manager)_.

The examples in this chapter show how to work with a coercion handler that uses descriptors. However the differences in working with the pointer-based type are fairly straight-forward.

To write a a coercion handler named `CoerceApplesToOranges`, based on the `AECoerceDescProcPtr` data type, you would declare the handler as shown in Listing 7-1.

__Listing 7-1__  Declaring a coercion handler

```
OSErr CoerceApplesToOranges (
    const AEDesc * fromDesc,// 1
    DescType toType,// 2
    long handlerRefcon,// 3
    AEDesc * toDesc// 4
);
```

The following are descriptions of the numbered parameters:

1. A pointer to the descriptor to be coerced.
2. The type to coerce to.
3. A reference variable that will be passed to your handler—you can use it for any purpose.
4. A descriptor pointer where the handler will store the coerced descriptor.

   This routine creates a new descriptor, so it is up to the calling routine to dispose of the descriptor.

Suppose that you want to write a coercion handler to convert text strings into your internal “bar” data type. The `typeBar` type is defined as shown in Listing 7-2.

__Listing 7-2__  An application-defined data type

```
enum {
  typeBar = 'bar!'
};
```

Listing 7-3 provides a slightly simplified version of the handler you might write.

__Listing 7-3__  A simple coercion handler

```swift
static OSErr TextToBarCoercionHandler(const AEDesc* fromDesc, DescType toType, long handlerRefcon, AEDesc* toDesc)
{
    require_noerr((fromDesc->descriptorType != typeChar),CoercionFailed);// 1
    require_noerr((toType != typeBar), CoercionFailed);
    require_noerr((handlerRefcon != 1234), CoercionFailed);// 2

    long dataSize = AEGetDescDataSize(fromDesc);// 3
    char dataPtr[dataSize];
    OSErr err = AEGetDescData(fromDesc, dataPtr, dataSize);
    require_noerr(err, CoercionFailed);

    long result = 0;
    const char* pChar = (const char*) dataPtr;
    while (dataSize-- > 0)// 4
        result += *pChar++;

    err = AECreateDesc(typeBar, &result, sizeof(result), toDesc);// 5

    if (err != noErr)// 6
        err = errAECoercionFail;

CoercionFailed:// 7
        return err;
}
```

Here’s what the code in `TextToBarCoercionHandler` does:

1. Checks the passed parameters to validate that it can handle the requested coercion, using the macro `require_noerr`, which jumps to the error label `CoercionFailed` if a value isn’t supported.

   Coercion handlers that support multiple types will have additional work to do here.
2. Checks that the passed reference constant matches the expected value. You previously set the reference constant when you installed the coercion handler (shown in [Installing a Coercion Handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhawugrkhjbaukski)).
3. Gets the size of the data in the descriptor to be coerced and uses it to get the actual data from the descriptor.
4. In a while loop, converts the data from type text to type bar (by summing the bytes).
5. Creates a new descriptor of type bar, using the coerced data.
6. If it was unable to create the coerced descriptor, returns an error indicating the coercion failed.
7. Whether it jumped to the error label or fell through on success, returns an error code indicating whether the coercion succeeded or failed.

These are the main differences if you want to write a coercion handler based on the `AECoercePtrProcPtr` data type, which works with a pointer to data:

- The coercion handler has two additional parameters: one specifies the descriptor type of the data the pointer parameter points to; the other specifies the size of the data.
- When obtaining the data to convert, you use the size and type information to extract the data from the pointer, rather than getting the type and the data from a passed descriptor.

To install a coercion handler, you use the `AEInstallCoercionHandler` function, which is declared as shown in Listing 7-4.

__Listing 7-4__  Declaration of AEInstallCoercionHandler

```
OSErr AEInstallCoercionHandler (
    DescType fromType,// 1
    DescType toType,// 2
    AECoercionHandlerUPP handler,// 3
    long handlerRefcon,// 4
    Boolean fromTypeIsDesc,// 5
    Boolean isSysHandler// 6
);
```

You specify as parameters to this function:

1. The descriptor type of the data coerced by the handler. You can pass `typeWildCard`to accept all types.
2. The descriptor type of the resulting data. You can pass `typeWildCard` to accept all types.
3. The address of the coercion handler for this descriptor type; the handler is declared as described in [Writing a Coercion Handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhawugrkhjjdessce).
4. A reference constant to pass to the handler when it is called. You can use the reference constant for any purpose you want.
5. A Boolean value that indicates whether your coercion handler expects the data to be specified as a descriptor or as a pointer to the actual data.
6. A Boolean value that indicates whether your coercion handler should be added to your application’s coercion dispatch table or the system coercion dispatch table.

To call the `TextToBarCoercionHandler` handler defined in [Listing 7-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhawugrkhivcemskf), you can use code like that shown in Listing 7-5.

__Listing 7-5__  Installing a coercion handler

```
OSErr err = AEInstallCoercionHandler(
                typeChar, // Coerce from this type
                typeBar, // to this type,
                TextToBarCoercionHandler, //using this handler,
                1234,   //  passing this reference constant.
                true,   //  The handler operates on descriptors,
                false); //  and resides in the application table.
```

Here’s what the parameters in this call specify:

1. Coerce from type `'TEXT'`.
2. Coerce to type `typeBar`.
3. Use the handler `TextToBarCoercionHandler` to perform the coercion.
4. Pass the reference constant 1234.
5. The handler operates on descriptors.
6. The handler resides in the application’s coercion dispatch table.

You can use code like that shown in Listing 7-6 to test the `TextToBarCoercionHandler` handler defined in [Listing 7-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbzfvbuqmrqhawugrkhivcemskf).

__Listing 7-6__  Testing a coercion handler

```
    AEDesc textDesc;
    const char* kText = "1234";
    OSErr err = AECreateDesc(typeChar, kText, strlen(kText), &textDesc);// 1

    AEDesc barDesc;
    err = AECoerceDesc(&textDesc, typeBar, &barDesc);// 2
    if (err == noErr)
    {
        // Use the descriptor as needed.

        // Dispose of the descriptor when finished with it.
        err = AEDisposeDesc(&barDesc);// 3
    }
    err = AEDisposeDesc(&textDesc);// 4
```

Here is what the code in this snippet does:

1. Creates a descriptor containing the text string “1234”.
2. Calls the Apple Event Manager function `AECoerceDesc`, passing the text descriptor, the desired type (type bar), and the address of a descriptor in which to store the coerced descriptor.
3. If the coercion is successful, disposes of the coerced descriptor. Because a coercion returns a new descriptor, your application must dispose of the descriptor when it is finished with it. (This code snippet does not include full error handling.)
4. Disposes of the text descriptor.

If the coercion fails, you can set a breakpoint in your coercion handler to determine if it is ever called. Possible problems include:

- You didn’t install the coercion handler.
- The type you passed to `AECoerceDesc` was different than the type you registered for your coercion handler.
- The text descriptor you created has a different descriptor type than you registered for your coercion handler.

You can install a single coercion handler that specifies the constant `typeWildCard` for both the to and from types. Then any time the Apple Event Manager attempts to dispatch a coercion to the application, it will invoke that handler. This provides a convenient bottleneck for debugging.

Using wildcards can also be convenient as a general way to handle coercions, with one or a small number of handlers converting between supported types and the application’s private data types.

[Next](Testing%20and%20Debugging%20Apple%20Event%20Code.md)[Previous](Creating%20and%20Sending%20Apple%20Events.md)

