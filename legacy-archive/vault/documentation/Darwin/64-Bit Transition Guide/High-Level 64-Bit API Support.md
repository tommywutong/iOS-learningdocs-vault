---
title: 64-Bit Transition Guide
apple_id: TP40001064
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/64bitPorting/HighLevelAPIs/HighLevelAPIs.html
archived_at: '2026-07-15T07:23:04.044805Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Transition Guide](Introduction%20to%2064-Bit%20Transition%20Guide.md)


[Next](Cross-Architecture%20Plug-in%20Support.md)[Previous](Compiling%2064-Bit%20Code.md)

# High-Level 64-Bit API Support

Beginning in OS X v10.5, most OS X APIs are available to 64-bit applications. Going forward, Apple plans to make new APIs 64-bit-compatible unless otherwise noted. However, not all existing 32-bit APIs are supported in 64-bit applications.

This chapter includes a brief summary of these API changes and limitations and includes pointers to other documentation that provides more detailed coverage for specific technology areas.

The high-level API changes related to 64-bit support generally fall into one of the following categories:

- [Changes to Data Types](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgqwvgvzr)
- [New/Replaced/Deprecated APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgqwvgvzt)

These are described in detail in the sections that follow.

The most significant change is to data types and type usage. A number of Apple-specific data types are defined differently in the 64-bit world. In some cases, 32-bit values have been replaced with 64-bit values for future expansion. In other cases, data types that become 64-bit in a 64-bit environment have been replaced with data types that remain 32-bit—to preserve file format compatibility, for example.

The result of these changes is that a number of derived data types have different sizes (and thus, different declarations) depending on whether they are being used in a 32-bit or 64-bit context.

To support 64-bit applications, OS X has changed its data types and type usage in these broad areas:

- Size (and alignment) of base data types (for example, `long`)
- Choice of underlying base data types used in derived data types (such as `SInt32`)
- Base data types used in structure fields (such as those in `ScriptLanguageRecord`) and arguments to functions and methods
- API replacement and deprecation

These data types go by many names in various technology areas, but in terms of their underlying representation, the affected data types are one of those shown in [Data Type Changes](Major%2064-Bit%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrqg4wviucykjcummjqgm). In addition, a number of functions that use these base data types directly have been changed to use derived data types so that their underlying type can vary between 32-bit and 64-bit environments.

There are four common situations in which data types differ in the 64-bit world:

- 32-bit `int` data types that need to hold pointers. Because a pointer is 64 bits in length, these uses of `int` data types were changed to `long` data types.
- 32-bit `int` data types that could reasonably hold a larger data set in a 64-bit application. Because the viable number of objects in a data set can be much larger in a 64-bit application, these have been changed to `long` data types when it makes sense for such a large collection to exist. This determination varies on an API-by-API basis.
- 32-bit `long` data types that represent part of a data structure whose size and structure must not change. Because `long` is 64-bit on 64-bit architectures, these were changed to `int` to preserve compatibility.
- 32-bit `long` data types that represent counts, constants, or flags that cannot practically exceed the limits of a 32-bit integer (for example, the window identifier). Because `long` is 64-bit on 64-bit architectures, many such occurrences of `long` were changed to `int` where it does not make sense for a larger value to ever occur. This determination varies between APIs.

For example, the data type `URefCon` is defined in 32-bit applications as:

```
typedef unsigned long URefCon;
```

and in 64-bit applications as:

```
typedef void *URefCon;
```

These changes, which are sprinkled throughout all of the functions and data types in nearly every technology area, represent the vast majority of changes you will encounter.

In addition to API changes resulting from changes to the data types used in parameters and return values, other technology areas are changing significantly in the 64-bit world. Most of these changes are specific to C language APIs.

In certain technology areas (Carbon particularly), a few APIs have been deprecated for 32-bit use beginning in OS X v10.5. Most of these APIs are not available in 64-bit applications. For example, any functions using `FSSpec` are gone, so you must use `FSRef`-based functions. This change affects a number of other related technology areas. There are also a number of other small, isolated changes in various APIs. You can find out more about these changes using the Research Assistant in Xcode.

In addition to these function-level deletions, some entire Carbon and QuickTime technologies will not be supported in 64-bit applications.

Changes to technology areas fall into these broad categories: Carbon, Cocoa/Objective C, QuickTime, and other C APIs. The sections that follow explain these changes in more detail.

