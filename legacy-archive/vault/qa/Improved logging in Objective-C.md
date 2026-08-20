---
title: Improved logging in Objective-C
apple_id: DTS40009343
resource_type: QA
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2011-10-04'
source_url: https://developer.apple.com/library/archive/qa/qa1669/_index.html
archived_at: '2026-07-18T02:33:36.145617Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1669

# Improved logging in Objective-C

## Q:  How can I add context information - such as the current method or line number - to my logging statements?

A: The C preprocessor provides a number of standard macros that give you information about the current file, line number, or function. Additionally, Objective-C has the `_cmd` implicit argument which gives the selector of the current method, and functions for converting selectors and classes to strings. You can use these in your `NSLog` statements to provide useful context during debugging or error handling.

__Listing 1__  Example of logging the current method and line number. Paste it into your project, and see what it prints!

```
NSMutableArray *someObject = [NSMutableArray array];
NSLog(@"%s:%d someObject=%@", __func__, __LINE__, someObject);
[someObject addObject:@"foo"];
NSLog(@"%s:%d someObject=%@", __func__, __LINE__, someObject);
```

The following tables list the most popular macros and expressions which might be useful in your logging statements.

__Table 1__  Preprocessor macros and for logging in C/C++/Objective-C.

| Macro | Format Specifier | Description |
| __func__ | %s | Current function signature. |
| __LINE__ | %d | Current line number in the source code file. |
| __FILE__ | %s | Full path to the source code file. |
| __PRETTY_FUNCTION__ | %s | Like __func__, but includes verbose type information in C++ code. |

__Table 2__  Expressions for logging in Objective-C.

| Expression | Format Specifier | Description |
| NSStringFromSelector(_cmd) | %@ | Name of the current selector. |
| NSStringFromClass([self class]) | %@ | Name of the current object's class. |
| [[NSString stringWithUTF8String:__FILE__] lastPathComponent] | %@ | Name of the source code file. |
| [NSThread callStackSymbols] | %@ | NSArray of the current stack trace as programmer-readable strings. For debugging only, do not present it to end users or use to do any logic in your program. |

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-10-04 | Expanded logging examples. |
| 2009-10-27 | New document that describes use of preprocessor macros and Objective-C language features to provide better context in log statements. |

