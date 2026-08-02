---
title: Porting UNIX/Linux Applications to OS X
apple_id: TP30001003
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Porting/Conceptual/PortingUnix/unix_environments/unix_environments.html
archived_at: '2026-07-18T01:50:47.932129Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting UNIX/Linux Applications to OS X](Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md)


[Next](Porting%20File%2C%20Device%2C%20and%20Network%20I-O.md)[Previous](Choosing%20a%20Graphical%20Environment%20for%20Your%20Application.md)

# Using Traditional UNIX Graphical Environments

UNIX-based operating systems have grown to include many environments for providing a graphical interface to users. The X Window System, also known as X11, is probably the most well known. As more specific needs have arisen, other architectures have been developed that assume an X11 implementation.

OS X does not use the X Window System by default, but implementations of X11 are available from Apple and from third-party developers. This means that X Window System–based applications can be run, as can many of the alternative UNIX-style graphical environments. This section gives more details on some of these environments.

If your application uses the X Window System you need to either port the user interface to a native OS X environment, provide an X Window System implementation with your application, or require that your users install the Apple X11 package (an installation option in the OS X installer beginning in OS X version 10.3).

If you are a commercial software developer or if your software will be used by traditional end users (including word processors, web browsers, and so on), you may want to consider porting to a native graphical environment instead of requiring X11. However, for internal tools or for tools with a specialized user base, it may be more reasonable to continue using X11. The sections in this chapter will help you decide how to choose an appropriate X11-based environment for your application.

Many UNIX applications are designed using high-level widget toolkits such as Tcl/Tk, Motif (or OpenMotif or Lesstif), and Qt. These environments work well across many platforms. However, that cross-platform nature comes with a price in flexibility. In essence, to be cross-platform, they can only support capabilities that are generic to all of the potential operating environments, and as such, they tend to provide only the lowest common denominator in terms of functionality.

Such toolkits are often weak in areas such as performance and flexibility, and many do not allow precise control over how GUI elements are laid out.

If they provide everything you need, then they are good choices. Otherwise, a more flexible alternative such as raw Xlib programming, or a more Mac-tuned alternative such as Carbon or Cocoa may be more appropriate.

Other UNIX solutions exist for more extreme cross-platform environments. One example is MicroWindows, which is designed to allow ease of code sharing between X11 and Windows by implementing a subset of the Win32 graphics APIs on X11. Because this is really just an X11 application, it should be possible to use it on OS X. However, due to the amount of abstraction involved, such a solution will not perform as well as a native application.

If you are trying to design an application for such an environment, it is generally better to rearchitect your code to have multiple front-ends—one for Windows, one for OS X, and one for UNIX (X11). See [(Re)designing for Portability](%28Re%29designing%20for%20Portability.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjxfvkfawcsivddcmbr) for more information on creating a graphics abstraction layer.

OS X does not include an X11R6 implementation by default. If you are intent on only porting your application without adding any OS X functionality, you can still run X11 on OS X. Along with your application, you should instruct your users on how to install one.

The easiest way to get an X11 implementation is to install the Apple X11 implementation. Beginning in OS X v10.3, the X11 package is an optional installation that comes on the install DVD or CD.

