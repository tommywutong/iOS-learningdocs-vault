---
title: 64-Bit Transition Guide for Cocoa
apple_id: TP40004247
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Cocoa64BitGuide/64BitChangesCocoa/64BitChangesCocoa.html
archived_at: '2026-07-15T07:11:58.983244Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Transition Guide for Cocoa](Introduction%20to%2064-Bit%20Transition%20Guide%20For%20Cocoa.md)


[Next](Converting%20an%20Existing%20Application%20to%2064-Bit.md)[Previous](Moving%20to%2064-Bit%20Addressing.md)

# 64-Bit Changes To the Cocoa API

The 64-bit changes to the Cocoa API are largely targeted at those parameter and return types required for 64-bit addressing. However, consistency, ease of porting, and "impedance match" are also goals and thus most 32-bit quantities in the API are growing to 64 bits. The Cocoa 64-bit changes fall into three major categories: integers, floating-point values, and enumeration constants.

If you are a creating a new Cocoa application and you want to make it 64-bit capable from the outset, you need to incorporate the API changes into your code. You also might want to maintain a source base that ensures binary compatibility and source compatibility for both 32-bit and 64-bit architectures.

The biggest 64-bit change in the Cocoa API is the introduction of the `NSInteger` and `NSUInteger` data types. These two types now replace most occurrences of `int` and `unsigned int` in the framework headers. The parameter and return types that remain as `int` and `unsigned int` in Cocoa header files are unchanged for one of two reasons:

- They need to be a fixed size,
- They need to correspond with those defined by another API, such as file descriptors, Mach ports, and four-character codes.

On 64-bit architectures, `NSInteger` and `NSUInteger` are defined as `long` and `unsigned long`, respectively. To maintain binary compatibility with 32-bit applications, they are declared in the Foundation header file `NSObjCRuntime.h` using the `__LP64__` macro to distinguish between 32-bit and 64-bit builds, as follows:

```
#if __LP64__
    typedef long NSInteger;
    typedef unsigned long NSUInteger;
#else
    typedef int NSInteger;
    typedef unsigned int NSUInteger;
#endif
```

Additionally for the 64-bit initiative, many new methods have been added to the Cocoa frameworks with "integer" in their names. These methods are counterparts to other methods in the same class with "int" in their names; these methods need to continue dealing with values that are specifically `int`. The "integer" methods have parameter or return types of `NSInteger` or `NSUInteger` while the "int" methods accept or return values of the native types `int` or `unsigned int`. Table 2-1 lists the new methods.

__Table 2-1__  "Integer" methods added to the Cocoa frameworks

