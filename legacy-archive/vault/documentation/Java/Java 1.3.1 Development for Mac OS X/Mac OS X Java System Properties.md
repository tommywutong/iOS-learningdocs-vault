---
title: Java 1.3.1 Development for Mac OS X
apple_id: TP40000885
resource_type: Guide
platform: Java
topic: Cross Platform
technology: null
published: '2002-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Java/Conceptual/Java131Development/system_properties/system_properties.html
archived_at: '2026-07-15T07:44:32.795719Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Java 1.3.1 Development for Mac OS X](About%20This%20Book.md)


[Next](Document%20Revision%20History.md)[Previous](MRJAppBuilder%20Tutorial.md)

# Mac OS X Java System Properties

This appendix lists the Mac OS X–specific system properties that you should be aware of.

You can use `System.getProperties().list(System.out)` to obtain a complete list of system properties. The most useful ones are included here, as well as brief descriptions.

The properties in [Table C-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomjsfvkfawcsivddcmbs) all return a value of type `String`. They can be used in this manner:

```
if (System.getProperty("os.version").equals("10.2"))
 System.out.println("Mac OS X version 10.2 Jaguar");
```


__Table C-1__  JVM properties

| Property | Value | Notes |
| `java.version` | 1.3.1 |  |
| `java.vm.version` | 1.3.1_03-69 |  |
| `line.separator` | ‘\n’ | This differs from MRJ in Mac OS 9, which used `\r`, but is consistent with UNIX-based Java implementations and with the BSD and Cocoa frameworks. |
| `mrj.version` | 3.3 | Testing for the existence of this property is the general way to detect whether you are using an Apple-developed JVM. To detect specific features like JDirect or MRJToolkit, it is better to use reflection to check for the existence of the specific classes they use. |
| `os.name` | Mac OS X | This value was `Darwin` in developmental versions of Mac OS X. The MRJ on Mac OS 9 used `Mac OS`. It is suggested that you use `System.getProperty("os.name").startsWith("Mac OS")` if you need to test whether your code is running on any version of Mac OS. |
| `os.version` | 10.2 | This is the version number available in the About This Mac dialog. Developmental versions of Java on Mac OS X used the Darwin kernel number (1.1, 1.2, and so forth) |

It is simple to wrap your pure Java application inside of a natively executable Mac OS X application bundle. This is discussed in [Mac OS X Java Applications](Deployment%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombwfvkfawcsivddcmbs). In so doing, there are two properties that must be defined. These are listed in [Table C-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomjsfvkfawcsivddcmbt). If you are using Project Builder or MRJAppBuilder, you do not need to do anything to define them since both of those applications take care of this for you.

__Table C-2__  required Mac OS X application properties

| Property | `Info.plist` key | Description |
| `com.apple.mrj.application.main` | `MainClass` | The fully qualified class name of the class containing the application’s `main` method. |
| `com.apple.mrj.application.classpath` | `ClassPath` | The paths of all required directories or JAR files. |

In addition, you can pass in the options listed in [Table C-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomjsfvkfawcsivddcmbu).

__Table C-3__  Application launch properties

| Property | Info.plist Key | Description |
| `com.apple.mrj.application.parameters` | `Arguments` | Space-separated list of arguments that are parsed to build the `String[]` passed to `main`. |
| `com.apple.mrj.application.workingdirectory` | `WorkingDirectory` | Sets the current working directory for the application. By default the current working directory is set to the parent directory of the application bundle. The `APP_PACKAGE` variable may be used to refer to the root of the application bundle. |
| `com.apple.mrj.application.vm.options` | `VMOptions` | Space-separated list of options for the Java virtual machine. These are the `-X` and `-XX` options without the `-X(X)` prefix. |

Note the following about these properties:

- None of these properties are set by default.
- If you are adding properties to an `Info.plist`, they should go into the Java dictionary.
- When adding properties to an `Info.plist`, do not use the fully qualified package name. Instead use the `Info.plist` key value designated in the appropriate table.
- In setting the values for any of these keys, you may take advantage of two variables unique to application bundles:

  **`APP_PACKAGE`**
  : The root directory of the application bundle.

  **`JAVAROOT`**
  : This is not set by default. If you do set it in the `Info.plist` file, you may use `$JAVAROOT` to resolve its value.

The properties listed in [Table C-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomjsfvkfawcsivddcmbv) are all properties that are found only on Mac OS X. Overall they help your applications to fit in more cleanly with the rest of the Mac OS X environment. They can be set three ways:

- In the `Info.plist` or `MRJApp.properties` files through Project Builder or MRJAppBuilder respectively. You can modify these files later with a text editor.
- In your `main` class as arguments to `System.setProperty`.
- From the command-line using the `-D` flag as follows:

  `java -Dcom.apple.macosx.useScreenMenuBar=true`_YourSwingApp_

__Table C-4__  System properties related to the graphical user interface

| Property | Default Value | Notes |
| `com.apple.hwaccel` | `true` | Turns on hardware graphics acceleration for the video cards not commented out of `/Library/Java/Home/lib/hwexclude.properties.`If set to `false`, hardware acceleration is turned off. It may be used in conjunction with the `com.apple.hwaccelexclude` property. |
| `com.apple.hwexclude` | `none` | When specific video card designation strings are passed in with this property, hardware graphics acceleration is not turned on for the respective video cards. It is be on for all other video cards. When this property is set, `/Library/Java/Home/lib/hwexclude.properties` is ignored. |
| `com.apple.macos.use-file-dialog-packages` | `false` | When set to `true`, causes `java.awt.FileDialog` to show application packages as if they were files and does not allow navigation into them. |
| `com.apple.macos.useScreenMenuBar` | `false` | Puts Swing menus in the Mac OS X menu bar if using the Aqua look and feel. Java applications created with Project Builder have this set to `true`. Note that JMenuBars in JDialogs are not moved to the Mac OS X menu bar. |
| `com.apple.macos.useSmallTabs` | `none` | If defined, and set to `true`, tab controls in Swing applications more closely resemble the Metal look and feel. If set to `false`, the tabs assume a larger size more similar to the default Aqua controls. |
| `com.apple.macosx.AntiAliasedTextOn` | `true` | Use anti-aliasing when rendering text. |
| `com.apple.macosx.AntiAliasedGraphicsOn` | `true` | Use anti-aliasing when rendering graphics. |
| `com.apple.mrj.application.apple.menu.about.name` | None | If defined, an About command is added to the top of the application menu and can be detected by registering a `com.apple.mrj.AboutHandler`. Java applications created with Project Builder have this set to initial name of your project. |
| `com.apple.mrj.application.growbox.intrudes` | `true` | Resizable window’s growbox (resize control) intrudes into AWT content. If turned off, the bottom of the window is pushed down 15 pixels. |
| `com.apple.mrj.application.live-resize` | `false` | Enables live resizing of windows. |

[Next](Document%20Revision%20History.md)[Previous](MRJAppBuilder%20Tutorial.md)

