---
title: NSValue
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsvalue
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue.json'
content_hash: 'sha256:1ac5fb53987e663b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSValue

<sub>Class</sub>

A simple container for a single C or Objective-C data item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSValue
```

## Overview

An [NSValue](nsvalue.md) object can hold any of the scalar types such as `int`, `float`, and `char`, as well as pointers, structures, and object `id` references. Use this class to work with such data types in collections (such as [NSArray](nsarray.md) and [NSSet](nsset.md)), [Key-value coding](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25), and other APIs that require Objective-C objects. [NSValue](nsvalue.md) objects are always immutable.

### Subclassing Notes

The abstract [NSValue](nsvalue.md) class is the public interface of a class cluster consisting mostly of private, concrete classes that create and return a value object appropriate for a given situation. It is possible to subclass [NSValue](nsvalue.md), but doing so requires providing storage facilities for the value (which is not inherited by subclasses) and implementing two primitive methods.

#### Methods to Override

Any subclass of [NSValue](nsvalue.md) _must_ override the primitive instance methods [- getValue:](<nsvalue/getvalue(__).md>) and [objCType](nsvalue/objctype.md). These methods must operate on the storage that you provide for the value.

You might want to implement an initializer for your subclass that is suited to the storage you provide. The [NSValue](nsvalue.md) class does not have a designated initializer, so your initializer need only invoke the [init()](<../objectivec/nsobject-swift.class/init().md>) method of `super`. The [NSValue](nsvalue.md) class adopts the [NSCopying](nscopying.md) and [NSSecureCoding](nssecurecoding.md) protocols; if you want instances of your own custom subclass created from copying or coding, override the methods in these protocols.

You may also wish to implement the [hash](../objectivec/nsobjectprotocol/hash.md) method to make your subclass work well in collections.

#### Alternatives to Subclassing

If you need only to use [NSValue](nsvalue.md) objects for wrap a custom data types or structures defined by your app, you need not create an [NSValue](nsvalue.md) subclass. Instead, create a category that uses existing [NSValue](nsvalue.md) methods to store and retrieve data of your custom type. For example, the code below defines a custom Polyhedron structure and creates [NSValue](nsvalue.md) convenience methods to store and retrieve it:

```objc
typedef struct {
    int numFaces;
    float radius;
} Polyhedron;
 
@interface NSValue (Polyhedron)
+ (instancetype)valuewithPolyhedron:(Polyhedron)value;
@property (readonly) Polyhedron polyhedronValue;
@end
 
