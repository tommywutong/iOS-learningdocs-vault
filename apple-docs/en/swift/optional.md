---
title: Optional
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/optional
source_url: 'https://developer.apple.com/documentation/swift/optional'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional.json'
content_hash: 'sha256:dae2f9d8dc43abe8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Optional

<sub>Enumeration</sub>

A type that represents either a wrapped value or the absence of a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum Optional<Wrapped> where Wrapped : ~Copyable, Wrapped : ~Escapable
```

## Overview

You use the `Optional` type whenever you use optional values, even if you never type the word `Optional`. Swift’s type system usually shows the wrapped type’s name with a trailing question mark (`?`) instead of showing the full type name. For example, if a variable has the type `Int?`, that’s just another way of writing `Optional<Int>`. The shortened form is preferred for ease of reading and writing code.

The types of `shortForm` and `longForm` in the following code sample are the same:

```swift
let shortForm: Int? = Int("42")
let longForm: Optional<Int> = Int("42")
```

The `Optional` type is an enumeration with two cases. `Optional.none` is equivalent to the `nil` literal. `Optional.some(Wrapped)` stores a wrapped value. For example:

```swift
let number: Int? = Optional.some(42)
let noNumber: Int? = Optional.none
print(noNumber == nil)
// Prints "true"
```

You must unwrap the value of an `Optional` instance before you can use it in many contexts. Because Swift provides several ways to safely unwrap optional values, you can choose the one that helps you write clear, concise code.

The following examples use this dictionary of image names and file paths:

```swift
let imagePaths = ["star": "/glyphs/star.png",
                  "portrait": "/images/content/portrait.jpg",
                  "spacer": "/images/shared/spacer.gif"]
