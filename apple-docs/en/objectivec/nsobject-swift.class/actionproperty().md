---
title: actionProperty()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/actionproperty()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/actionproperty()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/actionproperty%28%29.json'
content_hash: 'sha256:80eeb5c00fe6f977'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# actionProperty()

<sub>Instance Method</sub>

Sent to the delegate to request the property the action applies to.

<sub>macOS</sub>

```swift
func actionProperty() -> String!
```

## Return Value

The property that the action applies to.

## Discussion

See [Table 1The documentation for property-list constants](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/AccessingData.html#//apple_ref/doc/uid/20001023-136659) for the properties for person and group records.
