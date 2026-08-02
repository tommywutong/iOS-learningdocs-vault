---
title: Java 1.3.1 Development for Mac OS X
apple_id: TP40000885
resource_type: Guide
platform: Java
topic: Cross Platform
technology: null
published: '2002-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Java/Conceptual/Java131Development/about/about.html
archived_at: '2026-07-15T07:44:29.298438Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](How%20Java%20Is%20Implemented%20in%20Mac%20OS%20X.md)

# About This Book

With Mac OS X, Apple delivers a Java implementation that adds value for both developers and end users. Java is fully integrated into Mac OS X, which offers developers easy access to the Aqua user interface, UNIX-based tools and technologies, QuickTime, OpenGL, and Cocoa. This built-in flexibility allows developers to create robust, well-designed applications that offer users a wide range of rich features and functionality.

This book provides an overview of Java development on Mac OS X and discusses the available features. It also provides simple examples on using the development tools available with Mac OS X.

This book is for the Java developer interested in writing Java applications on Mac OS X version 10.2 with Java 2 Standard Edition (J2SE) version 1.3.1. It does not discuss Java 2 Standard Edition version 1.4 on Mac OS X. Information on previous versions of Java on Mac OS X can be found in the Release Notes at [http://developer.apple.com/documentation/java](https://developer.apple.com/documentation/java). It is primarily geared toward developers of pure Java applications, but it will also be useful for Cocoa Java development and WebObjects Java development.

This is not a tutorial for the Java language. If you are not already proficient in Java, this document will still be helpful to you but it will not teach you about the Java language and J2SE packages. Many resources exist in print and on the Web for learning the Java programming language. If you are new to programming in Java, you may want to start with one of Sun’s tutorials available online at [http://developer.java.sun.com/developer/onlineTraining/new2java/](http://developer.java.sun.com/developer/onlineTraining/new2java/).

Overall, the purpose is document to highlight how Java development in Mac OS X may be different if you are accustomed to Java development on other platforms. It does not attempt to present a conclusive overview of Java itself. It is meant as a supplemental guide to help you save time and development effort. It introduces you to the tools available to you, discusses some details of how Java is implemented, points out potential trouble spots, and provides some reference documentation.

This book has information for many different types of Java developers. To help you determine what information is important for you the following listing provides an overview of the contents of the following chapters:

- [How Java Is Implemented in Mac OS X](How%20Java%20Is%20Implemented%20in%20Mac%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombvfvkfawcsivddcmbr) Presents a broad overview of how Java works in Mac OS X. It also highlights some areas where things differ between Java in Mac OS X and other platforms. This chapter has many important details for anyone doing Java development on Mac OS X. It is a good place to begin if you don’t have specific questions, but want an overview of what is available.
- [Deployment Options](Deployment%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombwfvbegskhjjbesri) Reveals the four suggested deployment vehicles for your Java applications on the Mac OS X operating system. If you have a Java application that you want to distribute on Mac OS X, this chapter is important reading. It discusses not only details to be aware of in the standard distribution methods, but also presents some unique to Mac OS X.
- [The Development Environment](The%20Development%20Environment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombxfvkfawcsivddcmbr) If you are new to Java development on Mac OS X, this chapter provides important background information on what tools are available to you.
- [Cross-Platform Practices for Great Native Behavior](Cross-Platform%20Practices%20for%20Great%20Native%20Behavior.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombyfvbegskki5demri) Discusses some considerations you should make while designing your applications so that they will behave just as well on Mac OS X as they do on other platforms.
- [Using Native Features of Mac OS X in Java Applications](Using%20Native%20Features%20of%20Mac%20OS%20X%20in%20Java%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombzfvkfawcsivddcmbr) Explores some of the options available to you in Mac OS X that are not available on other platforms. Some things discussed in this chapter will tie your application to Mac OS X specifically, while other things will help you to add value to your Java applications on Mac OS X without affecting your application’s cross-platform compatibility. The information in this chapter may be important if you are designing a new application or modifying an existing one.
- [Project Builder Tutorial](Project%20Builder%20Tutorial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomjqfvkfawcsivddcmbr) If you want to take advantage of the free Project Builder IDE for you Java development, this is a useful place to start.
- [MRJAppBuilder Tutorial](MRJAppBuilder%20Tutorial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomjrfvkfawcsivddcmbr) This is a tutorial for anyone distributing a Java application on Mac OS X.
- [Mac OS X Java System Properties](Mac%20OS%20X%20Java%20System%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomjsfvkfami) Provides a listing of the common Java system properties useful in Mac OS X.

This document and other Java documentation for Mac OS X, including the javadoc API reference, is available online at [http://developer.apple.com/documentation/java](https://developer.apple.com/documentation/java). A subset of this documentation is installed in  `/Developer/Documentation/Mac OS X/Java` on a Mac OS X system with the Mac OS X Developer Tools. You can view this documentation through a Web Browser or through Project Builder (from Project Builder’s Help menu, choose Developer Help Center).

The main Java technology page [http://developer.apple.com/java](https://developer.apple.com/java) contains many links to information about Java development in Mac OS X.

The `java-dev` mailing list is a great source of information on a wide range of Java development topics in Mac OS X. You can sign up for this list at [http://lists.apple.com](http://lists.apple.com/).

Sun’s Java site, [http://java.sun.com](http://java.sun.com/) is the essential reference point for Java development in general.

If you find issues with the implementation of Java that are not represented in this document or want to follow the resolution of an issue, you may do so online through Radar, Apple’s bug tracking system. To access Radar, you will need an Apple Developer Connection (ADC) account. You can view the ADC membership options, including the free online membership at, [http://developer.apple.com/membership/index.html](https://developer.apple.com/membership/index.html). With an ADC membership, you can file and view bugs at [http://bugreport.apple.com](http://bugreport.apple.com/). When filing new bugs for Java on Mac OS X, please use Java (new bugs) for the Component and X as the Version.

[Next](How%20Java%20Is%20Implemented%20in%20Mac%20OS%20X.md)

