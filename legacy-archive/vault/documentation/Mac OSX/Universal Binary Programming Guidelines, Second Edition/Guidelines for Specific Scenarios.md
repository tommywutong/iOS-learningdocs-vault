---
title: Universal Binary Programming Guidelines, Second Edition
apple_id: TP40002217
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/universal_binary/universal_binary_tips/universal_binary_tips.html
archived_at: '2026-07-15T08:16:38.193724Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Universal Binary Programming Guidelines, Second Edition](Introduction.md)


[Next](Preparing%20Vector-Based%20Code.md)[Previous](Swapping%20Bytes.md)

# Guidelines for Specific Scenarios

This chapter lists an assortment of scenarios that relate to a specific technology or API. Although many of these scenarios are uncommon, you will want to at least glance at the topics to determine whether anything applies to your application. The topics are organized alphabetically.

Aliases are big-endian on all systems. Applications that add extra information to the end of an `AliasHandle` must ensure that the extra data is always endian-neutral or of a defined endian type, preferably big-endian.

The `AliasRecord` data structure is opaque when building your application with the Mac OS X v10.4(Universal) SDK. Code that formerly accessed the `userType` field of an `AliasRecord` must use the Alias Manager functions `GetAliasUserType`, `GetAliasUserTypeFromPtr`, `SetAliasUserType`, or `SetAliasUserTypeFromPtr`. Code that formerly accessed the `aliasSize` field of an `AliasRecord` must use the functions `GetAliasSize` or `GetAliasSizeFromPtr`.

