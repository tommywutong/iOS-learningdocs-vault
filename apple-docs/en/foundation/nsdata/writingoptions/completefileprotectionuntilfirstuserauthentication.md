---
title: completeFileProtectionUntilFirstUserAuthentication
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/writingoptions/completefileprotectionuntilfirstuserauthentication
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/writingoptions/completefileprotectionuntilfirstuserauthentication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/writingoptions/completefileprotectionuntilfirstuserauthentication.json'
content_hash: 'sha256:67953cb022866dd0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSData](../../nsdata.md) · [WritingOptions](../writingoptions.md)

# completeFileProtectionUntilFirstUserAuthentication

<sub>Type Property</sub>

An option to allow the file to be accessible after a user first unlocks the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var completeFileProtectionUntilFirstUserAuthentication: NSData.WritingOptions { get }
```

## Discussion

In this case, the app can read or write to the file while the device is unlocked, but while it’s booting up, the file has the protection equivalent to [NSDataWritingFileProtectionComplete](completefileprotection.md).

## See Also

### Constants

- [NSDataWritingAtomic](atomic.md) — An option to write data to an auxiliary file first and then replace the original file with the auxiliary file when the write completes.
- [NSDataWritingWithoutOverwriting](withoutoverwriting.md) — An option that attempts to write data to a file and fails with an error if the destination file already exists.
- [NSDataWritingFileProtectionNone](nofileprotection.md) — An option to not encrypt the file when writing it out.
- [NSDataWritingFileProtectionComplete](completefileprotection.md) — An option to make the file accessible only while the device is unlocked.
- [NSDataWritingFileProtectionCompleteUnlessOpen](completefileprotectionunlessopen.md) — An option to allow the file to be accessible while the device is unlocked or the file is already open.
- [NSDataWritingFileProtectionMask](fileprotectionmask.md) — An option the system uses when determining the file protection options that the system assigns to the data.
- [NSDataWritingFileProtectionCompleteWhenUserInactive](completefileprotectionwhenuserinactive.md) — An option to allow the file to be accessible after a user first unlocks the device.
