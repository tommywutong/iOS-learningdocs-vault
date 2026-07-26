---
title: 'addLogHandler(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtllogstate/addloghandler(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtllogstate/addloghandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllogstate/addloghandler%28_%3A%29.json'
content_hash: 'sha256:62e4dc7066501210'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLogState](../mtllogstate.md)

# addLogHandler(_:)

<sub>Instance Method</sub>

Adds a log handler to customize the presentation of shader logging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addLogHandler(_ block: @escaping @Sendable (String?, String?, MTLLogLevel, String) -> Void)
```

## Discussion

In absence of any log handlers, all messages goes through the unified log system and are available through the console.app, log tool, or Xcode.

Use this method to add your own shader logging presentation or filter messages using subsystem, category and levels. For more details on how to configure your logging, see [Generating Log Messages from Your Code](../../os/generating-log-messages-from-your-code.md#Create-a-Log-Object-to-Organize-Messages).
