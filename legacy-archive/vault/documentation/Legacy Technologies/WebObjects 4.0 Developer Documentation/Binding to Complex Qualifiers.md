---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.08.html
archived_at: '2026-07-15T07:58:02.477642Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](Changes%20to%20EOModeler.md)

# Binding to Complex Qualifiers

In Enterprise Objects Framework 3.0, you can bind user interface elements directly to variables in a complex qualifier that you created using the new Query Builder in EOModeler.
For example, suppose you want to create a WebObjects application that allows users to perform a complex query on the Movies entity in the Movies database. Suppose you want to allow users to query on the title, the date released, and the studio. You could use the __queryMatch__, __queryMin__, and __queryMax__ support in display group to easily construct such query. For example:

```
(title = $title) AND (dateReleased = $date) AND (studio = $studio)
```


However, __queryMatch__ support is limited to ANDed criteria; it isn't sufficient for more complex queries such as:

```
(title = $title) OR (dateReleased = $date) OR (studio = $studio)
```


For this qualifier you could define the qualifier in EOModeler and then bind to it in your user interface. In general, you would set this up by following these steps:

- In EOModeler, open the Movies model file and select the Movies entity.
- Create a fetch specification associated with the Movies entity by clicking the New Fetch Specification button.
- Use Query Builder's user interface to set up a query on the __title__, __dateReleased__, and __studio__ attributes of the entity (see the section "[Query Builder](Changes%20to%20EOModeler.md#apple-hazteoa)"). On the right side of each expression, use a $ syntax to denote the qualifier variable. For example, your fetch specification might look like this:

```
(title = $title) OR (dateReleased = $date) OR (studio = $studio)
```


Depending on the type of graphical user interface you build, you access the fetch specification's query bindings differently. In WebObjects Builder, you access the query bindings in the following way:

- Use WebObjects builder to create a component that allows the user to enter the query criteria. You might create text fields for the title and date released and a pop-up list for the studio, for example.
- Drag the fetch specification from EOModeler into your component. This has the effect of creating a new display group for your specification's entity.
- Choose "Add and Configure."
- Configure the new display group, setting its fetch specification to the one you defined in your model.
- In WebObjects Builder, bind the user interface elements to the __queryBindings.title__, __queryBindings.date__, and __queryBindings.studio__ keys of your display group (__movieDisplayGroup__, for example).

In Interface Builder, the steps are similar except that you bind the user interface elements to __@bindings.title__, __@bindings.date__, and __@bindings.studio__ keys of your display group. The @bindings syntax represents the value associated with the named qualifier variable.
Qualifier bindings are also useful when you want to bind a value to more than one qualifier component as in the following:

```
(title like $searchString) OR (description like $searchString)
```


In this example, __searchString__ could contain a user-provided keyword surrounded with wildcard characters.
The following tables describe the API added to support binding to complex qualifiers.

|  EOFetchSpecification |  EOFetchSpecification |
|  fetchSpecificationWithQualifierBindings: |  Returns a new fetch specification created by resolving the bindings for the fetch specification's qualifier using the bindings dictionary passed as an argument to this method. |
|  requiresAllQualifierBindingVariables and setRequiresAllQualifierBindingVariables:  |  Returns or sets whether a missing binding is ignored or whether it raises or throws an exception. If requiresAllQualifierBindingVariables is YES or true, a missing binding raises or throws an EOQualifierVariableSubstitutionException during variable substitution. If NO or false, any nodes for which there are no bindings should be pruned from the qualifier. The default is NO or false. |

```
```

|  EOQualifier |  EOQualifier |
|  qualifierWithBindings:requiresAllVariables: (Objective-C)  qualifierWithBindings(NSDictionary, Boolean) (Java) |  Returns a new qualifier created by substituting all EOQualifierVariables with the values contained in the provided argument. The object passed to this method is an NSDictionary containing the values to which the EOQualifierVariables are bound. (Typically the values are those entered by the user in the user interface fields.)  If the second argument (a boolean value) is YES or true, then the new qualifier requires all its variables (meaning that if a value is not found for a variable in the provided object, an EOQualifierVariableSubstitutionException is raised or thrown). If the second argument is NO or false, then the new qualifier doesn't require all its variables; and if any variable is not found in the bindings dictionary (that is, the user has left that field blank), the node containing that variable is simply pruned from the qualifier tree. |
|  bindingKeys |  Returns an array of strings representing the binding keys for the EOQualifierVariables contained in this qualifier. For example, if you have a qualifier such as "dateReleased = $date", this method returns an array containing the single string "date". Multiple occurrences of the same variable only appear once in this list. |
|  keyPathForBindingKey: |  Returns the lefthand side of a qualifier binding. For example, if you have a qualifier such as "movie.dateReleased = $date", this method returns "movie.dateReleased" for the key "date". |

```
```

|  EOClassDescription |  EOClassDescription |
|  defaultFormatterForKeyPath: |  Similar to defaultFormatterForKey:, except this method takes a key path (roles.roleName, for example). |

```
```

|  EODataSource |  EODataSource |
|  qualifierBindingKeys |  Returns an array of strings representing all of the binding keys from the fetch specification's qualifier and the data source's auxiliary qualifier. |
|  qualifierBindings and setQualifierBindings: |  Returns or sets the NSDictionary containing the bindings that will be used for variable replacement on the fetch specification's qualifier and the auxiliary qualifier before the fetch is executed. The keys to the dictionary are the keys returned by qualifierBindingKeys. The values are typically the values that the application's user entered through the user interface. |

```
```

|  New Exception |  New Exception |
|  EOQualifierVariableSubstitutionException |  Raised or thrown when the EOFetchSpecification's requiresAllQualifierBindingVariables is YES or true and a value for one of the variables in the qualifier is missing from the bindings object. |

```
```

[!Table of Contents](Table%20of%20Contents-2.md) [!Next Section](Merging%20Object%20Changes.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
