---
title: Java on Intel-based Macs
apple_id: DTS10003767
resource_type: QA
platform: Java
topic: Cross Platform
technology: null
published: '2006-10-17'
source_url: https://developer.apple.com/library/archive/qa/qa1295/_index.html
archived_at: '2026-07-18T02:30:21.376561Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1295

# Java on Intel-based Macs

## Q:  Do I need to change my Java application to run on Intel-based Macs?

A: The answer is probably no. Pure Java applications require no code changes to run on Intel-based Macs. This includes the following deployment scenarios:

- Shell script- or command line-based Java applications
- Double-clickable jar files
- Double-clickable Java applications packaged using Xcode, Jar Bundler, or Project Builder
- Java Applets
- Java Web Start applications

The story is different for Java applications containing native code. The two cases listed below __must__ be built as universal binaries by following the steps in the [Universal Binary Programming Guidelines](https://developer.apple.com/documentation/MacOSX/Conceptual/universal_binary/). These two cases have no exceptions: under no deployment scenarios — not even those listed above — do Java applications that interface with PowerPC-based native code run successfully on Intel-based Macs.

- __JNI Libraries.__ JNI libraries built for PowerPC-based Macs are not loaded under Rosetta because the Java Virtual Machine has already launched without Rosetta. Java applications fail on Intel-based Macs when trying to load PowerPC-only binaries.
- __Native launchers.__ Native applications that use the VM Invocation Interface to start a Java Virtual Machine must be built as universal binaries to run on Intel-based Macs. The Java VM must run natively; attempts by an application running under Rosetta to instantiate a JVM fail.

It is important to understand that __neither of the above cases run under Rosetta__ because the Java VM itself does not. JNI libraries or native applications which instantiate a JVM must be built as universal binaries to run on Intel-based Macs. computers.

Only Xcode targets that build native (C/C++/Objective-C) code need to be updated to build universal binaries; Java targets require no changes. If your targets were created with an older version of Xcode, they may need to be updated to native targets. To find out if this is necessary:

- Open your project in Xcode 2.1 or later
- Select the target in question (your JNI library target for example) in the Groups & Files list
- Click on the Project menu

If the Upgrade to Native Target menu item is enabled, the target must be upgraded before building a universal binary. When the upgrade is complete, a Native Target Upgrade Log appears summarizing any changes. Figure 1 shows an older target that needs to be upgraded.

__Figure 1__  Upgrading to a Native Target in Xcode.

!

Once the target is upgraded, it is ready to build a universal binary. See the Building a Universal Binary section of the Universal Binary Programming Guidelines and [Building a JNI Universal Application With Xcode](https://developer.apple.com/java/jniuniversal.html) for more information.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-10-17 | Minor editorial changes |
| 2006-01-10 | Editorial changes |
| 2005-08-29 | Image revision |
| 2005-08-25 | New document that required changes (if any) for Java applications to run on Intel-based Macs. |

