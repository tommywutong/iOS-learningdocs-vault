---
title: MLShapedArray
framework: Core ML
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coreml/mlshapedarray
source_url: 'https://developer.apple.com/documentation/coreml/mlshapedarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreml/mlshapedarray.json'
content_hash: 'sha256:7bbdd4307a2e2e1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core ML](../coreml.md)

# MLShapedArray

<sub>Structure</sub>

A machine learning collection type that stores scalar values in a multidimensional array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MLShapedArray<Scalar> where Scalar : MLShapedArrayScalar
```

## Overview

A shaped array is a multidimensional array type that’s the Swift counterpart to [MLMultiArray](mlmultiarray.md). [MLShapedArray](mlshapedarray.md) is one of the underlying types of `MLFeatureValue` that stores scalar values. You can convert a shaped array to an [MLMultiArray](mlmultiarray.md) with its [init(_:)](<mlmultiarray/init(__)-wk41.md>) initializer, and convert back to a shaped array with its [init(_:)](<mlshapedarray/init(__).md>) initializer. All elements in an [MLShapedArray](mlshapedarray.md) are of the same type, and that type must conform to [MLShapedArrayScalar](mlshapedarrayscalar.md):

- [Int32](../swift/int32.md)
- [Float](../swift/float.md)
- [Double](../swift/double.md)

Each dimension in a shaped array is typically significant or meaningful. For example, a model could have an input that accepts images as a three-dimensional array of pixels, C x H x W. The first dimension, _C_,_ _represents the number of color channels, and the second and third dimensions, _H_ and _W_, represent the image’s height and width, respectively. The number of dimensions and size of each dimension define the shaped array’s _shape_.

> [!note] Note
> Some models use a one-dimensional multiarray for an input or output. This type of shaped array is conceptually identical to a conventional [Array](../swift/array.md).

A shaped array’s [shape](mlmultiarray/shape.md) property is an integer array in which each element defines the size of the corresponding dimension. To inspect the shape and constraints of a model’s multiarray input or output feature:

1. Access the model’s [modelDescription](mlmodel/modeldescription.md) property.
2. Find the multiarray input or output feature in the model description’s [inputDescriptionsByName](mlmodeldescription/inputdescriptionsbyname.md) or [outputDescriptionsByName](mlmodeldescription/outputdescriptionsbyname.md) property, respectively.
3. Access the feature description’s [multiArrayConstraint](mlfeaturedescription/multiarrayconstraint.md) property.
4. Inspect the multiarray constraint’s [shape](mlmultiarrayconstraint/shape.md) and [shapeConstraint](mlmultiarrayconstraint/shapeconstraint.md).

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [MLShapedArrayProtocol](mlshapedarrayprotocol.md), [MutableCollection](../swift/mutablecollection.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Creating a shaped array

- [init(scalar:)](<mlshapedarray/init(scalar_).md>) — Creates a shaped array with exactly one value and zero dimensions.
- [init(scalars:shape:)](<mlshapedarray/init(scalars_shape_).md>) — Initialize with a sequence and the shape.
- [init(mutating:shape:)](<mlshapedarray/init(mutating_shape_).md>) — Creates a new `MLShapedArray` using a pixel buffer as the backing storage.

### Creating a shaped array from another type

- [init(_:)](<mlshapedarray/init(__).md>)
- [init(concatenating:alongAxis:)](<mlshapedarray/init(concatenating_alongaxis_).md>) — Merges a sequence of shaped arrays into one shaped array along an axis.

### Creating a shaped array with pointers to memory

- [init(unsafeUninitializedShape:initializingWith:)](<mlshapedarray/init(unsafeuninitializedshape_initializingwith_).md>) — Creates a shaped array from a shape and a closure that initializes its memory.

### Creating a shaped array from data

- [init(data:shape:)](<mlshapedarray/init(data_shape_).md>) — Creates a shaped array from a block of data and a shape.
- [init(data:shape:strides:)](<mlshapedarray/init(data_shape_strides_).md>) — Creates a shaped array from a block of data, a shape, and strides.

### Shaping the array

- [changingLayout(to:)](<mlshapedarray/changinglayout(to_).md>) — Returns a copy with the specified buffer layout.
- [expandingShape(at:)](<mlshapedarray/expandingshape(at_).md>) — Returns a new shaped array with expanded dimensions.
- [reshaped(to:)](<mlshapedarray/reshaped(to_).md>) — Returns a new reshaped shaped array.
- [squeezingShape()](<mlshapedarray/squeezingshape().md>) — Returns a new squeezed shaped array.
- [transposed()](<mlshapedarray/transposed().md>) — Returns a new transposed shaped array.
- [transposed(permutation:)](<mlshapedarray/transposed(permutation_).md>) — Returns a transposed shaped array using a custom permutation.

### Reading and writing the pixel buffer

- [withMutablePixelBufferIfAvailable(_:)](<mlshapedarray/withmutablepixelbufferifavailable(__).md>) — Writes to the underlying pixel buffer.
- [withPixelBufferIfAvailable(_:)](<mlshapedarray/withpixelbufferifavailable(__).md>) — Reads the underlying pixel buffer.

### Modifying a shaped array

- [withUnsafeMutableShapedBufferPointer(using:_:)](<mlshapedarray/withunsafemutableshapedbufferpointer(using___).md>) — Calls the given closure with a pointer to the array’s mutable storage that has a specified buffer layout.

### Encoding and decoding

- [init(from:)](<mlshapedarray/init(from_).md>) — Creates a shaped array from a decoder.
- [encode(to:)](<mlshapedarray/encode(to_).md>) — Encode a shaped array.

### Default Implementations

- [CustomStringConvertible Implementations](mlshapedarray/customstringconvertible-implementations.md)
- [Decodable Implementations](mlshapedarray/decodable-implementations.md)
- [Encodable Implementations](mlshapedarray/encodable-implementations.md)

## See Also

### Supporting types

- [MLFeatureType](mlfeaturetype.md) — The possible types for feature values, input features, and output features.
- [MLShapedArrayProtocol](mlshapedarrayprotocol.md) — An interface that defines a shaped array type.
- [MLMultiArray](mlmultiarray.md) — A machine learning collection type that stores numeric values in an array with multiple dimensions.
- [MLSequence](mlsequence.md) — A machine learning collection type that stores a series of strings or integers.
