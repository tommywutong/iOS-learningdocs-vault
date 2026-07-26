---
title: 'localizedDescription(forFilterName:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifilter-swift.class/localizeddescription(forfiltername:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/localizeddescription(forfiltername:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/localizeddescription%28forfiltername%3A%29.json'
content_hash: 'sha256:cdcaf1ef50b6a9e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# localizedDescription(forFilterName:)

<sub>Type Method</sub>

Returns the localized description of a filter for display in the user interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func localizedDescription(forFilterName filterName: String) -> String?
```

## Parameters

- `filterName` — The filter name.

## Return Value

The localized description of the filter.

## See Also

### Getting localized information for registered filters

- [+ localizedNameForFilterName:](<localizedname(forfiltername_).md>) — Returns the localized name for the specified filter name.
- [+ localizedNameForCategory:](<localizedname(forcategory_).md>) — Returns  the localized name for the specified filter category.
- [+ localizedReferenceDocumentationForFilterName:](<localizedreferencedocumentation(forfiltername_).md>) — Returns the location of the localized reference documentation that describes the filter.
