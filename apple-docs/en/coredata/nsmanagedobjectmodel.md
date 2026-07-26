---
title: NSManagedObjectModel
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectmodel
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel.json'
content_hash: 'sha256:fced4d6bce4f31a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSManagedObjectModel

<sub>Class</sub>

A programmatic representation of the `.xcdatamodeld` file describing your objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSManagedObjectModel
```

## Overview

The model contains one or more `NSEntityDescription` objects representing the entities in the schema. Each `NSEntityDescription` object has property description objects (instances of subclasses of [NSPropertyDescription](nspropertydescription.md)) that represent the properties (or fields) of the entity in the schema. The Core Data framework uses this description in several ways:

- Constraining UI creation in Interface Builder
- Validating attribute and relationship values at runtime
- Mapping between your managed objects and a database or file-based schema for object persistence

A managed object model maintains a mapping between each of its entity objects and a corresponding managed object class for use with the persistent storage mechanisms in the Core Data framework. You can determine the entity for a particular managed object with the `entity` method.

You typically create managed object models using the data modeling tool in Xcode, but it’s possible to build a model programmatically if needed.

### Loading a model file

Managed object model files are typically stored in a project or a framework. To load a model, you provide an URL to the constructor. Note that loading a model doesn’t have the effect of loading all of its entities.

### Storing fetch requests

Frequently, you need a collection of objects that share features in common. Sometimes you can define those features (property values) in advance; sometimes you need to be able to supply values at runtime. For example, suppose you want to retrieve all movies owned by Pixar, or retrieve all movies that earned more than an amount specified by the user at runtime.

Fetch requests are often predefined in a managed object model as templates. They allow you to predefine named queries and their parameters in the model. Typically they contain variables that need to be substituted at runtime. `NSManagedObjectModel` provides an API to retrieve a stored fetch request by name, and to perform variable substitution—see [- fetchRequestTemplateForName:](<nsmanagedobjectmodel/fetchrequesttemplate(forname_).md>) and [- fetchRequestFromTemplateWithName:substitutionVariables:](<nsmanagedobjectmodel/fetchrequestfromtemplate(withname_substitutionvariables_).md>).

You typically define fetch request templates using the Data Model editor in Xcode. You can also create fetch request templates programmatically, and associate them with a model using [- setFetchRequestTemplate:forName:](<nsmanagedobjectmodel/setfetchrequesttemplate(__forname_).md>).

### Supporting multiple configurations for the same model

You may want to specify different sets of entities for the same model to be used in different situations. For example, suppose certain entities should only be available if a user has administrative privileges. To support this requirement, a model may have more than one configuration. Each configuration is named, and has an associated set of entities. The sets may overlap. You establish configurations programmatically using [- setEntities:forConfiguration:](<nsmanagedobjectmodel/setentities(__forconfigurationname_).md>) or using the Xcode design tool, and retrieve the entities for a given configuration name using [- entitiesForConfiguration:](<nsmanagedobjectmodel/entities(forconfigurationname_).md>).

### Changing models

Because a model describes the structure of the data in a persistent store, changing any parts of a model that alters the schema renders it incompatible with (and so unable to open) the stores it previously created. If you change your schema, you therefore need to migrate the data in existing stores to new version (see [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)). For example, if you add a new entity or a new attribute to an existing entity, you _can’t_ open old stores; if you add a validation constraint or set a new default value for an attribute, you _can_ open old stores.

### Editing models at runtime

Managed object models are editable until they are used by an object graph manager (a managed object context or a persistent store coordinator). This allows you to create or modify them dynamically until their first use. However, once a model is being used, it _must not_ be changed. This is enforced at runtime—when the object manager first fetches data using a model, the whole of that model becomes uneditable. Any attempt to mutate a model or any of its sub-objects after that point throws an exception. If you need to modify a model that’s in use, create a copy, modify the copy, and then discard the objects with the old model.

### Enumerating entities with fast enumeration

In macOS 10.5 and later and on iOS, `NSManagedObjectModel` supports the [NSFastEnumeration](../foundation/nsfastenumeration.md) protocol. You can use this to enumerate over a model’s entities, as illustrated in the following example:

```objc
NSManagedObjectModel *aModel = ...;
for (NSEntityDescription *entity in aModel) {
    // entity is each instance of NSEntityDescription in aModel in turn
}
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSFastEnumeration](../foundation/nsfastenumeration.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a managed object model

- [- initWithContentsOfURL:](<nsmanagedobjectmodel/init(contentsof_).md>) — Initializes the managed object model using the model file at the specified URL.
- [- init](<nsmanagedobjectmodel/init().md>) — Initializes an empty managed object model.
- [+ mergedModelFromBundles:](<nsmanagedobjectmodel/mergedmodel(from_).md>) — Returns a model created by merging all the models found in given bundles.
- [+ mergedModelFromBundles:forStoreMetadata:](<nsmanagedobjectmodel/mergedmodel(from_forstoremetadata_).md>) — Returns a merged model from a specified array for the version information in provided metadata.
- [+ modelByMergingModels:](<nsmanagedobjectmodel/init(bymerging_).md>) — Creates a single model from an array of existing models.
- [+ modelByMergingModels:forStoreMetadata:](<nsmanagedobjectmodel/init(bymerging_forstoremetadata_).md>) — Returns, for the version information in given metadata, a model merged from a given array of models.

### Managing entities and configurations

- [entities](nsmanagedobjectmodel/entities.md) — The entities in the model.
- [entitiesByName](nsmanagedobjectmodel/entitiesbyname.md) — The entities of the model, keyed by name.
- [configurations](nsmanagedobjectmodel/configurations.md) — All the available configuration names of the model.
- [- entitiesForConfiguration:](<nsmanagedobjectmodel/entities(forconfigurationname_).md>) — Returns the entities of the model for a specified configuration.
- [- setEntities:forConfiguration:](<nsmanagedobjectmodel/setentities(__forconfigurationname_).md>) — Associates the specified entities with the model using the given configuration name.

### Manipulating fetch request templates

- [fetchRequestTemplatesByName](nsmanagedobjectmodel/fetchrequesttemplatesbyname.md) — A dictionary of the receiver’s fetch request templates, keyed by name.
- [- fetchRequestTemplateForName:](<nsmanagedobjectmodel/fetchrequesttemplate(forname_).md>) — Returns the fetch request with a specified name.
- [- fetchRequestFromTemplateWithName:substitutionVariables:](<nsmanagedobjectmodel/fetchrequestfromtemplate(withname_substitutionvariables_).md>) — Returns a copy of the fetch request template with the variables substituted by values from the substitutions dictionary.
- [- setFetchRequestTemplate:forName:](<nsmanagedobjectmodel/setfetchrequesttemplate(__forname_).md>) — Associates the specified fetch request with the receiver using the given name.

### Handling localization

- [localizationDictionary](nsmanagedobjectmodel/localizationdictionary.md) — The localization dictionary of the model.

### Versioning and migrating entities

- [versionChecksum](nsmanagedobjectmodel/versionchecksum.md) — The Base64-encoded 128-bit model version hash.
- [versionIdentifiers](nsmanagedobjectmodel/versionidentifiers.md) — The set of developer-defined version identifiers for the object model.
- [entityVersionHashesByName](nsmanagedobjectmodel/entityversionhashesbyname.md) — The dictionary of the model’s entity names and their corresponding version hashes.
- [- isConfiguration:compatibleWithStoreMetadata:](<nsmanagedobjectmodel/isconfiguration(withname_compatiblewithstoremetadata_).md>) — Returns a Boolean value that indicates whether a given configuration in the model is compatible with given metadata from a persistent store.

### Working with indexes

- [NSFetchIndexElementType](nsfetchindexelementtype.md) — Defines the possible types of index elements.
- [NSFetchIndexDescription](nsfetchindexdescription.md) — The description of the index.
- [NSFetchIndexElementDescription](nsfetchindexelementdescription.md) — Description of an Index Element

### Initializers

- [init(byMergingModels:)](<nsmanagedobjectmodel/init(bymergingmodels_).md>)
- [init(byMergingModels:forStoreMetadata:)](<nsmanagedobjectmodel/init(bymergingmodels_forstoremetadata_).md>)
- [init(coder:)](<nsmanagedobjectmodel/init(coder_).md>)
- [init(contentsOfURL:)](<nsmanagedobjectmodel/init(contentsofurl_).md>)

### Type Methods

- [makeManagedObjectModel(for:mergedWith:)](<nsmanagedobjectmodel/makemanagedobjectmodel(for_mergedwith_)-2tc31.md>)
- [makeManagedObjectModel(for:mergedWith:)](<nsmanagedobjectmodel/makemanagedobjectmodel(for_mergedwith_)-37opo.md>)
- [makeManagedObjectModel(for:mergedWith:)](<nsmanagedobjectmodel/makemanagedobjectmodel(for_mergedwith_)-7lqq9.md>)

## See Also

### Object Modeling

- [NSEntityDescription](nsentitydescription.md) — A description of a Core Data entity.
- [NSPropertyDescription](nspropertydescription.md) — A description of a single property belonging to an entity.
- [NSAttributeDescription](nsattributedescription.md) — A description of a single attribute belonging to an entity.
- [NSDerivedAttributeDescription](nsderivedattributedescription.md) — A description of an attribute that derives its value by performing a calculation on a related attribute.
- [NSRelationshipDescription](nsrelationshipdescription.md) — A description of a relationship between two entities.
