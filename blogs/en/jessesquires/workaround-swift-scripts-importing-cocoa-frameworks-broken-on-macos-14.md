---
title: 'Workaround: Swift scripts importing Cocoa frameworks broken on macOS 14'
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2024/01/22/swift-scripting-broken-macos-14/'
original_language: en
published: 2024-01-22
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:78f7ab2ffae4a4ae'
translated: false
---

> 原文：[Workaround: Swift scripts importing Cocoa frameworks broken on macOS 14](https://www.jessesquires.com/blog/2024/01/22/swift-scripting-broken-macos-14/)　·　Jesse Squires

On macOS 14 Sonoma there is a regression in Swift 5.9 which causes Swift scripts that import Cocoa frameworks to fail. This issue was first reported by [@rdj](https://github.com/rdj). I discovered it myself shortly after. There is a ticket open at [#68785](https://github.com/apple/swift/issues/68785) on the main Swift repo on GitHub to track the issue.

Considering the following Swift script:

```
#!/usr/bin/swift

import AppKit
import Foundation

NSPasteboard.general.clearContents()
NSPasteboard.general.setString("Hello, Swift!", forType: .string)

print("Hello, Swift!")
```

You can run directly from the command line:

```
$ ./hello.swift
Hello, Swift!
```

On macOS 13 and earlier, this works. Unfortunately, on macOS 14 it now fails with an error: _“JIT session error: Symbols not found”_.

```
JIT session error: Symbols not found: [ _OBJC_CLASS_$_NSPasteboard, _NSPasteboardTypeString ]
Failed to materialize symbols:

[...]
```

The [current workaround](https://github.com/apple/swift/issues/68785#issuecomment-1904624571) (also posted by [@rdj](https://github.com/rdj)) is to update the shebang, `#!/usr/bin/swift`, by replacing it with the following:

```
#!/usr/bin/env DYLD_FRAMEWORK_PATH=/System/Library/Frameworks /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swift
```

**Note:** you must also have Xcode installed for this to work.

I’ve verified that this does indeed fix the problem!
