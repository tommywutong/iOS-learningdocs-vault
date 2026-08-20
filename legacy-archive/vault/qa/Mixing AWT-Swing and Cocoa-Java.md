---
title: Mixing AWT/Swing and Cocoa-Java
apple_id: DTS10003189
resource_type: QA
platform: macOS
topic: Cross Platform
technology: null
published: '2006-10-12'
source_url: https://developer.apple.com/library/archive/qa/qa1342/_index.html
archived_at: '2026-07-18T02:30:25.483035Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1342

# Mixing AWT/Swing and Cocoa-Java

## Q:  Can Cocoa-Java and AWT/Swing code be mixed in a single application?

A: The mixing of Cocoa-Java and AWT/Swing is neither recommended nor supported by Apple. This includes calls to Cocoa-Java from AWT/Swing based applications, or showing AWT/Swing components from a Cocoa-Java application. While the mixing of these APIs may seem to work, it carries a high risk of causing deadlocks between the Cocoa and AWT event systems.

Additionally, the Cocoa-Java API is deprecated as of Mac OS X Tiger. The Java Native Interface (JNI) is the recommended mechanism for calling platform specific code from AWT/Swing processes on Mac OS X, as it is when using the JDK on any other platform. The JNI can be used to make non-graphical Foundation calls, integrate Application Kit views into an AWT container, or invoke a Java Virtual Machine from an Objectve-C Cocoa app. The details of JNI programming on Mac OS X, as well as an explanation of the risks involved when mixing Cocoa with Java, are explained in [Technical Note TN2147](https://developer.apple.com/technotes/tn2005/tn2147.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-10-12 | Fixed a broken link; noted deprecation of Cocoa-Java. |
| 2006-04-25 | Added reference to TN2147. |
| 2004-02-26 | New document that recommended alternatives to mixing Cocoa-Java and AWT/Swing. |

