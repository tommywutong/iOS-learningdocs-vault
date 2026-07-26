---
title: 'readDataToEndOfFileAndReturnError:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilehandle/readdatatoendoffileandreturnerror:'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilehandle/readdatatoendoffileandreturnerror:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilehandle/readdatatoendoffileandreturnerror%3A.json'
content_hash: 'sha256:797127f771614ea4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# readDataToEndOfFileAndReturnError:

<sub>Instance Method</sub>

Reads the available data synchronously up to the end of file or maximum number of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSData *) readDataToEndOfFileAndReturnError:(NSError **) error;
```

## Parameters

- `error` — When the return value is `nil`, this provides an [NSError](../nserror.md) indicating why the read operation failed.

## Return Value

The data available through the file handle up to the maximum size that can be represented by an [NSData](../nsdata.md) object or, if a communications channel, until an end-of-file indicator is returned.

## Discussion

This method invokes [- readDataOfLength:](<../filehandle/readdata(oflength_).md>) as part of its implementation.

## See Also

### Reading from a file handle synchronously

- [availableData](../filehandle/availabledata.md) — The data currently available in the receiver.
- [readDataUpToLength:error:](readdatauptolength_error_.md) — Reads data synchronously up to the specified number of bytes.
