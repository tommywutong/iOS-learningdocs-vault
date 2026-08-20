---
title: qtvectors.win
apple_id: DTS10001061
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtvectors.win/Listings/README_txt.html
archived_at: '2026-07-26T19:53:10.374484Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtvectors.win](qtvectors.win.md)


[Next](Application%20Files-ComApplication.c.md)[Previous](qtvectors.win.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# README.txt

```
README - QTVectors

QTVectors is a simple application that constructs a QuickTime
vector movie. It shows how to create a new movie, construct a
series of QTAtoms that describe a vector picture, and then save
the QTAtoms in the new movie. You can then open the movie to see
what was drawn.

Currently, QTVectors creates the atoms by using one of two methods:
(1) It can build the atoms by "brute force", just stuffing the data
into a handle, long word after long word. (Ouch!) (2) It can also
build an atom stream using the Curve Utilities described in the
"QuickTime Vectors" chapter of the developer documentation.
This second method is higher-level and far more readable in
the source code.

QTVectors can be compiled and run under the MacOS and under Windows.
The main vector code is found in the file QTVectors.c.
The remaining files in this folder are part of the general
Mac and Windows support code.

Enjoy,
QuickTime Team
```

[Next](Application%20Files-ComApplication.c.md)[Previous](qtvectors.win.md)