These Alias Manger functions are available in Mac OS X v10.4 and later. For more information, see _[Alias Manager Reference](https://developer.apple.com/documentation/coreservices/carbon_core/alias_manager)_.

For cross platform portability, avoid using bit fields. It’s best not to use the `NSArchiver` class to archive any structures that contain bit fields as integers. Individual values are stored in the archives in an architecture and compiler dependent manner. In cases where archives already contain such structures, you can read a structure correctly by changing its declaration so that the bit fields are swapped appropriately

AppleScript actions are platform-independent and do not need any changes to run on Intel-based Macintosh computers. However, any action that contains Cocoa code, whether it is a solely Cocoa action or an action that uses both AppleScript and Cocoa code, must be built as a universal binary to run correctly on both architectures.

For more information, see _[Automator Programming Guide](../../Apple%20Applications/Automator%20Programming%20Guide/Introduction%20to%20Automator%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinjq)_.

When you shift a value by the width of its type or more, the fill bits are undefined regardless of the architecture. In fact, two different compilers on the same architecture could differ on the value of `y` after these two statements:

`uint32_t x = 0xDEADBEEF;`

`uint32_t y = x >> 32;`

Don’t mix using the C bitwise operators with the Carbon functions [BitTst](https://developer.apple.com/documentation/coreservices/1494606-bittst), [BitSet](https://developer.apple.com/documentation/coreservices/1494618-bitset), and [BitClr](https://developer.apple.com/documentation/coreservices/1494616-bitclr) and the POSIX macros `setbit`, `clrbit`, `isset`, and `isclr`. If you consistently use the Carbon and POSIX functions and avoid the C bitwise operators, your code will function properly. Keep in mind, however, that you must use the Carbon and POSIX functions on the correct kind of data. The Carbon and POSIX functions perform a byte-by-byte traversal, which causes problems on an Intel-based Macintosh when they operate on data types that are larger than 1 byte. You can use these functions only on a pointer to a string of endian-neutral bytes. When you need to perform bit manipulation on integer values you should use functions such as `(int32 & (1 << 26))` instead of `BitTst(&int32, 5L`).

You’ll encounter problems when you use the function `BitTst` to test for 24-bit mode. For example, the following bit test returns `false`, which indicates that the process is running in 24-bit mode, or at least that the code is not running in 32-bit mode. The POSIX equivalents perform similarly:

```
Gestalt(gestaltAddressingModeAttr, &gestaltResult);
if (!(BitTst(&gestaltResult,31L)) )      /*If 24 bit
```

You can use any of the bit testing, setting, and clearing functions if you pass a pointer to data whose byte order is fixed. Used in this way, these functions behave the same on both architectures.

For more information, see the `ToolUtils.h` header file in the Core Services framework and _Mathematical and Logical Utilities Reference_.

Don't try to build a binary for a specific CPU subtype. Since the CPU subtype for Intel-based Macintosh computers is generic, you can't use it to check for specific functionality. If your application requires information about specific CPU functionality, use the `sysctlbyname` function, providing an appropriate selector. See _Mac OS X Man Pages_ for information on using `sysctlbyname`.

Dashboard widgets typically contain platform-independent elements such as HTML, JavaScript, CSS, and image files. If you create a widget that contains only these elements, it should work on both PowerPC and Intel-based Macintosh computers without any modification on your part. However, if your widget contains a plug-in, you must build the plug-in as a universal binary for it to run natively on an Intel-based Macintosh computer.

For more information, see _[Dashboard Programming Topics](../../Apple%20Applications/Dashboard%20Programming%20Topics/Introduction%20to%20Dashboard%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqmzx)_.

Many deprecated functions, such as those that use `PICT + PS` data, have byte swapping issues. You may want to replace deprecated functions at the same time you prepare your code to run as a universal binary. You’ll not only solve byte swapping issues, but your code will use functions that ultimately benefit future development.

A function that is deprecated has an availability statement in its header file that states the version of Mac OS X in which the function is deprecated. Many API reference documents provide a list of deprecated functions. In addition, compiler warnings for deprecated functions are on by default in Xcode 2.2 and later.

The standard disk partition format on an Intel-based Macintosh computer differs from the disk partition format of a PowerPC-based Macintosh computer. If your application depends on the partitioning details of the disk, it may not behave as expected. Partitioning details can affect tools that examine the hard disk at a low level.

By default, internal hard drives on Intel-based Macintosh computers use the GUID Partition Table (GPT) scheme and external drives use the Apple Partition Map (APM) partition scheme. To create an external USB or FireWire disk that can boot an Intel-based Macintosh computer, select the GPT disk partition scheme option using Apple Disk Utility. Starting up an Intel-based Macintosh using an APM disk is not supported.

Although both architectures are IEEE 754 compliant, there are differences in the rounding procedure used by each when operating on double-precision numbers. If your application is sensitive to bit-by-bit values in double-precision numbers, be aware that the same computation performed on each architecture may produce a different numerical result.

For more information, see Volume 1 of the Intel developer software manuals, available from the following website:

[http://developer.intel.com/design/Pentium4/documentation.htm](http://developer.intel.com/design/Pentium4/documentation.htm)

If your code operates on the file system at a low level and handles Finder information, keep in mind that the file system does not swap bytes for the following information:

- The `finderInfo` field in the HFSPlus data structures `HFSCatalogFolder`, `HFSPlusCatalogFolder`, `HFSCatalogFile`, `HFSPlusCatalogFile`, and `HFSPlusVolumeHeader`.
- The `FSPermissionInfo` data structure, which is used when the constant `kFSCatInfoPermissions` is passed to the HFSPlus functions `FSGetCatalogInfo` and `FSGetCatalogInfoBulk`.

The value of multibyte fields on disk always uses big-endian format. When running on a little-endian system, you must swap the bytes of any multibyte fields.

The `getattrlist` function retrieves the metadata associated with a file. The `getxattr` function, added in Mac OS X v10.4, retrieves extended attributes—those that are an extension of the basic set of attributes. When using the `getxattr` function to access the legacy attribute `"com.apple.FinderInfo"`, note that as with `getattrlist`, the information returned by this call is not byte swapped. (For more information on the `getxattr` and `getattrlist` functions see _Mac OS X Man Pages_.)

The FireWire bus uses big-endian format. If you are developing a universal binary version of an application that accesses a FireWire device, see “FireWire Device Access on an Intel-Based Macintosh” in _[FireWire Device Interface Guide](../../Device%20Drivers/FireWire%20Device%20Interface%20Guide/Introduction%20to%20FireWire%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrz)_ for a discussion of the issues you can encounter.

Font-related resource types (`FOND`, `NFNT`, `sfnt`, and so forth) are in big-endian format on both PowerPC and Intel-based Macintosh computers. If your application accesses font-related resource types directly, you must swap the fields of font-related resource types yourself.

The following functions from the ATS for Fonts API obtain font resources that are returned in big-endian format:

- `ATSFontGetTableDirectory`
- `ATSFontGetTable`
- `ATSFontGetFontFamilyResource`

The following functions from the Font Manager API obtain font resources that are returned in big-endian format. Note that Font Manager API is based on QuickDraw technology, which was deprecated in Mac OS X v10.4.

- `FMGetFontTableDirectory`
- `FMGetFontTable`
- `FMGetFontFamilyResource`

When the QuickDraw function `NewGWorld` allocates storage for the pixel buffer, and the depth parameter is 16 or 32 bits, the byte ordering within each pixel matters. The `pixelFormat` field of the `PixMap` data structure can have the values `k16BE555PixelFormat` or `k16LE555PixelFormat` for 2-byte pixels, and `k32ARGBPixelFormat` or `k32BGRAPixelFormat` for 4-byte pixels. (These constants are defined in the `Quickdraw.h` header file.) By default, `NewGWorld` always creates big-endian pixel formats (`k16BE555PixelFormat` or `k32ARGBPixelFormat`), regardless of the endian format of the system.

For best performance, it is generally preferable for you to use a pixel format that corresponds to the native byte ordering of the system. When you pass `kNativeEndianPixMap` in the `flags` parameter to `NewGWorld`, the byte ordering of the pixel format is big-endian on big-endian systems, and little-endian on little-endian systems.

You can use the GWorld pixel storage as input to the Quartz function `CGBitmapContextCreate` or as a data provider for the Quartz function `CGImageCreate`. The byte ordering of the source pixel format needs to be communicated to Quartz through additional flags in the `bitmapInfo` parameter. These flags are defined in the `CGImage.h` header file. Assuming that your `bitmapInfo` parameter is already set up, you now need to combine it (by using a bitwise `OR` operator) with `kCGBitmapByteOrder16Host` or `kCGBitmapByteOrder32Host` if you created the GWorld with a `kNativeEndianPixMap` flag. Similarly, you should use `kCGBitmapByteOrder16Big` or `kCGBitmapByteOrder32Big` when you know that your pixel byte order is big-endian.

Pure Java applications do not require any code changes to run on Intel-based Macintosh computers. However, Java applications that interface with PowerPC-based native code will not run successfully using Rosetta on Intel-based Macintosh computers.

Specifically, the following must be built as universal binaries:

- JNI libraries built for PowerPC-based Macintosh computers are not loaded using Rosetta because the Java Virtual Machine has already launched without using Rosetta. Java applications fail on Intel-based Macintosh computers when trying to load PowerPC-only binaries.
- Native applications that use the VM Invocation Interface to start a Java Virtual Machine must be built as universal binaries to run on Intel-based Macintosh computers. The Java VM must run natively; attempts by an application running using Rosetta to instantiate a JVM fail.

For more information, see _Technical Q &A QA1295: Java on Intel-based Macintosh Computers_ in the [ADC Reference Library](https://developer.apple.com/technicalqas/Java/index-title.html).

The I/O API (NIO) that was introduced in JDK 1.4 allows the use of native memory buffers. If you are a Java programmer who uses this API, you may need to revise your code. NIO byte buffers have a byte ordering that by default is big-endian. If you have Java code originally written for Mac OS X on PowerPC, when you create `java.nio.ByteBuffers` you should call the function `ByteBuffer.order(ByteOrder.nativeOrder())` to set the byte order of the buffers to the native byte order for the current architecture. If you fail to do this, you will obtain flipped data when you read multibyte data from the buffer using JNI.

The Memory Management Utilities data type `MachineLocation` contains information about the geographical location of a computer. The [ReadLocation](https://developer.apple.com/documentation/coreservices/1533377-readlocation) and `WriteLocation` functions use the geographic location record to read and store the geographic location and time zone information in extended parameter RAM.

If your code uses the `MachineLocation` data structure, you need to change it to use the `MachineLocation.u.dls.Delta` field that was added to the structure in Mac OS X version 10.0.

To be endian-safe, change code that uses the old field:

```
MachineLocation.u.dlsDelta = 1;
```

to use the new field:

```
MachineLocation.u.dls.Delta = 1;
```

The `gmtDelta` field remains the same—the low 24 bits are used. The order of assignment is important. The following is incorrect because it overwrites results:

```
MachineLocation.u.dls.Delta = 0xAA;    // u = 0xAAGGGGGG; G=Garbage
MachineLocation.u.gmtDelta = 0xBBBBBB;   // u = 0x00BBBBBB;
```

This is the correct way to assign the values:

```
MachineLocation.u.gmtDelta = 0xBBBBBB;   // u = 0x00BBBBB;
MachineLocation.u.dls.Delta = 0xAA;       // u = 0xAABBBBBB;
```

For more details see _Memory Management Utilities Reference_.

The `task_for_pid` function returns the task associated with a process ID (PID). This function can be called only if the process is owned by the `procmod` group or if the caller is `root`.

You can use PowerPlant on an Intel-based Macintosh computer by downloading the PowerPlant framework available from [http://sourceforge.net/projects/open-powerplant](http://sourceforge.net/projects/open-powerplant). This Open Source version of the PowerPlant Framework for Mac OS X includes support for Intel and GCC 4.0.

Multithreading is a technique used to improve performance and enhance the perceived responsiveness of applications. On computers with one processor, this technique can allow a program to execute multiple pieces of code _independently_. On computers with more than one processor, multithreading can allow a program to execute multiple pieces of code _simultaneously_. If your application is single-threaded, consider threading your application to take advantage of hardware multithreading processor capabilities. If your application is multithreaded, you’ll want to ensure that the number of threads is not hard coded to a fixed number of processors.

Dual-core technology improves performance by providing two physical cores within a single physical processor package. Multiprocessor and dual-core technology all exploit thread-level parallelism to improve application and system responsiveness and to boost processor throughput.

When you prepare code to run as a universal binary, the multithreading capabilities of the microprocessor are transparent to you. This is true whether your application is threaded or not. However, you can optimize your code to take advantage of the specific way hardware multithreading is implemented for each architecture.

In Objective-C, it is valid to send a message to a `nil` object. The Objective-C runtime assumes that the return value of a message sent to a `nil` object is `nil`, as long as the message returns an object or any integer scalar of size less than or equal to `sizeof(void*)`.

On Intel-based Macintosh computers, messages to a `nil` object always return `0.0` for methods whose return type is `float`, `double`, `long double`, or `long long`. Methods whose return value is a `struct`, as defined by the _[OS X ABI Function Call Guide](../../Developer%20Tools/OS%20X%20ABI%20Function%20Call%20Guide/Introduction%20to%20OS%20X%20ABI%20Function%20Call%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkmrr)_ to be returned in registers, will return `0.0` for every field in the data structure. Other `struct` data types will not be filled with zeros. This is also true under Rosetta. On PowerPC Macintosh computers, the behavior is undefined.

The information in this section is only for developers who use the Objective-C runtime library, which is used primarily for developing bridge layers between Objective-C and other languages, or for low-level debugging. Most developers do not need to use the Objective-C runtime library directly when programming in Objective-C.

If your application directly calls the Objective-C runtime function `objc_msgSend_stret`, you need to change your code to have it work correctly on an Intel-based Macintosh.

The x86 ABI for struct-return functions differs from the ABI for `struct-address-as-first-parameter` functions, but the two ABIs are identical on PowerPC. When you call `objc_msgSend_stret`, you must cast the function to a function pointer type that uses the expected `struct` return type. The same applies for calls to `objc_msgSendSuper_stret`.

For other details on the ABI, see [32-Bit Application Binary Interface](32-Bit%20Application%20Binary%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugywviucykjcummjqge).

If your application directly calls the Objective-C runtime function `objc_msgSend`, you should always cast to the appropriate return value. For instance, for a method that returns a `BOOL` data type, the following code executes properly on a PPC Macintosh but might not on an Intel-based Macintosh computer:

```
BOOL isEqual = objc_msgSend(string, @selector("isEqual:"), otherString);
```

To ensure that the code does executes properly on an Intel-based Macintosh computer, you would change the code to the following:

```
BOOL isEqual = ((BOOL (*)(id, SEL, id))objc_msgSend)(object, @selector("isEqual:"), otherString);
```


Macintosh computers that use an Intel microprocessor do not use Open Firmware. Although many parts of the I/O registry are present and work as expected, information that is provided by Open Firmware on a PowerPC Macintosh (such as a complete device tree) is not available in the I/O registry on a Macintosh that uses an Intel microprocessor. You can obtain some of the information from IODeviceTree by using the `sysctlbyname` or `sysctl` commands.

When defining an OpenGL image or texture, you need to provide a type that specifies to OpenGL which format the texture is in. Most of these functions (for example, `glTexImage2D`) take `format` and `type_` parameters that specify how the texture is laid out on disk or in memory. OpenGL supports a number of different image types; some are endian-neutral but others are not.

For example, a common image format is `GL_RGBA` with a type of `GL_UNSIGNED_BYTE`. This means that the image has a byte that specifies the red color data followed by a byte that specifies the green color data, and so forth. This format is not endian-specific; the bytes are in the same order on all architectures. Another common image format is `GL_BGRA`, often specified by the type `GL_UNSIGNED_INT_8_8_8_8_REV`. This type means that every 4 bytes of image data are interpreted as an `unsigned int`, with the most significant 8 bits representing the alpha data, the next most significant 8 bits representing the red color data, and so forth. Because this format is specific to the integer format of the host, the format is interpreted differently on little-endian systems than on big-endian systems. When using `GL_UNSIGNED_INT_8_8_8_8_REV`, the OpenGL implementation expects to find data in byte order ARGB on big-endian systems, but BGRA on little-endian systems.

Because there is no explicit way in OpenGL to specify a byte order of ARGB with 32-bit or 16-bit packed pixels (which are common image formats on Macintosh PowerPC computers), many applications specify `GL_BGRA` with `GL_UNSIGNED_INT_8_8_8_8_REV`. This practice works on a big-endian system such as PowerPC, but the format is interpreted differently on a little-endian system and causes images to be rendered with incorrect colors.

Applications that have this problem are those that use the OpenGL host-order format types, but assume that the data referred to is always big-endian. These types include, but are not limited to the following:

```
GL_SHORT
GL_UNSIGNED_SHORT
GL_INT
GL_UNSIGNED_INT
GL_FLOAT
GL_DOUBLE
GL_UNSIGNED_BYTE_3_3_2
GL_UNSIGNED_SHORT_4_4_4_4
GL_UNSIGNED_SHORT_5_5_5_1
GL_UNSIGNED_INT_8_8_8_8
GL_UNSIGNED_INT_10_10_10_2
GL_UNSIGNED_SHORT_5_6_5
GL_UNSIGNED_BYTE_2_3_3_REV
GL_UNSIGNED_SHORT_5_6_5_REV
GL_UNSIGNED_SHORT_4_4_4_4_REV
GL_UNSIGNED_SHORT_1_5_5_5_REV
GL_UNSIGNED_INT_8_8_8_8_REV
GL_UNSIGNED_INT_2_10_10_10_REV
```

If your application does not use any of these types, it is unlikely to have any problems with OpenGL. Note that an application is not necessarily incorrect to use one of these types. Many applications might already present host-order data tagged with one of these formats, especially with existing cross-platform code, because the Mac OS X implementation behaves the same way as a Windows implementation.

If an application incorrectly uses one of these types, its OpenGL textures and images are rendered with incorrect colors. For example, red might appear green, or the image might appear to be tinted purple.

You can fix this problem in one of the following ways:

1. If the images are generated or loaded algorithmically, change the code to generate the textures in host-order format that matches what OpenGL expects. For example, a JPEG decoder can be modified to store its output in 32-bit integers instead of four 8-bit bytes. The resulting data is identical on big-endian systems, but on a little-endian system, the bytes are in a different order. This matches the OpenGL expectation, and the existing OpenGL code continues to work on both architectures. This is the preferred approach.

   In many cases, rewriting the algorithms may prove a significant amount of work to implement and debug. If that’s the case, an approach that asks OpenGL to interpret the texture data differently might be a better approach for you to take.
2. If the application uses `GL_UNSIGNED_INT_8_8_8_8_REV` or `GL_UNSIGNED_INT_8_8_8_8`, it can switch between them based on the architecture. Since these two types are exactly byte swapped versions of the same format, using `GL_UNSIGNED_INT_8_8_8_8_REV` on a big-endian system is equivalent to using `GL_UNSIGNED_INT_8_8_8_8` on a little-endian system and vice versa. Code might look as follows:

```
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_BGRA_EXT,
#if __BIG_ENDIAN__
                    GL_UNSIGNED_INT_8_8_8_8_REV,
#else
                    GL_UNSIGNED_INT_8_8_8_8,
#endif
                    data);
```

   If this is a common idiom, it might be easiest to define it as a macro that can be used multiple times:

```
#if __BIG_ENDIAN__
#define ARGB_IMAGE_TYPE GL_UNSIGNED_INT_8_8_8_8_REV
#else
#define ARGB_IMAGE_TYPE GL_UNSIGNED_INT_8_8_8_8
#endif
/* later on, use it like this */
glTexImage2D (GL_TEXTURE_2D, 0, GL_RGB,
                width, height, 0, GL_BGRA_EXT,
                ARGB_IMAGE_TYPE, data);
```

   Note that switching between `GL_UNSIGNED_INT_8_8_8_8_REV` and `GL_UNSIGNED_INT_8_8_8_8` works only for this particular 32-bit packed-pixel data type. For 16-bit ARGB data stored using `GL_UNSIGNED_SHORT_1_5_5_5_REV`, there is no corresponding byte swapped type. Keep in mind that `GL_UNSIGNED_SHORT_5_5_5_1` is not a replacement for `GL_UNSIGNED_SHORT_1_5_5_5_REV` on an Intel-based Macintosh computer. The format is interpreted as bit-order `arrrrrbbbbbggggg` on a big-endian system, and as bit order `ggrrrrrabbbbbggg` on a little-endian system.
3. If you can’t use the previous approaches, you should either generate/load your data in the native endian format of the system and use the same pixel type on both architectures or use the `GL_UNPACK_SWAP_BYTES` pixel store setting to instruct OpenGL to swap the bytes of any texture loaded on a little-endian system. This setting applies to all texture or image calls made with the current OpenGL context, so it needs to be set only once per OpenGL context, for example:

```
#if __LITTLE_ENDIAN__
            glPixelStorei(GL_UNPACK_SWAP_BYTES, 1);
#endif
```

   This method causes images that use the problematic formats to be loaded as they would be on PowerPC. You should consider this option only if no other option is available. Enabling this option causes OpenGL to use a slower rendering path than normal. Performance-sensitive OpenGL applications may be significantly slower with this option enabled than with it off. Although this method can get an OpenGL-based program up and running in as little time as possible, it is highly recommended that you use one of the other two methods.

The kernel extension functions `OSDequeueAtomic` and `OSEnqueueAtomic` are not available on an Intel-based Macintosh.

For more information on these functions, see _[Kernel Framework Reference](https://developer.apple.com/documentation/kernel)_.

Applications that store pixel data in memory using ARGB format must take care in how they read data. If the code is not written correctly, it’s possible to misread the data; the result is colors or alpha that appear wrong.

If you see colors that appear wrong when your application runs on an Intel-based Macintosh computer, the following strategy may help you identify where pixel data is being read incorrectly.

Create a test image whose pixel data is easy to identify. For example, set each pixel so that alpha is `ff`, red is `aa`, green is `bb`, and blue is `cc`. Then read that image into your application. Figure 4-1 shows such an image.

__Figure 4-1__  A test image that can help locate the source of color problems

![A test image that can help locate the source of color problems](attachments/art/aabbcc.gif)

It's also helpful to go through your code and cast pixel data to the `unsigned char` data type.

Start with the portion of your code that reads the image. Use the following GDB command to examine the pixel data as hexadecimal bytes:

`x/<number_bytes>xb <address of first byte>`

This command prints the specified number of bytes, starting with the first byte of the first pixel. You should easily be able to see whether what’s displayed onscreen matches the values of the pixels in the test image. If the values you see do not match the test image, then you've identified the misreading problem. If the values match, then you need to identify other portions of your code that modify or transform pixel data, and inspect the pixel data after each transformation.

If you are using the Carbon Printing Manager, note that the PICT with PostScript (`'pictwps'`) printing path is not available on Intel-based Macintosh computers except under Rosetta. If you need only to support EPS data you can use Quartz drawing together with the function `PMCGImageCreateWithEPSDataProvider` to allow the inclusion of EPS data as part of your Quartz drawing. If you need to generate the PostScript code for your application drawing you should use the function `PMPrinterPrintWithFile`.

The Quartz constants shown in Table 4-1 specify the byte ordering of pixel formats. These constants, which are defined in the `CGImage.h` header file, are used in the `bitmapInfo` parameter. To specify byte ordering to Quartz, use a bitwise `OR` operator to combine the appropriate constant with the `bitmapInfo` parameter.

__Table 4-1__  Quartz constants that specify byte ordering

| Constant | Specifies |
| `kCGBitmapByteOrderMask` | The byte order mask |
| `kCGBitmapByteOrder16Big` | 16-bit, big-endian format |
| `kCGBitmapByteOrder32Big` | 32-bit, big-endian format |
| `kCGBitmapByteOrder16Little` | 16-bit, little-endian format |
| `kCGBitmapByteOrder32Little` | 32-bit, little-endian format |
| `kCGBitmapByteOrder16Host` | 16-bit, host-endian format |
| `kCGBitmapByteOrder32Host` | 32-bit, host-endian format |

If you have existing code that directly accesses the `picFrame` field of the QuickDraw `Picture` data structure, you should use the QuickDraw function `QDGetPictureBounds` to get the appropriately swapped bounds for a `Picture`. This function is available in Mac OS X version 10.3 and later. Its prototype is as follows:

```
Rect * QDGetPictureBounds(
            PicHandle   picH,
            Rect        *outRect)
```

If you have existing code that uses the QuickDraw `DeltaPoint` function or the HIToolbox `PinRect` function (defined in `MacWindows.h`), make sure that you do not cast the function result to a `Point` data structure. The horizontal difference is returned in the low 16 bits, and the vertical difference is returned in the high 16 bits. You can obtain the horizontal and vertical values by using code similar to the following:

```
    Point pointDiff;
    SInt32 difference = DeltaPoint (p1, p2);
    pointDiff.h = LoWord (difference);
    pointDiff.v = HiWord (difference);
```


The Component Manager recognizes which architectures are supported by a component by looking at the `'thng'` resource for the component, not the architecture of the file. You must specify the appropriate architectures in the `'thng'` resource. To accomplish this, in the `.r` file where you define the `'thng'` resource, modify your `ComponentPlatformInfo` array to look similar to the following:

```
#if defined(__ppc__)
kMyComponentFlags, kMyCodeType, kMyCodeID, platformPowerPCNativeEntryPoint,
#endif
#if defined(__i386__)
kMyComponentFlags, kMyCodeType, kMyCodeID, platformIA32NativeEntryPoint,
#endif
```

Then, rebuild your component. For details, see [Building a Universal Binary](Building%20a%20Universal%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrqgywviucykjcummjqge).

When you call the function `[QTMetaDataGetItemProperty](../../../../QuickTime/Conceptual/QT7Win_Update_Guide/Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcnmv2gcrdborquozlujf2gk3kqojxxazlsor4q)` and the type of the key whose value you are retrieving is `code`, the data returned is an `OSType`, not a buffer of four characters. (You can determine the key type by calling the function `[QTMetaDataGetItemPropertyInfo](../../../../QuickTime/Conceptual/QT7Win_Update_Guide/Chapter03/03QT7_Update_Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvcnmv2gcrdborquozlujf2gk3kqojxxazlsor4us3tgn4)`.) To ensure that your code runs properly on both PowerPC and Intel-based Macintosh computers, you must use a correctly-typed buffer so that the endian format of the data returned to you is correct. If you supply a buffer of the wrong type, for example a buffer of `UInt8` instead of a buffer of `OSType`, the endian format of the data returned in the buffer will be wrong on Intel-based Macintosh Computers.

If your application generates code at runtime, keep in mind that the compiler assumes that the stack must be 16-byte aligned when calling into Mac OS X libraries or frameworks. 16-byte stack alignment is enforced on Intel-based Macintosh computers, which means that you need to ensure that your code is 16-byte aligned to avoid having your application crash.

For more information, see _[OS X ABI Function Call Guide](../../Developer%20Tools/OS%20X%20ABI%20Function%20Call%20Guide/Introduction%20to%20OS%20X%20ABI%20Function%20Call%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkmrr)_.

A Spotlight importer is a plug-in bundle that extracts information from files created by an application. The Spotlight engine uses importers to gather information about new and existing files. Spotlight importers are not compatible with Rosetta. To run an importer on an Intel-based Macintosh as well as on a PowerPC-based Macintosh, you must compile it as a universal binary.

For more information on Spotlight, see _[Spotlight Overview](../../Carbon/Spotlight%20Overview/Introduction%20to%20Spotlight.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenry)_ and_[Spotlight Importer Programming Guide](../../Carbon/Spotlight%20Importer%20Programming%20Guide/About%20Spotlight%20Importers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrx)_.

The C preprocessor has several predefined macros whose purpose is to indicate the type of system and machine in use. If your code uses system-specific predefined macros, evaluate whether you really need to use them. In most cases applications need to know the capabilities available on a computer and not the specific system or machine on which the application is running. For example, if your application needs to know whether it is running on a little-endian or big-endian microprocessor, you should use the `__BIG_ENDIAN__` or `__LITTLE_ENDIAN__` macros or the Core Foundation function `CFByteOrderGetCurrent`. Do not use the `__i386__` and `__ppc__` macros for this purpose.

See _GNU C 4.0 Preprocessor User Guide_ for additional information.

USB uses little-endian format. If you are developing a universal binary version of an application that accesses a USB device, see “USB Device Access in an Intel-Based Macintosh” in _[USB Device Interface Guide](../../Device%20Drivers/USB%20Device%20Interface%20Guide/Introduction%20to%20USB%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzt)_ for a discussion of the issues you may encounter.

In addition to the following resources, check the ADC website periodically for updates and technical notes that might address other specific situations:

- _[Quartz Programming Guide for QuickDraw Developers](../../Carbon/Quartz%20Programming%20Guide%20for%20QuickDraw%20Developers/Introduction%20to%20Quartz%20Programming%20Guide%20for%20QuickDraw%20Developers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojy)_ which provides information on moving code from the deprecated QuickDraw API to Quartz
- _IA-32 Intel Architecture Optimization Reference Manual_, available from:

  [http://developer.intel.com/design/pentium4/manuals/index_new.htm](http://developer.intel.com/design/pentium4/manuals/index_new.htm)

[Next](Preparing%20Vector-Based%20Code.md)[Previous](Swapping%20Bytes.md)

