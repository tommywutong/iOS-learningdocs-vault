---
title: 64-Bit Guide for Carbon Developers
apple_id: TP40004381
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Carbon64BitGuide/PortingTo64Bit/PortingTo64Bit.html
archived_at: '2026-07-15T05:22:31.488042Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Guide for Carbon Developers](Introduction%20to%2064-Bit%20Guide%20for%20Carbon%20Developers.md)


[Next](Changes%20in%20the%20Human%20Interface%20Toolbox.md)[Previous](The%20Transition%20to%2064-Bit%20Addressing.md)

# Modifying Your Application to Use 64-Bit Addressing

This chapter explains what kinds of modifications are needed in existing Carbon applications to make them compile and run as 64-bit executables.

OS X v10.5 (Leopard) provides two different implementations of its programming interfaces: one for 32-bit applications and another for 64-bit applications. You may choose to build your application using either one or both of these implementations. Some Leopard header files have been modified to support both implementations, and these header files often select or remove code for 64-bit compilation.

For 32-bit applications, Apple’s goal is to maintain complete source compatibility; when recompiled on Leopard, 32-bit applications should not need to change their sources to compile against Leopard headers. If you find instances where changes to the Leopard headers have broken the compilation of your 32-bit application, you should treat these as bugs and report them to Apple.

If you plan to modify your application to use 64-bit addressing, you may need to adopt standard data types that can be used identically in both 32-bit and 64-bit applications. You also need to be aware that the APIs used to implement a Carbon user interface—menus, windows, views, toolbars, navigation dialogs, and so on—are generally not available. If you want to create a 64-bit application, you need to use Cocoa to implement its user interface.

Later in this document, you’ll learn more about replacement alternatives for the APIs and technologies that aren’t available to 64-bit applications.

The differences between the 32-bit and 64-bit programming interfaces are marked in header files using the following preprocessor conditionals:

```
#if __LP64__
(code available only to 64-bit applications)
#endif
```

```
#if !__LP64__
(code available only to 32-bit applications)
#endif
```

These two conditionals are used to select or remove code for 64-bit compilation in a manner that is independent of the machine architecture (PowerPC or Intel). This is the primary mechanism used to provide 32-bit and 64-bit versions of an API or a standard data type such as `CGFloat`.

In the context of this document, standard types are Apple-defined data types that can be used identically in both 32-bit and 64-bit applications. In OS X v10.5, Apple has redefined some of these types (or defined new types) to make it easier for you to maintain a source base that compiles for both 32-bit and 64-bit targets. These standard types are used in function parameters and return values to implement 64-bit addressing and 64-bit quantities when compiling 64-bit targets. You may need to modify your source code to take full advantage of these wider parameters and return values.

Commonly used standard types such as `ByteCount`, `ByteOffset`, `ItemCount`, and `UniCharCount` have been defined as `long`, which makes them 64-bit types for 64-bit applications:

```
typedef unsigned long     ByteCount;
typedef unsigned long     ByteOffset;
typedef unsigned long     ItemCount;
typedef unsigned long     UniCharCount;
```

New standard types have been added to provide consistent representation of user-specified data:

```
typedef void *            PRefCon;
#if __LP64__
typedef void *            URefCon;
typedef void *            SRefCon;
#else
typedef UInt32            URefCon;
typedef SInt32            SRefCon;
#endif
```

Core Foundation has redefined several standard types to accommodate wide values for 64-bit applications:

```
typedef unsigned long     CFTypeID;
typedef unsigned long     CFOptionFlags;
typedef unsigned long     CFHashCode;
typedef signed long       CFIndex;
```

Core Graphics (Quartz) has defined a new standard type to increase the precision of floating-point values for 64-bit applications:

```
#if __LP64__
typedef double CGFloat;
#else
typedef float CGFloat;
#endif
```

It’s also worth noting that declarations of the fixed-size types `SInt32` and `UInt32` have been changed to make them remain 32-bit quantities for 64-bit applications:

```
#if __LP64__
typedef unsigned int      UInt32;
typedef signed int        SInt32;
#else
typedef unsigned long     UInt32;
typedef signed long       SInt32;
#endif
```


The following general changes have been made in a number of C APIs to adopt standard types. These changes should have no effect on your application.

- Many functions and data structures now use standard types, such as `ItemCount`, `ByteCount`, `ByteOffset`, and `UniCharCount`, rather than fixed-size types, such as `UInt32` and `SInt32`.
- Function parameters that contain user-specified data and that were previously typed as a 32-bit integer value (`SInt32` or `UInt32`) are now typed as `SRefCon` or `URefCon`. For 64-bit applications, these new standard types will widen as necessary to allow a pointer to be passed in and out.
- Graphics-related functions that formerly used the `float` type now use the `CGFloat` type defined by Core Graphics. This type expands to `double` for 64-bit applications.

