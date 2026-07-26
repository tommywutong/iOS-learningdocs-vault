---
title: completeFileProtectionWhenUserInactive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/writingoptions/completefileprotectionwhenuserinactive
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/writingoptions/completefileprotectionwhenuserinactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/writingoptions/completefileprotectionwhenuserinactive.json'
content_hash: 'sha256:189630d44f5f23ab'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSData](../../nsdata.md) · [WritingOptions](../writingoptions.md)

# completeFileProtectionWhenUserInactive

<sub>Type Property</sub>

An option to allow the file to be accessible after a user first unlocks the device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static var completeFileProtectionWhenUserInactive: NSData.WritingOptions { get }
```

## Discussion

The app can read or write to the file while the device is unlocked, but while it’s booting up, the file has the protection equivalent to `NSDataWritingFileProtectionComplete`.

## See Also

### Constants

- [NSDataWritingAtomic](atomic.md) — An option to write data to an auxiliary file first and then replace the original file with the auxiliary file when the write completes.
- [NSDataWritingWithoutOverwriting](withoutoverwriting.md) — An option that attempts to write data to a file and fails with an error if the destination file already exists.
- [NSDataWritingFileProtectionNone](nofileprotection.md) — An option to not encrypt the file when writing it out.
- [NSDataWritingFileProtectionComplete](completefileprotection.md) — An option to make the file accessible only while the device is unlocked.
- [NSDataWritingFileProtectionCompleteUnlessOpen](completefileprotectionunlessopen.md) — An option to allow the file to be accessible while the device is unlocked or the file is already open.
- [NSDataWritingFileProtectionCompleteUntilFirstUserAuthentication](completefileprotectionuntilfirstuserauthentication.md) — An option to allow the file to be accessible after a user first unlocks the device.
- [NSDataWritingFileProtectionMask](fileprotectionmask.md) — An option the system uses when determining the file protection options that the system assigns to the data.
