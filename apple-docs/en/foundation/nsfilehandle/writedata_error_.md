---
title: 'writeData:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilehandle/writedata:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilehandle/writedata:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilehandle/writedata%3Aerror%3A.json'
content_hash: 'sha256:5e2feb903cddd56d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# writeData:error:

<sub>Instance Method</sub>

Writes the specified data synchronously to the file handle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) writeData:(NSData *) data error:(NSError **) error;
```

## Parameters

- `data` — The data to write to the file handle.

- `error` — When the return value is [false](../../swift/false.md), this provides an [NSError](../nserror.md) indicating why the write operation failed.

## Return Value

Returns [true](../../swift/true.md) when the data is successfullly written to the file handle.

## Discussion

If the handle represents a file, writing takes place at the file pointer’s current position. After it writes the data, the method advances the file pointer by the number of bytes written. This method provides an error if the file descriptor is closed or isn’t valid, if the handle represents an unconnected pipe or socket endpoint, if there isn’t any free space on the file system, or if any other writing error occurs.

## See Also

### Related Documentation

- [availableData](../filehandle/availabledata.md) — The data currently available in the receiver.
- [readDataUpToLength:error:](readdatauptolength_error_.md) — Reads data synchronously up to the specified number of bytes.
- [readDataToEndOfFileAndReturnError:](readdatatoendoffileandreturnerror_.md) — Reads the available data synchronously up to the end of file or maximum number of bytes.
