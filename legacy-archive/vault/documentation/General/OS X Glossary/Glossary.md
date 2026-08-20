---
title: OS X Glossary
apple_id: TP40008752
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2010-07-09'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/SLGlobalGlossary/Glossary/Glossary.html
archived_at: '2026-07-15T07:34:29.132007Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X Glossary](Introduction%20to%20OS%20X%20Glossary.md)


[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20OS%20X%20Glossary.md)

# Glossary

- __5.1 Surround Sound__

  A surround sound speaker configuration consisting of five speakers arranged in specific positions along the circumference of a circle and a subwoofer (the “.1”). The speaker channels are typically designated as follows: left, center, right, left surround. right surround, and LFE (low frequency effect).

- __8.24__

  Sometimes written as _Q8.24_ or _fx8.24_. A [fixed-point sample](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg43tm) size used as the canonical audio sample type for processing [linear PCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge2to) audio in iOS, in lieu of 32-bit floating-point samples. In an 8.24 audio sample there are eight bits to the left of the radix point, forming the integer (or “magnitude") portion of the value, and 24 bits to the right, forming the fractional portion.

- __AAC__

  Advanced Audio Coding. A compressed, lossy, [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2dq) scheme, originally a component of the MPEG-2 standard as MPEG-2 AAC. Defined in 1997 as part of ISO/IEC 13818-7. Enhanced for the MPEG-4 standard as MPEG-4 AAC. MPEG-2 AAC provides better perceived audio quality at the same bit rate compared to MPEG-1, layer 3 ( [MP3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3ti)), according to results published in ISO/IEC JTC1/SC29/WG11, N2006 (February 1998). MPEG-4 AAC extends MPEG-2 AAC with additional coding tools. See also [lossy compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4dg).

- __About window__

  A modeless window that displays an application’s version and copyright information.

- __absolute object specifier__

  An object specifier that has enough information to identify an object or objects uniquely. For an object specifier to an application object to be complete, its outermost container must be the application itself. Compare [relative object specifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy3dc).

- __absolute position__

  A specific position, given in coordinates, for the origin of each character or glyph in a line of text. Compare [absolute object specifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgaydm).

- __abstraction__

  (1) The process of separating the interface to some functionality from the underlying implementation in such a way that the implementation can be changed without changing the way that piece of code is used. (2) The API (interface) for some piece of functionality that has been separated in this way.

- __abstract type__

  In information property lists, a type that defines general characteristics of a family of documents. Each abstract type has corresponding concrete types. See also [concrete type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm4dq).

- __AC-3__

  A compressed, lossy, perceptual audio coding format developed by Dolby Laboratories, Inc. Sometimes called _Dolby Digital_ or _Dolby Surround AC-3_. See also [lossy compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4dg), [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2dq).

- __Accelerate framework__

  An OS X framework that serves as a container for several other frameworks related to optimization and high performance.

- __access control entry__

  See [ACE](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgazda).

- __access control list__

  See [ACL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgazdc).

- __accessibility__

  The successful access to information and information technologies by people with disabilities. OS X provides support for users with disabilities in the form of VoiceOver (Apple’s full-featured screen reading technology), speech recognition and text-to-speech features, and mouse and keyboard alternatives. OS X includes the accessibility programming interface, which defines how an assistive technology, such as a refreshable braille display or head-tracking mouse, can communicate with and control an application.

- __access layer__

  The classes in the package `com.webobjects.eoaccess` , which include the model-level classes `EOEntity`, `EOAttribute`, and `EORelationship`. You usually do not work with classes in this layer directly, but rather indirectly through the `EOModel` class.

- __access object__

  An opaque data structure containing one or more access control lists (ACLs). Each keychain item has one access object.

- __access permissions__

  See [permissions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2tc).

- __access rights__

  See [permissions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2tc).

- __accumulating attribute group__

  A set of attribute choices in which the user can select multiple items, such as Bold and Italic. Compare [mutually exclusive attribute group](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi4tk).

- __ACE__

  Access control entry. A component of an ACL that associates a user or group with a set of permissions and specifies whether each permission is allowed or denied. See also [Unicode Utilities](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2tk).

- __ACL__

  A structure containing information describing what must happen (display a confirmation dialog, ask for a password, and so forth) in order to permit a specific operation to occur. An ACL may also contain a list of applications that are always trusted to perform that operation. Each keychain item has one or more associated ACLs, and each ACL applies to a single operation that can be done with that item, such as encrypting or decrypting it. See also [access object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgaytm).

- __action__

  (1) In OS X, a connection that involves the sending of a message from one object to another when a certain user action occurs. For example, when a user presses a button, the button object calls the action method of its target object to notify that object that the action occurred. (2) In Automator, a building block used to build workflows.

- __action button__

  The button that confirms the message text in a dialog. The action button is in the lower-right corner of a dialog. It is often, but not always, the default button.

- __action line__

  In Xcode, the code line indicated by the pointer at the time you choose a debugging command from the shortcut menu.

- __action object__

  In Xcode, the object on which you want to perform an action.

- __activate__

  To bring a running application to the front of the screen, allowing the user to interact with it. Compare [launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgezdk).

- __active__

  In iOS, used to describe an [audio session](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tm) state in which playback or recording can proceed. Compare [inactive](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe2to).

- __active build configuration__

  The build configuration Xcode uses to build the active target and any targets it depends upon. See also [build configuration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgizto).

- __active driver__

  A device driver that implements advanced power management tasks, such as determining device idleness and performing pre-shutdown tasks. Compare [passive driver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqzta).

- __active end__

  The point at which the user releases the mouse button when selecting a range of text or other items. Compare [anchor point](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga3ti).

- __active executable__

  The executable environment that Xcode uses when you run or debug a product. See also [executable environment](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4ytm).

- __active extension__

  A [filename extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg42ta) claimed by at least one application registered with Launch Services. Compare [valid extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4tm).

- __active SDK__

  The SDK used to build a product and the runtime environment on which the product is to run. See also [SDK family](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhaydc).

- __active target__

  The target that Xcode uses when you build the project. See also [string atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe2dm).

- __active window__

  A window that applies to the user’s current task. Active windows are distinguished from inactive windows by the look of the title bar and the window controls. The active window is typically the frontmost non-floating window, but multiple windows can be active simultaneously. See also [key window](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgeytg), [main window](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4ti).

- __adaptor layer__

  In WebObjects, a sublayer of the access layer that provides classes that communicate directly with data sources.

- __adaptor__

  (1) For databases, a mechanism that connects your application to a particular database server. For each type of server you use, you need a separate adaptor. WebObjects provides an adaptor for databases conforming to JDBC. (2) In WebObjects, a process (or a part of one) that connects WebObjects applications to an HTTP server.

- __ADC__

  (1) Apple Developer Connection. The primary source for technical and business resources and information for anyone developing for Apple’s software and hardware platforms anywhere in the world. It includes programs, products, and services and a website filled with up-to-date technical documentation for existing and emerging Apple technologies. (2) Analog-to-digital converter. Circuitry that converts analog signals to corresponding digital code using sampling and quantization. ADCs are characterized by sample rate, amplitude resolution in terms of bit depth, quantization error and other distortion characteristics, and noise floor. Professional audio work usually employs ADCs with a linear response. Compare [DAC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq3te). See also [quantization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyydi), [sample](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg42ta).

- __addition model__

  A model for extending a continuous selection using Shift-click, in which new text is added to a selection. Compare [fixed-point model](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg43tk).

- __Address Book__

  A technology for managing names, addresses, phone numbers, and other contact-related information. OS X provides the Address Book application for users to manage contact data. It also provides the Address Book framework so that applications can programmatically manage the data.

- __address space__

  The virtual address ranges available to a given task (the task may be the kernel). In OS X, processes do not share the same address space. The address spaces of multiple processes can, however, point to the same physical address ranges. This is referred to as shared memory.

- __admin group__

  A group with special administrative privileges. For example, only members of the `admin` group can open locked system preferences or install software. See also [wheel group](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2tm).

- __administrator__

  A user in the admin group. The user who installs OS X is automatically assigned to the admin group. An administrator has fewer privileges than root, but more privileges than a normal user. An administrator cannot create, delete, or move files in the system domain.

- __ADPCM__

  Adaptive delta pulse code modulation. A variant of [pulse-code modulation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4to), and an extension of [DPCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyytm), that varies quantization step size to minimize bit rate for a given dynamic range.

- __advance delta__

  The distance between the end of one glyph’s advance and the next glyph’s real position.

- __advance height__

  The distance from the top of a glyph to the bottom of the glyph, including the top-side bearing and bottom-side bearing.

- __advance width__

  The full horizontal width of a glyph as measured from its origin to the origin of the next glyph on the line, including the side bearings on both sides.

- __AES__

  Audio Engineering Society. An international society of audio professionals that has established many important standards related to digital audio.

- __AES-3__

  A digital audio transport standard defined by the Audio Engineering Society, originally published in 1992. Also called the _AES/EBU interface_. Equivalent to IEC 60958 Part 4. The AES-3 standard includes parts for various physical connections including balanced twisted-pair wire, unbalanced coaxial cable, and optical fiber. The technical inspiration for AES-3 was the [S/PDIF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4ts) standard.

- __AES encryption__

  Advanced Encryption Standard encryption. A Federal Information Processing Standard (FIPS), described in FIPS publication 197. AES has been adopted by the US government for the protection of sensitive, nonclassified information. The algorithm was developed by Dr. Joan Daemen and Dr. Vincent Rijmen and was named the Rijndael algorithm. It is a symmetric-key algorithm that can use key sizes of 128, 192, or 256 bits. Apple has adopted the 128-bit version of AES for FileVault. There are approximately 3.4 x 10\*\*38 possible 128-bit keys.

- __AES/EBU interface__

  An alternate name for [AES-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga2ta). See also [EBU](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy2ti).

-  __`'aete'` resource__

  A resource that serves as the traditional mechanism for providing scriptability information in a Carbon application. An `'aete'` resource can also be included in a Cocoa application to control how scriptability information is displayed in a dictionary viewer, by applications such as Script Editor and Xcode. Starting in OS X version 10.4, it is not needed for this purpose, for applications that supply their scriptability information in the sdef format.

- __AFP__

  Apple Filing Protocol. A file-sharing protocol, used by AppleShare servers and clients.

- __aggregate device__

  A set of two or more audio devices interconnected to allow the set to be addressed by software applications as a single device. See also [device](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqguztk).

- __aggregate target__

  In Xcode, a combination of targets, not necessarily dependent on each other, that does not produce a product or contain build rules or information property list entries. An aggregate target exists so that you can make it dependent on other targets. The build system builds the targets that the aggregate target depends on sequentially or in parallel.

- __AGL framework__

  Apple Graphics Library framework. The Apple framework for using OpenGL graphics in Mac apps written in the Carbon environment.

- __AIAT__

  Apple Information Access Toolkit. In Classic Mac OS, an object-oriented information access engine that contained a collection of tools for indexing, searching, and analyzing large volumes of documents. Search Kit is the OS X implementation of the AIAT. AIAT was formerly known by its code name V-Twin.

- __AIFC__

  Audio Interchange File Format Extension for Compression. An extension of AIFF that supports storage of either compressed or uncompressed audio data. May also be abbreviated as _AIFF-C_. With the availability of newer audio compression schemes such as MP3 and AAC, AIFC is rarely used. It is still supported in OS X.

- __AIFF__

  Audio Interchange File Format. A digital audio file format developed by Apple, Inc., based on the Interchange File Format (IFF) developed by Electronic Arts, Inc. The audio data in an AIFF file is uncompressed, big-endian PCM and is stored in chunks. See also [synchronous](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4di), [linear PCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge2to).

- __alert__

  A dialog that appears when the system or an application needs to communicate information to the user. Alerts provide messages about error conditions and warn users about potentially hazardous situations or actions.

- __algorithm__

  A sequence of actions to accomplish some task. In cryptography, refers to a sequence of actions, usually mathematical calculations, performed on data to encrypt or decrypt it.

- __alias__

  A lightweight reference to files and folders in Mac OS Standard (HFS) and Mac OS Extended (HFS+) file systems. An alias allows multiple references to files and folders without requiring multiple copies of these items. Aliases are not as fragile as symbolic links because they identify the volume and location on disk of a referenced file or folder; the file or folder can be moved around without breaking the alias. See also [symbolic link](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe3ts).

- __aliased__

  Said of graphics whose edges appear jagged; can be remedied by performing anti-aliasing operations.

- __aliasing__

  The introduction of distortions or artifacts into digital information during processing operations. In graphics, aliasing can cause edges to appear jagged. In audio, aliasing results in artifacts below the [Nyquist frequency](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmztq), sometimes called _aliasing distortion_. To avoid aliasing, audio signals must be low-pass filtered to remove energy at or above the Nyquist frequency before sampling. Anti-aliasing operations can be performed to prevent or mitigate the results of aliasing. See [anti-aliasing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga4da).

- __alignment__

  The horizontal placement of lines of text with respect to the left and right edges of the text area. Alignment can be left, right, centered, or justified (flush on both left and right edges).

- __alpha__

  The graphics state parameter that Quartz uses to determine how to composite newly painted objects to the existing page. At full intensity (alpha =`1.0` ), newly painted objects are opaque. At zero intensity, newly painted objects are invisible (alpha =`0.0` ).

- __alpha channel__

  A channel dedicated to representing how opaque a given pixel is. Unlike the red, green, and blue channels, which specify the intensity of their respective colors, the alpha channel specifies the opacity of the entire pixel. For example, if a pixel was defined using `float` values ranging from 0.0 to 1.0, an alpha channel intensity of `1.0` would indicate 100% opacity, and an intensity of `0.0` would indicate 0% opacity, or transparent.

- __alternate track__

  A movie track that contains alternate data for another track. QuickTime chooses one track to be used when the movie is played. The choice may be based on such considerations as image quality or localization. See also [track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgeydi).

- __Anatomical Transfer Function__

  See [HRTF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqheydc).

- __anchor__

  For documentation sets, a location within an HTML file. When loading the documentation node’s landing page, Xcode scrolls to the location of this anchor. See also [documentation node](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyydq).

- __anchor certificate__

  A digital certificate trusted to be valid, which can then be used to verify other certificates. Anchor certificates can include [root certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4zdi)s, cross certified certificates (that is, certificates signed with more than one [certificate chain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4dc)), and locally defined sources of trust.

- __anchor point__

  The point at which the user presses the mouse button to begin selecting a range of text or other items by dragging through them. The anchor point is at one corner of the range of objects. Compare [active end](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgazta).

- __angle__

  In DVD-Video, a specific view of a scene, usually recorded from a certain camera angle. Different angles can be chosen while viewing the scene.

- __angled caret__

  A caret whose angle in relation to the baseline of the display text is equivalent to the slant of the glyphs making up the text.

- __animation__

  A visual technique that provides the illusion of motion by displaying a collection of images in rapid sequence.

- __animation proxy__

  An object that stands in for another object and provides animation capabilities without significantly impacting the original object’s API.

- __anonymous memory__

  Virtual memory backed by the default pager to swap files, rather than by a persistent object. Anonymous memory is zero-initialized and exists only for the life of the task. See also [default pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqguytc), [task](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgayti).

- __anti-aliasing__

  A technique that smoothes the roughness in images or sound caused by aliasing. During frequency sampling, aliasing generates a false (alias) frequency along with the correct one. With images this produces a stair-step effect. Anti-aliasing corrects this by adjusting pixel positions or setting pixel intensities so that there is a more gradual transition between pixels.

- __API__

  Application programming interface. A set of classes, protocols, methods, functions, and data structures that define the interface (calling convention) by which an application program accesses a service. This service may be provided by the operating system, by libraries, or by other parts of the application.

- __API reference search__

  A search type that looks through the available reference for a symbol name.

- __API-based adaptor__

  An HTTP adaptor based on a programming interface specific to a particular web server. It allows CGI-like tasks to run as part of the main server process, avoiding the creation and termination of a process for each request.

- __AppKit__

  A Cocoa framework that implements an application’s user interface. The AppKit provides a basic program structure for applications that draw on the screen and respond to events.

- __AppKit framework__

  Defines classes to support a graphical, event-driven user interface for applications. See also Cocoa framework.

- __Apple Core Audio Format__

  See [CAF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3de).

- __Apple Developer Connection__

  See [user focus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4dk).

- __Apple event__

  A high-level operating-system event that conforms to the Apple Event Interprocess Messaging Protocol (AEIMP). An Apple event typically consists of a message from an application to itself or to another application.

- __Apple Event Manager__

  The OS X API for creating and sending Apple events, and for receiving, extracting information from, and responding to them.

- __Apple event translator__

  A part of Cocoa scripting that uses scriptability information supplied by an application to evaluate an Apple event received by the application. In many cases, an Apple event is translated into a script command object that performs the action specified by the event.

- __Apple Help__

  The component that enables applications to display HTML files in Help Viewer, a simple browser.

- __Apple Information Access Toolkit (AIAT)__

  In Classic Mac OS, an object-oriented information access engine that contained a collection of tools for indexing, searching, and analyzing large volumes of documents. Search Kit is the OS X implementation of the AIAT. AIAT was formerly known by its code name V-Twin.

- __Apple Lossless__

  A compressed, lossless digital audio encoding format defined by Apple, Inc. See also [lossless compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4de).

- __Apple menu__

  A menu that provides items that are available to users at all times, regardless of which application is active. It is the leftmost menu in the menu bar.

- __Apple Public Source License__

  Apple’s Open Source license, available at [http://www.apple.com/publicsource](http://www.apple.com/publicsource). Darwin is distributed under this license. See also [open source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm3dm).

- __apple_ref__

  An informal name for a token identifier that uses the prefix `//apple_ref.` See also [token identifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga4tc).

- __AppleScript__

  A scripting language that makes possible direct control of scriptable applications and scriptable parts of OS X.

- __AppleScript command__

  A script command provided by AppleScript. AppleScript commands do not have to be included in `tell` statements.

- __AppleScript component__

  The scripting component in OS X that implements the AppleScript scripting language. A scripting component provides services for compiling and executing scripts (and relies on the [relationship key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy3da)).

- __AppleScript Kit__

  A framework that supplies advanced Cocoa scripting support and other features required by AppleScript Studio.

- __AppleScript object__

  A distinct object in an application or its documents that can be specified in a script.

- __AppleScript object class__

  A category for AppleScript objects that share characteristics, such as properties and elements.

- __AppleScript object model__

  A hierarchical structure that, for a given application, specifies the classes of objects a scripter can work with in scripts, the accessible properties of those objects, and the inheritance and containment relationships for those objects.

- __AppleScript script file__

  A file with the extension `.applescript` that contains statements in the AppleScript scripting language.

- __AppleScript Studio__

  A development environment and application framework that combines features from AppleScript, Xcode, Interface Builder, and the Cocoa application framework to provide a sophisticated environment for creating AppleScript Studio applications.

- __AppleScript Studio application__

  A Mac app that combines AppleScript scripts and Cocoa user-interface objects.

- __AppleScript text editor__

  An Xcode pane for editing and compiling AppleScript script files (files with the extension `.applescript` ). The editor relies on the `osacompile` shell tool to compile scripts.

- __AppleTalk__

  A suite of network protocols that is standard on Macintosh computers and can be integrated with other network systems, such as the Internet.

- __application__

  A specific style of program that displays a graphical interface to the user.

- __application bundle__

  A [bundle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi2tc) containing the executable code of an application and its associated resources.

- __application command__

  A command that is defined by a scriptable application to provide access to a scriptable feature. An application command must either be included in a `tell` statement or include the name of the application in its direct parameter.

- __application file__

  A file containing the executable code of an application.

- __application font__

  The font used as the default for user-created content. It is defined by each script system.

- __application host__

  A computer capable of running application instances.

- __application ID__

  A string that identifies an iPhone application or a set of iPhone applications from one vendor. They are similar to bundle identifiers. This is an example application ID: `GFWOTNXFIY.com.mycompany.MyApp` .

- __Application Kit__

  See [AppKit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga4di).

- __application menu__

  A menu that contains items that apply to the application as a whole, rather than to a specific document or other window. The application menu for the current active application appears immediately to the right of the Apple menu.

- __application-modal__

  A window state where the user cannot do anything else within the application until the window is dismissed. Compare [document-modal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4ts), [system modal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4to).

- __application-modal dialog__

  A dialog that prevents the user from performing any operations within the owner application other than those in the dialog. See also [document-modal dialog](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyyda), [sheet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2do), [system modal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4to).

- __application object__

  (1) An object stored in an application or its documents and managed by the application. (2) An object (of the `WOApplication` class) that represents a single instance of a WebObjects application. The application object’s main role is to coordinate the handling of HTTP requests, but it can also maintain application-wide state information.

- __application package__

  A file package containing the code and other resources that make up a Mac app. Application packages make it easy for users to move applications in their file systems. The contents of an application package are visible to users only when they Control-click the package and choose Show Package Contents.

- __application packaging__

  Putting code and resources in the prescribed directory locations inside application bundles. _Application package_ is sometimes used synonymously with _application bundle_.

- __application programming interface__

  See [API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga4dc).

- __application server__

  A JBoss instance, which is started through Server Admin.

- __application window__

  The primary window of an application that is not document-based.

- __Aqua__

  The overall appearance and behavior of Mac apps.

- __Aqua guidelines__

  A set of guidelines that define the appearance and behavior of Mac apps. These guidelines bring a unique look to applications, integrating color, depth, clarity, translucence, and motion to present a vibrant appearance. If you use Cocoa or X11 to create your application’s interface, you get the Aqua appearance automatically.

- __ARB__

  Architecture Review Board. This group oversees the OpenGL specification and extensions to it.

- __arbitrary reference form__

  In AppleScript, a reference form that specifies an arbitrary object in a container.

- __architecture-specific build setting__

  In Xcode, options for specific architectures, such as PowerPC or Intel.

- __arrow keys__

  The four keys on Apple keyboards (up, down, left, right) used to move the insertion point or change the selection. They can also be used with the Shift key to extend or shrink a selection.

- __ascent line__

  An imaginary horizontal line that corresponds approximately to the tops of the uppercase letters in the font. Uppercase letters are chosen because, among the regularly used glyphs in a font, these are generally the tallest.

- __ASCII__

  American Standard Code for Information Interchange. A 7-bit character set (commonly represented using 8 bits) that defines 128 unique character codes. See also [Unicode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2te).

- __aspect ratio__

  The width-to-height ratio of an image. For example, a 4:3 aspect ratio means the horizontal size is a third again wider than the vertical size. Every title on a DVD is authored for one of two aspect ratios: standard (4:3) or wide (16:9).

- __assignment statement__

  An AppleScript statement that assigns a value to a variable. Assignment statements use the `copy` or `set` commands.

- __asymmetric keys__

  A pair of related but dissimilar keys, one used for encrypting and the other used for decrypting a message or other data. See also [public key cryptography](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4ti). Compare [symmetric keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4da).

- __asynchronous__

  (1) In Audio Queue Services, describes one of two ways to stop an audio queue. Asynchronous stopping happens after all queued buffers have been played or recorded. (2) In digital communications, a transmission method that does not require the clock frequency of the sender and receiver to be the same. Compare [synchronous](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4di).

- __asynchronous design approach__

  The principle of organizing an application around blocks of code that can be run concurrently with an application’s main thread or other threads of execution. Asynchronous tasks are started by one thread but actually run on a different thread, taking advantage of additional processor resources to finish their work more quickly.

- __asynchronous launch__

  A [launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgezdk) operation in which control returns immediately to the calling program, without waiting for the launched application to complete its [launch sequence](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgezdo). Compare [synchronous launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4dk).

- __asynchronous progress indicator__

  A small round indeterminate progress indicator. It is usually visible only while active.

- __ATF__

  Anatomical Transfer Function. See [HRTF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqheydc).

- __atom__

  The basic unit of data in a movie resource, sprite, or other QuickTime data structure. There are a number of different atom types, including movie atoms, track atoms, and media atoms. There are two varieties of atoms: QT atoms, which may contain other atoms, and classic atoms, which do not contain any other atoms. See also [classic atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmzdi), [movie resource](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3tc), [QT atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyyda), [sprite](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhezda).

- __atom container__

  A tree-structured hierarchy of QT atoms. See also [QT atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyyda).

- __atom ID__

  A 32-bit integer that uniquely identifies an atom among other child atoms of the same parent atom. The root atom has an atom ID value of 0x0001. See also [child atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmyte), [parent atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqzdk), [root atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4zdg).

- __atom type__

  A 32-bit value that uniquely identifies the data type of an atom. It is normally an `OSType` value, rendered by four ASCII characters. An atom’s data type helps determine how the atom’s contents are interpreted.

- __ATSUI__

  Apple Type Services for Unicode Imaging. A technology that enables the rendering of Unicode-encoded text with advanced typographic features. ATSUI automatically handles many of the complexities inherent in text layout, including how to correctly render text in bidirectional and vertical script systems.

- __ATSUI style mask__

  A byte-length mask with one bit set for each ATSUI-supported style to be applied.

- __attach__

  In OpenGL, an operation that establishes a connection between two existing objects. Compare [bind](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgiyde).

- __attached editor__

  A text editor pane in the Xcode Project window.

- __attaching__

  The process of starting a debugging session on a process that’s already running and was not launched by Xcode.

- __attachment__

  A Core Foundation object associated with a video frame. This attachment, specified by a key-value pair, can hold any sort of information relevant to the frame, such as a timestamp.

- __attribute__

  (1) In key-value coding, a property that is a simple value, such as a scalar, string, or Boolean value, or to immutable objects such as `NSColor` and `NSNumber` objects. (2) In AppleScript, one of the two main descriptor data types that make up an Apple event. Not commonly used by scriptable Cocoa applications. (3) In an XML file, a name-value pair that specifies a single property for an element. (4) In Keychain Services, One data item, such as the name, type, date modified, account number, and so on, for a keychain item, other than the [secret](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayta). The attributes associated with a keychain item depend on the class of the item. (5) In Entity-Relationship modeling, an identifiable characteristic of an entity. For example, `lastName` can be an attribute of an Employee entity. An attribute typically corresponds to a column in a database table. See also [entity](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy4dk), [session](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhazte).

- __audio file stream__

  In Core Audio, a software object of type `AudioFileStreamID`, which represents data obtained from a TCP stream and supports manipulation of that data. See also [TCP/IP](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgaytk).

- __audio processing graph__

  A representation of a signal chain comprising an interconnection of audio units. Also called an _AUGraph_ or _graph_. Core Audio represents such an interconnected network as a software object of type `AUGraph`. Audio processing graphs must end in an [output unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm4dm). See also [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq).

- __audio queue__

  In Audio Queue Services, a software object of type `AudioQueueRef`, used for recording or playing back audio. There are two distinct types of audio queue. A recording audio queue (sometimes called an _input audio queue_) typically accepts incoming audio from a hardware device and uses a callback function on its output side. A playback audio queue (sometimes called _an output audio queue_) has a callback on its input side, and typically sends its output audio to external hardware.

- __audio queue buffer__

  In Audio Queue Services, a data structure used as a container for transient blocks of audio data being played or recorded. An audio queue buffer is managed by the [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2ti) that owns it.

- __audio session__

  An iOS software abstraction that represents audio behavior for an application, in context, on an iPhone or iPod touch. An audio session has a [category](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3tc) and can be [active](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgazdo) or [inactive](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe2to).

- __audio session category__

  See [category](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3tc).

- __audio unit__

  A Component Manager–based [Simulator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha3da) that adds an audio feature to a Mac app. Audio units can provide effects such as filtering and reverb, MIDI-based music synthesis, audio data format conversions, mixing, panning, sound generation, and audio playback. Unlike application-specific plug-ins, audio units are available systemwide. Multiple instances of a single audio unit can run simultaneously.

- __AUGraph__

  See [audio processing graph](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tg).

- __AUHAL__

  An Apple-supplied [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) used to interface with hardware input or output, so named because it interacts with the [HAL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqha3dg) (Hardware Abstraction Layer).

- __authentication__

  The act of verifying identity with something the user has, knows, or is. For example, a user knows information such as a name and password. The user may have something physical such as a smart card. The identity can be something the user is—a physical feature such as a fingerprint or retinal scan. Authentication may require two or more forms of identification. Compare [authorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3di), [identification](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqheyts).

- __authentication server__

  A server that has access to a store of authentication information and that can authenticate users. For example, an authentication server might verify a user’s identity by prompting the user for a name and password and comparing that information to the names and passwords in a database. In Kerberos authentication, the authentication server also looks up the user’s [private key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu2di), generates a [session key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhaztg), and creates a [TGT](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2to). See also [ticket-granting server](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3dk).

- __authorization__

  The process by which an entity such as a user or a server gets the right to perform a [privileged operation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu2dm). (Authorization can also refer to the right itself, as in “Bob has the authorization to run that program.”) Authorization usually involves first authenticating the entity and then determining whether it has the appropriate [permissions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2tc). Compare [authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3de).

- __authorization option__

  A parameter or field that instructs the Security Server how to proceed with a request. Options include requesting preauthorization, requesting partial authorization, appending rights, and interacting with the user.

- __authorization reference__

  A reference used by the Security Server to access an authorization session associated with a process.

- __Authorization Services__

  An OS X API that facilitates fine-grain control of privileged operations, such as accessing restricted areas of the operating system and self-restricted parts of your Mac app. The Security Server uses policy-based decisions to authorize rights for users.

- __authorization tag__

  A data field in an access control list ([ACL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgazdc)) that specifies an operation that can be done with that keychain item, such as decrypting or authenticating.

- __auto-key event__

  An event indicating the user has held a key down for a certain amount of time.

- __automatic guide__

  An alignment tool that shows the spacing required to meet the appropriate interface guidelines for the target platform. This type of guide appears and disappears automatically.

- __Automator action__

  A loadable bundle that performs discrete tasks that users can link together in a workflow using the Automator application.

- __auto-repeat__

  A feature that lets users produce numerous instances of the same character by holding down its key rather than pressing the key over and over. Users can make adjustments to this feature in Keyboard & Mouse preferences.

- __autosizing behavior__

  In Interface Builder, a mechanism that automatically adjusts the size and position of views during resize operations based on a set of options. See also [spring](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrheyts), [strut](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe2ta).

- __AV/C__

  Audio/Video Control. A standard, published by the [IEEE](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhezdo), that provides a music and audio device command protocol over [FireWire](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg43tc) (IEEE 1394) connections.

- __average bit rate__

  Describes an encoded audio representation that, while allowing variations in bit rate from frame to frame, maintains a specific average bit rate over a long time interval (typically between 10 and 60 seconds). You can use ABR-savvy encoders to fit a recording into a predetermined file size. Compare [constant bit rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgqydc), [variable bit rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4ts).

- __AVI__

  Audio Video Interleave. A chunk-based, container file format defined by Microsoft Corporation in 1992. AVI is a specialization of the [RIFF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4yta) format, which in turn is based on [IFF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhezta).

- __axial gradient__

  A fill that varies along an axis between two defined end points. All points that lie on a line perpendicular to the axis have the same color value. Also called a _linear gradient_.

- __azimuth__

  In [surround sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe3tm) and [immersive audio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe2te), the real or apparent horizontal angle of an audio source referenced to a line drawn from the listener’s head to a point directly ahead of the listener.

- __background__

  The part of a glyph bitmap that surrounds the pixels that constitute the glyph itself.

- __background color__

  The color of the background behind a sprite or other image.

- __background selection__

  A selection in an inactive window. In Aqua, such selections are in the secondary highlight color.

- __backing store__

  A file in which the Virtual Memory Manager stores the contents of unneeded pages of memory.

- __backtrace__

  A list of the handlers that have been invoked at any point in a script execution. Each handler is listed as a call frame.

- __band__

  A horizontal strip from an image. For raster printing, the image corresponding to the page raster is broken into strips of manageable size.

- __bandwidth__

  (1) In analog audio, the width of a frequency band for a [transmission channel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgezdm), from a lower to an upper frequency limit. The limits are defined in terms of signal attenuation, in decibels, relative to the level at the center of the band. See also [decibel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq4tq). (2) In digital data transmission, the available data throughput for a transmission channel. Digital bandwidth is typically expressed in terms of bits or bytes per second. See also [bit rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgiyte).

- __base class__

  In C++, the class from which another class (a subclass) inherits. It can also be used to specify a class from which all classes in a hierarchy ultimately derive (also known as a _root class_).

- __baseline__

  An imaginary horizontal line that coincides with the bottom of each character in a font, excluding descenders (tails on letters such as _p_).

- __baseline delta__

  The distance (in points) between a baseline and y = 0; sometimes referred to as delta-y. See also [baseline type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge4ds).

- __baseline type__

  The kind of baseline used with a particular kind of text.

- __base SDK__

  A project setting that specifies the default SDK to use when building the project’s targets. Targets can override this setting with the iOS Deployment Target build setting.

- __base URL__

  For documentation sets, an alternate location for documentation nodes whose documentation files reside on the web. The default location is in the installed documentation set bundle or its fallback web location.

- __basic animation__

  A simple animation from a start value to a target value.

- __batch faulting__

  An feature that allows you to reduce round trips to the database by firing multiple faults in a single fetch. See also [faulting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4ztk).

- __beat__

  The basic time unit of a musical piece; typically, the bottom number in a time signature. Core Audio’s [music player](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi4te) uses the notion of beats in the tempo track.

- __best size__

  The optimum size for displaying the contents of a window.

- __bevel button__

  A button with a beveled edge that gives the button a three-dimensional appearance.

- __Bézier curve__

  A cubic equation originally developed by Pierre Bézier. In typography, used to define the shape of a glyph.

- __bidi__

  See [bidirectional script system](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge4ts).

- __bidirectional script system__

  A script system in which text is generally right-aligned with most characters written from right to left, but with some left-to-right text as well. Arabic and Hebrew are bidirectional script systems.

- __bidirectional text__

  The combination of text with both left-to-right and right-to-left directions within a single line of text.

- __binary operator__

  An operator that derives a new value from a pair of values.

- __bind__

  An operation that creates a new object and then establishes a connection between that object and a rendering context.

- __binding__

  A two-way connection between the objects of a data model and the views of a user interface. Cocoa bindings provide automatic synchronization between data objects and the views displaying information about those objects.

- __binding information__

  The information maintained in the [Launch Services database](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgezds) about the kinds of documents and URLs an application is capable of opening.

- __binding preference__

  A preference set by the user specifying the application in which to open a given document or URL.

- __binding rules__

  The rules used by Launch Services to determine an item’s default application according to the binding information in the [Launch Services database](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgezds).

- __biometric identifier__

  A measurement of biological matter used for identification—for example, fingerprints, retinal scans, and face recognition.

- __bit depth__

  The number of bits used to describe something, such as an audio sample or the color of a pixel. Each additional bit in a binary number doubles the number of possibilities. For audio samples, bit depth along with some other factors, determines the [dynamic range](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy2ta) of a digital system.

- __bitmap__

  (1) A rectangular array (or raster) of pixels, each pixel representing a point in an image. Bitmap images are also called _sampled images_. (2) A data structure that represents the positions and states of a corresponding set of pixels.

- __bitmap graphics context__

  A bit-based offscreen drawing destination.

- __bitplane__

  A rectangular array of pixels.

- __bit rate__

  The data rate (or [bandwidth](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge4dk)) of a digital channel, in bits per second.

- __blend mode__

  The way Quartz combines the foreground painting with the background painting.

- __blit__

  Slang for copying an image from memory to the screen.

- __blitting__

  The process of moving bits from a back buffer to an onscreen location. Blitting is not necessary (not recommended) when using Quartz.

- __blocked__

  The state where an application or thread is waiting for some event or action to occur. While blocked, that particular code path uses no processor time.

- __block object__

  A C construct for encapsulating inline code and data so that it can be performed later. You use blocks to encapsulate tasks you want to perform, either inline in the current thread or on a separate thread using a dispatch queue.

- __bold text__

  The font style that Xcode uses in panes of Project and Target Info windows to indicate build settings specified at the current level. Build settings that are not in bold text are specified at lower layers.

- __BOM__

  Bill of materials. A file in an installer package used by the Installer to determine which files to install, remove, or upgrade. It contains all the files within a directory, along with information about each file such as the file’s permissions, its owner and group, size, its time of last modification, a checksum for each file, and information about hard links.

- __Bonjour__

  Apple’s technology for zero-configuration networking. Bonjour enables dynamic discovery of services over a network.

- __bookmark__

  A data object that specifies the current media position during playback of a DVD. Because the byte length of a bookmark is known, you can save the bookmark in a file for later use.

- __boolean__

  A logical truth value.

- __Boolean expression__

  An expression whose value can be either true or false.

- __Boolean searching__

  Matching of a query string to indexed terms using Boolean (logical) operators such as `AND` and `OR` between query terms, optionally employing grouping for precedence using parentheses. The entire query expression is matched. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayde).

- __bottomline input__

  A type of input method in which the user enters text in a small window, called a _floating input window_, that appears near the bottom of the screen. Compare [inline input](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe4do).

- __bottom-side bearing__

  The white space between the bottom of the glyph and the visible ending of the glyph.

- __bounding box__

  The smallest rectangle that entirely encloses the pixels or outline of a glyph.

- __breakpoint action__

  In Xcode, an action to perform when a program reaches a certain point in its execution, such as logging output to the console. The default breakpoint action is to pause program execution.

- __browse mode__

  In Xcode, a mode of the Documentation window in which you can traverse a hierarchy of categories in a documentation set until you get to a list of documents. Compare [search mode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhaydk).

- __browser view__

  The part of the Documentation window that displays the documentation category hierarchy.

- __BSD__

  Berkeley Software Distribution. Formerly known as the Berkeley version of UNIX, BSD is now simply called the BSD operating system. The BSD portion of Darwin is based on 4.4BSD Lite 2 and FreeBSD, a flavor of 4.4BSD.

- __buffer__

  A block of memory dedicated to storing a specific kind of data. For example, Core Audio uses buffers to supply audio to, and receive audio from, audio units. In graphics, a buffer stores data such as depth values and color index values.

- __buffer pool__

  A collection of preallocated buffers that can be used over and over. Keeping a pool of buffers available requires less overhead than allocating and deallocating a buffer each time it is needed.

- __buffer queue__

  In Audio Queue Services, an ordered list of audio queue buffers used by an audio queue. See also [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2ti), [audio queue buffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tk).

- __buffered window__

  A window with a memory buffer into which all drawing is rendered. All graphics are first drawn in the buffer, and then the buffer is flushed to the screen.

- __build__

  The process Xcode uses to create a target.

- __build client__

  The computer that performs a build operation. This is the computer that runs the Xcode or the `xcodebuild` instance that carries out the build command.

- __build configuration__

  A named set of build settings that tells Xcode how to build a product. The typical build configurations are Debug and Release, but you can define additional build configurations. See also [build setting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi2dk).

- __build configuration file__

  A file that contains Xcode build setting definitions. You can use it to share a set of build setting definitions among all the individuals working on a team. You can also use a configuration file to quickly configure targets and projects with common build setting definitions.

- __build directory__

  The file-system directory in which Xcode stores built products. It is usually the build folder in the project folder.

- __Build pane__

  The pane in the Xcode Project and Target info windows that lets you view and edit build settings at the target and project levels.

- __build phase__

  In Xcode, a set of operations performed on a group of files as part of building a product.

- __Build Results window__

  A view that displays a detailed account of the progress of a build, including each step of the build process and the full output of the build system. It can take you directly to the source of any errors or warnings.

- __build server__

  A computer that a build host uses to perform compilation tasks. Build servers do not need to run Xcode or `xcodebuild` to aid a build host, but they must at least be running the same version of the Mac OS as the build server.

- __build set__

  In Xcode, the host names of build servers to which a build client distributes compilation tasks. To distribute a build, you must define at least one build set on the build client, or use the Bonjour set when available.

- __build setting__

  In Xcode, a variable that contains the information for building a product. For each operation performed in the build process—such as compiling Objective-C source files—build settings control how that operation is performed.

- __build setting name__

  In Xcode, a label that identifies a build setting. It is similar to the names of environment variables in a command shell.

- __build setting specification__

  The information Xcode uses to determine the value of a build setting at build time.

- __build setting title__

  The label used to display the build setting in the Xcode user interface.

- __build style__

  A methodology of creating a product from a target in Xcode. Development and Deployment build styles use different methodologies.

- __bullet__

  In the Window menu, indicates that the document has unsaved changes.

- __bundle__

  A directory in the file system that typically stores executable code and the software resources related to that code. Applications, plug-ins, frameworks, and kernel extensions are types of bundles. Except for frameworks, bundles are file packages, presented by the Finder as a single file instead of a folder. See also [kernel extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4di).

- __bundle identifier__

  A unique identifying string used to locate an application’s bundle at runtime.

- __bundle information property list__

  A collection of key-value pairs giving information about an application, stored in a file named `Info.plist` in its application bundle.

- __bus__

  A transmission path on which signals can be dropped off or picked up by devices attached to it. Only devices addressed by the signals pay attention to them; the others discard the signals. Buses exist both within the CPU and connect it to physical memory and peripheral devices. Examples of I/O buses on Darwin are PCI, SCSI, USB, and FireWire. For its meaning in Core Audio, see [element](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy3dm).

- __bus master__

  A program, usually in a separate I/O controller, that directs traffic on the computer bus or input/output paths. The bus master actually controls the bus paths on which the address and control signals flow. DMA is a simple form of bus mastering where the bus master controls I/O transfers between a device and system memory and then signals to the CPU when it has done so. See also [DMA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4tg).

- __business logic__

  The rules associated with the data in a database that typically encode business policies. An example is automatically adding late fees for overdue items.

- __button__

  See [bevel button](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge4tm), [icon button](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqheytk), [push button](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4tq), [radio button](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyzdc).

- __bytecode__

  Computer object code that is processed by a virtual machine. The virtual machine converts generalized machine instructions into specific machine instructions (instructions that a computer’s processor can understand). Bytecode is the result of compiling source language statements written in any language that supports this approach. The best-known language today that uses the bytecode and virtual machine approach is Java. In Java, bytecode is contained in a binary file with a `.class` suffix. (Strictly speaking, “bytecode” means that the individual instructions are one byte long, as opposed to PowerPC code, for example, which is four bytes long.) See also [VM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizds).

- __byte offset__

  The indexed position of a 2-byte Unicode character in a text buffer, starting at zero for the first character. Sequential values for character offset correspond to the storage order of the characters. Compare [edge offset](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy2tm).

- __CA__

  [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2tg). In order for a digital certificate to be trusted, the certification authority must be a trusted organization that authenticates an applicant before issuing a certificate.

- __cache__

  A special type of memory that is substantially faster than typical main memory (RAM). When a program asks the CPU to read or write data in memory, it first checks to see whether this data is stored in cache memory (because it will be faster to retrieve or write). Cache sizes are usually quite small though, (under 2 MB) so in order to make use of it, the data must be small enough to fit in the cache.

- __CAF__

  Core Audio Format. Apple’s universal audio file format. CAF files are chunk-based and can contain AAC, MP3, and PCM audio data, among many other audio data formats, as well as MIDI data. See also [chunk](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmytm), [PCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2de).

- __call frame__

  The information about a handler call, including its calling parameters and local variables.

- __call stack__

  A collection of stack frames that positions the most recent calls on the top of the stack.

- __Carbon__

  An OS X application environment that uses procedural programming interfaces derived from earlier versions of the Mac OS.

- __Carbon Printing Manager__

  A collection of system software routines that can be used by a Carbon application. It replaces the Mac OS 9 [Printing Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrguztk).

- __caret__

  A vertical or slanted blinking bar, appearing at the caret position in the display text, that marks the point at which text is to be insert or deleted. See also [split caret](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrheyti).

- __caret angle__

  The angle of a caret or of the edges of a highlight. The caret angle can be perpendicular to the baseline or parallel to the angle of the style run’s text.

- __caret position__

  A location onscreen, typically between glyphs, that relates directly to the offset (in memory) of the current text insertion point in the source text. At the boundary between a right-to-left and left-to-right direction run on a line, one character offset may correspond to two caret positions, and one caret position may correspond to two offsets.

- __caret type__

  A designation of the behavior of the caret at direction boundaries in text. See also [dual caret](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyzti).

- __category__

  Also called _audio session category_. In iOS, a collection of audio behaviors for an application. For example, a category specifies whether an application intends to mix its audio with other applications or silence them. You specify your application’s category after initializing its audio session.

- __CBR__

  Constant bit rate. A data encoding scheme that can be used to stream audio data over a channel at a constant bit rate while supporting real-time decoding. In most cases, packet size is constant in CBR streams. In the case of constant bit rate AAC streams, packet size may vary slightly. Some encoding schemes, such as PCM, support only CBR encoding. Compare [average bit rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3tk), [variable bit rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4ts). See also [simple message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2tk).

- __CDSA__

  Common Data Security Architecture. An open software standard for a security infrastructure that provides a wide array of security services, including fine-grained access permissions, authentication of users, encryption, and secure data storage. CDSA has a standard application programming interface, called [CSSM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq2ti). In addition, OS X includes its own security APIs that call the CDSA API for you. See also [CDSA plug-in](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3ti).

- __CDSA plug-in__

  A software module that connects to [CDSA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3tg) through a standard interface and that implements or extends CDSA security services for a particular operating system and hardware environment.

- __ceiling__

  The maximum allowable signal level in an audio system. The ratio of the ceiling to the [noise floor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmzdc) is the [dynamic range](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy2ta). Also called _dynamic ceiling_.

- __center equalization__

  Placement of controls in a window so that overall, they are visually balanced across an imaginary vertical line in the center of the window.

- __center justification__

  The placement of controls or text where every item is centered on an imaginary vertical line in the center of a window.

- __certificate__

  See [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2tg).

- __Certificate Assistant__

  A utility available through the Keychain Access Utility that can be used to create certificates and keys, request certificates from a certificate authority, and evaluate certificates.

- __certificate authority__

  See [CA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3da).

- __certificate chain__

  A sequence of related [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2tg)s that are used to verify the validity of a digital certificate. Each certificate is digitally signed using the certificate of its certification authority ( [CA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3da)). This creates a chain of certificates ending in an [anchor certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga3tg).

- __certificate extension__

  A data field in a [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2tg) containing information such as allowable uses for the certificate.

- __certificate signing request__

  See [source text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4tm).

- __certificate subject__

  The entity associated with the public key that is in the certificate.

- __Certificate, Key, and Trust Services__

  An API you can use to create, manage, and read certificates; add certificates to a keychain; create encryption keys; and manage trust policies. In iOS, you can also use this API to encrypt, decrypt, and sign data.

- __certification authority__

  See [CA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3da).

- __CFHTTP__

  An API that you can use to create, serialize, deserialize, and manage HTTP protocol messages, including secure HTTPS messages. This component lets you add authentication information to a message. CFHTTP is a component of [CFNetwork](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4ta) and is built on top of [CFStream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4tc).

- __CFM__

  Code Fragment Manager. The library manager and code loader for processes based on PEF (Preferred Executable Format) object files (in Carbon).

- __CFNetServices__

  An API that allows you to use Bonjour. Bonjour enables applications to discover services that are available on the network and find all access information (such as name and IP address) needed to use each service. CFNetServices is a component of [CFNetwork](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4ta). This component has no security features.

- __CFNetwork__

  A high-level API used for creating, sending, and receiving serialized messages over a network. CFNetwork is built on top of [Secure Transport](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayti), and so can use the [Secure Transport](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayti) and [TLS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga4do) secure networking protocols.

- __CFStream__

  An API that creates and manages the read and write streams that [CFHTTP](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4do) depends on. CFStream is a component of [CFNetwork](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4ta) and is built on top of [Secure Transport](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayti). You can specify a [SSL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhezdi) or [TLS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga4do) protocol version to encrypt and decrypt the data stream.

- __CFString__

  An object that represents an array of Unicode characters ( `UniChar` ) along with a count of the number of characters. Unicode-based strings in Core Foundation provide a solid basis for internationalizing the software you develop. Unicode makes it possible to develop and localize a single version of an application for users who speak most of the world’s written languages, including Russian (Cyrillic), Arabic, Chinese, and Japanese. Although conceptually CFString objects store strings as arrays of Unicode characters, in practice they often store them more efficiently. The memory a CFString object requires is typically about the same or even less than that required by a simple `UniChar` array.

- __CG__

  The prefix used for functions in the Quartz API. See also [Core Graphics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgqztm).

- __CGI__

  Common Gateway Interface. A standard for interfacing external applications with information servers, such as HTTP or web servers.

- __CGI adaptor__

  An HTTP adaptor that uses the Common Gateway Interface (CGI) to translate requests from an web server into requests to an application instance, and responses from an application instance to responses to the web server. The web server creates a CGI process to handle each request.

- __CGLs framework__

  Core OpenGL framework. The Apple framework for using OpenGL graphics in Mac apps (Cocoa or Carbon) that need low-level access to OpenGL.

- __CGLayer__

  An offscreen graphics context, introduced in OS X v10.4, suited for high-quality offscreen rendering of content that you plan to reuse.

- __channel__

  A discrete track of audio. A monaural recording or live performance has exactly one channel. A stereo recording or live performance has two channels. A multitrack recording or performance can have any number of channels. Between audio units, a [connection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm4tk) has one or more channels. See also [channel layout](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmyda).

- __channel layout__

  A description of the playback roles for the channels in an audio recording. For example, in a stereo recording, channel 1 has the role of “left front” and channel 2 has the role of “right front.”

- __chapter__

  (1) In DVD-Video, a division of a title. Technically called a part of title (PTT). (2) A method of organizing different scenes of a movie for easy navigation and access. DVDs are indexed by chapter, similar to the way a CD has a track. DVD players allow you to skip to a particular chapter or scene.

- __chapter list__

  A set of named entry points into a movie, presented to the viewer as a text list.

- __character__

  An atomic unit of content for text data. A character is an abstract entity without any particular appearance; characters include letters, digits, punctuation, and symbols. Compare [character code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmydk), [glyph](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqha2dc).

- __character clusters__

  A collection of characters treated as individual components of a whole, including a principal character plus attachments in memory. For example, in Hebrew, a cluster may be composed of a consonant, a vowel, a dot to soften the pronunciation of the consonant, and a cantillation mark.

- __character code__

  A numerical representation of a character. Each writing system or language has one or more character encodings—tables that relate character codes to the characters they represent.

- __character encoding__

  A conversion table for interpreting a specific character set. See also [text encoding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgaztm).

- __character key__

  A key that sends a character to the computer. Character keys include letters, numbers, punctuation, and the Space bar, and nonprinting characters such as Tab and Return.

- __character rendering__

  The process of preparing characters for display, taking into account line direction, contextual rules, and character reordering. For example, the formation of ligatures and diphthongs occurs during the display of text.

- __checkbox__

  A control for an option that must be either on or off.

- __checkmark__

  In the Window menu, a checkmark appears next to the active document’s name. In other menus, checkmarks can be used to indicate that the setting applies to the entire selection. Checkmarks can be used for mutually exclusive attribute groups or for accumulating attribute groups.

- __chevrons__

  See [double angle brackets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyytg).

- __child atom__

  A QT atom inside a container atom, which is its parent atom. See also [container atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgqydi), [parent atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqzdk), [QT atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyyda).

- __child script object__

  A `script` object that inherits properties and handlers from another object, called the parent.

- __choice requirement__

  In PackageMaker, a test that compares the value of a system property (such as the amount of random-access memory available) with a value. Choice requirements determine the value of a choice’s user-interface properties: selected, actionable, and visible.

- __choice requirement editor__

  The area of a PackageMaker project window that allows packagers to specify a choice requirement (and how it affects the value of the choice’s user-interface properties). See also [choice requirement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmyti).

- __chunk__

  (1) In Core Audio, a linear block of data consisting of a short, descriptive header followed by the described data. A chunk-based file is an on-disk file laid out as a series of chunks. (2) In QuickTime, A collection of sample data in a media structure. Chunks, which may contain one or more samples, allow optimized data access. Chunks in a media structure may have different sizes, and the samples within a chunk may have different sizes.

- __chunk data section__

  The data content of a [synchronous](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4di). The format of the data depends on the chunk type, as specified in the chunk header.

- __chunk header__

  The descriptive, metadata section at the start of a [synchronous](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4di). Each element of information in a chunk header is called a _field_.

- __CIFS__

  Common Internet File System. A file-sharing protocol used widely on Windows and UNIX systems. CIFS is an extension of the [SMB](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha3te) protocol. CIFS has been given to the Internet Engineering Task Force (IETF), making it an Internet standard. Unlike SMB, CIFS runs only over TCP/IP. See also [Samba](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg42ds).

- __ciphertext__

  Text or other data that has been encrypted. Compare [plaintext](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq3tm).

- __claim__

  To declare to Launch Services that an application is capable of opening documents or URLs of a given type.

- __class__

  (1) In object-oriented languages such as Objective-C and Java, a prototype for a particular kind of object. A class definition declares instance variables and defines methods for all members of the class. Objects that belong to the same class have the same types of instance variables and have access to the same methods (included the instance variables and methods inherited from superclasses). (2) In AppleScript, a category for objects that share characteristics such as properties and elements and respond to the same commands.

- __class description__

  A scripting definition file (sdef) entry that describes a scriptable class, including its attributes and relationships and the KVC keys that Cocoa scripting uses to gain access to its values. When the sdef is loaded, the information is stored in an instance of `NSScriptClassDescription` .

- __classic atom__

  A QuickTime atom that contains no other atoms. A classic atom, however, may contain a table. An example of a classic atom is an edit list atom, containing the edit list table. Compare [QT atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyyda).

- __Classic Event Manager__

  The event handling interface used in Mac OS applications before the Carbon Event Manager. The Classic Event Manager often required a certain amount of polling of the event queue.

- __class property__

  In WebObjects, a field in an enterprise object that meets two criteria: It’s based on an attribute in your model, and it can be fetched from the database. Class property can refer either to an attribute or to a relationship.

- __clean__

  In Xcode, to remove all the product files, as well as any object files (`.o` files) or other intermediate files created during the build process.

- __click-through__

  A property of some controls that enables user to activate them in an inactive window. Whether a control supports click-through depends on the context.

- __client__

  (1) A driver object that consumes services of some kind supplied by its provider. In a driver stack, the client in a provider/client relationship is farther away from the Platform Expert. See also [provider](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4di). (2) In source control management, the program a developer uses to interact with the repository.

- __clip__

  Prepackaged “mini” Quartz Composer compositions that you can drag into a composition and customize for your own use.

- __Clipboard__

  A per-user server (also known as the _pasteboard_) that enables the transfer of data between applications, including the Finder. This server is shared by all running applications and contains data that the user has cut or copied, as well as other data that one application wants to transfer to another, such as in dragging operations. Data in the Clipboard is associated with a name that indicates how it is to be used. You implement data-transfer operations with the Clipboard using Core Foundation Pasteboard Services or the Cocoa `NSPasteboard` class. See also [pasteboard](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqztg).

- __clip coordinates__

  In OpenGL, the coordinate system used for view-volume clipping. Clip coordinates are applied after applying the projection matrix and prior to perspective division.

- __clipped movie boundary region__

  The region that combines the union of all track movie boundary regions for a movie, which is the movie’s movie boundary region, with the movie’s movie clipping region, which defines the portion of the movie boundary region that is to be used. See also [movie boundary region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3dg), [movie clipping region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3di).

- __clipping__

  (1) In OS X, data dragged from an application to the Finder desktop. (2) In graphics, the process of defining the boundaries of a graphics area. (3) In audio, distortion of a [waveform](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2dg) resulting from the limiting of signal amplitude to a specific level. See also [distortion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4dm).

- __clipping area__

  A path used to constrain the drawing of other objects within its bounds.

- __clock__

  (1) In Mach, an object used to abstract time. (2) The regular, periodic signal in a digital audio system used to pace audio recording and playback.

- __clock drift__

  In audio, the deviation, over time, of one [system output](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4ts) relative to another, due to differing counting rates. Clock drift interferes with synchronization.

- __clock recovery__

  In audio, extracting and reconstructing timing information from a data stream.

- __close button__

  A window control (the red button that appears in the upper left) that users can click to close the window.

- __CMP__

  Container-managered persistence. An enterprise bean persistence model in which the J2EE container is responsible for persisting enterprise-bean instances to a data store and populating the fields of enterprise-bean instances when they are retrieved.

- __Cocoa__

  An advanced object-oriented development platform in OS X. Cocoa is a set of frameworks used for the rapid development of full-featured applications in the Objective-C language. It is based on the integration of OpenStep, Apple technologies, and Java.

- __Cocoa framework__

  An object-oriented application framework, consisting of a collection of advanced object-oriented APIs. The Cocoa framework is made up of the AppKit and Foundation frameworks. Also referred to simply as_Cocoa_.

- __Cocoa scripting__

  In the Cocoa application framework, the support for creating scriptable applications. Cocoa scripting includes classes, categories, and scriptability information, which together support much of AppleScript’s Standard suite.

- __Cocoa user interface class__

  A class that supports a user interface item. The Application Kit provides many of these classes; for example, NSButton and NSBrowser are Cocoa user interface classes provided by the Application Kit.

- __Cocoa user interface object__

  An instance of a Cocoa user interface class.

- __codec (coder/decoder)__

  A generic term applied to, among other things, lossy and lossless audio compression technologies implemented in hardware or software. Encoded data can be wrapped in a file format appropriate for the data, or decoded from such a file format. For example, the MP3 file format is a wrapper that can hold perceptually encoded audio data.

- __code completion__

  In Xcode, a shortcut that automatically suggests likely completions as you type an identifier or a keyword. The suggestions are based on the text you type and the surrounding context within the file.

- __code focus__

  A feature of the Xcode text editor that highlights the scope of the selected source code.

- __code folding__

  A feature of the Xcode text editor that hides code you don’t want to see.

- __code fragment__

  In the CFM-based architecture, a code fragment is the basic unit for executable code and its static data. All fragments share fundamental properties such as the basic structure and the method of addressing code and data. A fragment can easily access code or data contained in another fragment. In addition, fragments that export items can be shared among multiple clients. A code fragment is structured according to the Preferred Executable Format (PEF).

- __Code Sense__

  In Xcode, a process that maintains an index to a rich store of information about the symbols defined in a project. Xcode uses this information as the basis for a number of features that let you browse the symbols in your project, view the class hierarchy of projects that use an object-oriented programming language, and search your project for symbol definitions.

- __code signing__

  The addition of a [digital signature](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2to) to an application or block of code.

- __coefficient__

  The number that is multiplied to each of the factors in a polynomial equation. For example, in the equation _x2 + 2x + 1_, the coefficients are _1_, _2_, and _1_.

- __coercion__

  The process of converting an object from one class to another. For example, an integer value can be coerced into a real value. Also, the software that performs such a conversion. Also known as _object conversion_.

- __color space__

  A one-, two-, three-, or four-dimensional environment whose components (or channels) represent intensity values. For example, RGB space is a three-dimensional color space whose stimuli are the red, green, and blue intensities that make up a given color; and red, green, and blue are color channels.

- __color-lookup table__

  A table of values used to map color indexes into actual color values.

- __ColorSync__

  An industry-standard architecture for reliably reproducing color images on various devices (such as scanners, video displays, and printers) and operating systems.

- __color well__

  A small rectangular or square control used to apply a color selection. The color of the control indicates the currently selected color.

- __column__

  In a relational database, the dimension of a table that holds values for a particular attribute. For example, a table that contains employee records might have a column titled “LAST_NAME” that contains the values for each employee’s last name. See also [attribute](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tc).

- __column view__

  A control that displays textual listings of hierarchical data in vertical columns. Navigation between columns reveals levels of the hierarchy.

- __combination box__

  A text entry field combined with a drop-down scrolling list. Combo boxes are useful for displaying a list of likely choices while still allowing the user to type in an item not in the list.

- __command__

  In AppleScript, a word or phrase in a script that requests an action. For example, a script can send a `stop` command to a progress indicator object. Compare [target dependency](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgayds). See also [SOAP engine](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4di).

- __command description__

  A scripting definition file (sdef) entry that describes the characteristics of an AppleScript command, including argument names (if any), command result type (if any), AppleScript command name, and name of the Objective-C class Cocoa instantiates to perform the command. When the sdef is loaded, the information is stored in an instance of `NSScriptCommandDescription` .

- __command gate__

  A mechanism that controls access to the lock of a work loop, thereby serializing access to the data involved in I/O requests. A command gate does not require a thread context switch to ensure single-threaded access. IOCommandGate event-source objects represent command gates in the I/O Kit.

- __command ID__

  A four-character code that uniquely identifies a menu item or control. Note that a menu item and a control can share the same command ID.

- __command pop-down menu__

  A menu that contains commands and appears in a window rather than in the menu bar. Use of this control is limited to cases where the window is shared among multiple applications and the menu contains commands that affect the window’s contents. A closed pop-down menu always displays the same text, which is the menu title. Pop-down menus have a single, downward-pointing triangle.

- __command-line utility__

  A tool without a graphical user interface, typically used in the command-line environment.

- __comment__

  Text that remains in a script after compilation but is ignored by AppleScript when the script is executed.

- __commit__

  To publish changes in an Xcode project to a repository.

- __compact__

  To make a search index smaller by removing unused bits. Over time, as documents get added to and removed from an index, the index’s disk or memory footprint may grow due to fragmentation. Search Kit includes APIs to check for fragmentation and to compact an index. See also [fragmentation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhayta).

- __compatibility version__

  One of two numbers used to track minor version information in a framework. This number marks changes to the public interfaces. The compatibility version typically lags behind the current version. Compare [current version](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq3do).

- __compile__

  In AppleScript, to convert a script from the form typed into a script editor to a form that can be used by AppleScript. The process of compiling a script includes syntax and vocabulary checks. A script is compiled when you first run it and again when you modify it and then run it again, save it, or check its syntax.

- __compiled script__

  The form to which an AppleScript script is converted when you compile it.

- __completeness__

  In OpenGL, a state that indicates whether a framebuffer object meets all the requirements for drawing.

- __completion list__

  A list that Xcode builds for a typed token and that you can display when using code completion. See [code completion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm2do).

- __component__

  (1) A part of a software product that resides at a distinct location in the file system. See also [component package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm3to). (2) A plug-in whose interface is defined by the Component Manager. For example, an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) is a component. (3) An object (of the `WOComponent` class) that represents a webpage or a reusable portion of one.

- __component package__

  An installation package whose payload is one of the components of a product. See also [product package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu2to).

- __component package editor__

  The area of a PackageMaker project window that specifies packaging and installation information about a product component. This editor is displayed when a component is selected in the Contents pane in the project window.

- __composite SDK__

  A group of additional SDKs used by a target. Xcode creates and caches the composite at build time.

- __composite value__

  In AppleScript, a value that contains other values. Lists, records, and strings are examples of composite values.

- __compositing__

  A method of overlaying separately rendered images into a final image. It encompasses simple copying as well as more sophisticated operations that take advantage of transparency.

- __composition__

  In Quartz Composer, a collection of interconnected patches that describe a data flow.

- __composition repository__

  In Quartz Composer, a central location for storing compositions. Any application can, using the Quartz Composer framework, query the repository for specific types of compositions or browse the repository to see what’s available.

- __compound statement__

  An AppleScript statement that occupies more than one line and contains other statements. A compound statement begins with a reserved word indicating its function and ends with the word `end` . See also [simple statement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2to).

- __compression__

  See [data compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq4dc), [level compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge2dg).

- __compressor__

  Hardware or software that implements either [data compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq4dc) or [level compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge2dg). A data compressor, along with its corresponding decompressor, is sometimes referred to as a _codec_.

- __concatenation__

  In Quartz 2D, an operation that combines two matrices by multiplying them together.

- __concrete type__

  Defines, in information property lists, specific characteristics of a type of document, such as extensions and HFS+ type and creator codes. Each concrete type has corresponding abstract types. See also [abstract type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgayds).

- __concurrent operation__

  An operation object that does not perform its task in the thread from which its start method was called. A concurrent operation typically sets up its own thread or calls an interface that sets up a separate thread on which to perform the work.

- __condition__

  A construct used to synchronize access to a resource. A thread waiting on a condition is not allowed to proceed until another thread explicitly signals the condition.

- __conditional build setting__

  In Xcode, setting values that apply only when one or more conditions are met (for example, the product is being built using a particular SDK). Xcode uses these definitions when generating executable code for a particular architecture or for a particular variant of the product.

- __conditional statement__

  See [if statement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhezds).

- __condition variable__

  A wait queue with additional locking semantics. When a thread sleeps, waiting for some event to occur, it releases a related lock so that another thread can cause that event to occur. When the second thread posts the event, the first thread wakes up, and, depending on the condition variable semantics used, either takes the lock immediately or begins waiting for the lock to become available.

- __configuration file__

  See [build configuration file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgiztq).

- __configuration unit__

  In Xcode, a group of configuration files joined together by `#include` directives.

- __connection__

  In Core Audio, a hand-off point for audio data entering or leaving an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq). A connection has one or more channels. See also [channel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4tq).

- __connections panel__

  In Interface Builder, a panel that appears as needed to display the connection status of outlets and actions.

- __considering statement__

  In AppleScript, a control statement that lists a specific set of attributes to be considered when AppleScript performs operations on strings or sends commands to applications.

- __console__

  (1) A text-based login environment that also displays system log messages, kernel panics, and other information. (2) A special window in OS X that displays messages that would be printed to the text console if the GUI were not in use. This window also displays output written to the standard error and standard output streams by applications launched from the Finder.

- __Console__

  An application that displays the console window.

- __constant__

  A reserved word with a predefined value.

- __constant bit rate__

  See [CBR](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3te).

- __consumer__

  (1) In Quartz Composer, a patch that renders a result to a destination. (2) In WebObjects, an application that executes a web service operation by sending a SOAP message to a web service provider.

- __container__

  (1) A file-based enclosure for a software product that facilitates delivery to its users. Disk images installation packages, and ZIP archives are the most popular product containers. (2) In AppleScript, a file-based enclosure for a product that facilitates delivery to its users. Disk images installation packages, and ZIP archives are the most popular product containers.

- __container atom__

  An atom that contains other atoms, possibly including other container atoms.

- __containment hierarchy__

  A hierarchy of event targets that determines which handler is to be called to process an event. Events are initially sent to the innermost (or lowest) relevant target in the hierarchy. If the handler associated with that event target does not handle the event (or if no handler exists), then the event is propagated to the next target in the hierarchy. If no handler in the hierarchy processes the event, the default handler is called.

- __content pane__

  In either browse mode or search mode, a view that displays category information or a document page.

- __content region__

  The portion of the window below the title bar. The content region can contain document content or controls.

- __content view__

  In Mac apps, the view object that acts as the root for all other views in the window. In iOS applications, the portion of an iPhone window that displays the application’s custom content. Each content view may be represented by one or more actual views and typically presents a single screen’s worth of application content.

- __context__

  (1) In OpenGL, a set of OpenGL state variables that affect how drawing is performed for a drawable object attached to that context. Also called a _rendering context_. (2) In the OS X printing system, a pointer to a custom data structure that contains state information shared among the functions in a printing dialog extension.

- __contextual features__

  Features that are applied to a glyph depending on the glyph’s position relative to adjacent glyphs. Compare [noncontextual features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmzde).

- __contextual form__

  An alternate form of a glyph whose use depends on the glyph’s placement in a word.

- __contextual menu__

  A menu that appears when the user presses the Control key and clicks an interface item. A contextual menu provides convenient access to frequently used commands associated with the item.

- __contiguous highlighting__

  Highlighting that consists of a single, contiguous shape across direction boundaries, even when it does not exactly match the selection range to which it corresponds. Compare [discontinuous highlighting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu3tk).

- __continuation character__

  In AppleScript, a character used in Script Editor to extend a statement to the next line. With a U.S. keyboard, you can enter this character by typing Option-l (lowercase L).

- __continue statement__

  In AppleScript, a statement that controls when and how other statements are executed. AppleScript defines standard control statements such as `if`, `repeat`, and `while` .

- __continuous selection__

  A selection that includes all content between the anchor point and the active end.

- __continuous style__

  In MLTE, a style value that is constant over an entire selection range.

- __control__

  A graphic object that causes instant actions or visible results when the user manipulates the object. Standard controls include buttons, scroll bars, checkboxes, sliders, and pop-up menus.

- __control layer__

  The classes in the package `com.webobjects.eocontrol` , which include `EOEditingContext` and `EOEnterpriseObject` . You use classes in this layer to fetch, create, manage, and save persistent data to a data source.

- __controller object__

  An object that manages the interactions between an application’s data objects and the objects that display that data.

- __control port__

  In Mach, access to the control port allows an object to be manipulated. Also called the _privileged port_. See also [name port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi4ts), [port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq4tk).

- __control reference__

  A pointer to an opaque data structure that describes a control’s properties. You manipulate a control by means of its control reference.

- __control statement__

  A statement that causes AppleScript to exit the current handler and transfer execution to the handler with the same name in the parent. A `continue` statement can also be used to invoke an inherited handler in the local context.

- __converter__

  A module used by the printing system to convert a document description from one document format to another.

- __convolution__

  A common image processing technique that changes the intensities of a pixel to reflect the intensities of the surrounding pixels. Using convolution, you can get image effects like blur, emboss, and sharpen.

- __cookie__

  See [magic cookie](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4tc).

- __cooperative multitasking__

  A multitasking environment in which a running program can receive processing time only if other programs allow it; each application must give up control of the processor cooperatively in order to allow others to run. Mac OS 9 is a cooperative multitasking environment. See also [preemptive multitasking](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrguytc).

- __coordinate scale__

  In Core Audio, for a [panner unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqyto), a parameter that specifies the maximum value for the distance parameter, in meters.

- __Copies & Pages pane__

  A pane in the Print dialog that lets the user set the number of copies and the range of pages to be printed.

- __CopyBits__

  A QuickDraw function that has no direct replacement in Quartz, primarily because Quartz does not use a bit-based graphics model, as QuickDraw does.

- __copy-on-write__

  A delayed copy optimization used in Mach. The object to be copied is marked temporarily read-only. When a thread attempts to write to any page in that object, a trap occurs, and the kernel copies only the page or pages that are actually being modified. See also [thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2tq).

- __Core Audio__

  A set of iOS and OS X frameworks that provides audio services (depending on the platform) that include recording, playback, synchronization, signal processing, format conversion, panning and surround sound, hardware abstraction, and others.

- __Core Audio Format__

  See [CAF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3de).

- __Core Data__

  A technology for managing structured data in your application. The data model of a Core Data application is built on a schema that defines one or more entities and their properties and the relationships between those entities. At runtime, Core Data manages the data for those entities using a database or other structured form of data store.

- __Core Foundation URL reference__

  A data object of type `CFURLRef` specifying a [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge3tm).

- __Core Graphics__

  The name of the framework (`CoreGraphics.framework`) in which the Quartz API resides. The Quartz API is sometimes referred to as the Core Graphics API.

- __Core Image__

  An image processing programming interface that is part of the Quartz Core framework.

- __Core Image filter__

  An image processing routine provided by the Core Image framework. Core Image filters are automatically read into Quartz Composer and made available as patches.

- __Core MIDI__

  An OS X framework for controlling and communicating with MIDI devices.

- __corpora__

  Plural form of [corpus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq2dc).

- __corpus__

  A collection of one or more documents, typically related, and available to an information retrieval system. Plural: corpora.

- __counter__

  The oval in glyphs such as “p” or “d”.

- __creator signature__

  In the Macintosh file system, a four-character code that identifies the application to which a file belongs.

- __credential__

  Proof of user authentication. It’s used by the Security Server. When the Security Server authenticates a user, it creates a credential as part of the authorization session.

- __credentials__

  Data that can be used to identify, authenticate, or authorize an entity. For example, a user name and password constitute [authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3de) credentials. A [Kerberos ticket](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4da), consisting of an encrypted [session key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhaztg) and other information, is an [identification](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqheyts) credential. In Kerberos version 5 and later, tickets can also carry [authorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3di) information.

- __critical section__

  A portion of code that must be executed by only one thread at a time.

- __cross-development__

  Creating software that can be deployed on, and take advantage of features from, specified versions of OS X, including versions different from the one you are developing on.

- __cross-project reference__

  A reference from the project that contains an application to a project that contains a framework. It lets you access the targets and products of the referenced project from your current project.

- __cross-stream kerning__

  The automatic movement of glyphs perpendicular to the line orientation of the text.

- __cross-stream shift__

  A type of positional shift that applies equally to all glyphs in a style run by raising or lowering the entire style run (or shifts it sideways if it’s vertical text). Compare [with-stream shift](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi3do).

- __cryptographic hash function__

  An algorithm that takes any amount of data and transforms it into a fixed-size output value. For a cryptographic hash function to be useful for security, it has to be extremely difficult or impossible to reconstruct the original data from the hash value, and it must be extremely unlikely that the same output value could result from any other input data. See also [message digest](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgizdo).

- __cryptographic hashing__

  The process whereby data is transformed using a [cryptographic hash function](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq2tc).

- __CSR__

  Certificate signing request. A file that contains personal information used to generate a development certificate. Certificate signing requests are created by the Keychain Access application.

- __CSSM__

  Common Security Services Manager. A public application programming interface for [CDSA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3tg). CSSM also defines an interface for plug-ins that implement security services for a particular operating system and hardware environment.

- __cubic curve__

  A curve defined by a cubic equation. See also [Bï¿½zier curve](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge4to).

- __culling__

  In OpenGL, eliminating parts of a scene that can’t be seen by the observer.

- __CUPS__

  Common UNIX Printing System. An open source architecture commonly used by the UNIX community to implement printing.

- __current application__

  The application that is using the AppleScript component to compile and execute scripts (typically, Script Editor).

- __current context__

  The rendering context to which OpenGL routes commands issued by your application.

- __current graphics state__

  The parameter values that determine how Quartz renders results as it paints.

- __current matrix__

  A matrix used by OpenGL to transform coordinates in one system to those of another system, such as the modelview matrix, the perspective matrix, and the texture matrix. GL shading language allows user-defined matrices.

- __current point__

  The last location Quartz used when painting a path.

- __current printer__

  The printer displayed in the Printer pop-up menu when the user opens the Print dialog.

- __current script__

  The AppleScript script currently being executed.

- __current target__

  In AppleScript, the object that is the current default target for commands.

- __current transformation matrix__

  An affine transform that Quartz uses to map points from one coordinate space to another.

- __current version__

  One of two numbers used to track minor version information in a framework. It tracks individual builds of your framework and is mostly for internal use by your team. Compare [compatibility version](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm3tc).

- __cursor__

  The onscreen representation of the mouse’s location. The cursor commonly looks like an arrow, but can also assume such shapes as a pencil, a cross, or a paintbrush, depending on the application and the user’s selection. (Also called a _pointer_.)

- __custom guide__

  In Interface Builder, an alignment tool that is placed by the user in order to align objects to an arbitrary location on the design surface.

- __custom install__

  A metapackage or distribution package installation that a user performs after modifying the default option selection.

- __custom patch__

  A subclass of [QCPlugIn](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4ts)that performs custom processing in the Quartz Composer development environment.

- __CVS__

  Concurrent Version System. A source-code control system that Xcode can use to manage changes in source code over time and across multiple developers.

- __DAC__

  Digital-to-analog converter. Circuitry that converts digital data to a corresponding analog signal. DACs are characterized by maximum sampling frequency, amplitude resolution in terms of bit depth, monotonicity, distortion characteristics, and noise floor. Compare [user focus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4dk).

- __daemon__

  A process that handles periodic service requests or forwards a request to another process for handling. Daemons run continuously, usually in the background, waking only to handle their designated requests. For example, the `httpd` daemon responds to HTTP requests for web information.

- __Darwin__

  The core of OS X, Darwin is an open source project that includes the Darwin kernel, the BSD commands and C libraries, and several additional features. The Darwin kernel is synonymous with the OS X kernel.

- __dash__

  In a menu, indicates that an attribute applies to only part of the selection. For example, if a highlighted selection contains text with different styles applied to it, a dash appears next to each style name in the menu.

- __Dashboard__

  A user technology for managing HTML-based programs called widgets. Activating the Dashboard via the F12 key displays a layer above the OS X desktop that contains the user’s current set of widgets.

- __Dashcode__

  A graphical application used to build and debug Dashboard widgets.

- __data__

  An AppleScript class used for data that do not belong to any of the other AppleScript classes; see the `data` class.

- __database server__

  A data storage and retrieval system. Database servers typically run on a dedicated computer and are accessed by client applications over a network.

- __data browser__

  A control that provides a standardized look for column browsers (such as seen in the column view of a Finder window or in an Open dialog) and scrolling lists (such as seen in the list view of a Finder window).

- __data compression__

  Algorithmic reduction of data size to improve storage or transmission efficiency. Data compression can be lossy or lossless. Compression is a special case of [encoding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy3tq). See also [lossless compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4de), [lossy compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4dg), [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2dq).

- __data fork__

  In a Macintosh file, the section that corresponds to a DOS/Windows file.

- __data formatter__

  In Xcode, a string that specifies how variables are displayed in debugger datatips and the variable list in the debugger.

- __data handler__

  In QuickTime, a piece of software that is responsible for reading and writing a media structure’s data. The data handler provides data input and output services to the media structure’s media handler. See also [media handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgiytg).

- __data modeling__

  The process of building a data model to describe the mapping between a relational database schema and an object model.

- __data reference__

  A reference to a QuickTime media structure’s data.

- __data run__

  See [run](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg42dc), [text run](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2dm).

- __data source object__

  An object supplied by AppleScript Studio that supplies data to a table view or other view with rows and columns.

- __data-source adaptor__

  In WebObjects, a mechanism that connects your application to a particular database server. For each type of server you use, you need a separate adaptor. WebObjects provides an adaptor for databases conforming to JDBC.

- __date__

  In AppleScript, a class that specifies a time, day of the month, month, and year.

- __date picker__

  A control that allows a user to input date and time information in either a textual or graphical format.

- __dB__

  See [decibel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq4tq).

- __dBu__

  An absolute measure of RMS voltage level in decibels relative to 0.775 Volts RMS. dBu measurements assume a circuit load with infinite impedance. See also [RMS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4yti).

- __debug rendering mode__

  A view that displays an animation of the data flow in a composition that can help track down issues. In this mode, patches in the workspace change colors as they move from one state to another. A drawer below the view displays log messages.

- __debugger__

  A process that lets you pause a program and examine its state.

- __debugger datatip__

  A way of viewing and modifying the contents of variables using a progressive disclosure mechanism.

- __debugger strip__

  A small control strip that appears above the content pane and contains controls for several debugging tasks.

- __decibel__

  A dimensionless unit for expressing the ratio of two quantities, abbreviated as _dB_. The decibel difference between two power levels is equal to 10 times the common logarithm of their ratio. The decibel difference between two voltage levels is equal to 20 times the common logarithm of their ratio. Decibel values are typically associated with a standard voltage or power level. For example, acoustic levels are commonly referenced to 0 dB SPL, equivalent to 20 µPa (micropascals). See also [SPL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrheyte).

- __declaration__

  In AppleScript, the first occurrence of a variable or property identifier in a script. The form and location of the declaration determine how AppleScript treats the identifier in that script—for example, as a property, global variable, or local variable.

- __decode__

  In audio, to retrieve the original signal from an encoded representation of it. For lossy encoding schemes such as MP3, the retrieved signal approximates the original signal. See also [codec (coder/decoder)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm2dm), [encoding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy3tq).

- __decryption__

  The transformation of [ciphertext](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmzda) back into the original [plaintext](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq3tm). Compare [encryption](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy4da). See also [asymmetric keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgeztm), [symmetric keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4da).

- __dedicated network build__

  In Xcode, a distributed build that is effective on large projects using ten or more build servers. See also [distributed build](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4do). Compare [shared workgroup build](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2dk).

- __deep fetch__

  In WebObjects, an option available to fetch specifications that causes database fetches to occur against the root table and any leaf tables. Applicable to inheritance hierarchies.

- __default application__

  The application selected by Launch Services, according to its own implicit [binding rules](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgiydm), in which to open a given document or URL in the absence of an explicit [binding preference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgiydk) set by the user.

- __default build configuration__

  The configuration Xcode uses when a project does not have a definition for the active build configuration.

- __default button__

  The button that provides a safe action in a dialog. The default button is indicated by a pulsing appearance. It is activated when the user presses the Return or Enter key.

- __default keyboard access mode__

  The mode in which tabbing and other keystrokes move keyboard focus only between fields that receive keyboard input, such as text entry fields and scrolling lists. See also [full keyboard access mode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhazdg).

- __default keychain__

  The keychain accessed by certain Keychain Services functions when no other keychain is specified in the function call. For example, newly created keychain items are stored in the default keychain unless a different keychain is specified in the function call. A default keychain is created for each new login account, but the user can use the Keychain Access utility to designate another keychain as the default.

- __default keychain search list__

  The list of keychains searched by certain Keychain Services functions when no other keychain or list of keychains is specified in the function call. The default keychain search list contains the same keychains as the keychain list displayed in the Keychain Access utility.

- __default output unit__

  An Apple-supplied [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) that connects with whichever hardware device the user has designated to be the default output.

- __default pager__

  In Mach, one of the built-in pagers. The default pager handles nonpersistent (anonymous) memory. See also [anonymous memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga3ts), [pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqydk), [vnode pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgiztc).

- __default target__

  In AppleScript, the object that receives a command if no object is specified or if the object is incompletely specified in the command. Default (or implicit) targets are specified in `tell` statements.

- __deferred faults__

  In WebObjects, a special kind of fault that represents a number of other faults in a single object. See also [fault](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4zti), [faulting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4ztk).

- __deferred recognition__

  In the Ink Services technology, the process of recognizing an ink phrase that was drawn by the user at an earlier time.

- __deinterleaving__

  In digital audio , retrieving discrete channels from an interleaved representation. Also called _reverse multiplexing_. Compare [interleaving](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgazdi).

- __delay__

  The time lag between one audio event and another. In audio processing, the second event is typically a processed or unprocessed copy of the original event. Delay is a settable [parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqzdg) in the AUDelay [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) included in OS X.

- __delegation__

  (1) A way of extending a class in an object-oriented framework. In object-oriented design methodology, delegation is a form of class composition. (2) In AppleScript, the use of a `continue` statement to call a handler in a parent object or the current application.

- __delivery vehicle__

  The means of transport used by users of a product to obtain the product’s files. These include optical media and the Internet.

- __demand paging__

  An operating-system facility that brings pages of data from disk into physical memory only as they are needed.

- __deployment build style__

  A methodology of creating a product from a target that makes the product more appropriate for distribution to users.

- __deployment descriptor__

  In WebObjects, an XML file that describes the configuration of a web application. It’s located in the `WEB-INF` directory of the application’s WAR file and named `web.xml` .

- __deployment tool__

  An HTML-based application through which J2EE application or component archives can be configured or assembled in preparation for deployment in OS X Server.

- __depth__

  In OpenGL, refers to the _z_ coordinate and specifies how far a pixel lies from the observer.

- __depth buffer__

  In OpenGL, block of memory used to store a depth value for each pixel. The depth buffer is used to determine whether or not a pixel can be seen by the observer. Those that are hidden are typically removed.

- __derived attribute__

  An attribute in a data model that does not directly correspond to a column in a database. Derived attributes are usually calculated from a SQL expression.

- __descent line__

  An imaginary horizontal line that usually corresponds to the bottoms of the descenders in a font. The descent line is the same distance from the baseline for all glyphs in the font, whether or not they have descenders.

- __descriptor__

  An abstract identifier used to access a file, socket, or other system resource.

- __descriptor dispatch source__

  A [dispatch source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvjvomq) used to process file-related events. A file descriptor source calls your custom event handler either when file data is available for reading or writing or in response to file system changes.

- __design surface__

  In Interface Builder, the content area of a window object. It’s the area in which you drop views and other visual objects and is also where you manipulate those objects directly.

- __desktop__

  The background on top of which all windows appear; the working environment displayed on Mac computers.

- __destination printer__

  The printer to which a print job is sent. This is the printer displayed in the Printer pop-up menu when the user clicks Print in the Print dialog.

- __destination rectangle__

  The rectangle defining the area in which text is drawn.

- __destination region__

  The part of a document that can accept data dragged to it. In a document window, the destination region is usually the content area minus the title bar and areas used for controls such as scroll bars and rulers.

- __detail view__

  In Xcode, a view that displays the item or items that you select in the Groups & Files list, providing a convenient way for you to find and access project contents.

- __development build style__

  A methodology of creating a product from a target that makes the product more appropriate for debugging and testing.

- __development certificate__

  A file that identifies an iPhone application developer. Xcode uses development certificates to sign application binaries.

- __device__

  (1) Computer hardware, typically excluding the CPU and system memory, that can be controlled and can send and receive data. Examples of devices include displays, disk drives, buses, and keyboards. (2) In audio generally, a piece of equipment or a software entity that produces, transforms, transmits, receives, or stores audio data. In MIDI, a piece of equipment or a software entity that responds to MIDI control or provides MIDI data. In Audio Queue Services, a source or destination for audio, such as a microphone or a loudspeaker.

- __device advance__

  The number of pixels of the advance for the glyph as actually drawn on the screen.

- __device color space__

  A color space that is tied to the system of color representation for a particular device. This type of color space is not suitable for interchanges of color data between different devices.

- __device delta__

  A value used to adjust truncated factional values for cases in which fractional positioning can’t be used. Device delta values are usually used when anti-aliasing is turned off. However, these values can be used when anti-aliasing is on, to assure that the glyphs in a connected script (such as one that uses the Zapfino font) are connected smoothly.

- __device driver__

  A component of an operating system that deals with getting data to and from a device, as well as the control of that device. A driver written with the I/O Kit is an object that implements the appropriate I/O Kit abstractions for controlling hardware.

- __device file__

  In BSD, a device file is a special file located in`/dev`that represents a block or character device such as a terminal, disk drive, or printer. If a program knows the name of a device file, it can use POSIX functions to access and control the associated device. The program can obtain the device name (which is not persistent across reboots or device removal) from the I/O Kit.

- __device interface__

  In the I/O Kit, a mechanism that uses a plug-in architecture to allow a program in user space to communicate with a nub in the kernel that is appropriate to the type of device the program wishes to control. Through the nub the program gains access to I/O Kit services and to the device itself. From the perspective of the kernel, the device interface appears as a driver object called a user client.

- __device matching__

  In the I/O Kit, a process by which an application finds an appropriate device interface to load. The application calls a special I/O Kit function that uses a matching dictionary to search the I/O Registry. The function returns one or more matching driver objects that the application can then use to load an appropriate device interface. Also referred to as _device discovery_.

- __device space__

  The coordinate system that defines the position and scale (pixel size) of a specific view device.

- __device-independent color space__

  A color representation that is portable between devices and that is used for the interchanges of color data from the native color space of one device to the native color space of another device. Colors in a device-independent color space appear the same when displayed on different devices, to the extent that the capabilities of the device allow.

- __diacritical marks__

  A mark, such as an accent, that is used in conjunction with a character to indicate phonetic value.

- __dialect__

  A version of the AppleScript language that resembles a specific human language or programming language.

- __dialog__

  A window designed to elicit a response from the user. See also [alert](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga3de).

- __diamond__

  In a Window menu, a mark that indicates that a document has been minimized into the Dock.

- __dictionary__

  In AppleScript, the set of commands, objects, and other terminology that is understood by an application or other scriptable entity. You can display an application’s dictionary with Script Editor.

- __dictionary browser__

  See_terminology browser._

- __Diffie-Hellman key exchange__

  A protocol that provides a way for two ends of a communication session to generate symmetric [private key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu2di)s through the exchange of [public key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4te)s.

- __digest__

  See [message digest](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgizdo).

- __digital certificate__

  A collection of data used to verify the identity of the holder or sender of the certificate. A digital certificate must conform to some standard in order for the recipient to be able to interpret it. OS X and iOS support the [X.509](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi4da) standard for digital certificates. See also [certificate chain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4dc).

- __digital ID__

  See [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2tg).

- __digital rights management__

  See [DRM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyzdo).

- __digital signal processing__

  See [DSP](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyztc).

- __digital signature__

  A way to ensure the integrity of a message or other data using [public key cryptography](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4ti). To create a digital signature, the signer generates a [message digest](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgizdo) of the data and then uses a [private key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu2di) to encrypt the digest. The signature includes the encrypted digest and identifies the signer. Anyone wanting to verify the signature uses the signer’s [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2tg), which contains the public key needed to decrypt the digest and specifies the algorithm used to create the digest.

- __dilation__

  An effect that takes each bright pixel in the source image and expands it into the shape of the kernel, flipped horizontally and vertically. The contribution of the source pixel to the kernel-shaped region depends on two things: the brightness of the source pixel (brighter pixels contribute more) and the values of the kernel pixels (pixels that are dark, relative to the center of the kernel, contribute more to their locations in the kernel-shaped region than pixels that are bright).

- __dimmed__

  Used to describe text or icons that are grayed out to indicate that they are currently unavailable. Menu items, for example, are dimmed rather than omitted when they aren’t applicable at a particular moment.

- __diphthong__

  A complex vowel sound that can be phonetically represented by 2 characters. The characters represent the initial and final sounds of the diphthong.

- __direct parameter__

  In AppleScript, the parameter immediately following a command, which typically specifies the object to which the command is sent.

- __Direct to Java Client__

  A WebObjects development approach that can generate a Java Client application from a model.

- __Direct to Java Client Assistant__

  A WebObjects tool used to customize a Direct to Java Client application.

- __Direct to Web__

  A WebObjects development approach that can generate a web application from a model.

- __Direct to Web Services__

  A WebObjects development approach that can generate a web service application from a model.

- __Direct to Web template__

  In WebObjects, a component used in Direct to Web applications that can generate a webpage for a particular task (for example, a list page) for any entity.

- __direct-access functions__

  ATSUI functions that allow you to manipulate glyph data directly.

- __direction boundary__

  A point, between offsets in memory or glyphs in a display, at which the direction of stored or displayed text changes.

- __direction run__

  A contiguous (in memory) sequence of characters having the same right-to-left or left-to-right line direction.

- __directory__

  A file-system object containing zero or more other named objects (files or other directories).

- __disc menu__

  In DVD Player, the main menu from which titles are selected. The disc menu is sometimes called the title menu, which more accurately refers to the menu within a title from which chapters and other features can be selected.

- __disclosure button__

  A control that expands a dialog to provide the user with additional choices that are associated with a specific list-based selection control (such as a pop-up menu).

- __disclosure triangle__

  A control that allows the display, or disclosure, of information that elaborates on the primary information in a window. Disclosure triangles are used in the Finder’s list view; clicking a triangle displays a folder’s contents.

- __discontinuity__

  In an audio data stream, a distinct break in the sequence of transmitted data. A discontinuity entails a period in which the stream is undefined. See also [TCP stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgaytm).

- __discontinuous highlighting__

  Highlighting that exactly matches the selection range it corresponds to. It may consist of discontinuous areas when the selection range crosses direction boundaries. Compare [contiguous highlighting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgqytg).

- __discontinuous selection__

  A selection in which unselected objects are between selected objects.

- __disk image__

  A file-based enclosure that facilitates the transport of a directory structure on the Internet. Disk images can also be compressed to allow a product’s files to be placed on optical media.

- __dispatch queue__

  A Grand Central Dispatch (GCD) structure that you use to execute your application’s tasks. GCD defines dispatch queues for executing tasks either serially or concurrently.

- __dispatch source__

  A Grand Central Dispatch (GCD) data structure that you create to process system-related events.

- __display coordinate system__

  The QuickDraw graphics world, which can be used to display QuickTime movies, as opposed to the movie’s time coordinate system, which defines the basic time unit for each of the movie’s tracks. Compare [time coordinate system](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3tk).

- __display link__

  A high-priority thread that, based on a specified hardware display, makes intelligent guesses as to how often frames must be output to synchronize with the display’s refresh rate.

- __display list__

  A list of OpenGL commands that have an associated name and that are uploaded to the GPU, preprocessed, and then executed at a later time. Display lists are often used for computing-intensive commands.

- __display name__

  The name of a file as it appears to the user. The display name reflects the user’s preference for hiding or showing the filename extension.

- __display order__

  The order in which glyphs are drawn on a screen. Glyphs are always drawn in left-to-right order. Because not all text is read left-to-right, the display order of glyphs may be different from the storage order of their corresponding character codes in memory.

- __Display pop-up menu__

  In Xcode, a menu that lets you choose when to display the Build Results window, overriding the default settings in the Building pane of Xcode Preferences.

- __display text__

  The visual representation of the text of a text layout object. Display text consists of a sequence of glyphs, arranged in display order. Compare [source text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4tm).

- __distance__

  In [surround sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe3tm) and immersive audio, the real or apparent straight line distance of an audio source from the listener.

- __distortion__

  A difference, typically unintentional and undesired, between the signals on the input and output of an audio device. Commonly measured types of distortion include harmonic distortion, intermodulation distortion, quantization distortion, and jitter. Intentional differences between input and output signals, such as level or equalization differences, are not described as distortion. Compare [noise](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmzda).

- __distributed build__

  In Xcode, a build that uses several computers to compile source files.

- __distribution package__

  A metapackage that contains a distribution script that specifies the installation experience for a product. Distribution packages provide a streamlined packaging experience for developers and an enhanced installation experience for users. See also [distribution script](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4ds), [metapackage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgizds).

- __distribution script__

  An XML file with the extension `.dist` that contains all the information that defines an installation experience in a distribution package. See also [distribution package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4dq).

- __dither__

  In audio, a low-amplitude noise applied to a signal to reduce quantization error. See also [quantization noise](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyydm).

- __dithering__

  A technique used to improve picture quality when you are attempting to display an image that exists at a higher bit-depth representation on a lower bit-depth device. For example, you might want to dither a 24-bits-per-pixel image for display on an 8-bit screen.

- __DLIL__

  Data Link Interface Layer. The part of the OS X kernel’s networking infrastructure that provides the interface between protocol handling and network device drivers in the I/O Kit. A generalization of the BSD “ifnet” architecture.

- __DMA__

  Direct memory access. A capability of some bus architectures that enables a bus controller to transfer data directly between a device (such as a disk drive) and a device with physically addressable memory, such as that on a computer’s motherboard. The microprocessor is freed from involvement with the data transfer, thus speeding up overall computer operation. See also [bus master](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi2tk).

-  __`.dmg` file__

  An OS X disk image file.

- __Dock__

  A user-configurable, onscreen, interface element that provides a simple way for users to launch frequently used applications and documents. It also houses minimized windows and the Trash.

- __document__

  A unit or collection of data, contained in a file or [sandboxing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg42to), that can be operated on by an application. In Search Kit, anything that contains text and that the Search Kit client application addresses as a document—an RTF document, a PDF file, a Mail message, an Address Book entry, the contents at an Internet URL, the result of a database query, and so on. See also [document URL object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyydk).

- __document collection__

  See [corpus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq2dc).

- __document file__

  A file containing a document.

- __document-modal__

  A window state where the user cannot do anything else within a particular document until the window is dismissed. Sheets are document-modal windows. Compare [application-modal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgeytq), [system modal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4to).

- __document-modal dialog__

  A dialog that prevents the user from performing further operations in the document until the user dismisses the dialog. All sheets are document modal and all Aqua document-modal dialogs should be sheets. See also [application-modal dialog](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgeyts), [sheet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2do).

- __document object hierarchy__

  A collection of documents in which each document exists at a location relative to a root document. The locations may may be real, as in a file system, or virtual.

- __document package__

  A [package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm4ta) containing a document along with related resources.

- __document type__

  A family of document files characterized by a given [file type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg42tq), [creator signature](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq2dg), or [filename extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg42ta). Compare [URL type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge3tq).

- __document type definition__

  See [DTD](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyztg).

- __document URL object__

  A URL to a document. In Search Kit, a document URL object comprises a scheme, a parent document URL object, and a name, with the format of each component defined by the client application. Search Kit document URL objects may be converted to or from CFURL objects. See also [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4tm), [parent document URL object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqzdm), [virtual address](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizdc).

- __document window__

  A window containing file-based data that users create and store.

- __documentation feed__

  An RSS-style web feed that Xcode can check periodically to determine when a publisher makes available updates to a documentation set or releases a new documentation set.

- __documentation node__

  In Xcode documentation sets, a documentation file or a folder of files within a set. Each documentation node is associated with a location that identifies the file to display when a user selects that node in the documentation window. A node may be a single document, a collection of documents, or a single HTML documentation page.

- __documentation search__

  In Xcode, a search composed of a search term, search type, and search scope.

- __documentation set__

  A subset of the reference library packaged as a standard OS X bundle. Each documentation set contains HTML-based content as well as indexes into that content, which Xcode uses to perform quick documentation searches. Also called a _doc set_.

- __Documentation window__

  In Xcode, a window designed for browsing and searching developer documentation. It provides access to a wider and more detailed view of the documentation than the Research Assistant.

- __domain__

  (1) In a file system, an area reserved for software, documents, and resources and limiting the accessibility of those items. A domain is segregated from other domains. There are four domains: user, local, network, and system. (2) In networking, a complete protocol family.

- __double angle brackets__

  Characters («,») typically used by AppleScript to enclose raw data. With a U.S. keyboard, you can enter double angle brackets (also known as chevrons) by typing Option-Backslash and Shift-Option-Backslash.

- __double buffering__

  The practice of using a front and back color buffer to achieve smooth animation. The back buffer is not displayed, but swapped with the front buffer.

- __downgradable component__

  A product component, such as an application binary or a plug-in, that can be replaced with an earlier version in an installation process.

- __DPCM__

  Differential pulse-code modulation. A variant of [pulse-code modulation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4to) that encodes the difference between the current and previous sample.

- __dpi__

  Dots per inch in the x and y directions; used to measure the resolution of a screen or printer. The higher the value, the finer the detail of the image.

- __drag and drop__

  The technique of dragging an item, such as a graphic or selected text, and dropping it on a suitable destination, such as another document.

- __drag area__

  The portion of a window that users can use to move the window.

- __drawable object__

  In OS X, an object allocated outside of OpenGL that can serve as an OpenGL framebuffer. A drawable object can be any of the following: a window, a view, a pixel buffer, offscreen memory, or a full-screen graphics device. See also [framebuffer object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhayti).

- __drawer__

  A child window that slides out from a parent window and that the user can open or close (show or hide) while the parent window is open. Drawers contain controls that are fairly frequently accessed but don’t need to be visible at all times.

- __driver__

  See [device driver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqguzts).

- __driver layer__

  I/O Kit drivers for various networking types.

- __driver matching__

  In the I/O Kit, a process in which a nub, after discovering a specific hardware device, searches for the driver or drivers most suited to drive that device. Matching requires that a driver have one or more personalities that specify whether it is a candidate for a particular device. Driver matching is a subtractive process involving three phases: class matching, passive matching, and active matching. See also [personality](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2te).

- __driver personality__

  A dictionary of key/value pairs that specify device property values, such as family type, vendor name, or product name. A driver is suitable for any device whose properties match one of the driver’s personalities.

- __driver stack__

  In an I/O connection, the series of driver objects (drivers and nubs) in client/provider relationships with each other. A driver stack often refers to the entire collection of software between a device and its client application (or applications).

- __DRM__

  Digital rights management. A generic term referring to embedded, electronic restriction over the use of electronic content. Usually applied to copyrighted material. See also [FairPlay](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4zdq).

- __drop capital__

  A large uppercase letter that drops below the main line of text for aesthetic reasons.

- __dropframe__

  In video, a synchronizing technique that skips timecodes to keep them current with video frames.

- __droplet__

  A script application that launches when you drag a file or folder icon in the Finder and drop it on the droplet’s icon. A droplet receives a list of descriptors for the folders or files dropped on it and typically performs operations on each item in the list.

- __DSP__

  Digital signal processing. In audio, analyzing or transforming digital representations of audio. Such transformations include, among others, filtering and equalization, reverberation, level compression, data compression, and sound effects such as pitch shifting. Digital signal processing can be performed by hardware, software, or a combination of both.

- __dSYM file__

  A file that stores an executable’s debugging information to minimize the size of the executable file without compromising the program’s debugging experience.

- __DTD__

  Document type definition. A file that describes the structure of an XML document.

- __dual caret__

  A type of caret that, at the boundary between text of opposite directions, divides into two parts: a high caret and a low caret, each measuring half the line’s height. The two separate half-carets merge into one in unidirectional text.

- __Duplex pane__

  A pane in the Print dialog (available for some printers) that provides the option to print to both sides of a sheet of paper.

- __duration__

  (1) The length of time, in seconds, it takes for an animation to complete. (2) In QuickTime, time values that are interpreted as spans of time, rather than as points in time.

- __DVD@ccess__

  An Apple technology you can use to add interactivity to a DVD when played on a computer. DVD@ccess makes it possible to open a web browser to display HTML files, or open a program to view PDF, PICT, or JPEG files.

- __DVD__

  An optical storage medium that provides greater capacity and bandwidth than CD-ROM; DVDs are frequently used for multimedia as well as data storage.

- __DVD event__

  A notification of a state change in DVD Playback Services during playback. An event is specified with a type identifier and associated data. Client applications can register callback functions to receive events of interest.

- __DVD player__

  (1) A hardware product that decodes and plays DVD-Video media stored on an optical disc. The output device is generally a television set, although some players have built-in displays and speakers. (2) A computer software program that decodes and plays DVD-Video media stored on an optical disc or a mass storage device such as a hard drive.

- __DVD-Video__

  A standard for storing and reproducing audio and video on DVD-ROM discs, based on MPEG-2 video compression, Dolby Digital and MPEG audio, and other proprietary data formats.

- __dyld__

  Dynamic link editor. The library manager for code in the Mach-O executable format. The dynamic link editor is a dynamic library that “lives” in all Mach-O programs on the system. See also [CFM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4dq), [Mach-O](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4do).

- __dyld (dynamic link editor)__

  A utility that allows programs to dynamically load (and link to) needed functions.

- __dynamic element__

  A dynamic version of an HTML element. WebObjects includes a list of dynamic elements with which you can build web components.

- __dynamic guide__

  In Interface Builder, an alignment tool that provides information about the position of a view relative to other objects on the design surface. Dynamic guides appear only when the Option key is held down.

- __dynamic library__

  A library for which binding of undefined symbols is delayed until execution. Code in dynamic shared libraries can be shared by multiple, concurrently running programs. See also [dynamic shared library](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy2te).

- __dynamic link editor__

  See [dyld](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy2de).

- __dynamic linking__

  The binding of modules, as a program executes, by the dynamic link editor (dyld). Usually the dynamic link editor binds modules into a program lazily (that is, as they are used). Thus modules not actually used during execution are never bound into the program.

- __dynamic menu item__

  A menu item that changes when the user presses a modifier key. For example, in the Finder File menu, if the user presses the Option key, the Close Window command changes to Close All. See also [toggled menu item](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga4dq).

- __dynamic range__

  A quality measure for an audio device or system that describes the difference between the loudest and softest signal that can appear at the output of the device. Dynamic range is equal to the ratio of dynamic ceiling to noise floor, typically described in decibels. See also [ceiling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3tk), [decibel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq4tq), [noise floor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmzdc).

- __dynamic shared library__

  A library whose code can be shared by multiple, concurrently running programs. Programs share exactly one physical copy of the library code and do not require their own copies of that code. With dynamic shared libraries, a program not only attempts to resolve all undefined symbols at runtime, but attempts to do so only when those symbols are referenced during program execution.

- __easy install__

  A metapackage or distribution package installation that a user performs using the default option selection.

- __EBU__

  European Broadcasting Union. A Europe-based, international, audio and broadcasting standards organization.

- __edge offset__

  A byte offset into the source text associated with a text layout object that specifies a position between byte values. Edge offsets in source text are related to caret positions in display text. Compare [byte offset](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi2ts).

- __editing context__

  An object that stores and manages a group of enterprise-object instances. An editing context, which is an instance of the `EOEditingContext` class, provides an in-memory view of data in a data store. Changes made to enterprise-object instances in an editing context are pushed to the data store by invoking a specific method. In addition, those changes can be undone, even after they have been committed to the corresponding data store.

- __edit list__

  In QuickTime, a data structure that arranges a media structure into a time sequence.

- __Edit menu__

  A menu that provides commands for changing (editing) the contents of documents. It contains commands such as Cut, Copy, and Paste.

- __edit state__

  In QuickTime, information defining the current state of a movie or track with respect to an edit session. QuickTime uses edit states to support undo facilities.

- __effect description__

  A data structure that specifies which component to use to implement an effect in a movie and how the component is configured.

- __effect track__

  In QuickTime, a modifier track that applies an effect (such as a wipe or dissolve) to a movie. See also [modifier track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi2tm).

- __effect unit__

  In Core Audio, an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) of type`'aufx'` that employs DSP to modify a stream of digital audio. See also [DSP](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyztc).

- __EGID__

  Effective Group ID. See [GID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhaztg).

- __EJB (Enterprise JavaBeans)__

  Enterprise JavaBeans. A specification that provides an infrastructure through which data-based components can be developed and deployed in a variety of platforms.

- __element__

  (1) In an XML file, such as a scripting definition file, a tag-delimited unit of data. (2) In Core Audio, an audio unit programming context nested within a scope. When part of an input or output scope of an audio unit, an element is analogous to a device signal bus—and is sometimes called a _bus_. See also [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq), [scope](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg43tg). (3) In a scripting definition file (or an AppleScript dictionary viewer), a characteristic of an object that refers to a contained collection of related objects. Synonymous with a key-value coding to-many relationship. A `document` object might have a `graphics` element (or to-many relationship).

- __elevation__

  In [surround sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe3tm) and [immersive audio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe2te), the real or apparent vertical angle of an audio source referenced to a line drawn from a listener’s head to a point directly ahead of the listener.

- __ellipsis character__

  Three unspaced periods that appear in menus, buttons, and other controls to indicate that additional information will be required to complete the command. Generate an ellipsis with Option-semicolon.

- __embedded objects__

  Graphics, sound, or movie data that is in a text object along with text data.

- __embedded speech command__

  A command embedded in textual input that a speech synthesizer interprets and applies to the pronunciation of the spoken version.

- __EMMI__

  External Memory Management Interface. Mach’s interface to memory objects that allows their contents to be contributed by user-mode tasks. See also [external pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4zdg).

- __emphasized mini system font__

  The bold version of the mini system font.

- __emphasized small system font__

  The bold version of the small system font.

- __emphasized system font__

  The bold version of the system font.

- __empty list__

  In AppleScript, a list containing no items.

- __enabled control__

  A control state where the control appears normally (that is, not grayed out) and responds to user input when active.

- __Encapsulate transformation__

  In Xcode, a refactoring operation that creates accessors for the transformation item, reduces its visibility, and changes code that directly accesses the item to use the accessors instead.

- __encoding__

  In audio, the algorithmic conversion of a signal from one representation to another. For example, compressing linear PCM data to AAC format is a form of encoding. Can be applied to perceptual or lossless data compression. See also [codec (coder/decoder)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm2dm), [decode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqguyda). Compare [data compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq4dc).

- __encrypt__

  To secure data so that it cannot be read by unauthorized entities, in such a way that its original state can be restored later (decrypted). In most cryptographic systems, encryption and decryption are performed by manipulating the data with a string of bytes called a _key_.

- __encryption__

  The transformation of data into a form in which it cannot be made sense of without the use of some [key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4ti). Such transformed data is referred to as _ciphertext_. Use of a key to reverse this process and return the data to its original (or _plaintext_) form is called _decryption_.

- __endpoint__

  See [MIDI endpoint](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgizti).

- __enterprise object__

  In WebObjects, an object that conforms to the key-value coding protocol and whose properties can map to stored data. An enterprise object brings together stored data with methods for operating on that data.

- __Enterprise Objects__

  Enterprise Objects is a set of frameworks for building feature-rich database applications that encapsulate business logic, yet are independent of any particular data source.

- __entitlement__

  A property that allows an application to access a protected iOS feature or capability.

- __entity__

  In Entity-Relationship modeling, a distinguishable object about which data is kept. An entity typically corresponds to a table in a relational database; an entity’s attributes, in turn, correspond to a table’s columns. An entity is used to map a relational database table to a Java class. See also [attribute](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tc), [table](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgaydm).

- __Entity-Relationship modeling__

  A discipline for examining and representing the components and interrelationships in a database system. Also known as ER modeling, this discipline factors a database system into entities, attributes, and relationships. See also [object-relational mapping](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm2do).

- __EOModeler__

  A tool used to create and edit models.

- __equalization__

  In image manipulation, a histogram operation that makes the resultant image conform to a uniform histogram, ensuring an equal frequency of pixel intensities.

- __erosion__

  In image manipulation, a morphological operation that is similar to dilation. It takes dark pixels in an image and spreads them around, causing them to “eat away” (or erode) objects in an image.

- __error expression__

  In AppleScript, an expression, usually a `text` object, that describes an error.

- __error handler__

  In AppleScript, a collection of statements that are executed in response to an error message.

- __Error Handling pane__

  A pane in the Print dialog that lets the user specify the actions to take when certain errors occur.

- __error message__

  A message that is supplied when an error occurs during the handling of a command.

- __error number__

  An integer that identifies an error.

- __Ethernet__

  A family of high-speed local area network technologies at the physical layer of the OSI model.

- __EUID__

  Effective User ID. See [UID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2ds).

- __evaluation__

  The conversion of an expression to a value.

- __even-odd rule__

  A fill rule that determines when to paint a pixel. The outcome does not depend on the direction that path segments are drawn. Compare [nonzero winding number rule](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmzdo).

- __event__

  (1) A constant that notifies an application that some action is occurring, or has occurred. (2) In AppleScript an action an object can respond to. For example, a button click is an event that may result in execution of a `clicked` handler for the button that was clicked. Compare [SMB/CIFS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha3tg). (3) In Interface Builder, a type of connection that is specific to iOS applications. Events represent different phases of user interaction for a control. Each event connection can also have multiple assigned target objects, each with its own distinct action message.

- __event class__

  The general category an event belongs to, typically associated with an particular action or user-interface element. Example classes are window events and volume events. Compare [event kind](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4ydg).

- __event coalescing__

  See [mouse event coalescing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3dc).

- __event handler__

  A callback procedure or function that processes one or more events.

- __event kind__

  A specific type of event within an event class (for example, a mouse-down event). Compare [event class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4yda).

- __event loop__

  In the Carbon Event Manager, an execution loop that obtains events from the Window Server and places them in an event queue. The event loop also fires timers.

- __event queue__

  A first-in-first-out stack where events pertaining to a thread are stored. Each preemptively scheduled thread has its own event queue.

- __event source__

  An I/O object that corresponds to a type of event that a device driver can be expected to handle; there are currently event sources for hardware interrupts, timer events, and I/O commands. The I/O Kit defines a class for each of these event types, respectively `IOInterruptEventSource`, `IOTimerEventSource`, and `IOCommandGate`.

- __event target__

  An object to which an event is sent. An event target is typically a user-interface element, such as a control or a window.

- __event timer__

  A timer mechanism that fires once, or at periodic intervals, calling a callback procedure when doing so.

- __event track__

  In audio, a stream of MIDI or event data which can be played using a [music player](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi4te). See also [channel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4tq), [sequence](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhazdk).

- __event type__

  The combination of event class and event kind that uniquely identifies an event to the Carbon Event Manager. See also [event class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4yda), [event kind](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4ydg).

- __every reference form__

  In AppleScript, a reference form that specifies every object of a particular type in a container.

- __exception__

  An interruption to the normal flow of program control that occurs when an error or other special condition is detected during execution. An exception transfers control from the code generating the exception to another piece of code, generally a routine called an exception handler.

- __exception port__

  A Mach port on which a task or thread receives messages when exceptions occur.

- __exclusive feature type__

  A feature for which you can choose only one of the available feature selectors, such as whether numbers are to be proportional or fixed-width. Compare [nonexclusive feature type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmzdg).

- __executable__

  An application that uses a project’s product and can be launched in order to debug that product.

- __executable environment__

  Defines how Xcode should execute a product in response to the Go command.

- __execute condition__

  In Xcode, a state that triggers a breakpoint.

- __exit statement__

  In AppleScript, a statement used in the body of a `repeat` statement to exit that statement.

- __explicit run handler__

  In AppleScript, a handler at the top level of a `script` object that begins with `on run` and ends with `end` . A single `script` object can include an explicit `run` handler or an implicit `run` handler, but not both.

- __expression__

  In AppleScript, any series of words that has a value.

- __extension__

  (1) An object module that can be dynamically added to a running system; often used as a synonym for kernel extension. (2) A feature of OpenGL that’s not part of the OpenGL core API and therefore not guaranteed to be supported by every implementation of OpenGL. The naming conventions used for extensions indicate how widely accepted the extension is. The name of an extension supported only by a specific company includes an abbreviation of the company name. If more then one company adopts the extension, the extension name is changed to include `EXT` instead of a company abbreviation. If the OpenGL Architecture Review Board approves an extension, the extension name changes to include `ARB` instead of `EXT` or a company abbreviation.

- __externally framed__

  Describes a [variable bit rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4ts) audio format where information about the sizes of the frames is transmitted separately from the audio data stream. Compare [internally framed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgazdk). See also [webpage template](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2tc).

- __external pager__

  A module that manages the relationship between virtual memory and a backing store. External pagers are clients of Mach’s EMMI. The pager API is currently not exported to user space. The built-in pagers in OS X are the default pager, the device pager, and the vnode pager. See also [EMMI](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy3tc).

- __Extract transformation__

  In Xcode, a refactoring operation that creates a function or method with the selected code as its body.

- __eye coordinates__

  In OpenGL, the coordinate system with the observer at the origin. Eye coordinates are produced by the modelview matrix and passed to the projection matrix.

- __factored application__

  An application that uses a helper tool to perform specific tasks. Interprocess communication mechanisms are used to communicate between processes. In a factored application that uses Authorization Services, the code that performs privileged operations is factored into a separate helper tool.

- __factory__

  A function in a printing plug-in that returns a pointer to an instance of the requested [interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgaytk).

- __FairPlay__

  The [DRM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyzdo) (digital rights management) system built into Apple’s QuickTime technology and used by the iPod music player, the iTunes music application, and the iTunes store. These systems use FairPlay to encrypt some AAC files to restrict their playback to authorized devices.

- __family__

  In the I/O Kit, a collection of software abstractions that are common to all devices of a particular category. Families provide functionality and services to drivers. Examples of families include protocol families (such as SCSI, USB, and Firewire), storage families (disk drives), network families, and families that describe human interface devices (mouse and keyboard).

- __fan out__

  In electronics generally, to direct one output signal to multiple inputs. Audio units cannot perform fan out of this sort. To feed multiple [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) inputs, you direct an audio unit output to a buffer (such as a splitter unit) that has multiple outputs, each of which can connect to a separate audio unit input.

- __fast user switching__

  A feature that allows users on a multiple-user computer to access their desktop, documents, and applications without requiring other logged in users to quit their applications.

- __FAT__

  File allocation table. A data structure used in the MS-DOS file system. Also synonymous with the file system that uses it. The FAT file system is also used as part of Microsoft Windows and has been adopted for use inside devices such as digital cameras.

- __fat files__

  See [universal binaries](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge3dg).

- __fault__

  (1) In the virtual-memory system, faults are the mechanism for initiating page-in activity. They are interrupts that occur when code tries to access data at a virtual address that is not mapped to physical memory. Soft faults happen when the referenced page is resident in physical memory but is unmapped. Hard (or page) faults occur when the page has been swapped out to backing store. See also [page](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqydc), [virtual memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizdi). (2) A type of object in Enterprise Objects that represents a partially formed enterprise object instance. Faults are proxy or stand-in objects that provide performance benefits by delaying the retrieval of data in an enterprise object until it’s absolutely needed.

- __faulting__

  A mechanism used by WebObjects to increase performance whereby destination objects of relationships are not fetched until they are explicitly accessed.

- __favorites bar__

  In the Xcode project window, an area below the toolbar that lets you save frequently accessed items and return to them quickly.

- __feature selectors__

  A means of defining particular font features in a feature type. See also [feature type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4ztq).

- __feature type__

  A group of font features in a style object that are applied to each style run based on font defaults. See also [feature selectors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4zto).

- __fence__

  A token used by the `GL_APPLE_fence` extension to determine whether a given command has completed or not.

- __fetch__

  In Enterprise Objects applications, to retrieve data from the database server into the client application, usually into enterprise objects.

- __fetch specification__

  In Enterprise Objects applications, used to retrieve data from the database server into the client application, usually into enterprise objects.

- __fetch timestamp__

  An attribute of an `EOEditingContext` object that records the time of the most recent fetch of objects into that editing context.

- __FIFO__

  First-in first-out. A data processing scheme in which data is read in the order in which it was written, processes are run in the order in which they were scheduled, and so forth.

- __file descriptor__

  A per-process unique, nonnegative integer used to identify an open file (or socket).

- __file fork__

  A section of a Macintosh file. See also [data fork](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq4de), [resource fork](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy4tm).

- __file GID__

  The [GID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhaztg) associated with a file-system object. Each file-system object has a user ID (the file UID, commonly referred to as the file’s owner), a group ID (the file GID, commonly referred to as the file’s group), and three sets of permission bits, known as owner, group, and other permissions. The first set of bits controls access to the object by the owner, the second controls access by members of the group, and the third controls access by everyone else. See also [process GID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu2ds).

- __File History menu__

  In Xcode, a pop-up menu in the navigation bar that contains all the files that you have viewed in the text editor, with the current file at the top of the list.

- __File Info window__

  In Xcode, the Info window for inspecting and editing settings for file, framework, and folder references.

- __File menu__

  A menu that contains commands that provide housekeeping tasks for files, such as Save As.

- __filename extension__

  A string of characters at the end of a filename, preceded by a period ( `.` ), that characterizes the nature of the file or the structure of its contents.

- __file package__

  A directory that the Finder presents to users as if it were a file. In other words, the Finder hides the contents of the directory from users. This opacity discourages users from inadvertently (or intentionally) altering the contents of the directory. See also [bundle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi2tc).

- __file preview__

  In QuickTime Player, a thumbnail picture from a movie that is displayed in the Open File dialog box. See also [thumbnail picture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3de).

- __file’s group__

  See [file GID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg42dm).

- __file’s owner__

  See [file UID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg43dc).

- __File’s Owner__

  In Interface Builder, the runtime object that manages the contents of a nib file. The File’s Owner is typically a controller object that maintains pointers to key objects in a nib file and responds to user interactions with those objects.

- __file system__

  A part of the kernel environment that manages the reading and writing of data on mounted storage devices of a certain volume format. A file system can also refer to the logical organization of files used for storing and retrieving them. File systems specify conventions for naming files, storing data in files, and specifying locations of files. See also [volume format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgiztk).

- __file-system reference__

  A data object of type `FSRef` designating a file residing on a local or remote file-system volume.

- __file type__

  A four-character code associated with a file that characterizes its nature or the structure of its contents.

- __file type atom__

  An atom of type `'ftyp'`, which defines which file specifications a file is compatible with.

- __File Types preferences pane__

  An Xcode preferences pane that lists all the folder and file types that Xcode handles and the preferred editor for each of those types.

- __file UID__

  The [UID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2ds) of a file system object, used to determine the object’s [permissions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2tc). Each file system object has a user ID (the file UID, commonly referred to as the file’s owner), a group ID (the file [GID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhaztg), commonly referred to as the file’s group), and three sets of permission bits, known as owner, group, and other permissions. The first set of bits controls access to the object by the owner (any process whose effective UID is equal to the file UID); the second controls access by members of the group; and the third controls access by everyone else.

- __fill__

  A drawing operation that paints the area within a path.

- __filling__

  A drawing operation that paints an area contained within a path, using either a solid color or a pattern. Quartz has two rules that it can use to determine whether a point should be filled—the winding number rule and the even-odd rule.

- __filter__

  (1) In Image Kit, code that uses Core Image to process digital images. (2) In vImage, an image process that when applied to an image causes its appearance to change. Many filters use kernel convolution to achieve their effect. Emboss, blur, smooth, and edge detect are all examples of common image filters that use convolution kernels. (3) In AppleScript, a phrase, added to a reference to a system or application object, that specifies elements in a container that match one or more conditions.

- __filter browser__

  The user term for the Image Kit filter browser panel class (`IKFilterBrowserPanel`), which allows users to browse Core Image filters.

- __filtering__

  A process that modifies an image by combining pixels or texels.

- __filter reference form__

  In AppleScript, a reference form that specifies all objects in a container that match a condition specified by a Boolean expression.

- __finalization action__

  An action required after a completed installation process. The possible finalization actions are log-out, restart, and shutdown.

- __Finder__

  The system application that acts as the primary user interface for file-system interaction.

- __firewall__

  Software (or a computer running such software) that prevents unauthorized access to a network by users outside the network. (A physical firewall prevents the spread of fire between two physical locations; the software analog prevents the unauthorized spread of data.)

- __FireWire__

  Apple’s implementation of the IEEE 1394 standard serial bus for connecting digital devices such as cameras and hard drives.

- __first responder__

  In object-oriented programming, the object given the first opportunity to respond to events. The first responder object is determined dynamically at runtime based on several conditions, including which view is selected or has focus and which view is willing to accept certain types of events. If the first responder does not handle an event, it passes the event to other objects in the responder chain.

- __fixed point__

  A point that uses fixed-point numbers to represent its coordinates. QuickTime uses fixed points to provide greater display precision for graphical and image data.

- __fixed-point model__

  A model for extending a continuous selection using Shift-click, in which the user can extend the selection on either side of the insertion point. Compare [addition model](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgazts).

- __fixed-point sample__

  A digital audio [simple message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2tk) that uses a fixed-point numerical representation, such as [8.24](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgaydg). Fixed-point samples support fixed-point arithmetic, which is a less computation-intensive alternative to floating-point arithmetic.

- __fixed-priority policy__

  In Mach, a scheduling policy in which threads execute for a certain quantum of time, and then are put at the end of the queue of threads of equal priority.

- __fixed rectangle__

  A rectangle that uses fixed points to represent its vertices. QuickTime uses fixed rectangles to provide greater display precision.

- __Flash__

  A vector-based graphics and animation technology. Flash data is exported by SWF files.

- __flattened attribute__

  In WebObjects, an attribute that is added from one entity to another by traversing a relationship.

- __flattening__

  The process of copying all of the original data referred to by reference in QuickTime tracks into a QuickTime movie file. This can also be called _resolving references_. Flattening is used to bring in all of the data that may be referred to from multiple files after QuickTime editing is complete. It makes a QuickTime movie stand-alone—that is, it can be played on any system without requiring any additional QuickTime movie files or tracks, even if the original file referenced hundreds of files. The flattening operation is essential if QuickTime movies are to be used with CD-ROM discs.

- __floating input window__

  A window used for text entry by an input method.

- __floating window__

  A window that is similar to a standard Window Manager window except that is occupies a special layer so that it always remains in front of any application windows.

- __flushness__

  See [alignment](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga3do).

- __focus box__

  In Xcode, a box that code focus uses to delineate scopes.

- __focus center__

  In Xcode, code in the text editor at the lowest scope. Code focus highlights a source file’s scope levels using a grayscale.

- __focus ribbon__

  In Xcode, a vertical strip to the right of the gutter in the text editor. You can use the focus ribbon to change where the focus box is.

- __focus ring__

  Highlighting around the onscreen area that is ready to accept user input.

- __fog__

  In graphics, an effect achieved by fading colors to a background color based on the distance from the observer. Fog provides depth cues to the observer.

- __folder__

  A [directory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu3ta) presented to the user in such a way that its contents are accessible (subject to the appropriate permissions) for browsing. Compare [package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm4ta).

- __font__

  A collection of glyphs that usually have some element of design consistency such as the shapes of the counters, the design of the stem, the stroke thickness, or the use of serifs.

- __font attributes__

  A group of flags that modify the behavior or identity of a font.

- __font description__

  A table that contains data that fully describes a font.

- __font family__

  A group of fonts that share certain characteristics and a common family name.

- __font features__

  The set of typographic and layout characteristics that create a specific appearance for a glyph.

- __font ID__

  A value that identifies a font to the font management system. The font ID is assigned to a font at system startup; the specific value does not persist across system startups.

- __font instance__

  A setting identified by the font’s designer that matches specific values along the available variation axes and gives those values a name.

- __font name__

  A set of specific information in a font object about a font, such as its family name, style, copyright date, version, and manufacturer. Some font names are used to build menus in an application, whereas other names are used to identify the font uniquely.

- __font run__

  A contiguous (in memory) sequence of characters having the same font.

- __font variation__

  An algorithmic way to produce a range of typestyles along a particular variation axis.

- __foreign key__

  In relational databases, an attribute in an entity that gives it access to rows in another entity. This attribute must be the primary key of the related entity. For example, an Employee entity can contain the foreign key `deptID` , which matches the primary key in the entity Department. You can then use `deptID` as the source attribute in Employee and as the destination attribute in Department to form a relationship between the entities. See also [primary key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrguzde), [relationship](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy2ts).

- __fork__

  (1) A stream of data that can be opened and accessed individually under a common filename. The Macintosh Standard and Extended file systems store a separate data fork and a resource fork as part of every file; data in each fork can be accessed and manipulated independently of the other. (2) In BSD, `fork` is a system call that creates a new process.

- __formal parameter__

  See [parameter variable](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqzdi).

- __Format menu__

  An optional menu that contains formatting commands.

- __format standard__

  A television video broadcast format standard. DVD Playback Services supports two format standards: the NTSC format used in North America and Japan, and the PAL format used in Europe and other continents.

- __formatting printer__

  The printer displayed in the “Format for” pop-up menu in the Page Setup dialog. The default formatting printer is the generic Any Printer. The printing system provides default page and paper sizes for this printer.

- __Foundation framework__

  A framework that defines a layer of useful primitive object classes, including support for Unicode strings, allocation and deallocation of objects, arrays and collections, dates, ports, and more.

- __four-character code__

  Four bytes of data that can be expressed as a string of four characters in the Mac OS Roman encoding. In AppleScript, used to uniquely identify terms and other items in an application’s scriptability information.

- __fragment__

  In OpenGL, the color and depth values for a single pixel; a fragment can also include texture coordinate values. A fragment is the result of rasterizing primitives.

- __fragmentation__

  In Search Kit, an unwanted increase in index size due to accumulation of unused capacity. Over time, as documents get added to and removed from an index, the index may become fragmented—its constituent documents and terms may become arranged in a manner that includes a significant amount of unused disk or memory space. See also [compact](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm3ta).

- __frame__

  (1) In video, a single image in a sequence of images. (2) In text handling, the viewable area of a text object; the view rectangle. Compare [destination rectangle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqguzta). (3) In Core Audio, a set of samples that contains one sample from each channel in an audio data stream. In the most common case, the samples in a frame are time-coincident—that is, sampled at the same moment. For example, in a stereo stream each frame contains one sample from the left channel and a time-coincident sample from the right channel. More generally, the various channels in a stream, and therefore in a frame, may be from unrelated sources and may have originated at unrelated times. See also [packet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm4to).

- __framebuffer__

  (1) In image display, a highly accessible part of video RAM (random-access memory) that continuously updates and refreshes the data sent to the devices that display images onscreen. (2) In OpenGL, the collection of buffers associated with a window or a rendering context.

- __framebuffer attachable image__

  In OpenGL, the rendering destination for a framebuffer object.

- __framebuffer object__

  An OpenGL extension that allows rendering to a destination other than the usual OpenGL buffers or destinations provided by the windowing system. A framebuffer object (FBO) contains state information for the OpenGL framebuffer and its set of images. A framebuffer object is similar to a drawable object, except that a drawable object is a window-system-specific object whereas a framebuffer object is a window-agnostic object. The context that’s bound to a framebuffer object can be bound to a window-system-provided drawable object for the purpose of displaying the content associated with the framebuffer object.

- __frame rate__

  (1) The rate at which video content is recorded or displayed, in number of frames per second. Frame rates may be fractional. (2) In Core Audio, the number of frames played per second for an audio data stream. Compare [sample rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg42ti).

- __framework__

  A type of bundle that packages a dynamic shared library with the resources that the library requires, including header files and reference documentation.

- __framing__

  See [stroke](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe2dq).

- __free atom__

  An atom of type `'free'`, which you can include in a QuickTime file as a placeholder for unused space.

- __FreeBSD__

  A variant of the BSD operating system.

- __frequency__

  The number of times a repeating phenomenon or activity occurs per unit time. The frequency of a sound wave is determined by the number of wavelengths (or fractions thereof) that pass a particular point per unit time. Sampling frequency indicates the number of digital samples taken per unit time. Frequency is typically measured in Hertz (cycles per second).

- __frustum__

  The region of space that is seen by an observer and that is warped by perspective division.

- __FSAA__

  Full scene anti-aliasing. A technique that takes multiple samples at a pixel and combines them with coverage values to arrive at a final fragment.

- __full keyboard access mode__

  The mode in which tabbing and other keystrokes move keyboard focus to more interface elements than is possible in default keyboard access mode.

- __full-text search__

  In Xcode, search option that looks for the documents whose content matches a search term. The search term can be a word or phrase or may be an elaborate expression using Boolean operators and wildcard characters

- __function key__

  One of the keys with the letter _F_ and a number, plus the Help, Home, Page Up, Page Down, Del, and End keys.

- __Function menu__

  In Xcode, a pop-up menu in the navigation bar that lists the identifiers in the current file.

- __gain__

  In audio, the ratio of output level to the corresponding input level for a device. Level is typically represented in terms of power or voltage, but gain is unitless and is identical whether voltages or powers were used to calculate it. Because gain is a ratio, it is usually described using decibels. A gain of 0 dB indicates no change in level, while a gain of 10 dB is perceived as approximately a doubling in loudness—depending on the nature of the sound and on the initial loudness.

- __gamma correction__

  An operation that changes color intensity values to correct for the nonlinear response of the eye or of a display.

- __GCD__

  Grand Central Dispatch, an OS X technology (available in OS X v10.6 and later) for executing asynchronous tasks concurrently.

-  __`gdb`__

  GNU debugger. `gdb` is a powerful, source-level debugger with a command-line interface. It’s a popular open source debugger and is included with the OS X developer tools.

- __Generic color space__

  A device-independent color space chosen automatically by OS X to produce the best color for the drawing destination.

- __generic password__

  A password other than an Internet password.

- __gesture__

  In Ink Services, a handwritten mark that is recognized as having a special meaning, such as, Select All, Cut, and Copy.

- __GID__

  Group ID. A unique identifier for a collection of users. In [BSD](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgizta), each user can belong to one or more groups. Each file-system object has an associated GID that is used to determine the object’s [permissions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2tc). Each process has an associated [group list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqha2tq). See also [process GID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu2ds).

- __GL__

  The core OpenGL library.

- __global coordinates__

  The coordinate system where the origin is set at the top-left corner of the main viewing screen. Compare [local coordinates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge3ds).

- __global dispatch queue__

  A dispatch queue provided to your application automatically by Grand Central Dispatch (GCD). You do not have to create global queues yourself or retain or release them. Instead, you retrieve them using the system-provided functions.

- __global socket filter__

  In the kernel, a socket filter that is automatically enabled for sockets of the type specified.

- __global variable__

  A variable that is available anywhere in the script in which it is defined.

- __GLU__

  The OpenGL Utilities library.

- __GLUT__

  The OpenGL Utility Toolkit, which is independent of the window system. In OS X, GLUT is implemented on top of Cocoa.

- __GLX__

  An OpenGL extension that supports using OpenGL within a window provided by the X Window system.

- __glyph__

  The distinct visual representation of a character in a form that a screen or printer can display. A glyph may represent one character (the lowercase a), more than one character (the fi ligature), part of a character (the dot over an i), or a nonprinting character (the space character). Compare [character](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmydg).

- __glyph code__

  A number that specifies a particular glyph in a font. Fonts map character codes to glyph codes, which in turn specify individual glyphs.

- __glyph direction__

  The direction in which successive glyphs are read.

- __glyph index__

  The order of a glyph in a line of display text. The leftmost glyph in a line of text has a glyph index of 0; each succeeding glyph to the right has an index one greater than the previous glyph. Compare [edge offset](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy2tm).

- __glyph orientation__

  A value that specifies which direction (vertical or horizontal) glyphs should be drawn.

- __glyph origin__

  The point used to position a glyph when drawing.

- __glyph outline__

  The curves that make up the shape of the glyph.

- __gradient__

  A fill that varies from one color to another. See also [axial gradient](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3to), [radial gradient](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyzda).

- __Grand Central Dispatch__

  [GCD](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvjvomy).

- __grafport__

  See [graphics context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqha2tc).

- __graph__

  (1) in Quartz Composer, a of connected patches on the workspace. (2) In Core Audio, short for [audio processing graph](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tg).

- __graphics context__

  An opaque data type ([CGContextRef](https://developer.apple.com/documentation/coregraphics/cgcontextref)) that encapsulates the information Quartz uses to draw images to an output device, such as a PDF file, a bitmap, or a window on a display. The information inside a graphics context includes graphics drawing parameters and a device-specific representation of the paint on the page.

- __graphics mode__

  In QuickTime, the method by which two overlapping images are blended together to produce a composite image.

- __graphics port__

  A drawing environment defined by a `CGContextRef` for Quartz 2D. The drawing environment contains all the information needed to translate drawing operations from bits in memory to the appropriate destination format (onscreen pixels, PDF, PostScript).

- __graphics state__

  Defines the drawing parameter settings (line width, fill color, and many other parameters) for a specific graphics context.

- __graphics world__

  In QuickTime, a software environment in which a movie track or set of images may be defined before importing them into a movie.

- __group__

  (1) In security, a collection of users. See also [GID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhaztg). (2) In Xcode, a collection of related files in the Groups & Files list. See also [smart group](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha3ta), [source group](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4ti).

- __group box__

  In a dialog, a visual indication that certain controls belong together.

- __group list__

  In security, the list of groups to which the owner of a process belongs plus any additional groups added to the list programatically (for example, using the `setgid` command). If the [file GID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg42dm) of a file system object matches the GID of any group in the group list, that group has group permissions for the object. See also [file UID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg43dc).

- __Groups & Files list__

  In Xcode, a view that contains a list of a project’s contents.

- __GSS-API__

  Generic Security Service Application Program Interface. An open-source API that can be used to adapt an application to use [Kerberos](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga3ts).

- __gutter__

  In Xcode, a vertical strip on the left side of the content pane in the editor. You can use it to quickly locate items in a file. A gutter can display numbers, errors and warning, and breakpoints.

- __HAL__

  Hardware abstraction layer. An object-like interface between Core Audio objects and hardware. The hardware abstraction layer typically addresses hardware by means of an I/O Kit driver, but this is not a requirement. The HAL gives applications a consistent way to communicate with external devices—insulating them from the complexity of addressing multiple, specialized hardware drivers.

- __handler__

  (1) In AppleScript, a named series of one or more script statements that are executed by calling its name. (2) A Java class used by Axis to process a SOAP message or a part of it in a specific way. For example, a handler can be implemented to perform authentication on the message’s sender before allowing it to be processed by the receiver.

- __handler chain__

  In WebObjects, a group of handlers that can be viewed as a unit.

- __handler reference atom__

  A QT atom of type `'hdlr'` that specifies the media handler to be used to interpret a media structure. See also [media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgiytc), [media handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgiytg), [QT atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyyda).

- __hanging baseline__

  The baseline used by Devanagari and similar scripts, where most of the glyph is below the baseline.

- __hanging glyphs__

  A set of glyphs, usually punctuation, that typically extend beyond the left and right margins of the text area and whose widths are not counted when line length is measured.

- __Hangul__

  A Korean subscript that consists of blocks of component glyphs called Jamo, which are characters different from typical character clusters in that they are treated as singular units in memory; there are no principal characters and attachments.

- __Hardware Abstraction Layer__

  See [HAL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqha3dg).

- __hash__

  Number derived from a string such that any change to the string produces a different number.

- __hash algorithm__

  See [cryptographic hash function](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq2tc).

- __head node__

  The final node in an [audio processing graph](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tg) in terms of signal flow; the output node of a graph. See also [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq), [shared workgroup build](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2dk).

- __Head Related Transfer Function__

  See [HRTF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqheydc).

- __headroom__

  In audio, the range, expressed in decibels, between a standard reference signal level and the maximum allowable signal level (the ceiling). See also [dynamic range](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy2ta).

- __help book__

  The collection of HTML files that provide onscreen help for a particular product.

- __Help button__

  A button that opens Help Viewer to the help content appropriate for the context. A help button is a round button with a question mark.

- __helper tool__

  A tool that executes some of an application’s functions as a separate process. In the case of security, a helper tool performs privileged operations for the application. See also [setuid tool](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhaztm).

- __Help Menu__

  A menu that provides access to the onscreen help documentation for an application.

- __help tag__

  A brief text explanation that appears when the user leaves the pointer over an interface element for a few seconds.

- __Help Viewer__

  The simple browser used to display Apple Help HTML files.

- __HFS__

  Hierarchical File System. The Mac OS Standard file-system format, used to represent a collection of files as a hierarchy of directories (folders), each of which may contain either files or other folders. HFS is a two-fork volume format.

- __HFS+__

  Hierarchical File System Plus. The Mac OS Extended file-system format. This format adds support for filenames longer than 31 characters, Unicode representation of file and directory names, and efficient operation on very large disks. HFS+ is a multiple-fork volume format.

- __hierarchical browser__

  The area in the Quartz Composer window used to view and navigate from one level to another in the patch hierarchy.

- __hierarchical menu__

  A menu that includes a menu item from which a submenu descends. Submenus offer additional menu item choices without taking up more space in the menu bar. Hierarchical menus are indicated with a triangle.

- __highlighting__

  The display of text in inverse video or with a colored background. Highlighting in display text corresponds to a selection range in source text.

- __hints__

  Information provided with a font that can be used to scale glyphs to various sizes.

- __hint track__

  A track in a QuickTime streaming movie that contains information for a packetizer about the data units to stream. See also [stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe2dg).

- __histogram__

  A diagram that shows the frequency of occurrences within a data set. In the graphics domain, histograms can be used to plot the frequencies of certain pixel intensities.

- __HIToolbox__

  Human Interface Toolbox. A collection of procedural APIs that apply an object-oriented model to windows, controls, and menus for Carbon applications. The HI Toolbox supplements older Macintosh Toolbox managers such as the Control Manager, Dialog Manager, Menu Manager, and Window Manager from Mac OS 9.

- __hit-testing__

  The process of converting a location within a line of display text into a caret offset in the source text of that line.

- __horizontal reflect__

  A type of geometric operation that reflects an image about its y-axis.

- __horizontal shear__

  In image processing, a filter that shifts pixels along the x-axis to create an effect that’s similar to physical shearing.

- __host__

  (1) The computer that is running (is host to) a particular program or service. The term is usually used to refer to a computer on a network. (2) In debugging, the computer that is running the debugger itself. In this context, the target is the machine running the application, kernel, or driver being debugged.

- __host application__

  A Mac app that loads and uses audio units. See also [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq).

- __host processor__

  The microprocessor on which an application program resides. When an application is running, the host processor may call other, peripheral microprocessors, such as a digital signal processor, to perform specialized operations.

- __host time__

  The clock time used by the computer running an audio application.

- __hot spot__

  (1) The portion of the pointer that must be positioned over a screen object for mouse clicks to have an effect on the object. (2) An area, typically in a VR presentation, that the user can click to invoke an action.

- __hot zone__

  The area of an onscreen object that the pointer’s hot spot must be within for mouse clicks to have an effect.

- __HRTF__

  Head related transfer function. Also called _Anatomical Transfer Function_, or _ATF_. A mathematical description of the frequency and phase filtering that takes place when an acoustic signal impinges on a person’s head and pinnae. The HRTF is used in DSP to add spatialization information to a signal. See also [DSP](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyztc), [panning](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqytq), [spatialization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4tq).

- __HTTP__

  Hypertext Transfer Protocol. The client-server TCP/IP protocol used on the web for the exchange of HTML documents.

- __HTTP adaptor__

  A process (or a part of one) that connects WebObjects applications to a web server.

- __HTTP server__

  See [web server](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2te).

- __hybrid metapackage__

  A metapackage that contains a distribution script. This type of installer package behaves as a distribution package when installed on computers running OS X v10.4 and later. On computers running earlier versions of the operating system, a hybrid metapackage behaves as a regular metapackage. See also [distribution package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4dq), [metapackage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgizds).

- __hypertext__

  Action media that contains a URL and takes the user to a website.

- __hyphenation point__

  An entry in an array of edge offsets in source text at which it is appropriate to break a line of display text.

- __I/O__

  Input/output. (1) The exchange of data between two parts of a computer system, usually between system memory and a peripheral device. (2) The software- or hardware-based audio inputs and outputs for a device.

- __I/O Catalog__

  A dynamic database that maintains entries for all available drivers on a Darwin system. Driver matching searches the I/O Catalog to produce an initial list of candidate drivers.

- __I/O Kit__

  A kernel-resident, object-oriented environment in Darwin that provides a model of system hardware. Each type of service or device is represented by one or more C++ classes in a family; each available service or device is represented by an instance (object) of that class.

- __I/O Kit framework__

  The framework that includes IOKitLib and makes the I/O Registry, user client plug-ins, and other I/O Kit services available from user space. It lets applications and other user processes access common I/O Kit object types and services. See also [framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhaytm)

- __I/O module__

  A module used by the printing system to provide a way to communicate with a printer using a standard interface for a transport type.

- __I/O Registry__

  A dynamic database that describes a collection of driver objects, each of which represents an I/O Kit entity. As hardware is added to or removed from the system, the I/O Registry changes to accommodate the addition or removal.

- __I/O service thread__

  See [interrupt service thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgazte).

- __icon button__

  A button that does not have a rectangular edge around it; the clickable region is the graphic (for example, the toolbar buttons in System Preferences windows).

- __icon genre__

  A group of icons that share similar visual design characteristics used to designate a particular category of items.

- __IDE__

  Integrated development environment. A program that typically combines text editing, compiling, and debugging features in one package in order to assist developers with the creation of software.

- __ideal metrics__

  Resolution-independent measurements used to describe how a glyph is drawn. Compare [screen metrics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg43ti).

- __identification__

  The process by which a process verifies that a person or entity is the same one it communicated with previously. Identification is in general faster than [authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3de) and does not require interaction with the user. In [Kerberos](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga3ts), for example, the authentication server authenticates a user and issues a credential (called a _ticket-granting ticket_), which can be used later for identification so that reauthentication is not necessary.

- __identifier__

  In AppleScript, series of characters that identifies a value or handler. Identifiers are used to name variables, handlers, parameters, properties, and commands.

- __identity__

  A digital certificate together with an associated private key.

- __identity matrix__

  In image processing, a transformation matrix that specifies no change in the coordinates of the source image. The resulting image corresponds exactly to the source image. See also [transformation matrix](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgezdg).

- __identity transform__

  An affine transform that, when applied to input coordinates, always returns the input coordinates.

- __idle sleep__

  A sleep state that occurs when there has been no device or system activity for the period of time the user specifies in the Energy Saver pane of System Preferences. See also [system sleep](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgaydi).

- __ID reference form__

  In AppleScript, a reference form that specifies an object by the value of its ID property.

- __IEC__

  International Electrotechnical Commission. An international standards organization, founded in 1906, that collaborates with [ISO](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga2di) on defining a wide variety of [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2dq) formats.

- __IEEE__

  Institute of Electrical and Electronic Engineers. An organization of electronics professionals that has established many technology and audio-related standards. Pronounced “eye triple-e.”

- __IEEE 1394__

  See [FireWire](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg43tc).

- __if statement__

  A control statement that contains one or more Boolean expressions whose results determine whether to execute other statements within the `if` statement.

- __IFF__

  Interchange File Format. A flexible, chunk-based file format for storing media content. Developed by Electronic Arts, Inc., and the technical inspiration for Apple’s [AIFF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga3dc).

-  __`ifnet` structure__

  A data structure containing function pointers and data related to a particular network interface.

- __ignore condition__

  A state that triggers a breakpoint only if the condition is true.

- __ignoring statement__

  A control statement that lists a specific set of attributes to be ignored when AppleScript performs operations on text strings or sends commands to applications.

- __IMA ADPCM__

  Interactive Multimedia Association ADPCM. A lossy, 16-bit audio compression format that provides 4:1 compression. The format is sometimes referred to as _IMA_ or _IMA4_. See also [ADPCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga2di).

- __image__

  A group of related pixels, often represented with a rectangular array of values.

- __imageable area__

  The part of the paper to which a printer can draw without the image being clipped.

- __image bounding rectangle__

  The smallest rectangle that completely encloses the filled or framed parts of a block of text. See also [typographic bounding rectangle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2dg).

- __image browser view__

  The Image Kit view class (`IKImageBrowserView` ) that is optimized for browsing images. The user term is _image browser_.

- __image buffer__

  An abstract buffer type that holds Core Video images. Pixel buffers, Core Video OpenGL buffers, and OpenGL textures derive from the CVImageBuffer type.

- __Image Edit panel__

  The Image Kit edit panel class (`IKImageEditPanel` ), which is optimized for editing images. The user term is _Image Edit window_.

- __image format__

  An image encoding standard that specifies the number of color channels and number of bits per channel.

- __Image I/O__

  A framework (`ImageIO.framework` ) that provides opaque data types for reading data from an image source and writing data to an image destination.

- __Image Kit__

  A programming interface that supports browsing, viewing, and editing images and browsing and controlling Core Image filters.

- __image mask__

  A bitmap that specifies an area to paint, but not the color. An image mask acts like a stencil to specify where to place color on the page.

- __image sequence__

  A series of visual representations usually represented by video over time. Image sequences may also be generated synthetically, such as from an animation sequence.

- __image track__

  Any track in a QuickTime movie that contains visual images. The term particularly applies to video tracks that contain VR data.

- __image unit__

  A Core Image filter that is packaged for distribution as an`NSBundle` object. Image units contain one or more filters for manipulating image date. See also [SIMD](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2tg).

- __image well__

  A rectangular, recessed area that displays an icon or picture and that serves as a drag-and-drop target.

- __imaging system__

  The system used to render text or graphics.

- __immediate mode__

  The practice of OpenGL executing commands at the time an application issues them. To prevent commands from being issued immediately, an application can use a [display list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4da).

- __immersive audio__

  Sound reproduction or generation that seems to surround a listener. See also [surround sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe3tm).

- __impedance__

  (1) In electronics, the amount of opposition a circuit presents to an AC (alternating current) signal at a given frequency. Impedance includes both a resistive (frequency-independent) and a reactive (frequency-dependent) component. (2) In acoustics, the ratio of average sound pressure to particle velocity over a given surface area and at a given frequency.

- __implicitly specified subcontainer__

  An object container that can be specified in an AppleScript script by context, rather than by an explicit reference. For example, explicitly specifying a `word` object in a `document` object might require this script reference: `fourth word of text of front document` . But if the application provides support for implicitly specifying the `text` container, the script reference can be simplified to this: `fourth word of front document` .

- __implicit run handler__

  In AppleScript, all the statements at the top level of a script except for property definitions, `script` object definitions, and other handlers. A single `script` object can include an explicit `run` handler or an implicit `run` handler, but not both.

- __imposed width__

  A control feature that forces a specific width onto the glyphs of a style run, regardless of its text content or other style properties.

- __inactive__

  In iOS, used to describe an audio session state in which playback or recording cannot proceed. Compare [active](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgazdo).

- __inactive window__

  A window that is in the background of other windows. Although some of its controls can be activated (click-through) and it can be a drag-and-drop target, an inactive window is not the focus of the user’s attention.

- __in-band__

  Said of communication on a socket or interface that contains actual data destined for the endpoint (for example, `send` and `recv` calls). Compare [out-of-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm4de).

- __inclusion/exclusion result__

  See [inclusion/exclusion searching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe3dc).

- __inclusion/exclusion searching__

  Unranked searching where the result simply includes documents that match the query and excludes documents that don’t. Inclusion/exclusion searches tend to be faster than ranked searches. Search Kit supports inclusion/exclusion searches. See also [relevance-based result](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy3dk).

- __index__

  In Search Kit, a memory- or file-based sequential collection of the terms in one or more documents. In addition to terms, Search Kit indexes contain context information that specifies which documents each term belongs to, along with term and document metadata useful during display of search results. Search Kit performs its searching and analysis on indexes. See also [inverted index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgaztk), [inverted-vector index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgaztm), [vector index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgiydk).

- __index group__

  A short-lived collection of one or more indexes; the target of a search. An index group corresponds to one or more aspects of the corpus of documents you want to search. For example, one index in a group might contain document titles, while another contains the body text of those same documents. An index group can also comprise indexes of multiple corpora. See also [corpus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq2dc).

- __index reference form__

  In AppleScript, a reference form that specifies an object by describing its position with respect to the beginning or end of a container.

- __indicator__

  The part of a control that visually represents its value. For example, on a scroll bar control, the scroller is the indicator.

- __info plist__

  See [information property list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe3do).

- __information property list__

  A property list that contains essential configuration information for bundles such as kernel extensions. A file named `Info.plist` (or a platform-specific variant of that filename) contains the information property list and is packaged inside the bundle. See also [bundle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi2tc), [property list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu3ti).

- __information retrieval__

  See [signal-to-noise ratio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2te).

- __Info window__

  A window in the Finder and other applications that presents information about and provides settings for a particular entity. In Interface Builder, an Info window has settings related to the attributes and connections for the associated user interface object. In Xcode Info windows, users can manipulate information about a project item, such as files, targets, and the project itself.

- __inheritance__

  (1) In object-oriented programming, the ability of a superclass to pass its characteristics (methods and fields) on to its subclasses, allowing subclasses to reuse these characteristics. (2) In AppleScript, the ability of a child `script` object to take on the properties and handlers of a parent object.

- __inheritance attribute__

  In Mach, a value indicating the degree to which a parent process and its child process share pages in the parent process’s address space. A memory page can be inherited as copy-on-write, shared, or not at all.

- __inheritance chain__

  The hierarchy of objects that AppleScript searches to find the target for a command or the definition of a term.

- __initialize__

  (1) In Core Audio, to configure an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) for use. (2) In AppleScript, to create a `script` object from the properties and handlers listed in a `script` object definition. AppleScript creates a `script` object when it runs a script or handler that contains a `script` object definition.

- __initialize__

  In Core Audio, to configure an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) for use.

- __initializing a script object__

  The process of creating a `script` object from the properties and handlers listed in a `script` object definition. AppleScript creates a `script` object when it runs a script or handler that contains a `script` object definition.

- __Ink__

  In the Ink technology, raw data that represents the input drawn by the user with the stylus.

- __Ink input method__

  In the Ink technology, a low-level task that takes the user input and then draws the appropriate data on the screen. In effect, converting physical pen strokes into electronic ink.

- __Ink pad__

  The part of the Ink window that provides a simple note pad interface where handwritten input is converted into editable text.

- __Ink phrase__

  In the Ink technology, the grouping of ink data created by the recognition system, based on the timing and spacing of the user’s handwriting. In Roman languages, an Ink phrase is typically a short string of characters with no spaces between them such as an individual character, several characters, a word, or, an entire URL. For most situations, an Ink phrase is equivalent to a word.

- __Ink server__

  The component of Ink technology that manages the recognizer, the language model, and the Ink window.

- __Ink text__

  In the Ink technology, words written in electronic ink.

- __Ink text object__

  An opaque object that contains information about an Ink phrase.

- __Ink toolbar__

  The toolbar that appears at the top of the Ink window.

- __Ink window__

  The Ink toolbar plus the Ink pad. The window allows the user to control various aspects of Ink and to enter Ink input.

- __Ink writing guides__

  In the Ink technology, the lines (alternating solid and broken) that appear when a user is writing directly into an application.

- __in-line data__

  Data that’s included directly in a Mach message, rather than referred to by a pointer. Compare [out-of-line data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm4dg).

- __inline input__

  An input method that allows the user to enter text directly into a document. In inline input, entry and conversion of characters take place at the current line position—where the converted text is intended to appear—rather than in a separate window. Inline input is the principal example of the kind of text service supported by the Text Services Manager. Compare [bottomline input](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgizdi).

- __input audio queue__

  See [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2ti).

- __input map__

  A QuickTime data structure that describes where to find information about tracks that are targets of a modifier track. See [modifier track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi2tm).

- __input method__

  A software module for multiple-byte script systems that converts phonetic or syllabic characters, entered from a keyboard, into ideographic or other complex representation of text. Because multiple-byte script systems have too many characters to be entered directly from a keyboard, the input method uses a conversion technique, such as translating sequences of phonetic characters that are typed into a special input window. For example, the Japanese script system provides software for transcribing Kana (phonetic Japanese) into ideographic Kanji.

- __input order__

  The order in which characters are written or entered from a keyboard. The input order of a line of text can differ from its display order. Compare [display order](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4de).

- __input source__

  A source of asynchronous events for a thread. Input sources can be port-based or manually triggered and must be attached to the thread’s run loop.

- __insertion point__

  (1) The point at which text or other data is to be inserted or deleted. An insertion point is specified by a single caret position. Compare [caret](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3do). (2) In AppleScript, the location where another object or objects can be added.

- __installation action__

  A task to be performed before or after an installation. PackageMaker defines several installation actions, including Quit Application and Show File in Finder.

- __installation destination__

  The directory in which Installer places a package’s payload.

- __installation host__

  The computer onto which a package is to be installed.

- __installation package__

  A file package with the `.pkg` or `.mpkg` extension. Installation packages (also known as packages) contain products or product components (known as the package’s payload) and installation information used by the Installer application and Remote Desktop to place product files on a file system.

- __installation property__

  Information in an installation package that specifies an installation requirement or an installation process detail, such as whether relocation is allowed.

- __installation receipt__

  A token that Installer uses to determine whether a component has already been installed on an installation volume.

- __installation requirement__

  A condition that the target computer or volume of an installation must meet in order for the installation to take place. The two types of installation requirements are system requirements and volume requirements.

- __installation volume__

  The volume (or mountpoint) onto which an installation package is to be installed.

- __install choice__

  An option users can select or deselect as part of the installation process to specify whether a product component is to be installed.

- __install customization pane__

  A pane users see while interacting with the Installer application if the package being installed allows the user to customize the installation by choosing the product components to be installed. See also [product component](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu2ti), [product package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu2to).

- __install experience__

  The tasks a user needs to perform in order to install a product on their computer.

- __install operation__

  Installation activity performed by an executable file that is invoked at a specific point during the installation process.

- __install operation executable__

  An executable file that is invoked by Installer during an installation, before or after copying a package’s payload to the installation destination.

- __Installer package database__

  System-level database of all the installation packages installed by the Installer application.

- __instance__

  In object-oriented languages such as Java and Objective-C, an object that belongs to (is a member of) a particular class. Instances are created at runtime according to the specification in the class definition.

- __instant mousing area__

  In the Ink technology, an area in which stylus input is interpreted as mouse input; the system “instantly” interprets the stylus as a mouse in these special places and ink is not generated.

- __instrument__

  A data-gathering agent developed using the Instruments application. Instruments collect performance information about an application or an entire system.

- __Instruments__

  An integrated performance analysis and debugging tool. Instruments lets you gather a configurable set of metrics while your application is running, providing you with visualization tools to analyze the data and see performance problems and potential coding errors within your software.

- __Instruments application__

  See [Instruments](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgaytc).

- __instrument unit__

  In Core Audio, an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) of type`'aumu'` that takes sound bank data and MIDI control data as inputs, and outputs digital audio.

- __integer__

  A positive or negative number without a fractional part.

- __interface__

  The calling conventions by which a client accesses a service. An interface provides a level of abstraction that hides the implementation details of the service from the client.

- __Interface Builder__

  An application that helps you easily create application menus, windows, dialogs, palettes, and other standard Aqua interface elements.

- __interface filter__

  A filter attached to a particular interface [Unicode decomposition](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2ti). An interface filter alters [in-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe2ts) and [out-of-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm4de) communication specific to a given interface.

- __interface KEXT__

  A network kernel extension that provides routines specific to a particular family of interfaces, such as ARP equivalence routines.

- __interface layer__

  A layer above the driver layer containing interface KEXTs, interface filters, and protocol plumbers.

- __interface object__

  In Interface Builder, an object in a nib file that is created for your application at load time. Interface objects can consist of both visual objects (such as windows, views, and menus) and nonvisual objects (such as controllers).

- __interlacing__

  A video mode that updates half the scan lines on one pass and goes through the second half during the next pass.

- __interleaved data__

  In image processing, arrays of dissimilar data that are grouped together, such as vertex data and texture coordinates. Interleaving can speed up data retrieval.

- __interleaved image format__

  A format that encodes each color (and alpha) channel, one after the other, for every pixel. In contrast to planar image formats which encode an entire image using one color at a time, interleaved image formats alternate through each channel, encoding data for all channels simultaneously within each pixel. For example, an interleaved image would encode an image in a RGBRGBRGB fashion, whereas a planar image would encode the same image as RRRGGGBBB.

- __interleaving__

  (1) In digital audio, converting a set of data streams representing discrete channels into a single stream that retains the capacity to be converted back to separate channels. A synonym for _multiplexing_. In Audio Converter Services and in audio file formats such as CAF, interleaving involves placing one [sample](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg42ta) from each channel in sequence such that a set of coincident samples, one from each channel represented in the data stream, appears in each frame. Compare [deinterleaving](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqguytk). (2) In QuickTime, a technique in which sound and video data are alternated in small pieces, so the data can be read off disk as it is needed. Interleaving allows for movies of almost any length to have little delay on startup.

- __internally framed__

  In audio, describes a variable-bit-rate audio format where information about the sizes of the frames is included in the audio data stream. Compare [externally framed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4zde). See also [webpage template](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2tc), [variable bit rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4ts).

- __internationalization__

  The design or modification of a software product, including its online help and documentation, to facilitate localization. Internationalization of software typically involves writing or modifying code to make use of locale-aware operating-system services for appropriate localized text input, display, formatting, and manipulation. See also [localization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge3ta).

- __Internet password__

  A password for an Internet server, such as a web or FTP server. Internet password items on the keychain include attributes such as the security domain and IP address.

- __interpolation__

  The calculation of intermediate values relative to known beginning and ending values.

- __interprocess communication__

  See [source control](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4te).

- __interrupt__

  An asynchronous event that suspends the currently scheduled process and temporarily diverts the flow of control through an interrupt handler routine. Interrupts can be caused by both hardware (I/O, timer, machine check) and software (supervisor, system call, or trap instruction).

- __interrupt handler__

  A routine executed when an interrupt occurs. Interrupt handlers typically deal with low-level events in the hardware of a computer system, such as a character arriving at a serial port or a tick of a real-time clock.

- __interrupt service thread__

  A thread running in kernel space for handling I/O that is triggered by an interrupt, but does not run in an interrupt context. Also called an _I/O service thread_.

- __inverse relationship__

  A relationship that goes in the reverse direction of another relationship. Also known as a _back relationship_.

- __inversion__

  In graphics, an operation that produces original coordinates from transformed ones.

- __inverted index__

  In Search Kit, an index containing terms, as keys, mapped to references to the documents they appear in. The index is sorted by its keys. “Inverted” means that the documents are found by matching on terms, rather than the other way around. See also [index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe3de), [inverted-vector index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgaztm), [vector index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgiydk).

- __inverted-vector index__

  In Search Kit, an index containing terms mapped to document URL objects representing the documents that the terms appear in, as well as document URL objects mapped to the terms that each document contains. See also [index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe3de), [inverted index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgaztk), [vector index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgiydk).

- __IP filter__

  A filter that alters IP traffic each time it enters the protocol stack. By its very nature, an IP filter can only filter [in-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe2ts) communication.

- __IPC__

  Interprocess communication. A set of programming interfaces that enables a process to communicate data or information to another process. Mechanisms for IPC exist in the various layers of the system, from Mach messaging in the kernel to distributed notifications and Apple events in the application environments. Each IPC mechanism has its own advantages and limitations, so it is not unusual for a program to use multiple IPC mechanisms. Other IPC mechanisms include pipes, named pipes, signals, message queueing, semaphores, shared memory, sockets, the Clipboard, and application services.

- __iOS Dev Center__

  An Apple developer center that provides all the resources needed to develop iOS applications. Access to this developer center requires an ADC membership. See also [user focus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4dk).

- __iOS Developer Program__

  A program that allows you to develop iOS applications, test them on devices, and distribute them to your customers through the App Store.

- __iOS Simulator application__

  An application that simulates the iOS runtime environment and user experience in OS X for testing iOS applications in early stages of development.

- __IPL__

  Interrupt priority level. A means of basic synchronization on uniprocessor systems in traditional BSD systems, set using the`spl`macro. Interrupts with lower priority than the current IPL are not acted upon until the IPL is lowered. In many parts of the kernel, changing the IPL in OS X is not useful as a means of synchronization. New use of`spl`macros is discouraged. See also [spl macro](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrheytg).

- __IR__

  Information retrieval. The process of locating information based on a well-defined information need. An information retrieval system consists of a corpus, one or more indexes of its content, a query interface, a search system, and a results interface.

- __ISO__

  A standards organization, called _International Organization for Standardization_ in English, that formulates and promotes industrial and commercial standards, including those for multimedia data formatting and transmission, such as JPEG, MP3, and MPEG. Pronounced “EYE-so.”

- __iSync__

  A tool for synchronizing address book and calendar information.

- __item__

  (1) In Launch Services, an application, document, or URL to be operated on. (2) In AppleScript, a value in a list or record. An item can be specified by its offset from the beginning or end of the list or record.

- __item information record__

  A data structure of type `LSItemInfoRecord` , used by Launch Services to return information about an [item](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga2dm).

- __J2EE__

  Java 2 Platform, Enterprise Edition. A specification that defines a platform for the development and deployment of web applications. It describes an environment under which enterprise beans, servlets, and JSP pages can share resources and work together.

- __Jamo__

  An individual phonetic glyph in the Korean script that is transformed and combined into clusters called Hangul.

- __JAR__

  Java archive. A file created using the `jar` utility (and saved with the `.jar` extension) that contains all the files that make up a Java application.

- __Java__

  A development environment for creating applications that can be seen in both standalone and networked environments.

- __Java Client__

  A WebObjects development approach that allows you to create graphical user interface applications that run on the user’s computer and communicate with a WebObjects server.

- __Java Foundation Classes__

  See [JFC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga3dc).

- __JavaMonitor__

  A tool used to configure and maintain deployed WebObjects applications capable of handling multiple applications, application instances, and applications hosts at the same time.

- __Java Native Interface__

  See [source file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4tg).

- __Java virtual machine__

  See [source group](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4ti).

- __JAXP__

  Java API for XML Processing. A specification that provides an API for processing XML documents.

- __JBoss__

  A Java-based open-source application server capable of deploying J2EE-based applications. JBoss provides many useful features in addition those defined in the J2EE standard, including support for clustering, session replication, mail, and security.

- __JDBC__

  Java Database Connectivity. An interface between Java platforms and databases.

- __JDBC adaptor__

  A datasource adaptor that allows WebObjects applications to connect to JDBC-compliant database management systems.

- __JFC__

  Java Foundation Classes. A set of graphical user interface components and services written in Java. The component set is known as _Swing_.

- __jitter__

  In audio, time-based inconsistencies in the clock signal or clock component in a digital signal stream. In digital audio, jitter can result in audible [distortion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4dm).

- __JMS__

  Java Message Service. A Java-based programming interface that implements an asynchronous message-exchange system. It facilitates the development of message-based applications. JMS is part of the J2EE platform.

- __JNI__

  Java Native Interface. A technology for bridging C-based code with Java.

- __job ticket__

  The top-level ticket used for a print job. See also [ticket](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3di).

- __join__

  In relational databases, an operation that provides access to data from two tables at the same time, based on values contained in related columns.

- __joinable thread__

  A thread whose resources are not reclaimed immediately upon termination. Joinable threads must be explicitly detached or be joined by another thread before the resources can be reclaimed. Joinable threads provide a return value to the thread that joins with them.

- __JPEG__

  Joint Photographic Experts Group. An international standard for compressing still images. This standard supplies the algorithm for image compression. The version of JPEG supplied with QuickTime complies with the baseline ISO standard bitstream, version 9R9. This algorithm is best suited for use with natural images.

- __JSP__

  JavaServer Pages. A technology that facilitates the development of dynamic web pages and web applications that use existing components, such as JavaBeans and WebObjects components.

- __justification__

  The process of typographically expanding or compressing a line of text to fit a text width.

- __justification gap__

  The difference in the length of a line before and after justification.

- __justification override__

  The degree to which a text layout system should override justification behavior for glyphs in a style run.

- __justification priority__

  The priority order in which classes of glyphs are processed during justification.

- __JVM__

  Java virtual machine. The runtime environment for executing Java code. This environment includes a just-in-time bytecode compiler and utility code.

- __kashida__

  An extension-bar glyph that is added to certain Arabic glyphs during justification.

- __KDC__

  Key distribution center. In Kerberos, the sum of two separate software processes: the [ticket-granting server](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3dk) and the [authentication server](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3dg).

- __KDP__

  The kernel shim used for communication with a remote debugger ( `gdb` ).

- __kerberized service__

  A service that has been configured to accept [Kerberos ticket](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4da)s for identification.

- __Kerberos__

  An industry-standard protocol created by the Massachusetts Institute of Technology (MIT) to provide authentication over a network. It is a symmetric-key, server-based protocol and is used widely in Macintosh, Windows, and UNIX networks.

- __Kerberos ticket__

  A credential used to identify a user who has been previously authenticated so that reauthentication is not needed. In [Kerberos](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga3ts), the [KDC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga3tm) (key distribution center) issues the user a [TGT](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2to) (ticket-granting ticket) when they first authenticate. Thereafter, when they need to access a secure server, they present the ticket-granting ticket to the KDC and are issued a ticket, which they present to the secure server as identification. See also [authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3de), [identification](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqheyts).

- __Kerberos Ticket Viewer__

  A utility available through the Keychain Access utility that shows any Kerberos tickets in use on the system and enables the user to renew or destroy a ticket or change a ticket’s password.

- __kernel__

  (1) The complete OS X core operating-system environment, which includes Mach, BSD, the I/O Kit, file systems, and networking components. Also called the _kernel environment_. (2) In image processing, a grid of numbers used in both convolution and morphological operations (such as dilation and erosion). It is typically represented as a square grid (or matrix) whose height and width are both odd, such as a 3 x 3 grid. Each cell in the grid contains a number. An image process that uses a kernel typically takes these numbers within the kernel and applies them to the image by undergoing a series of arithmetic operations between the kernel values and the image pixel intensity values.

- __kernel crash__

  An unrecoverable system failure in the kernel caused by an illegal instruction, memory access exception, or other failure rather than explicitly triggered as in a panic. Compare [panic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqytm).

- __kernel extension__

  See [KEXT](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4te).

- __kernel mode__

  See [supervisor mode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe3tg).

- __kernel module__

  See [KMOD](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgeytm).

- __kernel panic__

  See [panic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqytm).

- __kernel port__

  A Mach port whose receive right is held by the kernel. See also [task port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgmyda), [thread port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2ts).

- __kernel space__

  The protected memory partition in which the kernel resides. See also [user space](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4dq).

- __kerning__

  An adjustment to the normal spacing that occurs between two or more specifically named glyphs, known as the _kerning pair_.

- __kerning pair__

  Two specifically named glyphs that are kerned together by a set amount. See also [kerning](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4ta).

- __KEXT__

  Kernel extension. A dynamically loaded bundle that extends the functionality of the kernel. The I/O Kit, file system, and networking components of Darwin can be extended by KEXTs.

- __KEXT binary__

  See [KMOD](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgeytm).

- __key__

  (1) An arbitrary value (usually a string) used to locate a piece of data in a data structure such as a dictionary. (2) In security, a piece of secret information required to decode an encrypted message. In modern cryptographic methods, it is usually a lengthy integer.

- __keyboard and font synchronization__

  A process by which the current keyboard script is compared to the script of the font at the current insertion point. If the two don’t match, one or the other is changed so the two scripts are the same. In most cases, when the user starts typing, the font is automatically replaced with one belonging to the keyboard script, although it is possible to synchronize in the other direction.

- __keyboard focus__

  The state in which a window or control receives keystrokes. Keyboard input is directed to one window (and one control within the window) at a time.

- __keyboard glyph__

  A graphical representation of a physical key that doesn’t have a character equivalent (such as a function key or the Shift key).

- __keyboard script__

  The script system for keyboard input. It determines the character input method and the mapping of keystrokes to character codes. The keyboard script may be different from the script used to display text.

- __keychain__

  A database in OS X and iOS used to store encrypted passwords, private keys, and other secrets. It is also used to store certificates and other nonsecret information that is used in cryptography and authentication. The Keychain Manager and Keychain Services are public APIs that can be used to manipulate data in the keychain, and the Keychain Access utility is an application that can be used for the same purpose. See also [keychain item](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgeydc)

- __Keychain Access__

  A utility that allows users to create, delete, and modify keychains and keychain items.

- __keychain item__

  A secret that is encrypted and protected by the keychain, plus its associated attributes and access object. Each keychain item has a class that determines what attributes it has; for example Internet password items include an IP address attribute. The password or other secret stored as a keychain item is encrypted and is inaccessible when the keychain is locked. When the keychain is unlocked, the secret can be read by the trusted applications listed in the item’s access object and by the user (with the Keychain Access utility). The attributes are not currently encrypted.

- __Keychain Services__

  The programming interface used to create, delete, and modify keychains and keychain items.

- __key distribution center__

  See [KDC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga3tm).

- __key-down event__

  An event indicating the user pressed a key.

- __key frame__

  In QuickTime, a sample in a sequence of temporally compressed samples that does not rely on other samples in the sequence for any of its information. Key frames are placed into temporally compressed sequences at a frequency that is determined by the key frame rate. Typically, the term key frame is used with respect to temporally compressed sequences of image data. See also [key frame rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgeydo), [stencil buffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhezts).

- __keyframe animation__

  An animation that specifies an array of values that an animation uses as sequential targets.

- __key frame rate__

  The frequency with which key frames are placed into temporally compressed data sequences. See also [key frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgeydk).

- __keypath__

  A chain of keys supported by key-value coding that allows for the traversal of relationships between enterprise objects. See also [KVC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgeytq).

- __key-repeat__

  The repetition of a character when the user holds down a key representing that character.

- __key signing__

  In public key cryptography, electronically stating your trust that a public key really belongs to the person who claims to own it, and potentially that the person who claims to own it really is who he or she claims to be.

- __key-up event__

  An event indicating the user released a key.

- __key-value coding__

  See [KVC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgeytq).

- __key window__

  The window that currently accepts input from the keyboard.

- __keyword__

  (1) A word that is an explicit part of a programming language; also called a _reserved word_. (2) In a PostScript printer description file, a string used to describe a printer—for example, `*PageSize` and `*Font` . (3) A four-character code used by the Apple Event Manager to identify a specific descriptor within an Apple event.

- __kind string__

  A string used (in the Finder’s Get Info window, for example) to characterize the general nature of an item, such as `Application`, `Folder`, `Alias`, `JPEG Picture`, or `QuickTime Movie`.

- __KMOD__

  Kernel module. A binary in Mach-O format that is packaged in a KEXT (kernel extension). A KMOD is the minimum unit of code that can be loaded into the kernel. Also called a _KEXT binary_. See also [KEXT](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4te).

- __KPI__

  Kernel programming interface. A group of opaque data types and accessor functions designed to maintain binary compatibility across OS releases.

- __KVC__

  Key-value coding. A mechanism used in Cocoa and WebObjects for accessing object properties indirectly by key. See also [keypath](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgeydq).

- __labeled parameter__

  In AppleScript, a parameter that is identified by a label. See also [positional parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrguyda).

- __label font__

  The font used for labels with controls such as sliders and icon bevel buttons. It is 10-point Lucida Grande Regular.

- __Lanczos resampling__

  A commonly used math routine for resampling values in a data set. vImage uses it as a default technique for determining new pixels that did not previously exist in the input image.

- __language__

  The written and spoken methods of combining words to create meaning used by a particular group of people.

- __Last Resort font__

  A collection of glyphs that represent types of Unicode characters. These glyphs can be used as a backup to any other font; if the font cannot represent any particular Unicode character, the appropriate “missing” glyph from the Last Resort font can be used instead.

- __latency__

  In digital audio processing, the time required for an audio sample to proceed from an input to a corresponding output. Total latency, depending on the scope of the system under consideration, can include unavoidable hardware latency (sometimes called _I/O latency_), safety offset latency (required for robust driver operation), and buffer latency (typically software controlled; dependent on digital signal processing requirements).

- __launch__

  To start up an application that was not previously running. Compare [activate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgazdm).

- __launch options__

  A set of flags specifying the manner in which an application is to be opened.

- __launch sequence__

  The sequence of operations performed by an application immediately on being launched, indicated visually to the user by the application’s icon bouncing in the Dock.

- __Launch Services__

  A Mac app programming interface that enables a running program to open other applications, documents, or URLs in a way similar to the Finder or the Dock.

- __Launch Services database__

  The data structure in which Launch Services records information about available applications and the kinds of documents or URLs they are capable of opening.

- __launch specification__

  A data structure of type `LSLaunchFSRefSpec` or `LSLaunchURLSpec` , used to specify to Launch Services the manner in which an item or items are to be opened.

- __layer__

  In QuickTime, a mechanism for prioritizing the tracks in a movie or the overlapping of sprites. When it plays a movie, QuickTime displays the movie’s tracks according to their layer—tracks with lower layer numbers displayed first; tracks with higher layer numbers are displayed over those tracks.

- __layer-backed view__

  An instance of an `NSView` object that uses a Core Animation layer to cache its drawing content. The view is responsible for managing the layer tree; the developer should not manipulate the layer tree directly.

- __layer context__

  An offscreen drawing destination ([CGLayerRef](https://developer.apple.com/documentation/coregraphics/cglayerref)) designed for optimal performance. Introduced in OS X v10.4, a layer context is a much better choice for offscreen drawing than a bitmap graphics context.

- __layer-hosting view__

  An instance of an `NSView` object that hosts a Core Animation layer tree. The developer is responsible for managing the layer tree directly.

- __layout cache__

  A cache that contains all the information ATSUI needs to draw a range of text associated with a text layout object. This includes caret positions, the memory locations of glyphs, and other information needed to lay out the glyphs.

- __Layout pane__

  A pane in the Print dialog that lets the user set the number of pages per sheet and the type of border on a page.

- __LDAP__

  Lightweight Directory Access Protocol. A standard client-server protocol for accessing online directory services.

- __leading edge__

  The edge of a glyph that is encountered first when reading text of that glyph’s language. For glyphs of left-to-right text, the leading edge is the left edge; for glyphs of right-to-left text, the leading edge is the right edge.

- __leading frames__

  In audio data format conversion, frames of audio data that precede, in time, the nominal starting frame for an input [stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe2dg). See also [priming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrguzdi). Compare [trailing frames](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgezda).

- __leaf atom__

  In QuickTime, an atom that contains only data and no other atoms.

- __left-side bearing__

  The white space between the glyph origin and the visible beginning of the glyph.

- __level__

  A description of the nominal audio signal strength resulting from a given input level and gain in an audio device or system. Level within analog audio circuitry is often measured in dBu. The instantaneous signal strength, for any nominal level, can vary from the noise floor to the dynamic ceiling. Professional “line level” typically indicates a nominal level of +4 dBu, while “consumer level” typically indicates a nominal level of –10 dBu. See also [ceiling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3tk), [dBu](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq4tg), [noise floor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmzdc). Compare [volume](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizti).

- __level compression__

  Reduction of the dynamic range of an audio signal, typically by reducing the gain ratio for amplitudes above a specific level. Compare [limiting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge2tg).

- __level indicator__

  A control that displays the level or capacity of something.

- __level of trust__

  The confidence one can have in the validity of a certificate, based on the certificates in its [certificate chain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4dc) and on the [certificate extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4de)s the certificate contains. The level of trust for a certificate is used together with the [trust policy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgeztg) to answer the question “Should I trust this certificate for this action?”

- __LFE__

  Low frequency effect. One of the six typical channels in [5.1 Surround Sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgayde). The LFE channel covers the bottom two or three octaves of audio and is typically used to enhance the realism of sound effects such as explosions.

- __library__

  UNIX feature for monitoring low-level system events.

- __lifebeat__

  Status message sent by WebObjects applications to `wotaskd` to report their activity. The four types of lifebeat messages are: has started, is alive, will stop, and will crash.

- __lifetime__

  In AppleScript, the period of time over which a variable or property is in existence.

- __ligature__

  A glyph that is created when two or more characters are combined to create a new character.

- __ligature decomposition__

  The breaking up of a ligature into its component glyphs during justification so that the individual glyphs may more evenly occupy the space allotted to the ligature.

- __ligature splitting__

  The division of a ligature for hit-testing purposes into regions corresponding to each of its component glyphs.

- __limiter__

  In audio, circuitry or software that limits signal amplitude to a user-defined maximum. Compare [level compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge2dg).

- __limiting__

  In audio, the process of preventing signal amplitude from exceeding a user-defined maximum.

- __line and layout attributes__

  Attributes that specify how the lines of text associated with the text layout object are displayed and formatted. Line attributes control an individual line of text; layout attributes control all of the text associated with a text layout object.

- __linear__

  In audio, describes a transfer function whose output signal is directly proportional to the input.

- __linear gradient__

  See [axial gradient](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3to).

- __linear PCM__

  See [LPCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4dk).

- __line breaking__

  The process of determining the proper location at which to truncate a line of text so that it fits within a given text width.

- __line cap__

  The style that Quartz uses to draw the endpoint of a line—butt, round, or projecting square.

- __line dash pattern__

  In drawing, the repeating series of line segments and spaces used to paint a dashed line.

- __line direction__

  The direction in which text in a particular language is written and read. The English language has a left-to-right line direction; Arabic and Hebrew have a (primarily) right-to-left line direction.

- __line join__

  The style that Quartz uses to draw the junction between connected line segments—miter, round, or bevel.

- __line length__

  The distance, in points, from the origin of the first glyph on a line through the advance width of the last glyph.

- __line width__

  The total width of a line, expressed in user space units.

- __list__

  In AppleScript, an ordered collection of values.

- __list view__

  A control for displaying data in a list. The primary list may by accompanied by additional columns that display secondary attributes about that items in the list. Hierarchies are presented through the use of disclosure triangles.

- __literal__

  In AppleScript, a value that evaluates to itself.

- __load balancing__

  A technique used to distribute user-load among the instances of an application. When multiple instances of an application are running and a new user accesses the application, the WebObjects adaptor uses one of several algorithms to determine which instance to forward the request to.

- __local coordinates__

  The coordinate system for a window, where the origin is set at the upper-left corner of the window’s content region. Compare [global coordinates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhaztk).

- __localization__

  The adaptation of a software product, including its online help and documentation, for use in one or more regions of the world, in addition to the region for which the original product was created. Localization of software can include translation of user interface text, resizing of text-related graphical elements, and replacement or modification of user interface images and sound. See also [internationalization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgazdm).

- __localize__

  See [localization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge3ta).

- __local variable__

  In AppleScript, a variable that is available only in the handler in which it is defined. Variables that are defined within handlers are local unless they are explicitly declared as global variables.

- __lock__

  A data structure used to synchronize access to a shared resource. The most common use for a lock is in multithreaded programs where multiple threads need access to global data. Generally, only one thread can hold the lock at a time; by convention, this thread is the only one that can modify the data during this period. Some lock variants such as read-write locks allow multiple threads to hold a single lock under certain conditions. See also [mutex lock](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi4ti)

- __locked__

  A keychain state in which no key is available in memory to decrypt the passwords and other secrets protected by the keychain. When an application attempts to retrieve a secret from a locked keychain, the user is prompted for a password. The login keychain is unlocked automatically at login if its password matches that of the user’s login account. There is no way to extract secrets from a locked keychain without providing the keychain’’sassword. All of a users keychains lock automatically when the user logs out.

- __locking__

  A mechanism to ensure that data isn’t modified by more than one user at a time and that data isn’t read as it is being modified.

- __login keychain__

  A keychain automatically created for a new login account. The login keychain is automatically unlocked at login if its password matches that of the user’s login account.

- __log statement__

  In AppleScript, a script statement that reports the value of one or more variables to the Event Log pane of a script window, and to the Event Log History window, if it is open.

- __lookup table__

  A data structure used to quickly make computations or retrievals of certain values. In image processing, it is used to store precalculated values of an equation instead of calculating the value each time it is requested. For example, if the equation is _y = 2x_, and you know that there are at most _n_ distinct values, then you can create an array of size _n_ (one for each input) that stores the precalculated value of the equation for the corresponding input (for example,`[0] = 0, [1] = 2, [2] = 4, ... [n] = 2n` ).

- __loop__

  (1) A series of code statements that is repeated. (2) In audio, an excerpt of a recording, often a few seconds long or shorter, intended to be played repeatedly as part of a larger composition.

- __loopback__

  In WebObjects, a mechanism that allows you to open a connection to a computer that does not go over the network.

- __loop variable__

  In AppleScript, a variable whose value controls the number of times the statements in a `repeat` statement are executed.

- __lossless compression__

  Data size reduction without loss of information. Common lossless audio compression formats include FLAC (free lossless audio codec) and [Apple Lossless](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga4tg). Compare [lossy compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4dg).

- __lossy compression__

  Data size reduction that entails loss of information. Common lossy audio compression formats include [MP3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3ti), [AAC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgaydi), and [IMA ADPCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhezti). See also [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2dq). Compare [lossless compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4de).

- __loudness__

  A subjective term to describe perceived sound intensity. When [SPL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrheyte) (sound pressure level) increases by 10, loudness approximately doubles. Compare [gain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhazdo), [volume](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizti).

- __LPCM__

  Linear pulse code modulation. A linear and lossless uncompressed audio data format. _PCM_ is usually assumed to mean _linear PCM_, but sometimes the adjective _linear_ is used to differentiate from nonlinear PCM formats. See also [PCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2de).

- __Mach__

  A central component of the OS X kernel that provides such basic services and abstractions as threads, tasks, ports, interprocess communication (IPC), scheduling, physical and virtual address space management, virtual memory, and timers.

- __Mach-O__

  Mach object file format. The preferred object file format for OS X. See also [PEF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2dk).

- __Mach port dispatch source__

  A [dispatch source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvjvomq) used to process events arriving on a Mach port.

- __Mach server__

  A task that provides services to clients, using a MIG-generated RPC interface. See also [MIG](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgiztq).

- __MacinTalk synthesizer__

  The built-in speech synthesizer available in OS X.

- __macro patch__

  A Quartz Composer patch that contains other patches. A macro is similar to a subroutine in a traditional program. A macro can nest other macros within it. A macro is visually distinguished from a nonmacro patch by its shape—macros have squared-off corners and other patches have rounded corners.

- __magic cookie__

  In digital audio, an opaque data structure for transporting audio format metadata. For audio formats that use them, such as AAC, a magic cookie is produced during encoding, accompanies the data stream that it describes, and is employed during decoding. Magic cookie data is not accessed directly, but rather via a codec-specific interface.

- __main event loop__

  In Carbon, the code loop where the application spends most of its time. The application is blocked while waiting for events. When an event occurs, the application processes it and then returns to the blocked state.

- __main thread__

  A special type of [thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2tq) created when its owning process is created. When the main thread of a program exits, the process ends.

- __main window__

  The window that is the focus of the user’s actions. It may accept keyboard input itself or may work in conjunction with a key window. For example, a text editing document would be a main window when a user is actively typing or modifying text in it.

- __major version__

  A framework version specifier designating a framework that is incompatible with programs linked with a previous version of the framework’s dynamic shared library. Compare [minor version](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi2dm).

- __makefile__

  A specification file used by a build tool to create an executable version of an application. A makefile details the files, dependencies, and rules by which the application is built.

- __managed files__

  The files stored in a source control repository.

- __managed install__

  An Installer-driven installation process. Users open an installer package in the Installer application, which performs all installation tasks.

- __management tool__

  An HTML-based application through which an application-server configuration can be modified. It also allows for the viewing of statistics of resources and services deployed on application servers, starting and stopping services, and adding topics, queues, and data sources.

- __manager__

  In Carbon, a library or set of related libraries that define a programming interface.

- __man-in-the-middle attack__

  An attack on a communication channel in which the attacker can intercept messages going between two parties without the communicating parties’ knowledge. Typically, the man in the middle substitutes messages and even cryptographic keys to impersonate one party to the other.

- __manual install__

  A user-driven installation process. Users drag a product’s files to a location of their choosing in their file system. Compare [window](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2ts).

- __many-to-many relationship__

  In relational databases, a relationship in which each record in the source entity may correspond to more than one record in the destination entity, and each record in the destination may correspond to more than one record in the source. For example, an employee can work on many projects, and a project can be staffed by many employees. In Enterprise Objects, a many-to-many relationship is composed of multiple relationships. See also [relationship](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy2ts).

- __map__

  To translate a range of memory in one address space (physical or virtual) to a range in another address space. The virtual-memory manager accomplishes this by adjusting its VM tables for the kernel and user processes.

- __margins__

  The left, right, top, and bottom sides of the text area.

- __matching__

  See [device matching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2de), [driver matching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyzdi)

- __matching dictionary__

  A dictionary of key-value pairs that describe the properties of a device or other service. The values in a matching dictionary are compared against those in a driver personality during device matching.

- __matrix__

  A collection of numbers arranged in a grid. It can be thought of as the mathematical equivalent of a two-dimensional array. Much like two-dimensional arrays, matrices are composed of rows and columns with their elements referred to as _cells_. See also [transformation matrix](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgezdg).

- __matte__

  A defined region of a movie display that can be clipped and filled with another display.

-  __`mbuf`__

  A data structure containing data about a network packet.

- __media__

  A data structure that contains information that describes the data for a track in a movie. Note that a media does not contain its data; rather, a media contains a reference to its data, which may be stored on disk, CD-ROM disc, or any other mass storage device. Also called a _media structure_.

- __media folder__

  The video directory on a DVD disc volume. See [VIDEO_TS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgiytm).

- __media handler__

  A piece of software that is responsible for mapping from the movie’s time coordinate system to the media’s time coordinate system. The media handler also interprets the media’s data. The data handler for the media is responsible for reading and writing the media’s data. See also [data handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq4di).

- __media ID__

  A unique identifier assigned to a media folder by DVD Playback Services. This identifier can be used as a key when saving information about media playback, such as bookmarks.

- __memory cursor__

  An object that lays out the buffer ranges in a memory descriptor in physical memory, generating a scatter/gather list suitable for a particular device or DMA engine. The object is derived from the `IOMemoryCursor` class. See also [DMA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4tg), [memory descriptor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgiytm).

- __memory descriptor__

  An object that describes how a stream of data, depending on direction, should either be laid into memory or extracted from memory. It represents a segment of memory holding the data involved in an I/O transfer and is specified as one or more physical or virtual address ranges. The object is derived from the `IOMemoryDescriptor` class. See also [DMA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4tg), [memory cursor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgiytk)

- __memory-mapped file__

  A file whose contents are mapped into memory. The virtual-memory system transfers portions of these contents from the file to physical memory in response to page faults. Thus, the disk file serves as backing store for the code or data not immediately needed in physical memory.

- __memory object__

  An object managed by a pager that represents the memory, file, or other storage that backs a VM object. See also [pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqydk).

- __memory protection__

  A system of memory management in which programs are prevented from being able to modify or corrupt the memory partition of another program.

- __menu__

  A user interface element that displays a list of possible selections to the user.

- __menu bar__

  The strip at the top of the user’s primary display that contains menu titles. It includes system and application menus.

- __menu ID__

  A unique ID that identifies a menu.

- __menu item__

  One of the choosable options displayed in a menu.

- __menu item index__

  A one-based index that identifies a particular menu item in the menu. A menu item index of 3 indicates the third item in the menu.

- __message__

  A unit of data sent by one task or thread that is guaranteed to be delivered atomically to another task or thread. In Mach, a message consists of a header and a variable-length body. Some system services are invoked by passing a message from a thread to the Mach port representing the task that provides the desired service.

- __message bubble__

  In Xcode, a small window that displays a project message in place—that is, in the location the message applies to, such as a code line that contains an error.

- __message digest__

  The result of applying a [cryptographic hash function](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq2tc) to a message or other data. A cryptographically secure message digest cannot be transformed back into the original message and cannot (or is very unlikely to) be created from a different input. Message digests are used to ensure that a message has not been corrupted or altered. For example, they are used for this purpose in [digital signature](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2to)s. The digital signature includes a digest of the original message, and the recipient prepares their own digest of the received message. If the two digests are identical, then the recipient can be confident that the message has not been altered or corrupted.

- __metamorphosis__

  The process by which glyphs are rearranged, substituted, deleted, and inserted based upon their properties and contextual states.

- __metapackage__

  An installation package that contains other installation packages, usually component packages. Metapackages are used to deliver multicomponent products to users and to provide them with installation choices that allow them to choose which components to install. See also [component package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm3to).

- __method__

  In object-oriented programming, a procedure that can be executed by an object.

- __microkernel__

  A kernel implementing a minimal set of abstractions. Typically, higher-level OS services such as file systems and device drivers are implemented in layers above a microkernel, possibly in trusted user-mode servers. OS X is a hybrid between microkernel and monolithic kernel architectures. See also [monolithic kernel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi2tq).

- __middle reference form__

  In AppleScript, the reference form that specifies the middle object of a particular class in a container. This form is rarely used.

- __MIDI__

  Musical Instrument Digital Interface. A standard data protocol for communication between computers and electronic music instruments, first adopted in 1983 by the [AES](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga2dq). Core Audio uses MIDI to communicate with [instrument unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgaytg) audio units. MIDI data describes musical events, such as the starting or stopping of a note. Pronounced “MID-ee.”

- __MIDI endpoint__

  An abstract representation of a MIDI cable connection (or port) as used by Core MIDI.

- __MIDI entity__

  In Core MIDI, a logical grouping of MIDI endpoints. For example, a MIDI driver may group a MIDI-in and a MIDI-out endpoint together in a MIDI entity.

- __MIDI port__

  A one-way (send or receive) connection point in a hardware-based or virtual MIDI network. Each port can support up to 16 channels of MIDI data. In Core MIDI, a port is represented abstractly in software by a MIDI endpoint. See also [MIDI](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgiztg).

- __MIDI timecode__

  See [MTC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi4dk).

- __MIG__

  Mach interface generator. A language for generating RPC (remote procedure call) interfaces for interprocess communication between Mach tasks.

- __MIME__

  Multipurpose Internet Mail Extensions. A standard for transmitting formatted text, hypertext, graphics, and audio in email messages over the Internet.

- __MIME type__

  A string designating the type of data in an attachment transmitted via MIME, such as `text/plain`, `image/jpeg`, `audio/mp3`, or `video/quicktime` .

- __MIME type hint__

  Advisory metainformation suggesting the likely content type for a URL. In Search Kit, common MIME type hints include `text/plain`, `text/rtf`, `text/html`, `text/pdf`, and `application/msword`.

- __minimize button__

  A window control (the middle yellow button that appears at the top left) that the user clicks to put a window into the Dock.

- __minimum term frequency__

  In Search Kit, the fewest number of times a term can appear in a document and still be indexed. This functionality is not currently supported by Search Kit indexes.

- __minimum term length__

  In Search Kit, the shortest-length term to index. When Search Kit adds terms from a document to an index, it skips over words whose length is shorter than the minimum term length.

- __mini system font__

  The font used for the text in most mini controls. It is Lucida Grande Regular 9 pt.

- __minor version__

  A framework version specifier designating a framework that is compatible with programs linked with later builds of the framework within the same major version. Compare [major version](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4tk).

- __mipmaps__

  In graphics, a set of texture maps, provided at various resolutions, whose purpose is to minimize artifacts that can occur when a texture is applied to a geometric primitive whose onscreen resolution doesn’t match the source texture map. Mipmapping derives from the latin phrase _multum in parvo_, which means “many things in a small place.”

- __missing character glyph__

  The glyph in a font that is drawn when no glyph is defined for a character code in a font.

- __mLAN__

  Music local area network. A [FireWire](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg43tc)-based interconnection protocol that carries multichannel audio and MIDI over a single cable. See also [MIDI](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgiztg).

- __model__

  An object (of the EOModel class) that defines, in Entity-Relationship terms, the mapping between enterprise object classes and the database schema. This definition is typically stored in a file created with the EOModeler application. A model also includes the information needed to connect to a particular database server.

- __modeless dialog__

  A dialog that does not require the user to dismiss it before interacting with anything else onscreen. The “find and replace” dialog in many word processors is an example of a modeless dialog.

- __model object__

  In object-oriented programming, a type of object that contains the data of an application, provides access to that data, and implements logic to manipulate the data.

- __Model-View-Controller__

  See [MVC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi4tm).

- __modelview matrix__

  A 4 X 4 matrix used by OpenGL to transforms points, lines, polygons, and positions from object coordinates to eye coordinates.

- __modifier key__

  A key the user can hold down to alter the meaning of another key being pressed simultaneously or to alter the meaning of a mouse action. The Option and Command keys are examples of modifier keys.

- __modifier track__

  In QuickTime, a track in a movie that modifies the data or presentation of other tracks. For example, a tween track is a modifier track. See also [tween track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgeztq).

- __Monitor__

  WebObjects application used to administer deployed WebObjects applications. It’s capable of handling multiple applications, application instances, and applications hosts at the same time.

- __monolithic kernel__

  A kernel architecture in which all pieces of the kernel are closely intertwined. A monolithic kernel provides substantial performance improvements. It is difficult to evolve the individual components independently, however. The OS X kernel is a hybrid of the monolithic and microkernel models. See also [microkernel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgiztc).

- __monophonic__

  Describes an instrument that plays only one note at a time. Compare [polyphonic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq4te). See also [monotimbral](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3da), [multitimbral](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi4ta).

- __monotimbral__

  In Core Audio, describes an [instrument unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgaytg) configured to produce sounds of only a single timbre. Both [monophonic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi2ts) and [polyphonic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq4te) instrument units can be monotimbral. Compare [multitimbral](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi4ta).

- __mouse event coalescing__

  A process that merges `mouseMoved` and `mouseDragged` events by checking to see if one of these events exists in the event queue, and if it does, updating the queue with the position and delta information from the more recently generated event.

- __movie__

  A structure of time-based data that is managed by QuickTime. A movie may contain sound, video, animation, or a combination of any of these types of data. A QuickTime movie contains one or more tracks; each track represents a single data stream in the movie. See also [time-based data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3tc), [track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgeydi).

- __movie boundary region__

  In QuickTime, a region that describes the area occupied by a movie in the movie coordinate system, before the movie has been clipped by the movie clipping region. A movie’s boundary region is built up from the track movie boundary regions for each of the movie’s tracks. See also [movie clipping region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3di), [track movie boundary region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgeyti).

- __movie clipping region__

  The clipping region of a movie in the movie’s coordinate system. QuickTime applies the movie’’slipping region to the movie boundary region to obtain a clipped movie boundary region. Only that portion of the movie that lies in the clipped movie boundary region is then transformed into an image in the display coordinate system. See also [movie boundary region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3dg).

- __movie display boundary region__

  A region that describes the display area occupied by a movie in the display coordinate system, before the movie has been clipped by the movie display clipping region. See also [movie display clipping region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3dm).

- __movie display clipping region__

  The clipping region of a movie in the display coordinate system. Only that portion of the movie that lies in the clipping region is visible to the user. QuickTime applies the movie’s display clipping region to the movie display boundary region to obtain the visible image. See also [movie display boundary region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3dk).

- __movie file__

  A QuickTime file that stores a movie and its associated data.

- __movie header atom__

  A QT atom that specifies the characteristics of an entire QuickTime movie.

- __movie poster__

  A single visual image representing a QuickTime movie. You specify a poster as a point in time in the movie and specify the tracks that are to be used to constitute the poster image.

- __movie preview__

  A short dynamic representation of a QuickTime movie. Movie previews typically last no more than 3 to 5 seconds, and they should give the user some idea of what the movie contains. You define a movie preview by specifying its start time, its duration, and its tracks.

- __movie resource__

  One of several data structures that provide the medium of exchange for movie data between applications on a Macintosh computer and between computers, even computers of different types.

- __movie sprite__

  A sprite that lives in a sprite track and acts in a movie. See also [sprite track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhezdc).

- __Movie Toolbox Access Keys__

  A QuickTime API that can be used to add password protection to QuickTime data.

- __MP3__

  Common short form for _MPEG-1, audio layer 3_. A lossy, perceptual compression format for audio data that can achieve 10:1 data compression with usable sound quality. MPEG-1 does not define a standard encoding algorithm for MP3; it specifies only the decoding algorithm, the bit stream (packet) format, and the file format. See also [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2dq).

- __MP4__

  The [MPEG-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi4de) audio/video container format, also known as MPEG-4 Part 14. MP4 files can hold many different types of data, such as AAC and MP3 audio, or MPEG-2 and H.264 video. Typically, files with the`.mp4` extension contain both audio and video data, while`.m4a` denotes files containing only audio data.

- __MPEG__

  Moving Picture Experts Group. An international working group of ISO/IEC that develops standards for digitally coded representations of audio and video. MPEG is part of the names of many [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2dq) formats published by the group. Pronounced “EM-peg.” See also [IEC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhezdm), [ISO](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga2di).

- __MPEG-1__

  A set of audio and video [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2dq) formats, formally designated as ISO/IEC-11172. MPEG-1 encompasses the Video CD and [MP3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3ti) formats.

- __MPEG-1, audio layer 3__

  See [MP3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3ti).

- __MPEG-2__

  A set of audio and video [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2dq) formats, formally designated as ISO/IEC-13818, first published in 1994. MPEG-2 encompasses formats of generally higher quality than MPEG-1, including broadcast-quality video and (with modifications) DVD movies.

- __MPEG-2 AAC__

  See [AAC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgaydi).

- __MPEG-4__

  A set of audio and video [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2dq) formats, formally designated as ISO/IEC-14496, first published in 1998. MPEG-4 encompasses many of the features introduced in MPEG-1 and MPEG-2 and adds features useful for streaming media and broadcast, among others. See also [stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe2dg)

- __MPEG-4 AAC__

  See [AAC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgaydi).

- __MPEG-4 Part 14__

  See [MP4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3tm).

- __MTC__

  MIDI timecode. A music synchronization protocol, defined as part of the [MIDI](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgiztg) protocol. MTC emulates [SMPTE timecode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha3to). See also [timecode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3te).

- __multicast__

  A process in which a single packet can be addressed to multiple recipients. Multicast is used, for example, in streaming video, in which many megabytes of data are sent over the network.

- __multihoming__

  The ability to have multiple network addresses in one computer, usually on different networks. For example, multihoming might be used to create a system in which one address is used to talk to hosts outside a firewall and the other to talk to hosts inside; the computer provides facilities for passing information between the two.

- __multiplexing__

  See [interleaving](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgazdi).

- __multitasking__

  The concurrent execution of multiple programs. OS X uses preemptive multitasking.

- __multitimbral__

  In Core Audio, describes an [instrument unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgaytg) configured to allow production of more than one timbre simultaneously. Compare [monotimbral](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3da).

- __music__

  One of the QuickTime media types, in which sequences of sounds and tones are generated.

- __music player__

  The Core Audio programming construct that applications use to play MIDI or other event data.

- __mutex lock__

  A mutual-exclusion locking object that allows multiple threads to synchronize access to shared resources. A mutex has two states: locked and unlocked. Once a mutex has been locked by a thread, other threads attempting to lock it block. When the locking thread unlocks (releases) the mutex, one of the blocked threads (if any) acquires (locks) it and uses the resource. The thread that locks the mutex must be the one that unlocks it. The work-loop lock (which is used by a command gate) is based on a mutex. See also [lock](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge3tg), [work loop](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi3te)

- __mutually exclusive attribute group__

  A set of attribute choices in which the user can select only one item, such as font size. Compare [accumulating attribute group](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgayts).

- __MVC__

  Model-View-Controller. A design pattern that assigns objects in an application to one of three roles and recommends a distinct separation among model, view, and controller objects. This is one of the central design patterns for Cocoa applications.

- __name__

  In Search Kit, a document name as represented in a document URL object. For documents that are on-disk files, the name should correspond to the actual filename. For other types of documents, your application can assign any name to a document. See also [document URL object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyydk)

- __named region__

  In Mach, a form of named memory entry that provides a form of memory sharing.

- __name port__

  In Mach, a port that allows access to nonprivileged operations against an object (for example, obtaining information about the object). In effect, it provides a name for the object without providing any significant access to the object. See also [port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq4tk), [control port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgqzdc).

- __name reference form__

  In AppleScript, a reference form that specifies an object by name—that is, by the value of its `name` property.

- __named memory entry__

  A handle (a port) to a mappable object backed by a memory manager. The object can be a region or a memory object.

- __namespace__

  An agreed-upon context in which names (identifiers) can be defined. Within a given namespace, all names must be unique.

- __NAT__

  Network address translation. A scheme that transforms network packets at a gateway so network addresses that are valid on one side of the gateway are translated into addresses that are valid on the other side.

- __National Television System Committee__

  See [serif](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhazdo).

- __native curve type__

  The curve type—cubic or quadratic—used by a font designer to specify a font.

- __navigation bar__

  In Xcode, the bar along the top of the text editor that contains a number of controls that you can use to move between open files, jump to symbols, and open related files.

- __negative justification__

  A layout in which the glyphs on a line do not naturally fit within the line width set by the developer.

- __nested control statement__

  In AppleScript, a control statement that is contained within another control statement.

- __NetInfo__

  The network administrative information database and information retrieval system for OS X. Many OS X services consult the NetInfo database for their configuration information.

- __network__

  A group of hosts that can communicate with each other.

- __network kernel extension__

  See [NKE](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmytk).

- __NFS__

  Network File System. The main file-sharing protocol used by UNIX systems. An NFS file server allows users on the network to share files on other hosts as if they were on their own local disks.

- __nib document__

  The runtime representation of a nib file. Nib documents are the primary document type of the Interface Builder application. The on-disk representation of a nib document is a nib file.

- __nib file__

  A special file created by Interface Builder that contains information required to create user interface objects (windows, controls, and menus). Nib files contain binary data representing resources that you load into your application at runtime. See also [xib file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi4di).

- __NKE__

  Network kernel extension. A type of KEXT that provides a way to extend and modify the networking infrastructure of OS X dynamically without recompiling or relinking the kernel.

- __NMI__

  Nonmaskable interrupt. An interrupt produced by a particular keyboard sequence or button that cannot be blocked in software. It can be used to interrupt a hung system—for example to drop into a debugger.

- __nobody__

  A special user with very little access. To prevent someone running as `root` or as an administrator on one system from gaining control over another system through a network connection, such users are often mapped to the `nobody` user on the remote system.

- __node__

  (1) An [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) in an [audio processing graph](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tg). Each node has one or more inputs and outputs that must be connected to other audio units. See also [head node](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqha3tg). (2) A panorama or an object in a QuickTime VR movie.

- __nodes file__

  In Xcode, a file that describes the hierarchical structure of the documentation set. It defines the table of contents that users see in the browser view of the Xcode Documentation window and the relationships between entries in the documentation set hierarchy.

- __noise__

  Undesired energy or data components in a communication channel included with the signal that the channel is carrying. See also [noise floor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmzdc), [quantization noise](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyydm). Compare [distortion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4dm).

- __noise floor__

  The amplitude of the [noise](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmzda) in a communication channel when no signal is present, typically measured as a scalar, absolute level in decibels relative to a standard level such as using [dBu](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq4tg). Noise can vary according to frequency, and perceived noise is subject to psychoacoustics, so the derivation of a single number to describe noise floor can entail weighting. Common weighting schemes are dBA, dBC, and unweighted.

- __noncontextual features__

  Features that are applied in the same manner to a glyph regardless of the adjacent glyphs. Compare [contextual features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgqyta).

- __nonexclusive feature type__

  A feature for which you can enable any number of feature selectors at once. Compare [exclusive feature type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4yti).

- __non-premultiplied__

  In image processing, a technique for processing the alpha channel of a pixel. Instead of performing the alpha blend for each pixel, the alpha value is premultiplied to each of the other color channel values for that pixel. The pixel can then be interpreted as is from then on because all of the color channel values have been appropriately changed to reflect the alpha component.

- __nonretained window__

  A window without an offscreen buffer for screen pixel values.

- __nonsimple message__

  In Mach, a message that contains either a reference to a port or a pointer to data. Compare [simple message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2tk).

- __nonzero winding number rule__

  A fill rule that determines when to paint a pixel. The outcome depends on the direction that path segments are drawn. Compare with [even-odd rule](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy4tq).

- __notification__

  A programmatic mechanism for alerting interested recipients (observers) that some event has occurred during program execution. The observers can be users, other processes, or even the same process that originates the notification. In OS X, the term is used to identify specific mechanisms that are variations of the basic meaning. In the kernel environment, _notification_ is sometimes used to identify a message sent via IPC from kernel space to user space. Distributed notifications provide a way for a process to broadcast an alert (along with additional data) to any other process that makes itself an observer of that notification. Finally, the Notification Manager (a Carbon manager) lets background programs notify users—through blinking icons in the menu bar, by sounds, or by dialogs—that their intercession is required. In Enterprise Objects, it’s a mechanism that provides an asynchronous communication infrastructure between objects.

- __notify port__

  A special Mach port that is part of a task. A task’s notify port receives messages from the kernel advising the task of changes in port access rights and of the status of messages it has sent.

- __NSXMLOutputFormat__

  WebObjects class that encapsulates format properties for an NSXMLOutputStream object.

- __NSXMLOutputStream__

  WebObjects class that serializes objects and data into XML documents.

- __NTSC__

  National Television System Committee. A color-encoding standard adopted by the committee in 1953. It was the first monochrome-compatible, simultaneous color transmission system used for public broadcasting. This method is used widely in the United States.

- __nub__

  An I/O Kit object that represents a detected, controllable entity such as a device or logical service. A nub may represent a bus, disk, graphics adaptor, or any number of similar entities. A nub supports dynamic configuration by providing a bridge between two drivers (and, by extension, between two families). A nub can also provide services to code running in user space through a device interface. See also [device](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqguztk), [driver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyzde)

- __number__

  In AppleScript, a synonym for the classes `integer` and `real` .

- __NURBS__

  Non-uniform rational B-spline. A methodology use to specify parametric curves and surfaces.

- __NVRAM__

  Nonvolatile RAM. RAM storage that retains its state even when the power is off. See also [RAM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyzde).

- __Nyquist frequency__

  The highest frequency signal that can be faithfully recorded for a given sampling rate. Attempts to sample a signal containing higher frequencies results in the generation of an alias signal below the Nyquist frequency. The Nyquist frequency is half the sampling rate. See also [visual context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizdq).

- __object__

  (1) In object-oriented programming, a programming unit that groups together a data structure (fields) and the operations (methods) that can use or affect that data. Objects are the principal building blocks of object-oriented programs. (2) In Mach, a collection of data, with permissions and ownership. (3) In AppleScript, an instantiation of a class definition, which can include properties and actions. (4) A group of bright, high-intensity pixels in an image, as opposed to the darker pixels, which are considered part of the background.

- __object containment hierarchy__

  In AppleScript, the hierarchy of objects in a running application. AppleScript and Cocoa scripting depend on the object containment hierarchy to locate the objects on which to perform an operation. See also [AppleScript object model](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgeydg).

- __object conversion__

  See [coercion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm2ti).

- __object file__

  A file containing executable code and data. Object files in the Mach-O executable format take the suffix`.o`and are the product of compilation using the GNU compiler ( `gcc` ). Multiple object files are typically linked together along with required frameworks to create a program. See also [code fragment](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm2ta), [dynamic linking](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy2dq).

- __object-first command__

  In AppleScript, a command that invokes a specified method of each specified receiver. With an object-first command, objects perform the specified action on themselves. Compare [verb-first command](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgiydo).

- __object graph__

  In WebObjects, the graph of objects (especially enterprise object instances) that are contained by `EOEditingContext` objects.

- __Objective-C__

  An object-oriented programming language based on standard C and a runtime system that implements the dynamic functions of the language. The few Objective-C extensions to the C language are mostly based on Smalltalk, one of the first object-oriented programming languages. Objective-C is available in the Cocoa application environment.

- __object-relational mapping__

  In WebObjects, a system for transforming Entity-Relationship models to an object-oriented programming framework. Enterprise Objects performs object-relational mapping (mapping database structures to Java objects) with the help of Entity-Relationship models called EOModels. See also [Entity-Relationship modeling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy4dm).

- __object specifier__

  In AppleScript, a phrase that specifies the information needed to find another object in terms of the objects in which it is contained. Cocoa scripting makes use of object specifiers to find objects in your application while executing a script command and to return information requested by a script. See also [absolute object specifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgaydm), [object containment hierarchy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm2dc), [relative object specifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy3dc), [reference form](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy2te).

- __object track__

  A track in a QuickTime VR movie that contains a set of views of a VR object.

- __object wrapper__

  Code that defines an object-based interface for a set of procedural interfaces. Some Cocoa objects wrap Carbon interfaces to provide parallel functionality between Cocoa and Carbon applications.

- __offset-binary encoding__

  A method of digitally encoding sound that represents the range of amplitude values as an unsigned number, with the midpoint of the range representing silence. For example, an 8-bit sound sample stored in offset-binary format would contain sample values ranging from 0 to 255, with a value of 128 specifying silence (no amplitude). Samples in Macintosh sound resources are stored in offset-binary form. Compare [twos-complement encoding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgezts).

- __offsets__

  Monotonically increasing or decreasing values. In ATSUI, offsets are in `Unichars` units and are typically used to specify starting and ending points for a string of text.

- __Ogg__

  A free collection of digital codecs for multimedia, including [Ogg Vorbis](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm2tk) for lossy compression of audio at medium-to-high bit rates, and [Ogg FLAC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm2ti) for lossless audio.

- __Ogg FLAC__

  A free, open source, lossless audio codec. Ogg FLAC typically compresses CD audio by 50% with no data loss. FLAC is an acronym for _Free Lossless Audio Codec_. See also [lossless compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4de).

- __Ogg Vorbis__

  A free, open source, lossy audio codec intended to compete with [MP3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3ti).

- __OHCI__

  Open Host Controller Interface. The register-level standards that are used by most USB and FireWire controller chips.

- __one-shot timer__

  A Carbon event timer that fires only once. _See also_ [event timer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4ydq).

- __one-time pad authentication__

  A form of [shared secret authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2di) in which both parties have an identical list of pairs of numbers, words, or symbols and each pair is used only once.

- __op code__

  In the old Printing Manager, a value passed to a function that determines how the function should operate. These are not used in the Carbon Printing Manager. Accessor functions are used instead.

- __opaque type__

  In Core Foundation and Carbon, an aggregate data type plus a suite of functions that operate on instances of that type. The individual fields of an initialized opaque type are hidden from clients, but the type’s functions offer access to most values of these fields. An opaque type is roughly equivalent to a class in object-oriented programming.

- __open__

  To [launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgezdk) or [activate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgazdm) an application or to present a document or URL for viewing or editing within an application.

- __OpenCL__

  Open Computing Language. A standards-based technology for performing general-purpose computations on a computer’s graphics processor.

- __OpenGL__

  Open Graphics Language. An industry-wide standard for developing portable 2D and 3D graphics applications. OpenGL consists of an API and libraries that developers use to render content in their applications.

- __OpenGL buffer__

  A buffer that holds image information in graphics card memory. In Core Video, you manipulate OpenGL buffers using the `CVOpenGLBufferRef` type, which is a wrapper around the standard OpenGL buffer type.

- __OpenGL texture__

  An immutable image that OpenGL uses to wrap onto primitives. In Core Video, you manipulate OpenGL textures using the `CVOpenGLTextureRef` type, which is a wrapper around the standard OpenGL texture type.

- __Open Scripting Architecture__

  See [OSA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm3ts).

- __open source__

  Software that includes freely available access to source code, redistribution, modification, and derived works. The full definition is available at[http://www.opensource.org](http://www.opensource.org/).

- __Open Transport__

  A legacy communications architecture for implementing network protocols and other communication features on computers running the Mac OS. Open Transport provides a set of programming interfaces that supports, among other things, both the AppleTalk and TCP/IP protocols.

- __operand__

  An expression from which an operator derives a value.

- __operation__

  (1) In AppleScript, the evaluation of an expression that contains an operator. (2) In WebObjects, a specific process or task that a web service implements. Much like Java methods, a web service operation can define an arbitrary number of parameters and return values. Operations are invoked by web service consumers and executed by web service providers.

- __operation object__

  An instance of the [NSOperation](https://developer.apple.com/documentation/foundation/nsoperation) class. Operation objects wrap the code and data associated with a task into an executable unit.

- __operation queue__

  An instance of the [NSOperationQueue](https://developer.apple.com/documentation/foundation/operationqueue) class. Operation queues manage the execution of operation objects.

- __operator__

  A symbol, word, or phrase that derives a value from another value or pair of values. In Search Kit, operators include `AND` , `OR` , `NOT` , parentheses, quotation marks, and several others. Search Kit interprets operators and determines the user’s intended search type according to the operators’ meanings.

- __optical alignment__

  The fine adjustment of glyph positions at the ends of lines to give a more even visual appearance to margins.

- __optional parameter__

  In AppleScript, a parameter that need not be included for a command to be successful.

- __order__

  The maximum number of factors in an equation. For example, the equation _x_ 2 _+ x + 1_ has an order of 3 because there are three distinct factors in the equation ( _x_ 2, _x_, and _x_ 0).

- __ordered tasks__

  In Xcode, tasks that contain inputs that are the outputs of other tasks or outputs that are the inputs of other tasks. Compare [unordered tasks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge3do).

- __Organizer action__

  A predefined or custom task that Xcode performs on a directory.

- __Organizer item__

  In Xcode, a representation of a directory in the file system; these items are like symbolic links or folder references.

- __OSA__

  Open Scripting Architecture. A standard and extensible mechanism for interapplication communication in OS X. Implemented by a number of OS X frameworks and subframeworks, including the AE framework (which implements the Apple Event Manager) and the OpenScripting framework. Also includes the AppleScript component, which implements the AppleScript language.

- __osacompile__

  A shell tool for compiling script files.

- __outlet__

  A pointer to another object that can be set in Interface Builder. Applications use outlets to store references to objects in nib files.

- __out-of-band__

  Communication on a socket or interface that relates to the operation of the socket or interface rather than data destined for the endpoint (for example, `ioctl` and `getsockopt` calls). Compare [in-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe2ts).

- __out-of-line data__

  Data that is passed by reference in a Mach message, rather than being included in the message. Compare [in-line data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe4dm).

- __output audio queue__

  See [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2ti).

- __Output Options pane__

  A pane in the Print dialog that provides an option to save a print job as a file.

- __output unit__

  An [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) of type `'auou'`. Output units can start and stop the flow of audio data in the signal chain. Examples include the [default output unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqguyta) and the [AUHAL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3dc). See also [head node](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqha3tg).

- __outside property__

  A property in a `script` object that occurs outside of any handlers or nested `script` objects. Similarly, an outside variable or an outside statement occurs outside of handlers or nested `script` objects.

- __owner__

  See [UID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2ds).

- __pacing__

  The distribution of the interpolated values of an animation across the duration of the animation.

- __package__

  (1) In OS X, a [directory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu3ta) presented to the user so that it appears to be a single file, and whose contents are ordinarily inaccessible for browsing by the user. Compare [folder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg44ta). See also [application packaging](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgezde). (2) In Java, a way of storing, organizing, and categorizing related Java class files; typical package names are `java.util` and `com.apple.cocoa.foundation`.

- __package identifier__

  Identifies the package within the Installer package database. See also [Installer package database](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgaydo).

- __package list__

  A pane in a PackageMaker project window that lists the packages the project defines. This list is divided in two parts: the installation-package file (which contains all the product’s files) and the subpackages or package references that contain components of the product.

- __PackageMaker__

  A tool that builds an installable software package from the files you provide.

- __package properties__

  Installer package data that provides Installer details about the package itself, such as its identifier, version number, and resource fork processing.

- __package requirement__

  A test that determines whether a package can be installed on the computer. A package requirement can be optional; such requirements display a warning to the user but allows the installation to proceed. Non-optional requirements prevent an installation from taking place.

- __package version number__

  A positive integer that identifies an iteration of a single-component product package, or an iteration of a component package within a product package. This version number should be incremented when the contents or installation details of the package are changed. See also [product package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu2to), [component package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm3to).

- __packet__

  (1) In networking, an individual piece of information sent on a network. (2) In Core Audio, an encoding-defined unit of audio data comprising one or more frames. For PCM audio, each packet corresponds to one frame. For compressed audio, each packet corresponds to an encoding-defined number of uncompressed frames. For example, one packet of MPEG-2 AAC data decompresses to 1,024 frames of PCM data. Compare [webpage template](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2tc), [uniquing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2ts).

- __packet description__

  In a variable-packet-size audio file or stream, metadata that specifies where a packet of audio data starts as well as its size. In Core Audio, a data structure used to represent a packet description in an audio data buffer. See also [simple message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2tk), [packet table](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm4ts).

- __packet table__

  In a variable-packet-size audio file or stream, metadata consisting of a table of packet descriptions. See also [simple message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2tk), [packet description](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm4tq).

- __packing__

  Converting pixel color components from a buffer into the format needed by an application.

- __page__

  (1) (n.) The smallest unit (in bytes) of information that the virtual memory system can transfer between physical memory and backing store. (2) (v.) To transfer pages between physical memory and backing store. (3) (n.) In Quartz, the virtual canvas that Quartz paints to.

- __Page Attributes pane__

  A pane in the Page Setup dialog that allows the user to set page format options—paper size, paper orientation, and scaling.

- __page format object__

  An opaque data type used by the printing system to store information from the Page Setup dialog, such as paper size and orientation.

- __page formatting__

  A description of how the pages of a document should be printed; page formatting includes such information as page and paper sizes.

- __pager__

  A module responsible for providing the data for the pages of a memory object. See also [default pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqguytc), [vnode pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgiztc).

- __page rectangle__

  The rectangle marking the boundaries of the printable area on a page. The upper-left corner of the page rectangle always has the coordinates (0,0). The coordinates of the lower-right corner define the rectangle for the maximum imageable area attainable on the given printer; these coordinates are specified by the units used to express the resolution of the printing graphics port.

- __Page Setup dialog__

  A dialog—usually displayed by an application in response to the user choosing the Page Setup command—that allows the user to specify the printing options (such as the paper size and the printing orientation) used by an application to format a document.

- __pages view__

  In Xcode, one of the three views provided by the all-in-one layout.

- __painter’s model__

  In Quartz, a drawing model in which each successive drawing operation applies a layer of paint to a page.

- __painting__

  For the Quartz equivalent of the QuickDraw painting operation (such as that used for the QuickDraw function `PaintOval`), see [filling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg43dg).

- __PAL__

  Phase Alternation Line. A color-encoding system used widely in Europe, in which one of the subcarrier phases derived from the color burst is inverted in phase from one line to the next. This technique minimizes hue errors that may result during color video transmission. Sometimes called _Phase Alternating Line_.

- __palette__

  A window that is independent of document windows and that provides items to be used when other windows are open, such as a palette that provides drawing tools.

- __Palette window__

  An Interface Builder window that provides a number of palettes (or panes), each of which contains object instances you can add to an application.

- __pane__

  An area of changeable content in a dialog or other window. Panes usually change as the result of the user clicking a button or choosing an item from a pop-up menu. In some cases, panes change as a process takes place, such as while the Installer application is running.

- __panel__

  A window that floats above other windows and provides tools or controls that users can work with while documents are open. _Panel_ is not a user term; the equivalent term is _window_ or _dialog_, as appropriate. See also [document window](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyydm).

- __panic__

  An unrecoverable system failure explicitly triggered by the kernel with a call to `panic`. Compare [kernel crash](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4dg).

- __panner unit__

  In Core Audio, an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) of type `'aupn'` that distributes a set of input channels, using a [spatialization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4tq) algorithm, to a set of output channels. In the simplest case, a panner unit places a monaural signal at a left/right spot in a stereo field.

- __panning__

  From _panorama_. In audio, the placement of a monaural signal within a stereo or multichannel (such as [surround sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe3tm)) sound field. Variations include stereo, [SoundField](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4tc), spherical head, vector, and [HRTF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqheydc) panning. A more general term for panning is [spatialization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4tq).

- __panorama__

  A structure of QuickTime VR data that forms a virtual-world environment within which the user can navigate.

- __panorama track__

  A track in a QuickTime VR movie that contains a panorama.

- __Paper Feed pane__

  A pane in the Print dialog that lets the user specify the printer trays from which a print job should be printed.

- __paper rectangle__

  The rectangle that describes the size of a piece of paper on which a page is printed. This rectangle is defined in the same coordinate system as the [page rectangle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqydm). Thus, the upper-left coordinates of the paper rectangle are typically negative and its lower-right coordinates are greater than those of the page rectangle.

- __parameter__

  In an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq), a variable that defines an adjustable attribute such as volume, pitch, or filter cutoff frequency. Each audio unit parameter has a name, a unit (such as Hertz or decibels), a default value and a value range, and an optional set of flags. In an [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2ti), a parameter has only a value. Compare [element](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy3dm), [property](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu3tg), [scope](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg43tg).

- __parameter variable__

  In AppleScript, an identifier in a handler definition that represents the actual value of a parameter when the handler is called. Also called a _formal parameter_.

- __parent atom__

  A QT atom that contains other QT atoms, which are its child atoms. See also [child atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmyte).

- __parent document URL object__

  In Search Kit, for file-based documents, the location of the enclosing folder for a document or for another parent document URL object. Search Kit manages documents using parent-child relationships, not paths. You can construct the path of any document by following its parent document links. See also [document URL object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyydk).

- __parent object__

  In AppleScript, an object from which another `script` object, called the child, inherits properties and handlers. A parent object may be any object, such as a `list` or an `application` object, but it is typically another `script` object.

- __parser__

  In computer science generally, a program that works with a tokenizer to interpret a sequence of tokens. In Audio File Stream Services, a software object of type `AudioFileStreamID`, used for reading audio file streams.

- __partial string searching__

  Matching of the terms in a query string to indexed terms, with implied wildcard characters at the start and end of each query term. Each term is matched separately. Search Kit does not currently support partial string searching as an option, but a client application can provide it by adding wildcard operators (asterisks) around each term before handing a query off to Search Kit. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayde).

- __passive driver__

  A device driver that performs only basic power-management tasks, such as joining the power plane and changing the device’s power state. See also [active driver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgazds).

- __pass-through mode__

  A mode that does not modify data. With respect to keyboard-entry, pass-through mode allows users to enter ASCII characters in the context of a 2-byte script, without changing the keyboard script.

- __password__

  Data, usually a character string, used to authenticate a user for a service or application.

- __pasteboard__

  A standardized mechanism for exchanging data within applications or between applications. The most familiar use for pasteboards is handling copy and paste operations. The equivalent user term is _Clipboard_.

- __patch__

  In Quartz Composer, the base processing unit in a composition, which executes and produces a result. Patches are similar to routines in traditional programming languages. See also [macro patch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4ta).

- __patch hierarchy__

  In Quartz Composer, the levels in a composition created when macro patches are used. See also [macro patch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4ta).

- __path__

  (1) In Quartz, one or more shapes that Quartz paints as a unit. A path can consist of straight lines, curves, or both. It can be open or closed. (2) For documentation sets, the page to display when the user selects the documentation node or the folder containing that page. This path is interpreted relative to the base URL of the documentation node.

- __pathname separator__

  The “/” character that separates folder names in a raw pathname. A raw pathname should be displayed only to expert users or in a help tag.

- __pattern__

  A sequence of drawing operations that Quartz can repeatedly paint to a graphics context.

- __pattern space__

  In Quartz, an abstract space that maps to the default user space by the transformation matrix (the pattern matrix) you specify when you create the pattern. Pattern space is separate from user space. The untransformed pattern space maps to the base (untransformed) user space, regardless of the state of the current transformation matrix.

- __payload__

  The product or product components contained in an installation package. See also [installation package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe4to).

- __pbuffer__

  See [simple search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2tm).

- __PCM__

  Pulse code modulation. A lossless encoding technique widely used for working with audio, invented by Alec H. Reeves in 1937. Sometimes called _LPCM_ for _linear pulse-code modulation_, which distinguishes the process from [ADPCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga2di). In pulse-code modulation, an analog signal is linearly encoded to a series of binary numbers by sampling an analog signal at regular intervals. See also [encoding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy3tq), [linear](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge2tk), [quantization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyydi).

- __PDF__

  Portable document format. A file format created by Adobe Systems to represent documents in a manner independent of the software, hardware, and operating system. The format became an open standard in 2008.

- __peek__

  To examine an event in an event queue (obtaining its class, kind, parameters and so on) without removing it from the queue. Compare [pull](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4tm).

- __PEF__

  Preferred Executable Format. The format of executable files used for applications and shared libraries in Mac OS 9; supported in OS X. The preferred format for OS X is [Mach-O](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4do).

- __pen__

  See [stylus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe2to).

- __pen event__

  In the Ink Services technology, a mouse event that contains tablet data.

- __perceptual coding__

  Lossy compression that takes advantage of limitations in human perception. In perceptual coding, audio data is selectively removed based on how unlikely it is that a listener will notice the removal. MP3 and MPEG-2 AAC are popular examples of perceptual coding. See also [lossy compression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4dg).

- __per-file compiler flags__

  A flag that you can use to customize the build process of source files of a particular type.

- __permissions__

  In BSD, a set of attributes governing who can read, write, and execute resources in the file system. The output of the `ls -l` command represents permissions as a nine-position code segmented into three binary three-character subcodes; the first subcode gives the permissions for the owner of the file, the second for the group that the file belongs to, and the last for everyone else. The left-most position is reserved for a special character that says if this is a regular file (-), a directory (d), a symbolic link (l), or a special pseudo file device. The execute bit has a different semantic for directories, meaning they are searchable. See also [ACL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgazdc), [authorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3di), [UID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2ds).

- __personality__

  A set of properties specifying the kinds of devices a driver can support. This information is stored in an XML matching dictionary defined in the information property list (`Info.plist`) file in the driver’s KEXT bundle. A single driver may present one or more personalities for matching; each personality specifies a class to instantiate. Such instances are passed a reference to the personality dictionary at initialization.

- __Pet Store__

  A sample J2EE application from Sun Microsystems, which showcases the power and flexibility of the J2EE platform.

- __Phase Alternation Line__

  See [unidirectional text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2tm).

- __phoneme__

  A distinct unit that serves to distinguish between meanings of words.

- __phoneme modifier__

  A symbol defined to adjust the pronunciation of an individual phoneme. Phoneme modifiers are also called _prosodic control symbols_.

- __phrase searching__

  Matching of a query string to indexed terms, with the query string considered as a complete phrase. A match occurs when the exact query phrase appears in a document. Search Kit supports phrase searching in inverted and inverted-vector indexes. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayde).

- __phrase termination__

  Defines when Ink input should be processed by the recognizer.

- __physical address__

  An address to which a hardware device, such as a memory chip, can directly respond. Programs, including the Mach kernel, use virtual addresses that are translated to physical addresses by mapping hardware controlled by the Mach kernel.

- __physical memory__

  Electronic circuitry contained in random-access memory (RAM) chips, used to temporarily hold information at execution time. Addresses in a process’s virtual memory are mapped to addresses in physical memory. See also [virtual memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizdi)

- __picture comment__

  A command or data used for special processing by output devices, such as printer drivers. Picture comments are usually stored in the definition of a picture or are included in the drawing an application does when printing.

- __picture taker panel__

  The Image Kit picture taker class (`IKPictureTaker` ) that allows users to choose images by browsing the file system or by taking a snapshot with an iSight or other digital camera. The user term is _picture taker_.

- __PID__

  Process identifier. A number that uniquely identifies a process. Also called a _process ID_.

- __PIO__

  Programmed input/output. A way to move data between a device and system memory in which each byte is transferred under control of the host processor. See also [DMA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4tg).

- __pitch__

  In [psychoacoustics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4ta), a perceptual sound attribute that is roughly correlated with frequency. In general, pitch increases as the perceptually-dominant sound frequency increases. The strength of a pitch sensation depends on the sound character; noise-like sounds cause a weak pitch sensation, while pure tones evoke a strong pitch sensation.

- __pitch modulation__

  The maximum amount by which the actual frequency of speech may deviate from the speech pitch.

- __pixel__

  A picture element; the smallest element that the graphics hardware can display on the screen. In OpenGL, pixel is made up of all the bits at the location _x_, _y_, in all the bitplanes in the framebuffer.

- __pixel buffer__

  In general, a buffer that holds image information in main memory. In OpenGL, a type of drawable object that allows the use of offscreen buffers as sources for texturing. Pixel buffers allow hardware-accelerated rendering to a texture.

- __pixel depth__

  The number of bits per pixel in a pixel image.

- __pixel format__

  A format used to store pixel data in memory. The format describes the pixel components (that is, red, blue, green, alpha), the number and order of components, and other relevant information, such as whether a pixel contains stencil and depth values.

- __pixel manipulation__

  The process of operating on bits. Quartz does not provide functions that operate on a pixel-by-pixel basis. Core Image provides support for image processing on a per-pixel basis.

-  __`.pkg` file__

  An OS X Installer file. `.pkg` files can be combined into a metapackage (`.mpkg`).

- __PKI__

  Public key infrastructure. As defined by the [X.509](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi4da) standard, the set of hardware, software, people, policies, and procedures needed to create, manage, store, distribute, and revoke digital certificates that are based on [public key cryptography](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4ti). PKI provides key management, data integrity, and data confidentiality.

- __PKINIT__

  A protocol that defines the use of public key cryptography for initial authentication in [Kerberos](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga3ts).

- __placard__

  A control that displays information. Typically placards are used in document windows as a way to quickly modify the view of the contents—for example, to change the current page or the magnification.

- __plaintext__

  Ordinary, unencrypted data. Compare [ciphertext](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmzda).

- __planar image format__

  A format that encodes a color channel for images. Planar images tend to be faster to operate on than nonplanar images because operations do not need to be repeated for each color channel. A grayscale image is an example of a planar image because it encodes only one (black and white) channel.

- __plane__

  A subset of driver (or service) objects in the I/O Registry that have a certain type of provider/client relationship connecting them. The most general plane is the Service plane, which displays the objects in the same hierarchy in which they are attached during Registry construction. There are also the Audio, Power, Device Tree, FireWire, and USB planes.

- __Platform Expert__

  A driver object for a particular motherboard that knows the type of platform the system is running on. The Platform Expert serves as the root of the I/O Registry tree.

- __play state__

  One of four states that a DVD can be in during playback: playing at a normal rate, paused, scanning forward, or scanning backward.

- __playback audio queue__

  See [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2ti).

- __playback quality__

  A relative measure of the fidelity of a track in a QuickTime movie. You can control the playback quality of a movie during movie playback. QuickTime chooses tracks from alternate tracks that most closely correspond to the display quality desired. See also [alternate track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga3ta).

- __player__

  See [music player](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi4te).

- __plist__

  See [property list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu3ti).

- __plug-in__

  An external module of code and data separate from a host (such as an application, operating system, or other plug-in) that, by conforming to an interface defined by the host, can add features to the host without needing access to the source code of the host. Plug-ins are types of dynamically loadable bundles. They are implemented using the Core Foundation opaque type CFPlugin.

- __pmap__

  Part of Mach VM that provides an abstract way to set and fetch virtual-to-physical mappings from hardware. The pmap system is the machine-dependent layer of the VM system.

- __point size__

  The size of a font’s glyphs as measured from the baseline of one line of text to the baseline of the next line of single-spaced text. In the United States, point size is measured in typographic points.

- __pointer__

  (1) In programming, a data type whose value actually serves as a reference to a value stored in a specific location. (2) In a human interface, a [cursor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvjvomi).

- __policy-based system__

  A system that requires authorization to perform a privileged operations.

- __policy database__

  A database containing the set of rules the Security Server uses to determine authorization.

- __polynomial function__

  In image processing, an equation commonly used for transforming pixel intensities in an image that is a summation of n factors and coefficients in the form of _ax_ n _+ bx_ n _–1 + ... cx_ 0.

- __polyphonic__

  Describes an instrument capable of playing more than one note simultaneously. Compare [monophonic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi2ts). See also [monotimbral](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi3da), [multitimbral](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi4ta).

- __pool__

  See [buffer pool](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgizte).

- __pop-up menu__

  A menu that, when closed, displays the current choice and can be opened to present a list of mutually exclusive choices in a dialog or window. Pop-up menus have a double triangle indicator.

- __port__

  (1) In Mach, a secure unidirectional channel for communication between tasks running on a single system. (2) In IP transport protocols, an integer identifier used to select a receiver for an incoming packet or to specify the sender of an outgoing packet. (3) In Quartz Composer, the mechanism by which patches communicate. Ports can represent input or output parameters. Connections between input and output ports of different patches establish a data flow in a composition. See also [MIDI port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgiztm).

- __port name__

  In Mach, an integer index into a port namespace; a port right is specified with respect to its port name. See also [port right](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq4to).

- __port right__

  In [Mach](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4dm), a specification of which task can send to or receive from a particular [port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq4tk).

- __port right name__

  A small integer used to identify a Mach [port right](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq4to). Each process has a port right namespace, which maps port right names to their corresponding port rights. A port right name is meaningful only within that task’s port right namespace.

- __port set__

  In Mach, a set of zero or more Mach ports. A thread can receive messages sent to any of the ports contained in a port set by specifying the port set as a parameter to `msg_receive()`.

- __positional parameter__

  In AppleScript, a handler parameter that is identified by the order in which it is listed. In a handler call, positional parameters are enclosed in parentheses and separated by commas. They must be listed in the order in which they appear in the corresponding handler definition.

- __POSIX__

  Portable Operating System Interface. An operating-system interface standardization effort supported by ISO/IEC, IEEE, and The Open Group.

- __postcompensation action__

  In text layout, the extra processing, such as addition of kashidas and ligature decomposition, that occurs after glyphs have been repositioned during justification.

- __poster__

  A frame shot from a movie, used to represent its content to the user.

- __PostScript__

  A language that describes the appearance (text and graphics) of a printed page. PostScript is an industry standard for printing and imaging. Many printers contain or can be loaded with PostScript software. PostScript handles industry-standard, scalable typefaces in the Type 1 and TrueType formats. PostScript is an output format of Quartz.

- __power child__

  In the power plane, a driver for a device that relies on another object for its power. Compare [power parent](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrguydm). See also [plane](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq3tq).

- __power parent__

  In the power plane, an object that provides power for a device. Compare [power child](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrguydk). See also [plane](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq3tq).

- __PPD file__

  PostScript printer description file. A text file, created by a printer vendor, that contains keywords and other information to specify features, options, and settings for a specific printer.

- __preauthorization__

  A form of authorization used before performing the actual authorization. Preauthorization is used to determine if a user has the possibility of authorizing later.

- __prebinding__

  A process that Xcode applies when a program is built, by which the static linker replaces references to external symbols with the addresses of the symbols in the referenced libraries or tells the dynamic linker to resolve the references when a program is loaded or when a symbol is referenced.

- __preemption__

  The act of interrupting a currently running program in order to give time to another task.

- __preemptive multitasking__

  A type of multitasking in which the operating system can interrupt a currently running program in order to run another program, as needed. Compare [cooperative multitasking](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgqzdo).

- __preferred application__

  The application selected by Launch Services in which to open a given document or URL, either through an explicit [binding preference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgiydk) set by the user or, in the absence of such a user preference, by applying the implicit [binding rules](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgiydm) of Launch Services for determining the item’s [default application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqguydi).

- __preferred rate__

  The default playback rate for a QuickTime movie.

- __preferred volume__

  The default sound volume for a QuickTime movie.

- __prefetching__

  A feature in Enterprise Object that allows you to suppress fault creation for an entity’s relationships. Instead of creating faults, the relationship data is fetched when the entity is first fetched. See also [faulting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4ztk).

- __prefix searching__

  A specialized type of substring search. A prefix search involves matching a term in a query string to indexed terms, with an explicit wildcard character at the end of the query term. A match occurs when the characters in the query term (minus the wildcard character) match the beginning of an indexed term. For example, the query string `car*` will match `car`, `carpet`, and `carnivore`. Search Kit supports prefix searching in inverted and inverted-vector indexes. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayde), [substring searching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe3dg), [wildcard character](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2tq).

- __premultiplied__

  In image processing, said of a pixel that already has its intensity levels appropriately multiplied by the alpha value.

- __premultiplied alpha__

  A source color whose components are already multiplied by an alpha value. Premultiplying speeds up the rendering of an image by eliminating an extra multiplication operation per color component. See also [alpha](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga3dq).

- __preset__

  A predefined set of [parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqzdg) values for an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq).

- __preview__

  A short, potentially dynamic, visual representation of the contents of a file. Previews in file dialog boxes give the user a visual cue about a file’s contents. See also [file preview](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg42te).

- __preview atom__

  An atom of type `'pnot'`, which can appear in a QuickTime file to contain a movie’s file preview.

- __primary key__

  In relational databases, an attribute in an entity that uniquely identifies rows of that entity. For example, the Employee entity can contain an `empID` attribute that uniquely identifies each employee.

- __primary line direction__

  The dominant line direction (right-to-left or left-to-right) of the current text. The primary line direction is typically specified by the value of the global system direction variable. See also [line direction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge3dc).

- __priming__

  Adding [leading frames](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgezts) or [trailing frames](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgezda) to a set of audio data to support format conversion or [SRC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhezde) (sample rate conversion). If a converter requires priming and no leading or trailing frames are available, silent priming frames are typically used. See also [priming frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrguzdk).

- __priming frame__

  A [webpage template](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2tc) of audio data used for [priming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrguzdi).

- __primitives__

  The simplest elements in OpenGL—points, lines, polygons, bitmaps, and images.

- __Print Center__

  An application that allows users to locate and select printers, and control and obtain status for print jobs.

- __Print dialog__

  A dialog—usually displayed by an application in response to the user choosing the Print command—that solicits printing information from the user, such as the number of copies to print and the range of pages to print.

- __printer browser__

  A module used to discover specific types of printers, such as USB or LPR printers.

- __Printer Features pane__

  A pane in the Print dialog that contains any user interface feature specified in a PostScript printer description (PPD) file that isn’t already a feature in Apple-provided panes or a developer’s custom pane.

- __printer module__

  A printing plug-in that renders the graphics content in a print job for output to a specific model or family of printers. Printer modules are created by printer vendors to support a particular printer or printer family.

- __printer queue__

  A temporary holding area for print jobs waiting to be printed.

- __printing dialog__

  A window provided by the printing system to elicit a response from the user. See also [Page Setup dialog](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqydo), [Print dialog](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrguzdq).

- __printing dialog extension__

  A printing plug-in that implements one or more panes in a printing dialog.

- __Printing Manager__

  A collection of system software routines that can be used by a Classic application to print from the Macintosh computer to any type of connected printer. This has been replaced by the [Carbon Printing Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3dm).

- __printing plug-in__

  A stand-alone code module—packaged as a Core Foundation plug-in—that adds functionality to the OS X printing system.

- __printing presets__

  Printer-specific collections of settings for the Print dialog. Printing presets are provided by Apple or printer vendors to reduce the need for users to navigate to different panes in the Print dialog. Presets are defined for a specific printing task, such as printing a photo on glossy photo paper.

- __printing session object__

  An opaque data type used by the printing system to store information that’s needed by the page format and print settings objects, such as default page format and print settings values.

- __print job__

  The drawing commands that describe a document and the settings that control printing the document and keep track of it once the job has been added to a printer’s queue.

- __print loop__

  The sequence of function calls that set up and execute the printing of a document in an application.

- __print settings__

  Information that controls the execution of a print job on a specific printer; print settings include such information as the number of copies, number of pages per sheet, and print quality settings.

- __print settings object__

  An opaque data type used by the printing system to store information from the Print dialog, such as number of copies, number of pages per sheet, and print quality.

- __priority__

  In scheduling, a number that indicates how likely a thread is to run. The higher the thread’s priority, the more likely the thread is to run. See also [scheduling policy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg43do).

- __private key__

  A cryptographic [key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4ti) that must be kept secret. Whereas a pair of identical private keys can be used as [symmetric keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4da), [asymmetric keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgeztm) consist of one private key and one [public key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4te).

- __private MLTE scrap__

  Scrap used exclusively by MLTE.

- __privileged operation__

  An operation that requires special rights or permissions; for example, changing a locked system preference.

- __probe__

  A phase of active matching in which a candidate driver communicates with a device and verifies whether it can drive it. The driver’s `probe` member function is invoked to kick off this phase. The driver returns a probe score that reflects its ability to drive the device. See also [driver matching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyzdi).

- __process__

  The runtime instance of an application or program. A process has its own virtual memory space and system resources (including port rights) that are independent of those assigned to other programs. A process always contains at least one thread (the main thread) and may contain any number of additional threads.

- __process dispatch source__

  A [dispatch source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvjvomq) used to handle process-related events. A process source calls your custom event handler in response to changes to the process you specify.

- __process GID__

  The [GID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhaztg) of a process. Each process has three group IDs: the real group ID (RGID), effective group ID (EGID), and saved group ID (SGID). The RGID is always inherited from the user or process who executes the process. The EGID is the first GID in the [group list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqha2tq). The SGID is used by BSD to enable a privileged process to switch in and out of privileged mode.

- __process identifier__

  See [simple statement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2to).

- __processor__

  In Quartz Composer, a patch that processes data at specified intervals or in response to changing input values.

- __process UID__

  The [UID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2ds) of a process. Each process has three user IDs: the real user ID (RUID), effective user ID (EUID), and saved user ID (SUID). The RUID is always inherited from the user or process that executes the process. The EUID is normally the same as the RUID but can differ in special circumstances. It is the EUID that BSD checks to determine permissions. The SUID is used by BSD to enable a privileged process to switch in and out of privileged mode.

- __product__

  An application or framework produced by Xcode.

- __product component__

  A self-contained part of a product. A product can have one or more components. The OS X file system contains special locations for several types of components. For example, application binaries are placed in `Application` directories, plug-ins are housed in `Plugin` directories, fonts live in `Fonts` directories, and so on.

- __product container__

  A file that contains a packaged or unpackaged product. The two container types are disk image and ZIP archive.

- __product directory__

  The file-system directory that contains a project file, the project’s source code and resources, and the build directory.

- __product package__

  An installation package that contains all the components of a product. Product packages with multicomponent products contain or reference component packages. See also [installation package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe4to).

- __product package editor__

  A pane in a PackageMaker project window that specifies packaging and installation information about a product. This pane is displayed when the product package is selected in the [package list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm4te).

- __product reference__

  In Xcode, a special type of file reference that refers to the build system output for a particular target. A product reference lets you view your target’s products in the Groups & Files list.

- __profile atom__

  An atom of type `'prfl'`, which summarizes the features of a movie or track.

- __profile rendering mode__

  In Quartz Composer, a view that displays an analysis of each rendered frame in a composition; the analysis can help you to optimize performance.

- __program__

  A combination of code and resources that can be run to perform some task. Programs need not have a graphical user interface, although graphical applications are also considered programs.

- __programmatic socket filter__

  A socket filter that is enabled only under program control by calling `setsockopt` on a specific socket.

- __programmed I/O__

  I/O in which the CPU accomplishes data transfer with explicit load and store instructions to device registers, rather than DMA, and without the use of interrupts. This data transfer is often done in a byte-by-byte, or word-by-word fashion. Also known as _direct I/O_ or _polled I/O_. See also [DMA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4tg).

- __Program Portal__

  A restricted-access area of the iOS Dev Center that allows you to configure devices to test your iOS applications.

- __progress indicator__

  A control that lets the user know that a task is in progress.

- __project configuration__

  In Xcode, the set of development features, project attributes, and project and target build settings used in a project.

- __project file__

  A file created by Xcode that organizes source code, resources, and settings used to build a product.

- __Project Info window__

  In Xcode, the Info window for viewing and editing information kept at the project level, such as general information, project build settings, project build configurations, and project comments.

- __projection matrix__

  A matrix that OpenGL uses to transform points, lines, polygons, and positions from eye coordinates to clip coordinates.

- __project root__

  In Xcode, the directory at which source-control operations are rooted and that serves as the origin of a project hierarchy. By default, a project root is the project directory.

- __project window__

  A window that displays and organizes the files that make up an Xcode project.

- __property__

  (1) A labeled container in which to store a value. Properties can specify characteristics of objects. (2) In KVC, any of the three kinds of object values that KVC can access: attributes, to-one relationships, and to-many relationships. (3) In a scripting definition file, a characteristic of a class that has a single value and is identified by a label. Synonymous with a key-value coding (KVC) attribute or to-one relationship. A window’s `name` property would be equivalent to a KVC attribute, while its `document` property would be equivalent to a KVC to-one relationship. (3) In Core Audio, a key-value pair that declares an attribute or behavior, such as audio data stream format or latency. Each property has an associated data type to hold its value. Properties are typically non-time-varying and not directly settable by the user. Compare [parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqzdg). (4) In Entity-Relationship modeling, an attribute or relationship. See also [attribute](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tc), [relationship](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy2ts)

- __property list__

  A structured, textual representation of data, commonly stored in Extensible Markup Language (XML) format. Elements of a property list represent data of certain types, such as arrays, dictionaries, and strings. See also [information property list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe3do).

- __property reference form__

  In AppleScript, a reference form that specifies a property of an `application` , `record` , or `script` object.

- __prosodic control symbol__

  See [phoneme modifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2tm).

- __prosody__

  The rhythm, intonation, and lexical stress in speech.

- __protected memory__

  See [memory protection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgiyts).

- __protocol handler__

  A network module that extracts data from input packets (giving the data to interested programs) and inserts data into output packets (giving the output packet to the appropriate network device driver).

- __protocol plumber__

  A network kernel extension that routes data between an interface and a network protocol stack.

- __protocol stack__

  A layer of the kernel network architecture containing the core functionality for a protocol family such as TCP/IP.

-  __`protosw` structure__

  A data structure containing function pointers and data associated with a protocol family.

- __prototype attribute__

  A special type of attribute available in EOModeler to provide a template for creating attributes.

- __provider__

  (1) A driver object that provides services of some kind to its client. In a driver stack, the provider in a provider/client relationship is closer to the Platform Expert. See also [client](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmzds). (2) In Quartz Composer, a patch that supplies data from an outside source to a composition. (3) In web services, an application that executes the logic that implements a web service operation.

- __provider identifier__

  An identifier for the entity responsible for the contents of an installation package; for example,`com.apple` . PackageMaker uses this identifier to generate default package identifiers for a product package’s components. See also [package identifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm4tc).

- __provisioning profile__

  A file that allows applications in development to be installed on an iOS-based device. It contains one or more development certificates, an application ID, and one or more device IDs

- __proxy icon__

  An icon in the title bar of a document window that users can manipulate as if they were manipulating the corresponding file-system object. Users can Command-click the proxy icon to display a pop-up menu illustrating the document path.

- __proxy object__

  In Interface Builder, a placeholder for an object that is specified at runtime. Proxy objects act as stand-ins for objects that are not available at design time. Instead, such objects are created by a running application and connected to the objects in a nib file when that nib file is loaded. Cocoa nib files use proxy objects to represent the owner of a nib file’s contents, the application object itself, and the first object to respond to events.

- __pseudorandom number__

  A number generated by an algorithm that produces a series of numbers with no discernible pattern. It should be impossible or nearly impossible to deduce the algorithm from such a series. However, unlike a truly random number generator, a pseudorandom number generator always produces the same series if the algorithm is given the same starting value or values.

- __psychoacoustics__

  The study of the perception of sound. The development of [perceptual coding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2dq) techniques relies on psychoacoustics.

- __pthreads__

  The POSIX threads implementation. See also [WebObjects Builder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2ds), [thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2tq).

- __public key__

  A cryptographic key that can be shared or made public without compromising the cryptographic method. See also [public key cryptography](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4ti).

- __public key certificate__

  See [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2tg).

- __public key cryptography__

  A cryptographic method using [asymmetric keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgeztm) in which one key is made public while the other (the _private key_) is kept secure. Data encrypted with one key must be decrypted with the other. If the public key is used to encrypt the data, only the holder of the private key can decrypt it; therefore the data is secure from unauthorized use. If the private key is used to encrypt the data, anyone with the public key can decrypt it. Because only the holder of the private key could have encrypted it, however, such data can be used for [authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3de). See also [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2tg), [digital signature](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2to).

- __public key infrastructure__

  See [PKI](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq3tg).

- __pull__

  In Core Audio, to request and receive audio data, typically from a [buffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgiztc). Data typically moves through an [audio processing graph](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tg) by way of a cascade of pull requests initiated by the [head node](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqha3tg). The head node pulls, and each object upstream passes on the pull until the cascade reaches an audio data source.

- __pulse-code modulation__

  See [PCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2de).

- __push button__

  A rounded rectangle with a text label on it, which the user clicks to perform an instantaneous action, such as saving a document, completing operations defined by a dialog, or acknowledging an error message.

-  __`QCPlugIn`__

  A class defined by the Quartz framework that provides the base class to subclass for writing custom patches.

- __QT atom__

  A QuickTime atom that contains other atoms, possibly including other QT atoms and classic atoms. A data reference atom is an example of a QT atom. Compare [classic atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmzdi).

- __QTMA__

  QuickTime Music Architecture. The part of QuickTime that lets other code create and manipulate music tracks in movies.

- __QTVR track__

  A track in a QuickTime movie that maintains a list of VR nodes.

- __quadratic curve__

  A curve specified by a quadratic equation.

- __quantization__

  The process of representing an analog (continuous-scale) value by a digital (discrete-scale) value. Quantization is characterized by a [bit depth](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgiydq), which determines the dynamic range that can be represented, and a scaling factor, which determines the ratio between the analog and digital scales.

- __quantization error__

  The difference between an original analog signal value and its quantized digital representation. Quantization can sometimes results in a signal-correlated noise called [quantization noise](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyydm). See also [dither](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4ta).

- __quantization noise__

  Signal-correlated [noise](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmzda) resulting from rounding errors when quantizing a series of data samples. Application of a [dither](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4ta) signal during analog-to-digital conversion can decorrelate quantization noise from the signal. The perceptual result is low-amplitude noise instead of distortion.

- __quantum__

  The fixed amount of time a thread or process can run before being preempted.

- __quantum computer__

  A computer in which the logic gates are based on quantum phenomena such as electron spin rather than mechanical or conventional electronic components. Because of the superposition of quantum states (a consequence of the Heisenberg Uncertainty Principle), a properly designed quantum computer can in principle perform simultaneously certain types of calculations that require a huge number of sequential operations in a classic computer. Consequently, factoring large numbers should be several orders of magnitude faster on a quantum computer than on present-day supercomputers. Because the strength of most modern cryptographic methods depends on the difficulty of making such calculations, a practical quantum computer would break most cryptographic schemes in common use. Although small proof-of-concept quantum computers have been constructed, no such machine capable of solving practical problems has yet been demonstrated.

- __Quartz__

  The native 2D rendering API for OS X. Quartz contains programmatic interfaces that provide high-quality graphics, compositing, translucency, and other effects for rendered content. Quartz is included as part of the Application Services umbrella framework.

- __Quartz Compositor__

  An advanced windowing system that manages the onscreen presentation of Quartz, OpenGL, and QuickTime content, much as a video mixer does.

- __Quartz Extreme__

  A technology integrated into the lower layers of Quartz that enables many graphics operations to be offloaded to hardware. This offloading of work to the graphics processing unit (GPU) provides tremendous acceleration for graphics-intensive applications. This technology is enabled automatically by Quartz and OpenGL on supported hardware.

- __query__

  (n.) A text string, containing terms and operators, that represents a user’s information retrieval request. Various types of query supported by Search Kit include simple, prefix/suffix/substring, Boolean, phrase, and similarity. (v.) To invoke a request for information in an information retrieval system. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayde).

- __queue__

  A queue is a JMS construct that allows for point-to-point messaging between applications. A message sent to a queue can be received by only one application. When several applications are subscribed to the queue, the messages are load balanced between the subscribers.

- __queue-synchronized state__

  The state of an input device according to the events that have been dispatched from the event queue. This state may differ from the actual physical state of the input device.

- __QuickDraw__

  The original Mac OS two-dimensional drawing software, used by QuickTime.

- __Quick Look framework__

  A framework that provides a plug-in architecture for custom document types. A Quick Look document type can be displayed as a preview in the Finder and as an item in such applications as iPhoto or any application that supports slideshows created with the `IKSlideshow` class.

- __QuickTime__

  Apple’s multimedia authoring and rendering technology, implemented as a set of Macintosh system extensions or a Windows dynamic-link library that other code can use to create and manipulate time-based data.

- __QuickTime VR__

  A QuickTime media type that lets users interactively explore and examine photorealistic three-dimensional virtual worlds. QuickTime VR data structures are also called _panoramas_.

- __radial gradient__

  A fill that varies radially along an axis between two defined ends, which typically are both circles. Points share the same color value if they lie on the circumference of a circle whose center point falls on the axis. The radius of the circular sections of the gradient are defined by the radii of the end circles; the radius of each intermediate circle varies linearly from one end to the other.

- __radio button__

  A control for one of a set of mutually exclusive, but related, choices.

- __RAM__

  Random-access memory. Memory that a microprocessor can either read or write to.

- __Randomization Services__

  AniOS API that produces cryptographically secure [pseudorandom number](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4ds)s.

- __range reference form__

  In AppleScript, a reference form that specifies a series of objects of the same class in the same container.

- __ranked searching__

  See [relevance-based result](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy3dk).

- __raster graphics__

  Digital images created or captured (for example, by scanning a photo) as a set of samples of a given space. A raster is a grid of x-axis (horizontal) and y-axis (vertical) coordinates on a display space. (Three-dimensional images also have a z-coordinate.) A raster image identifies the monochrome or color value with which to illuminate each of these coordinates. The raster image is sometimes referred to as a bitmap because it contains information that is directly mapped to the display grid. A raster image is usually difficult to modify without loss of information. Examples of raster-image file types are BMP, TIFF, GIF, and JPEG files. See also [vector graphics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgiydi).

- __rasterization__

  In image processing, the process of converting vertex and pixel data to fragments, each of which corresponds to a pixel in the framebuffer.

- __rate__

  In QuickTime, a value that specifies the pace at which time passes for a time base. A time base’s rate is multiplied by the time scale to obtain the number of time units that pass per second. For example, consider a time base that operates in a time coordinate system that has a time scale of 60. If that time base has a rate of 1, 60 time units are processed per second. If the rate is set to 1/2, 30 time units pass per second. If the rate is 2, 120 time units pass per second. See also [time base](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3ds), [time unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga4dc).

- __rating indicator__

  A control that displays a number of stars that indicates the relative ranking of an object (such as a song) based on a criterion such as popularity.

- __raw format__

  In AppleScript, terms enclosed in double angle brackets («, »). AppleScript uses raw format when it cannot find a script term in any available dictionary, or cannot display data in its native format.

- __raw row fetching__

  In WebObjects, a possible option in a fetch specification that retrieves database rows without forming enterprise objects from those rows.

- __real number__

  A number that can include a decimal fraction.

- __real position__

  The actual drawing position on the x-axis for the origin of each character or glyph in a line of text given in coordinates relative to the preceding character or glyph.

- __real time__

  In reference to operating systems, a guarantee of a certain capability within a specified time constraint, thus permitting predictable, time-critical behavior. If the user defines or initiates an event and the event occurs instantaneously, the computer is said to be operating in real time. Real-time support is especially important for multimedia applications.

- __real-time performance__

  Performance characterized by guaranteed worst-case response times.

- __realm__

  In security, a subset of a large network served by its own Kerberos [authentication server](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3dg) and [ticket-granting server](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3dk).

- __receiver__

  The object in an application designated to receive an AppleScript command.

- __receive rights__

  In Mach, the ability to receive messages on a Mach port. Only one task at a time can have receive rights for any one port. Compare [send rights](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhazdg).

- __receivers specifier__

  In a script command object, the object specifier that specifies the objects in the application that should receive an command.

- __recognized text__

  In Ink Services, Ink words processed by the recognition system.

- __recognizer__

  The algorithmic component of Ink Services that identifies written text and gestures.

- __record__

  (1) In databases in general, the set of values that describes a single instance of an entity. (2) In AppleScript, an unordered collection of properties, identified by unique labels.

- __recordable application__

  In AppleScript, an application that uses Apple events to report user actions for recording purposes. When recording is turned on, Script Editor creates statements corresponding to any significant actions you perform in a recordable application.

- __recording audio queue__

  See [audio queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2ti).

- __recursive handler__

  A handler that calls itself.

- __recursive lock__

  A lock that can be locked multiple times by the same thread.

- __reentrant__

  Said of code that can process multiple interleaved requests for service nearly simultaneously. For example, a reentrant function can begin responding to one call, be interrupted by other calls, and complete them all with the same results as if the function had received and executed each call serially.

- __refactoring__

  The process of modifying source code for the purpose of improving its readability and maintainability while retaining the program’s functionality and behavior. See also [transformation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgezde).

- __reference__

  In AppleScript, the part of a script statement that identifies an object. Constructions such as `first rectangle` and `document "My Notes"` are references. Cocoa scripting provides built-in support for standard AppleScript reference forms.

- __reference constant__

  An arbitrary data item available for use by a program to convey information for its own purposes in an operation or data structure.

- __reference distance__

  In Core Audio, for a [panner unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqyto), a [parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqzdg) that specifies the real or apparent distance of an audio source from the listener beyond which the source’s level attenuates.

- __reference form__

  In AppleScript, the syntax for identifying an object or group of objects in an application or other container—that is, the syntax for constructing an object specifier. AppleScript defines reference forms for arbitrary, every, filter, ID, index, middle, name, property, range, and relative.

- __referential integrity__

  In relational databases, the rules governing the consistency of relationships.

- __reflexive relationship__

  In relational databases, a relationship within the same entity; the relationship’s source join attribute and destination join attribute are in the same entity.

- __region code__

  A code identifying one of the world regions for restricting DVD-Video playback. The world has been divided into eight separate regions to accommodate the varying release patterns of movies by the major studios. Therefore, each DVD player is compatible with a certain region: Region 1 for the United States and Canada, for example, and Region 2 for Japan and Europe. A DVD designated Region 0 can be played on any player regardless of its nationality.

- __region of interest__

  See [Security Server](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayto).

- __register__

  To make an application known to Launch Services, copying its [binding information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgiydi) into the [Launch Services database](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgezds) and making it available for opening documents and URLs.

- __relational database__

  A database designed according to the relational model, which uses the discipline of Entity-Relationship modeling and the data design standards called normal forms.

- __relationship__

  In relational databases, a link between two entities that’s based on attributes of the entities. For example, the Department and Employee entities can have a relationship based on the `deptID` attribute as a foreign key in Employee, and as the primary key in Department. This relationship would make it possible to find the employees for a given department.

- __relationship key__

  In relational databases, a key (an attribute) on which a relationship joins.

- __relative object specifier__

  In AppleScript, an object specifier that does not include enough information to identify an object or objects uniquely. When AppleScript encounters a partial object specifier, it uses the default object specified in the enclosing `tell` statement to complete the reference. Compare [absolute object specifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgaydm).

- __relative position__

  A position for the origin of each character or glyph in a line of text given in coordinates relative to the preceding character or glyph. Compare [absolute position](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgaydo).

- __relative reference form__

  In AppleScript, a reference form that specifies an object or location by describing its position in relation to another object, known as the _base_, in the same container.

- __release__

  A decrementing of the reference count of an object. When an object’s reference count reaches zero, it is freed. When your code no longer needs to reference a retained object, it should release it. Some APIs automatically execute a release on the caller’s behalf, particularly in cases where the object in question is being “handed off.” Retains and releases must be carefully balanced; too many releases can cause panics and other unexpected failures due to accesses of freed memory. See also [retain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4yda).

- __relevance-based result__

  See [relevance-based search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy3dm).

- __relevance-based search__

  A ranked search whose result includes a relevance rating for each document matching a query. In general, relevance ratings may be normalized to 100%, or nonnormalized. Search Kit supports only nonnormalized results. See also [inclusion/exclusion searching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe3dc), [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayde).

- __relevance indicator__

  A control that indicates the relative ranking of search results—the longer the bar, the more relevant the item is to the search criteria.

- __relocatable component__

  A product component, such as an application binary or a plug-in, that the user may move after it has been installed.

- __relocation__

  The ability of users to change the installation location of a package before an installation.

- __remote install__

  A network administrator–driven installation process. An administrator uses Apple Remote Desktop to install a package onto a set of client computers.

- __remote procedure call__

  See [RPC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4ztk).

- __render__

  In Core Audio, to apply a recipe or specification for signal processing to some audio data. An [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) typically contains a rendering method to obtain audio data and perform processing.

- __renderbuffer__

  In OpenGL, a rendering destination for a 2D pixel image, used for generalized offscreen rendering, as defined in the OpenGL specification for the `GL_EXT_framebuffer_object` extension.

- __renderer__

  A combination of hardware and software, or software only, that OpenGL uses to create an image from a view and a model. The hardware portion of a renderer is associated with a particular display device and supports specific capabilities, such as the ability to support a certain color depth or buffering mode. A renderer that uses only software is called a software renderer and is typically used as a fallback.

- __rendering context__

  In OpenGL, a container for state information.

- __rendering intent__

  Specifies how Quartz maps colors from the source color space to those that are within the gamut of the destination color space of a graphics context.

- __rendering pipeline__

  The order of operations used by OpenGL to transform pixel and vertex data to an image in the framebuffer.

- __render-to-texture__

  In OpenGL, an operation that draws content directly to a texture target.

- __repeat statement__

  In AppleScript, a control statement that contains a series of statements to be repeated and, in most cases, instructions that specify when the repetition stops.

- __reply port__

  A Mach port associated with a thread that is used in remote procedure calls.

- __repository__

  A directory tree or database that contains the files managed by a source control system.

- __repository configuration__

  A set of data that tells Xcode how to use a particular source-control client tool to access a specific repository.

- __request__

  A message conforming to the Hypertext Transfer Protocol (HTTP) sent from the user’s web browser to a web server that asks for a resource such as a webpage. See also [response](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy4tq).

- __request-response loop__

  The main loop of a WebObjects application, which receives a request, responds to it, and awaits the next request.

- __required events__

  Certain Apple events that all Mac apps that present a graphical user interface should be able to respond to. These events can be sent by the Mac OS, as well as by other applications and by users executing scripts. They include the `open application`, `open documents`, `print documents`, `open contents`, `reopen`, and `quit` events.

- __required parameter__

  In AppleScript, a parameter that must be included for a command to be successful.

- __resampling__

  (1) In audio, the process of taking samples of a digitized signal at a rate different from that of the original recording. Specific types of resampling include downsampling (resampling at a rate lower than the original) and upsampling (resampling at a higher rate). (2) In image processing, an operation that changes the dimensions of an image.

- __resampling filter__

  A function used to determine new pixel values for an image that has its dimensions changed somehow.

- __Research Assistant__

  A lightweight window that provides a condensed view of the API reference and links to related documentation for the selected system or build setting.

- __reserved word__

  A word that is part of the AppleScript language.

- __reset__

  (1) For audio units, to return an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) to its just-initialized state. (2) For codecs, to clear the codec’s input [buffer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgiztc) and return the codec to its just-initialized state.

- __resize control__

  The area in the lower-right corner of windows that users can drag to adjust the size of the window. It is not present if the window’s contents cannot vary in size.

- __resolution__

  The number of pixels (individual points of color) contained on a display, expressed in terms of the number of pixels on the horizontal axis and the number on the vertical axis. The sharpness of the image on a display depends on the resolution and the size of the monitor. The same resolution will be sharper on a smaller monitor and gradually lose sharpness on larger monitors because the same number of pixels are being spread out over a larger area. Resolution is usually specified in dots per inch, or [dpi](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyyto), in the x and y directions.

- __resolution independence__

  A feature that supports drawing to an abstract space such that drawing is the same size when rendered for raster devices of any native resolution.

- __resource__

  Anything used by executable code, especially by applications. Resources include images, sounds, icons, localized strings, archived user interface objects, and various other things. OS X supports both Resource Manager–style resources and “per-file” resources. Localized and nonlocalized resources are put in specific places within bundles.

- __resource fork__

  The part of a file that historically held an application’s resources. Use of the resource fork is discouraged in OS X, but you can store resources in the data fork.

- __responder chain__

  The set of objects responsible for handling events in a window.

- __response__

  In WebObjects, a message conforming to the Hypertext Transfer Protocol (HTTP) sent from the web server to the user’s web browser that contains the resource specified by the corresponding request. The response is typically a webpage. See also [request](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy4dg).

- __result__

  In AppleScript, a value generated when a command is executed or an expression evaluated.

- __retain__

  An incrementing of the reference count of an object. An object with a positive reference count is not freed. (A newly created object has a reference count of one.) Drivers can ensure the persistence of an object beyond the present scope by retaining it. Many APIs automatically execute a retain on the caller’s behalf, particularly APIs used to create or gain access to objects. Retains and releases must be carefully balanced; too many retains will result in wired memory leak. Compare [release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy3di).

- __retained window__

  A window with an offscreen buffer for screen pixel values. Images are rendered into the buffer for any portions of the window that aren’t visible onscreen.

- __return statement__

  In AppleScript, a statement that exits a handler and optionally returns a specified value.

- __reusable component__

  In WebObjects, a component that can be nested within other components and acts like a dynamic element.

- __reverb__

  See [reverberation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4ydk).

- __reverberation__

  An acoustic phenomenon produced by the cumulative addition of multiple sound reflections. Apple supplies the matrix reverb audio unit to simulate reverberation using [DSP](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyztc) (digital signal processing).

- __reverse multiplexing__

  See [deinterleaving](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqguytk).

- __revision number__

  A value that indicates a particular version of a project that’s been committed to the repository, also known as a _version number_.

- __RGBA__

  Red, green, blue, and alpha color components.

- __RGID__

  Real group ID. A group ID that is inherited from the user or process that executes a process. See also [GID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhaztg).

- __RIFF__

  Resource Interchange File Format. A minor variation on [IFF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhezta) that uses little-endian integers.

- __right__

  In security, a named privilege. The Security Server authorizes rights for a user to perform a privileged operation.

- __right-side bearing__

  The white space on the right side of the glyph; this value may or may not be equal to the value of the left-side bearing.

- __RMS__

  Root mean square. A statistical measure of a time-varying value, such as voltage, current, or sound pressure. An RMS value is derived as the square root of the mean of the squares of a series of values. In the case of a continuously varying value, it is derived from an integration of the transfer function. For the special case of a sine wave signal, the calculation simplifies to Vrms = 0.707 \* Vpeak. May also be written in lowercase as _rms_.

- __ROI__

  Region of interest. The portion of an image data buffer that is being operated upon by a function. It is not uncommon to allocate a large pixel buffer to hold several images and then process only the smaller ROIs when need be.

- __role__

  (1) An identifier of an application’s relation to a document type. There are five roles: Editor (reads and modifies), Viewer (can only read), Print (can only print), Shell (provides runtime services), and None (declares information about type). You specify document roles in an application’s information property list. (2) In Xcode, the scope of the header file in a project: public, private, or project.

- __role mask__

  A parameter specifying the [role](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4ytm) or roles that an application should [claim](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmzdc) with respect to a given item in order to be considered a candidate for opening that item.

- __ROM__

  Read-only memory. Memory that cannot be written to.

- __Roman baseline__

  The baseline used in most Roman scripts and in Arabic and Hebrew.

- __Roman character set__

  A set of characters used for the Roman writing system. Roman character sets include the Standard Roman character set and the ASCII character set.

- __Roman keyboard script__

  A keyboard script that uses the Roman character set.

- __root__

  (1) The user with unlimited system privileges. Also called the _superuser_. (2) The top directory in a BSD-style directory hierarchy. Written as a slash (/), it is the first element in every absolute pathname.

- __root atom__

  The largest atom container in a hierarchy, with atom type `'sean'`.

- __root certificate__

  A [certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi3tq) that can be verified without recourse to another certificate. Rather than being signed by a further certification authority (CA), a root certificate is verified using the widely available public key of the CA that issued the root certificate. Compare [anchor certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga3tg).

- __root certification authority__

  The owner of the [root certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4zdi).

- __root control__

  An invisible control within which all other controls for window are embedded.

- __root macro patch__

  In Quartz Composer, the main routine in a composition; the evaluation of a composition begins at the root macro patch. All patches are nested, at one level or another, within the root macro patch. Ports that you publish at the root macro patch are accessible externally.

- __root file system__

  The primary file system off which a computer boots, so named because it includes the root node of the file-system tree.

- __root user__

  The user on a UNIX system with a [UID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2ds) of 0. A process running with an [EUID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy4tm) of 0 is said to be _running as root_. The root user owns many of the primary system processes and has unlimited access to the file system objects on the devices attached to the computer. Also called the _superuser_.

- __root word__

  See [stem](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhezto).

- __rotation__

  In image processing, an operation that moves the coordinate space the specified angle.

- __round button__

  A circular push button.

- __routine__

  In Mach, a remote procedure call that returns a value. A routine can be used for synchronous or asynchronous operations. See also [simpleroutine](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2ts).

- __row__

  In a relational database, the dimension of a table that groups attributes into records.

- __RPC__

  Remote procedure call. An interface to IPC that appears (to the caller) as an ordinary function call. In Mach, RPCs are implemented using MIG-generated interface libraries and Mach messages.

- __RSA encryption__

  A system of [public key cryptography](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4ti), named for its inventors: Ron Rivest, Adi Shamir, and Leonard Adleman. The RSA algorithm takes two large prime numbers, finds their product, and then derives [asymmetric keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgeztm) from the prime numbers and their product. Because the public key includes the product, the private key could be derived from the public key if the product could be factored. No easy method for factoring products of large prime numbers is currently known, but it has not been mathematically proven that no such method is possible. Therefore, the discovery of a fast way to factor such numbers, or the development of [quantum computer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyyds)s, would break RSA.

- __RSS__

  Really Simple Syndication. A lightweight XML format used for displaying changes frequently updated websites.

- __ruby text__

  Text usually used to provide annotations or indicate pronunciation for Asian languages. Ruby text is displayed using a smaller font size than the text it annotates.

- __RUID__

  Real user ID. The [UID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2ds) inherited from the user or process that executes a process.

- __rule__

  A set of attributes used to set security policies for applications and for the system. See also [policy database](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq4ta).

- __run__

  A sequence of glyphs that are contiguous in memory and share a set of common attributes. See also [font run](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg44ts).

- __run loop__

  The fundamental mechanism for event monitoring in OS X. A run loop registers input sources such as sockets, Mach ports, and pipes for a thread; it also enables the delivery of events through these sources. In addition to sources, run loops can also register timers and observers. There is exactly one run loop per thread.

- __run loop mode__

  A collection of input sources, timer sources, and run loop observers associated with a particular name. When run in a specific mode, a run loop monitors only the sources and observers associated with that mode.

- __run loop object__

  An instance of the [NSRunLoop](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/cl/NSRunLoop) class or [CFRunLoopRef](https://developer.apple.com/documentation/corefoundation/cfrunloopref) opaque type. These objects provide the interface for implementing an event-processing loop in a thread.

- __run loop observer__

  A recipient of notifications during various phases of a run loop’s execution.

- __runtime__

  The period of time during which a program is being executed, as opposed to compile time or load time. Can also refer to the runtime environment, which designates the set of conventions that arbitrate how software is generated into executable code, how code is mapped into memory, and how functions call one another.

- __Safari__

  The default web browser that ships with OS X.

- __safety offset__

  A property of an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) or other audio device that specifies a time lag, in samples, to allow for improved robustness of driver operation. The safety offset required for a given architecture includes time needed for memory access and to account for inaccuracies in a driver’s timestamp resolution. Safety offset contributes to [latency](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgezdi).

- __Samba__

  Software that implements [SMB/CIFS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha3tg) on a UNIX server.

- __sample__

  (1) (n.) An instantaneous amplitude of the signal in a single audio channel, represented as an integer, floating-point, or fixed-point number. See also [fixed-point sample](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg43tm). (2) (v.) To collect samples from an audio source, typically an analog audio source. Sampling typically involves collecting samples at regular, very brief intervals such as 1/44,100 seconds. (3) (n.) An excerpt of a longer recording. When the excerpt is intended to be played repeatedly, it is called a [loop](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge3ts). (4) (v.) To record a sample to use as a loop or for inclusion in a another recording. (5) In QuickTime, a single element of a sequence of time-ordered data.

- __sample format__

  In QuickTime, the format of data samples in a track, such as a sprite track.

- __sample number__

  In QuickTime, a number that identifies the sample with data for a specified time.

- __sample period__

  The time span from one sample to the next. The inverse of [sample rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg42ti).

- __sample rate__

  During playback, the number of samples played per second for each channel of an audio file. During recording, the number of samples acquired per second for each channel. Also called _sampling rate_. More properly, but less commonly, called _sampling frequency_. Compare [frame rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhaytk).

- __sample rate conversion__

  See [SRC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhezde).

- __sampling frequency__

  An alternate name for [sample rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg42ti).

- __sandboxing__

  A system feature that provides fine-grained control of the ability of processes to access system resources, therefore limiting the amount of damage that can be done by a malicious hacker who gains control of an application.

- __SBR__

  Spectral Bandwidth Replication. A technique used in [AAC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgaydi) (Advanced Audio Coding) encoding (among other encoding technologies) to improve perceived audio quality.

- __scalar programming__

  A programming paradigm in which values are operated upon individually. Scalar programming is more common than [vector code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgiydg).

- __scale__

  To shrink or enlarge an image by a certain percent.

- __scaling__

  An operation that changes the scale of the coordinate space by the specified x and y factors, effectively stretching or shrinking coordinates. The magnitude of the x and y factors governs whether the new coordinates are larger or smaller than the original. A negative factor flips the corresponding axis.

- __scan direction__

  In DVD playback, a forward or backward direction with respect to the video stream.

- __scan rate__

  A constant used in DVD Playback Services to specify the speed of play. A scan rate of 1x represents the normal playback speed; other scan rates are multiples of the normal speed.

- __scene__

  See [chapter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmydc).

- __scheduler__

  The part of Mach that determines when each program (or program thread) runs, including assignment of start times. The priority of a program’s thread can affect its scheduling. See also [task](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgayti), [thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2tq).

- __scheduling__

  The determination of when each process or task runs, including assignment of start times.

- __scheduling policy__

  In Mach, how a thread’s priority is set and under what circumstances the thread runs. See also [priority](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu2dg).

- __schema__

  A file that describes the structure of an XML document. This file can be a DTD file or an XML Schema file.

- __scheme__

  The component of a URL that identifies the type of resource it represents or the protocol to be used for accessing it, such as `http`, `ftp`, `mailto`, or `file`. See also [document URL object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyydk).

- __scheme-definition dictionary__

  A dictionary, specified in an application’s [bundle information property list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi2tg), that declares a particular URL type that the application claims to handle. Compare [type-definition dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2dc).

- __SCM__

  Source control management. A set of tools and procedures developers can use for managing files and changes made to them over time. Also known simply as _source control_ or as _version control_.

- __SCM repository__

  Source Code Management repository. A code database used to enable the collaborative development of large projects by multiple engineers. An SCM repository is managed by specific tools (such as CVS and Subversion), which manage the repository and handle check-ins and check-outs of code resources by engineers.

- __scope__

  (1) The availability of resources such as variables and objects within various parts of a program. In traditional procedural programming, scope is either global or local; however, scopes can be nested. (2) In AppleScript, the range over which AppleScript recognizes a variable or property, which determines where else in a script you may refer to that variable or property. (3) In Core Audio, a programmatic context within an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq). Unlike the general computer science notion of scopes, however, audio unit scopes cannot be nested. Each scope is a discrete context. You use scopes when writing code that sets or retrieves values of parameters or properties. Compare [element](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy3dm). See also [parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqzdg), [property](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu3tg).

- __screen metrics__

  Resolution-dependent measurements used to describe how a glyph is drawn. Compare [ideal metrics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqheytq).

- __script__

  (1) A series of statements, written in a scripting language such as AppleScript or Perl, that instruct an application or the operating system to perform various operations. Interpreter programs translate scripts. (2) A method for depicting words visually. Some examples of scripts are Latin, Greek, Hiragana, Katakana, and Han.

- __scriptability information__

  Information that formally lays out the AppleScript object model for an application and maps it to application objects. Scriptability information specifies the terminology available for use in scripts that target the application. It also provides information, used by AppleScript and by Cocoa, about how support for that terminology is implemented in the application. See also [scripting definition format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg44di), [script suite format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg44ds).

- __scriptable application__

  An application that can be controlled by a script. For AppleScript, that means being responsive to interapplication messages, called Apple events, sent when a script command targets the application.

- __script application__

  An application whose only function is to run a script associated with it.

- __script command object__

  An object that encapsulates all the information needed to perform an AppleScript command. Cocoa scripting creates script command objects in response to Apple events received by the application. A script command object is instantiated from `NSScriptCommand` or from one of its subclasses—either those provided by Cocoa scripting to handle standard AppleScript commands, or those defined by your application to perform its unique operations.

- __Script Editor__

  An application distributed with OS X that provides a basic environment for editing, compiling, and executing scripts.

- __scripting addition__

  Code, stored in `/System/Library/SystemAdditions`, that makes additional commands or coercions available to scripts on the same computer.

- __scripting addition command__

  A command that is implemented as a scripting addition.

- __scripting definition file__

  A file in the scripting definition format that provides the scriptability information for an application. A scripting definition file has the extension `.sdef` and is also called an _sdef file_ or simply an _sdef_. Compare [script suite file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg44dq), [script terminology file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg44tc).

- __scripting definition format__

  An XML-based format that describes a set of scriptability terms and the commands, classes, constants, and other information used to support an application’s scriptability. Also called _sdef format_. Compare [script suite format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg44ds).

- __script object__

  A user-defined object, combining data (in the form of properties) and handlers, that can be used in a script.

- __script object definition__

  A compound statement that can contain collections of properties, handlers, and other AppleScript script statements.

- __script suite__

  The combination of at least one suite definition and one suite terminology that together define the scripting capabilities and terminology for Cocoa applications.

- __script suite file__

  A property list file, in a specific format, that describes scriptable classes in terms of their attributes, relationships, and supported commands and that has the extension `.scriptSuite`. Script suite files, together with corresponding script terminology files, declare the scriptability information for a scriptable application. See also [script terminology file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg44tc).

- __script suite format__

  A format for providing scriptability information in the form of property list files, consisting of a script suite file together with a corresponding script terminology file. Compare [scripting definition format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg44di).

- __script system__

  A collection of software utilities that provides for the representation of a specific writing system. It consists of a set of keyboard resources, a set of international resources, and one or more fonts. Script systems include Roman, Japanese, Arabic, traditional Chinese, Simplified Chinese, Hebrew, Greek, Thai, and Korean.

- __script terminology file__

  A property list file, in a specific format, that provides AppleScript terminology—the English-like words and phrases a scripter can use in a script—for the class and command descriptions in the corresponding script suite file. A script terminology file has the extension `.scriptTerminology`. Together with a corresponding script suite file, it declares the scriptability information for a scriptable application. See also [script suite file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg44dq).

- __scroll arrows__

  Small buttons that appear on the scroll control that let the user incrementally advance the scrollers without dragging.

- __scroll bar__

  A control for viewing areas of a document or a list that is larger than can fit in the current window. Only the active window can be scrolled. A window can have a horizontal scroll bar, a vertical scroll bar, both, or neither.

- __scroller__

  The part of a scroll bar that the user drags to view other parts of a document. The scroller size reflects how much of the document is visible; the smaller the scroller, the less of the content the user can see at that time. The scroller represents the relative location, in the whole document, of the portion that can be seen in the window.

- __scrolling list__

  A list in a dialog that uses scroll bars to reveal its contents.

- __scrolling menu__

  A menu that contains more items than are visible onscreen. Scrolling menus have triangles that indicate hidden menu items.

- __SCSI__

  Small Computer Systems Interface. A standard connector and communications protocol used for connecting devices such as disk drives to computers.

- __SCSI Architecture Model__

  A specification, approved as ANSI standard X3.270-1996, that defines a common interface standard between computers and devices such as disk drives, printers, and scanners.

- __sdef__

  See [scripting definition file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg44dg).

- __SDK__

  Software Development Kit. A complete set of header files and stub libraries as shipped in a particular version of OS X.

- __SDK family__

  Group of SDK releases used to build software products for a particular Apple platform. The available SDK families are iPhone Device SDK, iOS Simulator SDK, and OS X SDK.

- __search__

  In an information retrieval system, a process that attempts to locate documents that match a query, and that may assign relevance scores to the found documents. Upon a successful match, a search system returns references to the found documents. Search Kit supports a variety of search types, some of which can be combined. These types are simple, Boolean, ranked, unranked, phrase, similarity, prefix, suffix, and substring.

- __searchable Ink__

  In Ink Services, Ink that remains visible to the user, but for which recognition has taken place.

- __search field__

  A text field with rounded corners used for searching. It can include a menu and an icon to clear the field or steps of a search.

- __search mode__

  In Xcode, a mode that the Documentation window operates in. You can find documents by API symbol name, document title, or document content. Compare [browse mode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgizdq).

- __search object__

  In Search Kit, an opaque data type representing an asynchronous search and containing its results, accumulated as they are found. A search object is of type `SKSearchRef`.

- __search result__

  In Xcode, the set of documents that meet search criteria.

- __search strip__

  In Xcode, a user interface element that appears below the Documentation window toolbar during a search. It allows you to choose a type of search.

- __SECAM__

  Systeme Electronique Couleur avec Memoire. A color-encoding system in which the red and blue color-difference information is transmitted on alternate lines, requiring a one-line memory in order to decode green information. Translated into English as _Sequential Color with Memory_.

- __secret__

  The encrypted data in a keychain item, such as a password. Only a trusted application can read the secret of a keychain item. Compare [attribute](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tc).

- __secret key__

  A cryptographic key that cannot be made public without compromising the security of the cryptographic method. In _symmetric key cryptography_, the secret key is used both to encrypt and decrypt the data. In _asymmetric key cryptography_, the secret key is paired with a public key. Whichever one is used to encrypt the data, the other is used to decrypt it. See also [public key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4te), [public key cryptography](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4ti).

- __Secure Sockets Layer__

  See [SSL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhezdi).

- __secure storage__

  Encrypted storage of data that requires a user or process to authenticate itself before the data is decrypted. Secure storage persists when the power is turned off.

- __Secure Transport__

  The OS X and iOS implementation of [SSL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhezdi) (Secure Transport Layer) and [TLS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga4do), used to create secure connections over TCP/IP connections such as the Internet. On OS X, Secure Transport includes an API that is independent of the underlying transport protocol. The [CFNetwork](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4ta) and [URL Loading System](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge3to) APIs use the services of Secure Transport.

- __Security Agent__

  In OS X, a process used by the [Security Server](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayto) to communicate with the user through dialogs and other user interface elements.

- __Security Objective-C API__

  An OS X API providing a set of Objective-C methods that are wrappers for the Authentication Services functions plus a set of classes that display security-related UI elements.

- __Security Server__

  A daemon running in OS X and iOS that implements security protocols for such purposes as encryption, decryption, and authorization computation. The use of the Security Server to perform actions with cryptographic keys allows the keys to be maintained in a separate address space from the client application, keeping them more secure. In OS X, the Security Server uses a process called the _Security Agent_ to communicate with the user through dialogs and other user interface elements.

- __seek__

  To set an audio file or buffer’s read position to a specified [webpage template](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2tc).

- __segmented control__

  A control for changing modes or views; each segment represents a different state.

- __selection range__

  The contiguous sequence of characters in the source text that mark where the next editing operation is to occur. The glyphs corresponding to those characters are commonly highlighted onscreen.

- __self-restricted application__

  An application that restricts part of its features to specific users.

- __semaphore__

  A protected variable that restricts access to a shared resource. Semaphores are used to coordinate activities in which multiple processes compete for the same resources—for example, to share a common memory space or to share access to files. Mutexes and conditions are both types of semaphore. A semaphore is similar to a lock, except that a finite number of threads can be holding a semaphore at the same time. See also [lock](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge3tg).

- __send rights__

  In Mach, the ability to send messages to a Mach port. Many tasks can have send rights for the same port. Compare [receive rights](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyztq).

- __separator__

  A line used to break a window into visual regions.

- __sequence__

  In Core Audio, a collection of tracks to be played by a [music player](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi4te). A sequence always contains one or more event tracks and a tempo track. See also [event track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4yds).

- __sequencer__

  Software or hardware for recording, playback, and editing of MIDI data or audio samples (excerpts or loops). See also [SGML](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhazts), [MIDI](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgiztg).

- __serif__

  The fine lines stemming from and at an angle to the upper and lower ends of the main strokes of a letter—for example, the little “feet” on the bottom of the vertical strokes in the uppercase letter “M” in Times Roman typeface.

- __server__

  (1) A process that provides services to other processes (clients) in the same or other computers. In source control, a server is the process that modifies the repository. (2) A computer running OS X Server.

- __service__

  A service is an I/O Kit entity, based on a subclass of `IOService`, that has been published with the `registerService` method and provides certain capabilities to other I/O Kit objects. In the I/O Kit’s layered architecture, each layer is a client of the layer below it and a provider of services to the layer above it. A service type is identified by a matching dictionary that describes properties of the service. A nub or driver can provide services to other I/O Kit objects.

- __servlet__

  A Java program that runs as part of a network service, typically a web server and responds to requests from clients. Servlets extend a web server by generating content dynamically.

- __servlet container__

  A Java application that provides a working environment for servlets. It manages the servlet’s interaction with its client and provides the servlet access to various Java-based services. Containers can be implemented as standalone web servers, server plug-ins, and components that can be embedded in an application.

- __session__

  A period during which access to a WebObjects application and its resources is granted to a particular client (typically a browser). Also an object (of the `WOSession` class) representing a session.

- __session key__

  A cryptographic key calculated or issued for use only for the duration of a specific communication session. Session keys are used, for example, by the [Diffie-Hellman key exchange](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2tc) and [Kerberos](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga3ts) protocols.

- __setter__

  In refactoring code, the method to use to set the value of the transformation item.

- __setuid bit__

  The fourth bit in a resource’s permissions code. When this bit is set to `s` , the system allows the process running it to masquerade as another user. For example, `-r-sr-xr-x 1 root wheel traceroute` allows the process running the `traceroute` utility to run as root.

- __setuid tool__

  A tool that has its setuid bit set.

- __setup assistant__

  A small application that guides users through the setup options for a hardware device or software component.

- __SGID__

  Saved group ID. The [GID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhaztg) used by BSD to enable a privileged process to switch in and out of privileged mode.

- __SGML__

  Standard Generalized Markup Language. A language that allows the creation of sharable documents with a formal type and element structure.

- __shader__

  In image processing, a program that computes surface properties.

- __shading language__

  A high-level language, accessible in C, used to produce advanced imaging effects. The Apple implementation of OpenGL supports `ARB_shading_language_100` .

- __shadow__

  An image painted underneath, and offset from, a graphics object such that the shadow mimics the effect of a light source cast on the graphics object.

- __shadow object__

  In Mach VM, a memory object that holds modified pages that originally belonged to another memory object. It is used when an object that was duplicated in a copy-on-write fashion is modified. If a page is not found in this shadow object, the original object is referenced.

- __shared secret authentication__

  An authentication method based on a secret known to only the two parties involved. Verification of passwords is a commonly used shared secret authentication method.

- __shared workgroup build__

  In Xcode, a distributed build that works best with small to medium-sized projects that use up to ten build servers.

- __Shark__

  A tool for analyzing a running (or static) application. It returns metrics to help you identify potential performance bottlenecks.

- __sheet__

  A dialog attached to a specific window, ensuring that the user never loses track of which window the dialog belongs to. Sheets appear to slide out from underneath the window title and float above the window. A Print dialog is an example of a sheet. See also [document-modal dialog](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyyda).

- __shell__

  An interactive programming language interpreter that runs in a Terminal window. OS X includes several shells, each with a specialized syntax for executing commands and writing structured programs, called _shell scripts_.

- __Shift-click__

  To click while the Shift key is down. This combination is used to select multiple objects or to extend a selection.

- __Shift JIS__

  Shift Japanese Industrial Standard. A character encoding based on two JIS standards: JIS X 0201 and JIS X 0208. Shift JIS consists of codes from the JIS X 0208 standard that are shifted to make room for older Hankakukana codes from the JIS X 0201 standard.

- __sidebar__

  In the Finder, a user-specified list of disks, volumes, and other directories that allow users quick access to specific locations.

- __signal__

  A UNIX mechanism for manipulating a process from outside its domain. The system uses signals to deliver important messages to an application, such as whether the application executed an illegal instruction.

- __signal dispatch source__

  A [dispatch source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvjvomq) used to process UNIX signals. A signal source calls your custom event handler whenever the process receives a UNIX signal.

- __signal-to-noise ratio__

  See [SNR](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4de).

- __SIMD__

  Single Instruction, Multiple Data. A computing technique used to achieve data level parallelism. Commonly employed in vector processors, this technique allows for multiple data elements to be processed in a single CPU instruction.

- __similarity searching__

  The matching of a query string, typically consisting of a representative portion of a document, to indexed documents. A match occurs when Search Kit determines significant content similarity between the query and an indexed document. Search Kit supports similarity searching in vector and inverted-vector indexes. Similarity searching also works in inverted indexes in Search Kit, but performance is worse. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayde).

- __simple message__

  In Mach, a message that contains neither references to ports nor pointers to data. Compare [nonsimple message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmzdm).

- __simple search__

  The matching of the terms in a query string to indexed terms using exact, character-for-character matching. Each term is matched separately. In Search Kit, by default, spaces between terms behave like Boolean `AND` operators. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayde).

- __simple statement__

  In AppleScript, a statement that can be written on a single line. See also [compound statement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm4di).

- __simple value__

  A value, such as an integer or a constant, that does not contain other values.

-  __`simpleroutine`__

  In Mach, a remote procedure call that does not return a value and has no `out` or `inout` parameters. It can be used for asynchronous operations. See also [routine](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4ztg).

- __Simulator__

  See [iOS Simulator application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga2dc).

- __single caret__

  In unidirectional text, the standard text-insertion caret. In mixed-directional text, one caret that appears at the place where the user will insert the next character, given the current keyboard script. At a boundary between two direction runs, the single caret can correspond to either the primary line direction or the secondary line direction. Because changing the keyboard script in that situation changes the caret location, the single caret is also called a _moving caret_ or _jumping caret_.

- __single-fork movie file__

  A QuickTime movie file that stores both the movie data and the movie resource in the data fork of the movie file. You can use single-fork movie files to ease the exchange of QuickTime movie data between Macintosh computers and other computer systems.

- __single signon__

  A feature of a security system whereby users provide authentication credentials (such as user ID and password) only once, after which they can access additional services without reauthenticating. See also [authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3de), [ticket](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3di).

- __skip atom__

  An atom of type `'skip'`, which you can include in a QuickTime file as a placeholder for unused space.

- __slice__

  The number of frames requested and processed during one rendering cycle of an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq). See also [frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhaytc).

- __slider control__

  A control enabling users to choose among a continuous range of allowable values. Slider controls can be horizontal or vertical and can display incremental tick marks.

- __Small Computer System Interface__

  See [SCSI](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg44to).

- __small system font__

  The font used for informative text in alerts, headers in lists, help tags, and text in the small versions of many controls. It is 11-point Lucida Grande Regular.

- __smart card__

  A plastic card similar in size to a credit card that has memory and a microprocessor embedded in it. A smart card can store and process information, including passwords, certificates, and keys. A smart card normally requires a personal identification number (PIN) or biometric measurement (such as a fingerprint) before releasing information and can carry out its own authentication evaluation. Smart cards can exchange information with a personal computer through a smart card reader.

- __smart group__

  In Xcode, a group, either built-in or custom, that collect files that match a rule or pattern. You can customize the contents using wildcard patterns or regular expressions.

- __smart swash__

  A variation of an existing glyph (often ornamental) that is contextual. Compare [swash](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe3to).

- __SMB__

  Server Message Block. A file-sharing protocol used on Windows and UNIX systems. SMB can also be used to share printers and has calls to authenticate users. It runs over several different types of networks, including TCP/IP. For most purposes, SMB has been superseded by [CIFS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmyts). See also [Samba](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg42ds).

- __SMB/CIFS__

  See [CIFS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmyts), [SMB](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha3te).

- __S-MIME__

  Secure Multipurpose Internet Mail Extensions. A specification that adds [digital signature](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2to) authentication and encryption to electronic mail messages in [MIME](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgizts) format.

- __SMP__

  Symmetric multiprocessing. A feature of an operating system in which two or more processors are managed by one kernel, sharing the same memory and having equal access to I/O devices, and in which any task, including kernel tasks, can run on any processor.

- __SMPTE__

  Society of Motion Picture and Television Engineers. An organization that publishes standards related to film, television, and audio.

- __SMPTE timecode__

  A standard, time-based format for tagging film, video, and audio recordings to support [synchronization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4dg) and editing. The SMPTE timecode represents a given time in the format `hours:minutes:seconds:frames`.

- __SMTP__

  Simple Mail Transfer Protocol. A protocol used to transfer email between computers, usually over Ethernet.

- __snapshot__

  In Xcode, a view of the state of the files in project. Snapshots allow you to experiment freely with refactoring operations.

- __snapshot store__

  In Xcode, the set of snapshots taken from one or more projects with the same project root.

- __snapshotting__

  A part of the Enterprise Objects optimistic locking mechanism, in which snapshots of database rows in memory are compared with the data in the database.

- __SNR__

  Signal-to-noise ratio. The range, expressed in decibels, between a nominal signal [level](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge2de) and the [noise floor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmzdc). Compare [dynamic range](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgy2ta).

- __SOAP__

  XML-based, lightweight, platform-agnostic protocol used to exchange information in a decentralized, distributed environment. The protocol defines the XML elements that must be used to compose a message and how the data in a message should be processed. _SOAP_ was originally an acronym for _Simple Object Access Protocol_, but as of version 1.2 of the W3C specification, the term is no longer an acronym.

- __SOAP engine__

  Application or framework used by web service providers and consumers to process SOAP messages.

- __socket__

  (1) In BSD-derived systems, a socket refers to different entities in user and kernel operations. For a user process, a socket is a file descriptor that has been allocated using `socket(2)`. For the kernel, a socket is the data structure that is allocated when the kernel’s implementation of the `socket(2)` call is made. (2) In AppleTalk protocols, a socket serves the same purpose as a “port” in IP transport protocols.

- __socket filter__

  A filter that is associated with a particular socket or class of sockets, filtering [in-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe2ts) and [out-of-band](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm4de) operations on the socket. A socket filter resides between a socket and the protocol layer.

-  __`socket` structure__

  A data structure containing data associated with a network socket.

- __Software Development Kit__

  See [VM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizds).

- __sonogram__

  A three-dimensional visualization of a signal’s frequency content. Typically, a sonogram’s horizontal axis is time, its vertical axis is frequency, and the visual intensity (in terms of color or dot size) of each plotted point represents energy. Also called a [spectrogram](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrheyda).

- __sound field__

  In acoustics, the space in which a sound is produced, conveyed to a listener, and perceived. In audio reproduction, the virtual space from which a monaural sound can seem to emanate. See also [spatialization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4tq).

- __SoundField__

  A four-channel acoustic recording technique developed by the British company SoundField, Ltd.

- __source control__

  See [visual context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizdq).

- __source file__

  In Xcode, a file used to build a product. Source files include source code files, resource files, image files, and others.

- __source group__

  In Xcode, a group inside a project group in the source window that contains references to actual files somewhere on the hard disk.

- __source list__

  A list in a pane of an application window used to organize and navigate data. The width of the pane is adjustable. The Finder sidebar is an example of a source list.

- __source text__

  A stored sequence of character codes that represents a line of text. Characters in source text are stored in input order. Compare [display text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4di).

- __sparse SDK__

  An SDK that is not a system SDK. Sparse SDKs may be provided by third parties, or you can build them yourself.

- __spatialization__

  The manipulation of audio signals to create perceived localization of sounds within a sound field. Compare [panning](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqytq). See also [sound field](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4ta).

- __S/PDIF__

  Sony/Phillips Digital Interface. A consumer version of, and the inspiration for, the [AES-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga2ta) format. Part of the IEC-60958 standard. Devices such as CD players and DAT recorders use S/PDIF.

- __spectrogram__

  See [sonogram](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4ds).

- __speech attribute__

  A setting defined on a speech channel that affects the characteristics of the spoken output for a subset of voices or for all voices associated with a particular synthesizer.

- __speech channel__

  A structure through which an application communicates with a specific speech synthesizer and voice. An application may have more than one speech channel open at one time, but a speech channel may not be associated with more than one synthesizer and voice at one time.

- __speech pitch__

  The middle pitch of a voice, from which the actual pitches of the speech can vary with rising and falling tunes. Pitch is a combination of the average speaking frequency and its variations around that average.

- __speech rate__

  The approximate number of words of text that a speech synthesizer speaks in one minute.

- __speech recognition__

  The ability for a computer to understand spoken commands or responses.

- __speech synthesis__

  The ability for a computer to audibly communicate in the language of the user.

- __Speech Synthesis Manager__

  A C-based API that supports extensive control over speech synthesis.

- __speech synthesizer__

  A component that converts text into speech. A speech synthesizer usually contains executable code, built-in dictionaries, and pronunciation rules that help it determine how to pronounce text. Also called a _speech engine_.

- __speech volume__

  The average amplitude at which the speech channel generates speech.

- __spin/sleep lock__

  Any of a family of lock types characterized by some combination of the behaviors of spinlocks and mutex (sleep) locks.

- __spinlock__

  Any of a family of lock types characterized by continuously polling to see if a lock is available, rather than putting the waiting thread to sleep.

- __SPL__

  Sound pressure level. A measure of sound intensity. SPL is commonly expressed as a ratio in decibels relative to 0 dB SPL, or as an absolute level in Pascals (Pa). Although SPL is sometimes used to approximately indicate [loudness](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4di), the correlation of SPL to loudness is complex due to perceptual factors. See also [weighting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2tk).

-  __`spl` macro__

  Set priority level macro. A macro that sets the current IPL. Interrupts with lower priority than the current IPL are not be acted upon until the IPL is lowered. `spl` macros have no effect in many parts of OS X, so their use is discouraged as a means of synchronization in new programming except when modifying code that already uses `spl` macros. See also [IPL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga2de).

- __split caret__

  A type of caret that, at the boundary between text of opposite directions, divides into two parts, a high caret and a low caret, each measuring half the line’s height. The two separate half-carets merge into one in unidirectional text. Also called a _dual caret_. Compare [single caret](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha3dc).

- __splitter bar__

  A control for dividing a window into resizable sections.

- __split view__

  A view that groups together two or more subviews, such as list or column views. A split view includes one or more splitter bars to adjust the relative sizes of the subviews.

- __spool__

  To send files to a device or program (called a spooler or daemon) that puts them in a queue for later processing. The print spooler controls output of jobs to a printer. Other devices, such as plotters and input devices, can also have spoolers.

- __spool file__

  A temporary disk file used by an application to store data. It is generally used to save memory.

- __spring__

  In Interface Builder, an element in the size pane of the inspector window that controls the autosizing behavior of a view or control. When a spring is present, the width or height of your view grows and shrinks proportionally to its parent view. When no spring is present, the width or height of your view remains fixed.

- __sprite__

  An animated image that is managed by QuickTime. A sprite is defined once and is then animated by commands that change its position or appearance.

- __sprite track__

  A movie track populated by movie sprites.

- __SRC__

  Sample rate conversion. In digital audio, the process of converting PCM data from one sample rate to another.

- __SSE__

  Streaming SIMD Extensions. Intel’s SIMD instruction set.

- __SSL__

  Secure Sockets Layer. A protocol that provides secure communication over a TCP/IP connection. It uses [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2tg)s for [authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3de) and [digital signature](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2to)s to ensure message integrity, and can use [public key cryptography](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4ti) to ensure data privacy. An SSL service negotiates a secure session between two communicating endpoints. SSL is built into all major browsers and web servers. SSL has been superseded by [TLS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga4do) (Transport Layer Security).

- __stack frame__

  In Xcode, information the debugger stores about each function call that your program makes.

- __Standard Apple Plug-ins__

  Plug-ins for standard Apple applications, such as Interface Builder, Address Book, and Quartz Composer, and preference panes.

- __standard event handler__

  In Carbon applications, the event handler that processes an event if the application did not install one for it.

- __Standard Roman character set__

  The 256 characters and character codes that are supplied with the Macintosh Roman script system. The Standard Roman character set consists of the Macintosh character set plus additional defined characters with character codes between $D9 and $FF.

- __standard state__

  A new window’s initial size and position (determined by the application). See also [user state](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4ds), [zoom button](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi4ti).

- __Standard suite__

  The scriptability information for a set of standard AppleScript terms that scriptable applications should support if possible. The Standard suite contains commands such as `count`, `delete`, `duplicate`, and `make`, and classes such as `application`, `document`, and `window`. Cocoa scripting provides a great deal of automatic support for the Standard suite.

- __standard toolbox dispatcher__

  In the Carbon Event Manager, the default event target for events when running under `RunApplicationEventLoop` . Events sent to the standard toolbox dispatcher are automatically routed to the appropriate event targets.

- __statement__

  A series of lexical elements that follows a particular AppleScript syntax. Statements can include keywords, variables, operators, constants, expressions, and so on. See also [compound statement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgm4di), [simple statement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2to).

- __statement block__

  In AppleScript, one or more statements enclosed in a compound statement and having an `end` statement.

- __static library__

  A library for which all referenced symbols are bound at link time.

- __static text field__

  Text in a dialog that users can’t modify.

- __status bar__

  In Xcode, an area at the bottom of the project window that displays messages generated when building or running the project.

- __stem__

  The root of a family of morphological or inflectional variants of a word. For example, “swim” is the stem of “swimmer,” “swimming,” and “swam.”

- __stemming__

  The algorithm-based removal of morphological and inflectional word components, typically endings. Language dependent. Stemming is sometimes referred to as _suffix stripping_, although some stemming algorithms perform prefix stripping as well. Information retrieval systems use stemming to improve search quality and to reduce index size. Search Kit does not support stemming; if needed, client applications implement it. Some stemming algorithms handle only regular variants, such as converting “swimming” to “swim,” and do not handle irregular variants, such as converting “swam” to “swim.”

- __stencil buffer__

  In image processing, memory used specifically for stencil testing. A stencil test is typically used to identify masking regions, identify solid geometry that needs to be capped, and to overlap translucent polygons.

- __stepper control__

  A control for incrementing or decrementing a value. The control has an upward and a downward pointing arrow.

- __stopword__

  A word not to add to a search index. When Search Kit adds terms from a document to an index, it skips over words in its stopword list.

- __storage order__

  The order in which character codes are stored in memory. Storage order may be different from display order.

- __stream__

  (1) (n.) A continuous flow of data (especially audio or video) over a [transmission channel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgezdm) that can be interpreted as it is received, often for playback in real time. In audio, the packet boundaries used for encoding in a particular audio format may not coincide with transmission packet boundaries. (2) (v.) To send data as a stream. See also [audio file stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2te), [parser](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqzdq), [TCP stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgaytm).

- __strength__

  A measure of the amount of effort required to break a security system. For example, the strength of [RSA encryption](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4ztm) is believed to be related to the difficulty of factoring the product of two large prime numbers.

- __string__

  In AppleScript, a synonym for the `text` class.

- __string atom__

  An atom in VR media that contains text.

- __strip style__

  In Xcode, specifies the level of stripping performed when dead-code stripping is enabled. There are three levels of stripping available: all symbols, nonglobal symbols, debugging symbols.

- __stroke__

  (1) A drawing operation that follows a path. (2) In Ink Services, an array of points that define the path of the stylus, starting with a stylus-down event and ending when the stylus is lifted.

- __structure region__

  The entire area taken up by a window onscreen.

- __strut__

  In Interface Builder, an element in the size pane of the inspector window that controls the autosizing behavior of a view or control. When a strut is present, the distance between the edge of a view and its parent view remains fixed. When absent, the distance grows and shrinks as the size of the views change.

- __stub library__

  A library used for linking purposes. Stub libraries contain exported symbols only; they do not contain executable code.

- __style__

  A visual attribute, other than size, applied as a systematic variation to the plain (unstyled) characteristics of a font glyph—for example bold, italic, underline, outline, shadow, condense, and extend.

- __style attributes__

  A collection of values and settings that override the font-specified behavior for displaying and formatting text in a style run.

- __styled text__

  Text that may include style and font information. Not supported in AppleScript 2.0.

- __style object__

  An opaque object that contains a collection of stylistic attributes. Style objects can be applied to runs within a text layout object.

- __style run__

  A sequence of text that is contiguous in memory and in which all the characters are in the same style. Compare [text run](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2dm).

- __stylus__

  A hand-held instrument used to enter data into the computer. Also referred to as a [pen](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2dm).

- __subframework__

  A public framework that packages a specific Apple technology and is part of an umbrella framework. Through various mechanisms, Apple prevents or discourages developers from including or directly linking with subframeworks. See also [umbrella framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2ta).

- __submap__

  A collection of mappings in the VM system that is shared among multiple Mach tasks.

- __submenu__

  A menu that descends from another menu. The title of the submenu is a menu item in the parent menu. See also [hierarchical menu](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqha4dm).

- __subpatch__

  In Quartz Composer, a patch that is contained in a macro.

- __subpicture__

  A graphic bitmap overlay used in DVD-Video to create subtitles, captions, karaoke lyrics, menu highlighting effects, and so on.

- __substring searching__

  Matching of a term in a query string to indexed terms, with explicit wildcard characters at the start and end of the query term. A match occurs when the characters in the query term (minus the wildcard characters) match the beginning, ending, or middle of an indexed term. For example, the query string `*cat*` will match `cat`, `concatenate`, `tomcat`, and `cattle`. Search Kit supports substring searching in inverted and inverted-vector indexes. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayde).

- __suffix searching__

  A specialized type of substring search. A suffix search involves matching of a term in a query string to indexed terms, with an explicit wildcard character at the start of the query term. A match occurs when the characters in the query term (minus the wildcard character) match the ending of an indexed term. For example, the query string `*ion` will match `ion`, `lion`, and `version`. Search Kit supports suffix searching in inverted and inverted-vector indexes. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayde), [wildcard character](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2tq).

- __suffix stripping__

  See [stemming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrheztq).

- __SUID__

  Saved user ID. The ID used by BSD to enable a privileged process to switch in and out of privileged mode.

- __suite__

  Within an application’s scriptability information, a grouping of terms associated with related operations. For example, operations involving text, graphics, or databases are generally collected into separate text, graphics, and database suites.

- __suite definition__

  A property list that describes scriptable objects in terms of their attributes, relationships, and supported commands

- __suite terminology__

  A property list that maps AppleScript terminology—the English-like words and phrases you can use in a script—to the class and command descriptions in a suite definition.

- __summarization object__

  In Search Kit, an opaque data type representing summarization information, including the summary text. A summarization object is of type `SKSummaryRef`.

- __Summary pane__

  A pane in the Page Setup and Print dialogs that provides a textual list of the currently selected options for that dialog.

- __superuser__

  See [root user](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4zds).

- __supervisor mode__

  The processor mode in which certain privileged instructions can be executed, including those related to page table management, cache management, clock setting, and so on. Also known as _kernel mode_.

- __surface__

  The internal representation of a single buffer that OpenGL actually draws to and reads from. For windowed drawable objects, this surface is what the OS X window server uses to composite OpenGL content on the desktop.

- __surrogates__

  Values that allow additional characters to be mapped to the Unicode 16-bit character set.

- __surround sound__

  A loudspeaker configuration with more than two loudspeakers, intended to provide an [immersive audio](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe2te) experience. See also [5.1 Surround Sound](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgayde).

- __swash__

  A variation of an existing glyph (often ornamental) that is noncontextual. Compare [smart swash](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha3tc).

- __SWF file__

  A file that contains Flash data. See [Flash](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg43ts).

- __symbolic link__

  A lightweight reference to files and folders in UFS file systems. A symbolic link allows multiple references to files and folders without requiring multiple copies of these items. Symbolic links are fragile because if what they refer to moves somewhere else in the file system, the link breaks. However, they are useful in cases where the location of the referenced file or folder will not change. See also [alias](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga3di).

- __symmetric keys__

  A pair of identical keys used to encrypt and decrypt data. See also [private key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu2di). Compare [asymmetric keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgeztm).

- __symmetric multiprocessing__

  See [SMP](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha3tk).

- __sync__

  Short for _synchronization_. (1) The process of ensuring that the clocks of two or more systems remain locked together, counting at the same rate. This term is commonly used in the context of locking an audio track to a video track. See also [clock](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmztm), [clock drift](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmzto), [SMPTE timecode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha3to). (2) In a printing dialog extension, a procedure that maintains the correspondence between the current user interface settings and their recorded values in a job ticket. (3) In Sync Services, the process of establishing and maintaining data consistency between multiple clients.

- __synchronization__

  See [keyboard and font synchronization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4tk).

- __synchronous__

  In Audio Queue Services, describes one of two ways to stop an audio queue. Synchronous stopping happens immediately, without regard for previously buffered audio data. In digital communications, a transmission method that requires the clock frequency of the sender and receiver to be the same. Compare [asynchronous](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgezto).

- __synchronous launch__

  A [launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgezdk) operation in which control does not return to the calling program until the launched application has completed its launch sequence. Compare [asynchronous launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgeztq).

- __sync sample__

  A sample that does not rely on preceding frames for content. See also [key frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgeydk).

- __synonym__

  (1) A term that an information retrieval system considers to be equivalent to another term for both indexing and querying. For example, an IR system could define “car,” “passenger vehicle,” and “automobile” to be synonyms. See also [index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe3de), [information retrieval](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe3dq), [query](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyytg). (2) An AppleScript word, phrase, or language element that has the same meaning as another AppleScript word, phrase, or language element. For example, the operator `does not equal` is a synonym for `≠`.

- __syntax__

  The arrangement of words in an AppleScript statement.

- __syntax-aware indenting__

  In Xcode, a feature of the text editor that gives you a number of ways to control code layout. When you use syntax-aware indenting, the editor automatically indents your code as you type.

- __syntax description__

  The rules for constructing a valid AppleScript statement of a particular type.

- __syntax formatting__

  In Xcode, formatting that uses different fonts and colors to identify particular elements in a source code file, such as keywords and comments.

- __system direction__

  The horizontal placement of interface elements, including the default line direction (left-to-right or right-to-left) for text in the system script. System direction is specified by the global system direction variable.

- __Systeme Electronique Couleur avec Memoire__

  See [SECAM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayds).

- __system font__

  The font used for text in menus and in modeless dialogs, and for titles of document windows. It is 13-point Lucida Grande Regular.

- __system framework__

  A framework developed by Apple and installed in the file-system location for system software.

- __system keychain__

  A keychain that belongs to the system as a whole, rather than to a particular user. System keychains are usually used by system daemons and services, but can also be accessed by applications on behalf of users. One system keychain, named `System.keychain`, is created by the system and added by default to every user’s keychain list.

- __system modal__

  A window state in which the user cannot do anything else until the window is dismissed. You should avoid using the system-modal state if at all possible. Compare [application-modal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgeytq), [document-modal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu4ts).

- __system object__

  An object that is part of a scriptable element of OS X.

- __system output__

  In OS X, the hardware destination for all system sounds.

- __system output unit__

  An Apple-supplied [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) that connects with whichever hardware device the user has designated to be the [system output](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe4ts).

- __system requirement__

  A condition that must be met by the computer (and associated operating system) in order for an installation to proceed.

- __system-restricted application__

  An application that has a portion of its features restricted to specific users because of the BSD permissions system.

- __system script__

  The primary script system used by the operating system, such as in dialogs and menu bars. The system script affects system defaults, such as the system font, line direction, and text-formatting rules. All other scripts are secondary to the system script.

- __system sleep__

  A sleep state that occurs when the user chooses Sleep from the Apple menu or closes the lid of a laptop computer. See also [idle sleep](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhezdi)

- __tab view__

  A control that provides a convenient way to present information in a multipane format.

- __table__

  In relational databases, a two-dimensional set of values corresponding to an entity. The columns of a table represent characteristics of the entity and the rows represent instances of the entity.

- __tail time__

  The time, beyond an audio unit’s latency, for a nominal-level signal to decay to silence at an audio unit’’sutput after it has gone instantaneously to silence at the input. Tail time is significant for audio units performing an effect such as delay or reverberation. An [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) declares its tail time as a [setup assistant](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhazto).

- __target__

  (1) In Xcode, the instructions for building a finished product from a set of files in a project—for example, a framework, library, application, or command-line tool. Each target builds a single product. (2) In AppleScript, the recipient of a command. Potential targets include `application` objects, `script` objects (including the current script), and the current application.

- __target dependency__

  A relationship among Xcode targets that specifies the order in which they should be built.

- __targeted gesture__

  In Ink Services, a gesture that has a defined hot spot that an application can use to determine the area to which the gesture should apply.

- __Target Info window__

  A window in which you can view and modify target settings.

- __target OS version__

  The earliest version of OS X in which the installation package is to be installed. The package is installable on the specified version and later. For example, a package whose target is OS X v10.4 can be installed on computers running OS X v10.4 and later versions.

- __target template__

  An Xcode template that specifies the target product type, a list of default build phases, and default definitions for some build settings. A target template typically includes all build settings and build phases required to build an instance of the specified product.

- __task__

  (1) A quantity of work to be performed. (2) A Mach abstraction consisting of a virtual address space and a port name space. A task itself performs no computation; rather, it is the context in which threads run. See also [process](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu2dq), [thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2tq).

- __task port__

  A kernel port that represents a task and is used to manipulate that task. See also [kernel port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4dq), [thread port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2ts).

- __TCP/IP__

  Transmission Control Protocol/Internet Protocol. An industry-standard protocol used to deliver messages between computers over the network. TCP/IP support is included in OS X.

- __TCP stream__

  Transmission Control Protocol stream. A data stream used for audio delivery over networks. TCP is part of the IP (Internet Protocol) suite. It provides reliability and in-order delivery of packets..

- __TDM__

  Time division multiplexing. A method of combining multiple digital signals in a single data stream by [sound field](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha4ta) samples of each signal in time. For example, to carry a stereo signal on a single stream, the stream contains alternating samples of the left and right channels: L R L R L R.

- __tearing__

  In image processing, a visual anomaly caused when part of the current frame overwrites previous frame data in the framebuffer before the current frame is fully rendered on the screen.

- __tell statement__

  In AppleScript, a control statement that specifies the default target for the statements it contains.

- __template__

  (1) A pattern or model designed to guide development in accordance with a specific predefined format or structure. (2) In Xcode, a structured set of default resources (files, folders, frameworks, and so forth) necessary for a specific type of programming project. (2) In Quartz Composer, a composition file that contains a basic set of patches for a particular purpose. (3) In a WebObjects component, a file containing HTML that specifies the overall appearance of a Web page generated from the component.

- __tempo__

  The general speed of a piece of music, often described in beats per minute (BPM).

- __temporal compression__

  In QuickTime, image compression that is performed between frames in a sequence. This compression technique takes advantage of redundancy between adjacent frames in a sequence to reduce the amount of data that is required to accurately represent each frame in the sequence. Sequences that have been temporally compressed typically contain key frames at regular intervals.

- __tempo track__

  A special track used to synchronize all the other tracks in a [sequence](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhazdk). See also [event track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4yds).

- __tentative gesture__

  In Ink Services, Ink that the system treats tentatively as a gesture until your application either confirms the Ink is indeed a gesture or informs the system the Ink is not a gesture. The Join gesture is the only tentative gesture.

- __term__

  An atomic entry in a Search Kit index, typically corresponding to a word found in one of the index’s documents.

- __termination mode__

  In Ink Services, the conditions that define the end of an Ink phrase.

- __terminology browser__

  A graphical tool for displaying the scripting terminology for a scriptable application. Also known as a _dictionary browser_.

- __tessellation__

  An operation that reduces a surface to a mesh of polygons or a curve to a sequence of lines.

- __test__

  In AppleScript, a Boolean expression that specifies the conditions of a filter or an `if` statement.

- __test provisioning profile__

  A provisioning profile issued to users not on an iOS application developer team. It allows them to install and test applications that have not been published to the App Store.

- __texel__

  In image processing, a texture element used to specify the color to apply to a fragment.

- __text__

  A set of specific symbols that, when displayed in a meaningful order, conveys information.

- __text area__

  The space on a display device within which the text should fit.

- __text direction__

  The direction in which reading proceeds. Roman text has a left-to-right direction; Hebrew and Arabic have a (predominantly) right-to-left direction; Chinese and Japanese can have a vertical direction.

- __text editor__

  In Xcode, a view that displays a file for editing. The editor can be a pane in a window or a standalone window.

- __text encoding__

  The coded character set or character encoding scheme used to represent a particular piece of text.

- __Text Encoding Conversion (TEC) Manager__

  A pair of shared library extensions—namely, the Text Encoding Converter and the Unicode Utilities—that facilitate text encoding conversion on Mac OS–based computers.

- __Text Encoding Converter__

  A shared library extension that provides the services for general and algorithmic encoding conversions or multi-encoding streams. The Text Encoding Converter sometimes uses Unicode Utilities.

- __text extraction__

  In information retrieval systems, the selective copying of terms from one or more documents into an index. See also [stemming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrheztq), [stopword](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe2dc).

- __text face__

  An algorithmic way for your application to produce typestyles.

- __text input field__

  A rectangular area in which the user enters text or modifies existing text. Also called an _editable text field_, it supports keyboard focus and password entry.

- __text layout object__

  An opaque object that contains information to control the display and formatting of the text to which the object is associated.

- __text macro__

  In Xcode, a menu item or keystroke that lets you insert common constructs and blocks of code.

- __text manipulation__

  System-level procedures used to order and compare characters, determine line breaks, determine text directionality, and keep track of character properties, such as case.

- __text object__

  An opaque structure that the Multilingual Text Engine uses to handle text formatting at a document level.

- __text run__

  A sequence of text that is contiguous in memory and in which all characters are in the same font. Compare [run](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg42dc).

- __text segment__

  For text layout, the portion of a style run that falls on a single text line. (It may be the entire style run.) Most text measuring and drawing routines work on a single text segment at a time.

- __Text Services Manager (TSM)__

  The Mac OS technology that provides text services such as input methods. TSM handles communication between client applications that request text services and the software modules, known as text service components, that provide them.

- __text style__

  A visual attribute, other than size, applied as a systematic variation to the plain (unstyled) characteristics of a font’s glyphs. Some typical text styles include plain, bold, italic, underline, outline, shadow, condensed, and extended.

- __text to speech (TTS)__

  The ability of the computer to convert text into spoken words.

- __texture__

  In OpenGL, image data used to modify the color of rasterized fragments; can be one-, two-, three- dimensional or a cube map. See also [OpenGL texture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm3di).

- __texture cache__

  A pool of OpenGL textures.

- __texture mapping__

  In OpenGL, the process of applying a texture to a primitive.

- __texture matrix__

  A 4 x 4 matrix that OpenGL uses to transform texture coordinates to the coordinates that are used for interpolation and texture lookup.

- __texture object__

  In OpenGL, an opaque data structure used to store all data related to a texture. A texture object can include such things as an image, a mipmap, and texture parameters (width, height, internal format, resolution, wrapping modes, and so forth).

- __text width__

  The area between the margins; it is the length available for displaying a line of text.

- __TGT__

  Ticket-granting ticket. In Kerberos, a credential presented to the [ticket-granting server](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3dk) in order to obtain a [ticket](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3di). The ticket can then be used to gain access to a secure server. The use of TGTs and tickets enable the single signon feature, whereby the user need authenticate only once, after which they can access additional services without reauthenticating (by reentering their password, for example). See also [authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3de), [identification](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqheyts).

- __thread__

  A flow of execution in a process. Each thread has its own stack space but otherwise shares memory with other threads in the same process. A thread consists of a program counter, a set of registers, and a stack pointer. See also [task](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgayti).

- __thread port__

  A kernel port that represents a thread and is used to manipulate that thread. See also [kernel port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4dq), [task port](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgmyda).

- __thread-safe code__

  Code that can be executed safely by multiple threads simultaneously.

- __threshold__

  A preset signal level at which some sort of processing is activated. For example, a compressor [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) can allow you to specify the threshold above which compression begins.

- __thumbnail picture__

  In QuickTime, a picture that can be created from an existing image that is stored as a pixel map, a picture, or a picture file. A thumbnail picture is useful for creating small representative images of a source image and in previews for files that contain image data.

- __tick__

  1/60 second.

- __ticket__

  (1) In printing, an opaque data structure used by the system, printer modules, and printing dialog extensions to communicate information about a print job. Tickets are usually named for the type of information they contain, such as page format ticket and paper info ticket. (2) In security, a credential that a user can use to prove their identity. See also [authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3de), [identification](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqheyts), [Kerberos ticket](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4da).

- __ticket-granting server__

  In [Kerberos](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga3ts), the server that issues a [ticket](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3di) when presented with a [TGT](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2to) (ticket-granting ticket). See also [KDC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga3tm).

- __ticket-granting ticket__

  See [TGT](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2to).

- __tiling__

  In Quartz, the process of rendering pattern cells to a portion of a page. Quartz has three tiling options—no distortion, constant spacing with minimal distortion, and constant spacing.

- __timbre__

  The perceived quality of a sound as distinct from pitch, volume, envelope, and duration. For example, a tuning fork can be described as having a “gentle” timbre, while a strongly hit crash cymbal can be described as having a “harsh” timbre.

- __time base__

  A set of values that define the time basis for an entity, such as a QuickTime movie. A time base consists of a time coordinate system (that is, a time scale and a duration) along with a rate value. The rate value specifies the speed with which time passes for the time base.

- __time-based authentication__

  A form of [shared secret authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha2di) in which the secret is changed periodically in a way known only to the two parties involved.

- __time-based data__

  Data that changes or interacts with the user along a time dimension. QuickTime is designed to handle time-based data.

- __timecode__

  A standardized indexing system for identifying specific portions of a audio file. Timecodes are often used for synchronizing or editing audio data. See also [SMPTE timecode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrha3to).

- __timecode media__

  A media structure of type `'tmcd'` that is used to store timecode data.

- __timecode track__

  A movie track that stores external timing information, such as SMPTE timecodes.

- __time coordinate system__

  A set of values that defines the context for a time base. A time coordinate system consists of a time scale and a duration. Together, these values define the coordinate system in which a time value or a time base has meaning.

- __timeline__

  A visual representation of an audio signal over time.

- __timer__

  A kernel resource that triggers an event at a specified interval. The event can occur only once or can be recurring. Timers are one of the input sources for run loops. Timers are also implemented at higher levels of the system, such as NSTimer in Cocoa.

- __timer source__

  A source of synchronous events for a thread. Timers generate one-shot or repeated events at a scheduled future time.

- __time scale__

  The number of time units that pass per second in a time coordinate system. A time coordinate system that measures time in sixtieths of a second, for example, has a time scale of 60.

- __time-sharing policy__

  In Mach, a scheduling policy in which a thread’s priority is raised and lowered to balance its resource consumption against other timesharing threads.

- __time unit__

  The basic unit of measure for time in a time coordinate system. The value of the time unit for a time coordinate system is represented by the formula (1/time scale) seconds. A time coordinate system that has a time scale of 60 measures time in terms of sixtieths of a second.

- __time value__

  A value that specifies a number of time units in a time coordinate system. A time value may contain information about a point in time or about a duration.

- __title__

  The largest unit of a DVD-Video disc (other than the entire volume or side). Usually a movie, TV program, music album, or the like. A disc can hold up to 99 titles, which can be selected from the disc menu.

- __title bar__

  The bar at the top of the window that displays its name. The title bar can also contain controls and a proxy icon.

- __title search__

  In Xcode, a search type that finds the documents whose titles start with, contain, or match the search term.

- __TLD__

  Tag library descriptor. An XML document that describes a tag library. A JSP (JavaServer Pages) container uses the information contained in the TLD file to validate a JSP page’s tags.

- __TLS__

  Transport Layer Security. A protocol that provides secure communication over a TCP/IP connection such as the Internet. It uses [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2tg)s for [authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3de) and [digital signature](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2to)s to ensure message integrity, and can use [public key cryptography](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4ti) to ensure data privacy. A TLS service negotiates a secure session between two communicating endpoints. TLS is built into recent versions of all major browsers and web servers. TLS is the successor to [SSL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhezdi). Although the TLS and SSL protocols are not interoperable, [Secure Transport](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhayti) can back down to SSL 3.0 if a TLS session cannot be negotiated.

- __toggled menu item__

  A menu item or a set of two menu items that change between two states (for example, Turn Grid On and Turn Grid Off).

- __token__

  (1) In code completion, a string that does not contain spaces. (2) For documentation sets, the element used to associate a symbol with its reference documentation. The element includes a unique identifier representing the symbol, the location of the reference documentation for that symbol, summary information about that symbol, and information about related documentation and symbols.

- __token field__

  A control that creates a token out of a user’s text input.

- __token identifier__

  In Xcode, the unique identifier for a symbol described in a tokens file.

- __tokens file__

  In Xcode, a file that associates symbol names with locations in documentation. A tokens file is used to create the symbol index for a documentation set, which support fasts API lookup.

- __to-many relationship__

  (1) In relational databases, a relationship in which each source record has zero to many corresponding destination records. For example, a department has many employees. (2) In key-value coding, a property whose value is a collection of related objects. In an AppleScript scripting definition file, it is represented by an `element` element.

- __tool palette__

  A collection of buttons and other controls in a panel.

- __toolbar__

  A collection of buttons at the top of a window just below the title bar. A toolbar can be hidden or revealed with a toolbar button in the title bar.

- __toolbar button__

  A clear oblong button at the right end of a window’s title bar that shows and hides the toolbar (if one exists).

- __toolbox dispatcher__

  _See_ [standard toolbox dispatcher](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrheztc).

- __toolbox object class__

  A collection of event handlers and data that defines a custom object such as a control or window.

- __to-one relationship__

  (1) In relational databases, a relationship in which each source record has exactly one corresponding destination record. For example, each employee has one job title. (2) In key-value coding, a property whose value has properties of its own. In an AppleScript scripting definition file, it is represented by a `property` element.

- __topic__

  One of the message distribution center types for J2EE-based applications. Message senders send messages only to topics instead of specific applications, while only the applications interested in receiving messages sent to a particular topic subscribe to the topic and, therefore, receive the messages sent to it. A topic can have one or more subscribers. Any message sent to the topic is broadcasted to all the topic’s subscribers.

- __top-level specifier__

  In a nested object specifier, an object that has no container specifier. It represents the outermost container in the containment hierarchy. In most cases, the application object is the top-level specifier.

- __top-side bearing__

  The white space between the top of the glyph and the visible beginning of the glyph.

- __TosLink__

  An optical cable standard used to transmit digital audio signals. Short for _ToshibaLink_.

- __track__

  A Movie Toolbox data structure that represents a single data stream in a QuickTime movie. A movie may contain one or more tracks. Each track is independent of other tracks in the movie and represents its own data stream. Each track has a corresponding media structure, which describes the data for the track. See also [channel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4tq), [event track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4yds).

- __track boundary region__

  In QuickTime, a region that describes the area occupied by a track in the track’s coordinate system. QuickTime obtains this region by applying the track clipping region and the track matte to the visual image contained in the track rectangle.

- __track clipping region__

  In QuickTime, the clipping region of a track in the track’s coordinate system. QuickTime applies the track’’slipping region and the track matte to the image contained in the track rectangle to obtain the track boundary region. Only that portion of the track that lies in the track boundary region is then transformed into an image in the movie coordinate system.

- __track header atom__

  A QT atom that specifies the characteristics of a track in a QuickTime movie.

- __track height__

  The height, in pixels, of the track rectangle in a QuickTime movie.

- __tracking__

  Kerning between all glyphs in a line of text, not just the kerning pairs already defined by the font. You can increase or decrease interglyph spacing by adjusting the tracking setting. See also [tracking setting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgeyta). Compare [kerning](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4ta).

- __tracking setting__

  A value that specifies the relative tightness or looseness of interglyph spacing.

- __track input map__

  A structure of QT atoms that specifies how secondary data for a track is to be interpreted (clipping, blending, and so forth).

- __track load settings__

  In QuickTime, information that specifies how and when a track is to be preloaded before running in a movie.

- __track matte__

  In QuickTime, a pixel map that defines the blending of track visual data. The value of each pixel in the pixel map governs the relative intensity of the track data for the corresponding pixel in the result image. QuickTime applies the track matte, along with the track clipping region, to the image contained in the track rectangle to obtain the track boundary region. See [track boundary region](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgeydk), [track matte](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgeytg), [track rectangle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgeytm).

- __track movie boundary region__

  In QuickTime, a region that describes the area occupied by a track in the movie coordinate system, before the movie has been clipped by the movie clipping region. The movie boundary region is built up from the track movie boundary regions for each of the movie’s tracks.

- __track offset__

  In QuickTime, the blank space that represents the intervening time between the beginning of a movie and the beginning of a track’s data. In an audio track, the blank space translates to silence; in a video track, the blank space generates no visual image. All of the tracks in a movie use the movie’s time coordinate system. That is, the movie’s time scale defines the basic time unit for each of the movie’s tracks. Each track begins at the beginning of the movie, but the track’s data might not begin until some time value other than 0.

- __track rectangle__

  A rectangle that completely encloses the visual representation of a track in a QuickTime movie. The width of this rectangle in pixels is referred to as the track width; the height, as the track height.

- __track reference__

  In QuickTime, a data structure that defines the relation between movie tracks, such as the relation between a timecode track and other tracks. See also [timecode track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga3ti).

- __track width__

  The width, in pixels, of the track rectangle in a QuickTime movie.

- __trailing edge__

  The edge of a glyph that is encountered last when reading text of that glyph’s language. For glyphs of left-to-right text, the trailing edge is the right edge; for glyphs of right-to-left text, the trailing edge is the left edge.

- __trailing frames__

  In audio data format conversion, frames of audio data that follow, in time, the nominal ending frame for an input [stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe2dg). See also [priming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrguzdi). Compare [leading frames](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgezts).

- __transaction__

  A set of actions that is treated as a single operation that either succeeds completely (commit) or fails completely (rollback).

- __transformation__

  (1) An alteration to a coordinate system that defines a new coordinate system. Standard transformations include rotation, scaling, and translation. A transformation is represented by a matrix. (2) A refactoring operation that modifies source code.

- __transformation matrix__

  A 3-by-3 matrix that defines how to map points from one coordinate space into another coordinate space.

- __transition animation__

  An animation that uses a Core Image filter to apply a visual effect to an animation object being displayed or hidden.

- __translation__

  An operation that moves the origin of the coordinate space by the number of units specified for the x and y axes.

- __transmission channel__

  A hardware or software conduit for the conveyance of a data [stream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe2dg) or an analog signal.

- __transparency layer__

  A composite of two or more objects that Quartz treats as a single object when applying effects, such as shadows.

- __transparent authentication__

  Authentication without intervention by the user. After unlocking the keychain, the user does not have to log in separately to any services whose passwords are stored in the keychain.

- __Transport Layer Security__

  See [TLS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga4do).

- __trim frames__

  Frames added to the beginning or end of a [nub](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgmzti) to pad the audio data. Trim frames added before the audio data are typically used to prime an audio decompressor. See also [webpage template](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2tc), [priming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrguzdi), [priming frame](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrguzdk).

- __triple__

  Three values that consist of an attribute tag, a value for that tag, and the size of the value. In ATSUI, triples are used to specify style, line, and layout attributes.

- __trust__

  See [level of trust](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge2dk).

- __trust policy__

  A set of rules that specifies the appropriate uses for a certificate that has a specific [level of trust](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge2dk). For example, the trust policy for a browser might state that if a certificate has an SSL [certificate extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4de), but the certificate has expired, the user should be prompted for permission before a secure session is opened with a web server.

- __trusted application__

  An application that can read a keychain item’s secret when the keychain is unlocked. See also [Unicode Utilities](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge2tk).

- __try statement__

  In AppleScript, a two-part compound statement that contains a series of AppleScript statements, followed by an error handler to be invoked if any of those statements cause an error.

- __tween data__

  In QuickTime, the data in a tween track, such as interpolation values.

- __tweening__

  A process of interpolating new data between given values in conformance to an algorithm. It is an efficient way to expand or smooth a QuickTime movie’s presentation between its actual frames.

- __tween track__

  In QuickTime, a modifier track that performs a specific kind of tweening, such as path-to-matrix rotation.

- __twos-complement encoding__

  A system for digitally encoding sound that stores the amplitude values as a signed number—silence is represented by a sample with a value of 0. For example, with 8-bit sound samples, twos-complement values would range from –128 to 127, with 0 meaning silence. The Audio Interchange File Format (AIFF) stores samples in twos-complement form. Compare [offset-binary encoding](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm2tc).

- __type-ahead__

  The queuing of keystrokes for processing later. It occurs when the user types faster than the computer can handle or when the computer is unable to process the keystrokes.

- __type-definition dictionary__

  A dictionary, specified in an application’s [bundle information property list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi2tg), that declares a particular [document type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyydg) that the application claims to handle. Compare [scheme-definition dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg43ta).

- __typestyle__

  See [text style](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga2ds).

- __typographic bounding rectangle__

  The smallest rectangle that encloses the full span of the glyphs from the ascent line to the descent line. See also [image bounding rectangle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqheztq).

- __typographic point__

  A unit of measurement describing the size of glyphs in a font. There are 72.27 typographic points per inch, in contrast to 72 points per inch in the Mac OS.

- __UDDI__

  Universal Description, Discovery and Integration. A searchable directory of web services that web service requesters can use to search for web services and obtain their WSDL documents.

- __UDF__

  Universal Disk Format. The file-system format used in DVD disks.

- __UDP__

  User Datagram Protocol. A lightweight and efficient connectionless datagram transport protocol. Used to send self-routing data throughout a network.

- __UFS__

  UNIX file system. An industry-standard file-system format used in UNIX-like operating systems such as BSD. UFS in OS X is a derivative of 4.4BSD UFS. Its disk layout is not compatible with other BSD UFS implementations.

- __UID__

  User ID. In [BSD](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgizta), the UID is a unique attribute of a user account that is used to identify the user. Each file system object and each process has an associated UID. See also [file UID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg43dc), [GID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhaztg), [UUID](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4tg).

- __umbrella framework__

  A system framework that includes and links with constituent subframeworks and other public frameworks. An umbrella framework “contains” the system software defining an application environment or a layer of system software. See also [subframework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhe2tq).

- __unary operator__

  An operator that derives a new value from a single value.

- __Unicode__

  Unicode is an ISO standard for universal worldwide character encoding developed by a consortium that includes Apple. Unicode has enough capacity to handle unique encodings for all characters available in all scripts, including the 2-byte script systems such as Chinese, Japanese, and Korean.

- __Unicode code point__

  A unique number that represents a character and allows it to be represented in an abstract way, independent of how it is rendered.

- __Unicode decomposition__

  The splitting of a composite glyph into its component parts, such as a base character and a combining mark.

- __Unicode Utilities__

  A shared library extension that provides table-based conversion between Unicode and other encodings.

- __unidirectional text__

  A sequence of text that has a single line direction. Compare [bidirectional text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgiyda).

- __uniform resource locator__

  See [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge3tm).

- __uninitialize__

  To return an [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) to its unconfigured state. Compare [reset](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgy4tc).

- __uniquing__

  In relational databases, a mechanism to ensure that, within a given context, only one object is associated with each row in the database.

- __unit test__

  A piece of code that exercises some part of an application. A unit test provides a specific input and expects the application to return a specific output.

- __unity gain__

  A [gain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhazdo) of 0 dB.

- __universal binary__

  An executable file that can contain code and data for more than one architecture. You can create a single binary file that runs on both PowerPC-based and Intel-based Macintosh computers. In Xcode, the Architectures (`ARCHS` ) build setting lets you specify which architectures Xcode builds for.

- __universal binaries__

  Executable files containing object code for more than one machine architecture.

- __universal procedure pointer__

  See [UPP](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge3ti).

- __Universal Serial Bus__

  See [USB](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge3ts).

- __unlocked__

  In Keychain Services, a state in which a keychain has a key in memory that can be used to encrypt or decrypt items in that particular keychain. A keychain is considered unlocked after its password has been entered (by the user or programmatically). An unlocked keychain can provide access to its secrets, subject to ACL checks, until it is locked again.

- __unordered tasks__

  In Xcode, tasks with no inputs and outputs, or tasks whose inputs are not the outputs of other tasks and whose outputs are not the inputs of other tasks. Compare [ordered tasks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm3tm).

- __unranked searching__

  See [inclusion/exclusion searching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe3dc).

- __untargeted gesture__

  In Ink Services, a gesture that does not have a defined hot spot. An application should apply the gesture to the current selection or insertion point.

- __update conflict__

  In database application development, the problem of multiple users or processes accessing and updating the same set of data simultaneously.

- __update region__

  A region maintained by the Window Manager that includes the parts of a window’s content region that need updating.

- __update strategy__

  In database application development, a strategy for managing update conflicts. See also [update conflict](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge3ta).

- __UPL__

  Universal page list. A data structure used when communicating with the virtual memory system. UPLs can be used to change the behavior of pages with respect to caching, permissions, mapping, and so on.

- __UPP__

  Universal procedure pointer. A generalized procedure pointer that allows code with different calling conventions to call each other. Some Carbon functions require you to pass UPPs for callbacks because the calling routine doesn’t know in advance if your code is Mach-O based or CFM-based.

- __URI__

  Uniform Resource Identifier. The web naming and addressing technology. A URI is a string of characters that identify a resource. Some typical URI schemes are HTTP and FTP.

- __URL__

  Uniform resource locator. A string, in a standard format, designating a file, web page, or other resource, typically (but not necessarily) to be accessed via the Internet. A URL is one type of URI. See also [virtual address](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizdc).

- __URL Loading System__

  An API that you can use to access the contents of http://, https://, and ftp:// URLs. Because https:// websites use [SSL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhezdi) (Secure Sockets Layer) or [TLS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsga4do) (Transport Layer Security) to protect data transfers, you can use the URL Loading System as a secure transport API. The URL Loading System is layered on top of [CFNetwork](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgi4ta).

- __URL type__

  A family of URLs characterized by a given [scheme](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg43ds) component. Compare [document type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgyydg).

- __USB__

  Universal Serial Bus. A multiplatform bus standard for connecting hardware devices, such as computers, keyboards, and audio devices. Specified by the USB Implementers Forum (USB-IF), an international industry standards body.

- __user client__

  An interface provided by an I/O Kit family, that enables a user process (which can’t call a kernel-resident driver or other service directly) to access hardware. In the kernel, this interface appears as a driver object called a _user client_; in user space, it is called a _device interface_ and is implemented as a CFPlugin object. See also [device interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgu2dc).

- __user data__

  Auxiliary data that your application can store in a QuickTime movie, track, or media structure. The user data is stored in a user data list; items in the list are referred to as _user data items_. Examples of user data include a copyright, date of creation, name of a movie’s director, and special hardware and software requirements. See also [user data item](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4de), [user data list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4dg).

- __user data item__

  In QuickTime, a single element in a user data list, such as a modification date or copyright notice.

- __user data list__

  The collection of user data for a QuickTime movie, track, or media. Each element in the user data list is called a _user data item_.

- __user-defined command__

  In AppleScript, a command that is implemented by a handler defined in a `script` object.

- __user focus__

  The window or text field control to which keyboard input is directed. The user can change the user focus by using the mouse or (sometimes) the Tab key.

- __user ID__

  Data, usually a character string, used to identify a user for a service or application.

- __user size__

  The window size determined by the user.

- __user space__

  (1) Virtual memory outside the protected partition in which the kernel resides. Applications, plug-ins, and other types of modules typically run in user space. Compare [kernel space](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrga4ds). (2) In Quartz 2D, the device-independent coordinate system used for drawing.

- __user state__

  A window’s user-defined size and position. See also [standard state](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrhezds), [zoom button](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi4ti).

-  __`using terms from` statement__

  A control statement that instructs AppleScript to use the terminology from the specified application in compiling the enclosed statements.

- __UTF-8__

  8-bit Unicode Transformation Format 8. A format used to represent a sequence of 16-bit Unicode characters with an equivalent sequence of 8-bit characters, none of which are zero. This sequence of characters can be represented using an ordinary C-language string.

- __UTF-16__

  16-bit Unicode Transformation Format. A form of Unicode in which 16-bits are used to encode a character.

- __UUID__

  Universally Unique Identifier. A type of UID or GID that is unique across all systems and all networks.

- __V1__

  In Core Audio, the original version of the [audio unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge2tq) interface, deprecated in OS X v10.2 and unsupported starting in OS X v10.5. V1 audio units differ from V2 audio units in that they supported [fan out](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4zta), supported interleaved streams, and used a component type and subtype approach different from that of V2. New development should be done with the V2 audio unit interface. Compare [V2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4tk).

- __V2__

  In Core Audio, the current version of the audio unit interface, recommended since OS X v10.2 and the only supported version starting with OS X v10.5. Compare [V1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsge4ti).

- __valid extension__

  A [filename extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg42ta) that does not contain spaces, periods, or characters that are not supported by the underlying file system. Compare [active extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgazte).

- __validation__

  A mechanism to ensure that user-entered data lies within specified limits.

- __variable__

  A named container in which to store a value.

- __variable bit rate__

  See [VBR](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgiydc).

- __variation axis__

  A range of values used to produce different type styles for a font. For example, a font that has a weighting axis could be displayed with weights that range from 0.7 point (light) to 1.3 points (bold). It is possible to combine variations. For example, font width variations can be combined with weighting variations to produce font variations ranging from light, narrow to bold, wide.

- __VBR__

  Variable bit rate. An encoding method available for some compression formats, such as AAC, that allows bit rate to vary according to the source material. The aim is to provide consistent perceived audio quality while minimizing file size. It does this by increasing the bit rate for difficult-to-encode portions and decreasing the bit rate for easy-to-encode portions. Compare [average bit rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqge3tk), [constant bit rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgqydc).

- __vector__

  A grouped series of numbers. Commonly represented either as a row of numbers [1, 2, 3, 4] or a column of numbers. It is analogous to an array.

- __vector code__

  Code that makes use of available on-board vector processors. vImage uses vector code.

- __vector graphics__

  The creation of digital images through a sequence of commands or mathematical statements that place lines and shapes in a two-dimensional or three-dimensional space. One advantage of vector graphics over bitmap graphics (or raster graphics) is that any element of the picture can be changed at any time because each element is stored as an independent object. Another advantage of vector graphics is that the resulting image file is typically smaller than a bitmap file containing the same image. Examples of vector-image file types are PDF, encapsulated PostScript (EPS), and SVG. Compare [raster graphics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyzdm).

- __vector index__

  In Search Kit, an index containing document URL objects, as keys, mapped to the terms that each document contains. See also [index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqhe3de), [inverted index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgaztk), [inverted-vector index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgaztm)

- __vector processor__

  A processor that can perform arithmetic on several pairs of numbers simultaneously. Also called an _array processor_.

- __verb-first command__

  In AppleScript, a script command that invokes its `performDefaultImplementation` method. With a verb-first command, a single method performs the action (or verb) on any number of objects. Compare [object-first command](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgm2di).

- __version number__

  See [revision number](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4ydo).

- __versioned bundle__

  A type of bundle that allows for multiple versions of framework code and header files to be stored inside the bundle.

- __versioning__

  With frameworks, schemes to implement backward and forward compatibility of frameworks. Versioning information is written into a framework’s dynamic shared library and is also reflected in the internal structure of a framework. See also [major version](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge4tk), [minor version](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgi2dm).

- __vertex__

  A three-dimensional point. A set of vertices specify the geometry of a shape. Vertices can have a number of additional attributes such as colors and texture coordinates.

- __vertex array__

  A data structure that stores a block of data that specifies such things as vertex coordinates, texture coordinates, surface normals, RGBA colors, color indices, and edge flags.

- __vertical reflect__

  A type of geometric operation that reflects an image about its x-axis.

- __vertical shear__

  An image filter that shifts pixels along the y-axis to create an effect that’s similar to physical shearing.

- __VFS__

  Virtual File System. A set of standard internal file-system interfaces and utilities that facilitate support for additional file systems. VFS provides an infrastructure for file systems built into the kernel.

- __VIDEO_TS__

  The filename used for the video directory or folder on a standard-definition DVD disc volume. Files inside this directory contain pointers to the sectors on the disc that hold the program streams.

- __view font__

  The default font used in text and lists. This may be user adjustable, as it is in the Finder.

- __View menu__

  A menu that provides commands that affect what users see in a window. In the Finder, for example, the View menu contains commands for displaying windows as columns, icons, or lists.

- __view rectangle__

  In MLTE, the rectangle defining the portion of the window within which text is actually displayed. Text drawn in the destination rectangle is made visible to the application user in the view rectangle.

- __views__

  In Cocoa, objects that support drawing.

- __virtual address__

  A memory address that is usable by software. Each task has its own range of virtual addresses, which begins at address zero. The Mach operating system makes the CPU hardware map these addresses onto physical memory only when necessary, using disk memory at other times. Compare [physical address](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq2ts).

- __virtual destination__

  In Core Audio, a designation by a software MIDI device indicating that it can receive MIDI data. Compare [virtual source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizdm).

- __virtual machine__

  See [VM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizds).

- __virtual memory__

  See [VM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizds).

- __virtual screen__

  A combination of hardware, renderer, and pixel format that OpenGL selects as suitable for an imaging task. When the current virtual screen changes, the current renderer typically changes.

- __virtual source__

  A designation by a software MIDI device indicating that it can transmit MIDI data. Compare [virtual destination](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgizde).

- __visible region__

  The portion of a window’s content region that is visible to the user.

- __visual context__

  An abstract space that indicates where drawing should occur. For example, an OpenGL context specifies where OpenGL drawing should occur. A visual context is typically associated with an `NSView` or `HIView` object.

- __VM__

  (1) Virtual machine. A simulated computer in that it runs on a host computer but behaves as if it were a separate computer. The Java virtual machine works as a self-contained operating environment to run Java applications and applets. (2) Virtual memory. The use of a disk partition or a file on disk to provide the facilities usually provided by RAM. The virtual-memory manager in OS X provides either a 32-bit or 64-bit protected address space for each task (depending on the options used to build the task) and facilitates efficient sharing of that address space.

- __vnode__

  An in-memory data structure containing information about a file.

- __vnode pager__

  In Mach, one of the built-in pagers. The vnode pager maps files into memory objects. See also [default pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqguytc), [pager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgqydk).

- __voice__

  A component containing data and, optionally, executable code that helps to shape the sound of synthesized speech.

- __VoiceOver__

  A spoken user interface technology for visually impaired users. VoiceOver is part of OS X.

- __volume__

  (1) A storage device or a portion of a storage device that is formatted to contain folders and files of a particular file system. A hard disk, for example, may be divided into several volumes (also known as _partitions_) (2) In [psychoacoustics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgu4ta), the average perceived loudness of a sound. Compare [level](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge2de).

- __volume format__

  The structure of file and folder (directory) information on a hard disk, a partition of a hard disk, a CD-ROM, or some other volume mounted on a computer system. Volume formats can specify such things as multiple forks (HFS and HFS+), symbolic and hard links (UFS), case sensitivity of filenames, and maximum length of filenames. See also [file system](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg42tm).

- __volume requirement__

  A test that compares the value of a volume property (such as free space) with a value. Volume requirements determine whether the user can choose a particular volume as the destination volume of a product package.

- __VR__

  See QuickTime VR.

- __V-Twin__

  See [AIAT](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga2ts).

- __WaitNextEvent__

  The function that drove the event loop in older versions of the Mac OS. _See also_ [Classic Event Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgmzdk).

- __WAR__

  Web application archive. A file created using the `jar` utility (and saved with the `.war` extension) that contains all the files that make up a web application.

- __watchpoint__

  In Xcode, a place in code that pauses execution of the program whenever the value of the watched item changes.

- __WAV__

  A chunk-based digital audio file format originally developed for IBM-compatible PCs. Although WAV files can hold compressed audio data, they most commonly hold uncompressed [linear PCM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrge2to) data. WAV is a variant of the RIFF bitstream format. See also [RIFF](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4yta).

- __waveform__

  The shape of a signal when visualized as a graph showing its variation in amplitude over time.

- __wavelength__

  The span of one complete cycle in a repeating [waveform](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi2dg).

- __web application__

  A file structure that contains servlets, JSP pages, HTML documents and other resources. This structure can be deployed on any servlet-enabled web server.

- __Web Assistant__

  Tool used to customize a Direct to Web application.

- __web component__

  An object (of the `WOComponent` class) that represents a webpage or a reusable portion of one.

- __WebDAV__

  Web-based Distributed Authoring and Versioning. An extension of HTTP that allows collaborative file management on the web.

- __WebObjects Builder__

  An application used to edit web components.

- __WebObjects Deployment__

  A software package that allows you to deploy WebObjects applications on an intranet or the web. It includes tools to design applications using an object-oriented approach. You need to install a WebObjects deployment license on computers on which you want to install this package.

- __webpage template__

  An HTML file that specifies the overall appearance of a webpage generated from a web component.

- __web server__

  An application that serves webpages to web browsers using the HTTP protocol. In WebObjects, the web server lies between the browser and a WebObjects application. When the web server receives a request from a browser, it passes the request to the WebObjects adaptor, which generates a response and returns it to the web server. The web server then sends the response to the browser. Also called an _HTTP server_.

- __web service__

  A network-based repository of processes or tasks that can be used by applications to access data or execute operations across disparate platforms.

- __Web Services Assistant__

  Application used to customize a Direct to Web Services applications.

- __weighting__

  Systematic adjustment of a measurement to highlight a particular criterion. For example, [SPL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrheyte) (sound pressure level) measurements can be weighted to approximate how people perceive sound, placing more emphasis on midrange frequencies than on higher or lower ones.

- __wheel group__

  In [BSD](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgizta), a special group, membership in which confers on users the ability to become the [root user](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4zds) by using the `su` utility on the command line. Users who are not in the wheel group can’t become the root user, even if they have the correct password. In OS X, the [admin group](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqga2de) is used for this purpose rather than the wheel group.

- __widget__

  An HTML-based program that runs in the Dashboard layer of the system.

- __wildcard character__

  An operator used in a query that indicates matching on any character. In Search Kit, the wildcard character is the asterisk. Depending on usage, the wildcard character can indicate prefix, suffix, or substring searching. See also [Roman keyboard script](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg4zdc), [query](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgyytg).

- __window__

  The primary means of displaying screen information on Mac computers.

- __window layering__

  The layering of windows according to the window class hierarchy. Compare [window ordering](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi3de).

- __Window menu__

  A menu that contains commands for managing document windows. The menu lists an application’s open document windows, including minimized windows, in the order in which they were opened.

- __window ordering__

  The layering of windows within a specific window class. Compare [window layering](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbsgi3da).

- __window reference__

  A pointer to an opaque data structure that defines a window. All access to a window or its attributes is through the window reference.

- __window server__

  A systemwide process that is responsible for rudimentary screen displays, window compositing and management, event routing, and cursor management. It coordinates low-level windowing behavior and enforces a fundamental uniformity in what appears on the screen.

- __wired memory__

  A range of memory that the virtual-memory system does not page out or move. The memory involved in an I/O transfer must be wired down to prevent the physical relocation of data being accessed by hardware. In the I/O Kit memory is wired when the memory descriptor describing the memory prepares the memory for I/O (which happens when its `prepare` method is invoked).

- __wired sprite__

  A sprite such as a clickable button that has wired actions associated with it.

- __with-stream shift__

  A uniform shift parallel to the baseline of the positions of individual pairs or sets of glyphs in the style run. Compare [cross-stream shift](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqgq2ta).

-  __`with timeout` statement__

  An AppleScript control statement that specifies the amount of time AppleScript waits for application commands to complete before stopping execution of the script.

-  __`with transaction` statement__

  An AppleScript control statement that allows you to take advantage of applications that support the notion of a transaction—a sequence of related events that should be performed as if they were a single operation, such that either all of the changes are applied or none are.

- __WOA__

  WebObjects application bundle. A bundle that stores all the files needed by a WebObjects application.

- __word wrap__

  The automatic continuation of text from the end of one line to the beginning of the next without breaking in the middle of a word.

- __work loop__

  A gating mechanism that ensures single-threaded access to the data structures and hardware registers used by a driver. Specifically, it is a mutex lock associated with a thread. A work loop typically has several event sources attached to it; they use the work loop to ensure a protected, gated context for processing events. See also [event source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbqg4ydm).

- __workspace__

  The area in the Quartz Composer development tool used to assemble patches.

- __WorldScript__

  A group of Mac OS managers, extensions, and resources that facilitate multilingual text processing.

- __WOServices__

  A WebObjects service that monitors wotaskd processes. Its main duty is to monitor wotaskd and restart it if it dies or when the host is restarted. The implementation of this service is platform dependent.

- __wotaskd__

  WebObjects task daemon. A WebObjects Deployment tool that manages the instances on an application host. It’s used by Monitor to propagate site configuration changes throughout the site’s application hosts.

- __writing system__

  A set of characters and the basic rules for their use in creating a visual depiction of language. Writing systems may differ in the direction in which their characters and lines run, the size of the character set used, and the context sensitivity of character selection. Writing systems include Roman, Japanese, Arabic, and Hebrew. Compare [script system](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrg44ta).

- __WSDL__

  Web Services Description Language. XML-based language used to describe web services. Web service consumers can dynamically parse a WSDL document to determine the operations a web service provides and how to execute them.

- __WSS-Core__

  Web Services Security Core Specification. A specification that defines a set of SOAP extensions that can be used to provide message-level data integrity and confidentiality.

- __X.509__

  A standard for digital certificates promulgated by the International Telecommunication Union (ITU). The X.509 ITU standard is widely used on the Internet and throughout the information technology industry for designing secure applications based on a [PKI](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donjsfvbewmbrl5buqmbsfvbewmbrl5buqmbsl5gewmbrgq3tg) (public key infrastructure).

- __Xcode__

  An integrated development environment used to develop iOS and Mac applications. Xcode incorporates editor, compiler, debugger, linker, and other tools and resources.

- __Xcode application__

  The main application of the Xcode integrated development environment (IDE). It manages the other applications that are part of Xcode and provides the main user interface used to develop software products.

- __Xcode project__

  A group that contains the source files, libraries, media, and other resources needed to build a product.

- __xib file__

  An XML-based version of a nib file. Xib files are the preferred format to use during development of your application. At build-time, they are compiled into nib files so that they can be deployed in your application bundle.

- __XML__

  Extensible Markup Language. A metalanguage containing rules for constructing specialized markup languages. XML is very flexible, allowing users to define their own tags. XML is a dialect of SGML (Standard Generalized Markup Language).

- __XML namespaces__

  A specification that allows qualifying element names by associating element-name prefixes to URIs.

- __XML parser__

  A software engine that reads and writes XML documents.

- __XML-RPC__

  A simple protocol for making remote procedure requests to Internet-based servers.

- __XML Schema__

  A specification used to describe the structure of XML documents. XML Schema is more powerful than document type definition (DTD) because it includes facilities to specify the data type of elements and it is based on XML.

- __XNU__

  X is Not UNIX. The OS X kernel. XNU combines the functionality of Mach and BSD with the I/O Kit, the driver model for OS X.

- __XSLT__

  Extensible Stylesheet Language Transformations. A specification that allows the conversion of an XML document into another XML document or any other type of document.

- __XSLT stylesheet__

  A file written in XSLT that specifies how a source document is to be converted into another document.

- __XSLT transformer__

  Software that converts an XML document into another document using an XSLT stylesheet.

- __zoom button__

  A control that toggles a window between its standard state and its user state.

[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20OS%20X%20Glossary.md)

