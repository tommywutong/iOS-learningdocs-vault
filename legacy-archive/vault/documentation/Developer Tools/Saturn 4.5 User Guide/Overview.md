---
title: Saturn 4.5 User Guide
apple_id: TP40005157
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SaturnUserGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:25:26.154162Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20Saturn%20Front-end.md)

# Overview

After completing the first stages of program development, like design and debugging, you can use performance tools such as Saturn to help optimize your program. Saturn helps you understand your program’s function-calling structure and how much time was spent in each function. Saturn consists of two parts: a graphical front-end and a dynamic library back-end. The Saturn back-end library leverages the instrumentation infrastructure in `gcc` to generate an output file that summarizes how much time your program spends in various functions. The Saturn front-end can then read this file and present a representation of the function calling patterns and a function tree view.

UNIX implementations typically support a notion of compiler driven function instrumentation by specifying compiler flags to request instrumentation. The compiler supplied by Apple responds to two different command line options:

- `-pg`— This causes the insertion of call graph profile data generating code into every function prologue during compilation. Each execution of your program produces a `gmon.out` file. The standard tool for reviewing these files is the `gprof` command-line tool, but Saturn’s front end can display the same information in a graphical manner on PowerPC-based Macs only.
- `-finstrument-functions`— This causes the insertion of separate user-defined instrumentation routines for each function prologue _and_ epilogue. It incurs somewhat more overhead than `-pg`, but allows you to record a selection of custom data items in addition to basic timing. This option works with both PowerPC _and_ Intel-based Macs.

Saturn allows you to visualize the data in two ways: a traditional call-tree view and a graphical call-stack timeline. Using this information, you can eliminate expensive calling behavior (for example, deep call stacks which do not last long) as well as understand which functions take up the greatest portion of execution time.

[Next](The%20Saturn%20Front-end.md)

