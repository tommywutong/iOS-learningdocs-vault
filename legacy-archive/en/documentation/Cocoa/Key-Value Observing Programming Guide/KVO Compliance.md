---
title: Key-Value Observing Programming Guide
apple_id: 10000177i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/Articles/KVOCompliance.html
archived_at: '2026-07-15T07:16:18.106547Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Key-Value Observing Programming Guide](Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md)


[Next](Registering%20Dependent%20Keys.md)[Previous](Registering%20for%20Key-Value%20Observing.md)

# KVO Compliance

In order to be considered KVO-compliant for a specific property, a class must ensure the following:

- The class must be [key-value coding compliant](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25) for the property, as specified in [Ensuring KVC Compliance](../Key-Value%20Coding%20Programming%20Guide/Compliant.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3te).

  KVO supports the same data types as KVC, including Objective-C objects and the scalars and structures listed in Scalar and Structure Support.
- The class emits KVO change [notifications](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35) for the property.
- Dependent keys are registered appropriately (see [Registering Dependent Keys](Registering%20Dependent%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tslkciffekqkjivcq)).

There are two techniques for ensuring the change notifications are emitted. Automatic support is provided by `NSObject` and is by default available for all properties of a class that are [key-value coding compliant](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25). Typically, if you follow standard Cocoa coding and naming conventions, you can use automatic change notifications—you don’t have to write any additional code.

Manual change notification provides additional control over when notifications are emitted, and requires additional coding. You can control automatic notifications for properties of your subclass by implementing the class method [automaticallyNotifiesObserversForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1409370-automaticallynotifiesobservers).

`NSObject` provides a basic implementation of automatic key-value change notification. Automatic key-value change notification informs observers of changes made using key-value compliant [accessors](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2), as well as the key-value coding methods. Automatic notification is also supported by the [collection](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10) proxy objects returned by, for example, `mutableArrayValueForKey:`.

The examples shown in Listing 1 result in any observers of the property `name` to be notified of the change.

__Listing 1__  Examples of method calls that cause KVO change notifications to be emitted

```
// Call the accessor method.
[account setName:@"Savings"];

// Use setValue:forKey:.
[account setValue:@"Savings" forKey:@"name"];

// Use a key path, where 'account' is a kvc-compliant property of 'document'.
[document setValue:@"Savings" forKeyPath:@"account.name"];

// Use mutableArrayValueForKey: to retrieve a relationship proxy object.
Transaction *newTransaction = <#Create a new transaction for the account#>;
NSMutableArray *transactions = [account mutableArrayValueForKey:@"transactions"];
[transactions addObject:newTransaction];
```


In some cases, you may want control of the notification process, for example, to minimize triggering notifications that are unnecessary for application specific reasons, or to group a number of changes into a single notification. Manual change notification provides means to do this.

Manual and automatic notifications are not mutually exclusive. You are free to issue manual notifications in addition to the automatic ones already in place. More typically, you may want to completely take control of the notifications for a particular property. In this case, you [override](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57) the `NSObject` implementation of `automaticallyNotifiesObserversForKey:`. For properties whose automatic notifications you want to preclude, the subclass implementation of `automaticallyNotifiesObserversForKey:` should return `NO`. A subclass implementation should invoke super for any unrecognized keys. The example in Listing 2 enables manual notification for the `balance` property, allowing the superclass to determine the notification for all other keys.

__Listing 2__  Example implementation of automaticallyNotifiesObserversForKey:

```objc
+ (BOOL)automaticallyNotifiesObserversForKey:(NSString *)theKey {

    BOOL automatic = NO;
    if ([theKey isEqualToString:@"balance"]) {
        automatic = NO;
    }
    else {
        automatic = [super automaticallyNotifiesObserversForKey:theKey];
    }
    return automatic;
}
```

To implement manual observer notification, you invoke [willChangeValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416222-willchangevalueforkey) before changing the value, and [didChangeValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1411809-didchangevalue) after changing the value. The example in Listing 3 implements manual notifications for the `balance` property.

__Listing 3__  Example accessor method implementing manual notification

```objc
- (void)setBalance:(double)theBalance {
    [self willChangeValueForKey:@"balance"];
    _balance = theBalance;
    [self didChangeValueForKey:@"balance"];
}
```

You can minimize sending unnecessary notifications by first checking if the value has changed. The example in Listing 4 tests the value of `balance` and only provides the notification if it has changed.

__Listing 4__  Testing the value for change before providing notification

```objc
- (void)setBalance:(double)theBalance {
    if (theBalance != _balance) {
        [self willChangeValueForKey:@"balance"];
        _balance = theBalance;
        [self didChangeValueForKey:@"balance"];
    }
}
```

If a single operation causes multiple keys to change you must nest the change notifications as shown in Listing 5.

__Listing 5__  Nesting change notifications for multiple keys

```objc
- (void)setBalance:(double)theBalance {
    [self willChangeValueForKey:@"balance"];
    [self willChangeValueForKey:@"itemChanged"];
    _balance = theBalance;
    _itemChanged = _itemChanged+1;
    [self didChangeValueForKey:@"itemChanged"];
    [self didChangeValueForKey:@"balance"];
}
```

In the case of an ordered to-many relationship, you must specify not only the key that changed, but also the type of change and the indexes of the objects involved. The type of change is an [NSKeyValueChange](https://developer.apple.com/documentation/foundation/nskeyvaluechange) that specifies `NSKeyValueChangeInsertion`, `NSKeyValueChangeRemoval`, or `NSKeyValueChangeReplacement`. The indexes of the affected objects are passed as an [NSIndexSet](https://developer.apple.com/documentation/foundation/nsindexset) object.

The code fragment in Listing 6 demonstrates how to wrap a deletion of objects in the to-many relationship `transactions`.

__Listing 6__  Implementation of manual observer notification in a to-many relationship

```objc
- (void)removeTransactionsAtIndexes:(NSIndexSet *)indexes {
    [self willChange:NSKeyValueChangeRemoval
        valuesAtIndexes:indexes forKey:@"transactions"];

    // Remove the transaction objects at the specified indexes.

    [self didChange:NSKeyValueChangeRemoval
        valuesAtIndexes:indexes forKey:@"transactions"];
}
```

[Next](Registering%20Dependent%20Keys.md)[Previous](Registering%20for%20Key-Value%20Observing.md)