Most Objective-C APIs will not change substantially for 64-bit because most of the actual data types are sufficiently abstracted that the actual representation doesn’t matter to the application. For example, a `CFNumber` or `NSNumber` object could have arbitrary representation under the hood. However, if you extract this information into standard C types, you must be careful about the sizes of those types in a 64-bit environment.

There are exceptions, however. A number of `typedef` declarations in AppKit and Foundation are changing for 64-bit. Specifically, data types whose base types were originally defined as an `enum` now have base types that specify the desired integer representation, such as `int` or `long`.

In addition, the types `NSInteger` and `NSUInteger` have been added. These are used to replace the use of `int` and `unsigned int` in a number of function declarations. Because these types have the same underlying base type in a 32-bit environment, developers should not need to change their code for type compatibility in 32-bit applications. In 64-bit applications, however, the base types for `NSInteger` and `NSUInteger` are `long` and `unsigned long`, respectively. Thus in 64-bit applications, you will need to replace these uses of `int` and `unsigned int` with `NSInteger` and `NSUInteger`.

Finally, some Objective-C method declarations may change, particularly those that use the underlying C data types `int` and `long` or types derived from them. These APIs will have the same issues as standard C APIs, though to a lesser degree.

For more detailed information, see _[64-Bit Transition Guide for Cocoa](../../Cocoa/64-Bit%20Transition%20Guide%20for%20Cocoa/Introduction%20to%2064-Bit%20Transition%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbx)_.

As of v10.8, 32-bit kernel extensions are no longer supported. Drivers and other kernel extensions for earlier versions of OS X should provide 64-bit executables for OS X v10.6 and later.

In addition, the I/O Kit has been extended somewhat in OS X v10.5 to include support for 64-bit applications running on a 32-bit kernel. These changes are primarily in the form of additional methods in the `IOMemoryDescriptor` class.

All supported BSD kernel interfaces (KPIs) and system calls should be 64-bit clean beginning in OS X v10.4. Software that uses these calls from user space should not require any modifications specific to the use of these interfaces assuming they use the specified types for arguments and return values.

The QuickTime Kit classes will be the primary interface into QuickTime. Methods that take or return native QuickTime C identifiers (in particular, Movie, MovieController, Track, and Media) are not supported in 64-bit applications.

Although the QuickTime C APIs are not deprecated for 32-bit use, you cannot directly use them in 64-bit applications.

The QuickTime Music Architecture (QTMA) API is not available in 64-bit applications. As an alternative, you should use the Core Audio API.

For more information on QuickTime API support in 64-bit applications, see _[64-Bit Guide for Carbon Developers](../../Carbon/64-Bit%20Guide%20for%20Carbon%20Developers/Introduction%20to%2064-Bit%20Guide%20for%20Carbon%20Developers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobr)_.

Some Carbon Managers and technologies are significantly reduced or unavailable in 64-bit applications. For detailed information, see _[64-Bit Guide for Carbon Developers](../../Carbon/64-Bit%20Guide%20for%20Carbon%20Developers/Introduction%20to%2064-Bit%20Guide%20for%20Carbon%20Developers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobr)_.

In general, most C API changes are in the use of `int` and `long` within function prototypes. Similarly, many data types based on `int` or `long` have changed sizes.

In Core Graphics a number of functions that previously returned `int` now return `bool` to more accurately reflect the information returned. Also, a number of Core Graphics functions now use `CGFloat` instead of `float`. The size of a `CGFloat` is larger in 64-bit applications than in 32-bit applications to allow for greater precision and range.

Finally, in Core Foundation and other technology areas, a number of uses of `int` and `long` have been replaced by aliases to these types in the form of named types such as `CFIndex`. Some of these are new types created because the underlying type changes from `int` to `long` (or vice versa) between 32-bit and 64-bit declarations. In other cases, these are preexisting types that simply do a better job at explaining the usage of a given parameter (for example, using a `CFIndex` to hold an index value).

For more detailed information, see _[64-Bit Guide for Carbon Developers](../../Carbon/64-Bit%20Guide%20for%20Carbon%20Developers/Introduction%20to%2064-Bit%20Guide%20for%20Carbon%20Developers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobr)_.

[Next](Cross-Architecture%20Plug-in%20Support.md)[Previous](Compiling%2064-Bit%20Code.md)