@implementation NSValue (Polyhedron)
+ (instancetype)valuewithPolyhedron:(Polyhedron)value
{
    return [self valueWithBytes:&value objCType:@encode(Polyhedron)];
}
- (Polyhedron) polyhedronValue
{
    Polyhedron value;
    [self getValue:&value];
    return value;
}
@end
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSNumber](nsnumber.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Working with Raw Values

- [- initWithBytes:objCType:](<nsvalue/init(bytes_objctype_).md>) — Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.
- [+ value:withObjCType:](<nsvalue/init(__withobjctype_).md>) — Creates a value object containing the specified value, interpreted with the specified Objective-C type.
- [- getValue:](<nsvalue/getvalue(__).md>) — Copies the value into the specified buffer. _(deprecated)_
- [objCType](nsvalue/objctype.md) — A C string containing the Objective-C type of the data contained in the value object.

### Working with Pointer and Object Values

- [+ valueWithPointer:](<nsvalue/init(pointer_).md>) — Creates a value object containing the specified pointer.
- [+ valueWithNonretainedObject:](<nsvalue/init(nonretainedobject_).md>) — Creates a value object containing the specified object.
- [pointerValue](nsvalue/pointervalue.md) — Returns the value as an untyped pointer.
- [nonretainedObjectValue](nsvalue/nonretainedobjectvalue.md) — The value as a non-retained pointer to an object.

### Working with Range Values

- [+ valueWithRange:](<nsvalue/init(range_).md>) — Creates a new value object containing the specified Foundation range structure.
- [rangeValue](nsvalue/rangevalue.md) — The Foundation range structure representation of the value.

### Working with Foundation Geometry Values

- [+ valueWithPoint:](<nsvalue/init(point_).md>) — Creates a new value object containing the specified Foundation point structure.
- [+ valueWithSize:](<nsvalue/init(size_).md>) — Creates a new value object containing the specified Foundation size structure.
- [+ valueWithRect:](<nsvalue/init(rect_).md>) — Creates a new value object containing the specified Foundation rectangle structure.
- [pointValue](nsvalue/pointvalue.md) — The Foundation point structure representation of the value.
- [sizeValue](nsvalue/sizevalue.md) — The Foundation size structure representation of the value.
- [rectValue](nsvalue/rectvalue.md) — The Foundation rectangle structure representation of the value.

### Working with CoreGraphics Geometry Values

- [+ valueWithCGPoint:](<nsvalue/init(cgpoint_).md>) — Creates a new value object containing the specified CoreGraphics point structure.
- [+ valueWithCGVector:](<nsvalue/init(cgvector_).md>) — Creates a new value object containing the specified CoreGraphics vector structure.
- [+ valueWithCGSize:](<nsvalue/init(cgsize_).md>) — Creates a new value object containing the specified CoreGraphics size structure.
- [+ valueWithCGRect:](<nsvalue/init(cgrect_).md>) — Creates a new value object containing the specified CoreGraphics rectangle structure.
- [+ valueWithCGAffineTransform:](<nsvalue/init(cgaffinetransform_).md>) — Creates a new value object containing the specified CoreGraphics affine transform structure.
- [CGPointValue](nsvalue/cgpointvalue.md) — Returns the CoreGraphics point structure representation of the value.
- [CGVectorValue](nsvalue/cgvectorvalue.md) — Returns the CoreGraphics vector structure representation of the value.
- [CGSizeValue](nsvalue/cgsizevalue.md) — Returns the CoreGraphics size structure representation of the value.
- [CGRectValue](nsvalue/cgrectvalue.md) — Returns the CoreGraphics rectangle structure representation of the value.
- [CGAffineTransformValue](nsvalue/cgaffinetransformvalue.md) — Returns the CoreGraphics affine transform representation of the value.

### Working with UIKit Geometry Values

- [+ valueWithUIEdgeInsets:](<nsvalue/init(uiedgeinsets_).md>) — Creates a new value object containing the specified UIKit edge insets structure.
- [+ valueWithUIOffset:](<nsvalue/init(uioffset_).md>) — Creates a new value object containing the specified UIKit offset structure.
- [UIEdgeInsetsValue](nsvalue/uiedgeinsetsvalue.md) — Returns the UIKit edge insets structure representation of the value.
- [UIOffsetValue](nsvalue/uioffsetvalue.md) — Returns the UIKit offset structure representation of the value.

### Working with CoreAnimation Transform Values

- [+ valueWithCATransform3D:](<nsvalue/init(catransform3d_).md>) — Creates a new value object containing the specified CoreAnimation transform structure.
- [CATransform3DValue](nsvalue/catransform3dvalue.md) — The CoreAnimation transform structure representation of the value.

### Working with Media Time Values

- [+ valueWithCMTime:](<nsvalue/init(cmtime_).md>) — Creates a new value object containing the specified CoreMedia time structure.
- [+ valueWithCMTimeRange:](<nsvalue/init(cmtimerange_).md>) — Creates a new value object containing the specified CoreMedia time range structure.
- [+ valueWithCMTimeMapping:](<nsvalue/init(cmtimemapping_).md>) — Creates a new value object containing the specified CoreMedia time mapping structure.
- [CMTimeValue](nsvalue/timevalue.md) — The CoreMedia time structure representation of the value.
- [CMTimeRangeValue](nsvalue/timerangevalue.md) — The CoreMedia time range structure representation of the value.
- [CMTimeMappingValue](nsvalue/timemappingvalue.md) — The CoreMedia time mapping structure representation of the value.

### Working with Geographic Coordinate Values

- [+ valueWithMKCoordinate:](<nsvalue/init(mkcoordinate_).md>) — Creates a new value object containing the specified CoreLocation geographic coordinate structure.
- [+ valueWithMKCoordinateSpan:](<nsvalue/init(mkcoordinatespan_).md>) — Creates a new value object containing the specified MapKit coordinate span structure.
- [MKCoordinateValue](nsvalue/mkcoordinatevalue.md) — The CoreLocation geographic coordinate structure representation of the value.
- [MKCoordinateSpanValue](nsvalue/mkcoordinatespanvalue.md) — The MapKit coordinate span structure representation of the value.

### Working with SceneKit Vector and Matrix Values

- [+ valueWithSCNVector3:](<nsvalue/init(scnvector3_).md>) — Creates a value object that contains the specified three-element SceneKit vector.
- [+ valueWithSCNVector4:](<nsvalue/init(scnvector4_).md>) — Creates a value object that contains the specified four-element SceneKit vector.
- [+ valueWithSCNMatrix4:](<nsvalue/init(scnmatrix4_).md>) — Creates a value object that contains the specified SceneKit 4 x 4 matrix.
- [SCNVector3Value](nsvalue/scnvector3value.md) — The three-element Scene Kit vector representation of the value.
- [SCNVector4Value](nsvalue/scnvector4value.md) — The four-element Scene Kit vector representation of the value.
- [SCNMatrix4Value](nsvalue/scnmatrix4value.md) — The Scene Kit 4 x 4 matrix representation of the value.

### Comparing Value Objects

- [- isEqualToValue:](<nsvalue/isequal(to_).md>) — Returns a Boolean value that indicates whether the value object and another value object are equal.

### Initializers

- [+ valueWithCMVideoDimensions:](<nsvalue/init(cmvideodimensions_).md>)
- [+ valueWithGCPoint2:](<nsvalue/init(gcpoint2_).md>)
- [- initWithCoder:](<nsvalue/init(coder_).md>)
- [+ valueWithDirectionalEdgeInsets:](<nsvalue/init(directionaledgeinsets_).md>)
- [+ valueWithEdgeInsets:](<nsvalue/init(edgeinsets_).md>) — Creates a new value object containing the specified edge insets structure.

### Instance Properties

- [directionalEdgeInsetsValue](nsvalue/directionaledgeinsetsvalue.md)
- [edgeInsetsValue](nsvalue/edgeinsetsvalue.md) — The edge insets structure representation of the value.
- [GCPoint2Value](nsvalue/gcpoint2value.md)
- [CMVideoDimensionsValue](nsvalue/videodimensionsvalue.md)

### Instance Methods

- [- getValue:size:](<nsvalue/getvalue(__size_).md>) — Copies the value into the specified buffer.
- [value(of:)](<nsvalue/value(of_).md>)

## See Also

### Value Wrappers and Transformations

- [NSNumber](nsnumber.md) — An object wrapper for primitive scalar numeric values.
- [ValueTransformer](valuetransformer.md) — An abstract class used to transform values from one representation to another.
