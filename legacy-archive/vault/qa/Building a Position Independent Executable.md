---
title: Building a Position Independent Executable
apple_id: DTS40013354
resource_type: QA
platform: iOS|macOS
topic: Xcode
technology: null
published: '2014-02-20'
source_url: https://developer.apple.com/library/archive/qa/qa1788/_index.html
archived_at: '2026-07-18T02:34:45.486091Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1788

# Building a Position Independent Executable

## Q:  I received a "Non-PIE Binary - The executable '<appname>.app' is not a Position Independent Executable. Please ensure that your build settings are configured to create PIE executables." warning after uploading my app to iTunes Connect. How do I build my app as Position Independent Executable (PIE)?

A: Position Independent Executable (PIE) applications can be loaded at a random memory address when run. This has security benefits for your application. iOS 4.3 or later, and OS X 10.7 or later, fully support PIE executables.

1. In Xcode, select your target in the "Targets" section, then click the "Build Settings" tab to view its settings.
2. For iOS apps, set `iOS Deployment Target` to iOS 4.3 or later. For Mac apps, set `OS X Deployment Target` to OS X 10.7 or later.
3. Verify that `Generate Position-Dependent Code` is set at its default value of `NO`.
4. Verify that `Don't Create Position Independent Executables` is set at its default value of `NO`.

You can check whether your application is PIE by running `otool -hv` on your executable in the Terminal. Your application is PIE if its header contains the `PIE` flag. Listing 1 shows an example of how to do this for an iOS app.

__Listing 1__  Example of a PIE application

```
 $ otool -hv /path/to/MyApp.app/MyApp
MyApp:
Mach header
magic   cputype cpusubtype caps filetype  ncmds  sizeofcmds   flags
MH_MAGIC  ARM    V7        0x00  EXECUTE    23        2372     NOUNDEFS DYLDLINK TWOLEVEL PIE
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-02-20 | Clarified the notion of PIE for apps with dependencies. |
| 2013-05-23 | New document that addresses how to build a Position Independent Executable. |

