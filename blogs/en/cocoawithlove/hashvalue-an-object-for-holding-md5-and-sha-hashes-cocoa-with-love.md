---
title: 'HashValue: an object for holding MD5 and SHA hashes | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/07/hashvalue-object-for-holding-md5-and.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:262e6ce53038d951'
translated: false
---

> 原文：[HashValue: an object for holding MD5 and SHA hashes | Cocoa with Love](https://www.cocoawithlove.com/2009/07/hashvalue-object-for-holding-md5-and.html)　·　Cocoa with Love (Matt Gallagher)

Hash values are small, convenient values that you can generate from larger blocks of data for easy indexing, sorting and tracking. The traditional approach for generating MD5 and SHA hashes on Unix platforms to is to use command-line programs like openssl and md5. Apple provide easier approaches in the CommonCrypto library: here's how to use it, along with an NSValue subclass to wrap the result for interoperability with other Cocoa classes.

## Introduction to hashes

A hash value is a small, convenient number used to track or sort an arbitrary block of data.

A real-world example of a hash value is the initial letter in a word. You can use the initial letter of a word to lookup that word in a dictionary. If two words have different starting letters, they cannot be equal but if two words have the same starting letter, that doesn't guarantee they are the same.

For fast searching, you can immediately see the problem with only using an initial letter: if all you had to look up a word was its initial letter, you'd still have thousands of words to go through that all start with the same letter. You could use the first four letters but some combinations will be rare (like "aard") but others will contain hundreds of matches (like "stra").

In computing, we rarely ever use the first values in a block of data to track that block of data. Starting values of blocks of data are too often the same or similar — especially in the common case where we are sorting data that already has traits in common.

Instead, we use hash functions that use relatively complex mathematics to generate values from the source data that are well spread, even for source data that is nearly identical. Fortunately, you don't need to know the underlying mathematics, all you need to know is that a hash value can be used to:

- check if two blocks of data are the same
- sort data into hash tables
- checksum data (make certain your data hasn't changed)

Though these are the main purposes for which you should use hashes, MD5 and SHA hashes were actually developed for cryptography, not basic data handling. Nevertheless, for encryption and password handling in your own applications, I recommend using the Keychain (Security.framework) rather than manually using cryptographic hashes.

## Generating an MD5

MD5 is one of the most common hash functions. While it is no longer considered safe for security, its use as a checksum is very common.

The traditional Unix approach is to use the md5 program on the command-line:

```objc
matt$ md5 -s "Some data value."
MD5 ("Some data value.") = db7116c8634ad7fe3bd90bee94274ee0
```

The 32 character hexadecimal string is a human readable representation of the 16 byte output of the MD5 function.

On the Mac and iPhone, we can generate this value as follows:

```objc
#import &lt;CommonCrypto/CommonDigest.h&gt;

char input[] = "Some data value.";
char result[16];
CC_MD5(input, strlen(input), result);
```

However, we frequently want the human-readable hexadecimal string. The following will produce an identical ouput to the previous command-line invocation:

```objc
printf("MD5 (\"%s\") = %02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x\n",
    input,
    result[0], result[1], result[2], result[3], 
    result[4], result[5], result[6], result[7],
    result[8], result[9], result[10], result[11],
    result[12], result[13], result[14], result[15]);
```

Producing other kinds of hash works in the same way. e.g. For SHA256, use `CC_SHA256` instead of `CC_MD5` and increase the size of the result to 32 from 16.

## The HashValue class

Since hash values are frequently used to track blocks of data in a program, it would be nice to have an Objective-C class that wraps the hash values so we can use them in `NSDictionary` objects as keys for our data.

If we consider a hash value simply as a small C struct, i.e:

```objc
typedef struct
{
    char value[CC_MD5_DIGEST_LENGTH];
} HashValueMD5Hash;

typedef struct
{
    char value[CC_SHA256_DIGEST_LENGTH];
} HashValueShaHash;
```

then the easiest way to make it a fully fledged Objective-C object is to create an `NSValue` from it:

```objc
char input[] = "Some data value.";
HashValueMD5Hash result;
CC_MD5(input, strlen(input), &result);

NSValue *myHashValue = [NSValue valueWithBytes:&result objCType:@encode(HashValueMD5Hash)];
```

That's an okay solution but if you're generating a lot of hashes in your program, it would be good to have a class that:

- has an optimized construction method that can generate the hash directly from `NSData`
- abstracts away the C struct so you can deal exclusively with the Objective-C objects
- method to easily generate human-readable strings

So I wrote the `HashValue` class.

```objc
@interface HashValue : NSObject &lt;NSCoding, NSCopying&gt;
{
    unsigned char value[HASH_VALUE_STORAGE_SIZE];
    HashValueType type;
}

- (id)initMD5HashWithBytes:(const void *)bytes length:(NSUInteger)length;
+ (HashValue *)md5HashWithData:(NSData *)data;
- (id)initSha256HashWithBytes:(const void *)bytes length:(NSUInteger)length;
+ (HashValue *)sha256HashWithData:(NSData *)data;

- (const void *)value;
- (HashValueType)type;

@end
```

Despite being a class that wraps a value, there's no explicit reason to make it a subclass of `NSValue`. Since subclassing `NSValue` has inherent difficulties (you need to carefully override a lot of inherited methods) I've made the class a basic subclass of `NSObject`.

The `init` method implementations are fairly simple:

```objc
- (id)initMD5HashWithBytes:(const void *)bytes length:(NSUInteger)length
{
    self = [super init];
    if (self != nil)
    {
        CC_MD5(bytes, length, value);
        type = HASH_VALUE_MD5_TYPE;
    }
    return self;
}
```

The `description` method is overridden to provide the human-readable hexadecimal string:

```objc
- (NSString *)description
{
    NSInteger byteLength;
    if (type == HASH_VALUE_MD5_TYPE)
    {
        byteLength = sizeof(HashValueMD5Hash);
    }
    else if (type == HASH_VALUE_SHA_TYPE)
    {
        byteLength = sizeof(HashValueShaHash);
    }

    NSMutableString *stringValue =
        [NSMutableString stringWithCapacity:byteLength * 2];
    NSInteger i;
    for (i = 0; i < byteLength; i++)
    {
        [stringValue appendFormat:@"%02x", value[i]];
    }
    
    return stringValue;
}
```

Most of the other methods in the class are basic accessors or `NSCopying`, `NSCoding` and `NSObject` methods. The copying methods in particular are essential so that the object can be used as a key in an `NSDictionary`.

I will highlight one other method:

```objc
- (NSUInteger)hash
{
    return *((NSUInteger *)value);
}
```

You may wonder why it's necessary to have a hash method on a class that is itself a hash value. Hash methods in Cocoa are used for the same indexing and sorting tasks I identified above: sorting and finding objects in `NSSet` and `NSDictionary`. In Cocoa the default `hash` method calculates its hash value from the memory address of the object. Because we have overridden `isEqual:` to compare the object's internal `value`, we also need to override the `hash` method to also reflect this change. This is a basic requirement of hashes — equal objects must return the same hash value (imagine the confusion if two identically spelled words were sorted to different locations in a dictionary).

It may seem a little odd to simply return the first few bytes of the `value` as our new hash (after I explained that the first few bytes is rarely the best hash) but this case is an exception to the rule: our data is already "well-spread" and every bit in our hash is as well-spread as the next.

## Conclusion

> HashValue class as a .zip file
> 
> (2kB)

Hash values are used everywhere. Git uses SHA1 to track file changes in its repository, BitTorrent uses MD5s to identify torrents and many download programs use hashes to checksum downloaded data.

The CommonCrypto library (part of Foundation on the Mac and iPhone through libSystem) makes generating common hash functions very simple.

As with all data manipulation, I think a nice Cocoa class around the data makes it easier to use. I have only added MD5 and SHA256 to this particular implementation but it should be very simple to add other CommonCrypto hashes to the class should you require them.
