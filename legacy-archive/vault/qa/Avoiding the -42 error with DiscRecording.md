---
title: Avoiding the -42 error with DiscRecording
apple_id: DTS10002326
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: DiscRecording
published: '2004-05-25'
source_url: https://developer.apple.com/library/archive/qa/qa1292/_index.html
archived_at: '2026-07-18T02:30:21.264562Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1292

# Avoiding the -42 error with DiscRecording

## Q:  When burning a virtual filesystem, DiscRecording is retuning a -42 error which maps to tmfoErr (too many files open). How do I workaround this?

A: For historical BSD reasons, Mac OS X 10.2.x limits you to only 256 open file descriptors. Files used by DiscRecording can use two descriptors each; one for the data fork and one for the resource fork; so you can hit the limit pretty quickly if you're not careful.

The good news is that this limit is only a soft limit. You can actually have as many open files as you want. To allow this, you have to explicitly call setrlimit(2):

__Listing 1__  Code showing how to increase the open file limit.

```c
#include <sys/types.h>
#include <sys/time.h>
#include <sys/resource.h>

int main (int argc, const char * argv[])
{
    struct rlimit limit;
    int err;

    err = getrlimit(RLIMIT_NOFILE, &limit);
    if (err == 0) {
        limit.rlim_cur = RLIM_INFINITY;
        (void) setrlimit(RLIMIT_NOFILE, &limit);
    }

    return 0;
}
```

When the soft limit is set to `RLIM_INFINITY`, the restriction for your process is lifted, however, there's also an underlying limit which you can't do much about, which is the number of vnodes available in the kernel.

Each open file descriptor on the entire system takes up one vnode, and there's a limited number of vnodes available. The exact number is determined automatically based on how much RAM is in the system; you can find out what the limit is by entering "sysctl kern.maxvnodes" in the Terminal. Typical values range anywhere from 4500 to 35000.

If you need to create more than a few thousand files, you can still do so in Mac OS X 10.2.x; simply create virtual DRFiles instead of real DRFiles, and specify your own data producer. Your data producer should open the file when the first byte is sent and close it when the last byte is sent.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-05-25 | Updated code example. The previous code example was invalid. |
| 2003-09-18 | New document that explains how to workaround the -42 error when using the DiscRecording API. |

