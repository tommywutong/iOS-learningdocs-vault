---
title: Resolving App Rejections for GCC and LLVM Instrumentation
apple_id: DTS40017675
resource_type: QA
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-09-01'
source_url: https://developer.apple.com/library/archive/qa/qa1964/_index.html
archived_at: '2026-07-18T02:38:00.828257Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1964

# Resolving App Rejections for GCC and LLVM Instrumentation

## Q:  My app was rejected for containing GCC or LLVM instrumentation. How do I resolve this?

A: What is instrumentation?

In this context, instrumentation is additional code compiled in to your app that allows Xcode to analyze your code and produce reports about how much of your code is run by your test cases. This coverage information is only useful when developing an app; it negatively impacts the app's speed and increases the app's size, so apps submitted to the App Store can not contain any instrumentation code.

Apps, app extensions, or frameworks containing GCC instrumentation code are rejected by the App Store with the following message:


```
Invalid Bundle - Do not submit apps with GCC-style coverage instrumentation enabled. Specifically, the following Xcode build settings should be disabled: Instrument Program Flow Generate Test Coverage Files
```

To solve this rejection, configure the following build settings to `No` for every target in your app:

- Instrument Program Flow (`GCC_INSTRUMENT_PROGRAM_FLOW_ARCS`)
- Generate Test Coverage Files (`CLANG_ENABLE_CODE_COVERAGE`)

See [Configure build settings](https://help.apple.com/xcode/mac/current/index.html?localePath=en.lproj#/dev04b3a04ba) for instructions on finding and configuring build settings.

If you are unable to identify which binary in your app bundle is creating this error based on the build settings, follow the instructions in [Inspect The App Package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrxguwugsbrfveu4u2qivbvi) to identify the specific binary with the issue. Once you've done so, ensure the build settings for the Xcode target producing that binary are set correctly.

Apps, app extensions, or frameworks containing LLVM instrumentation code are rejected by the App Store with the following message:


```
Invalid Bundle - Disallowed LLVM instrumentation. Do not submit apps with LLVM profiling instrumentation or coverage collection enabled. Turn off LLVM profiling or code coverage, rebuild your app and resubmit the app.
```

To solve this rejection, there are multiple things to look for:

- Set the Instrument Program Flow (`GCC_INSTRUMENT_PROGRAM_FLOW_ARCS`) build setting to `No` and remove the flags `-fprofile-instr-generate` and -`fcoverage-mapping` from the Other C Flags (`OTHER_CFLAGS`) build setting. See [Configure build settings](https://help.apple.com/xcode/mac/current/index.html?localePath=en.lproj#/dev04b3a04ba) for instructions on finding and configuring build settings.
- [Disable coverage data](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/testing_with_xcode/chapters/07-code_coverage.html) on the scheme
- Ensure all pre-compiled frameworks are built using the archive build action

Starting with Xcode 9, if the [Gather coverage data option](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/testing_with_xcode/chapters/07-code_coverage.html) is enabled on the scheme, regular builds for the Run action will also build with code coverage instrumentation, but archive builds will not. If your app's build uses scripts to generate or move build products into place, you need to ensure these scripts only use archived build products when receiving the archive build action; otherwise, build products created with the build action will contain instrumentation and result in a rejection from the App Store.

If you are unable to identify which binary in your app bundle is creating this error based on the build settings, follow the instructions in [Inspect The App Package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrxguwugsbrfveu4u2qivbvi) to identify the specific binary with the issue. Once you've done so, ensure the build settings for the target producing that binary are set correctly.

If you are unable to identify which binaries are causing the instrumentation rejection, you can manually inspect the contents of the app to discover the source of the problem.

1. In the Xcode Organizer, right click on the archive producing the error and select "Show In Finder."
2. Right click on the `.xcarchive` and select "Show Package Contents."
3. Navigate to the `Products/Applications` directory. Right click on the app and select "Show Package Contents."
4. Find your app's binary, usually named the same as the app's target in Xcode.
5. Open Terminal, and run the command in Listing 1 to look for GCC instrumentation. Listing 2 shows an example binary with GCC instrumentation that must be removed for the App Store. Listing 3 shows the command for finding LLVM instrumentation, with Listing 4 showing an example binary with LLVM instrumentation that must be removed for the App Store. You can drag and drop the binary from Finder to the Terminal to fill in the path.
6. Repeat these steps for all app extensions and all frameworks in your app. If your app contains a watchOS app, also run the same procedure on the watch extension and all frameworks in the watchOS app. Make sure to give the `otool` command the path to the binary, and not the outer `.framework` or `.appex` directory.

__Listing 1__  Terminal command to look for GCC Instrumentation

```
$ nm -m -arch all <PathToArchive>/Products/Applications/<AppName>.app/<AppBinary> | grep gcov
```


__Listing 2__  Example app containing GCC Instrumentation

```
$ nm -m -arch all /Users/username/Desktop/Example.app/Example | grep gcov
0000000100009d34 (__TEXT,__text) external ___gcov_flush
000000010000cf20 (__DATA,__bss) non-external ___llvm_gcov_ctr
000000010000cf60 (__DATA,__bss) non-external ___llvm_gcov_ctr
000000010000d1a0 (__DATA,__bss) non-external ___llvm_gcov_ctr
000000010000d1b0 (__DATA,__bss) non-external ___llvm_gcov_ctr.1
000000010000cf70 (__DATA,__bss) non-external ___llvm_gcov_ctr.148
```


__Listing 3__  Terminal command to look for LLVM Instrumentation

```
$ otool -l -arch all <PathToArchive>/Products/Applications/<AppName>.app/<AppBinary> | grep __llvm_prf
```


__Listing 4__  Example app containing LLVM Instrumentation

```
$ otool -l -arch all /Users/username/Desktop/Example.app/Example | grep __llvm_prf
  sectname __llvm_prf_cnts
  sectname __llvm_prf_data
  sectname __llvm_prf_names
  sectname __llvm_prf_vnds
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-09-01 | New document that describes how to resolve an App Store rejection for an app containing instrumentation |

