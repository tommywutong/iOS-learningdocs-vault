---
title: Java Development Guide for Mac
apple_id: TP30001142
resource_type: Guide
platform: Java
topic: Languages & Utilities
technology: null
published: '2010-10-20'
source_url: https://developer.apple.com/library/archive/documentation/Java/Conceptual/Java14Development/02-JavaDevTools/JavaDevTools.html
archived_at: '2026-07-15T07:44:37.954163Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Java Development Guide for Mac](Introduction.md)


[Next](Java%20Deployment%20Options%20for%20OS%20X.md)[Previous](Overview%20of%20Java%20for%20OS%20X.md)

# Apple Developer Tools for Java

This article provides a broad overview of recommended tools for Java development. It covers integrated development environments (IDEs) from other manufacturers, Apple’s own Xcode IDE, the Jar Bundler application, and methods for obtaining and viewing documentation.

The Java development tools in OS X are similar to the tools you find on other UNIX-based platforms. The command-line tools that Sun provides as part of the JDK for Linux and Solaris are ported for OS X and work just as they do on those platforms. There are only a few significant differences between the standard JDK tools in OS X and those found on other UNIX-based platforms:

- The installed location of the JDK command-line tools is different in OS X. These tools are installed with the rest of `JavaVM.framework` in `/System`. The Java tools provided in the default path in `/usr/bin/` will execute the version of Java the user has selected as their preferred version for applications in Java Preferences. For more on Java Preferences, see [Other Tools](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqobufuzdaobqgmyq). For more information on overall differences in where Java components are in OS X, see [Finding Your Way Around](Overview%20of%20Java%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqobtfuzdanjuha4q).
- `tools.jar` does not exist. Classes usually located here are instead included in `classes.jar`. Scripts that rely on the existence of `tools.jar` need to be rewritten accordingly.

Java development on any platform often benefits from the use of an Integrated Development Environment (IDE), which provides a more fluid workflow between writing, compiling, running, debugging, and packaging Java code than a simple text editor and the command line. Different IDEs offer unique features and are often suited for different kinds of Java development. These IDEs are industry leaders and offer substantial support for OS X:

