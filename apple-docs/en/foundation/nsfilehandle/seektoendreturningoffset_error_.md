---
title: 'seekToEndReturningOffset:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilehandle/seektoendreturningoffset:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilehandle/seektoendreturningoffset:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilehandle/seektoendreturningoffset%3Aerror%3A.json'
content_hash: 'sha256:8f7d4a387564a8e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# seekToEndReturningOffset:error:

<sub>Instance Method</sub>

Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) seekToEndReturningOffset:(unsigned long long *) offsetInFile error:(NSError **) error;
```

## Parameters

- `offsetInFile` — When the return value is [true](../../swift/true.md), this provides the file pointer’s offset at the end of the file. This should therefore equal to the size of the file.

- `error` — When the return value is [false](../../swift/false.md), this provides an [NSError](../nserror.md) indicating why the operation failed.

## Return Value

Returns [false](../../swift/false.md) when there was an error. Otherwise, returns  [true](../../swift/true.md) and sets the `offsetInFile` parameter’s pointee to the current position of the file pointer within the file.

## Discussion

Returns [false](../../swift/false.md) if called on a file handle representing a pipe or socket, or if the file descriptor is closed.

## See Also

### Seeking within a file

- [getOffset:error:](getoffset_error_.md) — Get the current position of the file pointer within the file.
- [- seekToOffset:error:](<../filehandle/seek(tooffset_).md>) — Moves the file pointer to the specified offset within the file.
