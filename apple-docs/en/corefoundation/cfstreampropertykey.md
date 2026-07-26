---
title: CFStreamPropertyKey
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstreampropertykey
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreampropertykey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreampropertykey.json'
content_hash: 'sha256:016865782a729326'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStreamPropertyKey

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFStreamPropertyKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [kCFStreamPropertyAppendToFile](cfstreampropertykey/appendtofile.md) — Value is a `CFBoolean` value that indicates whether to append the written data to a file, if it already exists, rather than to replace its contents.
- [kCFStreamPropertyDataWritten](cfstreampropertykey/datawritten.md) — Value is a `CFData` object that contains all the bytes written to a writable memory stream. You cannot modify this value.
- [kCFStreamPropertyFileCurrentOffset](cfstreampropertykey/filecurrentoffset.md) — Value is a `CFNumber` object containing the current file offset.
- [kCFStreamPropertySocketNativeHandle](cfstreampropertykey/socketnativehandle.md) — Value is a `CFData` object that contains the native handle for a socket stream—of type [CFSocketNativeHandle](cfsocketnativehandle.md)—to which the socket stream is connected.
- [kCFStreamPropertySocketRemoteHostName](cfstreampropertykey/socketremotehostname.md) — Value is a `CFString` object containing the name of the host to which the socket stream is connected or `NULL` if unknown.
- [kCFStreamPropertySocketRemotePortNumber](cfstreampropertykey/socketremoteportnumber.md) — Value is a `CFNumber` object containing the remote port number to which the socket stream is connected or `NULL` if unknown.

### Initializers

- [init(_:)](<cfstreampropertykey/init(__).md>)
- [init(rawValue:)](<cfstreampropertykey/init(rawvalue_).md>)

## See Also

### Data Types

- [CFAllocatorTypeID](cfallocatortypeid.md)
- [CFCalendarIdentifier](cfcalendaridentifier.md)
- [CFDateFormatterKey](cfdateformatterkey.md)
- [CFErrorDomain](cferrordomain.md)
- [CFLocaleIdentifier](cflocaleidentifier.md)
- [CFLocaleKey](cflocalekey.md)
- [CFNotificationName](cfnotificationname.md)
- [CFNumberFormatterKey](cfnumberformatterkey.md)
- [CFRunLoopMode](cfrunloopmode.md)
- [CFTypeRef](cftyperef.md) — An untyped “generic” reference to any Core Foundation object.
