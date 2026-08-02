---
title: Availability of Quartz Composer Patches in Web Kit
apple_id: DTS10004192
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2007-03-05'
source_url: https://developer.apple.com/library/archive/qa/qa1505/_index.html
archived_at: '2026-07-18T02:31:39.797184Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1505

# Availability of Quartz Composer Patches in Web Kit

## Q:  I'm using the Quartz Composer Web Kit Plug-in to display my compositions, but I'm told that my composition is unsafe and cannot be run. Everything works in Quartz Composer, so what's happening?

A: When a Quartz Composer composition is loaded by the Quartz Composer Web Kit Plug-in, it inspects the patches that are in use. If an unsafe patch is discovered, you'll see the error message in Figure 1.

__Figure 1__  Quartz Composer Web Kit Plug-in error message

!

Using any of the following patches in a Quartz Composer composition inside of a web browser like Safari, a Dashboard widget, or in another application that uses Web Kit. Compositions using these patches are disabled because they access information from local files and folders, fetch information from local or network services, or communicate with certain hardware.

__Quartz Composer Patches That You Can't Use in Web Kit__

Using any of the following patches in a Quartz Composer composition on Mac OS X 10.4.7 or later will disable your composition when run inside the Quartz Composer Web Kit plug-in.

__Controllers__

- MIDI Clock
- MIDI Controllers
- MIDI Notes

__Generators__

- Video Input

__Sources__

- Audio Input
- Bonjour Services
- Folder Images
- Spotlight Images

__Tools__

- Quartz Composer Info

__References__

- [Quartz Composer Programming Guide](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/QuartzComposer/index.html)
- [Core Image Filter Reference](https://developer.apple.com/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-06 | First Version |
| 2007-03-05 | New document that details which Quartz Composer patches are available in Web Kit |

