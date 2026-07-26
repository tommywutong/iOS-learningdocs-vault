---
title: 'Key Value Information | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/07/key-value-information.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:899ffe3f83498fb8'
translated: false
---

> 原文：[Key Value Information | Cocoa with Love](https://www.cocoawithlove.com/2008/07/key-value-information.html)　·　Cocoa with Love (Matt Gallagher)

NSKeyValueCoding is used throughout Cocoa (Bindings, Core Data, Collections and more) but despite being a dynamic way of connecting to an object, it doesn't provide dynamic information about its own operation — which keys an object supports or the custom methods used to get and set values. This post will look at how NSKeyValueCoding works and show you how to get supported keys and their methods for any class or object.

## Previously on "Fundamentals of Cocoa Programming"...

Key Value Coding is a way of getting and setting data on an object. Key Value Coding means that you use a generic method on the object to ask it to get or set a value for a specific name (the "key"). By using a generic method on the object, Key Value Coding abstracts away the mechanics of how the value for the "key" is obtained or set on the object.

Key Value Coding is about connection logic; it does not normally perform the work of retrieving or changing values (normal getter and setter methods to do this). Instead, it defines how to invoke the getter and setter methods in an abstract way.

It is particularly useful in at least 5 situations situations:

- It reduces the appearance of an object to that of simple data storage — whether or not it is actually simple under the hood (e.g. NSManagedObject).
- It provides a simple interface for flexibly dealing with variable numbers of named values (e.g. NSDictionary).
- It removes the need to know the specific object type that you're dealing with — such as the generic connecting of objects in user-interface bindings.
- Allows easy chaining of access operations through "key paths" and provides operators for dealing with collections of data accessed in this way.
- Generic access to data makes possible other services such as NSKeyValueObserving.

It does (most) of this through two basic methods:

```objc
- (id)valueForKey:(NSString *)key
- (void)setValue:(id)value forKey:(NSString *)key
```

which are defined in the [NSKeyValueCoding](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Protocols/NSKeyValueCoding_Protocol/Reference/Reference.html) informal protocol (implicitly implemented by all NSObjects).

## How does it work?

Once you start asking how anything works, you immediately plunge into a gray area. [The documentation](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Protocols/NSKeyValueCoding_Protocol/Reference/Reference.html) at least tells us this:

- The default implementation will invoke the -(id)\<key\> or -(void)set\<key\>: methods, if they exist, to perform the work. There are a few other method names tried if these can't be found.
- If no method is found, any instance variable with the same name as the key will be automatically accessed (unless this feature is explicitly disabled for the class).
- If no matching instance variable is found either, the -(id)valueForUndefinedKey:(NSString *)key method is invoked which raises an NSUndefinedKeyException by default.

Distilling this information down, you can (in most cases) presume that key value coding will work for any "key" on any class that supports the methods -(id)\<key\> and -(void)set\<key\>:, or has an attribute named "key". Sometimes overrides valueForUndefinedKey: will support other keys too but that is highly implementation specific. Most other key and object combinations will throw an NSUndefinedKeyException.

## Definitive answers

Key Value Coding is all about dynamic connections, simplifying and abstracting — so it seems reasonable that you may eventually find a situation where you want to get a value from an object but you need to check at runtime if it supports the key for the value you want.

Unfortunately, the many fallback options for key lookup and the possibility of overrideable methods like valueForUndefinedKey: mean that there is no specific property you can read that will reveal if a key is supported.

In the most general sense, there is only one way of determining if an object supports a given key:

```objc
BOOL supportsSomeKey = YES;
@try
{
    [object valueForKey:somekey];
}
@catch (NSException *e)
{
    if ([[e name] isEqualTo:NSUndefinedKeyException])
    {
        supportsSomeKey = NO;
    }
}
```

If it throws an NSUndefinedKeyException, then it's not happy with the key.

## More detailed but less definitive answers

If you consider deliberately triggering exceptions to be a crime against programming or you wanted different information about how the value is accessed for a given key, then a different approach may be required.

Depending on your circumstances, you may simply want to perform the lookups that NSKeyValueCoding itself likely performs — i.e. build the different accessor method names from the "key" name, convert this to a SEL and ask the class or object if it handles the selector.

This is exactly the approach I took in a piece of code I was playing with recently. My code used Core Data's NSManagedObject and wanted to inspect generic NSManagedObjects to see if I had written custom accessor methods (as distinct from the automatically generated accessor methods) for specific keys. I was able to use the following method:

```objc
+ (SEL)getterSelectorForKey:(NSString *)key
{
    NSString *capitalizedKey =
        [[[key substringToIndex:1] uppercaseString]
            stringByAppendingString:[key substringFromIndex:1]];

    NSString *getString = [@"get" stringByAppendingString:capitalizedKey];
    SEL getSelector = NSSelectorFromString(getString);
    if ([self instancesRespondToSelector:getSelector])
    {
        return getSelector;
    }
    
    SEL plainSelector = NSSelectorFromString(key);
    if ([self instancesRespondToSelector:plainSelector])
    {
        return plainSelector;
    }
    
    NSString *isString = [@"is" stringByAppendingString:capitalizedKey];
    SEL isSelector = NSSelectorFromString(isString);
    if ([self instancesRespondToSelector:isSelector])
    {
        return isSelector;
    }
    
    return nil;
}
```

in an NSManagedObject category to lookup any custom written accessor for a specified key — this method simply follows the lookup path described in the documentation to find an accessor method if it exists.

The above method is able to differentiate between a custom accessor and Core Data's automatically generated accessors because it is invoked on the class. Core Data's automatically generated accessors only exist on object instances (the class doesn't have them in its list of instance methods), so the above method will only return the custom compiled methods for which I was searching.

You could use a similar approach to get the other types of method used in key value coding, i.e.:

```objc
+ (SEL)setterSelectorForKey:(NSString *)key;
+ (SEL)addObjectSelectorForKey:(NSString *)key;
+ (SEL)removeObjectSelectorForKey:(NSString *)key;
+ (SEL)countOfSelectorForKey:(NSString *)key;
+ (SEL)objectInAtIndexForKey:(NSString *)key;
```

Similarly, if you were interested in key value coding that may access instance variables directly, you could use class_getClassVariable to get any instance variables with the same name as the key.
