---
title: 'CFURLCreateStringByAddingPercentEscapes(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.11 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfurlcreatestringbyaddingpercentescapes(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreatestringbyaddingpercentescapes(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreatestringbyaddingpercentescapes%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:046c96be3e0128aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreateStringByAddingPercentEscapes(_:_:_:_:_:)

<sub>Function</sub>

Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding.

> [!warning] Deprecated
> Use [NSString stringByAddingPercentEncodingWithAllowedCharacters:] instead, which always uses the recommended UTF-8 encoding, and which encodes for a specific URL component or subcomponent (since each URL component or subcomponent has different rules for what characters are valid).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCreateStringByAddingPercentEscapes(_ allocator: CFAllocator!, _ originalString: CFString!, _ charactersToLeaveUnescaped: CFString!, _ legalURLCharactersToBeEscaped: CFString!, _ encoding: CFStringEncoding) -> CFString!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new `CFString` object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `originalString` — The `CFString` object to copy.

- `charactersToLeaveUnescaped` — Characters whose percent escape sequences you want to leave intact. Pass `NULL` to specify that all illegal characters be escaped.

- `legalURLCharactersToBeEscaped` — Legal characters to be escaped. Pass `NULL` to specify that no legal characters be replaced.

- `encoding` — The encoding to use for the translation. If you are uncertain of the correct encoding, you should use UTF-8 ([kCFStringEncodingUTF8](cfstringbuiltinencodings/utf8.md)), which is the encoding designated by RFC 2396 as the correct encoding for use in URLs.

## Return Value

A copy of `originalString` replacing certain characters. If it does not need to be modified (no percent escape sequences are missing), this function may merely return `originalString` with its reference count incremented. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The characters escaped are all characters that are not legal URL characters (based on RFC 2396), plus any characters in `legalURLCharactersToBeEscaped`, less any characters in `charactersToLeaveUnescaped`. To simply correct any non-URL characters in an otherwise correct URL string, pass `NULL` for the `allocator`, `charactersToLeaveEscaped`, and `legalURLCharactersToBeEscaped` parameters, and [kCFStringEncodingUTF8](cfstringbuiltinencodings/utf8.md) as the `encoding` parameter.

It may be difficult to use this function to “clean up” unescaped or partially escaped URL strings where sequences are unpredictable and you cannot specify `charactersToLeaveUnescaped`. Instead, you can “pre-process” a URL string using [CFURLCreateStringByReplacingPercentEscapesUsingEncoding](<cfurlcreatestringbyreplacingpercentescapesusingencoding(________).md>) then add the escape characters using [CFURLCreateStringByAddingPercentEscapes](<cfurlcreatestringbyaddingpercentescapes(__________).md>), as shown in the following code fragment.

```objc
CFStringRef originalURLString = CFSTR("http://online.store.com/storefront/?request=get-document&doi=10.1175%2F1520-0426(2005)014%3C1157:DODADSS%3E2.0.CO%3B2");
CFStringRef preprocessedString =
    CFURLCreateStringByReplacingPercentEscapesUsingEncoding(kCFAllocatorDefault, originalURLString, CFSTR(""), kCFStringEncodingUTF8);
CFStringRef urlString =
    CFURLCreateStringByAddingPercentEscapes(kCFAllocatorDefault, preprocessedString, NULL, NULL, kCFStringEncodingUTF8);
url = CFURLCreateWithString(kCFAllocatorDefault, urlString, NULL);
```

## See Also

### Converting URLs to Other Representations

- [CFURLCreateData](<cfurlcreatedata(________).md>) — Creates a `CFData` object containing the content of a given URL.
- [CFURLCreateStringByReplacingPercentEscapes](<cfurlcreatestringbyreplacingpercentescapes(______).md>) — Creates a new string by replacing any percent escape sequences with their character equivalent.
- [CFURLCreateStringByReplacingPercentEscapesUsingEncoding](<cfurlcreatestringbyreplacingpercentescapesusingencoding(________).md>) — Creates a new string by replacing any percent escape sequences with their character equivalent. _(deprecated)_
- [CFURLGetFileSystemRepresentation](<cfurlgetfilesystemrepresentation(________).md>) — Fills a buffer with the file system’s native string representation of a given URL’s path.
- [CFURLGetFSRef](<cfurlgetfsref(____).md>) — Converts a given URL to a file or directory object. _(deprecated)_
- [CFURLGetString](<cfurlgetstring(__).md>) — Returns the URL as a `CFString` object.
