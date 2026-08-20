---
title: Getting Started with Mac OS X
apple_id: TP30001081
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-12-05'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_MacOSX/_index.html
archived_at: '2026-07-18T02:39:24.299679Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Technology Overview

Mac OS X provides a robust set of tools and technologies to aid you in creating full-featured applications in a short amount of time. The application environments of Mac OS X provide both object-oriented and procedural interfaces supporting development in industry-standard languages such as C, C++, Objective-C, and Java. Whether you have an existing code base or are starting from scratch, there are application environments to help you create full-featured applications quickly.

The documents in Mac OS X Documentation fall into two types: overviews and systemwide concept documents. The overview documents help orient you to the system and provide background information about the application environments and tools you can use to develop software. The systemwide concept documents provide conceptual information that is relevant to all developers, regardless of the application environment they use.

### Start Here

Developers who are new to Mac OS X are advised to spend a little time getting familiar with the conventions and architecture of the platform. To do so, you should read the following:

- The [Mac OS X topic page](https://developer.apple.com/macosx/) to become familiar with the latest developments in Mac OS X.
- [Mac Technology Overview](../../documentation/Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx) to get an overview of the Mac OS X architecture, software development opportunities, and the technologies available for you to use in your software.
- [What's New in macOS](../../releasenotes/Mac%20OSX/What%27s%20New%20in%20macOS/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmjs) for information on the latest features introduced in Mac OS X.

These documents are essential reading before you start writing any code.

### Choose a Learning Path

If you’re new to Mac OS X development, you want to become familiar with the tools and technologies available for application development. If you’re an existing developer, you may want to learn more about some systemwide concepts.

#### Learning About Application Technologies

Once you understand the basic structure of Mac OS X and its technologies, you can expand your knowledge by reading the high-level technology overviews. These overviews provide more depth and orient you toward how you could use that technology in your application.

- __If you prefer using object-oriented interfaces to develop software__, read [Cocoa Fundamentals Guide](../../documentation/Cocoa/Cocoa%20Fundamentals%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzu).
- __If you prefer using procedural interfaces to develop software__, read [Carbon Overview](../../documentation/Carbon/Carbon%20Overview/Introduction%20to%20Carbon%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojq).
- __If you’re a Java developer__, read [Java Development Guide for Mac](../../documentation/Java/Java%20Development%20Guide%20for%20Mac/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbs) for an overview of Java support.
- __If you’re a multimedia application developer__, read [QuickTime Overview](../../documentation/Quick%20Time/QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs) for information about integrating QuickTime into your applications.
- __If you’re a UNIX developer__, read [Porting UNIX/Linux Applications to OS X](../../documentation/Porting/Porting%20UNIX-Linux%20Applications%20to%20OS%20X/Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambt) for information on how to build UNIX applications on Mac OS X.
- __If you are familiar with AppleScript and want to use scripts to build a standalone application__, read [AppleScript Studio Programming Guide](../../documentation/Apple%20Script/AppleScript%20Studio%20Programming%20Guide/Introduction%20to%20AppleScript%20Studio%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqobz).
- __If you’re interested in future Mac OS X technologies__, become an ADC member to receive information about future Mac OS X releases; learn more at [http://developer.apple.com/membership/](https://developer.apple.com/membership/).

#### Learning About Apple Development Tools

Mac OS X provides a suite of developer tools, including design tools, analysis tools, packaging tools, compilers, and debuggers. The Xcode Tools CD contains all of the tools you need to get started developing software for Mac OS X. This CD is included with all shipping Macintosh computers and with retail copies of Mac OS X. The contents of the CD can also be downloaded from the ADC website ([http://connect.apple.com](http://connect.apple.com/)).

- __For an overview of the available tools and examples of how to use them__, read [Mac Technology Overview](../../documentation/Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx).
- __For information on how to create universal binaries using Xcode__, read [Universal Binary Programming Guidelines, Second Edition](../../documentation/Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx).
- __For information about using Xcode__, read [A Tour of Xcode](../../documentation/Developer%20Tools/A%20Tour%20of%20Xcode/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqojq).
- __For information about using command-line tools__, read Mac OS X Man Pages.

#### Learning More About Systemwide Concepts

Mac OS X includes many technologies that are not specific to a particular application environment. In the course of development, you may encounter these technologies and want to know more information about them.

- __If you’re unfamiliar with bundles__, read [Bundle Programming Guide](../../documentation/Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i) to understand the Mac OS X bundle mechanism and how it is used to distribute applications and other types of software.
- __If you want to create code libraries__, read [Framework Programming Guide](../../documentation/Mac%20OSX/Framework%20Programming%20Guide/Introduction%20to%20Framework%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dg2i) to learn about the framework mechanism and how it is used to distribute libraries on Mac OS X.
- __If your code uses shared system resources__, read [Multiple User Environment Programming Topics](../../documentation/Mac%20OSX/Multiple%20User%20Environment%20Programming%20Topics/Introduction%20to%20Multiple%20User%20Environments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4da2i) to learn how to protect your resources from accidental intrusion by users in other login sessions.
- __If you want guidelines on how to use and access the file system__, read [File System Overview](../../documentation/Mac%20OSX/File%20System%20Overview/Introduction%20to%20the%20File%20System%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dk2i).

### Next Steps

The [Mac OS X Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000471) includes the following high-level resource pages, which can be bookmarked for easy access:

- [Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP30000426)

  Apple’s developer documentation on Mac OS X.

