---
title: How do I prevent my WebKit-enabled application from writing to the shared icon
  database?
apple_id: DTS40010811
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2011-03-23'
source_url: https://developer.apple.com/library/archive/qa/qa1736/_index.html
archived_at: '2026-07-18T02:34:32.227225Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1736

# How do I prevent my WebKit-enabled application from writing to the shared icon database?

## Q:  How do I prevent my WebKit-enabled application from writing to the shared icon database?

A: There are two ways you can prevent your application from writing to the shared icon database:

__No Code Method__

- Add the `WebIconDatabaseEnabled` key to your defaults.plist file, and set the value to `NO`.

__In-Code Method__

- Add the code from Listing 1 to your application's `main()` routine. You must add this code \*before\* calling `NSApplicationMain()`, or it will not work.

__Listing 1__

```
[[NSUserDefaults standardUserDefaults] setBool:NO forKey:@"WebIconDatabaseEnabled"];
```

The solution is to turn off the use of that database by your application. Setting `WebIconDatabaseEnabled` to `NO` does this. This key is not currently documented, but is safe to use.

Please refer to rdar://problem/9065438, where WebKit currently defaults to YES.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-03-23 | New document that shows how you can prevent your application from writing to the shared icon database. |

