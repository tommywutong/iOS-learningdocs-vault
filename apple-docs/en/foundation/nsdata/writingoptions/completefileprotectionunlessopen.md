---
title: completeFileProtectionUnlessOpen
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/writingoptions/completefileprotectionunlessopen
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/writingoptions/completefileprotectionunlessopen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/writingoptions/completefileprotectionunlessopen.json'
content_hash: 'sha256:8c90a6c2e0ca95db'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSData](../../nsdata.md) · [WritingOptions](../writingoptions.md)

# completeFileProtectionUnlessOpen

<sub>Type Property</sub>

An option to allow the file to be accessible while the device is unlocked or the file is already open.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var completeFileProtectionUnlessOpen: NSData.WritingOptions { get }
```

## Discussion

In this case, your app cannot open the file to read it or write to it when the device is locked, but your app can create new files with this class. If one of these files is open when the device is locked, your app can read and write to the opened file.

## See Also

### Constants

- [NSDataWritingAtomic](atomic.md) — An option to write data to an auxiliary file first and then replace the original file with the auxiliary file when the write completes.
- [NSDataWritingWithoutOverwriting](withoutoverwriting.md) — An option that attempts to write data to a file and fails with an error if the destination file already exists.
- [NSDataWritingFileProtectionNone](nofileprotection.md) — An option to not encrypt the file when writing it out.
- [NSDataWritingFileProtectionComplete](completefileprotection.md) — An option to make the file accessible only while the device is unlocked.
- [NSDataWritingFileProtectionCompleteUntilFirstUserAuthentication](completefileprotectionuntilfirstuserauthentication.md) — An option to allow the file to be accessible after a user first unlocks the device.
- [NSDataWritingFileProtectionMask](fileprotectionmask.md) — An option the system uses when determining the file protection options that the system assigns to the data.
- [NSDataWritingFileProtectionCompleteWhenUserInactive](completefileprotectionwhenuserinactive.md) — An option to allow the file to be accessible after a user first unlocks the device.
