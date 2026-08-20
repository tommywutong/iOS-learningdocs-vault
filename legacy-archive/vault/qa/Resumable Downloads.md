---
title: Resumable Downloads
apple_id: DTS40011825
resource_type: QA
platform: watchOS|iOS|macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2012-02-13'
source_url: https://developer.apple.com/library/archive/qa/qa1761/_index.html
archived_at: '2026-07-18T02:34:39.792089Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1761

# Resumable Downloads

## Q:  My app downloads large files over HTTP. How can I resume a partially completed download?

A: The answer depends on your target platform:

- If you're working on Mac OS X it's easy to resume downloads using the NSURLDownload class. See the [URL Loading System Programming Guide](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/URLLoadingSystem/URLLoadingSystem.html#//apple_ref/doc/uid/10000165i) for more information about this.
- NSURLDownload is not supported on iOS. However, if you're a Newsstand app, Newsstand has built-in support for resuming downloads. See [Newsstand Kit Framework Reference](https://developer.apple.com/library/ios/#documentation/StoreKit/Reference/NewsstandKit_Framework/_index.html#//apple_ref/doc/uid/TP40010838) for the details.
- If you're a generic iOS app, you will have to write the code to resume downloads yourself, as explained below.

Resuming an HTTP download isn't too difficult, but you need to understand some critical HTTP concepts:

- __entity tag__ — This is a unique identifier provided by the server that denotes a specific version of a specific resource; if someone changes the resource on the server, the entity tag will change.
- __Range header__ — This allows you to request a specific range of bytes from a resource.
- __If-Range header__ — This header specifies that you only want to get a range of bytes from a resource if the entity tag hasn't changed.

The basic strategy for resuming a download is:

1. When you do the initial download, save the entity tag associated the resource.
2. As you save data to disk, remember how much of the data is valid.
3. When you come to resume the download, get the entity tag and the amount of data you've saved and apply these values to the request via the `Range` and `If-Range` headers.
4. Execute the request. It will either succeed (and you'll receive the remaining bytes of the resource) or it will fail (in which case you have to get the entire resource from scratch).

If the server doesn't support entity tags you can do similar things with the last-modified date.

For a concrete example of this, you can use a packet trace (see [Technical Q&A QA1176, 'Getting a Packet Trace'](https://developer.apple.com/library/mac/#qa/qa1176/_index.html)) to look at how Safari resumes a download on your Mac. Listing 1 shows a typical resume request.

__Listing 1__  An HTTP resume request

```
GET /download.info.apple.com/[...]/MacOSXUpdCombo10.6.8.dmg HTTP/1.1
Host: supportdownload.apple.com
User-Agent: Safari/7534.52.7 [...]
Accept: */*
If-Range: "968f3f3e86e0339ce722170ae656bc73:1319461845"
Range: bytes=4041400-
Accept-Language: en-au
Accept-Encoding: gzip, deflate
[...]
Connection: keep-alive
```

The `Range` header tells the server you want to get the data starting at offset 4041400. The `If-Range` header tells the server you only want that data if the data hasn't changed since the server gave the client the supplied entity tag (that is, "968f3f3e86e0339ce722170ae656bc73:1319461845").

Listing 2 shows the corresponding response.

__Listing 2__  An HTTP resume response

```
HTTP/1.1 206 Partial Content
Server: Apache
Accept-Ranges: bytes
Content-Type: application/octet-stream
Last-Modified: Mon, 24 Oct 2011 13:04:42 GMT
ETag: "968f3f3e86e0339ce722170ae656bc73:1319461845"
Date: Mon, 23 Jan 2012 16:13:25 GMT
Content-Range: bytes 4041400-1087036999/1087037000
Content-Length: 1082995600
Connection: keep-alive
```

The HTTP status (206) tells you that the response only contains a subset of the resource. The `Content-Range` header tells you exactly what range of the resource the server is returning (byte 4041400 through to byte 1087036999) and total length of the resource (1087037000). Finally, the `Content-Length` header tells you how many bytes the server is returning in this particular response.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-02-13 | New document that explains how to resume HTTP downloads. |

