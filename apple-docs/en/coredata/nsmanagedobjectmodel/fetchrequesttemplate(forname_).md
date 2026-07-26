---
title: 'fetchRequestTemplate(forName:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectmodel/fetchrequesttemplate(forname:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/fetchrequesttemplate(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/fetchrequesttemplate%28forname%3A%29.json'
content_hash: 'sha256:9be40eb9840fbc06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# fetchRequestTemplate(forName:)

<sub>Instance Method</sub>

Returns the fetch request with a specified name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fetchRequestTemplate(forName name: String) -> NSFetchRequest<any NSFetchRequestResult>?
```

## Parameters

- `name` — A string containing the name of a fetch request template.

## Return Value

The fetch request named `name`.

## Discussion

If the template contains substitution variables, you should instead use [- fetchRequestFromTemplateWithName:substitutionVariables:](<fetchrequestfromtemplate(withname_substitutionvariables_).md>) to create a new fetch request.

## See Also

### Manipulating fetch request templates

- [fetchRequestTemplatesByName](fetchrequesttemplatesbyname.md) — A dictionary of the receiver’s fetch request templates, keyed by name.
- [- fetchRequestFromTemplateWithName:substitutionVariables:](<fetchrequestfromtemplate(withname_substitutionvariables_).md>) — Returns a copy of the fetch request template with the variables substituted by values from the substitutions dictionary.
- [- setFetchRequestTemplate:forName:](<setfetchrequesttemplate(__forname_).md>) — Associates the specified fetch request with the receiver using the given name.
