---
title: JNISample
apple_id: DTS10000684
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/JNISample/Introduction/Intro.html
archived_at: '2026-07-18T03:13:09.793933Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ExampleDylib.c.md)

# JNISample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Please see MyFirstJNIProject Sample Code instead. |
| __Build Requirements:__ | Mac OS X, Project Builder |
| __Runtime Requirements:__ | Mac OS X, Project Builder |

This project is deprecated. Please see MyFirstJNIProject Sample Code instead.
A demonstration of a Java application built in ProjectBuilder that calls native code through JNI and calling a dylib from a JNI library. Changes since 2.0 Set install location for dylib. Changes since 1.2 Remove the GUI to make the example simpler Added Makefile to show how to build from the command line. Show how to call into a dylib from a JNI library. Changes since 1.1 Use the BUNDLE flag in the LIBRARY_STYLE build settings. Changes since 1.0 The doJavah Shell script that's run javah to create the jni header file (JNIOut.h) for JNIOut.c. This shell script is run in the "Shell Script Build Phase" of the JNIout Target. The "Copy Files Build Phase" of the JNISample target which copies the libJNIOut.jnilib into the JNISample.app bundle.

[Next](ExampleDylib.c.md)

