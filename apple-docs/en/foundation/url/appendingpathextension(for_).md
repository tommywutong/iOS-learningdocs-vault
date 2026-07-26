---
title: 'appendingPathExtension(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/appendingpathextension(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/appendingpathextension(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/appendingpathextension%28for%3A%29.json'
content_hash: 'sha256:28248a5163bd4516'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# appendingPathExtension(for:)

<sub>Instance Method</sub>

Returns a URL by appending the preferred path extension for the type you specify to the URL’s last path component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func appendingPathExtension(for contentType: UTType) -> URL
```

## Parameters

- `contentType` — A uniform type identifier.

## Return Value

A URL with the default path extension for the type you specify.

## Discussion

Use this method when you want to mix partial input from a user or other source, and need to produce a complete filename suitable for that input. For example, if you download a file from the internet and know its MIME type, you can use this method to ensure the URL has the correct filename extension where you save the file.

If `partialName` already has a path extension, and that path extension is valid for file system objects of type `contentType`, the function doesn’t add an extension before appending it to the URL. For example, if the inputs are `puppy.jpg` and [jpeg](../../uniformtypeidentifiers/uttype-swift.struct/jpeg.md), respectively, the function returns a URL with an appended path component of `puppy.jpg`. However, if the inputs are `puppy.jpg` and [plainText](../../uniformtypeidentifiers/uttype-swift.struct/plaintext.md), respectively, the function returns a URL with an appended path component of `puppy.jpg.txt`. If you want to replace any existing path extension, use the [deletePathExtension()](<deletepathextension().md>) method first.

If the function can’t append the path component, it returns an unchanged URL.

For more information about types, see [Uniform Type Identifiers](../../uniformtypeidentifiers.md).

## See Also

### Adding a path extension

- [appendPathExtension(_:)](<appendpathextension(__).md>) — Appends the specified path extension to self.
- [appendingPathExtension(_:)](<appendingpathextension(__).md>) — Returns a URL by appending the specified path extension to self.
- [appendPathExtension(for:)](<appendpathextension(for_).md>) — Appends the preferred path extension for the type you specify.
