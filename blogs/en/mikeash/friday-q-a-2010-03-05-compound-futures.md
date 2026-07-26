---
title: 'Friday Q&A 2010-03-05: Compound Futures'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-03-05-compound-futures.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0b7221b430a58ed6'
translated: false
---

> 原文：[Friday Q&A 2010-03-05: Compound Futures](https://www.mikeash.com/pyblog/friday-qa-2010-03-05-compound-futures.html)　·　mikeash.com Friday Q&A

Posted at 2010-03-05 13:53 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-03-12: Subclassing Class Clusters](https://www.mikeash.com/pyblog/friday-qa-2010-03-12-subclassing-class-clusters.html)  
Previous article: [Friday Q&A 2010-02-26: Futures](https://www.mikeash.com/pyblog/friday-qa-2010-02-26-futures.html)  
Tags: [blocks](https://www.mikeash.com/pyblog/?tag=blocks) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [futures](https://www.mikeash.com/pyblog/?tag=futures)

Friday Q&A 2010-03-05: Compound Futures

by [Mike Ash](https://www.mikeash.com/)

I'm going to assume that you've read last week's article and understand what a future is and how the `MAFuture` library works. If you haven't seen it, please read that post before continuing with this one.

**Code**  
 As before, the library is available from my subversion repository:

```
    svn co http://mikeash.com/svn/MAFuture/
```

Or just click on the hyperlink above to browse it.

**Compound Futures**  
 The futures I discussed last week are implicit futures, which behave as a proxy to the result of the calculation being futured. They look and act like the real object. Once the proxy is messaged, then the future is resolved and the message is passed on to the real object.

A _compound_ future is more complex. Whenever possible, messaging a compound future doesn't resolve the future. Instead, it _returns another future_. This is also a compound future, which will in turn return more compound futures, until you have a whole chain of futures set up. Only when you send a message that can't be futured (essentially, a message that returns a primitive rather than an object) is the future resolved, with resolution proceeding up the chain.

As an example, consider this code:

```
    NSString *string = ...;
    NSArray *components = [string componentsSeparatedByString: @" "];
    NSString *first = [components objectAtIndex: 0];
    NSString *second = [components objectAtIndex: 1];
    second = [second uppercaseString];
    
    printf("%s: %s\n", [first UTF8String], [second UTF8String]);
```

Nothing unusual there. Now let's toss in a compound future:

```
    NSString *string = MACompoundLazyFuture(^{ return ...; });
    NSArray *components = [string componentsSeparatedByString: @" "];
    NSString *first = [components objectAtIndex: 0];
    NSString *second = [components objectAtIndex: 1];
    second = [second uppercaseString];
    
    printf("%s: %s\n", [first UTF8String], [second UTF8String]);
```

Now the futures start to chain. The call to

returns a future thet depends on the future stored in

. The calls to

return futures that depend on the array future. The call to

returns yet another future. Finally, the calls to

can't be futured because they return a primitive, and so they cause the entire chain to be resolved.

The sequence of futures ends up looking like this:

```
                MACompoundLazyFuture(^{ return ...; })
                                |
                                |
                                v
                    componentsSeparatedByString:
                    |                          |
                    |                          |
                    v                          v
            objectAtIndex:                objectAtIndex:
                                               |
                                               |
                                               v
                                        uppercaseString
```

Just like with simple futures, compound futures come in two varieties: lazy and background. A lazy compound future doesn't perform any computation until it's resolved. A background compound future begins the

as soon as it's created, and futures additional calls until that computation completes. Note that background futures are only one layer deep: the sub-futures that it creates are lazy futures. To pull from the above example,

will never execute until a future in the tree gets resolved, even if the original future was a background future.

It would be possible to develop a background compound future that performed each calculation in the tree in the background instead of just the first one, but I didn't take things that far. It would be an interesting mechanism for managing a large number of implicit, interdependent parallel computations.

**Design**  
 Compound futures are implemented in the `_MACompoundFuture` class, which is a subclass of `_MALazyBlockFuture`. This lets them inherit the behavior of wrapping a block and resolving the future represented by that block. Compound lazy futures directly wrap the block that's passed in to create the future. Compound background futures wrap the block in a `MABackgroundFuture` first, then use a small block that returns the value of the background future. This technique leverages the existing futures code to avoid duplication of effort.

Compound futures then override the forwarding machinery defined in `_MASimpleFuture` to implement the compound future mechanism.

For any given call, the future needs to decide whether that call requires resolution, or whether it can return a new future. This involves checking the method signature of the call. If it returns a primitive, or any of the parameters are pointers to primitives (which could be used to return a value by reference), then the future needs to be resolved. Otherwise, a future can be returned.

I decided to get fancy, and also return futures for any pointer-to-pointer-to-object parameters. This means that things like `NSError` return-by-references can be futured.

If a given call requires resolution, then `forwardingTargetForSelector:` detects that, resolves the future, and forwards the call to the target. If the call can be futured, then `forwardInvocation:` takes care of returning a future for the return value, and for any return-by-reference parameters.

**Method Signatures**  
 To know whether a call can be futured, and to use `forwardInvocation:`, the code needs a method signature for each selector which is sent.

This is problematic, because with a compound future, you want to be able to obtain this method signature without resolving the future. This means that you can't ask the target object for a method signature, because it doesn't exist yet.

I (mostly) solved this problem with a class called `MAMethodSignatureCache`. This class will take a selector and search all classes registered with the runtime for that selector. If it finds a method, and if all methods have the same method signature, then it returns it. Since this is slow, the result of each search is cached, thus the class name.

What happens if two classes implement the same method but have a different method signature? This is why I said "(mostly)" above. In this case it's impossible to know which one is correct. I solved this by simply giving up on the problem; if the method signature is unknown, then the future is resolved immediately, and the message forwarded directly to the object that can handle it.

**Will it Future?**  
 As you've seen, a key question that the code needs to answer is whether a particular selector can be futured or whether it requires resolution. `_MACompoundFuture` answers this question using a private `_canFutureSelector:` method.

This method fetches the method signature for the selector from `MAMethodSignatureCache`. If the signature doesn't exist, or if it doesn't return an object, then the answer is immediately NO:

```
    - (BOOL)_canFutureSelector: (SEL)sel
    {
        NSMethodSignature *sig = [[MAMethodSignatureCache sharedCache] cachedMethodSignatureForSelector: sel];
        
        if(!sig) return NO;
        else if([sig methodReturnType][0] != @encode(id)[0]) return NO;
```

If the signature passes those two tests, it then checks the parameter types to see if there are any non-object pointer arguments. If there are, then they prevent futuring as well. If that test passes too, then the selector can be futured:

```
        // it exists, returns an object, but does it return any non-objects by reference?
        unsigned num = [sig numberOfArguments];
        for(unsigned i = 2; i < num; i++)
        {
            const char *type = [sig getArgumentTypeAtIndex: i];
            
            // if it's a pointer to a non-object, bail out
            if(type[0] == '^' && type[1] != '@')
                return NO;
        }
        // we survived this far, all is well
        return YES;
    }
```

The implementation of

makes two checks. First, it checks to see if the future has been resolved. If it has, then it forwards the message to the result. If it hasn't, it then checks to see if the selector can be futured. If it can, then it returns

to get on the

path. Finally, if the selector can't be futured, then it resolves the future and forwards the message to it:

```
    - (id)forwardingTargetForSelector: (SEL)sel
    {
        LOG(@"forwardingTargetForSelector: %p %@", self, NSStringFromSelector(sel));
        
        id value = [self futureValue];
        if(value)
            return value;
        else if([self _canFutureSelector: sel])
            return nil;
        else
            return [self resolveFuture];
    }
```

The

method is much the same: grab a signature from the futured value if it's available, from the method signature cache if possible, and if all else fails, resolve the future and ask the real value:

```
    - (NSMethodSignature *)methodSignatureForSelector: (SEL)sel
    {
        LOG(@"methodSignatureForSelector: %p %@", self, NSStringFromSelector(sel));
        
        NSMethodSignature *sig = [[self futureValue] methodSignatureForSelector: sel];
        
        if(!sig)
            sig = [[MAMethodSignatureCache sharedCache] cachedMethodSignatureForSelector: sel];
        
        if(!sig)
            sig = [[self resolveFuture] methodSignatureForSelector: sel];
        
        return sig;
    }
```

The real magic of this class happens in its gigantic

implementation.

The beginning is straightforward. Grab the future value and whether it's been resolved. If it's been resolved, forward the invocation to the value. Normally, if the future has been resolved, this would be caught in `-forwardingTargetForSelector:`. However, it's possible that another thread could have caused it to be resolved in between the two calls, and this makes that case behave nicely. It also allows for handling `nil` in cases where the correct method signature can be determined, as a `nil` future value will always trigger `forwardInvocation:` due to the semantics of `forwardingTargetForSelector:`.

```
    - (void)forwardInvocation: (NSInvocation *)invocation
    {
        LOG(@"forwardInvocation: %p %@", self, NSStringFromSelector([invocation selector]));
        
        [_lock lock];
        id value = _value;
        BOOL resolved = _resolved;
        [_lock unlock];
        
        if(resolved)
        {
            LOG(@"forwardInvocation: %p forwarding to %p", invocation, value);
            [invocation invokeWithTarget: value];
        }
        else
```

If the future hasn't been resolved, then the method needs to run through the invocation and replace any return-by-reference objects with futures. This gets pretty hairy.

If there are any return-by-reference objects, then this code is going to create multiple compound futures (one for the actual return value, and one for each return-by-reference parameter) which all depend on the same invocation. It would be incorrect to invoke the invocation each time one of the futures resolves, because the method it's calling may have side effects and shouldn't be called twice. We need a way to have the invocation be called exactly once, on demand. Fortunately I already have code to do exactly that: it's called a lazy future!

Futuring the invocation is only necessary if there are return-by-reference parameters, which I don't know yet, so I start out without one. These parameter futures all use storage which needs to be tracked, so I declare an array variable here as well, which is also created on demand:

```
        {
            // look for return-by-reference objects
            _MALazyBlockFuture *invocationFuture = nil;
            NSMutableArray *parameterDatas = nil;
```

Now loop through all the arguments to the method:

```
            NSMethodSignature *sig = [invocation methodSignature];
            unsigned num = [sig numberOfArguments];
            for(unsigned i = 2; i < num; i++)
            {
```

Examine each argument's type. If the type is a pointer to object (starts with

) then we need to future it:

```
                const char *type = [sig getArgumentTypeAtIndex: i];
                if(type[0] == '^' && type[1] == '@')
                {
```

The first thing the code has to do is fetch the parameter that the caller passed in, so we know where to store the newly-created future:

```
                    // get the existing pointer-to-object
                    id *parameterValue;
                    [invocation getArgument: &parameterValue; atIndex: i];
```

Do a quick

check, since there's no need to create a future if the caller didn't ask for a value:

```
                    // if it's NULL, then we don't need to do anything
                    if(parameterValue)
                    {
                        LOG(@"forwardInvocation: %p found return-by-reference object at argument index %u", self, i);
```

Now we know where to store the future, but we still have to pass a parameter in to the called function. We can't leave the original parameter, because that's pointing to a local variable which could be gone by the time the code actually executes, and in any case will contain a future and shouldn't be altered arbitrarily. Instead, we need to pass a pointer to some new storage where the called method can safely store the return-by-reference value.

Allocating this space is tricky, because that space eventually needs to be freed. It would make sense free it after the future we create for that parameter has resolved, but we can't guarantee that it ever _will_ resolve. It's possible that the value would be ignored, and if the space was freed on resolution, it would leak in that case.

The solution is to allocate the space using `NSMutableData`, and to capture that data in the block used to create the future. This ties the `NSMutableData`'s lifetime to that of the block. If the future is resolved, the block is destroyed, and the space is destroyed. If the future is never resolved, it's eventually destroyed, destroying the block and the allocated space.

```
                        // allocate space to receive the final computed value
                        NSMutableData *newParameterSpace = [NSMutableData dataWithLength: sizeof(id)];
```

Now that we have that space allocated, we can set it as the new value for that parameter:

```
                        id *newParameterValue = [newParameterSpace mutableBytes];
                        
                        // set the parameter to point to the new space
                        [invocation setArgument: &newParameterValue; atIndex: i];
```

Near the top of the method, I declared

to hold a future that would resolve the invocation. Now I have to check it, and set it if this is the first parameter to need it. This future also keeps all of the

instances alive by capturing the

array. The individual parameter futures may be destroyed before the invocation is invoked, so the fact that they keep their individiual instances alive is not enough. Note that the future's side effect is what's important, not its value, so it just returns

:

```
                        // create a future to refer to the invocation, so that it
                        // only gets invoked once no matter how many
                        // compound futures reference it
                        if(!invocationFuture)
                        {
                            parameterDatas = [NSMutableArray array];
                            invocationFuture = [[_MALazyBlockFuture alloc] initWithBlock: ^{
                                [invocation invokeWithTarget: [self resolveFuture]];
                                // keep all parameter datas alive until the invocation is resolved
                                // by capturing the variable
                                [parameterDatas self];
                                return (id)nil;
                            }];
                            [invocationFuture autorelease];
                        }
                        [parameterDatas addObject: newParameterSpace];
```

All the preliminaries are taken care of, so now we can actually create the compound future that will be returned by reference to the caller, and "return" it by saving the pointer into their parameter:

```
                        // create the compound future that we'll "return" in this argument
                        _MACompoundFuture *parameterFuture = [[_MACompoundFuture alloc] initWithBlock: ^{
                            [invocationFuture resolveFuture];
                            // capture the NSMutableData to ensure that it stays live
                            // interior pointer problem
                            [newParameterSpace self];
                            return *newParameterValue;
                        }];
                        
                        // and now "return" it
                        *parameterValue = parameterFuture;
                        
                        // memory management
                        [parameterFuture autorelease];
                    }
                }
            }
```

Arguments are all taken care of, now it's time to create the return value. First I instruct the invocation to retain its arguments, because it needs to live in the long term, which I could do anywhere in this method but chose to do here:

```
            [invocation retainArguments];
```

Next, I create a new compound future for the return value. This future uses the value of

if it's been created. If not, then it manually invokes the invocation. Either way, it then fetches the invocation's return value and returns it as its own value:

```
            _MACompoundFuture *returnFuture = [[_MACompoundFuture alloc] initWithBlock:^{
                id value = nil;
                if(invocationFuture)
                    [invocationFuture resolveFuture];
                else
                    [invocation invokeWithTarget: [self resolveFuture]];
                [invocation getReturnValue: &value;];
                return value;
            }];
```

Finally, set this future as the invocation's return value, and we're done!

```
            LOG(@"forwardInvocation: %p creating new compound future %p", invocation, returnFuture);
            [invocation setReturnValue: &returnFuture;];
            [returnFuture release];
        }
    }
```

Like with the simple futures, I wrap this class in a couple of helper functions.

creates a compound future wrapping a regular background future:

```
    id MACompoundBackgroundFuture(id (^block)(void))
    {
        id blockFuture = MABackgroundFuture(block);
        
        _MACompoundFuture *compoundFuture = [[_MACompoundFuture alloc] initWithBlock: ^{
            return [blockFuture resolveFuture];
        }];
        
        return [compoundFuture autorelease];
    }
```

And

just wraps its block directly:

```
id MACompoundLazyFuture(id (^block)(void))
{
    _MACompoundFuture *compoundFuture = [[_MACompoundFuture alloc] initWithBlock: block];
    
    return [compoundFuture autorelease];
}
```

Like with the other helpers, I wrap these in some crazy macros to get the types right:

```
    #define MACompoundBackgroundFuture(...) ((__typeof((__VA_ARGS__)()))MACompoundBackgroundFuture((id (^)(void))(__VA_ARGS__)))
    #define MACompoundLazyFuture(...) ((__typeof((__VA_ARGS__)()))MACompoundLazyFuture((id (^)(void))(__VA_ARGS__)))
```

Amazingly, this stuff all works. You can create compound futures, chain them out a long way, and verify that they only get resolved once you hit a primitive return value.

**Caveats**  
 Simple futures are pretty robust and can generally be passed to code which has no idea what they are, with a big exception being if you ever return `nil` from one, as discussed last week.

Compound futures are not so nice. They have two big problems with unsuspecting code. First, because they chain, you end up with arbitrary messages being sent, and this can include ones which return `nil`, which falls into that dangerous case. Second, methods can have side effects, and compound futures can cause those side effects to happen out of order, which will cause hilarity to ensue.

To illustrate the first problem, imagine the following method, which just happens to use old-style enumeration instead of fast enumeration:

```
    - (NSArray *)appendedStringsFromArray: (NSArray *)array
    {
        NSMutableArray *outArray = [NSMutableArray array];
        NSEnumerator *enumerator = [array objectEnumerator];
        NSString *str;
        while((str = [enumerator nextObject]))
            [outArray addObject: [str stringByAppendingString: @" suffix"]];
        return outArray;
    }
```

This code is fine. However, consider what happens if you pass a compound future in as the array parameter. Nothing in this code will cause a compound future to resolve. The

object will be a compound future, and every call to

will also produce a compound future. This code will loop forever, and eventually crash when it runs out of memory. Oops!

To illustrate the second problem, consider this code:

```
    NSMutableArray *array = ...;
    NSString *s = [[array objectAtIndex: 0] retain];
    [array removeAllObjects];
    NSLog(@"%@", s);
```

This code works fine normally, but if

is a compound future then it falls apart. The

call will be futured, and then

will resolve the array future and remove the elements. However,

still contains a future. When it's resolved by the

call, it will call

on an array which is now empty, throwing a range error. Oops!

You must be careful when writing code that uses compound futures, and ensure that they never escape to code that you don't control. Making explicit calls to `resolveFuture` and passing what it returns is a way to make sure that can't happen.

**Practical Uses**  
 I'll be straight: I haven't been able to think of any.

I'm sure that there are cases where compound futures would be useful. The chaining nature makes it possible to put off computation for longer than with a basic future. However, the fact that you have to be careful never to let them escape to code you don't control (or to code you haven't written to tolerate them) places big restrictions on your code. Unlike simple futures, which I consider to be a useful tool, I see compound futures as more of an interesting programming exercise. I would love to see some real, useful applications of them, though.

**Conclusion**  
 Compound futures are an interesting concept which might, maybe, possibly have actual practical applications somewhere. They show that `NSInvocation` and forwarding are nothing to be afraid of, but can be bent to our will. And of course they continue to illustrate just how wonderful an addition blocks make to Objective-C.

That's everything for this week. Come back next week for another Friday Q&A. Friday Q&A is driven by reader submissions, so if you have an idea that you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

No comments have been posted.

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
