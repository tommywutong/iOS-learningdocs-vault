---
title: ValueTransformer
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/valuetransformer
source_url: 'https://developer.apple.com/documentation/foundation/valuetransformer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/valuetransformer.json'
content_hash: 'sha256:2640b37779858d5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ValueTransformer

<sub>Class</sub>

An abstract class used to transform values from one representation to another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class ValueTransformer
```

## Overview

You create a value transformer by subclassing [ValueTransformer](valuetransformer.md) and overriding the necessary methods to provide the required custom transformation. You then register the value transformer using the [+ setValueTransformer:forName:](<valuetransformer/setvaluetransformer(__forname_).md>) method, so that other parts of your app can access it by name with [+ valueTransformerForName:](<valuetransformer/init(forname_).md>).

Use the [- transformedValue:](<valuetransformer/transformedvalue(__).md>) method to transform a value from one representation into another. If a value transformer designates that its transformation is reversible by returning [true](../swift/true.md) for [+ allowsReverseTransformation](<valuetransformer/allowsreversetransformation().md>), you can also use the [- reverseTransformedValue:](<valuetransformer/reversetransformedvalue(__).md>) to perform the transformation in reverse. For example, reversing the characters in a string is a reversible operation, whereas changing the characters in a string to be uppercase is a nonreversible operation.

A value transformer can take inputs of one type and return a value of a different type. For example,  a value transformer could take an [NSImage](../appkit/nsimage.md) or [UIImage](../uikit/uiimage.md) object and return an [NSData](nsdata.md) object containing the PNG representation of that image.

### Example Usage

The following example defines a new value transformer that takes an object and returns a string based on the object’s class type. This transformer isn’t reversible because it doesn’t make sense to transform a class name into an object.

**Swift**

```swift
class ClassNameTransformer: ValueTransformer {
    override class func transformedValueClass() -> AnyClass {
        return NSString.self
    }
    
    override class func allowsReverseTransformation() -> Bool {
        return false
    }
    
    override func transformedValue(_ value: Any?) -> Any? {
        return (value as AnyObject).className
    }
}

extension NSValueTransformerName {
    static let classNameTransformerName = NSValueTransformerName(rawValue: "ClassNameTransformer")
}

ValueTransformer.setValueTransformer(ClassNameTransformer(), forName: .classNameTransformerName)
```

**Objective-C**

```objc
@interface ClassNameTransformer: NSValueTransformer {}
@end
@implementation ClassNameTransformer
+ (Class)transformedValueClass { 
    return [NSString class]; 
}
+ (BOOL)allowsReverseTransformation { 
    return NO; 
}
- (id)transformedValue:(id)value {
    return (value == nil) ? nil : NSStringFromClass([value class]);
}
@end
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Using the Name-Based Registry

- [+ setValueTransformer:forName:](<valuetransformer/setvaluetransformer(__forname_).md>) — Registers the provided value transformer with a given identifier.
- [+ valueTransformerForName:](<valuetransformer/init(forname_).md>) — Returns the value transformer identified by a given identifier.
- [+ valueTransformerNames](<valuetransformer/valuetransformernames().md>) — Returns an array of all the registered value transformers.
- [NSValueTransformerName](nsvaluetransformername.md) — Named value transformers defined by `NSValueTransformer`.

### Getting Information About a Transformer

- [+ allowsReverseTransformation](<valuetransformer/allowsreversetransformation().md>) — Returns a Boolean value that indicates whether the receiver can reverse a transformation.
- [+ transformedValueClass](<valuetransformer/transformedvalueclass().md>) — Returns the class of the value returned by the receiver for a forward transformation.

### Transforming Values

- [- transformedValue:](<valuetransformer/transformedvalue(__).md>) — Returns the result of transforming a given value.
- [- reverseTransformedValue:](<valuetransformer/reversetransformedvalue(__).md>) — Returns the result of the reverse transformation of a given value.

## See Also

### Value Wrappers and Transformations

- [NSNumber](nsnumber.md) — An object wrapper for primitive scalar numeric values.
- [NSValue](nsvalue.md) — A simple container for a single C or Objective-C data item.