```

Getting a dictionary’s value using a key returns an optional value, so `imagePaths["star"]` has type `Optional<String>` or, written in the preferred manner, `String?`.

## Optional Binding

To conditionally bind the wrapped value of an `Optional` instance to a new variable, use one of the optional binding control structures, including `if let`, `guard let`, and `switch`.

```swift
if let starPath = imagePaths["star"] {
    print("The star image is at '\(starPath)'")
} else {
    print("Couldn't find the star image")
}
// Prints "The star image is at '/glyphs/star.png'"
```

## Optional Chaining

To safely access the properties and methods of a wrapped instance, use the postfix optional chaining operator (postfix `?`). The following example uses optional chaining to access the `hasSuffix(_:)` method on a `String?` instance.

```swift
if imagePaths["star"]?.hasSuffix(".png") == true {
    print("The star image is in PNG format")
}
// Prints "The star image is in PNG format"
```

## Using the Nil-Coalescing Operator

Use the nil-coalescing operator (`??`) to supply a default value in case the `Optional` instance is `nil`. Here a default path is supplied for an image that is missing from `imagePaths`.

```swift
let defaultImagePath = "/images/default.png"
let heartPath = imagePaths["heart"] ?? defaultImagePath
print(heartPath)
// Prints "/images/default.png"
```

The `??` operator also works with another `Optional` instance on the right-hand side. As a result, you can chain multiple `??` operators together.

```swift
let shapePath = imagePaths["cir"] ?? imagePaths["squ"] ?? defaultImagePath
print(shapePath)
// Prints "/images/default.png"
```

## Unconditional Unwrapping

When you’re certain that an instance of `Optional` contains a value, you can unconditionally unwrap the value by using the forced unwrap operator (postfix `!`). For example, the result of the failable `Int` initializer is unconditionally unwrapped in the example below.

```swift
let number = Int("42")!
print(number)
// Prints "42"
```

You can also perform unconditional optional chaining by using the postfix `!` operator.

```swift
let isPNG = imagePaths["star"]!.hasSuffix(".png")
print(isPNG)
// Prints "true"
```

Unconditionally unwrapping a `nil` instance with `!` triggers a runtime error.

## Relationships

- **Conforms To**: [AccessibilityRotorContent](../swiftui/accessibilityrotorcontent.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [AttachmentContent](../realitykit/attachmentcontent.md), [AttributedTextFormattingDefinition](../swiftui/attributedtextformattingdefinition.md), [AxisContent](../charts/axiscontent.md), [AxisMark](../charts/axismark.md), [BitwiseCopyable](bitwisecopyable.md), [Chart3DContent](../charts/chart3dcontent.md), [ChartContent](../charts/chartcontent.md), [Commands](../swiftui/commands.md), [ConvertibleToGeneratedContent](../foundationmodels/convertibletogeneratedcontent.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomReflectable](customreflectable.md), [CustomTestStringConvertible](../testing/customteststringconvertible.md), [CustomizableToolbarContent](../swiftui/customizabletoolbarcontent.md), [Decodable](decodable.md), [DecodableWithConfiguration](../foundation/decodablewithconfiguration.md), [DynamicInstructions](../foundationmodels/dynamicinstructions.md), [Encodable](encodable.md), [EncodableWithConfiguration](../foundation/encodablewithconfiguration.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByNilLiteral](expressiblebynilliteral.md), [Gesture](../swiftui/gesture.md), [Hashable](hashable.md), [InstructionsRepresentable](../foundationmodels/instructionsrepresentable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [MapContent](../mapkit/mapcontent.md), [PromptRepresentable](../foundationmodels/promptrepresentable.md), [RelationshipCollection](../swiftdata/relationshipcollection.md), [SceneAccessoryContent](../swiftui/sceneaccessorycontent.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [SliderTickContent](../swiftui/slidertickcontent.md), [StoreContent](../storekit/storecontent.md), [TabContent](../swiftui/tabcontent.md), [TableColumnContent](../swiftui/tablecolumncontent.md), [TableRowContent](../swiftui/tablerowcontent.md), [ToolbarContent](../swiftui/toolbarcontent.md), [View](../swiftui/view.md)

## Topics

### Creating an Optional Value

- [Optional.some(_:)](<optional/some(__).md>) — The presence of a value, stored as `Wrapped`.
- [init(_:)](<optional/init(__).md>) — Creates an instance that stores the given value.

### Creating a Nil Value

- [Optional.none](optional/none.md) — The absence of a value.
- [init(nilLiteral:)](<optional/init(nilliteral_).md>) — Creates an instance initialized with `nil`.

### Transforming an Optional Value

- [map(_:)](<optional/map(__).md>) — Evaluates the given closure when this `Optional` instance is not `nil`, passing the unwrapped value as a parameter.
- [flatMap(_:)](<optional/flatmap(__).md>) — Evaluates the given closure when this `Optional` instance is not `nil`, passing the unwrapped value as a parameter.

### Coalescing Nil Values

- [??(_:_:)](<__(____)-9xjze.md>) — Performs a nil-coalescing operation, returning the wrapped value of an `Optional` instance or a default value.
- [??(_:_:)](<__(____)-1fjjj.md>) — Performs a nil-coalescing operation, returning the wrapped value of an `Optional` instance or a default `Optional` value.

### Comparing Optional Values

- [~=(_:_:)](<optional/~=(____).md>) — Returns a Boolean value indicating whether an argument matches `nil`.

### Encoding and Decoding

- [encode(to:)](<optional/encode(to_).md>) — Encodes this optional value into the given encoder.
- [init(from:)](<optional/init(from_).md>) — Creates a new instance by decoding from the given decoder.

### Inspecting an Optional

- [hash(into:)](<optional/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.
- [unsafelyUnwrapped](optional/unsafelyunwrapped.md) — The wrapped value of this instance, unwrapped without checking whether the instance is `nil`.
- [debugDescription](optional/debugdescription.md) — A textual representation of this instance, suitable for debugging.
- [customMirror](optional/custommirror.md) — The custom mirror for this instance.

### Publishing an Optional

- [publisher](optional/publisher-swift.property.md) — A Combine publisher that publishes this instance’s value to each subscriber exactly once, if it has any value at all.
- [Publisher](optional/publisher-swift.struct.md) — The type of a Combine publisher that publishes the value of a Swift optional instance to each subscriber exactly once, if the instance has any value at all.

### Deprecated

- [hashValue](optional/hashvalue.md) — The hash value.

### Operators

- [!=(_:_:)](<optional/!=(____)-6y4t6.md>) — Returns a Boolean value indicating whether the right-hand-side argument is not `nil`.
- [!=(_:_:)](<optional/!=(____)-9e46a.md>) — Returns a Boolean value indicating whether the left-hand-side argument is not `nil`.
- [==(_:_:)](<optional/==(____)-1j2c8.md>) — Returns a Boolean value indicating whether the right-hand-side argument is `nil`.
- [==(_:_:)](<optional/==(____)-2tyup.md>) — Returns a Boolean value indicating whether the left-hand-side argument is `nil`.

### Instance Methods

- [take()](<optional/take().md>) — Takes the wrapped value being stored in this instance and returns it while also setting the instance to `nil`. If there is no value being stored in this instance, this returns `nil` instead.

### Type Aliases

- [PartiallyGenerated](optional/partiallygenerated.md)
- [Specification](optional/specification.md)
- [TableRowBody](optional/tablerowbody.md)
- [TicksCollection](optional/tickscollection.md)
- [UnwrappedType](optional/unwrappedtype.md)
- [ValueType](optional/valuetype.md)

### Type Properties

- [defaultResolverSpecification](optional/defaultresolverspecification.md)

### Default Implementations

- [AtomicRepresentable Implementations](optional/atomicrepresentable-implementations.md)
- [CustomDebugStringConvertible Implementations](optional/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](optional/customreflectable-implementations.md)
- [Decodable Implementations](optional/decodable-implementations.md)
- [Encodable Implementations](optional/encodable-implementations.md)
- [Equatable Implementations](optional/equatable-implementations.md)
- [ExpressibleByNilLiteral Implementations](optional/expressiblebynilliteral-implementations.md)
- [Hashable Implementations](optional/hashable-implementations.md)
- [IntentValueConvertible Implementations](optional/intentvalueconvertible-implementations.md)
- [IntentValueExpressing Implementations](optional/intentvalueexpressing-implementations.md)
