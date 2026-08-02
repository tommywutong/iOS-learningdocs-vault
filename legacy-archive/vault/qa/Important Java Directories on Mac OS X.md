---
title: Important Java Directories on Mac OS X
apple_id: DTS10001702
resource_type: QA
platform: Java
topic: Cross Platform
technology: null
published: '2010-10-14'
source_url: https://developer.apple.com/library/archive/qa/qa1170/_index.html
archived_at: '2026-07-18T02:30:11.932761Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1170

# Important Java Directories on Mac OS X

## Q:  I am porting a Java product to Mac OS X. What are the equivalents for directories and paths common to JDK installations on other platforms?

A: I am porting a Java product to Mac OS X. What are the equivalents for directories and paths common to JDK installations on other platforms?

Since a JDK is preinstalled on every copy of Mac OS X, the location of the Java VM may vary, but can be found using tools built into the OS. User input should never be required to locate Java-related paths and directories.

Many Java applications need to know the location of a `$JAVA_HOME` directory. The `$JAVA_HOME` on Mac OS X should be found using the `/usr/libexec/java_home` command line tool on Mac OS X 10.5 or later. On older Mac OS X versions where the tool does not exist, use the fixed path "`/Library/Java/Home`". The `/usr/libexec/java_home` tool dynamically finds the top Java version specified in Java Preferences for the current user. This path allows access to the `bin` subdirectory where command line tools such as `java`, `javac`, etc. exist as on other platforms. The tool `/usr/libexec/java_home` allows you to specify a particular CPU architecture and Java platform version when locating a `$JAVA_HOME`.

Another advantage of dynamically finding this path, as opposed to hardcoding the fixed endpoint, is that it is updated when a new version of Java is downloaded via Software Update or installed with a newer version of Mac OS X. For this reason, it is important that developers do not install files in the JDKs inside of `/System`, since the changes will be lost with subsequent updates by newer versions of Java.

To obtain the path to the currently executing `$JAVA_HOME`, use the `java.home` System property.

Java software on other platforms often makes use of the `$JAVA_HOME/lib/ext` directory within a JDK installation to store support class or jar files. While Java for Mac OS X also contains a `lib/ext` directory, developers should not directly modify it for the same reasons mentioned above. The `/Library/Java/Extensions` directory can be used for additional jar files or JNI libraries that need to be placed on the system classpath. For more controlled access, the `~/Library/Java/Extensions` directory can be used for user-level installation of support libraries. Items placed in either of these directories do not need to be named in an application's classpath and will be available to all applications run under the respective scope (system-level or user-level, depending which directory is used).

On Mac OS X, the Java runtime provides the `java.util.prefs` API which is backed by the standard Mac OS X Preferences API and directories. Simply using this pure Java API reads and stores your application's preferences in `~/Library/Preferences` in a Mac OS X property list file. For applications that may already have their own preferences format, these preferences should be stored in the `~/Library/Preferences` directory as well. This directory can be reached from Java code by creating a file with the path of `System.getProperty("user.home") + "/Library/Preferences/" + "com.example.your.Application"`. An application that should have global preferences across all users could instead reside in `/Library/Preferences`, however this directory is not writable by non-admin users.

Some applications store user's data in database files or save-less file schemes which are not conventional documents the user can move around in the file system. On Mac OS X, these files should go into a directory with your application's name inside of the `~/Library` directory. Your app's directory in the top-level of `~/Library` should only be used for irreplaceable user data, and not preferences (like window positions or recently-used document lists). You can create a path to this directory by appending `System.getProperty("user.home") + "/Library/" + "Your App Name"`.

Applications that use temporary files to cache downloaded resources or complex calculations should store them in the secure Mac OS X temp directory. Use the `java.io.tmpdir` System property concatenated with a unique identifier for your application to create a place in the secure temp directory for your application. This location is periodically purged of files that have not been modified for several days, but is present on the startup disk.

If your application uses its own purging strategy, it may be appropriate to use the `~/Library/Caches` directory in the user's home directory. Keep in mind that this location may reside on a network mounted file system or in an encrypted FileVault image. You can create a directory in this location by appending `System.getProperty("user.home") + "/Library/Caches/" + "com.example.your.Application"`.

Using the `/tmp` directory is not recommended.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-10-14 | Fixing ~/Library typo. |
| 2010-05-22 | Adding information about cache and persistent application data. |
| 2010-02-10 | Updating how to obtain $JAVA_HOME via /usr/libexec/java_home, and other minor cleanup. |
| 2003-10-21 | New document that mac OS X equivalents of common Java runtime and development directories. |

