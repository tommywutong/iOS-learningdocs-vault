---
title: resourceBytes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/resourcebytes
source_url: 'https://developer.apple.com/documentation/foundation/url/resourcebytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/resourcebytes.json'
content_hash: 'sha256:c7ed4d692a518a7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# resourceBytes

<sub>Instance Property</sub>

The URL’s resource data, as an asynchronous sequence of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var resourceBytes: URL.AsyncBytes { get }
```

## Discussion

Use this property with Swift’s `for`-`await`-`in` syntax, to read the contents of a URL byte-by-byte, like this:

```swift
guard let url = URL(string: "https://www.example.com") else {
    return
}
do {
    // Read each byte of the data as it becomes available.
    for try await byte in url.resourceBytes
    {
        // Do something with byte.
    }
} catch {
    print ("Error: \(error)")
}
```

To wait for the entire resource to load, use the [URLSession](../urlsession.md) method [data(from:delegate:)](<../urlsession/data(from_delegate_).md>) with the `await` keyword. [URLSession](../urlsession.md) also offers methods to upload data to a URL endpoint and download a URL’s contents to a file.

## See Also

### Loading URL contents asynchronously

- [lines](lines.md) — The URL’s resource data, as an asynchronous sequence of lines of text.
- [AsyncBytes](asyncbytes.md) — An asynchronous sequence of bytes loaded from the URL.
