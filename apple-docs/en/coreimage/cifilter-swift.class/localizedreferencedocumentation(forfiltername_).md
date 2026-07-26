---
title: 'localizedReferenceDocumentation(forFilterName:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifilter-swift.class/localizedreferencedocumentation(forfiltername:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/localizedreferencedocumentation(forfiltername:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/localizedreferencedocumentation%28forfiltername%3A%29.json'
content_hash: 'sha256:b7e595e1fabc1a3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# localizedReferenceDocumentation(forFilterName:)

<sub>Type Method</sub>

Returns the location of the localized reference documentation that describes the filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func localizedReferenceDocumentation(forFilterName filterName: String) -> URL?
```

## Parameters

- `filterName` — The filter name.

## Return Value

A URL that specifies the location of the localized documentation, or `nil` if the filter does not provide localized reference documentation.

## Discussion

The URL can be a local file or a remote document on a web server. Because filters created prior to OS X v10.5 could return `nil`, you should be make sure that your code handles this case gracefully.

## See Also

### Getting localized information for registered filters

- [+ localizedNameForFilterName:](<localizedname(forfiltername_).md>) — Returns the localized name for the specified filter name.
- [+ localizedNameForCategory:](<localizedname(forcategory_).md>) — Returns  the localized name for the specified filter category.
- [+ localizedDescriptionForFilterName:](<localizeddescription(forfiltername_).md>) — Returns the localized description of a filter for display in the user interface.
