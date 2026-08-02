---
title: Carbon Overview
apple_id: TP30000990
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/newtocarbon/LegacyInterfaces/LegacyInterfaces.html
archived_at: '2026-07-15T05:25:15.212544Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon Overview](Introduction%20to%20Carbon%20Overview.md)


[Next](Document%20Revision%20History.md)[Previous](The%20Carbon%20Factory%20Tour.md)

# Legacy Interfaces

This chapter covers Carbon interfaces that are mostly of historical interest. These interfaces were included to assist developers porting legacy Mac OS code to Mac OS X. For new developers, these interfaces may be useful only to gain perspective on the evolution of Macintosh system software. In most cases, the functionality of these managers is covered in a newer interface

- _Code Fragment Manager._ Written to allow the system and applications to prepare and execute Preferred Executable Format (PEF) binaries, the native executable file format for Classic Mac OS PowerPC applications. While Mac OS X supports PEF binaries, the native executable file format is called Mach-O.
- _Collection Manager._ This interface let you create abstract data types to store related information together. You should use the Core Foundation interface instead.
- _Component Manager._ Older Mac OS programs often loaded special format plug-ins using the Component Manager. On Mac OS X, you should use the Plug-In Services interface in Core Foundation.
- _Device Manager._ Older Mac OS programs accessed hardware through the Device Manager. On Mac OS X, you should use the I/O Kit instead.
- _Display Manager._ Provided a way to manipulate multiple monitor locations and resolutions from your application. Deprecated in Mac OS X v10.4. Now replaced by the CGDirectDisplay API in Quartz Services..
- _Event Manager._ Originally written to handle the older cooperative multitasking event model. The Carbon Event Manager is more powerful and is a core component of the Human Interface Toolbox.
- _HTML Rendering Library._ Essentially, this interface allowed you to render text and images in a window as if it were in a browser. It provided support for such design elements as border and scroll bars, as well as for navigation using URL links. Deprecated In Mac OS X v10.4. Replaced by WebKit.
- _Keychain Manager._ Now replaced by Keychain Services. See _[Security Overview](../../Security/Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_for more information.
- _List Manager._ Formerly used to create columned lists of data (similar to the list view option in a Finder window), you should now use the data browser control (part of the Control Manager).
- _Low Memory Accessors._ These functions allowed you to access useful system information (such as the location of the mouse) stored as global variables in so-called "low memory." This practice of accessing low memory directly was questionable even then, and certainly not suggested now. In almost all cases, better, safer functions exist in other interfaces for obtaining the same information.
- _Memory Management Utilities_ are used for specialized low-level memory operations, such as direct memory access (DMA) and those that take place at the interrupt level. Many of the functions in this interface aren't even supported in Carbon, and it is unlikely that you will need to use the ones that are. Mostly deprecated in Mac OS X v10.4.
- _Memory Manager._ This interface allowed pre-Mac OS X applications to allocate and manage application memory to avoid fragmentation or low-memory conditions. Mac OS X handles any memory management for you transparently, so you only need to use `malloc` or `calloc` and `free` to allocate and free memory respectively.
- _Mixed Mode Manager._ Originally designed to allow PowerPC code to call emulated 68K code (and vice versa), the Mixed Mode Manager is now used to allow CFM-based PEF code to call Mac OS X's native Mach-O code and vice versa. If you build Mach-O-based, Mac OS X applications, you don't need this interface.
- _Open Transport_ was Carbon's low-level networking interface. Typically you need this interface only if you are implementing network protocols (such as TCP/IP) in your application or driver. Deprecated in Mac OS X v10.4. Use CFNetwork or socket library APIs instead.
- _Palette Manager._ This interface allowed to you specify the contents of palettes, which let you specify the colors to use to render an image. For example, if a picture contained mostly dark colors, grays and blues, you could index the palette to use only those colors, eliminating those that didn't appear (yellows, bright red). Using a fixed selection of colors allowed you to reduce the size of the image, because not as much information was needed to render it. The Palette Manager was useful in the days when, due to memory constraints, many computers could display only a limited number of colors.
- _Pascal String Utilities._ Contains functions for manipulating Pascal strings. In most cases you will be using Unicode Strings on Mac OS X, but if you need to manipulate Pascal strings, this is where to go. Deprecated in Mac OS X v10.4 and later.
- _Power Manager_ allows you to control power management features. For example, a screen saver program could use this interface to put the PowerBook to sleep after a given time. Other applications may want to monitor the battery status of the PowerBook. Mostly deprecated in Mac OS X v10.4. Use I/O Kit instead.
- _QuickDraw._ The original 2D graphics drawing interface. Deprecated in Mac OS X v10.4 and later. Superseded by Quartz and Core Graphics.
- _QuickDraw Text._ Superseded by MLTE or, if you need more complex text manipulations, Apple Type Services for Unicode Imaging (ATSUI).
- _The Resource Manager._ Let you access information in a bundle hierarchy stored as an old-style Mac OS resource (that is, in a data fork-based file with the .rsrc extension). The Resource Manager complements Bundle Services in allowing access to images, text, and other resources stored in a bundle.
- _Scrap Manager._ The original interface to handle cut-and-paste operations, this technology has been superseded by the Pasteboard Manager.
- _Script Manager_ allows you to handle older Mac OS script systems (or text encodings), providing support for text input and display processing. On Mac OS X you will usually be handling Unicode text, so you probably won't need this interface.
- _SCSI Manager._ Originally written to communicate with SCSI devices. On Mac OS X you should use the I/O Kit instead.
- _TextEdit._ An interface to perform basic text manipulation. Its replacement, the Multilingual Text Engine, offers significant additional features, such as Unicode support.
- _Text Utilities_ let you perform basic manipulation of non-Unicode text strings. If Mac OS X is your primary platform, you will likely be using Unicode strings, which means you should investigate the Unicode Utilities or Core Foundation String Services instead.
- _Time Manager._ Lets you set timers to perform periodic actions or to have actions occur at a particular time. Although timers in the Carbon Event Manager can provide some of the same functionality, the Time Manager is useful for cases where you need something to happen outside of your usual event loops. Mostly deprecated in Mac OS X v10.4 and later.
- _URL Access Manager_, which provides an easy interface for uploading and downloading files to and from a given URL. Deprecated in Mac OS X v10.4 and later.

[Next](Document%20Revision%20History.md)[Previous](The%20Carbon%20Factory%20Tour.md)