To advance your application toward the goal of being 64-bit capable, you are encouraged to adopt these standard types in your own source code. At a minimum, you need to make sure that the data you pass to and receive from system functions uses compatible types.

For example, if you are currently casting a pointer to `SInt32` or `UInt32` before passing it as user-specified data, you should instead cast the pointer to `SRefCon` or `URefCon` to avoid truncating your pointer in 64-bit targets. If you are currently passing an integer value as user-specified data, you will need to add a cast to `SRefCon` or `URefCon` to avoid errors when compiling your code for 64-bit targets.

If you’re already using standard types, your code may be making assumptions about their sizes that no longer hold true in 64-bit applications. Here are some examples.

In this example, the code assumes that `ItemCount` is a 32-bit type.

```
ItemCount count;   // Used to be declared as UInt32, now unsigned long
memmove(mem, &count, 4);
```

Instead of `4`, `sizeof(ItemCount)` should have been used.

In this example, the code assumes that `CFIndex` is the same size as `SInt32`.

```
CFIndex c;   // Used to be declared as SInt32, now long
CFNumberRef n = CFNumberCreate(NULL, &c, kCFNumberSInt32Type);
```

Instead of `kCFNumberSInt32Type`, `kCFNumberCFIndexType` should have been used.

In this example, the code assumes that a prototype exists for a function that returns a pointer-sized type.

```
CFStringRef s = SomeGetStringFunction();
```

If a prototype for `SomeGetStringFunction` is not encountered, the compiler assumes an `int`, hence 32-bit, return value.

This example uses variable-sized data across process boundaries—in this case, by writing the data to a file.

```
/* 32-bit process */
CGFloat floatValue;
fwrite(&floatValue, sizeof(floatValue), 1, file);  // writes out 4 bytes

/* 64-bit process */
CGFloat floatValue;
fread(&floatValue, sizeof(floatValue), 1, file);  // tries to read back 8 bytes
```

Basically, any use of variable-size types in data structures that go outside the address space of a process should be examined.

The Collection Manager is available to 64-bit applications, but unlike many other APIs, the `itemSize` parameters have not been widened to 64 bits; they remain `SInt32`. This can cause problems if your code is already casting an `itemSize` parameter to an `SInt32*` type before calling a Collection Manager function. For example, this code will compile without warnings in a 64-bit target but will fail at runtime because `sizeof(ByteCount)` is no longer equal to `sizeof(SInt32)`.

```
MyData data;
ByteCount itemSize = sizeof(data);
GetCollectionItem (collection, kDataTag, kDataID, (SInt32*) &itemSize, &data);
```

