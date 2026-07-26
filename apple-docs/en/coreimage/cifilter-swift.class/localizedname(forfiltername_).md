---
title: 'localizedName(forFilterName:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifilter-swift.class/localizedname(forfiltername:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/localizedname(forfiltername:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/localizedname%28forfiltername%3A%29.json'
content_hash: 'sha256:c66f3a96e211b875'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# localizedName(forFilterName:)

<sub>Type Method</sub>

Returns the localized name for the specified filter name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func localizedName(forFilterName filterName: String) -> String?
```

## Parameters

- `filterName` — A filter name.

## Return Value

The localized name for the filter.

## See Also

### Getting localized information for registered filters

- [+ localizedNameForCategory:](<localizedname(forcategory_).md>) — Returns  the localized name for the specified filter category.
- [+ localizedDescriptionForFilterName:](<localizeddescription(forfiltername_).md>) — Returns the localized description of a filter for display in the user interface.
- [+ localizedReferenceDocumentationForFilterName:](<localizedreferencedocumentation(forfiltername_).md>) — Returns the location of the localized reference documentation that describes the filter.
