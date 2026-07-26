---
title: Inspecting Core Data Attributes
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/05/inspecting-core-data-attributes/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:18b00c7306a7e349'
translated: false
---

> 原文：[Inspecting Core Data Attributes](https://oleb.net/blog/2011/05/inspecting-core-data-attributes/)　·　Ole Begemann

# Inspecting Core Data Attributes

When you design your Core Data data model, you can choose between a whole bunch of data types for your attributes. In your managed object model, many of these data types (namely, Integer 16, Integer 32, Integer 64, Double, Float, and Bool) are modeled with a property of type `NSNumber *`.

What if, for some reason, you need to determine the underlying data type of a Core Data attribute in your code? Turns out this is quite easy using Core Data’s introspection APIs.

# NSEntityDescription

As you probably know, each entity in your Core Data model is represented by an instance of `NSEntityDescription`. So suppose you have an entity named “Person”:

```
NSEntityDescription *personEntity = [NSEntityDescription entityForName:@"Person" inManagedObjectContext:self.managedObjectContext];
```

# NSPropertyDescription and NSAttributeDescription

Following this pattern, each property an entity has is represented by an instance of a subclass of `NSPropertyDescription`, depending on the kind of property we are dealing with: attribute (represented by `NSAttributeDescription`), relationship (`NSRelationshipDescription`), or fetched property (`NSFetchedPropertyDescription`).

To iterate over all properties of your entity, do this:

```
for (NSPropertyDescription *property in eventEntity) {
    ...
}
```

If you are just interested in the entity’s attributes, the `-attributesByName` method returns a dictionary you can either iterate over or ask for a specific attribute. The `NSPropertyDescription` and `NSAttributeDescription` classes then offer methods to inspect the attribute’s properties, e.g. the `-attributeType`:

```
NSDictionary *attributes = [eventEntity attributesByName];
NSAttributeDescription *ageAttribute = [attributes objectForKey:@"age"];
if ([ageAttribute attributeType == NSInteger32AttributeType]) {
    // We have a 32-bit Integer
    ...
}
```

# NSAttributeType

Valid values for `NSAttributeType` are listed in the NSAttributeDescription.h header:

```
// types explicitly distinguish between bit sizes to ensure data store
// independence of the underlying operating system
enum {
    NSUndefinedAttributeType = 0,
    NSInteger16AttributeType = 100,
    NSInteger32AttributeType = 200,
    NSInteger64AttributeType = 300,
    NSDecimalAttributeType = 400,
    NSDoubleAttributeType = 500,
    NSFloatAttributeType = 600,
    NSStringAttributeType = 700,
    NSBooleanAttributeType = 800,
    NSDateAttributeType = 900,
    NSBinaryDataAttributeType = 1000
    // If your attribute is of NSTransformableAttributeType, the attributeValueClassName
    // must be set or attribute value class must implement NSCopying.
    , NSTransformableAttributeType = 1800
    , NSObjectIDAttributeType = 2000
};

typedef NSUInteger NSAttributeType;
```