Passing the address of a `ByteCount` (or `long`) variable to [GetCollectionItem](https://developer.apple.com/documentation/coreservices/1551357-getcollectionitem) causes this function to return zero bytes instead of `sizeof(data)` bytes. The same issue applies to [GetIndexedCollectionItem](https://developer.apple.com/documentation/coreservices/1551437-getindexedcollectionitem) and [GetTaggedCollectionItem](https://developer.apple.com/documentation/coreservices/1551359-gettaggedcollectionitem). Consider reviewing your use of these functions to verify that you are using the correct parameter type for the `itemSize` parameter.

Some Core Foundation functions return a value by reference rather than as the function result. It’s easy to pass the address of an incorrectly sized variable to one of these functions. For example, suppose you have stored an integer in a dictionary and you wish to retrieve its value.

```
UInt32 value = 0;
if (CFDictionaryGetValueIfPresent (dict, CFSTR("key"), (void**) &value))
    DoSomething (value);
```

In a 64-bit target, this code will compile without warnings but will fail at runtime because `sizeof(UInt32)` is no longer equal to `sizeof(void*)`. The [CFDictionaryGetValueIfPresent](https://developer.apple.com/documentation/corefoundation/1516739-cfdictionarygetvalueifpresent) function will write an 8-byte value into the 4-byte memory location that you have provided, overwriting some other memory. To fix this, use a variable of type `long`, `unsigned long`, `CFIndex`, or `intptr_t`, any of which will properly resize to match the size of a pointer.

This section lists a few of the managers, services, and individual functions that are not available to 64-bit applications. You can find more detailed information about these changes in the next two chapters, [Changes in the Human Interface Toolbox](Changes%20in%20the%20Human%20Interface%20Toolbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnbnknltc) and [Changes in Other C APIs](Changes%20in%20Other%20C%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknlti).

A number of legacy Carbon technologies have been either wholly or partially deprecated in favor of more modern equivalents. You are discouraged from using these technologies in 32-bit applications. If you are creating 64-bit applications, you must use alternative technologies.

For example, these deprecated technologies are not available to 64-bit applications:

- QuickDraw. Functions to manipulate regions and simple data structures (`Point` and `Rect`) are still available, but you cannot use QuickDraw to draw in a 64-bit application. See [QuickDraw](Changes%20in%20Other%20C%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknltg).
- The `FSSpec` data type and functions that use this type. Most of these functions have replacements that use the `FSRef` type. See [File Manager](Changes%20in%20Other%20C%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknlte).
- Classic icon formats such as `'ICON'`, `'cicn'`, and icon suites. You must use the `IconRef` data type or a CGImage to represent an icon. See [Icon Services and Utilities](Changes%20in%20Other%20C%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknltcnq).
- Memory Manager. A number of deprecated or obsolete functions are not available. See [Memory Manager](Changes%20in%20Other%20C%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknltm).
- Scrap Manager. You can use the Pasteboard Manager or `NSPasteboard` instead. See [Scrap Manager](Changes%20in%20the%20Human%20Interface%20Toolbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnbnknltm).
- Display Manager. You must use the `CGDirectDisplayID` data type and Quartz Display Services instead. See [Display Manager](Changes%20in%20Other%20C%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknltk).
- Sound Manager. You should use Core Audio instead. See [Sound Manager](Changes%20in%20Other%20C%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknltcni).

Some other technologies are still supported for 32-bit applications but are not available to 64-bit applications. Among these technologies are the following:

- Carbon Human Interface Toolbox. APIs such as the Window Manager, Menu Manager, Data Browser, HIView, HIToolbar, and HIArchive are not available to 64-bit applications. You must implement your user interface with Cocoa. See [Choosing a Development Path for Your Carbon User Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqmznknlte).
- Navigation Services. You must use Cocoa to implement dialogs for navigating, opening, and saving files. See [Navigation Services](Changes%20in%20the%20Human%20Interface%20Toolbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnbnknltk).
- The Carbon Printing API. You must use Cocoa to implement printing features that display a user interface. See [Printing](Changes%20in%20Other%20C%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknlto).
- QuickTime C APIs. You must use QuickTime Kit instead. See [QuickTime](Changes%20in%20Other%20C%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknltq).
- MLTE. You should use the Cocoa text system instead. See [Multilingual Text Engine (MLTE)](Changes%20in%20the%20Human%20Interface%20Toolbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnbnknlte).
- ATSUI. You should use Core Text or Cocoa instead. See [Apple Type Services for Unicode Imaging (ATSUI)](Changes%20in%20Other%20C%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknlts).
- Carbon APIs for displaying standard color and font selection windows. You should use Cocoa to display these windows. See [Color Picker Manager](Changes%20in%20Other%20C%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknltcma) and [Fonts Window Services](Changes%20in%20Other%20C%20APIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobrfvbuqnjnknltcmi).

During the evolution of OS X, a number of improvements and new features have been added to Carbon to help you modernize your Carbon user interface (UI) and begin to incorporate Cocoa features. You have been encouraged to adopt newer UI technologies such as composited windows, HIView-based controls, and Quartz 2D for drawing. In OS X v10.5, the addition of HICocoaView has opened up a number of possibilities for adding Cocoa features to applications that use Carbon windows.

Because most Carbon UI functions are not available to 64-bit applications, you have two possible development paths. You can continue modernizing and improving your Carbon UI with the expectation that your application will remain a 32-bit application for the foreseeable future. Apple plans to support and maintain the 32-bit Carbon Human Interface Toolbox, although Apple will not be adding any significant new features to these APIs. The other development path is more challenging and also potentially more rewarding in the long term. You can develop a 64-bit version of your application, using Cocoa to implement your UI. As you do so, consider going one step further and implementing other parts of your application using Cocoa. For an introduction to Cocoa programming, see _[Cocoa Fundamentals Guide](../../Cocoa/Cocoa%20Fundamentals%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzu)_.

At this time, a reasonable approach would be to compare the amount of work required for each development path, assess the potential benefits, and decide which option is more attractive.

[Next](Changes%20in%20the%20Human%20Interface%20Toolbox.md)[Previous](The%20Transition%20to%2064-Bit%20Addressing.md)