For _older versions_ of OS X (before v10.4), you can download X11 from [http://www.apple.com/downloads/macosx/apple/macosx_updates/x11formacosx.html](http://www.apple.com/downloads/macosx/apple/macosx_updates/x11formacosx.html).

In addition, several other commercial and free alternatives exist.

XTools by Tenon Intersystems ([http://www.tenon.com](http://www.tenon.com/)) and eXodus from Powerlan USA both provide X11 servers that coexist with Aqua.

If you do not need a commercial implementation of X11, XFree86 offers a very robust free X11R6 implementation. The OS X version of XFree86 is an active project with integral support from the XQuartz (formerly XDarwin) project. More information on the XQuartz project including tips for installing X11 is available at [http://xquartz.macosforge.org/trac/wiki](http://xquartz.macosforge.org/trac/wiki). XFree86 itself can be downloaded from [http://xfree86.org/](http://xfree86.org/).

With an X Window System implementation, you are now free to use toolkits that you are already familiar with—for example, GTK+ or KDE.

- The de facto standard in display technology for UNIX-based operating systems
- Open source implementation is available
- Somewhat portable to certain embedded systems

- Complicated development environment
- Requires substantial disk space for a full installation
- Is not native to OS X. This means your application is treated as a second-class citizen to some extent, particularly in the areas of drag-and-drop and system services.

There is a native Aqua version of Tk available at [http://tcl.sourceforge.net](http://tcl.sourceforge.net/). With this you can easily add graphical elements to your existing Perl, Python, or Tcl scripts.

- Cross-platform development environment
- Easily integrates with Tcl, Perl, and Python scripts
- Open source implementation is available

- Not supported by default in OS X
- As with most high-level toolkits, flexibility is limited

Qt is a C++ toolkit for building graphical user interfaces. It is very popular in the UNIX world, as it is used by the very popular K Desktop Environment, KDE. Trolltech has a native version of Qt, Qt/Mac, available for OS X. If you already have a C++ application or are considering building one, Qt lets you build applications that run natively in OS X as well as Linux and Windows. Information about Qt/Mac is available at [http://www.qt.nokia.com](http://www.qt.nokia.com/). Qt/Mac does not run on top of X11 in OS X, but the source code is compatible with Qt’s X11 implementation.

- Cross-platform development environment
- Integrates easily with C++ code
- Robust feature set

- Requires licensing for commercial development
- As with most high-level toolkits, flexibility is limited

GTK+ and GTKmm are the C and C++ interfaces (respectively) to another toolkit for building graphical user interfaces. It is popular in the Gimp and Gnome development communities. There is a beta native version of the GTK+ 2.x toolkits available for OS X. If you already have a C or C++ application or are considering building one, GTK+ lets you build applications that run natively in OS X as well as Linux and Windows.

Information about Gtk-MacOSX (an implementation of the GTK+ 2.x toolkit) is available at [http://gtk-osx.sourceforge.net/](http://gtk-osx.sourceforge.net/).

These toolkits do not run on top of X11 in OS X, but are source-code–compatible with the equivalent X11 implementations.

- Cross-platform development environment
- Integrates easily with C/C++ code
- Robust feature set

- LGPL license reverse engineering clause may raise concerns for some commercial developers
- As with most high-level toolkits, flexibility is limited

The wxWidgets toolkit is another toolkit for building graphical user interfaces. It is a C++ framework for building native look-and-feel applications in a cross-platform way. It currently supports UNIX/Linux (X11), Windows, and OS X. Support for other platforms is in development.

More information about wxWidgets can be found at [http://www.wxwidgets.org](http://www.wxwidgets.org/).

Command line applications are a good first step in writing software for OS X. However, most OS X users tend to shy away from the command line (former UNIX and Linux users notwithstanding). For this reason, if you want your command line application to have mass appeal, you should consider wrapping it in a GUI interface.

OS X provides a number of methods for wrapping a command line application with a GUI interface. These include:

- `Do Shell Script` (AppleScript Studio)
- `NSTask` (Cocoa)

Each provides different capabilities for different purposes. This section points you to existing documentation on the topic and describes common issues that arise when wrapping a command line application with a GUI interface.

This section is primarily intended for open source developers, shareware/freeware developers, and in-house UNIX application developers, as these techniques do not offer the same level of functionality that you can get through tighter integration between the GUI and the underlying application.

If you just need to run a shell script by double-clicking it, and have no need for a GUI, you can simply rename the shell script to end with `.command` and it will open in Terminal automatically.

If you need more control over arguments but the command-line tool is non-interactive—that is, the GUI wrapper will merely start it and display the results—then either `NSTask` or `“Do Shell Script”` is acceptable, and you should use whichever one is most comfortable.

If the application needs to interact with the tool in any way, you should use the function `NSTask`. With it, you can chain arbitrary numbers of tasks using the `NSPipe` function.

Carbon, Cocoa, AppleScript, and other OS X development environments deal with files by using file references rather than referring to them by their path. As a result, you can move files anywhere on the disk and the file reference will still be valid even though the path has changed.

Using file references presents two problems for the developer. First, you have to explicitly convert them to POSIX paths to use them as the argument to a shell script. Second, the POSIX paths can contain spaces, so you must construct the command line carefully to prevent the script from failing if a directory name (or the name of your hard drive) contains a space.

Because of the potential side effects, you should always use the quoted form of the POSIX path when passing the path to a shell script. This is described in detail in _Technote #2065: Issuing Commands_.

The issue of spaces in pathnames is also a slight issue for Cocoa developers using the [NSTask](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/cl/NSTask) API, usually because of bugs in the shell script itself. (You do not need to escape strings passed as arguments using `NSTask`.)

You should always test any GUI-wrapped command-line application with filenames that contain spaces and other strange characters such as double quotes (“) and trademark (™) to make sure that there are no unexpected failures.

For more information on AppleScript’s `Do Shell Script` command, see _Technote #2065: Issuing Commands_, at [http://developer.apple.com/technotes/tn2002/tn2065.html](https://developer.apple.com/technotes/tn2002/tn2065.html) or the “simple sheet” example in AppleScript Studio.

For more information on Cocoa’s `NSTask` API, see _[Interacting with the Operating System](../../Cocoa/Interacting%20with%20the%20Operating%20System/Introduction%20to%20Interacting%20with%20the%20Operating%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tq2i)_.

[Next](Porting%20File%2C%20Device%2C%20and%20Network%20I-O.md)[Previous](Choosing%20a%20Graphical%20Environment%20for%20Your%20Application.md)

