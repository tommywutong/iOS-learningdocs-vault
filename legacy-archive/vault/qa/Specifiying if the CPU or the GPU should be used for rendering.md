---
title: Specifiying if the CPU or the GPU should be used for rendering.
apple_id: DTS10003520
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2005-08-16'
source_url: https://developer.apple.com/library/archive/qa/qa1416/_index.html
archived_at: '2026-07-18T02:30:34.553818Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1416

# Specifiying if the CPU or the GPU should be used for rendering.

## Q:  Which processor will Core Image use for rendering, and how can I specify it?

A: Core Image can either use the system's CPU or an ARB fragment-capable GPU for rendering. Unless specified, Core Image will use a simple set of rules to determine the best processor for rendering on the current system. Table 1 lists the rules and the order in which they are evaluated.

__Table 1__  Rules, in order, that Core Image uses to determine the best processor for rendering

| If the GPU is | Default Processor |
| GeForce 5200 series | CPU (See note) |
| ARB fragment capable HW (except for the GeForce 5200 series) | GPU |
| non-ARB fragment capable HW | CPU |

Developers may want to use a processing unit other then the default for a number of reasons, such as to:

- Free up the CPU to perform other processing in parallel. The GeForce 5200 may be fast enough for the specific application.
- Get reproducible accuracy. CPUs are IEEE accurate, whereas GPUs are implementation specific.
- Use fragment programs that have more than 64 instructions. Some GPUs are limited 64 instructions. Larger fragment programs can instead request that Core Image to use the CPU for processing.

To tell Core Image which processor to use for rendering, use the `kCIContextUseSoftwareRenderer` flag in the options parameter when creating the `CIContext`. If `kCIContextUseSoftwareRenderer` is equal to YES, Core Image will always render using the CPU. If `kCIContextUseSoftwareRenderer` equals NO, Core Image will use the GPU if possible. See Listing 1

__Listing 1__  Creates a Core Image context that will always use the CPU for rendering.

```
CIContext * CPUonlyCIContextFromCGContext(CGContextRef cgContext) {

    NSDictionary * contextOptions = [NSDictionary dictionaryWithObjectsAndKeys:
                               [NSNumber numberWithBool: YES],kCIContextUseSoftwareRenderer,nil];

    return [CIContext contextWithCGContext:cgContext options: contextOptions];
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-06 | Changed code sample to use kCIContextUseSoftwareRenderer constant. |
| 2005-08-16 | Changed code sample to use kCIContextUseSoftwareRenderer constant. |
| 2005-05-19 | New document that which processor will be used for rendering in Core Image and how to affect it. |

