---
title: fetchRequestTemplatesByName
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectmodel/fetchrequesttemplatesbyname
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/fetchrequesttemplatesbyname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/fetchrequesttemplatesbyname.json'
content_hash: 'sha256:243f190cf190c5a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# fetchRequestTemplatesByName

<sub>Instance Property</sub>

A dictionary of the receiver’s fetch request templates, keyed by name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fetchRequestTemplatesByName: [String : NSFetchRequest<any NSFetchRequestResult>] { get }
```

## Discussion

If the template contains a predicate with substitution variables, you should instead use [- fetchRequestFromTemplateWithName:substitutionVariables:](<fetchrequestfromtemplate(withname_substitutionvariables_).md>) to create a new fetch request.

## See Also

### Manipulating fetch request templates

- [- fetchRequestTemplateForName:](<fetchrequesttemplate(forname_).md>) — Returns the fetch request with a specified name.
- [- fetchRequestFromTemplateWithName:substitutionVariables:](<fetchrequestfromtemplate(withname_substitutionvariables_).md>) — Returns a copy of the fetch request template with the variables substituted by values from the substitutions dictionary.
- [- setFetchRequestTemplate:forName:](<setfetchrequesttemplate(__forname_).md>) — Associates the specified fetch request with the receiver using the given name.
