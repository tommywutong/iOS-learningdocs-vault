---
title: 'Friday Q&A 2013-05-17: Let''s Build stringWithFormat:'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-05-17-lets-build-stringwithformat.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:515788201f9d01ce'
translated: false
---

> 原文：[Friday Q&A 2013-05-17: Let's Build stringWithFormat:](https://www.mikeash.com/pyblog/friday-qa-2013-05-17-lets-build-stringwithformat.html)　·　mikeash.com Friday Q&A

Posted at 2013-05-17 14:40 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-05-31: C Quiz](https://www.mikeash.com/pyblog/friday-qa-2013-05-31-c-quiz.html)  
Previous article: [Friday Q&A 2013-05-03: Proper Use of Asserts](https://www.mikeash.com/pyblog/friday-qa-2013-05-03-proper-use-of-asserts.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2013-05-17: Let's Build stringWithFormat:

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Romanian (translation by Petry Krontory)](http://fotonin.com/edu/vineri-qa-2013-05-17-sa-build-stringwithformat/).

**String Formatting**  
It's hard to get very far in Cocoa without knowing about format strings, but just in case, here's a recap.

`stringWithFormat:`, as well as other calls like `NSLog`, take strings that can use special format specifiers of the form `%x`. The `%` indicates that it's a format specifier, which reads an additional argument and adds it to the string. The character after it specifies what kind of data to display. For example:

```
    [NSString stringWithFormat: @"Hello, %@: %d %f", @"world", 42, 1.0]
```

This produces the string:

```
    Hello, world: 42 1.0
```

This is useful for all sorts of things, from creating user-visible text, to making dictionary keys, to printing debug logs.

**Variable Arguments**  
This method takes variable arguments, which is an odd corner of C. For more extensive coverage of how to write such methods, see [my article on vararg macros and functions](https://www.mikeash.com/pyblog/friday-qa-2009-08-21-writing-vararg-macros-and-functions.html). Here's a quick recap.

You declare the function or method to take variable arguments by putting `...` at the end of the parameter list. For a method, this ends up being slightly odd syntax:

```
    + (id)stringWithFormat: (NSString *)format, ...;
```

That `, ...` thing at the end is actually legal Objective-C.

Once in the method, declare a variable of type `va_list` to represent the variable argument list. The `va_start` and `va_args` macros initialize and clean it up. The `va_arg` macro will extract one argument from the list and return it.

**Code**  
As usual, I have posted the code on GitHub. You can view the repository here:

[https://github.com/mikeash/StringWithFormat](https://github.com/mikeash/StringWithFormat)

This code supports an extremely limited subset of the full `NSString` formatting functionality. `NSString` supports a huge number of specifiers, as well as options such as field width, precision, and out-of-order arguments. My reimplementation sticks to a basic set that's enough to illustrate what's going on. In particular, it supports:

- `%d` - `int`
- `%ld` - `long`
- `%lld` - `long long`
- `%u`, `%lu`, and `%llu`, for the unsigned variants of the above.
- `%f` - `float`
- `%s` - C strings
- `%@` - Objective-C objects
- `%%` - Output a single `%` character.

Furthermore, no options are supported.

**Interface**  
For my reimplementation, I wrote a function called `MAStringWithFormat` that does the same thing as `[NSString stringWithFormat:]`. However, I wrapped the meat of the implementation in a class to organize the various bits of state needed. That function just makes a `va_list` for the arguments, instantiates a formatter, and asks it to do the work:

```
    NSString *MAStringWithFormat(NSString *format, ...)
    {
        va_list arguments;
        va_start(arguments, format);

        MAStringFormatter *formatter = [[MAStringFormatter alloc] init];
        NSString *result = [formatter format: format arguments: arguments];

        va_end(arguments);

        return result;
    }
```

The `MAStringFormatter` class essentially carries out two tasks in parallel. First, it reads through the format string character-by-character, and secondly, it writes the resulting string. Accordingly, it has two groups of instance variables. The first group deals with reading through the format string:

```
    CFStringInlineBuffer _formatBuffer;
    NSUInteger _formatLength;
    NSUInteger _cursor;
```

`CFStringInlineBuffer` is a little-known API in `CFString` that allows for efficiently iterating through the individual characters of a string. Making a function or method call for each character is slow, so `CFStringInlineBuffer` allows fetching them in bulk for greater efficiency. The length of the format string is stored to avoid running off the end, and the current position within the format string is stored in `_cursor`.

The second group deals with collecting the output of the formatting operation. It consists of a buffer of characters, the current location within that buffer, and its total size:

```
    unichar *_outputBuffer;
    NSUInteger _outputBufferCursor;
    NSUInteger _outputBufferLength;
```

This could be implemented using an `NSMutableData` or `NSMutableString`, but this is much more efficient. While this code isn't intended to be particularly fast in general, I just couldn't stand the thought of making each character run through a call to a string object.

**Reading**  
`MAStringFormatter` has a `read` method which fetches the next character from `_formatBuffer`, and returns `-1` once it reaches the end of the string. There isn't a whole lot to this, just an `if` check and a call to `CFStringGetCharacterFromInlineBuffer`:

```
    - (int)read
    {
        if(_cursor < _formatLength)
            return CFStringGetCharacterFromInlineBuffer(&_formatBuffer, _cursor++);
        else
            return -1;
    }
```

**Writing**  
Writing is a little more complex, because the size of the output string isn't known ahead of time. First, there's a `doubleOutputBuffer` method that increases the size of the output buffer. If the buffer is completely empty, it allocates it to hold `64` characters. If it's already allocated, it doubles the size:

```
    - (void)doubleOutputBuffer
    {
        if(_outputBufferLength == 0)
            _outputBufferLength = 64;
        else
            _outputBufferLength *= 2;
```

Once the new buffer length is computed, a simple call to `realloc` allocates or reallocates the buffer:

```
        _outputBuffer = realloc(_outputBuffer, _outputBufferLength * sizeof(*_outputBuffer));
    }
```

Next, there's a `write:` method, which takes a single `unichar` and appends it to the buffer. If the write cursor is already at the end of the buffer, it first increases the size of the buffer:

```
    - (void)write: (unichar)c
    {
        if(_outputBufferCursor >= _outputBufferLength)
            [self doubleOutputBuffer];
```

Once sufficient storage is assured, it places `c` at the current cursor position, and advances the cursor:

```
        _outputBuffer[_outputBufferCursor] = c;
        _outputBufferCursor++;
    }
```

**Formatting**  
The `format:arguments:` method is the entry point to where the real work gets done. The first thing it does is fill out the format string instance variables using the `format` argument:

```
    - (NSString *)format: (NSString *)format arguments: (va_list)arguments
    {
        _formatLength = [format length];
        CFStringInitInlineBuffer((__bridge CFStringRef)format, &_formatBuffer, CFRangeMake(0, _formatLength));
        _cursor = 0;
```

It also initializes the output variables. This isn't necessary, strictly speaking, but leaves open the possibility of reusing a single formatter object:

```
        _outputBuffer = NULL;
        _outputBufferCursor = 0;
        _outputBufferLength = 0;
```

After that, it loops through the format string until it runs off the end:

```
        int c;
        while((c = [self read]) >= 0)
        {
```

All format specifiers begin with the `'%'` character. If `c` is not a `'%'`, then just write the character directly to the output:

```
            if(c != '%')
            {
                [self write: c];
            }
```

This comparison uses the character literal `'%'` despite the fact that `read` deals in `unichar`. This works because the first 128 Unicode code points map directly to the 128 ASCII characters. When a `unichar` contains a `%`, it contains the same value as the ASCII `'%'`, and the same is true for any other ASCII character. This is terribly convenient when working with ASCII data in `NSString`s.

If `c` is a `'%'` character, then there's a format specifier to come. What happens at this point depends on what the next character is:

```
            else
            {
                int next = [self read];
```

If the format specifier is a `'d'`, then it reads an `int` from the arguments and passes it to the `writeLongLong:` method, which handles the actual work of formatting the value into the output. All signed integers pass through that method. Since `long long` is the largest signed data type handled, a single method that prints those will work for all signed types:

```
                if(next == 'd')
                {
                    int value = va_arg(arguments, int);
                    [self writeLongLong: value];
                }
```

If the format specifier is `'u'`, then it does the same thing as above, but with `unsigned`, and calling through to the `writeUnsignedLongLong:` method:

```
                else if(next == 'u')
                {
                    unsigned value = va_arg(arguments, unsigned);
                    [self writeUnsignedLongLong: value];
                }
```

Note that `int` and `unsigned` are the smallest integer types handled here. There is no code to handle `char` or `short`. This is because of C promotion rules for functions that take variable arguments. When passed as a variable arguments, values of type `char` or `short` are promoted to `int`, and likewise the `unsigned` variants are promoted to `unsigned int`. This means that the code for `int` handles the smaller data types as well, without any additional work.

If the next character is `'l'`, then we need to keep reading to figure out what to do:

```
                else if(next == 'l')
                {
                    next = [self read];
```

If the character following the `'l'` is `'d'`, then the argument is a `long`. Follow the same basic procedure as before:

```
                    if(next == 'd')
                    {
                        long value = va_arg(arguments, long);
                        [self writeLongLong: value];
                    }
```

Likewise, if the next character is `'u'`, it's an `unsigned long`:

```
                    else if(next == 'u')
                    {
                        unsigned long value = va_arg(arguments, unsigned long);
                        [self writeUnsignedLongLong: value];
                    }
```

If the next character is `'l'` again, then we need to read one character further

```
                    else if(next == 'l')
                    {
                        next = [self read];
```

Here, `'d'` indicates a `long long`, and `'u'` indicates an `unsigned long long`. These are handle in the same fashion as before:

```
                        if(next == 'd')
                        {
                            long long value = va_arg(arguments, long long);
                            [self writeLongLong: value];
                        }
                        else if(next == 'u')
                        {
                            unsigned long long value = va_arg(arguments, unsigned long long);
                            [self writeUnsignedLongLong: value];
                        }
                    }
                }
```

That's it for the deep sequence of `'l'` variants. Next comes a check for `'f'`. In that case, the argument is a `double', and gets passed off to a method built to handle that:

```
                else if(next == 'f')
                {
                    double value = va_arg(arguments, double);
                    [self writeDouble: value];
                }
```

Once again, promotion rules simplify things a bit. When a `float` is passed as a variable argument, it's promoted to a `double`, so no extra code is needed to handle `float`.

If the format specifier is an `'s'`, then the argument is a C string:

```
                else if(next == 's')
                {
                    const char *value = va_arg(arguments, const char *);
```

This is simple enough not to need a helper method. It iterates through the string until it reaches the terminating `0`, writing each character as it goes. This assumes the string contains only ASCII:

```
                    while(*value)
                        [self write: *value++];
                }
```

If the format specifier is a `'@'`, then the argument is an Objective-C object:

```
                else if(next == '@')
                {
                    id value = va_arg(arguments, id);
```

To find out what to output, ask the value for its description:

```
                    NSString *description = [value description];
```

The length of the description is also handy:

```
                    NSUInteger length = [description length];
```

Now, copy the contents of `description` into the output buffer. I decided to get a bit fancy here. A simple loop could suffice, perhaps using `CFStringInlineBuffer` for speed, but I wanted something nicer. An `NSString` can put its contents into an arbitrary buffer, so why not ask `description` to put its contents directly into the output buffer? To do that, the output buffer must first be made large enough to contain `length` characters:

```
                    while(length > _outputBufferLength - _outputBufferCursor)
                        [self doubleOutputBuffer];
```

Doing this in a `while` loop is mildly inefficient if `description` is larger than the buffer is already. However, that's an uncommon case, and the code is nicer by being able to share `doubleOutputBuffer`, so I decided to use this approach.

Now that the output buffer is sufficiently large, use `getCharacters:range:` to dump the contents of `description` into it, putting it at the location of the output cursor:

```
                    [description getCharacters: _outputBuffer + _outputBufferCursor range: NSMakeRange(0, length)];
```

Finally, move the cursor past the newly written data:

```
                    _outputBufferCursor += length;
                }
```

We're nearly to the end. If the character following the `'%'` is another `'%'`, that's the siganl to write a literal `'%'` character:

```
                else if(next == '%')
                {
                    [self write: '%'];
                }
            }
        }
```

That's the last case handled by this miniature implementation. Once the loop terminates, the resulting `unichar`s are located in `_outputBuffer`, with `_outputBufferCursor` indicating the number of `unichar`s in the buffer. Create an `NSString` from it and return the new string:

```
        NSString *output = [[NSString alloc] initWithCharactersNoCopy: _outputBuffer length: _outputBufferCursor freeWhenDone: YES];
        return output;
    }
```

Using the `NoCopy` variant makes this potentially more efficient, and removes the need to manually `free` the buffer.

That's the basic shell of the formatting code. To complete it, we need the code to print signed and unsigned `long long`s, and code to print `double`s.

**`unsigned long long`**  
Let's start with the most fundamental helper method, `writeUnsignedLongLong:`. The others ultimately rely on this one for much of their work.

The algorithm is simple: divide by successive powers of ten, produing a single digit each time. Convert the digit to a `unichar` and write it.

We'll store the power of ten in a variable called `cursor` and start it at `1`:

```
    - (void)writeUnsignedLongLong: (unsigned long long)value
    {
        unsigned long long cursor = 1;
```

However, what we really want is the power of ten with as many digits as the input number. For example, for `42`, we want `10`. For `123456`, we want `100000`. To obtain this, we just keep multiplying `cursor` by ten until it has the same number of digits as `value`, which is easily tested by seeing if `value` is less than ten times larger than `cursor`:

```
        while(value / cursor >= 10)
            cursor *= 10;
```

Now we just loop, dividing `cursor` by ten each time, until we run out of `cursor`:

```
        while(cursor > 0)
        {
```

The current digit is obtained by dividing `value` by `cursor`:

```
            int digit = value / cursor;
```

To compute the `unichar` that corresponds with `digit`, just add the literal `'0'` character. ASCII (and therefore Unicode) lays out digits sequentially starting with `'0'`, making this easy:

```
            [self write: '0' + digit];
```

With the digit written, we remove it from `value`, then move `cursor` down:

```
            value -= digit * cursor;
            cursor /= 10;
        }
    }
```

And just like that, the value flows into the output. This code even correctly handles zero, due to ensuring that `cursor` is always at least `1`.

**`long long`**  
The `writeLongLong:` method is simple. If the number is less than zero, write a `'-'` and negate the number. For positive numbers, do nothing special. Pass the final non-negative number to `writeUnsignedLongLong:`.

```
    - (void)writeLongLong: (long long)value
    {
        unsigned long long unsignedValue = value;
        if(value < 0)
        {
            [self write: '-'];
            unsignedValue = -unsignedValue;
        }
        [self writeUnsignedLongLong: unsignedValue];
    }
```

There's an odd corner case in here. Due to the nature of [the two's complement representation of signed integers](http://en.wikipedia.org/wiki/Two's_complement), the magnitude of the smallest representable `long long` is one greater than the magnitude of the largest representable `long long` on systems we're likely to encounter.

A `long long` on a typical system can hold numbers all the way down to `-9223372036854775808`, but only up to `9223372036854775807`. This means you can't negate the smallest possible negative number and get a positive number, because the data type can't hold the appropriate positive number. If you try to negate `-9223372036854775808`, you get an overflow and undefined behavior, although the result is usually just `-9223372036854775808` again.

However, negation is well defined on all `unsigned` values, and it has the same bitwise result as negation on the bitwise-equivalent signed values. In other words, `-signedLongLong` produces the same bits as `-(unsigned long long)signedLongLong`. It also works on the bits that make up `-9223372036854775808`, and produces `9223372036854775808`. By moving `value` into `unsignedValue` and then negating that, the above code works around the problem of undefined behavior when negating the smallest representable `long long`.

**`double`**  
Now it's time for the really fun one. Due to the nature of floating-point arithmetic, figuring out how to properly and accurately print the value of a `double` was pretty tough. I did some research, even dove into an open-source implementation of `printf` to see how they did it, but it was so crazy and incomprehensible that I didn't get too far. I finally settled on a technique which works fairly well, and I think is as accurate as the data type allows, although the output tends to have more digits than it strictly needs.

The first step in solving the problem is to break it into two pieces. I split the double into the integer part and the fractional part, then deal with each one separately. Print each part in base 10, separate the two with a dot, and done.

The trick, then, is how to print the integer and fractional parts in base 10. I didn't want to use the same technique of successive division that I used for `unsigned long long`, because I was concerned that it would lose accuracy. There are integers that can be represented in a `double`, but where the result of dividing the integer by ten can't be exactly represented in a `double`. Similarly, I was afraid that the equivalent successive multiplication by ten for the fractional part would lose precision.

However, dividing or multiplying a double by two to move is _always_ safe, unless it pushes it beyond the limits of what can be represented. If you only do this to push it closer to `1.0`, then it will never lose precision. Furthermore, it's possible to chop off the fractional part of a double without losing precision in the integer part, and vice versa. Put together, these operations allow extracting information from a `double` bit by bit, which is enough to compute an integer representation of its integer and fractional parts. With those in hand, the existing `writeUnsignedLongLong:` method can be used to print the digits.

With this in mind, I set off. The first step is to check for negative values. If `value` is negative, write a `'-'`, and negate it:

```
    - (void)writeDouble: (double)value
    {
        if(value < 0.0)
        {
            [self write: '-'];
            value = -value;
        }
```

Unlike the `long long` case, there are no `double` values less than `0.0` that can't be safely and correctly negated, so no shenanigans are needed here.

Next, check for infinity and NaN, and short circuit the whole attempt for them:

```
        if(isinf(value) || isnan(value))
        {
            const char *str = isinf(value) ? "INFINITY" : "NaN";
            while(*str)
                [self write: *str++];
            return;
        }
```

If the number is an actual number, extract the integer and fractional parts.

```
        double intpart = trunc(value);
        double fracpart = value - intpart;
```

With those in hand, call out to helper methods to write those two parts, separated by a dot:

```
        [self writeDoubleIntPart: intpart];
        [self write: '.'];
        [self writeDoubleFracPart: fracpart];
    }
```

**Integer Part**  
Writing the integer part is the simpler of the two, conceptually. The strategy is to shift the `double` value one bit to the right until the value becomes zero. Each bit that's extracted is added to an `unsigned long long` accumulator. Once the `double` becomes zero, the accumulator contains its integer value.

The one tricky part is how to handle the case where the `double` contains a value that's larger than an `unsigned long long` can contain. To handle this, whenever the value of the current bit extracted from the `double` threatens to overflow, the accumulator is divided by ten to shift it rightwards and allow more room. The total number of shifts is recorded, and the appropriate number of extra zeroes are printed at the end of the number. Dividing the accumulator by ten loses precision, but the 64 bits of an `unsigned long long` exceeds the `53` bits of precision in a `double`, so the lost precision should not actually result in incorrect output. At the least, while the output may not precisely match the integer value stored in the `double`, it will be closer to that value than to any other representable `double` value, which I'm calling close enough.

In order to know when the accumulator threatens to overflow, the code needs to know the largest power of ten that can be represented in an `unsigned long long`. This method computes it by just computing successive powers of ten until it gets close to `ULLONG_MAX`:

```
    - (unsigned long long)ullongMaxPowerOf10
    {
        unsigned long long result = 1;
        while(ULLONG_MAX / result >= 10)
            result *= 10;
        return result;
    }
```

The `writeDoubleIntPart:` method starts off by initializing a `total` variable to zero:

```
    - (void)writeDoubleIntPart: (double)intpart
    {
        unsigned long long total = 0;
```

This is the accumulator that will hold the total computed value so far. It also keeps track of the value of the current bit:

```
        unsigned long long currentBit = 1;
```

This is multiplied by two each time a bit is extracted from the `double`, and represents the value of that bit.

The maximum value that can be stored in `total` before overflow threatens is cached:

```
        unsigned long long maxValue = [self ullongMaxPowerOf10] / 10;
```

This is one digit less than the maximum representable power of ten, in order to make sure that it can never overflow the accumulator. There is a surplus of 11 bits of precision in the accumulator, so losing one digit doesn't hurt too much.

The number of times that `total` and `currentBit` have been shifted to the right is recorded so that the appropriate number of trailing zeroes can be output later:

```
        unsigned surplusZeroes = 0;
```

Setup is complete, now it's time to loop until `intpart` is exhausted:

```
        while(intpart)
        {
```

A bit is extracted from `intpart` by dividing it by two:

```
            intpart /= 2;
```

Because `intpart` contains an integer, dividing it by two produces a number with a fractional part that is either `.0` or `.5`. The `.5` case represents a one bit that needs to be added to `total`. The presence of `.5` is checked by using the `fmod` function, which computes the remainder when dividing by a number. Using `fmod` with `1.0` as the second argument just produces the fractional part of the number:

```
            if(fmod(intpart, 1.0))
            {
```

If the bit is set, then `currentBit` is added to `total`, and the `.5` is sliced off of `intpart` using the `trunc` function:

```
                total += currentBit;
                intpart = trunc(intpart);
            }
```

Next, `currentBit` is multiplied by two so that it holds the right value for the next bit to be extracted:

```
            currentBit *= 2;
```

If `currentBit` exceeds `maxValue`, then both `currentBit` and `total` get divided by ten, and `surplusZeroes` is incremented. Both are rounded when dividing by adding `5` to them first, to aid in preserving as much precision as possible:

```
            if(currentBit > maxValue)
            {
                total = (total + 5) / 10;
                currentBit = (currentBit + 5) / 10;
                surplusZeroes++;
            }
        }
```

Once `intpart` is exhausted, `total` contains an approximation of its original value, and `surplusZeroes` indicates how many times it got shifted over. First, it prints `total`:

```
        [self writeUnsignedLongLong: total];
```

Finally, it prints the appropriate number of trailing zeroes:

```
        for(unsigned i = 0; i < surplusZeroes; i++)
            [self write: '0'];
    }
```

**Fractional Part**  
The basic idea for printing the fractional part is similar to printing the integer part. The difference is that the accumulator can't directly represent the fractional value, because `unsigned long long` doesn't do fractions. Instead, it holds the fractional value, scaled up by some large power of ten. For example, `100` might represent `1.0`, in which case the value of the first bit in the fractional part of a `double` is `50`, the second bit is `25`, and so forth. The actual numbers used contain a lot more zeroes at the end.

The accumulator for the integer part can overflow, while the accumulator for the fractional part can _underflow_. If the `double` contains an extremely small value, the accumulator will end up containing zero, which is no good. A similar strategy is used to deal with this problem, but in the opposite direction: whenever the accumulator and current bit become too small, they are multiplied by ten, and an extra leading zero is output.

The method starts off with its accumulator initialized to zero:

```
    - (void)writeDoubleFracPart: (double)fracpart
    {
        unsigned long long total = 0;
```

The value of the current bit is started at the largest power of ten that will fit into an `unsigned long long`. This represents `1.0`, and will be divided by `2` right away to properly represent `0.5` for the first bit extracted from the `double`:

```
        unsigned long long currentBit = [self ullongMaxPowerOf10];
```

The threshold for when the numbers become too small is the maximum representable power of ten, divided by ten. When this value is reached, there's a conceptual leading zero, and it's time to shift everything over:

```
        unsigned long long shiftThreshold = [self ullongMaxPowerOf10] / 10;
```

Now it's time for the loop. Keep extracting bits from `fracpart` until there's nothing left:

```
        while(fracpart)
        {
```

`fracpart` is shifted to the left by one bit, while `currentBit` is simultaneously shifted to the right:

```
            currentBit /= 2;
            fracpart *= 2;
```

The integer part of the resulting number will be either `1` or `0`. If it's `1`, the corresponding bit is `1`, so add `currentBit` to `total`, and chop the `1` off `fracpart`:

```
            if(fracpart >= 1.0)
            {
                total += currentBit;
                fracpart -= 1.0;
            }
```

If both the accumulator and `currentBit` are below `shiftThreshold`, it's time to shift everything over, and write a leading zero. Note that the number of shifts doesn't need to be tracked like it did in the previous method, because the leading zeroes can be written out immediately:

```
            if(currentBit <= shiftThreshold && total <= shiftThreshold)
            {
                [self write: '0'];
                currentBit *= 10;
                total *= 10;
            }
        }
```

Once the loop exits, there's one more task to be done. `total` now contains an integer representation of the decimal representation of the fractional part that was passed into the method (whew!), but with potentially a large number of redundant trailing zeroes. For example, if `fracpart` contained `0.5`, then `total` now contains `5000000000000000000`, but those trailing zeroes shouldn't be printed in the output. They're removed by just dividing `total` by ten repeatedly to get rid of trailing zeroes:

```
        while(total != 0 && total % 10 == 0)
            total /= 10;
```

Once that's done, `total` is ready to print, so it's passed to `writeUnsignedLongLong:`

```
        [self writeUnsignedLongLong: total];
    }
```

That's the end of the adventure of printing a `double`.

**Conclusion**  
`stringWithFormat:` is an extremely useful method that is, at its heart, a straightforward function that takes variable arguments. There are a ton of subtleties in how to output all of the various data formats, such as the adventure in printing a `double` above. There are further complications in supporting all of the various options available in format strings, which the above code doesn't even address. However, it's ultimately a big loop that looks for `'%'` format specifiers, and uses `va_arg` to extract the arguments passed in by the caller. Although `stringWithFormat:` is considerably more complex, you now have a basic idea of how it's put together.

That's it for today. Come back next time for more bitwise adventures. Friday Q&A is driven by reader suggesions, so until the next time, please keep [sending in your ideas for topics](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-05-17-lets-build-stringwithformat.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
