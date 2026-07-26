---
title: 'setFetchRequestTemplate(_:forName:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectmodel/setfetchrequesttemplate(_:forname:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/setfetchrequesttemplate(_:forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/setfetchrequesttemplate%28_%3Aforname%3A%29.json'
content_hash: 'sha256:d21ef0efc104750d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# setFetchRequestTemplate(_:forName:)

<sub>Instance Method</sub>

Associates the specified fetch request with the receiver using the given name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setFetchRequestTemplate(_ fetchRequestTemplate: NSFetchRequest<any NSFetchRequestResult>?, forName name: String)
```

## Parameters

- `fetchRequestTemplate` — A fetch request, typically containing predicates with variables for substitution.

- `name` — A string that specifies the name of the fetch request template.

## Discussion

For more details on using this method, see [Creating Predicates](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pCreating.html#//apple_ref/doc/uid/TP40001793).

### Special Considerations

This method raises an exception if the receiver has been used by an object graph manager.

## See Also

### Manipulating fetch request templates

- [fetchRequestTemplatesByName](fetchrequesttemplatesbyname.md) — A dictionary of the receiver’s fetch request templates, keyed by name.
- [- fetchRequestTemplateForName:](<fetchrequesttemplate(forname_).md>) — Returns the fetch request with a specified name.
- [- fetchRequestFromTemplateWithName:substitutionVariables:](<fetchrequestfromtemplate(withname_substitutionvariables_).md>) — Returns a copy of the fetch request template with the variables substituted by values from the substitutions dictionary.
