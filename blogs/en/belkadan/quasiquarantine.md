---
title: quasiquarantine
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2019/12/Quasiquarantine/'
original_language: en
published: 2019-12-24
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:626010fd92deab6d'
translated: false
---

> 原文：[quasiquarantine](https://belkadan.com/blog/2019/12/Quasiquarantine/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Queue, Queeu, Quuee](https://belkadan.com/blog/2019/09/Queue-Queeu-Quuee/)

[ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/) »

« [Keyboard Adventures](https://belkadan.com/blog/2012/04/Keyboard-Adventures/?tag=mac-os-x)

« [\> go east](https://belkadan.com/blog/2019/08/go-east/?tag=source-code)

[ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/?tag=source-code) »

## [quasiquarantine](#)

In Apple’s TN2206, “[macOS Code Signing in Depth](https://developer.apple.com/library/archive/technotes/tn2206/)”, there’s a section about “[Checking Gatekeeper Compliance](https://developer.apple.com/library/archive/technotes/tn2206/_index.html#//apple_ref/doc/uid/DTS40007919-CH1-TNTAG211)”.

> - Package your program the way you ship it, such as in a disk image.
> - Download it from its website, or mail it to yourself, or send it to yourself using AirDrop or Message. This will quarantine the downloaded copy. This is necessary to trigger the Gatekeeper check as Gatekeeper only checks quarantined files the first time they’re opened.
> - Drag-install your app and launch it.

I figured jumping through a “download” or “send” step was overkill. Surely there’s a way to get the same effect programmatically, right? Turns out the answer is yes, and here’s the code to do it:

```
#!/usr/bin/swift
// License: CC0 1.0 Public Domain Dedication
// https://creativecommons.org/publicdomain/zero/1.0/

import Foundation

guard CommandLine.arguments.count >= 2 else {
  print("usage: quasiquarantine file ...")
  exit(EXIT_FAILURE)
}

let urls = CommandLine.arguments.lazy.dropFirst().map {
  URL(fileURLWithPath: $0)
}
for url in urls {
  do {
    if url.pathExtension == "app" {
      print("\(url.path): warning: manual quarantine only seems to work on archives, not app bundles")
    }

    let existingInfo = try url.resourceValues(forKeys: [.quarantinePropertiesKey])
    guard existingInfo.quarantineProperties == nil else {
      print("\(url.path): already quarantined by \(existingInfo.quarantineProperties?[kLSQuarantineAgentNameKey as String] ?? "<unknown>")")
      continue
    }

    var newInfo = URLResourceValues()
    newInfo.quarantineProperties = [
      kLSQuarantineAgentNameKey as String: "quasiquarantine",
      kLSQuarantineTypeKey as String: kLSQuarantineTypeOtherAttachment,
      kLSQuarantineAgentBundleIdentifierKey as String: "com.belkadan.Quasiquarantine"]
    var mutableURL = url
    try mutableURL.setResourceValues(newInfo)
    print("\(url.path): quarantined!")

  } catch let error {
    print("\(url.path): \(error.localizedDescription)")
  }
}
```

Save this as “quasiquarantine” and run it with `swift quasiquarantine`, or mark it as executable and run it directly.

_After_ I made this, I tried it out on a locally-built .app I had lying around. No dice. I went searching around and found that the [homebrew](https://brew.sh) project had made [nearly the same script](https://github.com/Homebrew/brew/pull/4656/files#diff-85199f8c185a73fd0a240a6a8cf7f964) last year, and so I figured I’d better try again. This time I read the directions more carefully:

> - Package your program the way you ship it, such as in a disk image.

Ah, right. When you unarchive an app or load it from a disk image, it inherits the quarantine info from the original downloaded file. I tried zipping up my locally-built app, “quasi-quarantining” the archive, and then unzipping it. And that worked!

So, here you go. quasiquarantine. Hopefully it helps someone.

This entry was posted on [December](https://belkadan.com/blog/2019/12) 24, [2019](https://belkadan.com/blog/2019) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Mac OS X](https://belkadan.com/blog/tags/mac-os-x), [Source code](https://belkadan.com/blog/tags/source-code)
