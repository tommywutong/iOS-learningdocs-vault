---
title: NSCoding / NSKeyedArchiver
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/nscoding/'
original_language: en
published: 2013-05-13
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:7a24284cedc19a4a'
translated: false
---

> 原文：[NSCoding / NSKeyedArchiver](https://nshipster.com/nscoding/)　·　NSHipster (Mattt)

# [NSCoding / NSKeyed​Archiver](https://nshipster.com/nscoding/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  May 13^th, 2013

Among the most important architectural decisions made when building an app is how to persist data between launches. The question of how, exactly, to re-create the state of the app from the time it was last opened; of how to describe the object graph in such a way that it can be flawlessly reconstructed next time.

On iOS and OS X, Apple provides two options: [Core Data](https://developer.apple.com/library/mac/#documentation/cocoa/Conceptual/CoreData/cdProgrammingGuide.html) or [`NSKeyedArchiver`](https://developer.apple.com/library/ios/#Documentation/Cocoa/Reference/Foundation/Classes/NSKeyedArchiver_Class/Reference/Reference.html) / [`NSKeyedUnarchiver`](https://developer.apple.com/library/ios/#documentation/Cocoa/Reference/Foundation/Classes/NSKeyedUnarchiver_Class/Reference/Reference.html) (which serializes `<NSCoding>`-compliant classes to and from a data representation).

> Or rather: three, if you include `NSURLCache`. In the case of a client-server application, having the client load necessary data on each launch is a viable design, especially when combined with a disk-based cache, which allows stored server responses to be returned immediately from matching requests. In practice, some combination of network and object caching is advisable.

When it comes to modeling, querying, traversing and persisting complex object graphs, there is no substitute for Core Data. Core Data is a big hammer, but not every problem is a nail—much less a sufficiently large nail.

A fair and common comparison of Core Data to `NSKeyedArchiver` might go something like this:

|  | Core Data | NSKeyedArchiver |
|---|---|---|
| Entity Modeling | Yes | No |
| Querying | Yes | No |
| Speed | Fast | Slow |
| Serialization Format | SQLite, XML, or NSData | NSData |
| Migrations | Automatic | Manual |
| Undo Manager | Automatic | Manual |

Et cetera. In a heads-up, apples to apples comparison, it looks rather one-sided.

…that is, until you look at it from a slightly different perspective:

|  | Core Data | NSKeyedArchiver |
|---|---|---|
| Persists State | Yes | Yes |
| Pain in the Ass | Yes | No |

By these measures, `NSKeyedArchiver` becomes a perfectly reasonable choice in certain situations. Not all apps need to query data. Not all apps need automatic migrations. Not all apps work with large or complex object graphs. And even apps that do may have certain components better served by a simpler solution.

This article will look at the how’s, when’s, and why’s of `NSKeyedArchiver` and `NSCoding`. And with this understanding, hopefully provide you, dear reader, with the wisdom to choose the best tool for the job.

---

`NSCoding` is a simple protocol, with two methods: `-initWithCoder:` and `encodeWithCoder:`. Classes that conform to `NSCoding` can be serialized and deserialized into data that can be either be archived to disk or distributed across a network.

For example:

```
class Book: NSObject, NSCoding {
    var title: String
    var author: String
    var pageCount: Int
    var categories: [String]
    var available: Bool

    // Memberwise initializer
    init(title: String, author: String, pageCount: Int, categories: [String], available: Bool) {
        self.title = title
        self.author = author
        self.pageCount = pageCount
        self.categories = categories
        self.available = available
    }

    // MARK: NSCoding
    
    required convenience init?(coder decoder: NSCoder) {
        guard let title = decoder.decodeObjectForKey("title") as? String,
            let author = decoder.decodeObjectForKey("author") as? String,
            let categories = decoder.decodeObjectForKey("categories") as? [String]
            else { return nil }
        
        self.init(
            title: title,
            author: author,
            pageCount: decoder.decodeIntegerForKey("pageCount"),
            categories: categories,
            available: decoder.decodeBoolForKey("available")
        )
    }
    
    func encodeWithCoder(coder: NSCoder) {
        coder.encodeObject(self.title, forKey: "title")
        coder.encodeObject(self.author, forKey: "author")
        coder.encodeInt(Int32(self.pageCount), forKey: "pageCount")
        coder.encodeObject(self.categories, forKey: "categories")
        coder.encodeBool(self.available, forKey: "available")
    }
}
```

```
@interface Book : NSObject <NSCoding>
@property NSString *title;
@property NSString *author;
@property NSUInteger pageCount;
@property NSSet *categories;
@property (getter = isAvailable) BOOL available;
@end

@implementation Book

#pragma mark - NSCoding

- (id)initWithCoder:(NSCoder *)decoder {
    self = [super init];
    if (!self) {
        return nil;
    }

    self.title = [decoder decodeObjectForKey:@"title"];
    self.author = [decoder decodeObjectForKey:@"author"];
    self.pageCount = [decoder decodeIntegerForKey:@"pageCount"];
    self.categories = [decoder decodeObjectForKey:@"categories"];
    self.available = [decoder decodeBoolForKey:@"available"];

    return self;
}

- (void)encodeWithCoder:(NSCoder *)encoder {
    [encoder encodeObject:self.title forKey:@"title"];
    [encoder encodeObject:self.author forKey:@"author"];
    [encoder encodeInteger:self.pageCount forKey:@"pageCount"];
    [encoder encodeObject:self.categories forKey:@"categories"];
    [encoder encodeBool:[self isAvailable] forKey:@"available"];
}

@end
```

As you can see, `NSCoding` is mostly boilerplate. Each property is encoded or decoded as an object or type, using the name of the property of as the key each time. (Some developers prefer to define `NSString *` constants for each keypath, but this is usually unnecessary).

But boilerplate can be a good thing sometimes—with direct control over the entire serialization process, it remains flexible to account for things like:

- **Migrations**: If a data model changes—such as adding, renaming, or removing a field—it should maintain compatibility with data serialized in the old format. Apple provides some guidelines on how to go about this in [“Forward and Backward Compatibility for Keyed Archives”](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/Archiving/Articles/compatibility.html#//apple_ref/doc/uid/20001055-BCICFFGE).
- **Archiving non-`NSCoding`-compatible Classes**: According to object-oriented design, objects should take responsibility for encoding and decoding to and from a serialization format. However, when a class doesn’t come with `NSCoding` support built in, it may be left up to class that uses it to help out.

> One library that aims to cut down the boilerplate of NSCoding is [Mantle](https://github.com/github/Mantle), from the good folks over at GitHub. If you’re looking for more of the conveniences of Core Data modeling with `NSCoding`, Mantle is definitely worth a look.

---

Of course, serialization is only one part of the story. Determining where this data will persist is another question. Again, there are two approaches: writing to the local file system and using `NSUserDefaults`.

## File System

`NSKeyedArchiver` and `NSKeyedUnarchiver` provide a convenient API to read / write objects directly to / from disk.

An `NSCoding`-backed table view controller might, for instance, set its collection property from the file manager

#### Archiving

```
NSKeyedArchiver.archiveRootObject(books, toFile: "/path/to/archive")
```

```
[NSKeyedArchiver archiveRootObject:books toFile:@"/path/to/archive"];
```

#### Unarchiving

```
guard let books = NSKeyedUnarchiver.unarchiveObjectWithFile("/path/to/archive") as? [Book] else { return nil }
```

```
[NSKeyedUnarchiver unarchiveObjectWithFile:@"/path/to/archive"];
```

## `NSUserDefaults`

Each app has its own database of user preferences, which can store and retrieve any `NSCoding`-compatible object or C value.

While it is not advisable to store an entire object graph into `NSUserDefaults`, it can be useful to encode compound objects in this way, such as “current user” objects ~~or API credentials~~ (use [Keychain](https://developer.apple.com/library/mac/#documentation/security/Conceptual/keychainServConcepts/iPhoneTasks/iPhoneTasks.html) instead).

#### Archiving

```
let data = NSKeyedArchiver.archivedDataWithRootObject(books)
NSUserDefaults.standardUserDefaults().setObject(data, forKey: "books")
```

```
NSData *data = [NSKeyedArchiver archivedDataWithRootObject:books];
[[NSUserDefaults standardUserDefaults] setObject:data forKey:@"books"];
```

#### Unarchiving

```
if let data = NSUserDefaults.standardUserDefaults().objectForKey("books") as? NSData {
    let books = NSKeyedUnarchiver.unarchiveObjectWithData(data)
}
```

```
NSData *data = [[NSUserDefaults standardUserDefaults] objectForKey:@"books"];
NSArray *books = [NSKeyedUnarchiver unarchiveObjectWithData:data];
```

---

As developers, it is our responsibility to understand the goals and needs of our applications, and to resist the urge to over-engineer and prematurely optimize our solutions.

The decision to use Core Data in an application may appear to be a no-brainer, if not harmless. But in many cases, Core Data is discovered to be so unwieldy or unnecessary as to become a real hindrance to making something useful, let alone functional.

And even if most applications _would_ benefit from Core Data at some point, there is wisdom to letting complexity evolve from a simple as necessary. And as far as persistence goes, it doesn’t get much simpler than `NSCoding`.
