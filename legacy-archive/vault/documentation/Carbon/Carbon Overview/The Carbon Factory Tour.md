---
title: Carbon Overview
apple_id: TP30000990
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/newtocarbon/FactoryTour/FactoryTour.html
archived_at: '2026-07-15T05:25:14.853053Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon Overview](Introduction%20to%20Carbon%20Overview.md)


[Next](Legacy%20Interfaces.md)[Previous](Carbon%20Basics.md)

# The Carbon Factory Tour

Carbon contains many programming interfaces. What interfaces you will require depends on the type of applications you want to write, but as is often the case, some are more commonly used than others. This section divides up the Carbon interfaces according to usage (from fundamental to esoteric) and gives some useful information about each one. To learn more about a particular interface, you can use the Documentation Help feature integrated into Xcode. You can also consult the technical documentation on the Apple developer web site.

Carbon interfaces are defined as those accessed through the Carbon umbrella framework. See the header `Carbon.h` to see which interfaces are included.

This section covers the interfaces most likely to be called by a Macintosh application. These managers and services provide the basic user interface as well as fundamental features, such as the ability to save and print files. You can build basic but fully functional Carbon applications using the interfaces described here.

The following interfaces (sometimes called the Human Interface Toolbox or HIToolbox) are grouped together because they generally work together to create and manage the user interface. In most cases, Interface Builder and the Interface Builder Services programming interface can handle the creation and control of the basic user interface. However, to accomplish more esoteric tasks, you may need to call additional functions in the Human Interface Toolbox interfaces:

- _HIView/Control Manager_. Lets you create and manipulate views, which are building blocks for user interface elements. All standard controls (buttons, scroll bars, sliders, and so on) are views, as is content displayed in a menu. Special views also exist for displaying text, HTML, and QuickTime content. HIView is superseding the older Control Manager, which let you manipulate controls. At the implementation level, however, HIViews and controls are identical objects in memory and can be used interchangeably.
- _Dialog Manager_. Lets you create and manipulate dialogs, which are windows that either prompt you for input or display information. Interface Builder and Carbon event handlers mostly supersede the Dialog Manager, except in the cases where you want to put up a standard alert dialog box or sheet.
- _Menu Manager._ Lets you create and manipulate menus.
- _Window Manager._ Lets you create and manipulate windows, which are the user's primary means of interacting with your software.
- _HIToolbar._ Lets you create and manipulate toolbars.
- _HITheme/Appearance Manager._ Provides the underlying support for themes, which unify the appearance of human interface objects in your application, including alert icons, controls, background colors, dialogs, menus, and windows. When you draw nonstandard user interface elements with HITheme, their appearance will continue to match the standard elements even if the theme changes (for example, from Aqua to Graphite). The Appearance Manager is the older QuickDraw-centric version of HITheme.
- _Carbon Event Manager._ Controls the event model for Macintosh applications. Note that Carbon also contains an older event-handling system (simply called the Event Manager), which is included only to assist legacy applications moving to Mac OS X.
- _Interface Builder Services._ Lets your code access the user interface elements created with Interface Builder and stored in a nib file. While Interface Builder is not required for creating your user interface, it simplifies the process and makes localization easier as well.

While the HIToolbox interfaces are flexible enough to let you do just about anything with your user interface, that doesn't mean you should. When designing and laying out your user interface, you need to follow the _Apple Human Interface Guidelines_. Just as adherence to common rules and customs when designing steering wheels and dashboards makes driving more pleasant and less confusing, following the Apple guidelines lets your application provide the best possible experience for your users.

If you use Interface Builder, adhering to the Apple Guidelines is that much easier; you can have it automatically tell you when various items in a window are spaced correctly.

While the standard user interface is sufficient for most users, those who have disabilities may need alternate methods to interact with your application. Apple provides a number of special accessibility features to meet this need. If you plan to sell your application to governmental agencies in the United States, your application must support accessibility.

Accessibility is not just a benefit for disabled users. An application that supports accessibility is also easier to test, and it makes it easier to provide explanatory help for all users.

