---
title: OpenCL Parallel Prefix Sum (aka Scan) Example
apple_id: DTS40008183
resource_type: Sample Code
platform: macOS
topic: Performance
technology: OpenCL
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_Parallel_Prefix_Sum_Example/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:17:50.657405Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL Parallel Prefix Sum (aka Scan) Example](OpenCL%20Parallel%20Prefix%20Sum%20%28aka%20Scan%29%20Example.md)


[Next](LICENSE.txt.md)[Previous](scan.c.md)

# ReadMe.md

```
# OpenCL Parallel Prefix Sum, a.k.a. "Scan"

Shows how to perform an efficient parallel prefix sum (aka Scan) using OpenCL.  Scan is a common data parallel primitive which can be used for variety of different operations -- this example uses local memory for storing partial sums and avoids memory bank conflicts on architectures which serialize memory operations that are serviced on the same memory bank by offsetting the loads and stores based on the size of the local group and the number of memory banks (see appropriate macro definition).  As a result, this example requires that the local group size > 1.

Note that the .cl compute kernel file(s) are loaded and compiled at runtime.  The example source assumes that these files are in the same path as the built executable.

For simplicity, this example is intended to be run from the command line. If run from within XCode, open the Run Log (Command-Shift-R) to see the output.  Alternatively, run the applications from within a Terminal.app session to launch from the command line.

## Requirements

### Build

Xcode 4 or later

### Runtime

OS X 10.6 or later
```

[Next](LICENSE.txt.md)[Previous](scan.c.md)

