---
title: completeFileProtection
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/writingoptions/completefileprotection
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/writingoptions/completefileprotection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/writingoptions/completefileprotection.json'
content_hash: 'sha256:957a237af09eade2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSData](../../nsdata.md) · [WritingOptions](../writingoptions.md)

# completeFileProtection

<sub>Type Property</sub>

An option to make the file accessible only while the device is unlocked.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var completeFileProtection: NSData.WritingOptions { get }
```

## Discussion

In this case, the system stores the file in an encrypted format and your app may only read or write to the file while the device is unlocked. At all other times, any  attempts your app makes to read and write the file will fail.

## See Also

### Constants

- [NSDataWritingAtomic](atomic.md) — An option to write data to an auxiliary file first and then replace the original file with the auxiliary file when the write completes.
- [NSDataWritingWithoutOverwriting](withoutoverwriting.md) — An option that attempts to write data to a file and fails with an error if the destination file already exists.
- [NSDataWritingFileProtectionNone](nofileprotection.md) — An option to not encrypt the file when writing it out.
- [NSDataWritingFileProtectionCompleteUnlessOpen](completefileprotectionunlessopen.md) — An option to allow the file to be accessible while the device is unlocked or the file is already open.
- [NSDataWritingFileProtectionCompleteUntilFirstUserAuthentication](completefileprotectionuntilfirstuserauthentication.md) — An option to allow the file to be accessible after a user first unlocks the device.
- [NSDataWritingFileProtectionMask](fileprotectionmask.md) — An option the system uses when determining the file protection options that the system assigns to the data.
- [NSDataWritingFileProtectionCompleteWhenUserInactive](completefileprotectionwhenuserinactive.md) — An option to allow the file to be accessible after a user first unlocks the device.
