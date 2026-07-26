---
title: 'Friday Q&A 2013-02-08: Let''s Build Key-Value Coding'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-02-08-lets-build-key-value-coding.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2455c810cad34765'
translated: false
---

> 原文：[Friday Q&A 2013-02-08: Let's Build Key-Value Coding](https://www.mikeash.com/pyblog/friday-qa-2013-02-08-lets-build-key-value-coding.html)　·　mikeash.com Friday Q&A

Posted at 2013-02-08 14:17 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-02-22: Let's Build UITableView](https://www.mikeash.com/pyblog/friday-qa-2013-02-22-lets-build-uitableview.html)  
Previous article: [Friday Q&A 2013-01-25: Let's Build NSObject](https://www.mikeash.com/pyblog/friday-qa-2013-01-25-lets-build-nsobject.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2013-02-08: Let's Build Key-Value Coding

by [Mike Ash](https://www.mikeash.com/)

**Basics**  
Key-value coding (KVC) is an API that allows string-based access to object properties. `NSObject` implements the methods to look up accessor methods or instance variables based on the key name, and fetch or set the value using those.

There are two basic methods that form the basis of KVC.

The `valueForKey:` method searches for a getter method with the same name as the key. If found, it calls the method and returns its return value. If none is found, it searches for an instance variable with the same name as the key. Failing those, it looks for an instance variable with the same name as the key, but prefixed with an underscore. If an instance variable is found, it returns the value it currently holds.

The `setValue:forKey:` method performs the same search, except that it searches for a setter method rather than a getter. It then either calls the setter or sets the instance variable directly.

An interesting feature of both of these methods is that they work with primitive values by automatically boxing and unboxing them into instances of `NSNumber` or `NSValue`. You can use `valueForKey:` to invoke a method that returns `int`, and the result will be an `NSNumber` object containing the return value. Likewise, you can use `setValue:forKey:` to invoke a method that takes `int`, pass it an `NSNumber`, and it will automatically extract the integer value.

KVC also has the concept of key paths, which are sequences of keys put together with periods, like:

```
    foo.bar.baz
```

There are corresponding methods to work with key paths: `valueForKeyPath:` and `setValue:forKeyPath:`. These simply call the more primitive methods recursively.

There are a bunch of other KVC features for managing collections, but these are less interesting and I'm going to skip over them here.

**Code**  
Today's code is available on GitHub as part of the `MAObject` project:

[https://github.com/mikeash/MAObject](https://github.com/mikeash/MAObject)

Let's get to it.

**valueForKey:**  
The first thing that `valueForKey:` does is check for a getter method with the same name as the key.

```
    - (id)valueForKey: (NSString *)key
    {
        SEL getterSEL = NSSelectorFromString(key);
        if([self respondsToSelector: getterSEL])
        {
```

If the object responds to that selector, it will use the accessor to get the value. Exactly how that's done will depend on the accessor's return type. To get ready, it fetches the return type and `IMP` for the method:

```
            NSMethodSignature *sig = [self methodSignatureForSelector: getterSEL];
            char type = [sig methodReturnType][0];
            IMP imp = [self methodForSelector: getterSEL];
```

If the return type is an object or a class, then the code is simple: cast the `IMP` to the right function pointer type, call it, and return what it returns:

```
            if(type == @encode(id)[0] || type == @encode(Class)[0])
            {
                return ((id (*)(id, SEL))imp)(self, getterSEL);
            }
```

Otherwise, the method returns a primitive, which is where things get interesting.

There is no convenient way to take a function pointer with an arbitrary type, call it, and box up the result. We have to do things the brute-force way, by enumerating all of the possibilities one by one and writing code to handle each possible type. I created a small macro to help with this:

```
            else
            {
                #define CASE(ctype, selectorpart) \
                    if(type == @encode(ctype)[0]) \
                        return [NSNumber numberWith ## selectorpart: ((ctype (*)(id, SEL))imp)(self, getterSEL)];
```

The idea is that each type gets a single line. You pass the type name as one parameter, and a selector part that fits in with `[NSNumber numberWithType:]` as the other parameter. The macro uses these to construct code that checks for the type and calls the `IMP` with the right function pointer type if it matches. With this macro, it's just a matter of writing out every supported primitive type:

```
                CASE(char, Char);
                CASE(unsigned char, UnsignedChar);
                CASE(short, Short);
                CASE(unsigned short, UnsignedShort);
                CASE(int, Int);
                CASE(unsigned int, UnsignedInt);
                CASE(long, Long);
                CASE(unsigned long, UnsignedLong);
                CASE(long long, LongLong);
                CASE(unsigned long long, UnsignedLongLong);
                CASE(float, Float);
                CASE(double, Double);
```

Let's not forget to undefine the `CASE` macro so we can reuse the name later:

```
                #undef CASE
```

If a matching case was found, then the method returned immediately. If the method is still running at this point, then the type isn't known. Rather than try to handle this gracefully somehow, the method just throws an exception to complain:

```
                [NSException raise: NSInternalInconsistencyException format: @"Class %@ key %@ don't know how to interpret method return type from getter, signature is %@", [isa description], key, sig];
            }
        }
```

That was the code to handle the case where a getter method exists. If no getter exists, then KVC falls back to instance variables. First, it tries to get an instance variable with the same name as the key:

```
        Ivar ivar = class_getInstanceVariable(isa, [key UTF8String]);
```

If that fails, it tries again with a leading underscore:

```
        if(!ivar)
            ivar = class_getInstanceVariable(isa, [[@"_" stringByAppendingString: key] UTF8String]);
```

If either of those found an instance variable, it proceeds to actually fetching its value. In order to fetch the contents of the variable, we need to know where it's stored. This is done by getting the variable's offset, and adding it to the value of `self`:

```
        if(ivar)
        {
            ptrdiff_t offset = ivar_getOffset(ivar);
            char *ptr = (char *)self;
            ptr += offset;
```

`self` is cast to `char *` first, because the offset is in bytes, and operating on a `char *` ensures that the `+=` operation does what we need.

We also need to know the type of the variable:

```
            const char *type = ivar_getTypeEncoding(ivar);
```

If the type is an object or class, then it just extracts the value directly and returns it:

```
            const char *type = ivar_getTypeEncoding(ivar);
            if(type[0] == @encode(id)[0] || type[0] == @encode(Class)[0])
            {
                return *(id *)ptr;
            }
```

Otherwise, it falls back to special cases again. This code uses a slightly different `CASE` macro. This one checks the type and then extracts the value from `ptr` if there's a match:

```
            else
            {
                #define CASE(ctype, selectorpart) \
                    if(strcmp(type, @encode(ctype)) == 0) \
                        return [NSNumber numberWith ## selectorpart: *(ctype *)ptr];
```

Once again, there's a long list of supported types:

```
                CASE(char, Char);
                CASE(unsigned char, UnsignedChar);
                CASE(short, Short);
                CASE(unsigned short, UnsignedShort);
                CASE(int, Int);
                CASE(unsigned int, UnsignedInt);
                CASE(long, Long);
                CASE(unsigned long, UnsignedLong);
                CASE(long long, LongLong);
                CASE(unsigned long long, UnsignedLongLong);
                CASE(float, Float);
                CASE(double, Double);
```

Followed by macro cleanup:

```
                #undef CASE
```

This code falls back to creating a generic `NSValue` with the contents of `ptr` if there's no match. Because the data is already laid out in memory, it's trivial to have a fallback here, rather than just throwing an exception like the getter code above does:

```
                return [NSValue valueWithBytes: ptr objCType: type];
            }
        }
```

Finally, if no getter or instance variable was found, the method throws an exception. The dummy return statement at the end is just to ensure that the compiler doesn't complain about not returning a value:

```
        [NSException raise: NSInternalInconsistencyException format: @"Class %@ is not key-value compliant for key %@", [isa description], key];
        return nil;
    }
```

That takes care of `valueForKey:`.

**setValue:forKey:**  
The `setValue:forKey:` method works similarly, but there are some differences due to the fact that it has to set values rather than retrieve them.

The first thing it does is construct the name of the setter method to search for. `valueForKey:` can simply translate the key directly to a selector, but this method needs to do a bit of work. The setter method is generated by capitalizing the first letter of the key, then adding "set" to the beginning, and a colon at the end:

```
    - (void)setValue: (id)value forKey: (NSString *)key
    {
        NSString *setterName = [NSString stringWithFormat: @"set%@:", [key capitalizedString]];
```

It then turns that into a selector and checks to see if the object responds:

```
        SEL setterSEL = NSSelectorFromString(setterName);
        if([self respondsToSelector: setterSEL])
        {
```

If it does, it fetches the method's argument type and `IMP` much like the getter code above:

```
            NSMethodSignature *sig = [self methodSignatureForSelector: setterSEL];
            char type = [sig getArgumentTypeAtIndex: 2][0];
            IMP imp = [self methodForSelector: setterSEL];
```

If the type is an object or class, it simply calls the setter, passing `value`, and returns:

```
            if(type == @encode(id)[0] || type == @encode(Class)[0])
            {
                ((void (*)(id, SEL, id))imp)(self, setterSEL, value);
                return;
            }
```

Otherwise, it's once again time for a `CASE` macro. This one calls the `IMP`, passing `[value typeValue]` as the parameter, when a match is found:

```
            else
            {
                #define CASE(ctype, selectorpart) \
                    if(type == @encode(ctype)[0]) { \
                        ((void (*)(id, SEL, ctype))imp)(self, setterSEL, [value selectorpart ## Value]); \
                        return; \
                    }
```

Here is the big list of cases:

```
                CASE(char, char);
                CASE(unsigned char, unsignedChar);
                CASE(short, short);
                CASE(unsigned short, unsignedShort);
                CASE(int, int);
                CASE(unsigned int, unsignedInt);
                CASE(long, long);
                CASE(unsigned long, unsignedLong);
                CASE(long long, longLong);
                CASE(unsigned long long, unsignedLongLong);
                CASE(float, float);
                CASE(double, double);
```

Followed by macro cleanup:

```
                #undef CASE
```

Last, if the type is unknown, it throws an exception:

```
                [NSException raise: NSInternalInconsistencyException format: @"Class %@ key %@ set from incompatible object %@", [isa description], key, value];
            }
        }
```

If no setter method is found, then it searches for instance variables. No string manipulation is needed, since the instance variable's name doesn't change the way the setter's name does. This code does the same check for instance variables with a leading underscore:

```
        Ivar ivar = class_getInstanceVariable(isa, [key UTF8String]);
        if(!ivar)
            ivar = class_getInstanceVariable(isa, [[@"_" stringByAppendingString: key] UTF8String]);
```

If the instance variable exists, it creates a pointer to it and gets its type just like `valueForKey:` does:

```
        if(ivar)
        {
            ptrdiff_t offset = ivar_getOffset(ivar);
            char *ptr = (char *)self;
            ptr += offset;

            const char *type = ivar_getTypeEncoding(ivar);
```

If the variable is an object or class pointer, the code can set it directly. Well, nearly directly. There's a minor `retain` `release` dance to be done in order to ensure that memory management is correct:

```
            if(type[0] == @encode(id)[0] || type[0] == @encode(Class)[0])
            {
                value = [value retain];
                [*(id *)ptr release];
                *(id *)ptr = value;
                return;
            }
```

Otherwise, `value` is boxed, and the primitive value needs to be extracted. If `value` is an `NSValue` with the _exact_ same type as the instance variable, the `getValue:` method can be used to simply copy the value over directly:

```
            else if(strcmp([value objCType], type) == 0)
            {
                [value getValue: ptr];
                return;
            }
```

If that doesn't work, it's time to fall back to the last long list of cases. This version of the `CASE` macro sets the value at `ptr`, appropriately cast, to `[value typeValue]`:

```
            else
            {
                #define CASE(ctype, selectorpart) \
                    if(strcmp(type, @encode(ctype)) == 0) { \
                        *(ctype *)ptr = [value selectorpart ## Value]; \
                        return; \
                    }
```

The traditional exhaustive enumeration of primitive types follows:

```
                CASE(char, char);
                CASE(unsigned char, unsignedChar);
                CASE(short, short);
                CASE(unsigned short, unsignedShort);
                CASE(int, int);
                CASE(unsigned int, unsignedInt);
                CASE(long, long);
                CASE(unsigned long, unsignedLong);
                CASE(long long, longLong);
                CASE(unsigned long long, unsignedLongLong);
                CASE(float, float);
                CASE(double, double);
```

Macro cleanup:

```
                #undef CASE
```

Finally, if none of the cases were hit, throw an exception:

```
                [NSException raise: NSInternalInconsistencyException format: @"Class %@ key %@ set from incompatible object %@", [isa description], key, value];
            }
        }
```

If neither setter method nor instance variable was found, throw an exception to complain:

```
        [NSException raise: NSInternalInconsistencyException format: @"Class %@ is not key-value compliant for key %@", [isa description], key];
    }
```

**Key Paths**  
To round out the implementation of KVC, I'll implement `valueForKeyPath:` and `setValue:forKeyPath:` as well.

The first thing that `valueForKeyPath:` does is look for a `.` in the key path. If it doesn't exist, then it's treated as a plain key and passed to `valueForKey:`

```
    - (id)valueForKeyPath: (NSString *)keyPath
    {
        NSRange range = [keyPath rangeOfString: @"."];
        if(range.location == NSNotFound)
            return [self valueForKey: keyPath];
```

Otherwise, the key is split into two pieces. The piece up to the `.` is the local key, and the following piece is the remainder of the key path:

```
        NSString *key = [keyPath substringToIndex: range.location];
        NSString *rest = [keyPath substringFromIndex: NSMaxRange(range)];
```

The key is passed to `valueForKey:`

```
        id next = [self valueForKey: key];
```

Then `valueForKeyPath:` is sent recursively to the `next` object:

```
        return [next valueForKeyPath: rest];
    }
```

Its implementation will decompose `rest` further until every `.` is consumed. The result is a chain of `valueForKey:` calls, returning the result of the very last call.

`setValue:forKeyPath:` works similarly. If there's no `.` in the key path, call `setValue:forKey:` and return:

```
    - (void)setValue: (id)value forKeyPath: (NSString *)keyPath
    {
        NSRange range = [keyPath rangeOfString: @"."];
        if(range.location == NSNotFound)
        {
            [self setValue: value forKey: keyPath];
            return;
        }
```

Otherwise, extract the key and remainder:

```
        NSString *key = [keyPath substringToIndex: range.location];
        NSString *rest = [keyPath substringFromIndex: NSMaxRange(range)];
```

Grab the next object using `valueForKey:`

```
        id next = [self valueForKey: key];
```

Then recursively send `setValue:forKeyPath:` to `next`, passing `rest` as the key path:

```
        [next setValue: value forKeyPath: rest];
    }
```

The result is a chain of `valueForKey:` calls, culminating in a call to `setValue:forKey:` on the last object in the chain.

**Conclusion**  
You can now see how key-value coding works on the inside. There isn't anything particularly complicated. It's largely just a long list of different things to try. Cocoa's implementation is a bit smarter, and can leverage things like `NSInvocation` for more comprehensive coverage, but that's the basic idea. A large part of `NSInvocation` is simply baked-in knowledge of all the different cases that need to be handled as well.

That's it for today. May you code your keys and values in peace. Until next time, since Friday Q&A is driven by reader suggestions, please [send in your ideas for topics](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-02-08-lets-build-key-value-coding.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
