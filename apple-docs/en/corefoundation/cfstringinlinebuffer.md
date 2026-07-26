---
title: CFStringInlineBuffer
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstringinlinebuffer
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringinlinebuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringinlinebuffer.json'
content_hash: 'sha256:8f717e88119e3f7e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringInlineBuffer

<sub>Structure</sub>

Defines the buffer and related fields used for in-line buffer access of characters in CFString objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFStringInlineBuffer
```

## Overview

This structure is used for in-line buffer access of characters contained by a CFString object. Use the [CFStringInitInlineBuffer](<cfstringinitinlinebuffer(______).md>) function for initializing the fields of this structure; do not do it manually. Once the buffer is initialized, use the [CFStringGetCharacterFromInlineBuffer](<cfstringgetcharacterfrominlinebuffer(____).md>) function to access characters from the buffer. Do not access the fields directly as they might change between releases.

The only reason this structure is not opaque is to allow the in-line functions to access its fields.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfstringinlinebuffer/init().md>)
- [init(buffer:theString:directUniCharBuffer:directCStringBuffer:rangeToBuffer:bufferedRangeStart:bufferedRangeEnd:)](<cfstringinlinebuffer/init(buffer_thestring_directunicharbuffer_directcstringbuffer_rangetobuffer_bufferedrangestart_bufferedrangeend_).md>)

### Instance Properties

- [buffer](cfstringinlinebuffer/buffer.md)
- [bufferedRangeEnd](cfstringinlinebuffer/bufferedrangeend.md)
- [bufferedRangeStart](cfstringinlinebuffer/bufferedrangestart.md)
- [directCStringBuffer](cfstringinlinebuffer/directcstringbuffer.md)
- [directUniCharBuffer](cfstringinlinebuffer/directunicharbuffer.md)
- [rangeToBuffer](cfstringinlinebuffer/rangetobuffer.md)
- [theString](cfstringinlinebuffer/thestring.md)

## See Also

### Data Types

- [CFStringEncoding](cfstringencoding.md) — An integer type for constants used to specify supported string encodings in various CFString functions.
- [CFStringEncodings](cfstringencodings.md) — Index type for constants used to specify external string encodings.
- [CFStringCompareFlags](cfstringcompareflags.md) — A [CFOptionFlags](cfoptionflags.md) type for specifying options for string comparison .
