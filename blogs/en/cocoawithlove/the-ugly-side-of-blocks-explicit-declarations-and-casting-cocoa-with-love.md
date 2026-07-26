---
title: 'The ugly side of blocks: explicit declarations and casting. | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/10/ugly-side-of-blocks-explicit.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:137965566ec3a7b4'
translated: false
---

> 原文：[The ugly side of blocks: explicit declarations and casting. | Cocoa with Love](https://www.cocoawithlove.com/2009/10/ugly-side-of-blocks-explicit.html)　·　Cocoa with Love (Matt Gallagher)

Blocks are a welcome addition to C/Objective-C/C++/Objective-C++ with Snow Leopard but they carry with them the worst aspect of Standard C: function pointer declaration and casting syntax. In this post, I'll show you how to understand declarations and casting syntax for blocks and function pointers, even in the worst of scenarios.

## Simple block declarations and casting

Used as intended (simple inline code implementations) blocks are fairly elegant. This is due to one advantage they offer: in simple cases, you do not need to specify the return type — it can be inferred from the return statement in the block itself.

So declaring a block that returns an `int` can be as simple as:

```objc
int (^alwaysReturnIntZero)() = ^{ return 0; };
```

In this case though, an unqualified integral value is correctly assumed to be an `int`. If we want the block to return an `NSInteger`, we need to either cast the return type or not rely on type inference and declare the return fully:

```objc
NSInteger (^alwaysReturnNSIntegerZero)() = ^ NSInteger (){ return 0; };
```

Notice that the _block literal_ (righthand side) does not follow the structure as the _block declaration_ (lefthand side). The block literal uses a straightforward "caret, return type, parameter list" order but the block declaration uses the C function pointer declaration syntax, which can grow more complex (as I'll show later). At this point though, the two are of similar complexity.

Casting a block looks much like declaring a block, minus the name of the variable from the declaration.

```objc
long long (^alwaysReturnLongLongZero)() = (long long (^)())alwaysReturnNSIntegerZero;
```

If you look at what is done here, all that is needed to create a cast for a value to the variable type, is to copy the variable's declaration, put parentheses around the copied declaration and remove the variable name.

### Function pointers

Blocks borrow their syntax from standard C function pointers. In almost all cases, the only difference between a block declaration or cast and a function pointer declaration or cast is the "`^`" character is used for the block and the "`*`" character is used for the function pointer. e.g.:

```objc
long long (*fnAlwaysReturnLongLongZero)() = (long long (*)())fnAlwaysReturnNSIntegerZero;
```

Of course, functions cannot be declared inline, so you cannot have function literals in the same way as you can have block literals. However, all other syntactic traits remain the same.

## Reading declarations correctly

Unfortunately, blocks follow the typical C declaration rules which become outright confusing when you try to return something. Before it all gets complicated, I'm going to explain something simple about C declarations.

Consider how a pointer is declared:

```objc
int *myVariable;
```

If you're reading this blog at all, you should know that this statement creates a pointer named `myVariable` which points to an `int`.

But the operator used here is a "dereference", it is not the "make a pointer" (address of) operator. The correct way to read this line is:

1. Declare a variable:  
  `myVariable`
2. It can be dereferenced (and by _implication_ is therefore a pointer)  
  `*myVariable`
3. If it is deferenced, then the value yielded from the dereference should be treated as an `int`:  
  `int *myVariable;`.

Let's look at the `alwaysReturnIntZero` declaration from above again and we'll apply this same reading to it.

```objc
int (^alwaysReturnIntZero)() = ^{ return 0; };
```

1. Declare a variable:  
  `alwaysReturnIntZero`
2. It can be dereferenced to yield block information (and by _implication_ is therefore a block pointer):  
  `^alwaysReturnIntZero`
3. Its block implementation takes no parameters and returns an `int`:  
  `int (^alwaysReturnIntZero)()`

This approach to reading a declaration is quite simple but you'll need to it to follow the next section.

## Declaring a block that returns a block

Imagine you wanted to use a block to compare a `double` to an `int` and return `true` if the `double` is greater than the `int` or `false` if the double is equal or smaller. In the simple case, that might look like this:

```objc
bool (^compareDoubleToInt)(int i, double j) = ^{ return j > i; };
```

Easy enough but imagine now that you want to break this into two pieces:

1. A first block which takes only the `int` and returns a second block, pre-configured to use this `int`.
2. The second block then takes the `double`, compares it to its pre-configured `int` and returns the result.

The first block is then a _factory block_ which creates instances of the second block that operate like the `compareDoubleToInt` shown above for a single, pre-configured value of `i`.

The complete implemention of this would be:

```objc
bool (^(^newDoubleToIntComparison)(int))(double) =
    ^(int i)
    {
        return Block_copy(^ (double j)
        {
            return j > i;
        });
    };
```

> Pay careful attention to the "new" in the name — this serves to notify that you must use `Block_destroy` on any blocks created in this fashion when you're done.

If everything about the syntax on that first line (the declaration) makes immediate sense to you, then you may consider yourself skilled at syntactic recursion.

The reason most people find this hard to read is that verbally, we would describe this scenario in a very different order:

1. Declare a variable:  
  `newDoubleToIntComparison`
2. It can be dereferenced to yield block information (and by _implication_ is therefore a block pointer):  
  `^newDoubleToIntComparison`
3. The block takes an `int` parameter:  
  `(^newDoubleToIntComparison)(int)`
4. Its return value can be dereferenced to yield block information (and by _implication_ the return value is therefore a block pointer):  
  `(^(^newDoubleToIntComparison)(int))`
5. This returned block takes a `double` parameter  
  `(^(^newDoubleToIntComparison)(int))(double)`
6. And the returned block returns a `bool`  
  `bool (^(^newDoubleToIntComparison)(int))(double);`

If C declarations read from left-to-right, it would be far less confusing. Instead, we have a situation where blocks that return blocks are recursively nested inside each other.

Of course, most people mitigate this by `typedef`'ing absolutely function pointer they ever use. Doing this for the previous block declaration changes it to:

```objc
typedef bool (^IsDoubleBiggerBlock)(double);
IsDoubleBiggerBlock (^newDoubleToIntComparison)(int);
```

## Functions or methods that return blocks

It may also be helpful to see the subtle difference between declaring a block that returns a block and the definition of of a function returns a block.

Replacing the _factory block_ with a _factory function_ in the previous example would lead to:

```objc
bool (^NewDoubleToIntComparisonFunction(int i))(double)
{
    return (bool (^)(double))Block_copy(^ (double j)
    {
        return j > i;
    });
};
```

This function takes a single `int` as its parameter and yet the last component on the function prototype line is `(double)`. The `int` parameter that the function actually takes and the name of the function are nested inside of the return type (the return type comprises the `double` parameter to the right, the caret character and the `bool` return value to the left).

Also notice that you need to cast the output of `Block_copy` to have it recognized as the correct return type.

As with the variable declarations, this nested behaviour is normally considered too annoying, so typedefs are employed to simplify:

```objc
typedef bool (^IsDoubleBiggerBlock)(double);
IsDoubleBiggerBlock NewDoubleToIntComparisonFunction(int i)
{
    return (IsDoubleBiggerBlock)Block_copy(^ (double j)
    {
        return j > i;
    });
};
```

This has the huge advantage that it puts the function's parameter back where it belongs — as the last component on the function prototype line.

An Objective-C method that returns a block is a much simpler situation since the method does not become nested within the return type in the same way. Instead, the return type looks identical to the cast of the returned copied block and the rest of the method remains distinct.

```objc
- (bool (^)(double))newDoubleToIntComparison:(int)i
{
    return (bool (^)(double))Block_copy(^ (double j)
    {
        return j > i;
    });
}
```

## Conclusion

The declaration of C function pointers is widely regarded as the worst syntax in the language. There is a good reason for this: the information in a function pointer's declaration flows from the most significant components which are nestled on the inside of the declaration to the least significant components which encircle the outside. They could flow left-to-right like a sentence but instead they flow outwards from an identifier somewhere in the middle.

Sadly, blocks follow in this tradition. All you can do to mitigate the torment is use `typedef`'d declarations judiciously and try to keep your blocks simple. They're not really intended for large numbers of parameters and complex return values, anyway.
