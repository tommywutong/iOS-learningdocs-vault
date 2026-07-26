---
title: 'Friday Q&A 2015-07-31: Tagged Pointer Strings'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-07-31-tagged-pointer-strings.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:35c80e270ee2896b'
translated: false
---

> 原文：[Friday Q&A 2015-07-31: Tagged Pointer Strings](https://www.mikeash.com/pyblog/friday-qa-2015-07-31-tagged-pointer-strings.html)　·　mikeash.com Friday Q&A

Posted at 2015-07-31 14:10 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-08-14: An Xcode Plugin for Unsmoothed Text](https://www.mikeash.com/pyblog/friday-qa-2015-08-14-an-xcode-plugin-for-unsmoothed-text.html)  
Previous article: [Friday Q&A 2015-07-17: When to Use Swift Structs and Classes](https://www.mikeash.com/pyblog/friday-qa-2015-07-17-when-to-use-swift-structs-and-classes.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2015-07-31: Tagged Pointer Strings

by [Mike Ash](https://www.mikeash.com/)

**Recap**  
Objects are aligned in memory, such that their address is always at least a multiple of the pointer size, and in practice typically a multiple of `16`. Object pointers are stored as a full 64-bit integer, but this alignment means that some of the bits will always be zero.

Tagged pointers take advantage of this fact to give special meaning to object pointers where those bits are _not_ zero. In Apple's 64-bit Objective-C implementation, object pointers with the least significant bit set to one (which is to say, odd numbers) are considered tagged pointers. Instead of doing the standard `isa` dereference to figure out the class, the next three bits are considered as an index into a tagged class table. This index is used to look up the class of the tagged pointer. The remaining 60 bits are then left up to the tagged class to use as they please.

A simple use for this would be to make suitable `NSNumber` instances be tagged pointers, with the extra `60` bits used to hold the numeric value. The bottom bit would be set to `1`. The next three bits would be set to the appropriate index for the `NSNumber` tagged class. The following `60` bits could then hold, for example, any integer value that fits within that space.

From the outside, such a pointer would look and act like any other object. It responds to messages like any other object, because `objc_msgSend` knows about tagged pointers. If you ask it for its `integerValue`, it will extract the data from those `60` bits and return it to you. However, you've saved a memory allocation, a pointer indirection on every access, and reference counting can be a no-op since there's no memory to free. For commonly used classes, this can make for a substantial performance improvement.

`NSString` doesn't seem like a good candidate for tagged pointers, since it's of variable length and can be much longer than the `60` bits in a tagged pointer. However, a tagged pointer class can coexist with a normal class, using tagged pointers for some values and normal pointers for others. For example, with `NSNumber`, any integer larger than `2^60 - 1` won't fit in the tagged pointer, and instead needs to be stored in a normal `NSNumber` objcet allocated in memory. As long as the code that creates the objects is written appropriately, this all works fine.

`NSString` could do the same thing. For strings that fit inside `60` bits, it could create a tagged pointer. Other strings would be placed in normal objects. This assumes that small strings are used often enough for this to be a noticeable performance gain. Is that actually the case in real-world code? It appears Apple thinks it is, since they went ahead and implemented it.

**Possible Implementations**  
Before we look at how Apple did things, let's take a moment to think about how we might implement tagged string storage. The basics are simple: set the bottom bit to one, set the remaining bits to the appropriate tagged class index, set the remaining bits to whatever. How to use the remaining bits is the big question. We want to take the maximum advantage of the `60` bits available to us.

A Cocoa string is conceptually a sequence of Unicode code points. There are 1,112,064 valid Unicode code points, so one code point takes `21` bits to represent. That means we could fit two code points into these `60` bits, with `18` bits wasted. We could borrow some of those extra bits to hold a length, so that a tagged string could be zero, one, or two code points. Being limited to only two code points doesn't seem very useful, though.

The `NSString` API is actually implemented in terms of `UTF-16`, not raw Unicode code points. `UTF-16` represents Unicode as a sequence of `16` bit values. The most common code points, which occupy the Basic Multilingual Plane or BMP, fit into a single `16` bit value, while code points above 65,535 require two. We could fit three `16` bit values into the `60` bits available, with `12` bits left over. Borrowing some bits for the length would allow us to represent 0-3 `UTF-16` code units. This would allow up to three code points in the BMP, and one code point beyond the BMP (plus, optionally, one code point within it). Being limited to three is still pretty tight though.

Most strings in an app are probably ASCII. Even if the app is localized into a non-ASCII language, strings are used for far more than just displaying UI. They're used for URL components, file extensions, object keys, property list values, and much more. The `UTF-8` encoding is an ASCII-compatible encoding that encodes each ASCII character as a single byte, while using up to four bytes for other Unicode code points. We can fit seven bytes in the `60` bits allotted to us, with `4` bits left over to use as a length. This allows our tagged strings to hold seven ASCII characters, or somewhat fewer non-ASCII characters, depending on exactly what they are.

If we're optimizing for ASCII, we might as well drop full Unicode support altogether. Strings containing non-ASCII characters can use real objects, after all. ASCII is a seven-bit encoding, so what if we allot only `7` bits per character? That lets us store up to eight ASCII characters in the `60` bits available, plus `4` bits left over for the length. This is starting to sound useful. There are probably a lot of strings in an app which are pure ASCII and contain eight characters or fewer.

Can we take it further? The full ASCII range contains a lot of stuff that isn't frequently used. There are a bunch of control characters, for example, and unusual symbols. Alphanumerics make up most of what's used. What can we squeeze into `6` bits?

`6` bits results in `64` possible values. There are `26` letters in the ASCII alphabet. Including both upper and lower case brings it up to `52`. Including all digits 0-9 brings it up to `62`. There are two spots to spare, which we might give to, say, space and period. There are probably a lot of strings which only contain these characters. At `6` bits each, we can fit ten in our `60` bits of storage! But wait! We don't have any leftover bits to store the length. So either we store nine characters plus a length, or we remove one of the `64` possible values (I nominate the space to be the one to go) and use zero as a terminator for strings shorter than ten characters.

How about `5` bits? This isn't totally ludicrous. There are probably a lot of strings which are just lowercase, for example. `5` bits gives `32` possible values. If you include the whole lowercase alphabet, there are `6` extra values, which you could allot to the more common uppercase letters, or some symbols, or digits, or some mix. If you find that some of these other possibilities are more common, you could even remove some of the less common lowercase letters, like `q`. `5` bits per character gives eleven characters if we save room for length, or twelve if we borrow a symbol and use a terminator.

Can we take it further? `5` bits is about as far as you can reasonably go with a fixed-size alphabet. You could switch to a variable length encoding, for example using a [Huffman code](https://en.wikipedia.org/wiki/Huffman_coding). This would allow the letter `e`, which is common, to be encoded with fewer bits than the letter `q`. This might allow for as little as `1` bit per character, in the unlikely case that your string is all `e`s. This would come at the cost of more complex and presumably slower code.

Which approach did Apple take? Let's find out.

**Exercising Tagged Strings**  
Here's a bit of code that creates a tagged string and prints its pointer value:

```
    NSString *a = @"a";
    NSString *b = [[a mutableCopy] copy];
    NSLog(@"%p %p %@", a, b, object_getClass(b));
```

The `mutableCopy`/`copy` dance is necessary for two reasons. First, although a string like `@"a"` could be stored as a tagged pointer, constant strings are never tagged pointers. Constant strings must remain binary compatible across OS releases, but the internal details of tagged pointers are not guaranteed. This works fine as long as tagged pointers are always generated by Apple's code at runtime, but it would break down if the compiler embedded them in your binary, as would be the case with a constant string. Thus we need to copy the constant string to get a tagged pointer.

The `mutableCopy` is necessary because `NSString` is too clever for us, and knows that a `copy` of an immutable string is a pointless operation, and returns the original string as the "copy." Constant strings are immutable, so the result of `[a copy]` is just `a`. A mutable copy forces it to make an actual copy, and then making an immutable copy of the result is enough to convince the system to give us a tagged pointer string.

Note that you must never depend on these details in your own code! The circumstances in which the `NSString` code decides to give you a tagged pointer could change at any time and if you write code that somehow relies on it, that code will eventually break. Fortunately, you have to go out of your way to do that, and all normal, sensible code will work fine, blissfully ignorant of tagged anything.

Here's what the above code prints on my computer:

```
    0x10ba41038 0x6115 NSTaggedPointerString
```

You can see the original pointer first, a nice round number indicative of an object pointer. The copy is the second value, and its taggedness is abundantly clear. It's an odd number, which means it can't be a valid object pointer. It's also a small number, well within the unmapped and unmappable 4GB zero page at the beginning of the 64-bit Mac address space, making it doubly imposible to be an object pointer.

What can we deduce from this value of `0x6115`? We know that the bottom four bits are part of the tagged pointer mechanism itself. The lowest nybble `5` is `0101` in binary. The bottom one bit indicates that it's a tagged pointer. The next three bits indicate the tagged class. Here those bits are `010`, indicating that the tagged string class occupies index `2`. Not that there's much to do with that information.

The `61` that leads the value is suggestive. `61` in hexadecimal happens to be the ASCII value of the lowercase letter `a`, which is exactly what the string contains. It looks like there's a straight ASCII encoding in use. Convenient!

The class name makes it obvious what this class is for, and gives us a good starting point when it comes to looking into the actual code that implements this feature. We'll get to that shortly, but let's do some more outside inspection first.

Here's a loop that builds up strings of the form `abcdef...` and prints them out one by one until it stops getting tagged pointers back:

```
    NSMutableString *mutable = [NSMutableString string];
    NSString *immutable;
    char c = 'a';
    do {
        [mutable appendFormat: @"%c", c++];
        immutable = [mutable copy];
        NSLog(@"0x%016lx %@ %@", immutable, immutable, object_getClass(immutable));
    } while(((uintptr_t)immutable & 1) == 1);
```

The first iteration prints:

```
    0x0000000000006115 a NSTaggedPointerString
```

This matches what we saw above. Note that I'm printing out the full pointer with all leading zeroes to make things a bit more clear when comparing subsequent iterations. Let's compare with the second iteration:

```
    0x0000000000626125 ab NSTaggedPointerString
```

The bottom four bits didn't change, as we'd expect. That `5` will remain constant, always indicating that this is a tagged pointer of type `NSTaggedPointerString`.

The original `61` stays where it was, joined now by a `62`. `62` is, of course, the ASCII code for `b`, so we can see that this encoding is an eight-bit encoding that uses ASCII. The four bits just before the terminal `5` changed from `1` to `2`, suggesting that this might be the length. Subsequent iterations confirm this:

```
    0x0000000063626135 abc NSTaggedPointerString
    0x0000006463626145 abcd NSTaggedPointerString
    0x0000656463626155 abcde NSTaggedPointerString
    0x0066656463626165 abcdef NSTaggedPointerString
    0x6766656463626175 abcdefg NSTaggedPointerString
```

Presumably that's the end of it. The tagged pointer is full, and the next iteration will allocate an object and terminate the loop. Right? Wrong!

```
    0x0022038a01169585 abcdefgh NSTaggedPointerString
    0x0880e28045a54195 abcdefghi NSTaggedPointerString
    0x00007fd275800030 abcdefghij __NSCFString
```

The loop goes through two more iterations before terminating. The length section continues to increase, but the rest of the tagged pointer turns into gibberish. What's going on? Let's turn to the implementation to find out.

**Disassembly**  
The `NSTaggedPointer` class lives in the CoreFoundation framework. It seems like it ought to live in Foundation, but a lot of the core Objective-C classes have been moved to CoreFoundation these days as Apple slowly gives up on making CoreFoundation an independent entity.

Let's start by looking at the implementation of `-[NSTaggedPointerString length]`:

```
    push       rbp
    mov        rbp, rsp
    shr        rdi, 0x4
    and        rdi, 0xf
    mov        rax, rdi
    pop        rbp
    ret
```

Hopper provides this handy decompilation to go along with it:

```
    unsigned long long -[NSTaggedPointerString length](void * self, void * _cmd) {
        rax = self >> 0x4 & 0xf;
        return rax;
    }
```

In short, to obtain the length, extract bits 4-7 and return them. This confirms what we observed above, that the four bits just before the terminal `5` indicate the length of the string.

The other primitive method for an `NSString` subclass is `characterAtIndex:`. I'll skip the lengthy disassembly and go straight to Hopper's decompiled output, which is pretty readable:

```
    unsigned short -[NSTaggedPointerString characterAtIndex:](void * self, void * _cmd, unsigned long long arg2) {
        rsi = _cmd;
        rdi = self;
        r13 = arg2;
        r8 = ___stack_chk_guard;
        var_30 = *r8;
        r12 = rdi >> 0x4 & 0xf;
        if (r12 >= 0x8) {
                rbx = rdi >> 0x8;
                rcx = "eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX";
                rdx = r12;
                if (r12 < 0xa) {
                        do {
                                *(int8_t *)(rbp + rdx + 0xffffffffffffffbf) = *(int8_t *)((rbx & 0x3f) + rcx);
                                rdx = rdx - 0x1;
                                rbx = rbx >> 0x6;
                        } while (rdx != 0x0);
                }
                else {
                        do {
                                *(int8_t *)(rbp + rdx + 0xffffffffffffffbf) = *(int8_t *)((rbx & 0x1f) + rcx);
                                rdx = rdx - 0x1;
                                rbx = rbx >> 0x5;
                        } while (rdx != 0x0);
                }
        }
        if (r12 <= r13) {
                rbx = r8;
                ___CFExceptionProem(rdi, rsi);
                [NSException raise:@"NSRangeException" format:@"%@: Index %lu out of bounds; string length %lu"];
                r8 = rbx;
        }
        rax = *(int8_t *)(rbp + r13 + 0xffffffffffffffc0) & 0xff;
        if (*r8 != var_30) {
                rax = __stack_chk_fail();
        }
        return rax;
    }
```

Let's clean this up a little. The first three lines are just Hopper telling us which registers get which arguments. Let's go ahead and replace all uses of `rsi` with `_cmd` and `rdi` with `self`. `arg2` is actually the `index` parameter, so let's replace all uses of `r13` with `index`. And we'll get rid of the `__stack_chk` stuff, as it's just a security hardening thing and not relevant to the actual workings of the method. Here's what the code looks like when cleaned up in this way:

```
    unsigned short -[NSTaggedPointerString characterAtIndex:](void * self, void * _cmd, unsigned long long index) {
        r12 = self >> 0x4 & 0xf;
        if (r12 >= 0x8) {
                rbx = self >> 0x8;
                rcx = "eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX";
                rdx = r12;
                if (r12 < 0xa) {
                        do {
                                *(int8_t *)(rbp + rdx + 0xffffffffffffffbf) = *(int8_t *)((rbx & 0x3f) + rcx);
                                rdx = rdx - 0x1;
                                rbx = rbx >> 0x6;
                        } while (rdx != 0x0);
                }
                else {
                        do {
                                *(int8_t *)(rbp + rdx + 0xffffffffffffffbf) = *(int8_t *)((rbx & 0x1f) + rcx);
                                rdx = rdx - 0x1;
                                rbx = rbx >> 0x5;
                        } while (rdx != 0x0);
                }
        }
        if (r12 <= index) {
                rbx = r8;
                ___CFExceptionProem(self, _cmd);
                [NSException raise:@"NSRangeException" format:@"%@: Index %lu out of bounds; string length %lu"];
                r8 = rbx;
        }
        rax = *(int8_t *)(rbp + index + 0xffffffffffffffc0) & 0xff;
        return rax;
    }
```

Right before the first `if` statement is this line:

```
    r12 = self >> 0x4 & 0xf
```

We can recognize this as the same length extraction code that we saw in the implementation of `-length` above. Let's go ahead and replace `r12` with `length` throughout:

```
    unsigned short -[NSTaggedPointerString characterAtIndex:](void * self, void * _cmd, unsigned long long index) {
        length = self >> 0x4 & 0xf;
        if (length >= 0x8) {
                rbx = self >> 0x8;
                rcx = "eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX";
                rdx = length;
                if (length < 0xa) {
                        do {
                                *(int8_t *)(rbp + rdx + 0xffffffffffffffbf) = *(int8_t *)((rbx & 0x3f) + rcx);
                                rdx = rdx - 0x1;
                                rbx = rbx >> 0x6;
                        } while (rdx != 0x0);
                }
                else {
                        do {
                                *(int8_t *)(rbp + rdx + 0xffffffffffffffbf) = *(int8_t *)((rbx & 0x1f) + rcx);
                                rdx = rdx - 0x1;
                                rbx = rbx >> 0x5;
                        } while (rdx != 0x0);
                }
        }
        if (length <= index) {
                rbx = r8;
                ___CFExceptionProem(self, _cmd);
                [NSException raise:@"NSRangeException" format:@"%@: Index %lu out of bounds; string length %lu"];
                r8 = rbx;
        }
        rax = *(int8_t *)(rbp + index + 0xffffffffffffffc0) & 0xff;
        return rax;
    }
```

Looking inside the `if` statement, the first line shifts `self` right by `8` bits. The bottom `8` bits are bookkeeping: the tagged pointer indicator, and the string length. The remainder is then, we presume, the actual data. Let's replace `rbx` with `stringData` to make that more clear. The next line appears to put some sort of lookup table into `rcx`, so let's replace `rcx` with `table`. Finally, `rdx` gets a copy of the value of `length`. It looks like it gets used as some sort of cursor later, so let's replace `rdx` with `cursor`. Here's what we have now:

```
    unsigned short -[NSTaggedPointerString characterAtIndex:](void * self, void * _cmd, unsigned long long index) {
        length = self >> 0x4 & 0xf;
        if (length >= 0x8) {
                stringData = self >> 0x8;
                table = "eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX";
                cursor = length;
                if (length < 0xa) {
                        do {
                                *(int8_t *)(rbp + cursor + 0xffffffffffffffbf) = *(int8_t *)((stringData & 0x3f) + table);
                                cursor = cursor - 0x1;
                                stringData = stringData >> 0x6;
                        } while (cursor != 0x0);
                }
                else {
                        do {
                                *(int8_t *)(rbp + cursor + 0xffffffffffffffbf) = *(int8_t *)((stringData & 0x1f) + table);
                                cursor = cursor - 0x1;
                                stringData = stringData >> 0x5;
                        } while (cursor != 0x0);
                }
        }
        if (length <= index) {
                rbx = r8;
                ___CFExceptionProem(self, _cmd);
                [NSException raise:@"NSRangeException" format:@"%@: Index %lu out of bounds; string length %lu"];
                r8 = rbx;
        }
        rax = *(int8_t *)(rbp + index + 0xffffffffffffffc0) & 0xff;
        return rax;
    }
```

That's almost everything labeled. One raw register name remains: `rbp`. That's actually the frame pointer, so the compiler is doing something tricky indexing directly off the frame pointer. Adding the constant `0xffffffffffffffbf` is the two's-complement "everything is ultimately an unsigned integer" way to subtract `65`. Later on, it subtracts `64`. This is all probably the same local variable on the stack. Given the bytewise indexing going on, it's probably a buffer placed on the stack. But it's weird, because there's a code path which does nothing but _read_ from that buffer, without ever writing to it. What's going on?

It turns out that what's going on is Hopper forgot to decompile the `else` branch of that outer `if` statement. The relevant assembly looks like this:

```
    mov        rax, rdi
    shr        rax, 0x8
    mov        qword [ss:rbp+var_40], rax
```

`var_40` is how Hopper shows that offset of `64` in the disassembly. (`40` being the hexadecimal version of `64`.) Let's call the pointer to this location `buffer`. The C version of this missing branch would look like:

```
    *(uint64_t *)buffer = self >> 8
```

Let's go ahead and insert that, and replace the other places where `rbp` is used to access `buffer` with more readable versions of the code, plus add a declaration of `buffer` to remind us what's going on:

```
    unsigned short -[NSTaggedPointerString characterAtIndex:](void * self, void * _cmd, unsigned long long index) {
        int8_t buffer[11];
        length = self >> 0x4 & 0xf;
        if (length >= 0x8) {
                stringData = self >> 0x8;
                table = "eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX";
                cursor = length;
                if (length < 0xa) {
                        do {
                                *(int8_t *)(buffer + cursor - 1) = *(int8_t *)((stringData & 0x3f) + table);
                                cursor = cursor - 0x1;
                                stringData = stringData >> 0x6;
                        } while (cursor != 0x0);
                }
                else {
                        do {
                                *(int8_t *)(buffer + cursor - 1) = *(int8_t *)((stringData & 0x1f) + table);
                                cursor = cursor - 0x1;
                                stringData = stringData >> 0x5;
                        } while (cursor != 0x0);
                }
        } else {
            *(uint64_t *)buffer = self >> 8;
        }
        if (length <= index) {
                rbx = r8;
                ___CFExceptionProem(self, _cmd);
                [NSException raise:@"NSRangeException" format:@"%@: Index %lu out of bounds; string length %lu"];
                r8 = rbx;
        }
        rax = *(int8_t *)(buffer + index) & 0xff;
        return rax;
    }
```

Getting better. All those crazy pointer manipulation statements are a bit hard to read, though, and they're really just array indexing. Let's fix those up:

```
    unsigned short -[NSTaggedPointerString characterAtIndex:](void * self, void * _cmd, unsigned long long index) {
        int8_t buffer[11];
        length = self >> 0x4 & 0xf;
        if (length >= 0x8) {
                stringData = self >> 0x8;
                table = "eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX";
                cursor = length;
                if (length < 0xa) {
                        do {
                                buffer[cursor - 1] = table[stringData & 0x3f];
                                cursor = cursor - 0x1;
                                stringData = stringData >> 0x6;
                        } while (cursor != 0x0);
                }
                else {
                        do {
                                buffer[cursor - 1] = table[stringData & 0x1f];
                                cursor = cursor - 0x1;
                                stringData = stringData >> 0x5;
                        } while (cursor != 0x0);
                }
        } else {
            *(uint64_t *)buffer = self >> 8;
        }
        if (length <= index) {
                rbx = r8;
                ___CFExceptionProem(self, _cmd);
                [NSException raise:@"NSRangeException" format:@"%@: Index %lu out of bounds; string length %lu"];
                r8 = rbx;
        }
        rax = buffer[index];
        return rax;
    }
```

Now we're getting somewhere.

We can see that there are three cases depending on the length. Length values less than 8 go through that missing `else` branch that just dumps the value of `self`, shifted, into `buffer`. This is the plain ASCII case. Here, `index` is used to index into the value of `self` to extract the given byte, which is then returned to the caller. Since ASCII character values match Unicode code points within the ASCII range, there's no additional manipulation needed to make the value come out correctly. We guessed above that the string stored plain ASCII in this case, and this confirms it.

What about the cases where the length is `8` or more? If the length is `8` or more but less than `10` (`0xa`), then the code enters a loop. This loop extracts the bottom `6` bits of `stringData`, uses that as an index into `table`, and then copies that value into `buffer`. It then shifts `stringData` down by `6` bits and repeats until it runs through the entire string. This is a six-bit encoding where the mapping from raw six-bit values to ASCII character values is stored in the table. A temporary version of the string is built up in `buffer`, and the indexing operation at the end then extracts the requested character from it.

What about the case where the length is `10` or more? The code there is almost identical, except that it works five bits at a time instead of six. This is a more compact encoding that would allow the tagged string to store up to `11` characters, but only using an alphabet of `32` values. This will use the first half of `table` as its truncated alphabet.

Thus we can see that the structure of the tagged pointer strings is:

1. If the length is between `0` and `7`, store the string as raw eight-bit characters.
2. If the length is `8` or `9`, store the string in a six-bit encoding, using the alphabet `"eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX"`.
3. If the length is `10` or `11`, store the string in a five-bit encoding, using the alphabet `"eilotrm.apdnsIc ufkMShjTRxgC4013"`

Let's compare with the data we generated earlier:

```
    0x0000000000006115 a NSTaggedPointerString
    0x0000000000626125 ab NSTaggedPointerString
    0x0000000063626135 abc NSTaggedPointerString
    0x0000006463626145 abcd NSTaggedPointerString
    0x0000656463626155 abcde NSTaggedPointerString
    0x0066656463626165 abcdef NSTaggedPointerString
    0x6766656463626175 abcdefg NSTaggedPointerString
    0x0022038a01169585 abcdefgh NSTaggedPointerString
    0x0880e28045a54195 abcdefghi NSTaggedPointerString
    0x00007fbad9512010 abcdefghij __NSCFString
```

The binary expansion of `0x0022038a01169585` minus the bottom eight bits and divided into six-bit chunks is:

```
    001000 100000 001110 001010 000000 010001 011010 010101
```

Using these to index into the table, we can see that this does indeed spell out `"abcdefgh". Similarly, the binary expansion of`0x0880e28045a54195` minus the bottom eight bits and divided into six-bit chunks is:

```
    001000 100000 001110 001010 000000 010001 011010 010101 000001
```

We can see that it's the same string, plus `i` at the end.

But then it goes off the rails. After this point, it should switch to a five-bit encoding and give us two more strings, but instead it starts allocating objects at length `10`. What gives?

The five-bit alphabet is _extremely_ limited, and doesn't include the letter `b`! That letter must not be common enough to warrant a place in the `32` hallowed characters of the five-bit alphabet. Let's try this again, but instead start the string at `c`. Here's the output:

```
    0x0000000000006315 c NSTaggedPointerString
    0x0000000000646325 cd NSTaggedPointerString
    0x0000000065646335 cde NSTaggedPointerString
    0x0000006665646345 cdef NSTaggedPointerString
    0x0000676665646355 cdefg NSTaggedPointerString
    0x0068676665646365 cdefgh NSTaggedPointerString
    0x6968676665646375 cdefghi NSTaggedPointerString
    0x0038a01169505685 cdefghij NSTaggedPointerString
    0x0e28045a54159295 cdefghijk NSTaggedPointerString
    0x01ca047550da42a5 cdefghijkl NSTaggedPointerString
    0x39408eaa1b4846b5 cdefghijklm NSTaggedPointerString
    0x00007fbd6a511760 cdefghijklmn __NSCFString
```

We now have tagged strings all the way up to a length of `11`. The binary expansions of the last two tagged strings are:

```
    01110 01010 00000 10001 11010 10101 00001 10110 10010 00010
    01110 01010 00000 10001 11010 10101 00001 10110 10010 00010 00110
```

Exactly what we're expecting.

**Creating Tagged Strings**  
Since we know how tagged strings are encoded, I won't go into much detail on the code that creates them. The code in question is found within a private function called `__CFStringCreateImmutableFunnel3` which handles every conceivable string creation case all in one gigantic function. This function is included in the open source release of CoreFoundation available on [opensource.apple.com](http://opensource.apple.com), but don't get excited: the tagged pointer strings code is not included in the open source version.

The code here is essentially the inverse of what's above. If the string's length and content fits what a tagged pointer string can hold, it builds a tagged pointer piece by piece, containing either ASCII, six-bit, or five-bit characters. There's an inverse of the lookup table. The table seen above as a constant string lives as a global variable called `sixBitToCharLookup`, and there's a corresponding table called `charToSixBitLookup` in the `Funnel3` function.

**That Weird Table**  
The full six-bit encoding table is:

```
    eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX
```

A natural question here is: why is it in such a strange order?

Because this table is used for both six-bit and five-bit encodings, it makes sense that it wouldn't be entirely in alphabetical order. Characters that are used most frequently should be in the first half, while characters that are used less frequently should go in the second half. This ensures that the maximum number of longer strings can use the five-bit encoding.

However, with that division in place, the order within the individual halves doesn't matter. The halves themselves could be sorted alphabetically, but they're not.

The first few letters in the table is similar to the order in which letters appear in English, sorted by frequency. The most common letter in English is E, then T, then A, O, I, N, and S. E is right at the beginning of the table, and the others are near the beginning. The table appears to be sorted by frequency of use. The discrepancy with English probably arises because short strings in Cocoa apps aren't a random selection of words from English prose, but a more specialized bit of language.

I speculate that Apple originally intended to use a fancier variable-length encoding, probably based on a [Huffman code](https://en.wikipedia.org/wiki/Huffman_coding). This turned out to be too difficult, or not worth the effort, or they just ran out of time, and so they dialed it back to the less ambitious version seen above, where strings choose between constant-length encodings using eight, six, or five bits per character. The weird table lives on as a leftover, and a starting point if they decide to go for a variable-length encoding in the future. This is pure guesswork, but that's what it looks like to me.

**Conclusion**  
Tagged pointers are a really cool technology. Strings are an unusual application of it, but it's clear that Apple put a lot of thought into it and they must see a significant benefit. It's interesting to see how it's put together and how they got the most out of the very limited storage available.

That's it for today. Come back next time for more strange explorations of the trans-mundane. Friday Q&A is driven by reader suggestions, so if you have an idea for a subject you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-07-31-tagged-pointer-strings.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
