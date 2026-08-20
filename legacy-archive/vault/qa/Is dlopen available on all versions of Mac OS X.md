---
title: Is dlopen available on all versions of Mac OS X?
apple_id: DTS10001709
resource_type: QA
platform: macOS
topic: General
technology: null
published: '2008-08-19'
source_url: https://developer.apple.com/library/archive/qa/qa1180/_index.html
archived_at: '2026-07-18T02:30:12.180295Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1180

# Is dlopen available on all versions of Mac OS X?

## Q:  Is dlopen available on all versions of Mac OS X?

A: Prior to version 10.3, dlopen was only available for Mac OS X as a third party library called [dlcompat](http://pdb.finkproject.org/pdb/package.php/dlcompat).

In order to better support the compilation of various software projects on Mac OS X, Apple rolled dlcompat into the operating system in Mac OS X 10.3. Then for Mac OS X 10.4, Apple rewrote dlopen and integrated it into the dyld project. Consequently, dlopen, dlclose, dlsym, and dlerror are all implemented using dyld calls.

Software written using a higher level framework in most cases should use the dynamic linking facilities available at that level. [Core Foundation](https://developer.apple.com/documentation/CoreFoundation/index.html) provides two mechanisms for dynamically linking to libraries and plug-ins: [CFBundle](https://developer.apple.com/documentation/CoreFoundation/Reference/CFBundleRef/index.html) and, layered on top of that, [CFPlugIn](https://developer.apple.com/documentation/CoreFoundation/Reference/CFPlugInRef/index.html). Cocoa programmers will probably want to use [NSBundle](https://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSBundle_Class/Reference/Reference.html).

Detailed information about using dynamic libraries on Mac OS X can be found in the ADC document "[Introduction to Dynamic Library Programming Topics](https://developer.apple.com/documentation/DeveloperTools/Conceptual/DynamicLibraries/Introduction.html)".

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-08-19 | Fixed broken links. |
| 2006-05-11 | Moved to Darwin>Porting category. |
| 2005-12-02 | Changed title and content to reflect dlopen's inclusion in Panther and beyond. |
| 2002-08-19 | New document that describes how to dynamically link to libraries and plug-ins, typically done with dlopen. |

