---
title: NSData.WritingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/writingoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/writingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/writingoptions.json'
content_hash: 'sha256:40482ec2c7bc7190'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# NSData.WritingOptions

<sub>Structure</sub>

Options for methods used to write data objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct WritingOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<writingoptions/init(rawvalue_).md>)

### Constants

- [NSDataWritingAtomic](writingoptions/atomic.md) — An option to write data to an auxiliary file first and then replace the original file with the auxiliary file when the write completes.
- [NSDataWritingWithoutOverwriting](writingoptions/withoutoverwriting.md) — An option that attempts to write data to a file and fails with an error if the destination file already exists.
- [NSDataWritingFileProtectionNone](writingoptions/nofileprotection.md) — An option to not encrypt the file when writing it out.
- [NSDataWritingFileProtectionComplete](writingoptions/completefileprotection.md) — An option to make the file accessible only while the device is unlocked.
- [NSDataWritingFileProtectionCompleteUnlessOpen](writingoptions/completefileprotectionunlessopen.md) — An option to allow the file to be accessible while the device is unlocked or the file is already open.
- [NSDataWritingFileProtectionCompleteUntilFirstUserAuthentication](writingoptions/completefileprotectionuntilfirstuserauthentication.md) — An option to allow the file to be accessible after a user first unlocks the device.
- [NSDataWritingFileProtectionMask](writingoptions/fileprotectionmask.md) — An option the system uses when determining the file protection options that the system assigns to the data.
- [NSDataWritingFileProtectionCompleteWhenUserInactive](writingoptions/completefileprotectionwhenuserinactive.md) — An option to allow the file to be accessible after a user first unlocks the device.

### Legacy Constants

- [NSAtomicWrite](writingoptions/atomicwrite.md) — An option that attempts to write data to an auxiliary file first and then exchange the files. _(deprecated)_
- [NSAtomicWrite](writingoptions/atomicwrite.md) — An option that attempts to write data to an auxiliary file first and then exchange the files. _(deprecated)_

### Entitlements

- [Data Protection Entitlement](../../bundleresources/entitlements/com.apple.developer.default-data-protection.md) — The level of data protection for sensitive user data when an app accesses it on a device.

### Instance Methods

- [contains(_:)](<writingoptions/contains(__).md>)
- [formIntersection(_:)](<writingoptions/formintersection(__).md>)
- [formSymmetricDifference(_:)](<writingoptions/formsymmetricdifference(__).md>)
- [formUnion(_:)](<writingoptions/formunion(__).md>)
- [insert(_:)](<writingoptions/insert(__).md>)
- [isSubset(of:)](<writingoptions/issubset(of_).md>)
- [remove(_:)](<writingoptions/remove(__).md>)

## See Also

### Writing Data to a File

- [- writeToFile:atomically:](<write(tofile_atomically_).md>) — Writes the data object’s bytes to the file specified by a given path.
- [- writeToFile:options:error:](<write(tofile_options_).md>) — Writes the data object’s bytes to the file specified by a given path.
- [- writeToURL:atomically:](<write(to_atomically_).md>) — Writes the data object’s bytes to the location specified by a given URL.
- [- writeToURL:options:error:](<write(to_options_).md>) — Writes the data object’s bytes to the location specified by a given URL.
