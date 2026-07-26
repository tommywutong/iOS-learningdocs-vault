---
title: 'filterWithName:keysAndValues:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifilter-swift.class/filterwithname:keysandvalues:'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/filterwithname:keysandvalues:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/filterwithname%3Akeysandvalues%3A.json'
content_hash: 'sha256:d9443f4d6d71ae36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# filterWithName:keysAndValues:

<sub>Type Method</sub>

Creates a [CIFilter](../cifilter-swift.class.md) object for a specific kind of filter and initializes the input values with a `nil`-terminated list of arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIFilter *) filterWithName:(NSString *) name keysAndValues:(id) key0;
```

## Parameters

- `name` — The name of the filter. You must make sure the name is spelled correctly, otherwise your app will run but not produce any output images. For that reason, you should check for the existence of the filter after calling this method.

- `key0` — A list of key-value pairs to set as input values to the filter. Each key is a constant that specifies the name of the input value to set, and must be followed by a value. You signal the end of the list by passing a `nil` value.

## Return Value

A [CIFilter](../cifilter-swift.class.md) object whose input values are initialized.

## Discussion

As with all Objective-C methods that accept `nil`-terminated argument lists, to prevent unintended behavior you must take take care not to pass a `nil` value before the intended end of the argument list. You can avoid such issues by using the [init(name:withInputParameters:)](<init(name_withinputparameters_).md>) method to create a filter, expressing the parameter list as a dictionary literal.

## See Also

### Creating a filter

- [+ filterWithName:](<init(name_).md>) — Creates a [CIFilter](../cifilter-swift.class.md) object for a specific kind of filter.