| Class | Methods |
| `NSCoder` | [encodeInteger:forKey:](https://developer.apple.com/documentation/foundation/nscoder/1411551-encodeinteger)  [decodeIntegerForKey:](https://developer.apple.com/documentation/foundation/nscoder/1409246-decodeinteger) |
| `NSUserDefaults` | [setInteger:forKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/setInteger:forKey:)  [integerForKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/integerForKey:)  (Note: available since OS X v10.0) |
| `NSString` | [integerValue](https://developer.apple.com/documentation/foundation/nsstring/1410267-integervalue) |
| `NSCell` | [integerValue](https://developer.apple.com/documentation/appkit/nscell/1527783-integervalue)  [setIntegerValue:](https://developer.apple.com/documentation/appkit/nscell/1527783-integervalue) |
| `NSControl` | [integerValue](https://developer.apple.com/documentation/appkit/nscontrol/1428969-integervalue)  [setIntegerValue:](https://developer.apple.com/documentation/appkit/nscontrol/1428969-integervalue) |
| `NSScanner` | [scanInteger:](https://developer.apple.com/documentation/foundation/nsscanner/1411082-scaninteger) |
| `NSNumber` | [integerValue](https://developer.apple.com/documentation/foundation/nsnumber/1412554-integervalue)  [unsignedIntegerValue](https://developer.apple.com/documentation/foundation/nsnumber/1413324-uintvalue)  [initWithInteger:](https://developer.apple.com/documentation/foundation/nsnumber/1409397-init)  [initWithUnsignedInteger:](https://developer.apple.com/documentation/foundation/nsnumber/1412531-init)  [numberWithInteger:](https://developer.apple.com/documentation/foundation/nsnumber/1551473-numberwithinteger)  [numberWithUnsignedInteger:](https://developer.apple.com/documentation/foundation/nsnumber/1551469-numberwithunsignedinteger) |
| `NSActionCell` | [integerValue](https://developer.apple.com/documentation/appkit/nsactioncell/1807046-integervalue) |

To set limits for the new `NSInteger` and `NSUInteger` types, `NSObjCRuntime.h` also defines the following constants:

```
#define NSIntegerMax LONG_MAX
#define NSIntegerMin LONG_MIN
#define NSUIntegerMax ULONG_MAX
```


As shown in the previous section, Cocoa defines `NSInteger` and `NSUInteger` conditionally (using the `__LP64__` macro) so that, as long as the project consistently uses the new data types, the underlying primitive type varies according to whether the target architecture is 32-bit or 64-bit.

The `NS_BUILD_32_LIKE_64` preprocessor macro works in a different manner. It declares `NSInteger` to be `long` (instead of `int`) and `NSUInteger` to be `long unsigned int` even on 32-bit portions of the source base.

```
#if __LP64__ || NS_BUILD_32_LIKE_64
    typedef long NSInteger;
    typedef unsigned long NSUInteger;
#else
    typedef int NSInteger;
    typedef unsigned int NSUInteger;
#endif
```

This makes it possible to do something like the following without getting warnings.

```
NSInteger i;
printf("%ld", i);
```

The `NS_BUILD_32_LIKE_64` macro is useful when binary compatibility is not a concern, such as when building an application.

Floating point quantities in the Core Graphics framework (Quartz), which are `float` on 32-bit architectures, are being expanded to `double` to provide a wider range and accuracy for graphical quantities. Core Graphics declares a new type for floating-point quantities, `CGFloat`, and declares it conditionally for both 32-bit and 64-bit. This change affects Cocoa because of its close dependency on Core Graphics. Where a parameter or return value in the Cocoa frameworks is a graphical quantity, `CGFloat` now replaces `float`.

The `CGFloat` changes made in the Foundation and, especially, the Application Kit are so numerous that its easier to point out the methods with floating-point parameters and return types that _don't_ change to `CGFloat`; that is, they remain as `float`. These methods fall into certain categories, described in the captions to Table 2-2, Table 2-3, Table 2-4, Table 2-5, and Table 2-6.

__Table 2-2__  Type-specific parameters and return values

| Class | Methods |
| `NSActionCell` | [floatValue](https://developer.apple.com/documentation/appkit/nsactioncell/1807042-floatvalue) |
| `NSCell` | [floatValue](https://developer.apple.com/documentation/appkit/nscell/1534292-floatvalue)  [setFloatValue:](https://developer.apple.com/documentation/appkit/nscell/1534292-floatvalue) |
| `NSControl` | [floatValue](https://developer.apple.com/documentation/appkit/nscontrol/1428889-floatvalue)  [setFloatValue:](https://developer.apple.com/documentation/appkit/nscontrol/1428889-floatvalue) |
| `NSString` | [floatValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/floatValue) |
| `NSNumber` | [floatValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/floatValue)  [initWithFloat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/initWithFloat:)  [numberWithFloat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/clm/NSNumber/numberWithFloat:) |
| `NSScroller` | [setFloatValue:knobProportion:](https://developer.apple.com/documentation/appkit/nsscroller/1523664-setfloatvalue) |
| `NSPrinter` | [floatForKey:inTable:](https://developer.apple.com/documentation/appkit/nsprinter/1525195-floatforkey): |
| `NSUserDefaults` | [floatForKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/floatForKey:)  [setFloat:forKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/setFloat:forKey:) |
| `NSScanner` | [scanFloat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanFloat:) |
| `NSKeyedArchiver` | [encodeFloat:forKey:](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1417776-encode) |
| `NSKeyedUnarchiver` | [decodeFloatForKey:](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1412252-decodefloatforkey) |
| `NSCoder` | [encodeFloat:forKey:](https://developer.apple.com/documentation/foundation/nscoder/1414384-encode)  [decodeFloatForKey:](https://developer.apple.com/documentation/foundation/nscoder/1408104-decodefloatforkey) |
| `NSByteOrder.h` | About a dozen "swap" functions. |

__Table 2-3__  Typesetting factors

| Class | Methods |
| `NSATSTypesetter` | [hyphenationFactor](https://developer.apple.com/documentation/appkit/nsatstypesetter/1526758-hyphenationfactor)  [hyphenationFactorForGlyphAtIndex:](https://developer.apple.com/documentation/appkit/nsatstypesetter/1533979-hyphenationfactorforglyphatindex)  [setHyphenationFactor:](https://developer.apple.com/documentation/appkit/nsatstypesetter/1526758-hyphenationfactor) |
| `NSLayoutManager` | [hyphenationFactor](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403134-hyphenationfactor)  [hyphenationFactor](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403134-hyphenationfactor) |
| `NSTypesetter` | [hyphenationFactor](https://developer.apple.com/documentation/appkit/nstypesetter/1535877-hyphenationfactor)  [setHyphenationFactor:](https://developer.apple.com/documentation/appkit/nstypesetter/1535877-hyphenationfactor) |
| `NSParagraphStyle` | [hyphenationFactor](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1529275-hyphenationfactor)  [tighteningFactorForTruncation](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1529278-tighteningfactorfortruncation) |

__Table 2-4__  Media: frame rate, volume, animation percentage

| Class | Methods |
| `NSAnimation` | [frameRate](https://developer.apple.com/documentation/appkit/nsanimation/1526694-framerate)  [setFrameRate:](https://developer.apple.com/documentation/appkit/nsanimation/1526694-framerate)  [currentValue](https://developer.apple.com/documentation/appkit/nsanimation/1531043-currentvalue)  `animation:valueForProgress:` |
| `NSMovieView` | `setRate:`  `rate`  `setVolume:`  `volume` |
| `NSSound` | [setVolume:](https://developer.apple.com/documentation/appkit/nssound/1477315-volume)  `volume` |

__Table 2-5__  Compression factor

| Class | Methods |
| `NSBitmapImageRep` | `getCompression:factor:`  `setCompression:factor:`  `TIFFRepresentationUsingCompression:factor:`  `TIFFRepresentationOfImageRepsInArray:usingCompression:factor:` |
| `NSImage` | `TIFFRepresentationUsingCompression:factor:` |

__Table 2-6__   Tablet-event pressure and rotation

| Class | Methods |
| `NSEvent` | `pressure`  `rotation`  `tangentialPressure`  `mouseEventWithType:location:modifierFlags:timestamp:windowNumber:context:eventNumber:clickCount:pressure:` |

A problem with enumeration (`enum`) constants is that their data types are frequently indeterminate. In other words, `enum` constants are not predictably `unsigned int`. With conventionally constructed enumerations, the compiler actually sets the underlying type based on what it finds. The underlying type can be (signed) `int` or even `long`. Take the following example:

```
type enum {
    MyFlagError = -1,
    MyFlagLow = 0,
    MyFlagMiddle = 1,
    MyFlagHigh = 2
} MyFlagType;
```

The compiler looks at this declaration and, finding a negative value assigned to one of the member constants, declares the underlying type of the enumeration `int`. If the range of values for the members does not fit into an `int` or `unsigned int,` then the base type silently becomes 64-bit (`long`). The base type of quantities defined as enumerations can thus change silently size to accord with the values in the enumeration. This can happen whether you're compiling 32-bit or 64-bit. Needless to say, this situation presents obstacles for binary compatibility.

As a remedy for this problem, Apple has decided to be more explicit about the enumeration type in the Cocoa API. Instead of declaring arguments in terms of the enumeration, the header files now separately declare a type for the enumeration whose size can be specified. The members of the enumeration and their values are declared and assigned as before. For example, instead of this:

```
typedef enum {
    NSNullCellType = 0,
    NSTextCellType = 1,
    NSImageCellType = 2
} NSCellType;
```

there is now this:

```
enum {
    NSNullCellType = 0,
    NSTextCellType = 1,
    NSImageCellType = 2
};
typedef NSUInteger NSCellType;
```

The enumeration type is defined in terms of `NSInteger` or `NSUInteger` to make the base enumeration type 64-bit capable on 64-bit architectures. For OS X v10.5 all enumerations declared in the Cocoa frameworks now take this form. In some cases, an enumeration type is now declared where one had not existed before.

Unfortunately, this change affects type checking of enumeration constants; you can pass any integer value in a method parameter typed as, say, `NSCellType`, not just one of the values in the enumeration. However, the change does allow more specific typing of bit masks, which were previously declared as `unsigned int`. You can now use the `typedef`s for parameters which are bit masks. For instance,

```objc
- (NSComparisonResult)compare:(NSString *)string options:(unsigned)mask;
```

can now be

```objc
- (NSComparisonResult)compare:(NSString *)string options:(NSStringCompareOptions)mask;
```


The use of some of the other primitive C types in the Cocoa API are changing in the 64-bit initiative, while others are unaffected. The following summarizes the changes and non-changes:

- `char` and `short` — No changes in the Cocoa API.
- `long` — In versions of OS X prior to version 10.5, the scripting and Apple event part of the Cocoa API used `long` for four-byte codes; these return types and parameter types are now changing to `FourCharCode`.
- `long long` — Prior to OS X v10.5, the [NSFileHandle](https://developer.apple.com/documentation/foundation/filehandle) class used `long long` for file offsets, which gives a 64-bit value on both 32-bit and 64-bit architectures. This is unchanged.

The Cocoa OpenGL API (including the classes [NSOpenGLContext](https://developer.apple.com/documentation/appkit/nsopenglcontext), [NSOpenGLPixelBuffer](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer), [NSOpenGLPixelFormat](https://developer.apple.com/documentation/appkit/nsopenglpixelformat), and [NSOpenGLView](https://developer.apple.com/documentation/appkit/nsopenglview)) follow the data-type changes made for the C OpenGL framework for Leopard by adopting the standard OpenGL types such as `GLint`, `GLsizei`, and `GLenum` for parameters and return values. These types were chosen in part to maintain binary compatibility under 32-bit (where `long` and `int` are the same size).

The Objective-C runtime API `(/usr/include/objc`) has undergone significant modification for OS X v10.5. Most Cocoa developers don't directly call these functions, so these changes should not affect them. However, if you do use the Objective-C runtime API, you should be aware that there are implications for 64-bit binaries. If you are building your project 64-bit, you cannot use the old Objective-C runtime API.

[Next](Converting%20an%20Existing%20Application%20to%2064-Bit.md)[Previous](Moving%20to%2064-Bit%20Addressing.md)

