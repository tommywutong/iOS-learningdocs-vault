---
title: Addressing missing framework crashes
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/addressing-missing-framework-crashes
source_url: 'https://developer.apple.com/documentation/xcode/addressing-missing-framework-crashes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/addressing-missing-framework-crashes.json'
content_hash: 'sha256:e1dbb25151dc7995'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md) · [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md)

# Addressing missing framework crashes

<sub>Article</sub>

Identify missing frameworks from a crash report, and adjust your app’s build to correctly include the framework.

## Overview

If you modularize your app’s functionality into frameworks, the app must link the frameworks at build time, and also embed a copy of the frameworks inside the app bundle during the build. If an app links a framework but doesn’t embed it, the app crashes at launch, because the dynamic linker can’t locate the missing framework.

### Identify the missing framework

The dynamic linker, `dyld`, outputs detailed information about the framework it couldn’t locate, in the `Termination Description` of the crash report:

```other
Exception Type: EXC_CRASH (SIGABRT)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Exception Note: EXC_CORPSE_NOTIFY
Termination Description: DYLD, 
    dependent dylib '@rpath/MyFramework.framework/MyFramework' not found for '<path>/MyCoolApp.app/MyCoolApp',
    tried but didn't find: 
    '/usr/lib/swift/MyFramework.framework/MyFramework' 
    '<path>/MyCoolApp.app/Frameworks/MyFramework.framework/MyFramework' 
    '@rpath/MyFramework.framework/MyFramework' 
    '/System/Library/Frameworks/MyFramework.framework/MyFramework'
```

The exact message depends on the operating system and operating system version. Here’s a different example:

```other
Exception Type: EXC_CRASH (SIGABRT)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Exception Note: EXC_CORPSE_NOTIFY
Termination Description: DYLD, Library not loaded: @rpath/MyFramework.framework/MyFramework 
    | Referenced from: <path>/MyCoolApp.app/MyCoolApp 
    | Reason: image not found
```

> [!note] Note
> For readability, extra line breaks are in this example. In the original crash report file for these examples, the `dyld` information is on fewer lines.

### Inspect the framework’s configuration

Ensure the framework is correctly embedded in the app bundle—see [Embedding Frameworks In An App](https://developer.apple.com/library/archive/technotes/tn2435/_index.html#//apple_ref/doc/uid/DTS40017543).

If you can’t reproduce the crash, archive the app, export it for Development distribution, and apply app thinning, as described in [Distributing your app for beta testing and releases](distributing-your-app-for-beta-testing-and-releases.md). Test the different variants produced through app thinning to see if the framework is missing only after applying app thinning. If this reproduces the crash, do the following:

- Verify the framework’s build setting for Architectures (`ARCHS`) is the default value.
- Verify the framework’s build setting for Valid Architectures (`VALID_ARCHS`) is the default value.
- Verify the [UIRequiredDeviceCapabilities](../bundleresources/information-property-list/uirequireddevicecapabilities.md) key in the framework’s `Info.plist` file correctly specifies the CPU architectures the framework supports.

> [!note] Note
> If the missing framework is from a third-party framework vendor or uses third-party development tools to integrate it in your app, contact the vendor for assistance in addressing the issue.

## See Also

### Related Documentation

- [Analyzing a crash report](analyzing-a-crash-report.md) — Identify clues in a crash report that help you diagnose problems.
