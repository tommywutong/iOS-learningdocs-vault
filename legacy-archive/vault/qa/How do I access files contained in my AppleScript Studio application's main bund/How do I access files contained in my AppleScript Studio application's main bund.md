---
title: How do I access files contained in my AppleScript Studio application's main
  bundle?
apple_id: DTS10004102
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: null
technology: null
published: '2007-02-05'
source_url: https://developer.apple.com/library/archive/qa/qa1493/_index.html
archived_at: '2026-07-18T02:31:29.717749Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1493

# How do I access files contained in my AppleScript Studio application's main bundle?

## Q:  How do I access files contained in my AppleScript Studio application's main bundle?

A: How do I access files contained in my AppleScript Studio application's main bundle?

If you have files in your AppleScript Studio application's bundle (that is, in your Resources folder under Groups & Files (see Figure 1), you can access them by using "`resource path of main bundle`" plus the pathname hierarchy to the file. See Listing 1 for an example.

__Figure 1__  Groups & Files showing pathname hierarchy.

!

__Listing 1__  Using 'resource path of main bundle'

```
set myFile to (resource path of main bundle) & "/path/to/your/file.txt"
```

When you run this, `myfile` would contain a path similar to "`/Users/username/AppleScript Studio.app/Contents/Resources/path/to/your/file.txt`". (This path would likely include "...`/build/Debug`" when testing within Xcode.)

For more information on bundles in AppleScript Studio, see the Application Suite > Terminology > bundle section of "AppleScript Studio Terminology Reference"; you can find it in the ADC Reference Library at [Reference > AppleScript > Tools](https://developer.apple.com/reference/AppleScript/idxTools-date.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-02-05 | Clarified pathname hierarchy references; added pointer to reference guide. |
| 2006-10-09 | New document that explains how to access files stored within an AppleScript Studio application. |

