---
title: 'urlSession(_:dataTask:didReceive:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:didreceive:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:didreceive:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondatadelegate/urlsession%28_%3Adatatask%3Adidreceive%3A%29.json'
content_hash: 'sha256:513e576ee6fe9bbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionDataDelegate](../urlsessiondatadelegate.md)

# urlSession(_:dataTask:didReceive:)

<sub>Instance Method</sub>

Tells the delegate that the data task has received some of the expected data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didReceive data: Data)
```

## Parameters

- `session` — The session containing the data task that provided data.

- `dataTask` — The data task that provided data.

- `data` — A data object containing the transferred data.

## Discussion

Because the data object parameter is often pieced together from a number of different data objects, whenever possible, use the [- enumerateByteRangesUsingBlock:](<../nsdata/enumeratebytes(__).md>) method to iterate through the data rather than using the [bytes](../nsdata/bytes.md) method (which flattens the data object into a single memory block).

This delegate method may be called more than once, and each call provides only data received since the previous call. The app is responsible for accumulating this data if needed.
