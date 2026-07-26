---
title: 'init(fetchRequest:completionBlock:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsasynchronousfetchrequest/init(fetchrequest:completionblock:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/init(fetchrequest:completionblock:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsasynchronousfetchrequest/init%28fetchrequest%3Acompletionblock%3A%29.json'
content_hash: 'sha256:18004a7fdaced276'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAsynchronousFetchRequest](../nsasynchronousfetchrequest.md)

# init(fetchRequest:completionBlock:)

<sub>Initializer</sub>

Initializes a new asynchronous fetch request configured with the provided fetch request and completion block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(fetchRequest request: NSFetchRequest<ResultType>, completionBlock blk: ((NSAsynchronousFetchResult<ResultType>) -> Void)? = nil)
```
