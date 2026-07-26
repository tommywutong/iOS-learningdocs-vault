---
title: serviceExtensionWillTerminate()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationpushserviceextension/serviceextensionwillterminate()
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationpushserviceextension/serviceextensionwillterminate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationpushserviceextension/serviceextensionwillterminate%28%29.json'
content_hash: 'sha256:a2d51d5af0950240'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationPushServiceExtension](../cllocationpushserviceextension.md)

# serviceExtensionWillTerminate()

<sub>Instance Method</sub>

Notifies your app extension that the system is about to terminate the extension because it’s taking too long to complete its task.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func serviceExtensionWillTerminate()
```

## Discussion

If your [- didReceiveLocationPushPayload:completion:](<didreceivelocationpushpayload(__completion_).md>) method takes too long to collect a location and call its completion block, the system calls this method on the main thread. Use this method to execute the completion block from [- didReceiveLocationPushPayload:completion:](<didreceivelocationpushpayload(__completion_).md>) as quickly as possible.