See _[Accessibility Programming Guide for OS X](https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/index.html#//apple_ref/doc/uid/TP40001078)_ to learn more about accessibility on Mac OS X, and _[Accessibility Programming Guidelines for Carbon](../Accessibility%20Programming%20Guidelines%20for%20Carbon/Introduction%20to%20Accessibility%20Programming%20Guidelines%20for%20Carbon.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrx)_ to learn what you need to do to support accessibility in Carbon applications.

The following interfaces work behind the scenes, as it were, to provide the basic functionality that you expect from most applications:

- _Carbon Printing Manager._ Lets you print from Macintosh applications.
- _Navigation Services._ Creates a standard user interface for opening and saving documents.
- _File Manager._ Lets you read and write data to storage media (hard drives, USB drives, and so on).
- _HIObject_. A "base class" that provides the underlying support for HIViews. You probably won't need to access HIObject APIs directly unless you are creating custom HIViews.
- _HIArchive._ Provides an easy way to store and retrieve data and HIObjects (including HIViews). HIArchives are stored in a flattened format that you can save on disk or pass to other applications or services as desired.
- _Bundle Services._ Lets you access data stored in a bundle file hierarchy, which is the standard method of packaging applications in Mac OS X. Bundle Services is part of Core Foundation.
- _String Services._ Allows basic manipulation of Unicode strings. String Services is part of Core Foundation.
- _Multilingual Text Engine (MLTE)._ Provides basic text display and formatting features. Because it is Unicode-based, MLTE can easily handle other languages and script systems. MLTE also provides support for spellchecking and accessing the standard system font panel.
- _Quartz._ Handles all the 2D drawing to the Macintosh screen. Quartz is a powerful imaging technology that provides easy access to features such as transparency, layers, path-based drawing, offscreen rendering, advanced color management, anti-aliased rendering, and PDF document creation, display, and parsing.
- _HIShape._ A Quartz-compatible interface for creating and manipulating arbitrary graphical shapes.
- _HIGeometry._ A Quartz-compatible interface for defining and manipulating basic graphical forms (points and rectangles).
- _Uniform Type Identifers._ Not a technology, but a standard for identifying data and file types that eliminates having to keep track of all the possible ways to tag a particular type (for example, using file extensions, MIME types, OSTypes, and so on). Navigation Services and the Pasteboard Manager are two technologies that use uniform type identifiers.

This section lists interfaces that are desirable, but not necessary for most applications. Full-featured commercial applications usually adopt a number of these interfaces.

- _Pasteboard Manager._ Lets the user copy items to and from the Clipboard for cut-and-paste operations. More generally, you can use pasteboards for any sort of data interchange. For example, the Drag Manager uses pasteboards to transfer drag and drop data.
- _Drag Manager._ Used for implementing drag and drop between applications. For example, the user can select text in one application and then, rather than copying and pasting, simply drag the text into the window of another application.
- _Icon Services._ Provides a simplified way to present icons in your application. Instead of storing every type of icon you need with your application, you can obtain commonly used icons through Icon Services. Doing so minimizes the amount of work you have to do and increases system efficiency.
- _Folder Manager._ Lets you find, create, and otherwise manipulate specific folders such as a user's home directory or the system's Fonts folder.
- _Alias Manager._ Lets you create and resolve aliases to files and folders. An alias is a link or reference to an application, folder, or file.
- _Open Scripting Architecture._ Describes the interfaces to control or automate the actions of one or more applications. You use the _Apple Event Manager_ portion to interpret and react to events received from other applications, and _AppleScript_ is the scripting language that you use to describe what actions to take. For example, if your application might be used in an automated workflow, where multiple applications manipulate a file in turn, you should make your application Apple Event savvy so it can act upon commands sent to it from an external script.
- _Core Foundation._ A collection of object-based interfaces that can handle data types and various system services. Bundle Services and String Services (already described in "The Starter Kit") are Core Foundation services. Other Core Foundation interfaces handle plug-ins, preferences, and so on. For the complete list of Core Foundation interfaces see _[Core Foundation Framework Reference](https://developer.apple.com/documentation/corefoundation)_. To learn how to use Core Foundation APIs, see _[Getting Started with Core Foundation](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_CoreFoundation/_index.html#//apple_ref/doc/uid/TP30001089)_.
- _Search Kit._ Provides powerful text searching capability for your application. Apple’s Spotlight technology is built on top of Search Kit to provide content searching in Finder, Mail, and the Spotlight menu.
- _Gestalt Manager._ Lets your application determine specific information about the system, its interfaces, or the underlying hardware. For example, you can call the Gestalt Manager to determine what version of a particular technology is installed. Doing so lets you avoid calling functions that may not be available on a particular computer.
- _Notification Manager._ This interface allows applications in the background to notify the user (for example, after finishing a lengthy calculation). A primary use of the Notification Manager is to notify the Dock about changes to the application.
- _Process Manager_. Lets you obtain useful information about running processes.
- _Multiprocessing Services._ Lets you create preemptively scheduled execution tasks (threads) in your application. If your application might want to perform several actions simultaneously (such as downloading files or performing background calculations), you should consider adopting Multiprocessing Services. Tasks created with this interface will automatically take advantage of multiple processors, if present.
- _Thread Manager._ Lets you create cooperatively scheduled threads in your application. This interface is generally not as useful as Multiprocessing Services. However, if you need a certain amount of control over when your threads execute, you should consider the Thread Manager.
- _Quartz Services._ Lets you access low-level features of the Mac OS X Window Server. For example, you can use Quartz Services to change display modes, monitor configurations, and so on.

These are more esoteric interfaces that you generally would not use unless you were interested in creating specific types of applications. Some provide specialized features, while others expand on basic functionality (such as text manipulation). You use these interfaces to create highly sophisticated applications that take full advantage of the system software.

Many of these interfaces are not part of the Carbon framework, but can be called from Carbon applications.

Some of these interfaces have Objective-C APIs, which will require you to write some Objective-C code. For details on how to call Objective C code from C code, see _[Carbon-Cocoa Integration Guide](../../Cocoa/Carbon-Cocoa%20Integration%20Guide/Introduction%20to%20Carbon-Cocoa%20Integration%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqojt)_.

_QuickTime_ is Apple's multimedia programming interface. You use QuickTime to create and play file-based or streaming movies, virtual reality environments, sounds, and music files. The QuickTime programming interface is broad and very powerful. To gain a better understanding of its features, read _[Getting Started with QuickTime](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_QuickTime/_index.html#//apple_ref/doc/uid/TP30001099)_ and _[QuickTime Overview](../../Quick%20Time/QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs)_.

_Core Video_ complements QuickTime as it provides a way to access individual frames in the video pipeline. You can then manipulate the frames using OpenGL or Core Image. For example, if you want to add filter effects to the video, or map the video onto a shape, you can use Core Video to do so. See _[Core Video Programming Guide](../../Graphics%20Imaging/Core%20Video%20Programming%20Guide/Introduction%20to%20Core%20Video%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmzw)_ for more information.

_Core Audio_ is the audio architecture for Mac OS X. It provides a broad range of audio and MIDI services for hardware and application developers, such as state-of-the-art audio recording and playback, digital signal processing, MIDI sequencing, low-level access to audio devices, software-based sound synthesis, and much more.

These interfaces are for applications that create and manipulate images, such as a photo retouching program:

- _Color Picker Manager_ lets you bring up a simple user interface for choosing colors, which can be useful for paint programs as well as any application that allows the user to customize colors.
- _ColorSync_ is an Apple technology that ensures consistent color calibration across different applications and hardware. For example, when using ColorSync, users can be sure that the particular shade of green they see on their monitor is as close as possible to what they will get when the local print house prints their brochure.
- _Picture Utilities_ are used to obtain information about a graphic image, such as the colors used, its resolution, and any comments that may be included.
- _Core Image_ provides access to built-in image filters for both still images and video and provides support for custom filters and near real-time processing. Core Image is an Objective-C API.

For high-quality 3D graphics, the interface of choice is _OpenGL_. In actuality this is an industry-standard interface and not part of Carbon, but it is fully compatible with Carbon (just make sure you link to the OpenGL framework when you build). You can use OpenGL's 3D rendering capabilities for everything from medical imaging to virtual reality to incredibly photorealistic games. See _[OpenGL Programming Guide for Mac](../../Graphics%20Imaging/OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_ for more information about how to use OpenGL in Mac OS X.

To render HTML in Carbon windows, you can use _Web Kit._ HIView has a special web view that can display HTML acquired with Web Kit. See _Web Kit C Reference_ for more details.

These interfaces let your application interact with CDs or DVDs.

- To burn data or audio to a CD or DVD from your application, use the _Disc Recording_ API.
- To access and play DVD video content, use the _DVD Playback_ API.

If your application needs to synchronize some of its data with a device, such as an iPod or PDA, you should use _Sync Services_ to do so. You can also synchronize separate Macintosh computers if the user has a .Mac account. Sync Services is an Objective-C API.

These interfaces let your application speak text or recognize speech:

- _Speech Recognition Manager_ lets your application recognize spoken commands. For example, you can navigate between windows, open files, or run scripts solely through voice commands. It can be especially useful to activate commands that would normally require navigating deeply nested menus or multiple dialogs.
- _Speech Synthesis Manager_ lets your application speak lines of text using a number of different voices. Note that the speech recognition and speech synthesis interfaces use the same English dictionary, which allows them to work in conjunction with each other. For example, you could use the Speech Synthesis Manager to determine how to pronounce a word, so the Speech Recognition Manager can recognize it more easily.

Most of these interfaces are only for developers writing text-intensive applications. For basic text input and display, the Multilingual Text Engine provides a much simpler interface for most of the same functionality.

- _ATSUI_ is the interface for drawing Unicode text. It allows precise control over all aspects of the text, from kerning to ligatures to bidirectionality.
- _ATS Types_ interface defines data types and callback functions used by ATSUI and other text interfaces.
- _Date, Time, and Measurement Utilities_ contain functions to obtain and manipulate date, time, location, and other values that may need to be localized for different countries or regions.
- _Dictionary Manager_ provides an easy interface to access dictionary files. For example, if your application contained a spell checker, it could use this interface to look up words in a dictionary file. Similarly, text input methods that require looking up words in a file could also use this interface.
- _Font Manager._ Lets you manipulate the fonts that your application uses to display or print text.
- _International Resources_ contain structures and constants that are used for localizing text to different countries or regions. In most cases, you won't need to access this interface yourself, because other text interfaces will access it for you.
- _Text Services Manager_ provides support for text input methods. For example, editing some types of non-Western text requires close cooperation between the application and the Text Services Manager to allow text input methods to access the application's windows. If you use the Multilingual Text Engine, all Text Services Manager support is handled automatically.
- _FontSync_ allows you to synchronize fonts available on different computers or printers to prevent font mismatches. For example, two fonts on different computers may have the same name but not be identical. FontSync can attempt to match fonts based on content rather than name, thus minimizing the possibility of a mismatch when a text file is moved from one computer to another.
- _Language Analysis Manager_ allows your application to manage language analysis engines (stored as plug-ins). These engines are typically used with text input methods to isolate meaningful words or characters. For example, for Japanese text input you may use a language analysis engine to interpret the keystrokes the user enters, so you can display the Kanji characters that match their meaning.
- _Text Encoding Conversion Manager_ allows you to change text from one encoding to another. This conversion can be useful for text going to or from the Internet, where many different text encodings exist. For example, to read text streamed over a network from a Windows computer, you may need to convert it from the Windows text encoding to the corresponding one for Macintosh computers. Similarly, if you are handling input methods or file systems that only support the older Mac OS encodings, you can use the Text Encoding Converter to convert between them and Unicode.
- _Unicode Utilities_ let you perform basic manipulation of Unicode strings. Note that Core Foundation String Services provide similar functionality and are more portable across Mac OS X execution environments.
- _Ink Services_ is an interface that lets users enter text using a stylus on a graphics tablet. The text is automatically recognized and translated into keystrokes that your application can then interpret.

If your application uses or enables network access, you may need to use one of the following managers or services:

- Core Foundation's _CFNetwork Services_ provides interfaces for basic networking tasks, such as working with BSD sockets, managing information about remote hosts, and working with HTTP, HTTPS, and FTP servers. See _[CFNetwork Programming Guide](../../Networking/CFNetwork%20Programming%20Guide/Introduction%20to%20CFNetwork%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzs)_ for more information.
- _Network Services Location Manager_, which provides an easy way to find network services on a local network.
- _Web Services_, which provides an interface for transferring data over the internet using standard protocols such as HTTP and XML.
- _Internet Config_, which is used to access Internet networking preferences from a global repository on a user's machine. For example, Internet Config stores the user's default browser selection, so if another application needs to launch a browser (when a URL is clicked), it can easily determine which one to activate.

Mac OS X also supports standard networking security features, such as SSL/TLS. See [Security](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnjufvjvomq) for more information.

Mac OS X supports a number of standard security services (certificates, an authentication interface, SSL/TLS for networking, and so on) as well as Apple-specific features, such as keychains, which allow you store and access multiple passwords using a master password. For an overview of basic security concepts and the security services available in Mac OS X, see _[Security Overview](../../Security/Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_. _Getting Started With Security_ describes documentation available for implementing security features.

Mac OS X is designed to shield applications from low-level workings of the system. However, if you are writing driver-level code that needs to talk directly to hardware (such as a video card), you need to use _I/O Kit._ Most applications don't need this level of control and should not be at all dependent on hardware.To that end, you should use I/O Kit only if you are sure you need it.

This section covers utility interfaces that may be useful, depending on the application. These managers and services aren't particularly related to any technology or functionality:

- _Finder._ This interface contains a number of structures that are useful for giving information to the Finder.
- _Debugger Services._ Contains functions that can assist you in debugging your application. In most cases, however, you should begin with the debugging facilities available with Xcode before using this interface.
- _Assert Macros._ Contains debugging macros that you might find useful. Many Apple code samples use these macros, so it's useful to understand how they work. These macros are defined in `AssertMacros.h`, which you can find in the `/usr/include` directory (use Terminal to access).
- _Mathematical and Logical Utilities._ Contains functions and constants for mathematical and logical operations (for example, `FloatToFixed`, `pi`, and `BitAnd`).

[Next](Legacy%20Interfaces.md)[Previous](Carbon%20Basics.md)

