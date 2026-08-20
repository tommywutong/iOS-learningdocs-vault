---
title: 'Logging: Using the os_log APIs'
apple_id: TP40017510
resource_type: Sample Code
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Logging/Listings/find_largest_file_ReadMe_md.html
archived_at: '2026-07-18T03:13:47.959678Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Logging: Using the os_log APIs](Logging-%20Using%20the%20oslog%20APIs.md)


[Next](README.md.md)[Previous](find-largest-file-find-largest-file-main.c.md)

# find-largest-file/ReadMe.md

```

find-largest-file
=================

The find-largest-file sample project demonstrates a simple use case of some of the logging APIs in C. Covered topics include:

- When to use the available log levels

- Format specifiers for printing specific types

- `{public}` and `{private}` modifiers

For a more in-depth sample of the os_log APIs (including profile support and usage), please see the Paper Company sample code.


Using the Sample
================

The sample code requires Xcode 8 or later and the macOS 10.12 SDK or later. find-largest-file recursively searches a given directory to find the file of maximum size. To change the default directory (`/Applications/`), select `Product > Scheme > Edit Scheme...`. Select `Run` on the left, then `Arguments` at the top. Edit the first item in `Arguments Passed on Launch` to change the default directory to search.
```

[Next](README.md.md)[Previous](find-largest-file-find-largest-file-main.c.md)

