---
title: execute()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/execute()
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/execute()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/execute%28%29.json'
content_hash: 'sha256:548a5f3d16900a19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# execute()

<sub>Instance Method</sub>

Executes the fetch request against the managed object context that is associated with the current queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func execute() throws -> [ResultType]
```

## Discussion

Calling `execute` on an [NSFetchRequest](../nsfetchrequest.md) will cause the [NSFetchRequest](../nsfetchrequest.md) to run against the managed object context ([NSManagedObjectContext](../nsmanagedobjectcontext.md)) that is associated with the queue on which the `execute` is called.
