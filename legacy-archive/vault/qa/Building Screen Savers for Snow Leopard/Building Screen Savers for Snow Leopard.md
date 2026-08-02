---
title: Building Screen Savers for Snow Leopard
apple_id: DTS40009292
resource_type: QA
platform: macOS
topic: User Experience
technology: ScreenSaver
published: '2009-10-09'
source_url: https://developer.apple.com/library/archive/qa/qa1666/_index.html
archived_at: '2026-07-18T02:33:24.827220Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1666

# Building Screen Savers for Snow Leopard

## Q:  My screen saver is grayed out in the list in the Screen Savers System Preferences panel on Snow Leopard. When I click on it a sheet pops down that says: "You cannot use the <XXX> screen saver on this computer. Contact the developer of this screen saver for a newer version.". I am the developer of this screen saver, what do I have to do to make it work with Snow Leopard?

A: My screen saver is grayed out in the list in the Screen Savers System Preferences panel on Snow Leopard.

When I click on it a sheet pops down that says: "You cannot use the <XXX> screen saver on this computer. Contact the developer of this screen saver for a newer version.".

I am the developer of this screen saver, what do I have to do to make it work with Snow Leopard?

__Figure 1__  Mac OS X 10.6 (Snow Leopard) Screen Saver System Preference Panel.

!!

Mac OS X 10.6 (Snow Leopard) screen savers should be built to require Garbage Collection on the X86_64 architecture.

For example, to build a screen saver that will run on both Leopard (10.5) and Mac OS X 10.4 (Tiger):

- The architectures should be set to build 32 and 64-bit Intel (and optionally 32-bit PowerPC).
- The deployment target should be set to the oldest version of the OS that you want to support (for this example Mac OS X 10.4 (Tiger)).
- The SDK root should be set to the newest version of the OS that you want to support (for this example Mac OS X 10.6 (Snow Leopard)).
- Garbage Collection should be set to "unsupported" for 32-bit on OS versions prior to Mac OS X 10.6 (Snow Leopard).
- Garbage Collection should be set to "required" for 64-bit Intel on Mac OS X 10.6 (Snow Leopard).

__Listing 1__  Xcode Project or Target Settings necessary for Snow Leopard Screen Savers

```
ARCHS = x86_64 $(ARCHS_STANDARD_32_BIT) MACOSX_DEPLOYMENT_TARGET = 10.4 SDKROOT = macosx10.6 GCC_ENABLE_OBJC_GC = unsupported GCC_ENABLE_OBJC_GC[sdk=macosx10.6][arch=x86_64] = required
```


__Figure 2__  Xcode Screen Saver Target Settings

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-10-09 | New document that shows how to build screen savers that will work with Snow Leopard (10.6) |

