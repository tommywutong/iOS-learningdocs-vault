---
title: How do I use asserts while debugging?
apple_id: DTS10003934
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2006-06-30'
source_url: https://developer.apple.com/library/archive/qa/qa1431/_index.html
archived_at: '2026-07-18T02:30:40.885036Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1431

# How do I use asserts while debugging?

## Q:  Why don't my assertion failures log or break when I'm debugging?

A: Why don't my assertion failures log or break when I'm debugging?

The "check", "verify" and "require" macros defined in <AssertMacros.h> generate "production" (i.e. non-debug) code by default. In order for these macros to generate debug code that outputs to stderr and breaks in the debugger you have to either have DEBUG defined to non-zero or DEBUG_ASSERT_PRODUCTION_CODE defined to zero when the <AssertMacros.h> header is included.

To test this create a new Xcode 2.2 project for a standard tool, and replace the contents of the default <main.c> file with the following text:

__Listing 1__  <main.c>

```c
#include <stdio.h> #include <AssertMacros.h>  int main( int argc, char* argv[] ) {     int error = 1;      verify_noerr( error );     require_noerr( error, Oops );      printf("You shouldn't be here!\n");  Oops: ;     return error; }
```

If you build this project for the debug configuration, set a break point on the first line of main and then single step through you'll see that the "verify_noerr" is ignored and the "require_noerr" will (silently) branch to the "CantDoAnything" label. (Note: click the "console" button in the debugging windows toolbar to open the gdb output pane.) This is the expected behavior for production code. Now add "#define DEBUG 1" as the first line before the includes, build, run and single step thru the code again. This time the debugging console should output the following text as you step thru the code:


```
AssertMacros: error == 0 ,  file: /<your/path/here>/main.c, line: 10 AssertMacros: error == 0 ,  file: /<your/path/here>/main.c, line: 11
```

To define DEBUG in your project you can do any of the below:

- add "#define DEBUG 1" before any of the "#include"'s in your prefix file.
- Add "DEBUG=1" to your "extra preprocessor defines" for your Debug target, so assertions are quiet in the Release target.
- In Xcode's "Debug" configuration, in the "Preprocessing" collection set the "Preprocessor Macros" value to "DEBUG=1"
- In your project or target build settings set "OTHER_CFLAGS" to "$(value) -DDEBUG=1" for the "Debug" configuration.
- Add "#define DEBUG 1" to just the source files where you want assertions enabled and then every exception in just those files will cause an assertion.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-06-30 | New document that how do I enable asserts so they log their messages and/or break when I'm debugging? |

