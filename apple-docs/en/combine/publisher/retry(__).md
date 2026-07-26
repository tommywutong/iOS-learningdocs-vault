---
title: 'retry(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/retry(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/retry(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/retry%28_%3A%29.json'
content_hash: 'sha256:3c95dfd3e204392f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# retry(_:)

<sub>Instance Method</sub>

Attempts to recreate a failed subscription with the upstream publisher up to the number of times you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func retry(_ retries: Int) -> Publishers.Retry<Self>
```

## Parameters

- `retries` — The number of times to attempt to recreate the subscription.

## Return Value

A publisher that attempts to recreate its subscription to a failed upstream publisher.

## Discussion

Use [retry(_:)](<retry(__).md>) to try a connecting to an upstream publisher after a failed connection attempt.

In the example below, a [URLSession.DataTaskPublisher](../../foundation/urlsession/datataskpublisher.md) attempts to connect to a remote URL. If the connection attempt succeeds, it publishes the remote service’s HTML to the downstream publisher and completes normally. Otherwise, the retry operator attempts to reestablish the connection. If after three attempts the publisher still can’t connect to the remote URL, the [catch(_:)](<catch(__).md>) operator replaces the error with a new publisher that publishes a “connection timed out” HTML page. After the downstream subscriber receives the timed out message, the stream completes normally.

```swift
struct WebSiteData: Codable {
    var rawHTML: String
}

let myURL = URL(string: "https://www.example.com")

cancellable = URLSession.shared.dataTaskPublisher(for: myURL!)
    .retry(3)
    .map({ (page) -> WebSiteData in
        return WebSiteData(rawHTML: String(decoding: page.data, as: UTF8.self))
    })
    .catch { error in
        return Just(WebSiteData(rawHTML: "<HTML>Unable to load page - timed out.</HTML>"))
}
.sink(receiveCompletion: { print ("completion: \($0)") },
      receiveValue: { print ("value: \($0)") }
 )

// Prints: The HTML content from the remote URL upon a successful connection,
//         or returns "<HTML>Unable to load page - timed out.</HTML>" if the number of retries exceeds the specified value.
```

After exceeding the specified number of retries, the publisher passes the failure to the downstream receiver.

## See Also

### Handling errors

- [assertNoFailure(_:file:line:)](<assertnofailure(__file_line_).md>) — Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.
- [catch(_:)](<catch(__).md>) — Handles errors from an upstream publisher by replacing it with another publisher.
- [tryCatch(_:)](<trycatch(__).md>) — Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.
