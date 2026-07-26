---
title: withoutOverwriting
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/writingoptions/withoutoverwriting
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/writingoptions/withoutoverwriting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/writingoptions/withoutoverwriting.json'
content_hash: 'sha256:fab5fc531a777584'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSData](../../nsdata.md) · [WritingOptions](../writingoptions.md)

# withoutOverwriting

<sub>Type Property</sub>

An option that attempts to write data to a file and fails with an error if the destination file already exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var withoutOverwriting: NSData.WritingOptions { get }
```

## Discussion

You can’t combine this constant with [NSDataWritingAtomic](atomic.md) because atomic allows the system to overwrite the original file.

## See Also

### Constants

- [NSDataWritingAtomic](atomic.md) — An option to write data to an auxiliary file first and then replace the original file with the auxiliary file when the write completes.
- [NSDataWritingFileProtectionNone](nofileprotection.md) — An option to not encrypt the file when writing it out.
- [NSDataWritingFileProtectionComplete](completefileprotection.md) — An option to make the file accessible only while the device is unlocked.
- [NSDataWritingFileProtectionCompleteUnlessOpen](completefileprotectionunlessopen.md) — An option to allow the file to be accessible while the device is unlocked or the file is already open.
- [NSDataWritingFileProtectionCompleteUntilFirstUserAuthentication](completefileprotectionuntilfirstuserauthentication.md) — An option to allow the file to be accessible after a user first unlocks the device.
- [NSDataWritingFileProtectionMask](fileprotectionmask.md) — An option the system uses when determining the file protection options that the system assigns to the data.
- [NSDataWritingFileProtectionCompleteWhenUserInactive](completefileprotectionwhenuserinactive.md) — An option to allow the file to be accessible after a user first unlocks the device.
