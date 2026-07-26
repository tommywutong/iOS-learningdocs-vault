---
title: Exposing NSDictionary – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/exposing-nsdictionary/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c6ef6e44026a9aea'
translated: false
---

> 原文：[Exposing NSDictionary – Bartosz Ciechanowski](https://ciechanow.ski/exposing-nsdictionary/)　·　Bartosz Ciechanowski

# [Exposing NSDictionary](https://ciechanow.ski/exposing-nsdictionary/)

Hash tables are just awesome. To this day I find it fascinating that one can fetch an object corresponding to an arbitrary key in constant time. Although iOS 6.0 introduced an [explicit hash table](http://nshipster.com/nshashtable-and-nsmaptable/), it is `NSDictionary` that’s almost exclusively used for associative storage.

`NSDictionary` doesn’t make any promise of its internal implementation. It would make little sense for a dictionary to store its data in a completely random fashion. However, this assumption doesn’t answer the key question: does `NSDictionary` make use of a hash table? This is what I’ve decided to investigate.

Why not to tackle the full featured `NSMutableDictionary`? A mutable dictionary is, understandably, much more complex and the amount of disassembly I would have had to go through was terrifying. Regular `NSDictionary` still provided a nontrivial ARM64 deciphering challenge. Despite being immutable, the class has some very interesting implementation details which should make the following ride enjoyable.

This blog post has a [companion repo](https://github.com/Ciechan/NSDictionaryExplorer) which contains discussed pieces of code. While the entire investigation has been based on the iOS 7.1 SDK targeting a 64-bit device, neither iOS 7.0 nor 32-bit devices impact the findings.

# The Class[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#the-class)

Plenty of Foundation classes are class clusters and `NSDictionary` is no exception. For quite a long time `NSDictionary` used `CFDictionary` as its default implementation, however, starting with iOS 6.0 things have changed:

```plain
(lldb) po [[NSDictionary new] class]
__NSDictionaryI
```

Similarly to `__NSArrayM`, `__NSDictionaryI` rests within the CoreFoundation framework, in spite of being publicly presented as a part of Foundation. Running the library through class-dump generates the following ivar layout:

```objc
@interface __NSDictionaryI : NSDictionary
{
    NSUInteger _used:58;
    NSUInteger _szidx:6;
}
```

It’s surprisingly short. There doesn’t seem to be any pointer to either keys or objects storage. As we will soon see, `__NSDictionary` literally keeps its storage to itself.

# The Storage[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#the-storage)

## Instance Creation[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#instance-creation)

To understand where `__NSDictionaryI` keeps its contents, let’s take a quick tour through the instance creation process. There is just one class method that’s responsible for spawning new instances of `__NSDictionaryI`. According to class-dump, the method has the following signature:

```objc
+ (id)__new:(const id *)arg1:(const id *)arg2:(unsigned long long)arg3:(_Bool)arg4:(_Bool)arg5;
```

It takes five arguments, of which only the first one is named. If you were to use it in a `@selector` statement it would have a form of `@selector(__new:::::)`. The first three arguments are easily inferred by setting a breakpoint on this method and peeking into the contents of `x2`, `x3` and `x4` registers which contain the array of keys, array of objects, and number of keys (objects) respectively. Notice, that keys and objects arrays are swapped in comparison to the public facing API which takes a form of:

```objc
+ (instancetype)dictionaryWithObjects:(const id [])objects forKeys:(const id <NSCopying> [])keys count:(NSUInteger)cnt;
```

It doesn’t matter whether an argument is defined as `const id *` or `const id []` since [arrays decay into pointers](http://c-faq.com/aryptr/aryptrparam.html) when passed as function arguments.

With three arguments covered we’re left with the two unidentified boolean parameters. I’ve done some assembly digging with the following results: the fourth argument governs whether the keys should be copied, and the last one decides whether the arguments should _not_ be retained. We can now rewrite the method with named parameters:

```objc
+ (id)__new:(const id *)keys :(const id *)objects :(unsigned long long)count :(_Bool)copyKeys :(_Bool)dontRetain;
```

Unfortunately, we don’t have explicit access to this private method, so by using the regular means of allocation the last two arguments are always set to `YES` and `NO` respectively. It is nonetheless interesting that `__NSDictionaryI` is capable of a more sophisticated keys and objects control.

## Indexed ivars[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#indexed-ivars)

Skimming through the disassembly of `+ __new:::::` reveals that both `malloc` and `calloc` are nowhere to be found. Instead, the method calls into `__CFAllocateObject2` passing the `__NSDictionaryI` class as first argument and requested storage size as a second. Stepping down into the sea of ARM64 shows that the first thing `__CFAllocateObject2` does is call into `class_createInstance` with the exact same arguments.

Fortunately, at this point we have access to [the source code](https://opensource.apple.com/source/objc4/objc4-551.1/) of Objective-C runtime which makes further investigation much easier.

The `class_createInstance(Class cls, size_t extraBytes)` function merely calls into `_class_createInstanceFromZone` passing `nil` as a zone, but this is the final step of object allocation. While the function itself has many additional checks for different various circumstances, its gist can be covered with just three lines:

```c
_class_createInstanceFromZone(Class cls, size_t extraBytes, void *zone)
{
    ...
    size_t size = cls->alignedInstanceSize() + extraBytes;
    ...
    id obj = (id)calloc(1, size);
    ...
    return obj;
}
```

The `extraBytes` argument couldn’t have been more descriptive. It’s literally the number of extra bytes that inflate the default instance size. As an added bonus, notice that it’s the `calloc` call that ensures all the ivars are zeroed out when the object gets allocated.

The indexed ivars section is nothing more than an additional space that sits at the end of regular ivars:

![Allocating objects](https://ciechanow.ski/images/dictionaryIndexedIvars@2x.jpg)

Allocating objects

Allocating space on its own doesn’t sound very thrilling so the runtime publishes an accessor:

```objc
void *object_getIndexedIvars(id obj)
```

There is no magic whatsoever in this function, it just returns a pointer to the beginning of indexed ivars section:

![Indexed ivars section](https://ciechanow.ski/images/dictionaryGetIndexedIvars@2x.jpg)

Indexed ivars section

There are few cool things about indexed ivars. First of all, each instance can have _different_ amount of extra bytes dedicated to it. This is exactly the feature `__NSDictionaryI` uses.

Secondly, they provide faster access to the storage. It all comes down to being [cache-friendly](http://stackoverflow.com/a/16699282/558816). Generally speaking, jumping to random memory locations (by dereferencing a pointer) can be expensive. Since the object has just been accessed (somebody has called a method on it), it’s very likely that its indexed ivars have landed in cache. By keeping everything that’s needed very close, the object can provide as good performance as possible.

Finally, indexed ivars can be used as a crude defensive measure to make object’s internals invisible to the utilities like class-dump. This is a very basic protection since a dedicated attacker can simply look for `object_getIndexedIvars` calls in the disassembly or randomly probe the instance past its regular ivars section to see what’s going on.

While powerful, indexed ivars come with two caveats. First of all, `class_createInstance` can’t be used under ARC, so you’ll have to compile some parts of your class with `-fno-objc-arc` flag to make it shine. Secondly, the runtime doesn’t keep the indexed ivar size information anywhere. Even though `dealloc` will clean everything up (as it calls `free` internally), you should keep the storage size somewhere, assuming you use _variable_ number of extra bytes.

# Looking for Key and Fetching Object[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#looking-for-key-and-fetching-object)

## Analyzing Assembly[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#analyzing-assembly)

Although at this point we could poke the `__NSDictionaryI` instances to figure out how they work, the ultimate truth lies within the assembly. Instead of going through the entire wall of ARM64 we will discuss the equivalent Objective-C code instead.

The class itself implements very few methods, but I claim the most important is `objectForKey:` – this is what we’re going to discuss in more detail. Since I made the assembly analysis anyway, you can read it on [a separate page](https://ciechanow.ski/extra/objectforkeyassembly/index.html). It’s dense, but the thorough pass should convince you the following code is more or less correct.

## The C Code[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#the-c-code)

Unfortunately, I don’t have access to the Apple’s code base, so the reverse-engineered code below is not _identical_ to the original implementation. On the other hand, it seems to be working well and I’ve yet to find an edge case that behaves differently in comparison to the genuine method.

The following code is written from the perspective of `__NSDictionaryI` class:

```objc
- (id)objectForKey:(id)aKey
{
    NSUInteger sizeIndex = _szidx;
    NSUInteger size = __NSDictionarySizes[sizeIndex];
    
    id *storage = (id *)object_getIndexedIvars(dict);
    
    NSUInteger fetchIndex = [aKey hash] % size;
    
    for (int i = 0; i < size; i++) {
        id fetchedKey = storage[2 * fetchIndex];

        if (fetchedKey == nil) {
            return nil;
        }
        
        if (fetchedKey == aKey || [fetchedKey isEqual:aKey]) {
            return storage[2 * fetchIndex + 1];
        }

        fetchIndex++;
        
        if (fetchIndex == size) {
            fetchIndex = 0;
        }
    }
    
    return nil;
}
```

When you take a closer look at the C code you might notice something strange about key fetching. It’s always taken from even offsets, while the returned object is at the very next index. This is the dead giveaway of `__NSDictionaryI`’s internal storage – it keeps keys and objects alternately:

![Keys and objects are stored alternately](https://ciechanow.ski/images/dictionaryLayout@2x.jpg)

Keys and objects are stored alternately

**Update:** Joan Lluch [provided](#comment-1345004966) a very convincing explanation for this layout. The original code could use an array of very simple structs:

```objc
struct KeyObjectPair {
    id key;
    id object;
};
```

The `objectForKey:` method is very straightforward and I highly encourage you to walk through it in your head. It’s nonetheless worth pointing out a few things. First of all, the `_szidx` ivar is used as an index into the `__NSDictionarySizes` array, thus it most likely stands for “size index”.

Secondly, the only method called on the passed key is `hash`. The reminder of dividing key’s hash value by dictionary’s size is used to calculate the offset into the index ivars section.

If the key at the offset is `nil`, we simply return `nil`, the job is done:

![When the key slot is empty, nil is returned](https://ciechanow.ski/images/dictionaryMiss@2x.jpg)

When the key slot is empty, nil is returned

However, if the key at the offset is non `nil`, then the two cases may occur. If the keys are equal, then we return the adjacent object. If they’re not equal then the hash collision occurred and we have to keep looking further. `__NSDictionaryI` simply keeps looking until either match or `nil` is found:

![Key found after one collision](https://ciechanow.ski/images/dictionaryHit@2x.jpg)

Key found after one collision

This kind of searching is known as [linear probing](http://en.wikipedia.org/wiki/Linear_probing). Notice how `__NSDictionaryI` wraps the `fetchIndex` around when the storage end is hit. The `for` loop is there to limit the number of checks – if the storage was full and the loop condition was missing we’d keep looking forever.

## __NSDictionarySizes & __NSDictionaryCapacities[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#__nsdictionarysizes--__nsdictionarycapacities)

We already know `__NSDictionarySizes` is some kind of array that stores different possible sizes of `__NSDictionaryI`. We can reason that it’s an array of `NSUInteger`s and indeed, if we ask Hopper to treat the values as 64-bit unsigned integers it suddenly makes a lot of sense:

```s
___NSDictionarySizes:
0x00000000001577a8         dq         0x0000000000000000
0x00000000001577b0         dq         0x0000000000000003
0x00000000001577b8         dq         0x0000000000000007
0x00000000001577c0         dq         0x000000000000000d
0x00000000001577c8         dq         0x0000000000000017
0x00000000001577d0         dq         0x0000000000000029
0x00000000001577d8         dq         0x0000000000000047
0x00000000001577e0         dq         0x000000000000007f
...
```

In a more familiar decimal form it presents as a beautiful list of 64 primes starting with the following sequence: 0, 3, 7, 13, 23, 41, 71, 127. Notice, that those are not consecutive prime numbers which begs the question: what’s the average ratio of the two neighboring numbers? It’s actually around `1.637` – a very close match to the `1.625` which was the growth factor for `NSMutableArray`. For details of why primes are used for the storage size [this Stack Overflow answer](http://stackoverflow.com/a/1147232/558816) is a good start.

We already know how much storage `__NSDictionaryI` can have, but how does it know which size index to pick on initialization? The answer lies within the previously mentioned `+ __new:::::` class method. Converting some parts of the assembly back to C renders the following code:

```objc
int szidx;
for (szidx = 0; szidx < 64; szidx++) {
    if (__NSDictionaryCapacities[szidx] >= count) {
        break;
    }
}

if (szidx == 64) {
    goto fail;
}
```

The method looks linearly through `__NSDictionaryCapacities` array until `count` fits into the size. A quick glance in Hopper shows the contents of the array:

```s
___NSDictionaryCapacities:
0x00000000001579b0         dq         0x0000000000000000
0x00000000001579b8         dq         0x0000000000000003
0x00000000001579c0         dq         0x0000000000000006
0x00000000001579c8         dq         0x000000000000000b
0x00000000001579d0         dq         0x0000000000000013
0x00000000001579d8         dq         0x0000000000000020
0x00000000001579e0         dq         0x0000000000000034
0x00000000001579e8         dq         0x0000000000000055
...
```

Converting to base-10 provides 0, 3, 6, 11, 19, 32, 52, 85 and so on. Notice that those are _smaller_ numbers than the primes listed before. If you were to fit 32 key-value pairs into `__NSDictionaryI` it will allocate space for 41 pairs, conservatively saving quite a few empty slots. This helps reducing the number of hash collisions, keeping the fetching time as close to constant as possible. Apart from trivial case of 3 elements, `__NSDictionaryI` will never have its storage full, on average filling at most 62% of its space.

As a trivia, the last nonempty value of `__NSDictionaryCapacities` is 0x11089481C742 which is 18728548943682 in base-10. You’d have to try really hard to _not_ fit within the pairs count limit, at least on 64-bit architectures.

### Non Exported Symbols[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#non-exported-symbols)

If you were to use `__NSDictionarySizes` in your code by declaring it as an `extern` array, you’d quickly realize it’s not that easy. The code wouldn’t compile due to a linker error – the `__NSDictionarySizes` symbol is undefined. Inspecting the CoreFoundation library with nm utility:

```bash
nm CoreFoundation | grep ___NSDictionarySizes
```

…clearly shows the symbols are there (for ARMv7, ARMv7s and ARM64 respectively):

```bash
00139c80 s ___NSDictionarySizes
0013ac80 s ___NSDictionarySizes
0000000000156f38 s ___NSDictionarySizes
```

Unfortunately the nm manual clearly states:

> If the symbol is local (non-external), the symbol’s type is instead represented by the corresponding lowercase letter.

The symbols for `__NSDictionarySizes` are simply not exported – they’re intended for internal use of the library. I’ve done some research to figure out if it’s possible to link with non-exported symbols, but apparently it is not (_please_ tell me if it is!). We can’t access them. That is to say, we can’t access them easily.

### Sneaking in[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#sneaking-in)

Here’s an interesting observation: in both iOS 7.0 an 7.1 the `kCFAbsoluteTimeIntervalSince1904` constant is laid out directly _before_ `__NSDictionarySizes`:

```s
_kCFAbsoluteTimeIntervalSince1904:
0x00000000001577a0         dq         0x41e6ceaf20000000
___NSDictionarySizes:
0x00000000001577a8         dq         0x0000000000000000
```

The best thing about `kCFAbsoluteTimeIntervalSince1904` is that it _is_ exported! We’re going to add 8 bytes (size of `double`) to the address of this constant and reinterpret the result as pointer to `NSUInteger`:

```objc
NSUInteger *Explored__NSDictionarySizes = (NSUInteger *)((char *)&kCFAbsoluteTimeIntervalSince1904 + 8);
```

Then we can access its values by convenient indexing:

```objc
(lldb) p Explored__NSDictionarySizes[0]
(NSUInteger) $0 = 0
(lldb) p Explored__NSDictionarySizes[1]
(NSUInteger) $1 = 3
(lldb) p Explored__NSDictionarySizes[2]
(NSUInteger) $2 = 7
```

This hack is very fragile and will most likely break in the future, but this is a test project so it’s perfectly fine.

# __NSDictionaryI Characteristics[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#__nsdictionaryi-characteristics)

Now that we’ve discovered the internal structure of `__NSDictionaryI` we can use this information to figure out why things work they way they work and what unforeseen consequences the present implementation of `__NSDictionaryI` introduces.

## Printout Code[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#printout-code)

To make our investigation a little bit easier we will create a helper `NSDictionary` category method that will print the contents of the instance

```objc
- (NSString *)explored_description
{
    assert([NSStringFromClass([self class]) isEqualToString:@"__NSDictionaryI"]);
    
    BCExploredDictionary *dict = (BCExploredDictionary *)self;

    NSUInteger count = dict->_used;
    NSUInteger sizeIndex = dict->_szidx;
    NSUInteger size = Explored__NSDictionarySizes[sizeIndex];
    
    __unsafe_unretained id *storage = (__unsafe_unretained id *)object_getIndexedIvars(dict);
    
    NSMutableString *description = [NSMutableString stringWithString:@"\n"];
    
    [description appendFormat:@"Count: %lu\n", (unsigned long)count];
    [description appendFormat:@"Size index: %lu\n", (unsigned long)sizeIndex];
    [description appendFormat:@"Size: %lu\n", (unsigned long)size];

    for (int i = 0; i < size; i++) {
        [description appendFormat:@"[%d] %@ - %@\n", i, [storage[2*i] description], [storage[2*i + 1] description]];
    }
    
    return description;
}
```

## Order of keys/objects on enumeration is the same as order of keys/objects in storage[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#order-of-keysobjects-on-enumeration-is-the-same-as-order-of-keysobjects-in-storage)

Let’s create a simple dictionary containing four values:

```objc
NSDictionary *dict = @{@1 : @"Value 1",
                       @2 : @"Value 2",
                       @3 : @"Value 3",
                       @4 : @"Value 4"};

NSLog(@"%@", [dict explored_description]);
```

The output of the explored description is:

```plain
Count: 4
Size index: 2
Size: 7
[0] (null) - (null)
[1] 3 - Value 3
[2] (null) - (null)
[3] 2 - Value 2
[4] (null) - (null)
[5] 1 - Value 1
[6] 4 - Value 4
```

With that in mind let’s do a quick enumeration over dictionary:

```objc
[dict enumerateKeysAndObjectsUsingBlock:^(id key, id obj, BOOL *stop) {
    NSLog(@"%@ - %@", key, obj);
}];
```

And the output:

```plain
3 - Value 3
2 - Value 2
1 - Value 1
4 - Value 4
```

Enumeration seems to simply walk through the storage, ignoring the `nil` keys and calling the block only for non-empty slots. This is also the case for fast enumeration, `keyEnumerator`, `allKeys` and `allValues` methods. It makes perfect sense. The `NSDictionary` is not ordered, so it doesn’t really matter what sequence the keys and values are provided in. Using the internal layout is the easiest and probably the fastest option.

## If you mess up, __NSDictionaryI may return something for nil key![![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#if-you-mess-up-__nsdictionaryi-may-return-something-for-nil-key)

Let’s consider an example. Imagine we’re building a simple 3D strategy game set in space. The entire universe is split into cube-like sectors that imaginary factions can fight over. A sector can be referenced by its `i`, `j`, and `k` indexes. We shouldn’t use a 3D array to store the sectors info – the game space is huge and most of it is empty, so we would waste memory storing `nil` pointers. Instead, we’re going to use a sparse storage in a form of `NSDictionary` with a custom key class that will make it super easy to query if there is something at a given location.

Here’s the interface for key, a `BC3DIndex` class:

```objc
@interface BC3DIndex : NSObject <NSCopying>

@property (nonatomic, readonly) NSUInteger i, j, k; // you actually can do that

- (instancetype)initWithI:(NSUInteger)i j:(NSUInteger)j k:(NSUInteger)k;

@end
```

And its equally trivial implementation:

```objc
@implementation BC3DIndex

- (instancetype)initWithI:(NSUInteger)i j:(NSUInteger)j k:(NSUInteger)k
{
    self = [super init];
    if (self) {
        _i = i;
        _j = j;
        _k = k;
    }
    return self;
}

- (BOOL)isEqual:(BC3DIndex *)other
{
    return other.i == _i && other.j == _j && other.k == _k;
}

- (NSUInteger)hash
{
    return _i ^ _j ^ _k;
}

- (id)copyWithZone:(NSZone *)zone
{
    return self; // we're immutable so it's OK
}

@end
```

Notice how we’re being a good subclassing citizen: we implemented both `isEqual:` and `hash` methods and made sure that if two 3D-indexes are equal then their hash values are equal as well. The object equality requirements _are_ fulfilled.

Here’s a trivia: what will the following code print?

```objc
NSDictionary *indexes = @{[[BC3DIndex alloc] initWithI:2 j:8 k:5] : @"A black hole!",
                          [[BC3DIndex alloc] initWithI:0 j:0 k:0] : @"Asteroids!",
                          [[BC3DIndex alloc] initWithI:4 j:3 k:4] : @"A planet!"};

NSLog(@"%@", [indexes objectForKey:nil]);
```

It should be `(null)` right? Nope:

```plain
Asteroids!
```

To investigate this further let’s grab a dictionary’s description:

```c
Count: 3
Size index: 1
Size: 3
[0] <BC3DIndex: 0x17803d340> - A black hole!
[1] <BC3DIndex: 0x17803d360> - Asteroids!
[2] <BC3DIndex: 0x17803d380> - A planet!
```

It turns out `__NSDictionaryI` doesn’t check if the `key` passed into `objectForKey:` is `nil` (and I argue this is a _good_ design decision). Calling `hash` method on `nil` returns `0`, which causes the class to compare key at index `0` with `nil`. This is important: it is the _stored_ key that executes the `isEqual:` method, not the passed in key.

The first comparison fails, since `i` index for “A black hole!” is `2` whereas for `nil` it’s zero. The keys are not equal which causes the dictionary to keep looking, hitting another stored key: the one for “Asteroids!”. This key has all three `i`, `j`, and `k` properties equal to `0` which is also what `nil` will return when asked for its properties (by the means of `nil` check inside `objc_msgSend`).

This is the crux of the problem. The `isEqual:` implementation of `BC3DIndex` may, under some conditions, return `YES` for `nil` comparison. As you can see, this is a very dangerous behavior that can mess things up easily. _Always_ ensure that your object is not equal to `nil`.

## A Helper Key Class[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#a-helper-key-class)

For the next two tests we’re going to craft a special key class that will have a configurable hash value and will print stuff to the console when executing `hash` and `isEqual:` method.

Here’s the interface:

```objc
@interface BCNastyKey : NSObject <NSCopying>

@property (nonatomic, readonly) NSUInteger hashValue;

+ (instancetype)keyWithHashValue:(NSUInteger)hashValue;

@end
```

And the implementation:

```objc
@implementation BCNastyKey

+ (instancetype)keyWithHashValue:(NSUInteger)hashValue
{
    return [[BCNastyKey alloc] initWithHashValue:hashValue];
}

- (instancetype)initWithHashValue:(NSUInteger)hashValue
{
    self = [super init];
    if (self) {
        _hashValue = hashValue;
    }
    return self;
}

- (id)copyWithZone:(NSZone *)zone
{
    return self;
}

- (NSUInteger)hash
{
    NSLog(@"Key %@ is asked for its hash", [self description]);

    return _hashValue;
}

- (BOOL)isEqual:(BCNastyKey *)object
{
    NSLog(@"Key %@ equality test with %@: %@", [self description], [object description], object == self ? @"YES" : @"NO");

    return object == self;
}

- (NSString *)description
{
    return [NSString stringWithFormat:@"(&:%p #:%lu)", self, (unsigned long)_hashValue];
}

@end
```

This key is awful: we’re only equal to self, but we’re returning an arbitrary hash. Notice that this _doesn’t_ break the equality contract.

## `isEqual` doesn’t have to be called to match the key[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#isequal-doesnt-have-to-be-called-to-match-the-key)

Let’s create a key and a dictionary:

```objc
BCNastyKey *key = [BCNastyKey keyWithHashValue:3];
NSDictionary *dict = @{key : @"Hello there!"};
```

The following call:

```c
[dict objectForKey:key];
```

Prints this to the console:

```plain
Key (&:0x17800e240 #:3) is asked for its hash
```

As you can see, the `isEqual:` method has not been called. This is very cool! Since the vast majority of keys out there are `NSString` literals, they share _the same_ address in the entire application. Even if the key is a very long literal string, the `__NSDictionaryI` won’t run the potentially time consuming `isEqual:` method unless it absolutely has to. And since 64-bit architectures introduced tagged pointers, some instances of `NSNumber`, `NSDate` and, [apparently](https://twitter.com/Catfish_Man/status/393238389266194434), `NSIndexPath` benefit from this optimization as well.

## Worst case performance is linear[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#worst-case-performance-is-linear)

Let’s create a very simple test case:

```objc
BCNastyKey *targetKey = [BCNastyKey keyWithHashValue:36];

NSDictionary *b = @{[BCNastyKey keyWithHashValue:1] : @1,
                    [BCNastyKey keyWithHashValue:8] : @2,
                    [BCNastyKey keyWithHashValue:15] : @3,
                    [BCNastyKey keyWithHashValue:22] : @4,
                    [BCNastyKey keyWithHashValue:29] : @5,
                    targetKey : @6
                    };
```

A single killer line:

```objc
NSLog(@"Result: %@", [[b objectForKey:targetKey] description]);
```

Reveals the disaster:

```plain
Key (&:0x170017640 #:36) is asked for its hash
Key (&:0x170017670 #:1) equality test with (&:0x170017640 #:36): NO
Key (&:0x170017660 #:8) equality test with (&:0x170017640 #:36): NO
Key (&:0x170017680 #:15) equality test with (&:0x170017640 #:36): NO
Key (&:0x1700176e0 #:22) equality test with (&:0x170017640 #:36): NO
Key (&:0x170017760 #:29) equality test with (&:0x170017640 #:36): NO
Result: 6
```

This is extremely pathological case – every single key in the dictionary has ben equality tested. Even though each hash was different, it still collided with every other key, because the keys' hashes were [congruent modulo](http://en.wikipedia.org/wiki/Modular_arithmetic#Congruence_relation) 7, which turned out to be the storage size of the dictionary.

As mentioned before, notice that the last `isEqual:` test is missing. The `__NSDictionaryI` simply compared the pointers and figured out it must be the same key.

Should you care for this linear time fetching? Absolutely not. I’m not that into probabilistic analysis of hash distribution, but you’d have to be _extremely_ unlucky for all your hashes to be modulo congruent to dictionary’s size. Some collisions here and there will always happen, that is the nature of hash tables, but you will probably never run into the linear time issue yourself. That is, unless you mess up your `hash` function.

# Final Words[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#final-words)

I’m fascinated how simple the `__NSDictionaryI` turned out to be. Needless to say, the class certainly serves its purpose and there’s no need to make things excessively complex. For me, the most beautiful aspect of the implementation is the key-object-key-object layout. This is a brilliant idea.

If you were to take one tip from this article then I’d go with watching out for your `hash` and `isEqual:` methods. Granted, one rarely writes custom key classes to be used in a dictionary, but those rules apply to `NSSet` as well.

I’m aware that at some point in time `NSDictionary` will change and my findings will become obsolete. Internalizing the current implementation details may become a burden in the future when the memorized assumptions will no longer apply. However, right here and right now it’s just so much fun to see how things work and hopefully you share my excitement.
