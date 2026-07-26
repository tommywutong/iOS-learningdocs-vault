---
title: 'dataDetectorWithTypes:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdatadetector/datadetectorwithtypes:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdatadetector/datadetectorwithtypes:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatadetector/datadetectorwithtypes%3Aerror%3A.json'
content_hash: 'sha256:16a4104c150441a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDataDetector](../nsdatadetector.md)

# dataDetectorWithTypes:error:

<sub>Type Method</sub>

Creates and returns a new data detector instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSDataDetector *) dataDetectorWithTypes:(NSTextCheckingTypes) checkingTypes error:(NSError **) error;
```

## Parameters

- `checkingTypes` — The checking types. The supported checking types are a subset of the types specified in [CheckingType](../nstextcheckingresult/checkingtype.md). Those constants can be combined using the C-bitwise OR operator.

- `error` — An out parameter that if an error occurs during initialization contains the encountered error.

## Return Value

Returns the newly initialized data detector. If an error was encountered returns `nil`, and `error` contains the error.

## Discussion

Currently, the supported data detectors `checkingTypes` are:  [NSTextCheckingTypeDate](../nstextcheckingresult/checkingtype/date.md), [NSTextCheckingTypeAddress](../nstextcheckingresult/checkingtype/address.md), [NSTextCheckingTypeLink](../nstextcheckingresult/checkingtype/link.md), `NSTextCheckingTypePhoneNumber`, and `NSTextCheckingTypeTransitInformation`.

## See Also

### Related Documentation

- [checkingTypes](checkingtypes.md) — Returns the checking types for the data detector.

### Creating data detector instances

- [- initWithTypes:error:](<init(types_).md>) — Initializes and returns a data detector instance.
