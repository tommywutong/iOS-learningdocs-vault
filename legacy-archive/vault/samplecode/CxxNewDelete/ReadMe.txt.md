---
title: CxxNewDelete
apple_id: DTS10003967
resource_type: Sample Code
platform: macOS
topic: Xcode
technology: null
published: '2011-05-13'
source_url: https://developer.apple.com/library/archive/samplecode/CxxNewDelete/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:05:48.852458Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CxxNewDelete](CxxNewDelete.md)


[Next](main.cpp.md)[Previous](CxxNewDelete.md)

# ReadMe.txt

```
This simple example shows how to override the C++ 'new' and 'delete' operators.  See sections [lib.support.dynamic] and [basic.stc.dynamic.allocation] in the ISO C++ standard, ISO/IEC 14882:2003 or later, for a precise description of the rules affecting this example.

There's only one source file, main.cc, which contains both the overridden operators and a simple main program to exercise them.

Typical output from the main program is:

new was called 2 times and delete was called 2 times

The sample also shows:
- How to set up Xcode when doing this;
- How to work around a bug which, especially in small examples, might cause this overriding to not work; and
- The variations on new and delete you don't need to override because the standard C++ library will forward them to your overridden versions.
```

[Next](main.cpp.md)[Previous](CxxNewDelete.md)

