---
title: Porting UNIX/Linux Applications to OS X
apple_id: TP30001003
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Porting/Conceptual/PortingUnix/glossary/glossary.html
archived_at: '2026-07-18T01:50:46.957261Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting UNIX/Linux Applications to OS X](Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md)


[Next](Document%20Revision%20History.md)[Previous](%28Re%29designing%20for%20Portability.md)

# Glossary

- __ADC__

  See [Apple Developer Connection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjzfvbuuqskijfeoqq)

- __Apple Developer Connection__

  The primary source for technical and business resources and information for anyone developing for Apple's software and hardware platforms anywhere in the world. It includes programs, products, and services and a website filled with up-to-date technical documentation for existing and emerging Apple technologies. The Apple Developer Connection is at [http://www.apple.com/developer/](http://www.apple.com/developer/).

- __Aqua__

  The graphical user interface for OS X.

- __bom (Bill Of Materials)__

  A file in an installer package used by the Installer to determine which files to install, remove, or upgrade. It contains all the files within a directory, along with information about each file such as the file's permissions, its owner and group, size, its time of last modification, a checksum for each file, and information about hard links.

- __bundle__

  A directory in the file system that stores executable code and the software resources related to that code. Applications, plug-ins, and frameworks are types of bundles. Except for frameworks, bundles are file packages, presented by the Finder as a single file.

- __Carbon__

  An application environment for OS X that features a set of programming interfaces derived from earlier versions of the Mac OS. The Carbon API has been modified to work properly with OS X, especially with the foundation of the operating system, the kernel environment. Carbon applications can run in OS X, Mac OS 9, and all versions of Mac OS 8 later than Mac OS 8.1.

- __Classic__

  An application environment for OS X that lets you run non-Carbon legacy Mac OS software. It supports programs built for both Power PC and 68K chip architectures and is fully integrated with the Finder and the other application environments.

- __Cocoa__

  An advanced object-oriented development platform for OS X. Cocoa is a set of frameworks with programming interfaces in both Java and Objective-C. It is based on the integration of OPENSTEP, Apple technologies, and Java.

- __Darwin__

  Another name for the core of the OS X operating system. The Darwin kernel is equivalent to the OS X kernel plus the BSD libraries and commands essential to the BSD command-line environment. Darwin is open source technology.

- __.dmg file__

  An OS X disk image file.

- __Finder__

  The system application that acts as the primary user interface for file-system interaction.

- __HFS (Hierarchical File System)__

  The Mac OS Standard file-system format, used to represent a collection of files as a hierarchy of directories (folders), each of which may contain either files or folders themselves. HFS is a two-fork volume format.

- __HFS+__

  The Mac OS Extended file-system format. This file-system format was introduced as part of Mac OS 8.1, adding support for filenames longer than 31 characters, Unicode representation of file and directory names, and efficient operation on very large disks. HFS+ is a multiple-fork volume format.

- __Mach-O__

  The executable format of Mach object files. This is the default executable format in OS X.

- __NetInfo__

  The network administrative information database and information retrieval system for OS X. Many OS X services consult the NetInfo database for their configuration information.

- __nib file__

  An XML archive that describes the user interface of applications built with Interface Builder.

- __`.pkg` file__

  An OS X Installer file. May be grouped together into a metapackage (`.mpkg`).

- __plist__

  See [property list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjzfvbuuqsiifbuksa).

- __property list__

  A structured, textual representation of data that uses the Extensible Markup Language (XML) as the structuring medium. Elements of a property list represent data of certain types, such as arrays, dictionaries, and strings.

- __Xcode__

  Apple’s graphical integrated development environment. It is available free with the OS X Developer Tools package.

- __XNU__

  The OS X kernel. The acronym stands for X is Not Unix. XNU combines the functionality of Mach and BSD with the I/O Kit, the driver model for OS X.

[Next](Document%20Revision%20History.md)[Previous](%28Re%29designing%20for%20Portability.md)

