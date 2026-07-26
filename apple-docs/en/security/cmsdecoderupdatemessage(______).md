---
title: 'CMSDecoderUpdateMessage(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecoderupdatemessage(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecoderupdatemessage(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecoderupdatemessage%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:dd08756e2aa89bad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderUpdateMessage(_:_:_:)

<sub>Function</sub>

Feeds raw bytes of the message to be decoded into the decoder.

<sub>macOS</sub>

```swift
func CMSDecoderUpdateMessage(_ cmsDecoder: CMSDecoder, _ msgBytes: UnsafeRawPointer, _ msgBytesLen: Int) -> OSStatus
```

## Parameters

- `cmsDecoder` — The CMSDecoder reference returned by the `CMSDecoderCreate` function.

- `msgBytes` — A pointer to the data to be decoded.

- `msgBytesLen` — The length of the data, in bytes.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). Returns [errSecUnknownFormat](errsecunknownformat.md) upon detection of an improperly formatted CMS message.

## Discussion

This function can be called multiple times. Call the `CMSDecoderFinalizeMessage` function when you have no more data to decode.

## See Also

### Related Documentation

- [CMSDecoderCreate](<cmsdecodercreate(__).md>) — Creates a CMSDecoder reference.
