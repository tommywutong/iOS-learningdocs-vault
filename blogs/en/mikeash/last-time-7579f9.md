---
title: Last time
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-07-06-lets-build-nsnumber.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:75715e668c01132a'
translated: false
---

> 原文：[Last time](https://www.mikeash.com/pyblog/friday-qa-2012-07-06-lets-build-nsnumber.html)　·　mikeash.com Friday Q&A

Posted at 2012-07-06 15:08 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-07-27: Let's Build Tagged Pointers](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html)  
Previous article: [Friday Q&A 2012-06-22: Objective-C Literals](https://www.mikeash.com/pyblog/friday-qa-2012-06-22-objective-c-literals.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-07-06: Let's Build NSNumber

by [Mike Ash](https://www.mikeash.com/)

**Overview**  
Like many (but not all) object-oriented languages, Objective-C has a divide between objects and non-objects. Objects respond to messages, can be queried at runtime without knowing their exact type, placed in collections, compared for equality, and share a common set of behavior. Non-objects are largely compile-time constructs, with all of their type information essentially gone at runtime. In Objective-C, these non-objects are everything that comes from C, from the integer `42` to the string `"Hello, world"` to complicated structs.

Boxing is the process of placing these non-objects into an object so that they can be used like other objects, typically so that they can be placed in a collection. `NSNumber` is the Cocoa class used to box C numbers. You can't have an `NSArray` of `int`, but you can have an `NSArray` of `NSNumber`. `NSNumber` shows up a lot in Cocoa programming. Just about any place a Cocoa collection is used to store a number, `NSNumber` is there. Among many other places, `NSNumber` objects are what `NSUserDefaults` stores and retrieves when you ask it to save a number.

**Interface**  
Our surrogate `NSNumber` will be called `MANumber`. Unlike the Cocoa version, which is a subclass of the more general boxing class `NSValue`, this one will directly subclass `NSObject`:

```
    @interface MANumber : NSObject
```

There are a _lot_ of methods for initializing an instance. There's one initializer for each C numeric type, plus some extra ones for types specific to Cocoa:

```
    - (id)initWithChar:(char)value;
    - (id)initWithUnsignedChar:(unsigned char)value;
    - (id)initWithShort:(short)value;
    - (id)initWithUnsignedShort:(unsigned short)value;
    - (id)initWithInt:(int)value;
    - (id)initWithUnsignedInt:(unsigned int)value;
    - (id)initWithLong:(long)value;
    - (id)initWithUnsignedLong:(unsigned long)value;
    - (id)initWithLongLong:(long long)value;
    - (id)initWithUnsignedLongLong:(unsigned long long)value;
    - (id)initWithFloat:(float)value;
    - (id)initWithDouble:(double)value;
    - (id)initWithBool:(BOOL)value;
    - (id)initWithInteger:(NSInteger)value;
    - (id)initWithUnsignedInteger:(NSUInteger)value;
```

There are also getters for these types:

```
    - (char)charValue;
    - (unsigned char)unsignedCharValue;
    - (short)shortValue;
    - (unsigned short)unsignedShortValue;
    - (int)intValue;
    - (unsigned int)unsignedIntValue;
    - (long)longValue;
    - (unsigned long)unsignedLongValue;
    - (long long)longLongValue;
    - (unsigned long long)unsignedLongLongValue;
    - (float)floatValue;
    - (double)doubleValue;
    - (BOOL)boolValue;
    - (NSInteger)integerValue;
    - (NSUInteger)unsignedIntegerValue;
```

Note that any of these getters works no matter which initializer was used. `MANumber` will have to perform the appropriate conversions.

Finally, there are a few other methods for string conversion and comparison:

```
    - (NSString *)stringValue;
    - (NSComparisonResult)compare:(MANumber *)otherNumber;
    - (BOOL)isEqualToNumber:(MANumber *)number;
    - (NSString *)descriptionWithLocale:(id)locale;
```

**Implementation Strategy**  
`MANumber` will use a `union` to store the underlying numeric value. `union` is a rarely-seen feature of standard C. It looks just like a `struct`, but works differently. A `struct` stores many values together in one spot. A `union` does this as well, but you can only access the last one you stored. When you store a value in a `union`, the value of all other fields becomes undefined.

In typical unhelpful-but-efficient C fashion, the compiler doesn't enforce that rule, nor does it help you follow it by, say, letting you query which field was the last one set. You have to keep track of this yourself, typically with an accompanying `enum`.

The `union` could be used to hold every C numeric type, with a big `enum` to say which one is in use. However, this is unnecessarily complex. All we really need is three fields: the largest possible integer type, the largest possible unsigned integer type, and the largest possible floating-point type. From the types we have to handle, these are `long long`, `unsigned long long`, and `double`. Everything else can be converted to and from those without loss.

This implementation does not precisely match that of `NSNumber`, which keeps track of the specific type used to create it. However, using these three types is plenty close enough, and eliminates a lot of extra repetitive code. The fact that `NSNumber` precisely tracks the original type isn't visible most of the time, and only shows up when using a method like `-descriptionWithLocale:` or `-objCType`.

**Storage**  
Here are the instance variables:

```
    @implementation MANumber {
        enum { INT, UINT, DOUBLE } _type;
        union {
            long long i;
            unsigned long long u;
            double d;
        } _value;
    }
```

The `_type` variable holds an anonymous `enum` saying whether the value is an `INT` (`long long`), `UINT` (`unsigned long long`), or `DOUBLE` (guess). The `_value` variable then holds the actual number, using a `union` so that it only ends up storing one.

The code will set `_type` and the corresponding `_value` in the initializers. The getters can then check the `_type` and extract the value accordingly.

**Initializers**  
There's a ton of boilerplate to deal with all of the different types. All of the signed integer types just call through to `initWithLongLong:`, and the unsigned types call through to `initWithUnsignedLongLong:`

```
    - (id)initWithChar:(char)value
    {
        return [self initWithLongLong: value];
    }

    - (id)initWithUnsignedChar:(unsigned char)value
    {
        return [self initWithUnsignedLongLong: value];
    }

    - (id)initWithShort:(short)value
    {
        return [self initWithLongLong: value];
    }

    - (id)initWithUnsignedShort:(unsigned short)value
    {
        return [self initWithUnsignedLongLong: value];
    }

    - (id)initWithInt:(int)value
    {
        return [self initWithLongLong: value];
    }

    - (id)initWithUnsignedInt:(unsigned int)value
    {
        return [self initWithUnsignedLongLong: value];
    }

    - (id)initWithLong:(long)value
    {
        return [self initWithLongLong: value];
    }

    - (id)initWithUnsignedLong:(unsigned long)value
    {
        return [self initWithUnsignedLongLong: value];
    }

    - (id)initWithBool:(BOOL)value
    {
        return [self initWithLongLong: value];
    }

    - (id)initWithInteger:(NSInteger)value
    {
        return [self initWithLongLong: value];
    }

    - (id)initWithUnsignedInteger:(NSUInteger)value
    {
        return [self initWithUnsignedLongLong: value];
    }
```

Those initialisers then simply set the `_type`, `_value`, and return `self`. (Note that I'm leaving out the traditional call to `[super init]` for brevity, as it's not strictly necessary when your superclass is `NSObject`, although still a good idea.)

```
    - (id)initWithLongLong:(long long)value
    {
        _type = INT;
        _value.i = value;
        return self;
    }

    - (id)initWithUnsignedLongLong:(unsigned long long)value
    {
        _type = UINT;
        _value.u = value;
        return self;
    }
```

The floating-point initializers are similar. The one for `float` just calls through to `initWithDouble:`, and that one just sets `_type` and `_value` appropriately:

```
    - (id)initWithFloat:(float)value
    {
        return [self initWithDouble: value];
    }

    - (id)initWithDouble:(double)value
    {
        _type = DOUBLE;
        _value.d = value;
        return self;
    }
```

**Getters**  
The getters are even more similar then the initializers. They all check the `_type`, then return the appropriate field of `_value`. The compiler will handle the final conversion from the active field of `_value` to the requested return type.

Since these methods all contain the same code, this is a perfect candidate for a macro to encapsulate the identical bits. Here's a macro that checks `_type` and then returns the corresponding field of `_value`:

```
    #define RETURN() do { \
            if(_type == INT) \
                return _value.i; \
            else if(_type == UINT) \
                return _value.u; \
            else \
                return _value.d; \
        } while(0)
```

With that macro, the getters pretty much write themselves:

```
    - (char)charValue
    {
        RETURN();
    }

    - (unsigned char)unsignedCharValue
    {
        RETURN();
    }

    - (short)shortValue
    {
        RETURN();
    }

    - (unsigned short)unsignedShortValue
    {
        RETURN();
    }

    - (int)intValue
    {
        RETURN();
    }

    - (unsigned int)unsignedIntValue
    {
        RETURN();
    }

    - (long)longValue
    {
        RETURN();
    }

    - (unsigned long)unsignedLongValue
    {
        RETURN();
    }

    - (long long)longLongValue
    {
        RETURN();
    }

    - (unsigned long long)unsignedLongLongValue
    {
        RETURN();
    }

    - (float)floatValue
    {
        RETURN();
    }

    - (double)doubleValue
    {
        RETURN();
    }

    - (NSInteger)integerValue
    {
        RETURN();
    }

    - (NSUInteger)unsignedIntegerValue
    {
        RETURN();
    }
```

That's a lot of boring and ugly code.

The one exception to this uniform sea of macro invocations is the `-boolValue` method. Since `BOOL` pretends to be a real boolean value, this method should always return `YES` for any non-zero value stored in the `MANumber` object. The compiler's built-in conversion won't do this. For example, the integer `256` will return NO if converted to a `BOOL`, since `BOOL` is just a `signed char`, which is an 8-bit integer. Because of that, `-boolValue` replicates the macro logic, but with an explicit check for zero:

```
    - (BOOL)boolValue
    {
        if(_type == INT)
            return _value.i != 0;
        else if(_type == UINT)
            return _value.u != 0;
        else
            return _value.d != 0;
    }
```

**String Conversion**  
There are two string conversion methods: `-stringValue` and `-descriptionWithLocale:`. `-stringValue` simply calls `-descriptionWithLocale:` with a `nil` parameter:

```
    - (NSString *)stringValue
    {
        return [self descriptionWithLocale: nil];
    }
```

`-descriptionWithLocale:` then uses `-[NSString initWithFormat:locale:]` to build the string. There's no fancy way to deal with the different numeric types here, so it simply checks `_type` and uses a different format string for each case:

```
    - (NSString *)descriptionWithLocale:(id)locale
    {
        if(_type == INT)
            return [[NSString alloc] initWithFormat: @"%lld" locale: locale, _value.i];
        else if(_type == UINT)
            return [[NSString alloc] initWithFormat: @"%llu" locale: locale, _value.u];
        else
            return [[NSString alloc] initWithFormat: @"%f" locale: locale, _value.d];
    }
```

Note that I'm using ARC, which is why there are no `autorelease` calls here.

**Comparison**  
The comparison methods get interesting, because they need to work between `MANumber` objects of different types. For example, the `double` value `-1.1` should compare less than the unsigned integer value `99999`.

There are nine permutations of the types, so nine different cases to handle. This can be reduced to only six cases by enforcing an order. If the two objects have types `INT` and `UINT`, the two cases for that can be reduced to one by only handling the case where `self` is `INT` and the other object is `UINT`, and swapping the two objects if they show up the other way around.

To help with comparison between the different types, I wrote a simple macro that takes two numbers and returns the appropriate `NSComparisonResult`. All it does is take two arguments, save them into temporary variables to avoid multiple evaluation, then return the appropriate constant depending on how they're ordered. There's also a bit of floating-point trickery here. With floating-point numbers, `NAN` (not a number) never compares equal to anything, and all comparisons with it are false. Since `NSComparisonResult` has no way to represent an ordering which means, "this number is not equal to anything, not even itself," I arbitrarily decide to make `NAN` equal to itself and less than any other number, for the purposes of `MANumber` comparison:

```
    #define COMPARE(a, b) do { \
            __typeof__(a) __a_local = a; \
            __typeof__(b) __b_local = b; \
            BOOL __a_isnan = isnan(__a_local); \
            BOOL __b_isnan = isnan(__b_local); \
            if(__a_isnan && __b_isnan) \
                return NSOrderedSame; \
            else if(__a_isnan) \
                return NSOrderedAscending; \
            else if(__b_isnan) \
                return NSOrderedDescending; \
            else if(__a_local > __b_local) \
                return NSOrderedDescending; \
            else if(__a_local < __b_local) \
                return NSOrderedAscending; \
            else \
                return NSOrderedSame; \
        } while(0)
```

The first thing the comparison method itself does is extract the types of the two objects to compare:

```
    - (NSComparisonResult)compare:(MANumber *)otherNumber
    {
        int selfType = _type;
        int otherType = otherNumber->_type;
```

If the two types aren't in order, we reverse the comparison by calling `compare:` again with the arguments reversed, and returning the inverse of the result. Since `NSComparisonResult` is just `-1`, `0`, or `1`, we can invert its meaning by negating it:

```
        if(selfType > otherType)
            return -[otherNumber compare: self];
```

Now we're left with sorted types. There are six cases. If `selfType` is INT, then `otherType` could be anything. If `selfType` is `UINT`, then `otherType` can only be `UINT` or `DOUBLE`. If `selfType` is `DOUBLE`, then `otherType` must be `DOUBLE` as well.

Let's look at the cases where `selfType` is `INT`. If both values are `INT`, the code is easy:

```
        if(selfType == INT)
        {
            if(otherType == INT)
            {
                COMPARE([self longLongValue], [otherNumber longLongValue]);
            }
```

If `otherType` is `UINT`, there's a bit of extra work. Directly comparing with `[otherNumber unsignedLongLongValue]` won't work. C will promote `[self longLongValue]` to unsigned before the comparison, turning negative numbers into positive numbers and wrecking the comparison. `-1` will compare greater than `1` because of this. To prevent that, we make a special check for negative numbers, then compare their unsigned values if both are known to be positive:

```
            else if(otherType == UINT)
            {
                if([self longLongValue] < 0)
                    return NSOrderedAscending;
                else
                    COMPARE([self unsignedLongLongValue], [otherNumber unsignedLongLongValue]);
            }
```

Next comes the case for `DOUBLE`. This gets pretty complicated, because floating-point numbers work fairly differently from integers. There are several different subcases here, which I'll take one by one. However, the first thing it does is extract the `doubleValue` from the other number to make it more convenient to work with:

```
            else
            {
                double other = [otherNumber doubleValue];
```

`double` can hold a much larger range than `long long`. The first subcase is to figure out the largest possible number a `long long` can hold, and see if `other` is beyond it. If it is, it's obviously larger than `self`, since self is a `long long`.

The built-in macro `LLONG_MAX` gives us the largest number a `long long` can hold. However, we can't directly convert this to a `double`. That number is equal to 2^63-1, which can't be represented in a `double`. Due to the internal format of `double`, it can only represent even numbers when it gets beyond 2^54. To perform the comparison accurately, we calculate one number beyond the largest `long long`, careful to use an `unsigned` one when adding, and compare against that:

```
                double longLongMaxPlusOne = LLONG_MAX + 1ULL;
                if(other >= longLongMaxPlusOne)
                    return NSOrderedAscending;
```

We also check in the negative direction. This is a bit easier, as the smallest possible `long long` can be directly represented in a `double`:

```
                if(other < LLONG_MIN)
                    return NSOrderedDescending;
```

If we're still running at this point, then the `double` is within the range of a `long long` and they need to be compared directly. However, we can't just whip out the `>` operator, because there are a lot of `double`s that can't be represented in `long long` (e.g. `1.5`), and there are a lot of `long long`s that can't be represented as a `double` (e.g. any odd number above a threshold, as mentioned above).

Beyond a certain threshold, `double` can only represent integer values, as the magnitude of the value exceeds the precision of the representation. When beyond that threshold, and below the maximum possible `long long`, the `double` can safely be converted to a `long long` with no loss of precision. The two values can then be compared as `long long`s. Below that threshold, `double` can represent any integer, and so the `long long` can safely be converted to a `double` with no loss of precision, and the two values compared as `double`s.

The location of that threshold is actually fairly easy to figure out. C provides a macro, `DBL_MANT_DIG`, which gives the precision of the `double` type. By raising that to a power of two (since `double` is a binary representation), we get the threshold:

```
                double pureIntegerStart = 1LL << DBL_MANT_DIG;
```

Then we simply compare based on where `other` lies relative to that. Note that the threshold applies equally for negative numbers, so we must check it in both directions:

```
                if(other >= pureIntegerStart || other <= -pureIntegerStart)
                    COMPARE([self longLongValue], (long long)other);
                else
                    COMPARE([self doubleValue], other);
            }
        }
```

Next up comes the case where `selfType` is `UINT`. As before, when `otherType` is also `UINT`, the code is easy:

```
        else if(selfType == UINT)
        {
            if(otherType == UINT)
            {
                COMPARE([self unsignedLongLongValue], [otherNumber unsignedLongLongValue]);
            }
```

Note that we don't have to handle `INT`, due to the type sorting performed above. We move on to `DOUBLE`, which is once again complicated. As before, we fetch the value of `otherNumber` into a local variable:

```
            else
            {
                double other = [otherNumber doubleValue];
```

The first thing we do is see if `other` is negative. If it is, then we know the order, as `self` is unsigned (and thus either zero or positive):

```
                if(other < 0)
                    return NSOrderedDescending;
```

Otherwise, we do the same basic threshold calculations as before. This time we have to compare `other` against the largest possible `unsigned long long`. Doing this is a bit tricky. Just like with `long long`, we have to add `1` to get a number that works as a `double`. However, we can't represent anything greater than the largest possible `unsigned long long` as an integer, since `unsigned long long` is the largest integer type we have. Instead, we calculate `(LLONG_MAX + 1) * 2`, which gives one greater than the largest `unsigned long long`, carefully doing so with all the right types to avoid overflow or imprecision:

```
                double unsignedLongLongMaxPlusOne = (double)(LLONG_MAX + 1ULL) * 2.0;
                if(other >= unsignedLongLongMaxPlusOne)
                    return NSOrderedAscending;
```

At this point, we know that both numbers are within each type's range, and so we use the same `pureIntegerStart` strategy as before to compare them directly:

```
                double pureIntegerStart = 1LL << DBL_MANT_DIG;
                if(other >= pureIntegerStart)
                    COMPARE([self unsignedLongLongValue], (unsigned long long)other);
                else
                    COMPARE([self doubleValue], other);
            }
        }
```

All that's left now is the `DOUBLE` case, which is actually really easy. Due to the type sorting, the only possible case here is when they're both `DOUBLE`, so we can just directly compare them:

```
        else
        {
            COMPARE([self doubleValue], [otherNumber doubleValue]);
        }
    }
```

Now that `compare:` implemented, equality checking is trivial:

```
    - (BOOL)isEqualToNumber:(MANumber *)number
    {
        return [self compare: number] == NSOrderedSame;
    }
```

We also want `isEqual:` from `NSObject`. This can simply check the class of the other object, then leverage `isEqualToNumber:`

```
    - (BOOL)isEqual: (id)other
    {
        if(![other isKindOfClass: [MANumber class]])
            return NO;

        return [self isEqualToNumber: other];
    }
```

Finally, since we override `isEqual:`, we must also override `hash`. The implementation of `hash` gets mildly tricky due to the semantics of floating-point numbers. For non-floats, we can simply return the straight integer value as the hash:

```
    - (NSUInteger)hash
    {
        if(_type != DOUBLE)
            return [self unsignedIntegerValue];
```

For floats that are integer values, we want to do the same thing. Since our `isEqual:` considers an integer-valued `DOUBLE` equal to an `INT` or `UINT` of the same value, we _must_ return the same hash as the `INT` and `UINT` equivalent. To accomplish this, we check to see if the `DOUBLE` value is actually an integer, and return the integer value if so:

```
        if(_value.d == floor(_value.d))
            return [self unsignedIntegerValue];
```

Beyond this, we have non-integer values. The ultimate goal is to simply return the bit pattern of the `double`, which will give a nice hash. However, this only works for numbers where bit pattern equality implies `isEqual:`. This is _not_ true for all `double`s. First is `NAN`, which we made compare equal to itself, but which has many different possible bit representations. To handle that, we check for `NAN` explicitly and return a constant hash for it:

```
        if(isnan(_value.d))
            return 0;
```

The other special case is a bit weirder. IEEE 754 floats (the kind used by just about any modern CPU) have two possible values for zero: positive and negative. These are typically indistinguishable, as they compare equal and produce the same results for most calculations. However, they have different bit patterns, so we have to special-case them. I take advantage of the fact that negative zero compares equal to positive zero to make a simple check and return a constant hash for both zeroes:

```
        if(_value.d == 0.0)
            return 0;
```

Having ruled out all the special cases, if the code reaches this point then the number must be one where numerical equality is the same as bit pattern equality. Thus we simply return the bit pattern for the hash. We do this by returning the `u` field of the `union`:

```
        return _value.u;
    }
```

But wait! Previously I said that you're not allowed to access any field in a `union` besides the one that was last set, so this is clearly not allowed. While technically correct according to the language spec, C compilers have generally settled on allowing it and simply reinterpreting the existing value. This code takes the `double` that's stored in the `union` and reinterprets its bits as an `unsigned long long`, which is exactly what we want. Technically this relies on undefined behavior, but it's officially blessed by the compilers we're actually using.

**Conclusion**  
`NSNumber` is a conceptually simple class which mainly exists so that we can stuff numeric values into Cocoa collections, but its flexibility implies a fair amount of underlying complication. By implementing a workalike `MANumber` class, we can see what kinds of things `NSNumber` has to be doing on the inside. Automatic conversion to different integer types requires a fair amount of boilerplate code, and reliable conversion between number of different types can get pretty complicated.

That's it for today. Come back next time for yet another Friday Q&A. As always, Friday Q&A is driven by reader suggestions, so if you have a topic you'd like to see covered, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-07-06-lets-build-nsnumber.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
