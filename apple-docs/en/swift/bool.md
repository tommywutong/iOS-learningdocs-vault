---
title: Bool
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/bool
source_url: 'https://developer.apple.com/documentation/swift/bool'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bool.json'
content_hash: 'sha256:699d501ca167991b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Bool

<sub>Structure</sub>

A value type whose instances are either `true` or `false`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Bool
```

## Overview

`Bool` represents Boolean values in Swift. Create instances of `Bool` by using one of the Boolean literals `true` or `false`, or by assigning the result of a Boolean method or operation to a variable or constant.

```swift
var godotHasArrived = false

let numbers = 1...5
let containsTen = numbers.contains(10)
print(containsTen)
// Prints "false"

let (a, b) = (100, 101)
let aFirst = a < b
print(aFirst)
// Prints "true"
```

Swift uses only simple Boolean values in conditional contexts to help avoid accidental programming errors and to help maintain the clarity of each control statement. Unlike in other programming languages, in Swift, integers and strings cannot be used where a Boolean value is required.

For example, the following code sample does not compile, because it attempts to use the integer `i` in a logical context:

```swift
var i = 5
while i {
    print(i)
    i -= 1
}
// error: Cannot convert value of type 'Int' to expected condition type 'Bool'
```

The correct approach in Swift is to compare the `i` value with zero in the `while` statement.

```swift
while i != 0 {
    print(i)
    i -= 1
}
```

## Using Imported Boolean values

The C `bool` and `Boolean` types and the Objective-C `BOOL` type are all bridged into Swift as `Bool`. The single `Bool` type in Swift guarantees that functions, methods, and properties imported from C and Objective-C have a consistent type interface.

## Relationships

- **Conforms To**: [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BNNSScalar](../accelerate/bnnsscalar.md), [BindableData](../realitykit/bindabledata.md), [BitwiseCopyable](bitwisecopyable.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](cvararg.md), [ConvertibleFromGeneratedContent](../foundationmodels/convertiblefromgeneratedcontent.md), [ConvertibleToBytes](convertibletobytes.md), [ConvertibleToGeneratedContent](../foundationmodels/convertibletogeneratedcontent.md), [Copyable](copyable.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByBooleanLiteral](expressiblebybooleanliteral.md), [Generable](../foundationmodels/generable.md), [Hashable](hashable.md), [InstructionsRepresentable](../foundationmodels/instructionsrepresentable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [LosslessStringConvertible](losslessstringconvertible.md), [MLDataValueConvertible](../createml/mldatavalueconvertible.md), [MLTensorScalar](../coreml/mltensorscalar.md), [MusicLibraryRequestFilterValueEquatable](../musickit/musiclibraryrequestfiltervalueequatable.md), [PromptRepresentable](../foundationmodels/promptrepresentable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [USDPrim.Attribute.MetadataValue](../usdkit/usdprim/attribute/metadatavalue.md), [USDPrim.Attribute.Value](../usdkit/usdprim/attribute/value.md), [USDValueProtocol](../usdkit/usdvalueprotocol.md)

## Topics

### Comparing Boolean Values

- [==(_:_:)](<bool/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [!=(_:_:)](<bool/!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.

### Transforming a Boolean

- [toggle()](<bool/toggle().md>) — Toggles the Boolean variable’s value.
- [!(_:)](<bool/!(__).md>) — Performs a logical NOT operation on a Boolean value.
- [||(_:_:)](<bool/__(____).md>) — Performs a logical OR operation on two Boolean values.
- [&&(_:_:)](<bool/&&(____).md>) — Performs a logical AND operation on two Boolean values.

### Creating a Random Value

- [random()](<bool/random().md>) — Returns a random Boolean value.
- [random(using:)](<bool/random(using_).md>) — Returns a random Boolean value, using the given generator as a source for randomness.

### Describing a Boolean

- [description](bool/description.md) — A textual representation of the Boolean value.

### Inspecting a Boolean

- [customMirror](bool/custommirror.md) — A mirror that reflects the `Bool` instance.
- [customPlaygroundQuickLook](bool/customplaygroundquicklook.md) — A custom playground Quick Look for the `Bool` instance. _(deprecated)_
- [hashValue](bool/hashvalue.md) — The hash value.
- [hash(into:)](<bool/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Creating a Boolean From Another Value

- [init(_:)](<bool/init(__)-25sp9.md>) — Creates an instance equal to the given Boolean value.
- [init(_:)](<bool/init(__)-83vgw.md>) — Creates a new Boolean value from the given string.

### Converting an NSNumber to a Boolean

- [init(_:)](<bool/init(__)-3mody.md>)
- [init(exactly:)](<bool/init(exactly_).md>)
- [init(truncating:)](<bool/init(truncating_).md>)

### Encoding and Decoding

- [init(from:)](<bool/init(from_).md>) — Creates a new instance by decoding from the given decoder.
- [encode(to:)](<bool/encode(to_).md>) — Encodes this value into the given encoder.

### Infrequently Used Intializers

- [init()](<bool/init().md>) — Creates an instance initialized to `false`.
- [init(booleanLiteral:)](<bool/init(booleanliteral_).md>) — Creates an instance initialized to the specified Boolean literal.

### Boolean Literals

- [true](true.md) — A true value.
- [false](false.md) — A false value.

### Structures

- [IntentDisplayName](bool/intentdisplayname.md)

### Type Aliases

- [Specification](bool/specification.md)
- [UnwrappedType](bool/unwrappedtype.md)
- [ValueType](bool/valuetype.md)

### Type Properties

- [defaultResolverSpecification](bool/defaultresolverspecification.md)

### Default Implementations

- [AtomicRepresentable Implementations](bool/atomicrepresentable-implementations.md)
- [CustomReflectable Implementations](bool/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](bool/customstringconvertible-implementations.md)
- [Decodable Implementations](bool/decodable-implementations.md)
- [Encodable Implementations](bool/encodable-implementations.md)
- [Equatable Implementations](bool/equatable-implementations.md)
- [ExpressibleByBooleanLiteral Implementations](bool/expressiblebybooleanliteral-implementations.md)
- [Hashable Implementations](bool/hashable-implementations.md)
- [LosslessStringConvertible Implementations](bool/losslessstringconvertible-implementations.md)
