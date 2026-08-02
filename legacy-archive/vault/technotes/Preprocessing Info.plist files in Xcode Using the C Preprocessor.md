---
title: Preprocessing Info.plist files in Xcode Using the C Preprocessor
apple_id: DTS10004415
resource_type: Technical Note
platform: macOS
topic: Languages & Utilities
technology: null
published: '2010-05-07'
source_url: https://developer.apple.com/library/archive/technotes/tn2175/_index.html
archived_at: '2026-07-26T19:54:09.178699Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2175

# Preprocessing Info.plist files in Xcode Using the C Preprocessor

This document provides solutions to several challenges faced when preprocessing Info.plist files with the GCC C preprocessor in Xcode. It details how to keep URLs from being converted to comments, how to format strings to preserve whitespace in <string> properties and a successful technique to handle macro expansion.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbrguwugsbrfvke4vcbi4yq)[Preserving whitespace within strings defined in an Info.plist file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbrguwugsbrfvke4vcbi4za)[Preventing URLs from being converted to comments and discarded](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbrguwugsbrfvke4vcbi4zq)[Eliminating whitespace between tokens in the macro expansion process](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbrguwugsbrfvke4vcbi42a)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbrguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

There are several well-known challenges faced by the development community using the GCC C preprocessor to preprocess their property list (`Info.plist`) files in Xcode. Some developers have faced issues with the whitespace in their user-defined strings being compressed after preprocessing. Others faced problems concerning URLs being turned into comments and discarded, or being unable to successfully expand user-defined macros in reference to the `Info.plist` files. This document will present workarounds for each of these issues.

[Back to Top](#)

## Preserving whitespace within strings defined in an Info.plist file

In Xcode a `<string>` property in an `Info.plist file` will have any embedded runs of spaces converted to a single space when the plist is copied to the built product. This is an issue when string properties are used in cases where strings are compared for matching purposes.

This problem is often seen in device driver development. For example, the IOSCSIPeripheralDeviceNub for a particular drive model has the property "Product Identification" with the value

```
 "DVD-R   TLF-313"
```

- there are three consecutive spaces in this value. By default, if that key/value pair is placed in the `Info.plist` of a device driver, the value in the built KEXT is changed to

```
"DVD-R TLF-313"
```

- where the three consecutive spaces have been compressed into a single space. As a result, the property in the `Info.plist` does not match the device and the driver silently fails to start.

To preserve the whitespace within the `<string>` property, replace the space characters inside the string with the XML character reference `&#x20;`. In the device driver example, the `Info.plist` would contain the property:

```
<string>DVD-R &#x20;&#x20;&#x20;TLF-313</string>
```

[Back to Top](#)

## Preventing URLs from being converted to comments and discarded

Using the GCC C preprocessor to preprocess your `Info.plist` files may have some unintended side-effects. Such as using URLs in your file. That is, the C preprocessor treats the text in the same way it would treat source code - anything following "//" characters are treated as comments and discarded. Therefore, a `<string>` property that is originally represented as this:

```
<string>http://developer.apple.com</string>
```

will get converted into this:

```
<string>http:
```

To work around this feature of the C preprocessor, we can pass the `-traditional` flag to the `Info.plist Other Preprocessor Flags` build setting in Xcode. This will cause the preprocessor to use the traditional ANSI C `/*` and  `*/` character strings as tokens to recognize and discard text as comments.

[Back to Top](#)

## Eliminating whitespace between tokens in the macro expansion process

Many developers wish to use macros to represent specific things about their software in the `Info.plist` file. One such usage is to represent the values for the major, minor and maintenance versions of their software. For example:

```
#define MAJORVERSION 2 #define MINORVERSION 4 #define MAINTVERSION 6
```

placed in the Info.plist prefix header with a corresponding `Info.plist` file containing:

```
<key>CFBundleShortVersionString</key> <string>MAJORVERSION.MINORVERSION.MAINTVERSION</string>
```

will cause the string `"1 . 2 . 3"` to appear in the `About` window of the application. The spaces between the numbers in the macro expansion process can be avoided by passing `-traditional` to the `Info.plist Other Preprocessor Flags` build setting.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-05-07 | Fixed typo. Pass the "-traditional" flag rather than the "-CC" flag to eliminate whitespace between tokens in the macro expansion process. |
| 2007-08-14 | New document that describes workarounds for several issues concerning preprocessing Info.plist files in Xcode with the C preprocessor. |

