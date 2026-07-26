---
title: checkingTypes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdatadetector/checkingtypes
source_url: 'https://developer.apple.com/documentation/foundation/nsdatadetector/checkingtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatadetector/checkingtypes.json'
content_hash: 'sha256:77fc9363f1af55e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDataDetector](../nsdatadetector.md)

# checkingTypes

<sub>Instance Property</sub>

Returns the checking types for the data detector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var checkingTypes: NSTextCheckingTypes { get }
```

## Discussion

The supported subset of checking types are specified in [CheckingType](../nstextcheckingresult/checkingtype.md). Those constants can be combined using the C-bitwise OR operator.

Currently, the supported data detectors `checkingTypes` are:  [NSTextCheckingTypeDate](../nstextcheckingresult/checkingtype/date.md), [NSTextCheckingTypeAddress](../nstextcheckingresult/checkingtype/address.md), [NSTextCheckingTypeLink](../nstextcheckingresult/checkingtype/link.md), `NSTextCheckingTypePhoneNumber`, and `NSTextCheckingTypeTransitInformation`.
