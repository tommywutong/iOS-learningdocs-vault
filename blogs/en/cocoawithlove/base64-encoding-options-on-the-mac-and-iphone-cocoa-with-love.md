---
title: 'Base64 encoding options on the Mac and iPhone | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/06/base64-encoding-options-on-mac-and.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:0c5891af42939beb'
translated: false
---

> 原文：[Base64 encoding options on the Mac and iPhone | Cocoa with Love](https://www.cocoawithlove.com/2009/06/base64-encoding-options-on-mac-and.html)　·　Cocoa with Love (Matt Gallagher)

On Unix platforms, a common approach for Base64 encoding is to use libcrypto (the OpenSSL library). However, like most C libraries, you need to wrap it to integrate with Objective-C data types (like NSData and NSString) and it isn't available on the iPhone. I'll show you how to handle base64 encoding/decoding with OpenSSL and without so you can handle the Mac and iPhone equally.

## Introduction

[Base64](http://en.wikipedia.org/wiki/Base64) is an encoding for transferring binary data in 7-bit text. Originally used in [email](http://en.wikipedia.org/wiki/MIME#Content-Transfer-Encoding), it is also used for binary encoding data in HTML files. Another common use for Base64 is in [HTTP Basic Access Authentication](http://en.wikipedia.org/wiki/Basic_access_authentication) where it is used to transfer login details (which might not be printable characters).

The key library for handling Base64 on the Mac is normally libcrypto (the OpenSSL library), so it's a little disappointing that libcrypto isn't available on the iPhone.

## Using OpenSSL

### Via the command line

On the Mac, you can handle simple encoding tasks like base64 encoding with OpenSSL on the command line:

```objc
echo "Base64 encode this text." | openssl enc -base64
```

gives the encoding result:

```objc
QmFzZTY0IGVuY29kZSB0aGlzIHRleHQuCg==
```

The reverse is handled in the following manner:

```objc
echo "QmFzZTY0IGVuY29kZSB0aGlzIHRleHQuCg==" | openssl enc -d -base64
```

giving

```objc
Base64 encode this text.
```

### In code

As you'd expect, doing the same work in code takes a little more typing. First, we're using a library, so we need to include it (in your Project's Build Settings under Other Linker Flags add the flag `-lcrypto`). Once that's done, you should be able to use the following method in a category on `NSData`:

```objc
#include &lt;openssl/bio.h&gt;
#include &lt;openssl/evp.h&gt;

- (NSString *)base64EncodedString
{
    // Construct an OpenSSL context
    BIO *context = BIO_new(BIO_s_mem());

    // Tell the context to encode base64
    BIO *command = BIO_new(BIO_f_base64());
    context = BIO_push(command, context);

    // Encode all the data
    BIO_write(context, [self bytes], [self length]);
    BIO_flush(context);

    // Get the data out of the context
    char *outputBuffer;
    long outputLength = BIO_get_mem_data(context, &outputBuffer);
    NSString *encodedString = [NSString
        stringWithCString:outputBuffer
        length:outputLength];

    BIO_free_all(context);

    return encodedString;
}
```

To handle a Base64 encode.

By default, `encodedString` will have newlines every 64 characters. If needed, you can disable the inclusion of newlines by adding the following line before the `BIO_write`:

```objc
BIO_set_flags(context, BIO_FLAGS_BASE64_NO_NL);
```

Tthe "BIO" system (I think it stands for buffered I/O) is not very symmetric so the code for decoding is quite different:

```objc
+ (NSData *)dataByBase64DecodingString:(NSString *)decode
{
    decode = [decode stringByAppendingString:@"\n"];
    NSData *data = [decode dataUsingEncoding:NSASCIIStringEncoding];
    
    // Construct an OpenSSL context
    BIO *command = BIO_new(BIO_f_base64());
    BIO *context = BIO_new_mem_buf((void *)[data bytes], [data length]);
        
    // Tell the context to encode base64
    context = BIO_push(command, context);

    // Encode all the data
    NSMutableData *outputData = [NSMutableData data];
    
    #define BUFFSIZE 256
    int len;
    char inbuf[BUFFSIZE];
    while ((len = BIO_read(context, inbuf, BUFFSIZE)) > 0)
    {
        [outputData appendBytes:inbuf length:len];
    }

    BIO_free_all(context);
    [data self]; // extend GC lifetime of data to here

    return outputData;
}
```

An interesting point to note at the top of this function: I add an extra newline to the start of the string. This is because if you have not disabled newlines and the string does not contain at least 1 newline, `BIO_read` will fail.

## Handling Base64 on the iPhone

Using libcrypto isn't possible by default on the iPhone — the library isn't there. You could probably build libcrypto.a and link it statically against your app but that can be difficult to set up and would require that you notify Apple that your app contains encryption.

Normally, it is better to avoid libcrypto on the iPhone. The other functions that libcrypto handles can be found elsewhere:

- md5 — use the CommonCrypto implementation `CC_MD5`
- sha — use the CommonCrypto implementation `CC_SHA`
- /

  functions in the Security framework

You can find the documentation for the Security Framework by performing a standard Xcode API lookup. For some reason though, the CommonCrypto functions only appear in a full-text search.

The Base64 functionality of OpenSSL doesn't have an accessible equivalent on the iPhone, even though `NSURLConnection`, `CFHTTPMessageRef` and WebKit must all have access to an implementation — whatever they use is not accessible.

### Encoding Base64

Fortunately, Base64 is a fairly simple encoding. At its heart, it looks like this:

```objc
static unsigned char base64EncodeLookup[65] =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

//
// Inner loop: turn 3 bytes into 4 base64 characters
//
outputBuffer[j++] = base64EncodeLookup[(inputBuffer[i] & 0xFC) &gt;&gt; 2];
outputBuffer[j++] = base64EncodeLookup[((inputBuffer[i] & 0x03) &lt;&lt; 4)
    | ((inputBuffer[i + 1] & 0xF0) &gt;&gt; 4)];
outputBuffer[j++] = base64EncodeLookup[((inputBuffer[i + 1] & 0x0F) &lt;&lt; 2)
    | ((inputBuffer[i + 2] & 0xC0) &gt;&gt; 6)];
outputBuffer[j++] = base64EncodeLookup[inputBuffer[i + 2] & 0x3F];
```

This might be a little ugly to look at if you're not use to seeing bitmasks and bitshifts but it is only a couple lines. It does little more than the comment states: it turns 3 bytes into 4 chars, with the specific chars specified by the `base64EncodeLookup` mapping.

Of course, while this code handles the center of the main loop, there's almost a hundred lines total in the complete implementation that I wrote.

As part of keeping the function optimal, I wanted to keep the conditionals out of the inner loop (making vectorizing easier). I succeeded and there are no conditionals in the inner loop but this means that there are a few tail conditions to handle in the epilogue.

I also wanted to calculate the exact size that would be required for the output buffer, so it can be allocated once with no waste, but this too occupies a few lines worth of space.

### Decoding Base64

Decoding works similarly to encoding, except that in decoding we are reducing 4 characters down to 3 bytes instead of vice versa:

```objc
//
// Store the 6 bits from each of the 4 characters as 3 bytes
//
outputBuffer[j] = (accumulated[0] &lt;&lt; 2) | (accumulated[1] &gt;&gt; 4);
outputBuffer[j + 1] = (accumulated[1] &lt;&lt; 4) | (accumulated[2] &gt;&gt; 2);
outputBuffer[j + 2] = (accumulated[2] &lt;&lt; 6) | accumulated[3];
```

More interesting than the code in this case is the lookup table that each of these accumulated bytes passes through before being used here:

```objc
//
// Definition for "masked-out" areas of the base64DecodeLookup mapping
//
#define xx 65

//
// Mapping from ASCII character to 6 bit pattern.
//
static unsigned char base64DecodeLookup[256] =
{
    xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, 
    xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, 
    xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, 62, xx, xx, xx, 63, 
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, xx, xx, xx, xx, xx, xx, 
    xx,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, xx, xx, xx, xx, xx, 
    xx, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, xx, xx, xx, xx, xx, 
    xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, 
    xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, 
    xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, 
    xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, 
    xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, 
    xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, 
    xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, 
    xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, xx, 
};
```

The "`xx`"s in this table are just a `#define` of 65 (i.e. outside the valid range of Base64) but they provide an interesting visual representation of the 6-bits that each Base64 character can occupy within the 8-bit byte.

I was unable to remove all of the conditionals from the inner loop of the decode side and keep the "skip over invalid characters" requirement.

This "skip over invalid characters" stage (where characters are accumulated until 4 valid characters are found) is handled by the following loop (which immediately preceeds the previous "store the 6 bits from each of the 4 characters as 3 bytes" code):

```objc
//
// Accumulate 4 valid characters (ignore everything else)
//
unsigned char accumulated[BASE64_UNIT_SIZE];
size_t accumulateIndex = 0;
while (i < length)
{
    unsigned char decode = base64DecodeLookup[inputBuffer[i++]];
    if (decode != xx)
    {
        accumulated[accumulateIndex] = decode;
        accumulateIndex++;
        
        if (accumulateIndex == BASE64_UNIT_SIZE)
        {
            break;
        }
    }
}
```

This is the only part which makes the decode stage sub-optimal. If you had Base64 input data with no newlines and no other characters requiring skipping, I think you could remove this section entirely so that the inner loop of the decode function could be vectorizable.

## Conclusion

> NSData+Base64 class and header
> 
> (4kB).

In this post, I've shown you how to use the default command-line and library options for Base64 handling on Mac OS X. I've also shown you the approach I use for Base64 encoding and decoding on the iPhone.

The libcrypto libraries (when available) are not as tight and simple as custom code for the task but do have the advantage that the pipeline for feeding data into them is more configurable.

I'm certainly not the only one to present C libraries for Base64 encoding that will work on the iPhone but the approach I've used should be efficient (especially the internal implementations in the C-functions) and it should drop into a Cocoa project on the iPhone very easily.
