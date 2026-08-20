---
title: Jar Bundler User Guide
apple_id: TP40000884
resource_type: Guide
platform: Java
topic: Languages & Utilities
technology: null
published: '2009-12-01'
source_url: https://developer.apple.com/library/archive/documentation/Java/Conceptual/Jar_Bundler/Introduction/Introduction.html
archived_at: '2026-07-15T07:44:17.751700Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Jar%20Bundler.md)

# Introduction to Jar Bundler User Guide

This document covers the packaging of existing Java applications into Mac app bundles using Jar Bundler.

You should read this document if you have working Java 1.3.1, Java 1.4.2, and J2SE 5.0 applications that you want to deploy as Mac apps. That is, you want your application’s users to double-click an application package with a nice-looking icon instead of a JAR file with a generic JAR-file icon.

This document is intended for developers as well as regular users. For example, you may be a developer that has several Java applications happily running on several platforms. However, you might want OS X users to enjoy using your applications with the niceties their platform of choice provides, such as the easy-to-use Macintosh menu bar, and straightforward application installation and uninstallation. Or you may be a regular OS X user who wants to take advantage of the myriad of Java-based applications available but want to package them so that you can manage them better.

Or you may be both. Whatever the case is, this document shows you how to group several files containing Java code, and C code in the form of Java Native Interface (JNI) libraries, into a self-contained application package. You also learn how to change the application’s normal behavior so that it provides a familiar interface to OS X users.

This document has the following chapters:

- [About Jar Bundler](About%20Jar%20Bundler.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqobufvbuqmrqgiwueqkkineugqkb) provides an overview of Jar Bundler’s user interface.
- [Application Packaging](Application%20Packaging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqobufvbuqmrqgmwueqkcjjducrcg) guides you through the creation of an OS X application package using Jar Bundler.

This document also contains a revision history.

There are companion files intended to be used while reading this document. You find them in `/Developer/ADC Reference Library/documentation/Java/Conceptual/Jar_Bundler/Jar_Bundler_companion.dmg`. That volume is called `Jar_Bundler_companion` in the remainder of this document. You can also download the companion files from [http://developer.apple.com/java/](https://developer.apple.com/java/).

For detailed information on application packaging, see _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_ and _[Framework Programming Guide](../../Mac%20OSX/Framework%20Programming%20Guide/Introduction%20to%20Framework%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dg2i)_.

For information on Java development in OS X, visit [http://developer.apple.com/java/](https://developer.apple.com/java/).

This product includes software developed by the SpeedLegal Group for use in the Xerlin XML Editor www.xerlin.org and software developed by ChannelPoint, Inc. for use in the Merlot XML Editor [http://www.merlotxml.org/](http://www.merlotxml.org/).

The Xerlin XML Editor is Copyright © 2002 SpeedLegal Holdings, Inc. and other contributors. It includes software developed for the Merlot XML Editor which is Copyright © 1999-2000 ChannelPoint, Inc. All rights reserved.

[Next](About%20Jar%20Bundler.md)

