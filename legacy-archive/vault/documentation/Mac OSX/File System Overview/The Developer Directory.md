---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/DeveloperDirectory.html
archived_at: '2026-07-15T08:15:24.664505Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Overview](Introduction%20to%20the%20File%20System%20Overview.md)


[Next](Where%20to%20Put%20Application%20Files.md)[Previous](The%20Library%20Directory.md)

# The Developer Directory

The Xcode Tools CD contains the applications, tools, documentation, and other resources for developing Mac OS X software. Developers install these tools separately from the Mac OS X installation. When you install the tools, the installer places all of the software components in the `/Developer` directory of the boot volume. [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dgljrgaydsnzwfvbegskcjjduoqi) lists the contents of this directory.

__Table 1__  Subdirectories of the developer directory

| Directory | Contents |
| `ADC Reference Library` | Contains the locally installed documentation and links to additional resources available via the web. The pages in this directory offer easy navigation and consistent access to the complete ADC technical collection, including documentation, sample code, and other resources critical to Mac OS X development. |
| `Applications` | Contains the applications used to manage and build software projects. These tools include Xcode and Interface Builder for creating code and [interface](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34) files. It also includes a set of performance tools, Java tools, graphics tools, and general utilities. |
| `Documentation` | Contains additional developer-related documentation. |
| `Examples` | Contains example projects organized by general type. These are working projects that you can build and use to increase your knowledge of Mac OS X. |
| `Extras` | Contains optional files that you can install as needed for your development. |
| `Headers` | Contains special header files, such as the stub “flat” Carbon headers and headers for debugging remote applications. |
| `Java` | Contains files needed for Java bridging in the [Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) application environment. |
| `Makefiles` | Contains makefiles and jamfiles for building and converting legacy projects. |
| `Palettes` | Contains the Apple-supplied Interface Builder palettes. |
| `SDKs` | Contains the software development kits used to create software targeted specifically for previous versions of Mac OS X. Each SDK contains header files and stub libraries from a particular version of Mac OS X. |
| `Tools` | Contains command-line development tools and utilities, including those for creating and manipulating HFS resource forks. |

[Next](Where%20to%20Put%20Application%20Files.md)[Previous](The%20Library%20Directory.md)

