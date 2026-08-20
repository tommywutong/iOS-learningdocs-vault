---
title: UnsupportedClassVersionError With J2SE 5.0 Release 4
apple_id: DTS10003922
resource_type: QA
platform: macOS
topic: Cross Platform
technology: null
published: '2006-04-14'
source_url: https://developer.apple.com/library/archive/qa/qa1474/_index.html
archived_at: '2026-07-18T02:30:57.402613Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1474

# UnsupportedClassVersionError With J2SE 5.0 Release 4

## Q:  After installing J2SE 5.0 Release 4, my Java projects no longer build and run properly. What happened?

A: J2SE 5.0 (JDK 1.5) becomes the "default" command-line JDK on Mac OS X as of J2SE 5 Release 4. This includes the `javac` executable, which is used by Xcode, ant, and many other build scripts and systems to build Java source files. As a result, your project produces 1.5 bytecode, which is not compatible with earlier versions of Java that you may have chosen for running your application (such as 1.4).

Even with J2SE 5.0 Release 4 installed, a bundled Java application still runs under Java 1.4 if the following conditions are met:

- The Xcode project's Target VM Version (`JVMVersion` property list key) is set to 1.3\* or 1.4\*
- J2SE 1.4.2 is selected as the preferred version under Java Application Runtime Settings in `/Applications/Utilities/Java/J2SE 5.0/Java Preferences.app`

Script- or command-line-based projects may also run into this problem if explicitly running the 1.4 `java` command. Listing 1 shows the typical exception thrown in this situation.

__Listing 1__  Exception thrown when loading 1.5 bytecode in 1.4 or earlier.

```
 Exception in thread "main" java.lang.UnsupportedClassVersionError: lol (Unsupported major.minor version 49.0)
    at java.lang.ClassLoader.defineClass0(Native Method)
    at java.lang.ClassLoader.defineClass(ClassLoader.java:539)
    at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:123)
    at java.net.URLClassLoader.defineClass(URLClassLoader.java:251)
    at java.net.URLClassLoader.access$100(URLClassLoader.java:55)
    at java.net.URLClassLoader$1.run(URLClassLoader.java:194)
    at java.security.AccessController.doPrivileged(Native Method)
    at java.net.URLClassLoader.findClass(URLClassLoader.java:187)
    at java.lang.ClassLoader.loadClass(ClassLoader.java:289)
    at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:274)
    at java.lang.ClassLoader.loadClass(ClassLoader.java:235)
    at java.lang.ClassLoader.loadClassInternal(ClassLoader.java:302)
    at java.lang.Class.forName0(Native Method)
    at java.lang.Class.forName(Class.java:219)
    at apple.launcher.LaunchRunner.loadMainMethod(LaunchRunner.java:55)
    at apple.launcher.LaunchRunner.run(LaunchRunner.java:84)
    at apple.launcher.LaunchRunner.callMain(LaunchRunner.java:50)
    at apple.launcher.JavaApplicationLauncher.launch(JavaApplicationLauncher.java:52)
```

The solution is to tell the compiler that you want to create bytecode compatible with earlier versions of Java. Within Xcode, this is done in the Java Compiler Settings section of your Java target, as illustrated in Figure 1. If you have this problem, the Target VM version and Source version dropdowns will initially be set to "Unspecified", which makes `javac` produce 1.5 bytecode. Changing both of these dropdowns to 1.4 will make the built classes compatible with Java 1.4.

__Figure 1__  Modifying Java Compiler Settings in Xcode.

!!

Command-line builds do this using the `-source` and `-target` flags.


```
javac -source 1.4 -target 1.4 owMyBytecodes.java
```

If your application is using JDK 1.5 APIs, then it obviously requires 1.5 and a 1.4- or 1.3-based `JVMVersion` key is not appropriate. You should change your required version to 1.5\* or 1.5+. For more on the `JVMVersion` property list key see the [Java Dictionary Info.plist Keys](https://developer.apple.com/documentation/Java/Conceptual/JavaPropVMInfoRef/Articles/JavaDictionaryInfo.plistKeys.html#//apple_ref/doc/uid/TP40001969) section of [Java Property, VM Option, and Info.plist Key Reference for Mac OS X](https://developer.apple.com/documentation/Java/Conceptual/JavaPropVMInfoRef/index.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-04-14 | New document that explains problems running existing Xcode projects after upgrading to J2SE 5.0 Release 4 |

