---
title: PlaceDescriptor
framework: GeoToolbox
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/geotoolbox/placedescriptor
source_url: 'https://developer.apple.com/documentation/geotoolbox/placedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/geotoolbox/placedescriptor.json'
content_hash: 'sha256:06ccc4d8ab02943e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [GeoToolbox](../geotoolbox.md)

# PlaceDescriptor

<sub>Structure</sub>

A structure that contains identifying information about a place that a mapping service may use to attempt to find rich place information such as phone numbers, websites, and so on.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PlaceDescriptor
```

## Discussion

A [PlaceDescriptor](placedescriptor.md) allows you to construct a collection of metadata about a place, including at least one [PlaceRepresentation](placedescriptor/placerepresentation.md) which contains common geographic concepts like an address or coordinate. `PlaceDescriptor` may optionally include a [supportingRepresentations](placedescriptor/supportingrepresentations.md) which contains identifiers that match the place for mapping service providers. Use `PlaceDescriptor` in conjunction with a mapping service to request rich information about a place.

For example to create a [PlaceDescriptor](placedescriptor.md) that describes an address with a common name use [init(representations:commonName:supportingRepresentations:)](<placedescriptor/init(representations_commonname_supportingrepresentations_).md>) as shown here.

```swift
    let fountain = PlaceDescriptor(
        representations: [.address("121-122 James's St \n Dublin 8 \n D08 ET27 \n Ireland")],
        commonName: "Obelisk Fountain"
    )
```

You can also initialize a `PlaceDescriptor` using an [MKMapItem](../mapkit/mkmapitem.md) as shown below.

```swift
    guard let descriptor = PlaceDescriptor(item: myMapItem) else {
        return
    }
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomLocalizedStringResourceConvertible](../foundation/customlocalizedstringresourceconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [DisplayRepresentable](../appintents/displayrepresentable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [InstanceDisplayRepresentable](../appintents/instancedisplayrepresentable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [PersistentlyIdentifiable](../appintents/persistentlyidentifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TypeDisplayRepresentable](../appintents/typedisplayrepresentable.md)

## Topics

### Creating place descriptors

- [init(representations:commonName:supportingRepresentations:)](<placedescriptor/init(representations_commonname_supportingrepresentations_).md>) — Creates a place descriptor, suitable for use when searching or retrieving rich data about a place.
- [init(item:)](<placedescriptor/init(item_).md>) — Creates a place descriptor from a map item.

### Getting the attributes of a place descriptor

- [commonName](placedescriptor/commonname.md) — Publicly known name of the area or place of interest.
- [address](placedescriptor/address.md) — A full address, that one could use in postal or administrative scenarios.
- [coordinate](placedescriptor/coordinate.md) — The latitude and longitude for a place.
- [representations](placedescriptor/representations.md) — An array of representations of the place using common mapping concepts.
- [supportingRepresentations](placedescriptor/supportingrepresentations.md) — An array of proprietary or non-uniform representations of the place, such as representations you can use with other mapping services.
- [serviceIdentifier(for:)](<placedescriptor/serviceidentifier(for_).md>) — Retrieves the identifier for the specified service provider, if available.

### Enumeration values that describe places and mapping service representations

- [PlaceRepresentation](placedescriptor/placerepresentation.md) — Values that represent a physical place, suitable for use when searching or retrieving rich data.
- [SupportingPlaceRepresentation](placedescriptor/supportingplacerepresentation.md) — Values that describe the representation of a physical place using proprietary attributes, such as an alphanumeric location identifier from a mapping service provider.

### Type Aliases

- [Specification](placedescriptor/specification.md)
- [UnwrappedType](placedescriptor/unwrappedtype.md)
- [ValueType](placedescriptor/valuetype.md)

### Type Properties

- [defaultResolverSpecification](placedescriptor/defaultresolverspecification.md)
