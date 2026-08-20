---
title: Where are the LiveConnect classes on Mac OS X?
apple_id: DTS10003371
resource_type: QA
platform: macOS
topic: Cross Platform
technology: null
published: '2006-10-02'
source_url: https://developer.apple.com/library/archive/qa/qa1364/_index.html
archived_at: '2026-07-18T02:30:26.349260Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1364

# Where are the LiveConnect classes on Mac OS X?

## Q:  I receive compiler errors when I try to build an Applet that uses the LiveConnect classes. Where are these classes located on Mac OS X?

A: The LiveConnect classes are in one of two possible archives, depending on the version of Java you have installed and selected as the default. For systems with J2SE 5.0 Release 4 or any later version of Java on Mac OS X, they can be found at

`/Library/Java/Home/lib/plugin.jar`

Mac OS X Tiger systems without J2SE 5.0 Release 4 or later, as well as Mac OS X Panther systems, store the classes in

`/Library/Java/Home/lib/netscape.jar`

You can add the classes to an Xcode project by dragging the appropriate jar from the Finder into your project's file list. When prompted by Xcode, copying the file to the project directory is not necessary; it only needs to be referenced.

Terminal or script-based builds can reference the classes using the `-classpath` flag:

`javac -classpath /Library/Java/Home/lib/plugin.jar [sourcefiles]`

Note that explicitly referencing the appropriate jar is only necessary when building your Applet sources; the LiveConnect classes are on the runtime classpath by default on Mac OS X.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-10-02 | Cited new location as of J2SE 5.0 Release 4. |
| 2005-02-08 | New document that locating classes necessary to build Java-Javascript communication into Java Applets on Mac OS X. |

