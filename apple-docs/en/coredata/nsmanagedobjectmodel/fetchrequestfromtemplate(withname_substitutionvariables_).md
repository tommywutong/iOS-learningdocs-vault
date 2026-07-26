---
title: 'fetchRequestFromTemplate(withName:substitutionVariables:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectmodel/fetchrequestfromtemplate(withname:substitutionvariables:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/fetchrequestfromtemplate(withname:substitutionvariables:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/fetchrequestfromtemplate%28withname%3Asubstitutionvariables%3A%29.json'
content_hash: 'sha256:c719aae5fd7e9e6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# fetchRequestFromTemplate(withName:substitutionVariables:)

<sub>Instance Method</sub>

Returns a copy of the fetch request template with the variables substituted by values from the substitutions dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fetchRequestFromTemplate(withName name: String, substitutionVariables variables: [String : Any]) -> NSFetchRequest<any NSFetchRequestResult>?
```

## Parameters

- `name` — A string containing the name of a fetch request template.

- `variables` — A dictionary containing key-value pairs where the keys are the names of variables specified in the template; the corresponding values are substituted before the fetch request is returned. The dictionary must provide values for all the variables in the template.

## Return Value

A copy of the fetch request template with the variables substituted by values from `variables`.

## Discussion

The `variables` dictionary must provide values for all the variables. If you want to test for a nil value, use `[NSNull null]`.

This method provides the usual way to bind an “abstractly” defined fetch request template to a concrete fetch. For more details on using this method, see [Creating Predicates](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pCreating.html#//apple_ref/doc/uid/TP40001793).

## See Also

### Manipulating fetch request templates

- [fetchRequestTemplatesByName](fetchrequesttemplatesbyname.md) — A dictionary of the receiver’s fetch request templates, keyed by name.
- [- fetchRequestTemplateForName:](<fetchrequesttemplate(forname_).md>) — Returns the fetch request with a specified name.
- [- setFetchRequestTemplate:forName:](<setfetchrequesttemplate(__forname_).md>) — Associates the specified fetch request with the receiver using the given name.
