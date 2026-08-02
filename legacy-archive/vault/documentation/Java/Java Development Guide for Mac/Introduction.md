---
title: Java Development Guide for Mac
apple_id: TP30001142
resource_type: Guide
platform: Java
topic: Languages & Utilities
technology: null
published: '2010-10-20'
source_url: https://developer.apple.com/library/archive/documentation/Java/Conceptual/Java14Development/00-Intro/JavaDevelopment.html
archived_at: '2026-07-15T07:44:37.194322Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20Java%20for%20OS%20X.md)

# Introduction

The Java Platform, Standard Edition for OS X provides a Java environment that is highly integrated with OS X. This integration brings together the Java platform’s versatility and OS X’s advanced technologies to offer users a wider selection of applications and developers a first-class development and deployment platform.

OS X version 10.6 includes both 32-bit and 64-bit versions of Java SE 6 out of the box. This opens up the entire Mac user base to Java application and applet developers, and conversely, the world of Java applications to OS X users.

While Java's promise of “write once, run anywhere” is true on OS X, there are a number of things you should do to ensure that your application's user experience adheres to conventions and behaviors that Mac users have come to expect from their applications. This document seeks to highlight these methods so you can spend your time writing applications instead of troubleshooting.

This document is for the Java developer interested in writing Java applications in OS X v10.6 with Java SE 6. This document is primarily for developers of pure Java applications.

This is not a tutorial for the Java language. This document assumes you have a basic understanding of Java development and Java development environments. Many resources exist in print and on the web for learning the Java programming language. If you are new to programming in Java, you may want to start with one of Sun’s tutorials available online at [http://java.sun.com/learning/new2java/](http://java.sun.com/learning/new2java/).

This guide contains the following articles:

- [Overview of Java for OS X](Overview%20of%20Java%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqobtfvjvomi) describes the Java platforms available on OS X.
- [Apple Developer Tools for Java](Apple%20Developer%20Tools%20for%20Java.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqobufvjvomi) introduces you to the Apple suite of developer tools, along with recommended tools from other manufacturers.
- [Java Deployment Options for OS X](Java%20Deployment%20Options%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqobvfvjvomi) discusses how you can distribute your Java application on OS X.
- [OS X Integration for Java](OS%20X%20Integration%20for%20Java.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmbzfvjvomi) provides you with some handy tips for making your Java application act and feel more like a native Mac app.
- [User Interface Toolkits for Java](User%20Interface%20Toolkits%20for%20Java.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmbrfvjvomi) shows you the different user interface elements common in OS X.
- [Core Java APIs and the Java Runtime on OS X](Core%20Java%20APIs%20and%20the%20Java%20Runtime%20on%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmbsfvjvomi) discusses the how core Java APIs vary on OS X.

General information about OS X, including more on many of the topics discussed in this document can be found in _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.

Answers to frequently asked questions about Java for OS X are addressed in the [Java FAQ](https://developer.apple.com/java/faq/).

General information on previous versions of Java for OS X can be found in the [Release Notes > Java](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000872-TP30000425).

This document and other Java documentation for OS X, including the Javadoc API reference, are available in the [Java Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000425). A subset of this documentation is installed in `/Developer/Documentation/DocSets/` on an OS X system with the OS X Developer Tools. You can view this documentation through a web browser or through Xcode (from Xcode’s Help menu, choose _Documentation_ and then click _Java_).

The main Apple website for Java technology, [http://developer.apple.com/java/](https://developer.apple.com/java/), contains links to information about Java development in OS X.

The `java-dev` mailing list is a great source of information on a wide range of Java development topics in OS X. You can sign up for this list at [http://lists.apple.com/](http://lists.apple.com/).

Sun’s Java website, [http://java.sun.com/](http://java.sun.com/) is the essential reference point for Java development in general.

If you find issues with the implementation of Java that are not covered in this document or you want to follow the resolution of an issue, you may do so online through Radar, Apple’s bug tracking system. To access Radar, you need an Apple Developer Connection (ADC) account. You can view the ADC membership options, including the free online membership, at [http://developer.apple.com/membership/](https://developer.apple.com/membership/). With an ADC membership, you can file and view bugs at [http://bugreport.apple.com/](http://bugreport.apple.com/). When filing new bugs for Java in OS X, please select `Java` from the Product field and enter `X` in the Version/Build Number field.

[Next](Overview%20of%20Java%20for%20OS%20X.md)