- Eclipse IDE for Java Developers ([http://www.eclipse.org](http://www.eclipse.org/)) is a free download.
- Netbeans IDE ([http://www.netbeans.org](http://www.netbeans.org/)) is a free download.
- Jetbrains IntelliJ IDEA ([http://www.jetbrains.com/idea/](http://www.jetbrains.com/idea/)) requires a license for continued use after a trial period.
- Xcode ([http://developer.apple.com/tools/xcode/](https://developer.apple.com/tools/xcode/)) is a free download with a free account from the Apple Developer Connection.

If you are developing a JNI library or intend to have your application communicate with Cocoa, you should plan to use the Xcode Tools for those portions of your development. For more information on JNI development, see [JNI](Core%20Java%20APIs%20and%20the%20Java%20Runtime%20on%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmbsfuzdcmbxhaya).

Apple provides a full suite of general developer tools with OS X. This suite of tools, the Xcode Tools, is free but not installed by default. The tools are available for download at the Apple Developer Connection (ADC) Member Site [http://connect.apple.com/](http://connect.apple.com/). If you do not have an ADC membership, you can enroll for various levels of membership, including a free online membership that allows you access to the member site, at [http://developer.apple.com/products/](https://developer.apple.com/products/).

Apple frequently releases updates to the OS X Developer Tools. Even if you already have the Xcode Tools installed, you should check the Member Site for the most up-to-date version.

With the Xcode Tools, you have a full-featured development environment including:

- Command-line tools, installed in `/Developer/Tools/`
- Graphical tools, installed in `/Developer/Applications/`
- Sample code, installed in `/Developer/Extras/Java/`

The core component of the OS X development environment is Xcode. Xcode is a complete IDE that allows you to edit, compile, debug, and package Mac apps written in multiple languages. Even if you do not intend to use it for your primary Java development, it is helpful to become familiar with Xcode. Downloadable [sample code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30000425) and the sample code installed in `/Developer/Extras/Java/` are both usually provided as Xcode projects. Additionally, there are some elements of documentation viewing that are available only through Xcode.

For more on using Xcode for Java development, see the Xcode Help menu.

Xcode helps you manage Java applications with the Organizer. You can open it by choosing Organizer from the Window menu. Figure 1 shows the Organizer window.

__Figure 1__  The Xcode Organizer

!

The Organizer shows your project exactly as it is laid out in the file system. This is in contrast to the main Xcode project windows, which allow you to arrange files arbitrarily without altering their location on disk. The Organizer’s direct reflection of the file system better serves Java development and is similar to other Java IDEs.

To create a new Java project in Xcode, choose New From Template from the New menu in the bottom-left corner of the Organizer.

Xcode uses Apache Ant to compile and run Java applications. You can customize your build settings by modifying the `build.xml` file that is automatically generated when you create a new Java project. By default, the `source` and `target` compiler flags in `build.xml` are set to `1.3` and `1.2`, respectively. This is to ensure compatibility with as many Java versions as possible. Raise these default values to take advantage of APIs and features, such as assertions and generics, that are available only with later versions of Java.

Jar Bundler is an application that takes Java applications deployed as standalone Jar files and turns them into applications that can be launched just like native Mac apps. Although the Terminal application is a part of every installation of OS X, many OS X users never use it. To prevent your users from having to use Terminal for your Java applications, you should wrap your application as an OS X application bundle (see [OS X Application Bundles](Java%20Deployment%20Options%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqobvfuzdaobugq3q)). Jar Bundler allows you to do this very easily. It also provides a simple interface for you to set system properties that make your applications perform their best in OS X.

Jar Bundler is available in `/Developer/Applications/Utilities/`. More information on Jar Bundler is available in _[Jar Bundler User Guide](../Jar%20Bundler%20User%20Guide/Introduction%20to%20Jar%20Bundler%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqobu)_.

Applet Launcher (in `/Developer/Applications/Utilities/`) provides a graphical interface to Sun’s Java Plug-in. Applet Launcher loads an applet from an HTML page. For example, entering the following URL launches the ArcTest applet:

`file:///Developer/Extras/Java/Applets/ArcTest/example1.html`

Applet Launcher is useful for testing your applets in OS X. Performance and behavior settings for applets may be adjusted in the Java Preferences application installed in `/Applications/Utilities/`.

In addition to containing Xcode and Jar Bundler, `/Developer/Applications/Utilities/` contains some applications that you can use for Java development though they are not Java-specific:

- Package Maker helps you create an installer PKG for your application.
- File Merge provides a graphical interface for comparing and merging source files.
- Icon Composer helps you create an ICNS file for your application bundle.

Additional development tools for Java and other languages can be found in `/usr/share/`. Of particular use for Java development are:

- JUnit, a common Java unit-testing framework.
- Apache Ant, a tool for automating builds. The Ant executable can also be found in `/usr/bin/`.
- Apache Maven, a tool for consolidating multiple elements of development, including dependency management and release management.
- Derby, a lightweight database.

Documentation for Java development in OS X is provided both online and as a download from Apple Developer Connection. The most current version of the documentation is available from the Java Reference Library on the Apple Developer Connection website. A snapshot of this documentation is also installed on your computer when you install the Java documentation package. This documentation is easily accessible in Xcode by selecting Documentation from the Help menu. Man pages for the command-line tools are accessible from the command line `man` program and through the Xcode Help menu.

Sun’s Java SE 6 API documentation is available in `/System/Library/Frameworks/JavaVM.framework/Versions/1.6.0/Home/docs.jar`. Documentation for Apple’s Java extensions is available in `appledocs.jar` in the same directory.

Note that Apple does not attempt to provide a full Java documentation suite online or with the Xcode Tools. Sun supplies very thorough documentation available online at [http://java.sun.com/reference/docs/](http://java.sun.com/reference/docs/). Apple’s documentation only aims to augment Sun’s documentation for Java development issues specific to OS X and to document OS X–specific features of Java. Your primary source for Java platform documentation is [Sun’s Java documentation website](http://java.sun.com/).

If you find errors in the Java documentation or would like to request either feature or content enhancements, you can file bugs at [http://bugreport.apple.com/](http://bugreport.apple.com/). When filing documentation bugs on Java documentation in OS X, please select `Java` from the product field and enter `X` in the Version/Build Number field.

[Next](Java%20Deployment%20Options%20for%20OS%20X.md)[Previous](Overview%20of%20Java%20for%20OS%20X.md)

