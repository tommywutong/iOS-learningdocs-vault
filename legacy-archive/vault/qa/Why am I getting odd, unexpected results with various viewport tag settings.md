---
title: Why am I getting odd, unexpected results with various viewport tag settings
apple_id: DTS10004492
resource_type: QA
platform: Safari|macOS
topic: General
technology: null
published: '2014-08-05'
source_url: https://developer.apple.com/library/archive/qa/qa1560/_index.html
archived_at: '2026-07-18T02:32:18.298243Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1560

# Why am I getting odd, unexpected results with various viewport tag settings

## Q:  Why am I getting odd, unexpected results with various viewport tag settings?

A: The most likely cause is that you are using semicolons to separate property/value pairs in your viewport declaration as shown in Listing 1.

__Listing 1__  Incorrect viewport declaration

```
<meta name="viewport" content="width=device-width; user-scalable=no">
```

The `viewport` tag uses commas to separate property/value pairs. Semicolons are not valid delimiters or separators, and will result in undefined behavior on your webpage. See Listing 2, which correctly declares the `viewport` tag.

__Listing 2__  Correct viewport declaration

```
<meta name="viewport" content="width=device-width, user-scalable=no">
```

Read [Safari Web Content Guide > Configuring the Viewport](https://developer.apple.com/library/safari/documentation/AppleApplications/Reference/SafariWebContent/UsingtheViewport/UsingtheViewport.html#//apple_ref/doc/uid/TP40006509-SW1) for more information about viewports.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-08-05 | Editorial update. Removed all self-closing tags. |
| 2007-11-29 | New document that advocates the use of commas to separate property/value pairs in the viewport declaration. |

