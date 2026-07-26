---
title: lines
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/lines
source_url: 'https://developer.apple.com/documentation/foundation/url/lines'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/lines.json'
content_hash: 'sha256:6e858f654788d774'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# lines

<sub>Instance Property</sub>

The URL’s resource data, as an asynchronous sequence of lines of text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var lines: AsyncLineSequence<URL.AsyncBytes> { get }
```

## Discussion

Use this property with Swift’s `for`-`await`-`in` syntax, to read the contents of a URL line-by-line, like this:

```swift
guard let url = URL(string: "https://www.example.com") else {
    return
}
do {
    // Read each line of the data as it becomes available.
    for try await line in url.lines
    {
        // Do something with line.
    }
} catch {
     print ("Error: \(error)")
}
```

To wait for the entire resource to load, use the [URLSession](../urlsession.md) method [data(from:delegate:)](<../urlsession/data(from_delegate_).md>) with the `await` keyword. [URLSession](../urlsession.md) also offers methods to upload data to a URL endpoint and download a URL’s contents to a file.

## See Also

### Loading URL contents asynchronously

- [resourceBytes](resourcebytes.md) — The URL’s resource data, as an asynchronous sequence of bytes.
- [AsyncBytes](asyncbytes.md) — An asynchronous sequence of bytes loaded from the URL.
