---
title: Generating a Non-Maskable Interrupt (NMI)
apple_id: DTS10002294
resource_type: QA
platform: macOS
topic: General
technology: null
published: '2013-06-04'
source_url: https://developer.apple.com/library/archive/qa/qa1264/_index.html
archived_at: '2026-07-18T02:30:18.160418Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1264

# Generating a Non-Maskable Interrupt (NMI)

## Q:  I need to do remote debugging on a Mac computer which is hung in the kernel. How do I interrupt this system so I can attach to it from a kernel debugging session?

A: If OS X is started with the `DB_NMI` bit set in the `debug` boot argument, momentarily pressing the system's power button will generate a non-maskable interrupt instead of sleeping or waking the system.

The system reads the `debug` flags at boot time from the `boot-args` firmware variable.

To set the `DB_NMI` bit, start by entering this command in Terminal:


```
$ nvram boot-args
```

This will display the current setting of the boot arguments. Now, add `debug=0x4` to the current settings with this command:


```
$ sudo nvram boot-args="<current settings> debug=0x4"
```

You must restart the computer for the new settings to take effect.

For other useful debug flags, please see [Table 20-1 'Debugging flags' of Kernel Programming Guide: When Things Go Wrong: Debugging the Kernel](../documentation/Darwin/Kernel%20Programming%20Guide/Building%20and%20Debugging%20Kernels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbvfvbuqmrsgewueqkcirdukr2g).

The power button will retain this functionality until OS X is restarted without the `DB_NMI` bit set. You can clear this bit by issuing the `nvram` command with the `-d` option:


```
$ sudo nvram -d boot-args
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-06-04 | Revised for OS X v10.9. |
| 2008-10-13 | Modernized and made editorial revisions. Added details related to Intel-based Macs. |
| 2004-04-26 | Unspecified content revisions. |
| 2003-04-23 | New document that explains how to generate a non-maskable interrupt (NMI) on Mac systems. |

