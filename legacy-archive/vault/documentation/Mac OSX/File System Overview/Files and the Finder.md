---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/FilesAndFinder.html
archived_at: '2026-07-15T08:15:27.638237Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Overview](Introduction%20to%20the%20File%20System%20Overview.md)


[Next](Sorting%20Rules.md)[Previous](Where%20to%20Put%20Application%20Files.md)

# Files and the Finder

The Finder is how most users interact with files in Mac OS X. It is in the best interest of developers to understand these interactions and make sure their software does not behave in an unexpected way.

Mac OS X supports several different types of file systems natively in the Finder. The most common formats are HFS+ (Mac OS Extended), HFS (Mac OS Standard), and UFS. Other file formats include the Universal Disk Format (UDF) for DVD disks and the ISO 9660 format used for CD-ROM volumes. Each of these file systems implements file storage in slightly different ways, but the Finder masks these differences to provide a seamless user experience.

Copy and move operations in which the source and destination use the same volume format occur much as you might expect, with the file information appearing at the destination. Things get interesting when files are copied or moved across volumes that support different volume formats.

What happens when a user copies a file from an HFS+ volume to a UFS volume? The file on the HFS+ volume includes additional information, such as the file type and creator codes. It may also include a resource fork, a concept that is not supported by UFS files. When such an operation occurs, the Finder splits out any information that is not located in the data fork of the file and writes it to a hidden file on the destination volume. The name of this file is the same as the original file except that it has a “dot-underscore” prefix. For example, if you copy an HFS+ file named `MyMug.jpg` to a UFS volume, there will be a file named `._MyMug.jpg` in addition to the `MyMug.jpg` file in the same location.

When copying a file from a UFS volume to an HFS or HFS+ volume, the Finder looks for a matching “dot-underscore” file. If one exists, the Finder creates an HFS+ (or HFS) file, using the information in the dot-underscore file to recreate the resource fork and Finder attributes. If the hidden file does not exist, these attributes are not recreated.

Note that the Finder accomplishes these operations through the Carbon API on which it is based.

HFS (Mac OS Standard) and HFS+ (Mac OS Extended) file systems include the file-system entity known as an alias. An alias bears some similarities to a symbolic link in a UFS file system, but the differences are significant. See [Aliases and Symbolic Links](Aliases%20and%20Symbolic%20Links.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dqlkciffeerkiizba) for a description of these differences.

How the Finder manages a file-system world in which both aliases and symbolic links coexist is simple. It recognizes symbolic links but creates only aliases (when given the appropriate menu command). Even when it encounters a symbolic link in the file system, it presents it as an alias—that is, there is no visual differentiation between the two. The only way to make a symbolic link in Mac OS X is to use the BSD command `ln -s` from a Terminal window or shell script. 

When the Finder displays a file or folder, it takes great care in making sure that what it displays is what the user expects to see. The user may have several applications on the system capable of handling a given document type. The user may also manipulate file names individually or as a whole through language preferences or filename extension hiding. All of these options are handled automatically by the Finder.

The Finder uses several pieces of information to determine an appropriate icon for a file or folder. The file’s bundle bit, type code, creator code, and filename extension all help determine the icon. User settings also play a role. The following steps explain the process used to choose icons for files and directory:

1. The Finder checks to see if an item is a file or a directory. If it is a file, it asks Launch Services for an appropriate icon and displays the icon.
2. For directories, the Finder checks to see if it is a [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4).

   The bundle bit or file extension can indicate that the directory is a bundle and should be displayed as an opaque entity. Most bundles are displayed as opaque entities but some, including [frameworks](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56), are not.
3. If the bundled directory has the extension `.app` in its filename, the Finder hides that extension.
4. For a bundled directory, the Finder looks up the type code, creator code, and filename extension in the Launch Services database and uses that information to locate the appropriate custom icon.
5. If no custom icon is available for either a file or directory, the Finder displays the default icon appropriate for the given item type.

   The default icon can differ based on whether the item is a document, unbundled directory, application, plug-in, or generic bundle, among others.

Two additional features that affect the way the Finder presents files to the user are filename extension hiding and filename localization. These features are cosmetic additions to the Aqua interface that alter the displayed name of a file without changing the actual name of the file in the file system. The Finder uses routines provided by Launch Services to obtain a _display name_ for each file or folder. A display name takes into account user-specified options and returns a read-only name suitable for display from a user interface.

If your application displays file or folder names, you also need to be aware of display names and use them wherever you would otherwise display a file or folder name. Both [Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) and Launch Services provide interfaces for obtaining display names. For more information, see [Display Names](Display%20Names.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4tqlkdjjbeqskiizda).

The Finder relies on Launch Services to launch applications and manage the bindings between applications and documents. If you need to perform operations that involve opening unknown document types, following URLs in a document, launching helper applications, or opening embedded document components, you should investigate the Launch Services API. Among the tasks handled by Launch Services are the following:

- Launch another application
- Open a document or URL in another application
- Identify the preferred application for opening a document or URL
- Register information about the kinds of files and URLS an application is capable of opening
- Obtain the icon, display name, or kind string of a file or URL
- Maintain and update the contents of the Recent Items menu.

For information about Launch Services, including how you can use it in your own applications, see _[Launch Services Programming Guide](../../Carbon/Launch%20Services%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojz)_.

[Next](Sorting%20Rules.md)[Previous](Where%20to%20Put%20Application%20Files.md)

